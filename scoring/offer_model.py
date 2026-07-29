#!/usr/bin/env python3
"""
Offer model v3 — built on researched competitor pricing and realistic CPL.

Changes from v2:
  * Placed salary 22,000 (mass market, per operator direction) not 34,000
  * CPL 75 not 100. Meta B2B CPL benchmarks 2026: overall FB average $27.66;
    B2B band $30-80; finance $58.70, legal $72.40; qualified B2B $150-250.
    A hiring offer to US business owners sits with finance/legal.
  * Fee structure copied from Somewhere: refundable $500 deposit that gates
    the SEARCH (not the close), 35% single-stage, 6-month replacement.
  * Funnel restructured to match Somewhere's actual flow:
        lead -> call held -> deposit paid (search starts) -> shortlist -> hire
  * Full market fee stack modelled as toggles
  * Novel mechanics from v2 (stay-bonus escrow, 30%+5% split) kept only as a
    comparison config — v2 showed the split costs ~$1,020/placement

Run:  python3 scoring/offer_model.py > scoring/OFFER-MODEL.md
"""

from dataclasses import dataclass, replace

# ---------------------------------------------------------------- environment

CPL = 75.0
SALARY = 22_000.0
HORIZON = 36

# Funnel — Somewhere's actual shape [E/?]
LEAD_TO_CALL = 0.22      # cold Meta B2B lead -> discovery call HELD
CALL_TO_DEPOSIT = 0.35   # call -> $500 refundable deposit paid, search opens
DEPOSIT_TO_HIRE = 0.80   # search -> placement. High: we replace until matched
SALES_COST_PER_CALL = 60.0

# Delivery cost, scaling with placed salary
SEARCH_LABOUR_PCT = 0.035
CANDIDATE_ADS_PCT = 0.015
SHORTLIST_PCT = 0.005          # per SEARCH opened, not per fill
SCREENING_PASSTHRU = 175.0     # background $50-200 + assessment $25-150 +
                               # reference verification $25-75 [V]
TOOLING = 50.0
PROCESSING = 0.029

# Attrition regime [C/?] — pessimistic
REPLACEMENT_RATE = 0.50
REFUND_SHARE_OF_FEE = 0.15

# Lifetime behaviour [?]
P_EXPAND = 0.35
P_PAID_REPLACE = 0.45
PROTECTION_MARGIN = 0.70
MONTHLY_SEAT_COGS = 150.0      # payroll/remittance admin + AM time, per seat/mo


@dataclass
class Offer:
    name: str
    salary: float = SALARY
    # --- fee stack (all market-observed structures)
    deposit: float = 500.0          # refundable, credited to final invoice
    fee_pct: float = 0.35           # single-stage placement fee
    fee_tail_pct: float = 0.0       # deferred slice at month 12
    volume_pct: float = 0.0         # blended rate on repeat seats (slide)
    charge_screening: bool = False  # pass screening costs through to client
    protection_attach: float = 0.0  # $297/mo protection layer
    protection_price: float = 297.0
    protection_months: float = 12.0
    monthly_spread: float = 0.0     # managed-seat spread per month
    monthly_tenure: float = 18.0
    escrow: float = 0.0             # stay-bonus escrow (pass-through, not revenue)
    claim_rate: float = REPLACEMENT_RATE   # share of placements claiming
    refund_share: float = REFUND_SHARE_OF_FEE  # share of claims paid in CASH
    bench_shortlist: float = 0.0    # cost per call held to show bench candidates
    managed_convert: float = 0.0    # share of clients converted to a managed seat later
    # --- funnel
    lead_to_call: float = LEAD_TO_CALL
    call_to_deposit: float = CALL_TO_DEPOSIT
    deposit_to_hire: float = DEPOSIT_TO_HIRE
    multi_hire: float = 0.0
    extra_seats: float = P_EXPAND + P_PAID_REPLACE
    note: str = ""


