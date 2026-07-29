#!/usr/bin/env python3
"""
Offer configuration model — optimises 30-day and lifetime LTGP:CAC.

Every configuration shares the same funnel and cost engine; they differ only in
offer terms. Run:  python3 scoring/offer_model.py > scoring/OFFER-MODEL.md
"""

from dataclasses import dataclass, field, replace

# --------------------------------------------------------------- environment

CPL = 100.0            # Meta cost per lead [E]
HORIZON = 36           # lifetime window, months

# Funnel, free-shortlist path [E/?]
# 20% not 40%: a cold Meta B2B lead is low-intent. 40% would be an inbound
# referral rate, and using it was the error in v1 of this model.
LEAD_TO_INTAKE = 0.20  # form fill -> intake call HELD
INTAKE_TO_SEARCH = 0.50  # intake -> they accept terms and we start searching
FILL_RATE = 0.60       # search accepted -> placement made
SALES_COST_PER_CALL = 60.0   # human time per intake call held -> belongs in CAC

# Delivery cost. Scales with placed salary — a $34k senior search is not the
# same work as a $22k bookkeeper search. Flat COGS was the second v1 error.
SEARCH_LABOUR_PCT = 0.035    # recruiter + screening time
CANDIDATE_ADS_PCT = 0.015    # senior candidates cost more to source
SHORTLIST_PCT = 0.005        # grading 3 candidates, charged per SEARCH not per fill
TOOLING = 50.0
PROCESSING = 0.029

# Attrition regime [C/?] — modelled pessimistically per OFFER.md §4
REPLACEMENT_RATE = 0.50       # share of placements triggering a free replacement
REFUND_SHARE_OF_FEE = 0.15    # share of claims that become refunds, not replacements
P_ALIVE_M12 = 0.40            # still employed at month 12

# Lifetime behaviour [?]
P_EXPAND = 0.35        # client hires a second, separate role within 36 months
P_PAID_REPLACE = 0.45  # buys a paid replacement after the guarantee window lapses
PROTECTION_MARGIN = 0.70


@dataclass
class Offer:
    name: str
    salary: float = 22_000          # placed annual salary
    fee_now: float = 0.25           # collected at start
    fee_m12: float = 0.05           # collected at month 12 if still employed
    deposit: float = 0.0            # credited against fee; changes funnel
    slo_price: float = 0.0          # paid front-end product
    slo_take: float = 0.0           # share of leads buying it
    slo_to_place: float = 0.0       # SLO buyer -> placement
    slo_cost: float = 0.0
    protection_attach: float = 0.0  # share taking $297/mo
    protection_price: float = 297.0
    protection_months: float = 12.0
    multi_hire: float = 0.0         # share hiring 2 seats on one acquisition
    note: str = ""

    # funnel adjustments the deposit causes
    dep_search_mult: float = 1.0
    dep_fill_mult: float = 1.0


def economics(o: Offer):
    """Return a dict of per-acquired-client economics."""
    # ---- funnel -> cost per placement
    if o.slo_price:
        # paid front end gates the funnel at the top
        placements_per_lead = o.slo_take * o.slo_to_place
        front_rev = o.slo_take * o.slo_price
        front_cost = o.slo_take * o.slo_cost
        searches_per_lead = o.slo_take * o.slo_to_place / FILL_RATE
    else:
        search_rate = INTAKE_TO_SEARCH * o.dep_search_mult
        fill = min(FILL_RATE * o.dep_fill_mult, 0.95)
        searches_per_lead = LEAD_TO_INTAKE * search_rate
        placements_per_lead = searches_per_lead * fill
        front_rev = front_cost = 0.0

    # shortlist labour is spent on every search, filled or not
    searches_per_placement = searches_per_lead / placements_per_lead
    shortlist_cost = SHORTLIST_PCT * o.salary * searches_per_placement
    gross_cac = CPL / placements_per_lead
    if o.slo_price:
        sales_calls = 0.0   # SLO buyers self-select; no pre-sale call
    else:
        sales_calls = LEAD_TO_INTAKE / placements_per_lead
    net_cac = (gross_cac + sales_calls * SALES_COST_PER_CALL
               - (front_rev - front_cost) / placements_per_lead)

    # ---- seats per acquired client
    seats_now = 1 + o.multi_hire

    # ---- 30-day revenue
    fee_upfront = o.salary * o.fee_now * seats_now
    rev_30 = fee_upfront + o.deposit * 0  # deposit is credited, not additive

    # ---- 30-day COGS
    unit = ((SEARCH_LABOUR_PCT + CANDIDATE_ADS_PCT) * o.salary
            + shortlist_cost + TOOLING)
    direct = unit * seats_now
    # a claim costs a fresh search, and a minority become outright refunds
    claim_cost = (SEARCH_LABOUR_PCT + CANDIDATE_ADS_PCT) * o.salary \
        + REFUND_SHARE_OF_FEE * o.salary * o.fee_now
    reserve = REPLACEMENT_RATE * claim_cost * seats_now
    cogs_30 = direct + reserve + rev_30 * PROCESSING
    gp_30 = rev_30 - cogs_30

    # ---- lifetime
    tail = o.salary * o.fee_m12 * P_ALIVE_M12 * seats_now
    extra_seats = P_EXPAND + P_PAID_REPLACE
    extra_fee = o.salary * o.fee_now * extra_seats
    extra_cogs = (unit * extra_seats
                  + REPLACEMENT_RATE * claim_cost * extra_seats
                  + extra_fee * PROCESSING)
    prot = (o.protection_attach * o.protection_price * o.protection_months
            * PROTECTION_MARGIN)
    gp_life = gp_30 + tail * (1 - PROCESSING) + (extra_fee - extra_cogs) + prot

    return dict(rev_30=rev_30, gp_30=gp_30, margin_30=gp_30 / rev_30 if rev_30 else 0,
                cac=net_cac, r30=gp_30 / net_cac, gp_life=gp_life,
                rlife=gp_life / net_cac, seats=seats_now,
                life_seats=seats_now + extra_seats)


