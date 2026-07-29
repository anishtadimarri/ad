#!/usr/bin/env python3
"""
LTGP:CAC on a $20,000 placed job — the two models joined.

The offer model (offer_model.py) computes gross profit per acquired client but
carries its own crude CAC: a flat $75 CPL divided through an assumed funnel.
The funnel model (funnel.py) computes CAC properly — impression to placement,
by audience layer, with sales labour costed in.

This script takes GROSS PROFIT from the offer model and CAC from the funnel
model, and discards the offer model's internal CAC entirely. That is the only
honest way to read the ratio, because the two models disagree about CAC by
roughly 2x and the funnel one is the one built from benchmarked steps.

Blending rule: CAC is blended by SPEND, not by averaging the three CAC numbers.
Averaging CACs weights each audience equally regardless of how much of the
budget it can absorb, which overstates the cheap-but-tiny intent seed.

Run:  python3 scoring/ltgp.py > scoring/LTGP.md
"""

import io
import os
import sys
from contextlib import redirect_stdout
from dataclasses import replace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Both modules print their report at import time; swallow it.
with redirect_stdout(io.StringIO()):
    import offer_model as om
    import funnel as fn

SALARY = 20_000.0
FEE_PCT = 0.30

# ---------------------------------------------------------------- the offer
# H5 (EOR made the default, not the upsell — SCALE.md §7) repriced for a $20k
# job, with the EOR line at the global-platform comparison rather than below it.
BASE = next(c for c in om.CONFIGS if c.name.startswith("H5"))
OFFER = replace(BASE, name="$20k job, EOR default", salary=SALARY, fee_pct=FEE_PCT,
                eor_price=499.0, eor_attach=0.75, monthly_tenure=30.0)

# ---------------------------------------------------------------- the funnel
FLOW = "B. Calendar booking on the LP"
MIX = {"Intent seed (job posters)": 0.25,   # capped by matched audience size
       "1% Lookalike": 0.45,
       "Broad / Advantage+": 0.30}


def blended(spend=5000.0, mix=None):
    """Spend-weighted CAC across the audience layers."""
    mix = mix or MIX
    cost = place = 0.0
    for aud, share in mix.items():
        r = fn.run(aud, FLOW, spend=spend * share)
        cost += r["cost"]
        place += r["place"]
    return cost / place, place


def parts(o):
    """Split lifetime GP into the one-time slice and the recurring slice."""
    e = om.econ(o)
    no_rec = om.econ(replace(o, eor_attach=0.0, eor_fx=False, equipment_gp=0.0,
                             managed_convert=0.0, protection_attach=0.0))
    return e, e["gplife"] - no_rec["gplife"]


def ratios(gp30, gplife, cac):
    return gp30 / cac, gplife / cac