def econ(o: Offer):
    place_per_lead = o.lead_to_call * o.call_to_deposit * o.deposit_to_hire
    searches_per_place = 1.0 / o.deposit_to_hire
    calls_per_place = o.lead_to_call / place_per_lead

    cac = CPL / place_per_lead + calls_per_place * SALES_COST_PER_CALL
    seats = 1 + o.multi_hire

    # ---- 30-day revenue
    fee = o.salary * o.fee_pct * seats
    screening_rev = (SCREENING_PASSTHRU * 1.6 * seats) if o.charge_screening else 0.0
    monthly_rev = o.monthly_spread * seats            # month 1 only, in window
    rev30 = fee + screening_rev + monthly_rev

    # ---- 30-day COGS
    unit = ((SEARCH_LABOUR_PCT + CANDIDATE_ADS_PCT) * o.salary
            + SHORTLIST_PCT * o.salary * searches_per_place
            + SCREENING_PASSTHRU + TOOLING)
    claim = ((SEARCH_LABOUR_PCT + CANDIDATE_ADS_PCT) * o.salary
             + o.refund_share * o.salary * o.fee_pct)
    cogs30 = (unit * seats + o.claim_rate * claim * seats
              + o.bench_shortlist * calls_per_place
              + MONTHLY_SEAT_COGS * seats * (1 if o.monthly_spread else 0)
              + rev30 * PROCESSING)
    gp30 = rev30 - cogs30

    # ---- lifetime
    tail = o.salary * o.fee_tail_pct * (1 - REPLACEMENT_RATE) * seats
    extra = o.extra_seats
    rate = o.volume_pct or o.fee_pct
    xfee = o.salary * rate * extra
    xscreen = (SCREENING_PASSTHRU * 1.6 * extra) if o.charge_screening else 0.0
    xcogs = (unit * extra + o.claim_rate * claim * extra
             + (xfee + xscreen) * PROCESSING)
    prot = (o.protection_attach * o.protection_price * o.protection_months
            * PROTECTION_MARGIN)
    mrec = (o.monthly_spread - MONTHLY_SEAT_COGS) * max(o.monthly_tenure - 1, 0) * seats
    # later conversion of placement clients onto managed seats — recurring layer
    mrec += (o.managed_convert * (800.0 - MONTHLY_SEAT_COGS) * o.monthly_tenure * seats)
    gplife = gp30 + tail * (1 - PROCESSING) + (xfee + xscreen - xcogs) + prot + mrec

    return dict(rev30=rev30, gp30=gp30, gm=gp30 / rev30 if rev30 else 0, cac=cac,
                r30=gp30 / cac, gplife=gplife, rlife=gplife / cac,
                ppl=place_per_lead, seats=seats)


# --------------------------------------------------------------- configurations

SW = Offer("S1  Somewhere, copied", note="$500 deposit · 35% single · 6mo guarantee")
OPT = dict(lead_to_call=0.30, call_to_deposit=0.45, deposit_to_hire=0.88)