# ------------------------------------------------------------ configurations

BASE = Offer("C1  OFFER.md as written", note="$22k · 25%+5% · free shortlist")

CONFIGS = [
    BASE,
    replace(BASE, name="C2  + $500 engagement deposit", deposit=500,
            dep_search_mult=0.76, dep_fill_mult=1.30,
            note="fewer searches, better ones"),
    replace(BASE, name="C3  senior tier $26k", salary=26_000,
            note="same everything, better candidate"),
    replace(BASE, name="C4  senior tier $34k", salary=34_000,
            note="accountant, not bookkeeper"),
    replace(BASE, name="C5  $34k · 35% single-stage", salary=34_000,
            fee_now=0.35, fee_m12=0.0, note="all cash now, no alignment"),
    replace(BASE, name="C6  $34k · 30%+5% · deposit", salary=34_000, fee_now=0.30,
            deposit=500, dep_search_mult=0.76, dep_fill_mult=1.30),
    replace(BASE, name="C7  C6 + protection 30%", salary=34_000, fee_now=0.30,
            deposit=500, dep_search_mult=0.76, dep_fill_mult=1.30,
            protection_attach=0.30),
    replace(BASE, name="C8  C7 + 20% two-seat", salary=34_000, fee_now=0.30,
            deposit=500, dep_search_mult=0.76, dep_fill_mult=1.30,
            protection_attach=0.30, multi_hire=0.20),
    replace(BASE, name="C9  $297 SLO front end", salary=34_000, fee_now=0.30,
            slo_price=297, slo_take=0.08, slo_to_place=0.35, slo_cost=120,
            note="paid attraction offer"),
    replace(BASE, name="C10 heavy deferral 20/10/10", salary=34_000, fee_now=0.20,
            fee_m12=0.20, note="max client de-risking"),
]

# Capture tunables so sensitivity loops can restore exactly, rather than
# resetting to hardcoded literals that drift when a constant is edited.
_DEFAULTS = {k: globals()[k] for k in
             ("CPL", "REPLACEMENT_RATE", "FILL_RATE", "LEAD_TO_INTAKE", "INTAKE_TO_SEARCH")}


def restore(*keys):
    for k in (keys or _DEFAULTS):
        globals()[k] = _DEFAULTS[k]


# ------------------------------------------------------------------- output

print("# Offer Model — optimising 30-day and lifetime LTGP:CAC\n")
print(f"Generated by [`scoring/offer_model.py`](offer_model.py). "
      f"CPL ${CPL:.0f} · lead→intake {LEAD_TO_INTAKE:.0%} · replacement rate {REPLACEMENT_RATE:.0%} · "
      f"{HORIZON}-month lifetime.\n")
print("All configurations share one funnel and cost engine; only offer terms differ.\n")

print("## Configurations\n")
print("| Config | Salary | Fee | 30-day rev | 30-day GP | GM | CAC | **30d** | Lifetime GP | **Life** |")
print("|---|---|---|---|---|---|---|---|---|---|")
rows = []
for o in CONFIGS:
    e = economics(o)
    fee = (f"{o.fee_now:.0%}" + (f"+{o.fee_m12:.0%}" if o.fee_m12 else "")
           + (" SLO" if o.slo_price else ""))
    flag = "" if e["r30"] >= 1.5 else " ⚠️"
    print(f"| {o.name} | ${o.salary/1000:.0f}k | {fee} | ${e['rev_30']:,.0f} "
          f"| ${e['gp_30']:,.0f} | {e['margin_30']:.0%} | ${e['cac']:,.0f} "
          f"| **{e['r30']:.2f}:1**{flag} | ${e['gp_life']:,.0f} | **{e['rlife']:.2f}:1** |")
    rows.append((o, e))

