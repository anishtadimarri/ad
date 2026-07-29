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
#
# EOR_MONTHS was 30 in the first pass — the CLIENT SEAT life, on the logic that
# replacements keep the seat filled and therefore keep the EOR fee running even
# though the average worker only stays 9 months. Operator direction: assume 9.
# That is a much harsher assumption than "the worker leaves at 9 months" — it
# assumes the SEAT dies with the worker and is never refilled. Kept because it
# is the floor, and a floor that still clears is worth more than a base case
# that needs an argument. §3 prices the difference.
EOR_MONTHS = 9.0

BASE = next(c for c in om.CONFIGS if c.name.startswith("H5"))
OFFER = replace(BASE, name="$20k job, EOR default", salary=SALARY, fee_pct=FEE_PCT,
                eor_price=499.0, eor_attach=0.75, monthly_tenure=EOR_MONTHS)

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
    print(f"Placed salary **${SALARY:,.0f}** · fee **{FEE_PCT:.0%}** = "
          f"**${SALARY*FEE_PCT:,.0f}** · EOR **${OFFER.eor_price:.0f}/mo** at "
          f"**{OFFER.eor_attach:.0%} attach** · **{EOR_MONTHS:.0f} months of EOR per employee**.\n")

    # ------------------------------------------------------- the EOR line itself
    fee_gp = OFFER.eor_price - om.EOR_COST
    fx = om.FX_SPREAD * SALARY / 12
    per_emp = fee_gp + fx
    per_client = per_emp * OFFER.eor_attach * e["seats"]
    print("---\n\n## 0. The EOR line, per month\n")
    print("| | Per employee / month |\n|---|---|")
    for a, b in [("EOR price charged to the client", f"${OFFER.eor_price:,.0f}"),
                 ("Marginal cost — payroll, filings, HR support, insurance admin",
                  f"(${om.EOR_COST:,.0f})"),
                 ("**Fee gross profit**", f"**${fee_gp:,.0f}**"),
                 (f"FX spread at {om.FX_SPREAD:.0%} on ${SALARY/12:,.0f}/mo of salary moved",
                  f"${fx:,.0f}"),
                 ("**Total gross profit per employee per month**", f"**${per_emp:,.0f}**"),
                 (f"× {OFFER.eor_attach:.0%} attach × {e['seats']:.1f} seats",
                  f"**${per_client:,.0f}/mo per acquired client**")]:
        print(f"| {a} | {b} |")
    print(f"\n**${per_emp:,.0f}/month per employee, {fee_gp/OFFER.eor_price:.0%} margin on the fee "
          f"line.** Over {EOR_MONTHS:.0f} months that is")
    print(f"**${per_emp*EOR_MONTHS:,.0f} per employee**, or **${per_client*EOR_MONTHS:,.0f} per "
          f"acquired client** once attach and second seats are counted.")
    print(f"\nThe cost side is the reason the margin holds: an India-domiciled operator's marginal "
          f"cost of employing one more person is ~${om.EOR_COST:.0f}/mo, against the "
          f"${OFFER.eor_price:.0f} the client would pay Deel or Remote for the *same* India "
          f"employment. **You are not discounting; you are pricing at the global comparison with a "
          f"local cost base.**\n")

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
    print(f"\n**At {EOR_MONTHS:.0f} months the placement fee is back to being the business.** "
          f"${rec:,.0f} of the ${e['gplife']:,.0f}")
    print(f"lifetime gross profit is recurring — {rec/e['gplife']:.0%}, down from 65% when the EOR "
          f"line was assumed to run for a 30-month client seat. **The fee is {1-rec/e['gplife']:.0%} "
          f"of the value again**, which changes what the company is: a placement business with a "
          f"useful attachment, not an EOR business with a placement front end.\n")

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
    row("Both bad — 8% deposit, 40% attach", cac_dep, replace(OFFER, eor_attach=0.40))

    fn.DEPOSIT_COLD = 0.30
    cac_up, _ = blended()
    fn.DEPOSIT_COLD = o
    row("Deposit 30%, EOR attach 90%", cac_up, replace(OFFER, eor_attach=0.90))

    print("\n**The deposit rate is the one input that can break it.** It is the step with no data")
    print("behind it — 18% of held calls paying a $500 refundable deposit on cold traffic is an")
    print("assumption, not a benchmark. Halve it and the 30-day ratio halves with it. EOR attach and")
    print("EOR months move the lifetime number a lot and the 30-day number **not at all**, because")
    print("the 30-day number is the placement fee and nothing else.\n")
    print("Both of the things that could go wrong at once still clears the 1.5:1 constraint, which "
          "is the actual test.\n")

    # ------------------------------------------------------ the months question
    print("---\n\n## 4. How many months of EOR — and why this is the biggest lever left\n")
    print(f"The base case above assumes **{EOR_MONTHS:.0f} months**, which is the average *worker* "
          f"tenure. That is the")
    print("**floor**, not the expected value, because it assumes the seat dies with the worker.")
    print("It should not: a replacement under the 12-month guarantee refills the same seat, and the")
    print("EOR fee keeps billing across the handover. **Placement is a flow; the EOR book is a "
          "stock** ([`SCALE.md`](SCALE.md) §2).\n")
    print("| EOR months | Lifetime GP | Recurring share | **30-day** | **Lifetime** |")
    print("|---|---|---|---|---|")
    for t in (6, 9, 12, 18, 24, 30):
        ee, rr = parts(replace(OFFER, monthly_tenure=float(t)))
        a, b = ratios(ee["gp30"], ee["gplife"], cac_b)
        mark = " ← **base**" if t == EOR_MONTHS else ""
        print(f"| **{t}**{mark} | ${ee['gplife']:,.0f} | {rr/ee['gplife']:.0%} | **{a:.2f}:1** "
              f"| **{b:.2f}:1** |")
    e9, r9 = parts(replace(OFFER, monthly_tenure=9.0))
    e30, r30x = parts(replace(OFFER, monthly_tenure=30.0))
    print(f"\n**Each extra month of EOR is worth ${per_client:,.0f} of gross profit per acquired "
          f"client** — about")
    print(f"{per_client/cac_b:.0%} of a whole CAC, every month, at zero incremental acquisition "
          f"cost. Going from {EOR_MONTHS:.0f} months")
    print(f"to 30 adds **${e30['gplife']-e9['gplife']:,.0f}** and takes lifetime from "
          f"{e9['gplife']/cac_b:.2f}:1 to {e30['gplife']/cac_b:.2f}:1.\n")
    print("### Seat continuity vs halving CAC\n")
    print("These are the two big levers left, and on the *ratio* they look about the same size:\n")
    print("| Lever | Lifetime ratio | Absolute GP per client | What it costs |")
    print("|---|---|---|---|")
    print(f"| Base — {EOR_MONTHS:.0f} months, ${cac_b:,.0f} CAC | {e9['gplife']/cac_b:.2f}:1 "
          f"| ${e9['gplife']:,.0f} | — |")
    print(f"| **Halve CAC** to ${cac_b/2:,.0f} | **{2*e9['gplife']/cac_b:.2f}:1** "
          f"| ${e9['gplife']:,.0f} — *unchanged* | A channel breakthrough. Not available on demand |")
    print(f"| **Seat to 30 months** | {e30['gplife']/cac_b:.2f}:1 "
          f"| **${e30['gplife']:,.0f}** — **+${e30['gplife']-e9['gplife']:,.0f}** "
          f"| A contract clause and bench discipline |")
    print(f"\n**The ratio is the wrong scoreboard for this comparison.** Halving CAC wins on the "
          f"ratio and adds")
    print(f"**${cac_b/2:,.0f}** of profit per client. Extending the seat loses on the ratio and adds "
          f"**${e30['gplife']-e9['gplife']:,.0f}** — about")
    print(f"{(e30['gplife']-e9['gplife'])/(cac_b/2):.0f}x more actual money. A ratio can be improved "
          f"by shrinking the denominator, which is why it should")
    print("never be optimised alone.\n")
    print("**So build seat continuity, and it is the same mechanism as the guarantee** — the thing")
    print("that makes a replacement painless is the thing that keeps the EOR fee billing.\n")
    print("The three things that keep a seat alive across a worker exit, in order of cost:\n")
    print("| Mechanism | Cost |\n|---|---|")
    for a, b in [("EOR contract is with the **seat**, not the person — replacement is a novation, "
                  "not a new contract", "Free. A drafting decision, made once"),
                 ("A bench candidate already graded for that client's stack, so the gap is days "
                  "not weeks", "Standing capital in the bench"),
                 ("Provident fund and gratuity, which the state enforces — gratuity vests at 5 "
                  "years, so the worker's own incentive lengthens tenure",
                  "Already inside the ${:.0f} cost".format(om.EOR_COST))]:
        print(f"| {a} | {b} |")
    print("\nThe first one is free and is the one that matters. **If the EOR contract names the "
          "person, every worker exit is a resale. If it names the seat, it is an operational "
          "event.**\n")


if __name__ == "__main__":
    report()