CONFIGS = [
    SW,
    replace(SW, name="S2  + screening billed through", charge_screening=True),
    replace(SW, name="S3  + optimised funnel", **OPT),
    replace(SW, name="S4  S3 + screening + protection", charge_screening=True,
            protection_attach=0.30, **OPT),
    replace(SW, name="S5  S4 + 20% two-seat", charge_screening=True,
            protection_attach=0.30, multi_hire=0.20, **OPT),
    replace(SW, name="S6  S5 + slide to 27%, no volume gained", charge_screening=True,
            protection_attach=0.30, multi_hire=0.20, volume_pct=0.27, **OPT),
    replace(SW, name="S6b S5 + slide to 27% that WORKS", charge_screening=True,
            protection_attach=0.30, multi_hire=0.20, volume_pct=0.27,
            extra_seats=1.10, **OPT),
    replace(SW, name="S7  traditional 22% (F&A norm)", fee_pct=0.22, **OPT),
    replace(SW, name="S8  Hey Foster's 20%", fee_pct=0.20, **OPT),
    replace(SW, name="S9  pure monthly managed", fee_pct=0.0, monthly_spread=800.0,
            **OPT),
    replace(SW, name="S10 monthly + 1mo placement fee", fee_pct=0.0833,
            monthly_spread=800.0, **OPT),
    replace(SW, name="S11 v2 novel structure", fee_pct=0.30, fee_tail_pct=0.05,
            escrow=2500.0, **OPT),
    # --- Hormozi revisions
    replace(SW, name="H1  S5 + 12mo UNLIMITED replace, no refunds",
            charge_screening=True, protection_attach=0.30, multi_hire=0.20,
            claim_rate=0.70, refund_share=0.0, **OPT),
    replace(SW, name="H2  H1 + free bench shortlist pre-deposit",
            charge_screening=True, protection_attach=0.30, multi_hire=0.20,
            claim_rate=0.70, refund_share=0.0, bench_shortlist=90.0,
            lead_to_call=0.30, call_to_deposit=0.60, deposit_to_hire=0.88),
    replace(SW, name="H3  H2 + 25% convert to managed seats",
            charge_screening=True, protection_attach=0.30, multi_hire=0.20,
            claim_rate=0.70, refund_share=0.0, bench_shortlist=90.0,
            managed_convert=0.25,
            lead_to_call=0.30, call_to_deposit=0.60, deposit_to_hire=0.88),
]

_D = {k: globals()[k] for k in
      ("CPL", "REPLACEMENT_RATE", "LEAD_TO_CALL", "CALL_TO_DEPOSIT", "DEPOSIT_TO_HIRE")}


def restore(*keys):
    for k in (keys or _D):
        globals()[k] = _D[k]


# --------------------------------------------------------------------- output

print("# Offer Model v3 — built on researched competitor pricing\n")
print(f"Generated by [`scoring/offer_model.py`](offer_model.py). "
      f"Placed salary **${SALARY:,.0f}** · CPL **${CPL:.0f}** · "
      f"replacement rate {REPLACEMENT_RATE:.0%} · {HORIZON}-month lifetime.\n")

print("## What the market actually charges\n")
print("| Structure | Market figure | Source |")
print("|---|---|---|")
for a, bb, c in [
    ("Somewhere placement fee", "**25–35%** of first-year salary, sliding down with volume", "somewhere.com"),
    ("Somewhere deposit", "**Refundable**, credited to final invoice. Gates the **search**", "somewhere.com"),
    ("Somewhere guarantee", "**6-month** perfect-hire guarantee, free replacement", "somewhere.com"),
    ("Somewhere speed", "Candidates in **as little as 3 days**; most hire **under 21 days**", "somewhere.com"),
    ("Somewhere scale", "**250+ placements** in a recent month; **18+ countries**", "somewhere.com"),
    ("Somewhere 2nd product", "**Talent On-Demand** — monthly fee, 10–20 days, *unlimited* free replacements", "somewhere.com/pricing"),
    ("Somewhere rate card", "Sample candidate rates **$1,200–$7,000/month**", "somewhere.com/pricing"),
    ("Hey Foster", "**20%** of salary, *or* subscription **$1,000/mo** (≤6 hires/yr) / **$3,167/mo** (≤30/yr)", "heyfoster.com"),
    ("Oceans", "**From $3,000/mo** managed · **3-month trial** then rolling · month-long in-person training", "oceanstalent.com"),
    ("Managed seat spread", "Client pays **$2,000–2,600/mo**, contractor gets **$1,000–1,600/mo**", "morestaffing.co"),
    ("Managed bookkeeper", "**$1,250–1,700/mo** vs US domestic **$4,200–5,400/mo**", "morenow.co"),
    ("US perm placement norm", "Entry **11–20%** · mid **20–22%** · senior **21–30%** · **accountants 18–22%**", "secondtalent.com"),
    ("Flat-fee norm", "Entry **$1,000–3,000** · mid **$3,000–7,500**", "secondtalent.com"),
    ("Volume discounts", "11–25 placements **1–10% off** · 25+ **10–20%** · exclusive up to **21%**", "secondtalent.com"),
    ("Screening pass-throughs", "Background **$50–200** · assessments **$25–150** · references **$25–75**", "secondtalent.com"),
    ("Market add-ons", "Placement fee **on top of** monthly (1 month salary) · equipment · contract minimums **6–12mo** with penalties", "morenow.co"),
    ("Staffing margins", "Temp gross **14–41%** (avg 21%); net profit **3–8%**", "secondtalent.com"),
]:
    print(f"| {a} | {bb} | {c} |")