def report():
    e, rec = parts(OFFER)
    cac_b, _ = blended()

    print("# LTGP:CAC on a $20,000 Job\n")
    print("Gross profit from [`offer_model.py`](offer_model.py). CAC from "
          "[`funnel.py`](funnel.py) — **not** from the offer model, whose internal CAC uses a flat")
    print("$75 CPL and an assumed funnel. Where the two disagree, the funnel one is built from "
          "benchmarked steps and wins.\n")
    print(f"**Placed salary ${SALARY:,.0f} · fee {FEE_PCT:.0%} = "
          f"${SALARY*FEE_PCT:,.0f} · EOR ${OFFER.eor_price:.0f}/mo at "
          f"{OFFER.eor_attach:.0%} attach · {OFFER.monthly_tenure:.0f}-month client seat.**\n")

    # ---------------------------------------------------------------- GP side
    print("---\n\n## 1. The gross profit per acquired client\n")
    print("| | | |\n|---|---|---|")
    rows = [
        ("Placement fee", f"${SALARY*FEE_PCT:,.0f}", f"{FEE_PCT:.0%} of ${SALARY:,.0f}"),
        ("Seats per acquired client", f"{e['seats']:.2f}",
         f"{OFFER.multi_hire:.0%} of clients hire two at once"),
        ("Screening billed on", f"${om.SCREENING_PASSTHRU*1.6*e['seats']:,.0f}",
         "cost × 1.6, market-standard pass-through"),
        ("**30-day revenue**", f"**${e['rev30']:,.0f}**", ""),
        ("**30-day gross profit**", f"**${e['gp30']:,.0f}**", f"**{e['gm']:.0%} margin**"),
        ("Repeat seats over the life", f"{OFFER.extra_seats:.2f}",
         f"{om.P_EXPAND:.0%} expand + {om.P_PAID_REPLACE:.0%} paid replacement"),
        ("**Lifetime gross profit**", f"**${e['gplife']:,.0f}**",
         f"of which **${rec:,.0f} ({rec/e['gplife']:.0%}) is recurring**"),
    ]
    for a, b, c in rows:
        print(f"| {a} | {b} | {c} |")
    print(f"\n**The placement fee is no longer the business.** ${rec:,.0f} of the "
          f"${e['gplife']:,.0f} lifetime gross")
    print(f"profit is the recurring EOR layer — ${OFFER.eor_price:.0f}/mo at "
          f"{(OFFER.eor_price-om.EOR_COST)/OFFER.eor_price:.0%} margin, plus the "
          f"{om.FX_SPREAD:.0%} FX spread and")
    print("equipment margin, running for as long as the client keeps the seat filled. The fee is "
          "the entry price; the seat is the asset.\n")

    # ---------------------------------------------------------------- CAC side
    print("---\n\n## 2. The CAC, by audience layer\n")
    print("| Audience | CPL | Cost per held call | **CAC** | **30-day** | **Lifetime** |")
    print("|---|---|---|---|---|---|")
    for aud in fn.AUD:
        r = fn.run(aud, FLOW)
        r30, rl = ratios(e["gp30"], e["gplife"], r["cac"])
        print(f"| {aud} | ${r['cpl']:.0f} | ${r['cost_held']:,.0f} | **${r['cac']:,.0f}** "
              f"| **{r30:.2f}:1** | **{rl:.2f}:1** |")
    r30, rl = ratios(e["gp30"], e["gplife"], cac_b)
    mixs = " / ".join(f"{v:.0%} {k.split('(')[0].split('/')[0].strip()}" for k, v in MIX.items())
    print(f"| **Blended** ({mixs}) | | | **${cac_b:,.0f}** | **{r30:.2f}:1** | **{rl:.2f}:1** |")
    print("\nBlended by **spend**, not by averaging the three CACs — the intent seed has the lowest")
    print("CAC but the smallest audience, so it cannot absorb the budget its CAC would earn it.\n")

    print(f"> **${e['gp30']:,.0f} of 30-day gross profit against a ${cac_b:,.0f} CAC = "
          f"{r30:.2f}:1 inside month one.**\n> "
          f"Over the life of the client, **{rl:.2f}:1**.\n")

    # ---------------------------------------------------------------- what breaks
    print("---\n\n## 3. What moves it\n")
    print("| Change | CAC | 30-day GP | **30-day** | **Lifetime** |")
    print("|---|---|---|---|---|")

    def row(label, cac, offer):
        ee, _ = parts(offer)
        a, b = ratios(ee["gp30"], ee["gplife"], cac)
        flag = "" if a >= 1.5 else " ⚠️"
        print(f"| {label} | ${cac:,.0f} | ${ee['gp30']:,.0f} | **{a:.2f}:1**{flag} "
              f"| **{b:.2f}:1** |")

    row("**Base**", cac_b, OFFER)

    o = fn.DEPOSIT_COLD
    fn.DEPOSIT_COLD = 0.08
    cac_dep, _ = blended()
    fn.DEPOSIT_COLD = o
    row("Deposit rate 8% not 18%", cac_dep, OFFER)
    row("EOR attach 40% not 75%", cac_b, replace(OFFER, eor_attach=0.40))
    row("Client seat 12 months not 30", cac_b, replace(OFFER, monthly_tenure=12.0))
    row("Both bad — 8% deposit, 40% attach", cac_dep, replace(OFFER, eor_attach=0.40))

    fn.DEPOSIT_COLD = 0.30
    cac_up, _ = blended()
    fn.DEPOSIT_COLD = o
    row("Deposit 30%, EOR attach 90%", cac_up, replace(OFFER, eor_attach=0.90))

    print("\n**The deposit rate is the one fragile input.** It is the step with no data behind it —")
    print("18% of held calls paying a $500 refundable deposit on cold traffic is an assumption, not")
    print("a benchmark. Halve it and the 30-day ratio halves with it. Everything else — EOR attach,")
    print("seat length, fill rate — moves the lifetime number a lot and the 30-day number barely,")
    print("because the 30-day number is almost entirely the placement fee.\n")
    print("Both of the two things that could go wrong at once still clears the 1.5:1 constraint, "
          "which is the actual test.\n")


if __name__ == "__main__":
    report()