best30 = max(rows, key=lambda r: r[1]["r30"])
bestlife = max(rows, key=lambda r: r[1]["rlife"])
print(f"\n**Best 30-day:** {best30[0].name} at {best30[1]['r30']:.2f}:1  ")
print(f"**Best lifetime:** {bestlife[0].name} at {bestlife[1]['rlife']:.2f}:1")

# ---- lever isolation
print("\n---\n\n## Which lever actually moves it\n")
print("Each row changes exactly one thing from C1.\n")
print("| Lever | 30-day | vs C1 | Lifetime | vs C1 |")
print("|---|---|---|---|---|")
b = economics(BASE)
levers = [
    ("Baseline C1", BASE),
    ("Salary $22k → $34k", replace(BASE, salary=34_000)),
    ("Fee 25% → 35% upfront", replace(BASE, fee_now=0.35, fee_m12=0.0)),
    ("Add $500 deposit", replace(BASE, deposit=500, dep_search_mult=0.76,
                                 dep_fill_mult=1.30)),
    ("Protection attach 30%", replace(BASE, protection_attach=0.30)),
    ("20% take two seats", replace(BASE, multi_hire=0.20)),
    ("Add $297 SLO", replace(BASE, slo_price=297, slo_take=0.08,
                             slo_to_place=0.35, slo_cost=120)),
]
for label, o in levers:
    e = economics(o)
    d30 = e["r30"] - b["r30"]
    dl = e["rlife"] - b["rlife"]
    print(f"| {label} | **{e['r30']:.2f}:1** | {d30:+.2f} "
          f"| **{e['rlife']:.2f}:1** | {dl:+.2f} |")

# ---- sensitivity on the two unknowns that matter
REC = rows[7][0]  # C8
print("\n---\n\n## Sensitivity on the recommended configuration (C8)\n")
print("### CPL × replacement rate\n")
print("| | " + " | ".join(f"repl {r:.0%}" for r in (0.15, 0.30, 0.50, 0.70)) + " |")
print("|---|" + "---|" * 4)
for cpl in (50, 100, 150, 200, 250):
    cells = []
    for rr in (0.15, 0.30, 0.50, 0.70):
        g = globals()
        g["CPL"], g["REPLACEMENT_RATE"] = float(cpl), rr
        e = economics(REC)
        mark = "" if e["r30"] >= 1.5 else "⚠️"
        cells.append(f"{e['r30']:.2f}:1{mark}")
    print(f"| **CPL ${cpl}** | " + " | ".join(cells) + " |")
restore("CPL", "REPLACEMENT_RATE")

print("\n### Fill rate — the constraint\n")
print("| Fill rate | CAC | 30-day | Lifetime |")
print("|---|---|---|---|")
for f in (0.80, 0.70, 0.60, 0.50, 0.40, 0.30):
    globals()["FILL_RATE"] = f
    e = economics(REC)
    mark = "" if e["r30"] >= 1.5 else " ⚠️"
    print(f"| {f:.0%} | ${e['cac']:,.0f} | **{e['r30']:.2f}:1**{mark} | {e['rlife']:.2f}:1 |")
restore("FILL_RATE")

print("\n### Lead → intake × intake → search (the two unmeasured rates)\n")
print("| | " + " | ".join(f"search {s:.0%}" for s in (0.30, 0.40, 0.50, 0.60)) + " |")
print("|---|" + "---|" * 4)
for li in (0.25, 0.30, 0.40, 0.50):
    cells = []
    for s in (0.30, 0.40, 0.50, 0.60):
        globals()["LEAD_TO_INTAKE"], globals()["INTAKE_TO_SEARCH"] = li, s
        e = economics(REC)
        mark = "" if e["r30"] >= 1.5 else "⚠️"
        cells.append(f"{e['r30']:.2f}:1{mark}")
    print(f"| **intake {li:.0%}** | " + " | ".join(cells) + " |")
restore("LEAD_TO_INTAKE", "INTAKE_TO_SEARCH")

e = economics(REC)
print(f"\n---\n\n## Recommended: {REC.name}\n")
print(f"| | |\n|---|---|")
print(f"| Placed salary | **${REC.salary:,.0f}** |")
print(f"| Fee | **{REC.fee_now:.0%} at start + {REC.fee_m12:.0%} at month 12** |")
print(f"| Engagement deposit | **${REC.deposit:,.0f}**, credited |")
print(f"| Protection attach | {REC.protection_attach:.0%} at ${REC.protection_price:.0f}/mo |")
print(f"| Two-seat share | {REC.multi_hire:.0%} |")
print(f"| 30-day revenue | ${e['rev_30']:,.0f} |")
print(f"| 30-day gross profit | **${e['gp_30']:,.0f}** ({e['margin_30']:.0%}) |")
print(f"| Net CAC | ${e['cac']:,.0f} |")
print(f"| **30-day LTGP:CAC** | **{e['r30']:.2f}:1** |")
print(f"| Lifetime gross profit | ${e['gp_life']:,.0f} over {e['life_seats']:.2f} seats |")
print(f"| **Lifetime LTGP:CAC** | **{e['rlife']:.2f}:1** |")