print("\n---\n\n## Configurations\n")
print("| Config | Fee | 30-day rev | 30-day GP | GM | CAC | **30-day** | Lifetime GP | **Lifetime** |")
print("|---|---|---|---|---|---|---|---|---|")
for o in CONFIGS:
    e = econ(o)
    fee = (f"{o.fee_pct:.0%}" + (f"+{o.fee_tail_pct:.0%}" if o.fee_tail_pct else "")
           + (f" +${o.monthly_spread:.0f}/mo" if o.monthly_spread else ""))
    flag = "" if e["r30"] >= 1.5 else " ⚠️"
    print(f"| {o.name} | {fee} | ${e['rev30']:,.0f} | ${e['gp30']:,.0f} | {e['gm']:.0%} "
          f"| ${e['cac']:,.0f} | **{e['r30']:.2f}:1**{flag} | ${e['gplife']:,.0f} "
          f"| **{e['rlife']:.2f}:1** |")

print("\n---\n\n## Funnel optimisation\n")
print("Somewhere's actual flow. The deposit gates the **search**, not the close — which is why")
print("their fill rate can run high. An unfunded search never opens.\n")
print("```")
print("LEAD ──► CALL HELD ──► $500 DEPOSIT ──► SHORTLIST ──► HIRE")
print("        (biggest leak)  (search opens)    (3 in 48h)")
print("```\n")
print("| Stage | Base | Optimised | Lever |")
print("|---|---|---|---|")
for s, bv, ov, lever in [
    ("Lead → call held", "22%", "**30%**",
     "Booking widget on the thank-you page, same-day slots, SMS + email reminder sequence, "
     "two qualifying questions on the form to trade volume for intent"),
    ("Call → deposit paid", "35%", "**45%**",
     "**Show 2–3 real candidate profiles on the call itself.** Turns *trust me* into *look at "
     "these three people*. Only possible because we run one role in one country — Somewhere "
     "cannot do this across 18 countries and dozens of roles"),
    ("Deposit → hire", "80%", "**88%**",
     "Standing bench, present 3 never 1, replace until matched, anchor salary in writing at intake"),
]:
    print(f"| {s} | {bv} | {ov} | {lever} |")

b, o2 = econ(SW), econ(replace(SW, **OPT))
print(f"\n| | Lead→placement | CAC | 30-day |\n|---|---|---|---|")
print(f"| Base | {b['ppl']:.2%} | ${b['cac']:,.0f} | **{b['r30']:.2f}:1** |")
print(f"| Optimised | {o2['ppl']:.2%} | ${o2['cac']:,.0f} | **{o2['r30']:.2f}:1** |")
print(f"\n**Funnel work is worth {o2['r30']/b['r30']:.1f}x on the ratio — more than any pricing")
print("change in the table above, and it costs nothing but craft.**\n")

print("### Which stage to fix first\n")
print("| Stage | −25% | base | +25% | +50% |")
print("|---|---|---|---|---|")
for key, label in [("lead_to_call", "Lead → call"), ("call_to_deposit", "Call → deposit"),
                   ("deposit_to_hire", "Deposit → hire")]:
    cells = []
    for m in (0.75, 1.0, 1.25, 1.5):
        e = econ(replace(SW, **{key: min(getattr(SW, key) * m, 0.95)}))
        cells.append(f"{e['r30']:.2f}:1")
    print(f"| {label} | " + " | ".join(cells) + " |")
print("\nAll three are near-equivalent in leverage, so fix them in cost order: the reminder")
print("sequence is free, candidate profiles on the call cost one recruiter-hour, bench depth")
print("costs standing capital.\n")

print("### The volume slide has a breakeven\n")
s5 = next(c for c in CONFIGS if c.name.startswith("S5"))
s6 = next(c for c in CONFIGS if c.name.startswith("S6 "))
s6b = next(c for c in CONFIGS if c.name.startswith("S6b"))
print("Somewhere slides 35% down to 25% on volume. The slide **costs** margin on repeat seats and")
print("only pays if it buys enough extra seats to cover the discount.\n")
print("| | Repeat seats | Lifetime GP | Lifetime ratio |")
print("|---|---|---|---|")
for c in (s5, s6, s6b):
    ec = econ(c)
    print(f"| {c.name} | {c.extra_seats:.2f} | ${ec['gplife']:,.0f} | **{ec['rlife']:.2f}:1** |")
disc = (0.35 - 0.27) / 0.35
print(f"\nDiscounting 35% → 27% gives up **{disc:.0%}** of the fee on every repeat seat, so the slide")
print(f"must lift repeat seats by more than {disc:.0%} — from {s5.extra_seats:.2f} to "
      f"**{s5.extra_seats*(1+disc):.2f}+** — to break even. **Do not publish a slide until repeat")
print("behaviour is measured.** Offer it deal-by-deal on request instead.\n")


print("---\n\n## The full model landscape\n")
print("| Model | Market pricing | Wins when |")
print("|---|---|---|")
for a, bb, c in [
    ("Contingency placement", "15–30% of salary; offshore specialists **25–35%**", "**Under 15–20 hires/yr**"),
    ("Zero-fee flat hourly", "Virtustant **$7–8/hr all-in**, median $8.00 across 2,018 placements", "Client refuses a fee, accepts markup"),
    ("Managed monthly seat", "**$1,250–2,600/mo** bookkeeper; spread ~$800–1,000/mo", "Client wants zero employment burden"),
    ("Monthly fee per hire", "Pearl Talent — monthly per hire by role complexity", "Blend of both"),
    ("Per-FTE / hourly", "1840 & Co **under $25/hr**, min engagement **~$10,000**", "Larger, custom engagements"),
    ("Subscription recruiting", "**$2,000–10,000/mo** (refined $3,000–8,000). Cuts cost **50–70%** vs contingency for multi-hire", "**Senior salaries, multiple hires**"),
    ("RPO", "**$3,000–10,000/hire** or **$8,000–15,000/mo** per embedded recruiter", "**15–25+ roles/yr**"),
    ("Retained search", "**21–31%**, paid in thirds", "Executive"),
]:
    print(f"| {a} | {bb} | {c} |")

print("\n### Why the percentage model is structurally right at $22k\n")
print("Subscription and RPO win on **high salaries and high volume**, because a flat fee does not")
print("grow with salary while a percentage does. Inverted at the mass-market salary band:\n")
print("| Client hires/yr | Our 35% of $22k | Subscription at $3,000/mo | Winner |")
print("|---|---|---|---|")
for n in (1, 2, 3, 5, 8, 12):
    ours = 0.35 * SALARY * n
    sub = 36_000
    print(f"| {n} | ${ours:,.0f} | ${sub:,.0f} | "
          f"{'**us**' if ours < sub else 'subscription'} |")
print("\n**Below ~5 hires a year we are structurally cheaper than any subscription competitor, and")
print("cannot be undercut.** Above that we lose the account to a flat fee. So the volume slide is")
print("not a nice-to-have — it is the defence on multi-hire accounts. Keep it unpublished and bring")
print("it out at hire five.\n")

print("---\n\n## The guarantee is the cheapest differentiation available\n")
print("Every player offers the same **6-month replacement**. It is a commodity. But a")
print("*stronger-sounding* guarantee can cost **less** if you change what is being guaranteed —")
print("because labour is a cheaper currency than cash.\n")
s5x = next(c for c in CONFIGS if c.name.startswith("S5"))
h1x = next(c for c in CONFIGS if c.name.startswith("H1"))
print("| | Claim rate | Refunds | Reserve/placement | 30-day GP | 30-day |")
print("|---|---|---|---|---|---|")
for c in (s5x, h1x):
    ec = econ(c)
    res = c.claim_rate * ((SEARCH_LABOUR_PCT + CANDIDATE_ADS_PCT) * c.salary
                          + c.refund_share * c.salary * c.fee_pct)
    print(f"| {c.name.split('+')[-1].strip() if '+' in c.name else c.name} | {c.claim_rate:.0%} "
          f"| {'cash on ' + format(c.refund_share, '.0%') + ' of claims' if c.refund_share else '**none — labour only**'} "
          f"| ${res:,.0f} | ${ec['gp30']:,.0f} | **{ec['r30']:.2f}:1** |")
print("\n**Doubling the guarantee window to 12 months AND making replacements unlimited is")
print("*cheaper* than the 6-month industry standard**, because eliminating cash refunds saves more")
print("than the extra claims cost. Best guarantee in the market, at negative cost.\n")

REC = next(c for c in CONFIGS if c.name.startswith('H3'))
print("---\n\n## Sensitivity — recommended (S6)\n")
print("### CPL × replacement rate\n")
print("| | repl 15% | repl 30% | repl 50% | repl 70% |")
print("|---|---|---|---|---|")
for cpl in (40, 75, 120, 175, 250):
    cells = []
    for rr in (0.15, 0.30, 0.50, 0.70):
        globals()["CPL"], globals()["REPLACEMENT_RATE"] = float(cpl), rr
        e = econ(REC)
        cells.append(f"{e['r30']:.2f}:1" + ("" if e["r30"] >= 1.5 else "⚠️"))
    tag = {75: " *(B2B benchmark)*", 175: " *(qualified B2B)*"}.get(cpl, "")
    print(f"| **CPL ${cpl}**{tag} | " + " | ".join(cells) + " |")
restore("CPL", "REPLACEMENT_RATE")

e = econ(REC)
print(f"\n---\n\n## Recommended — {REC.name}\n")
print("| | |\n|---|---|")
print(f"| Placed salary | **${REC.salary:,.0f}** |")
print(f"| Deposit | **${REC.deposit:,.0f}** refundable, credited — gates the search |")
slide = (f", sliding to **{REC.volume_pct:.0%}** on repeat seats" if REC.volume_pct
         else " single-stage, **no published slide** — see breakeven above")
print(f"| Placement fee | **{REC.fee_pct:.0%}**{slide} |")
print(f"| Screening | Billed through at cost × 1.6 (${SCREENING_PASSTHRU*1.6:,.0f}) |")
print(f"| Protection layer | {REC.protection_attach:.0%} attach at ${REC.protection_price:.0f}/mo |")
g = ("**12-month unlimited free replacement, no cash refunds**"
     if REC.refund_share == 0 else "6-month replacement with cash refunds")
print(f"| Guarantee | {g} |")
if REC.bench_shortlist:
    print(f"| Attraction offer | **Free graded shortlist from the bench, before any deposit** "
          f"(${REC.bench_shortlist:.0f}/call held) |")
print(f"| 30-day revenue | ${e['rev30']:,.0f} |")
print(f"| 30-day gross profit | **${e['gp30']:,.0f}** ({e['gm']:.0%}) |")
print(f"| Net CAC | ${e['cac']:,.0f} |")
print(f"| **30-day LTGP:CAC** | **{e['r30']:.2f}:1** |")
print(f"| Lifetime gross profit | ${e['gplife']:,.0f} |")
print(f"| **Lifetime LTGP:CAC** | **{e['rlife']:.2f}:1** |")
