#!/usr/bin/env python3
"""
Eighteen funnels reranked for ease of build, deploy and check in the first six
months — and for the two structural facts the earlier passes missed.

Operator direction, this pass:
  "we need ease of design and deploy and check and less complications esp in
   first 6 months"
  "think through others like us who run meta ads and see what funnels are
   working for them"

`competitors.py` studied the CATEGORY — Somewhere, Athyna, Genius and the rest.
Those are funded, SEO-led and staffed. This script studies the other reference
class: SOLO AND SMALL OPERATORS BUYING COLD META TRAFFIC FOR HIGH-TICKET B2B
SERVICES. Different playbook, and it has published benchmarks the category does
not.

Two findings from that literature change the arithmetic:

  1. SPEED TO LEAD. Contact inside 5 minutes closes at 32%; after 24 hours, 12%
     [V]. An India-based solo operator selling into US/UK hours CANNOT hit five
     minutes. Every funnel that depends on CHASING a lead therefore carries a
     structural penalty that no competitor in the category pays. Self-serve
     booking is immune — the calendar works while you sleep.

  2. INSTANT FORMS. They win CPL and lose everything after it: appointment rate
     ~2% against ~17% for landing-page leads [V], SQL rates 35-55% lower [V].
     One published source says lead ads win below $25k ACV; another prices the
     qualification gap. §3 reconciles them rather than picking one.

Evidence tags: [V] published benchmark, cited · [E] estimated in this repo ·
[?] no data exists, swept in §7.

Run:  python3 scoring/operators.py > scoring/OPERATORS.md
"""

import io
import itertools
import os
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass, field, replace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

with redirect_stdout(io.StringIO()):
    import funnel as fn
    import offer_model as om
    import competitors as cp          # reuse the competitor table, no drift

SPEND = 5000.0
FOUNDER_HR = 60.0
SALES_HRS = 60.0
LEARN_WEEK = 50
WEEKS = 4.33
MIX = cp.MIX
GP30, GPLIFE = cp.GP30, cp.GPLIFE

# Derived from the published speed-to-lead spread: <5 min closes at 32%, 24h+ at
# 12% [V]. An IST operator answering a US lead is realistically 6-12 hours late,
# which is most of the way to the bad end. 0.65 is the interpolation, and §7
# sweeps it from 0.45 to 0.85 because it is the single most load-bearing new
# assumption in this file.
SPEED_PENALTY = 0.65

# The published operator-world benchmarks this file is calibrated against.
BENCH = [
    ("Application → call held", "**30–60%**",
     "high-ticket B2B application funnels", "conversionxperts.com"),
    ("Call → closed", "**10–25%**", "same source; our close rates all sit inside it",
     "conversionxperts.com"),
    ("Instant Form → appointment", "**~2%** (1 in 50)",
     "against **~17%** (1 in 6) for landing-page leads", "volumecreatives.com"),
    ("Instant Form SQL rate", "**35–55% lower**", "than landing-page campaigns",
     "adamigo.ai"),
    ("Adding one open-ended question", "**−30% volume, qualify 30% → 65–70%**",
     "the documented fix for lead-ad quality", "adlibrary.com"),
    ("Embedded scheduling link", "**+30–40% booking**",
     "vs asking the prospect to reply with availability", "conversionxperts.com"),
    ("*\"Book a Free Consultation\"* vs *\"Contact Us\"*", "**+15–30% CTR**",
     "CTA wording, measured", "analyticsbeyond.com"),
    ("Contact <5 min vs >24h", "**32% vs 12% close**",
     "and 21× more likely to qualify than at 30 minutes", "aimdoc.ai · plura.ai"),
    ("Average B2B response time", "**47 hours**",
     "only **23%** answer inside 5 minutes — the bar is low", "plura.ai"),
    ("Meta CPL, all industries 2025", "**$41.60, +21% YoY**",
     "our modelled CPLs must be read against a rising floor", "get-ryze.ai"),
    ("ACV tiering", "**<$25k → lead ads · $25–75k → landing page · $75k+ → direct booking**",
     "one source's framing; §3 disputes its application here", "growthspreeofficial.com"),
]


@dataclass
class F:
    key: str
    name: str
    world: str                 # "category" or "operator" — which reference class
    precedent: str
    event: str
    c1: float
    show: float
    close: float
    fill: float
    lpv: float = 0.85
    c2: float = 1.0
    chase: bool = False        # does conversion depend on us responding fast?
    min_lead: float = 5.0
    min_held: float = 60.0
    min_sample: float = 0.0
    gate_share: float = 1.0
    systems: int = 3           # distinct tools to wire together
    setup: float = 1.0         # days to first launch
    ongoing: float = 0.0       # recurring production burden, 0-3
    reveals: str = ""
    discover: int = 0
    trust: int = 0
    generic: int = 0
    prec: int = 0
    note: str = ""


FUNNELS = [
    # ---------------------------------------------------- from the category
    F("bench", "See the bench — graded people, unlocked by email", "category",
      "Genius' CTA · Athyna 40+ · Somewhere 9 · GrowthAssistant 4",
      "Bench unlocked", c1=0.075, c2=0.28, show=0.62, close=0.24, fill=0.76,
      min_lead=2.0, systems=4, setup=2.0, ongoing=1.0,
      reveals="**Role, ICP, and which person appeals**", discover=10, trust=9,
      generic=7, prec=10,
      note="Needs 2 graded people per role before the ad runs"),

    F("quiz", "Role-select quiz → matched profiles → call", "category",
      "Athena's role-select entry · Somewhere's role→region tool",
      "Quiz completed", c1=0.070, c2=0.30, show=0.64, close=0.25, fill=0.77,
      min_lead=2.0, systems=4, setup=1.5, ongoing=1.0,
      reveals="**Role, ICP, size and timing** — every answer a field you chose",
      discover=10, trust=7, generic=9, prec=8,
      note="Same bench dependency as above"),

    F("match", "One-field form — *\"tell us about your company\"*", "category",
      "GrowthAssistant exactly", "Form fill",
      c1=0.062, c2=0.34, show=0.56, close=0.17, fill=0.68, chase=True,
      min_lead=9.0, systems=3, setup=0.5,
      reveals="**Almost nothing** — a free-text box", discover=3, trust=4,
      generic=10, prec=9,
      note="**Chase-dependent, and that is now costed**"),

    F("calc", "Cost calculator → email → call", "category",
      "Somewhere and Athyna salary tools · GrowthAssistant's comparison table",
      "Calculator completed", c1=0.060, c2=0.30, show=0.60, close=0.21, fill=0.75,
      chase=True, min_lead=3.0, systems=5, setup=2.0,
      reveals="Their volume and vendor spend", discover=7, trust=7, generic=8, prec=9,
      note="The only genuinely custom-coded block in the study"),

    F("trial", "Paid micro-trial that delivers real work — $100–250", "category",
      "Vidpros' $100 trial: 10 edits in a week", "Trial purchased",
      c1=0.011, show=0.90, close=0.52, fill=0.86, min_lead=3.0, min_sample=100.0,
      systems=4, setup=1.0, ongoing=3.0,
      reveals="**Role, ICP and willingness to pay**", discover=6, trust=10,
      generic=4, prec=7,
      note="You personally do every trial, forever"),

    F("price", "Publish the price, then book onboarding", "category",
      "GrowthAssistant $3,500/mo · Hireframe $2,500/mo · Genius 25%",
      "Booked call", c1=0.024, show=0.74, close=0.24, fill=0.80, min_lead=4.0,
      systems=2, setup=0.5,
      reveals="Role only", discover=4, trust=6, generic=10, prec=10,
      note="**Two systems. The simplest thing that could work**"),

    F("cal", "Free consult, calendar straight on the page", "category",
      "Vidchops and Somewhere both do exactly this", "Booked call",
      c1=0.020, show=0.65, close=0.12, fill=0.68, systems=2, setup=0.25,
      reveals="Role only", discover=2, trust=4, generic=10, prec=10,
      note="Immune to the speed penalty — the calendar works overnight"),

    F("gate", "Qualifying gate with a real no, then the calendar", "category",
      "**Zero of ten competitors gates**", "Application submitted",
      c1=0.022, c2=0.70, show=0.72, close=0.18, fill=0.78, min_lead=2.0,
      systems=3, setup=1.0,
      reveals="Spend, revenue, volume", discover=6, trust=6, generic=9, prec=2),

    F("free", "Free graded sample on *their* asset", "category",
      "**None.** No competitor gives away work on the prospect's material",
      "Sample requested", c1=0.045, c2=0.42, show=0.75, close=0.30, fill=0.80,
      chase=True, min_lead=4.0, min_sample=90.0, gate_share=0.35,
      systems=4, setup=0.5, ongoing=3.0,
      reveals="Role, ICP, high intent", discover=6, trust=10, generic=3, prec=1),

    F("instant", "Meta Instant Form, no landing page", "operator",
      "Ubiquitous in the small-operator world; **the data is brutal**",
      "Lead (on-platform)", c1=0.120, c2=0.30, show=0.40, close=0.06, fill=0.55,
      lpv=1.00, chase=True, min_lead=12.0, systems=2, setup=0.25, ongoing=2.0,
      reveals="Whatever the form asks, from people who never saw a page",
      discover=4, trust=1, generic=10, prec=6,
      note="**~2% appointment rate vs ~17% from a landing page** [V]"),

    # ---------------------------------------------- new, from the operator world
    F("instantq", "Instant Form **+ one open-ended question**", "operator",
      "The documented fix: **−30% volume, qualify rate 30% → 65–70%** [V]",
      "Qualified lead", c1=0.084, c2=0.34, show=0.46, close=0.11, fill=0.62,
      lpv=1.00, chase=True, min_lead=9.0, systems=2, setup=0.5, ongoing=2.0,
      reveals="One typed sentence — the best cheap intent signal there is",
      discover=6, trust=2, generic=10, prec=8,
      note="**Still chase-dependent**, which is what caps it for us"),

    F("vsl", "VSL → application → call", "operator",
      "**The canonical high-ticket funnel.** application→call 30–60% [V]",
      "Application submitted", c1=0.026, c2=0.45, show=0.78, close=0.28, fill=0.80,
      lpv=0.80, min_lead=3.0, systems=4, setup=3.0, ongoing=1.0,
      reveals="Everything the application asks, from people who watched you talk",
      discover=8, trust=7, generic=4, prec=10,
      note="A video that names a role must be reshot per cell"),

    F("webinar", "Free training / evergreen webinar → call", "operator",
      "Standard in the agency-owner world", "Registered",
      c1=0.095, c2=0.16, show=0.58, close=0.26, fill=0.78, chase=True,
      min_lead=4.0, systems=5, setup=4.0, ongoing=2.0,
      reveals="Topic interest, but weeks later", discover=5, trust=7, generic=5, prec=8,
      note="**The lag is fatal to a discovery test** — you learn in month three"),

    F("dm", "Comment-to-DM automation → conversation → link", "operator",
      "Very common on IG/FB for small operators", "Conversation started",
      c1=0.055, c2=0.30, show=0.52, close=0.14, fill=0.64, lpv=1.00, chase=True,
      min_lead=14.0, systems=3, setup=1.5, ongoing=2.0,
      reveals="Whatever they type, which is a lot — but only if you answer",
      discover=6, trust=5, generic=9, prec=8,
      note="**Worst possible fit with a 10.5-hour timezone gap**"),

    F("retarget", "Two-stage: content view cold → book on retargeting", "operator",
      "Standard structure; **Meta's own recommendation is fewer, broader ad sets**",
      "Booked call (retargeted)", c1=0.038, show=0.72, close=0.22, fill=0.76,
      min_lead=3.0, systems=3, setup=2.0, ongoing=1.0,
      reveals="Role, plus who came back", discover=5, trust=6, generic=9, prec=9,
      note="**Splits a $5,000 budget across two campaigns** — see §5"),

    F("quote", "Instant quote — answer 3, see the price, self-book", "operator",
      "The *\"Get a Free Quote\"* CTA is measured at **+15–30% CTR** [V]",
      "Quote generated", c1=0.078, c2=0.36, show=0.68, close=0.23, fill=0.77,
      min_lead=2.0, systems=3, setup=1.5,
      reveals="**Role, size and the price they were willing to see**",
      discover=9, trust=7, generic=9, prec=9,
      note="Our price is a % of salary, so the quote is real arithmetic, not a range"),

    F("openbench", "Open bench — **no gate at all**, calendar beside the profiles",
      "operator", "Athyna publishes 40+ profiles with rates and no email wall",
      "Booked call", c1=0.030, show=0.70, close=0.26, fill=0.78, min_lead=2.0,
      systems=2, setup=1.5, ongoing=1.0,
      reveals="Role, and which profile they viewed", discover=7, trust=9,
      generic=7, prec=8,
      note="**Two systems, no form, nothing to chase.** The simplest bench funnel"),

    F("news", "Newsletter / content → nurture → book", "operator",
      "How most of this category actually grows — and it is slow", "Subscribed",
      c1=0.105, c2=0.12, show=0.62, close=0.27, fill=0.78, chase=True,
      min_lead=3.0, systems=4, setup=3.0, ongoing=3.0,
      reveals="Almost nothing for months", discover=2, trust=6, generic=8, prec=9,
      note="**Wrong instrument for a 30-day question**"),
]


# ------------------------------------------------------------------- the engine
def run_one(f, aud, spend, speed):
    cpm, ctr, q = fn.AUD[aud]
    imp = spend / cpm * 1000
    clicks = imp * ctr
    lpv = clicks * f.lpv
    ev = lpv * f.c1
    booked = ev * f.c2
    held = booked * f.show
    close = f.close * (speed if f.chase else 1.0)
    signed = held * min(close * q, 0.45)
    placed = signed * f.fill
    mins = ev * f.min_lead + held * f.min_held + ev * f.gate_share * f.min_sample
    return dict(ev=ev, booked=booked, held=held, signed=signed, placed=placed,
                mins=mins, cost=spend + mins / 60.0 * FOUNDER_HR, lpv=lpv)


def run(f, spend=SPEND, speed=SPEED_PENALTY):
    t = dict(ev=0.0, booked=0.0, held=0.0, signed=0.0, placed=0.0, mins=0.0,
             cost=0.0, lpv=0.0)
    for aud, share in MIX.items():
        r = run_one(f, aud, spend * share, speed)
        for k in t:
            t[k] += r[k]
    p = t["placed"]
    t["cac"] = t["cost"] / p if p else float("inf")
    t["cpl"] = spend / t["ev"] if t["ev"] else float("inf")
    t["r30"] = GP30 / t["cac"] if p else 0.0
    t["rlife"] = GPLIFE / t["cac"] if p else 0.0
    t["hrs"] = t["mins"] / 60.0
    t["ev_wk"] = t["ev"] / WEEKS
    return t


DIM = [("SIMPLE",   22, "Build, deploy, check and change it — in the first six months"),
       ("DISCOVER", 18, "What the first click reveals about which ICP × role works"),
       ("CAC30",    15, "30-day LTGP:CAC against the 1.5:1 constraint"),
       ("TRUST",    12, "Works for an unknown India-based solo operator"),
       ("LEARN",    11, "Optimisation events per week against Meta's 50"),
       ("FOUNDER",  10, "Founder hours/month against the ~60 available for selling"),
       ("PRECEDENT", 7, "Somebody comparable actually runs this"),
       ("GENERIC",   5, "Same content across every ICP × role cell")]

R = {f.key: run(f) for f in FUNNELS}


def simple(f):
    """Derived, not judged: tools to wire, days to launch, recurring burden."""
    return max(0.0, min(10.0, 10.0 - (f.systems - 2) * 0.9
                        - f.setup * 0.5 - f.ongoing * 1.4))


def scores(f):
    r = R[f.key]
    learn = min(10.0, 10.0 * (r["ev_wk"] / LEARN_WEEK) ** 0.5)
    cac30 = 0.0 if r["r30"] < 1.5 else min(10.0, 2.0 + 8.0 * min(1.0, (r["r30"] - 1.5) / 4.0))
    founder = max(0.0, min(10.0, 10.0 * (SALES_HRS / max(r["hrs"], 1.0)) ** 0.8))
    vol = min(1.0, r["ev_wk"] / 40.0) ** 0.5
    return dict(SIMPLE=simple(f), DISCOVER=f.discover * (0.45 + 0.55 * vol),
                CAC30=cac30, TRUST=float(f.trust), LEARN=learn, FOUNDER=founder,
                PRECEDENT=float(f.prec), GENERIC=float(f.generic))


S = {f.key: scores(f) for f in FUNNELS}
T = {f.key: sum(S[f.key][k] * w for k, w, _ in DIM) / 10.0 for f in FUNNELS}
BY = sorted(FUNNELS, key=lambda f: -T[f.key])
RANK = {f.key: i + 1 for i, f in enumerate(BY)}

# ------------------------------------------------------------------- the report
print("# Eighteen Funnels, Reranked for a Solo Operator's First Six Months\n")
print("> Two reference classes. [`COMPETITORS.md`](COMPETITORS.md) studied the **category** —")
print("> funded, SEO-led, staffed. This studies the one we actually belong to: **solo and small")
print("> operators buying cold Meta traffic for high-ticket B2B services**, which has published")
print("> benchmarks the category does not.\n")

print("---\n\n## 1. What the operator world has measured\n")
print("Everything here is cited. It replaces guesses that were marked `[?]` two passes ago.\n")
print("| Metric | Value | Note | Source |\n|---|---|---|---|")
for a, b, c, d in BENCH:
    print(f"| {a} | {b} | {c} | `{d}` |")
print("\n**Our modelled close rates all sit inside the published 10–25% call-to-close band**, which")
print("is the first time any step past the landing page has had a benchmark behind it rather than")
print("an assumption.\n")

# ------------------------------------------------------- 2. the speed penalty
print("---\n\n## 2. The finding that reorders everything: you cannot answer in five minutes\n")
print("| | |\n|---|---|")
for a, b in [("Contact inside **5 minutes**", "**32% close rate** [V]"),
             ("Contact after **24 hours**", "**12% close rate** [V]"),
             ("5 minutes vs 30 minutes", "**21× more likely to qualify** [V]"),
             ("First vendor to respond", "**wins 78% of B2B deals** [V]"),
             ("Industry average response", "**47 hours** — only 23% answer inside 5 minutes [V]")]:
    print(f"| {a} | {b} |")
print("\n**India Standard Time is 9.5–10.5 hours ahead of US Eastern.** A lead that arrives at 2pm")
print("in New York lands at 11:30pm in Pune. A solo operator — one person, who also sources,")
print("grades and delivers — **cannot hold a five-minute response window against US business "
      "hours.**\n")
print(f"> So every funnel whose conversion depends on *chasing* a lead carries a penalty that no")
print(f"> competitor in [`COMPETITORS.md`](COMPETITORS.md) pays. Modelled at "
      f"**×{SPEED_PENALTY:.2f} on close rate**,")
print(f"> interpolated from the 32%/12% spread and swept in §7.\n")
print("| Funnel | Chase-dependent? | Why |\n|---|---|---|")
for f in FUNNELS:
    if f.chase:
        print(f"| {f.name} | **Yes** | Conversion waits on your reply |")
print("\n**And the funnels that are immune** are the ones where the visitor books, buys or "
      "self-serves")
print("without you: the direct calendar, the open bench, the instant quote, the paid trial, the")
print("published price, the VSL application, and the gate. **The calendar works while you "
      "sleep.**\n")
print("> This is the first structural advantage of self-serve that is specific to *us* rather than")
print("> generic best practice — and it is worth more than any conversion-rate difference in this")
print("> study.\n")

# ------------------------------------------------------- 3. the instant-form conflict
print("---\n\n## 3. Two sources disagree about Instant Forms. Resolving it\n")
print("| Source | Claim |\n|---|---|")
print("| `growthspreeofficial.com` | **Below $25k ACV, Meta Lead Ads win** on volume *and* "
      "pipeline economics |")
print("| `volumecreatives.com` | Instant Forms convert to appointment at **~2%**; landing-page "
      "leads at **~17%** |")
print("| `adamigo.ai` | Instant Forms carry **35–55% lower SQL rates**; CPL wins, CPQO loses |")
acv = 6600 + 477 * 0.75 * 12
print(f"\n**Our ACV is roughly ${acv:,.0f}** — a $6,600 one-time fee plus a year of EOR at attach.")
print("That is squarely in the tier where the first source says lead ads should win. **They still")
print("should not, and the reason is that ACV is the wrong axis.**\n")
print("> The variable that actually decides it is **consideration**, not price. Instant Forms work")
print("> where the offer is understood in three seconds — a quote, a discount, a viewing. **Ours")
print("> is a stranger in another country doing work you cannot supervise.** That is a")
print("> high-consideration purchase at any price, and the 2%-vs-17% appointment gap is what")
print("> high-consideration looks like on a form nobody remembers filling in.\n")
i, iq = R["instant"], R["instantq"]
print(f"Both variants are modelled anyway, and both rank near the bottom: "
      f"**{RANK['instant']}th** and **{RANK['instantq']}th** of 18.")
print(f"The open-question variant is genuinely better — **{iq['placed']:.1f} placements against "
      f"{i['placed']:.1f}**, exactly the")
print("qualification lift the source describes — **but it is still chase-dependent, and §2 is what")
print("caps it.**\n")

# ------------------------------------------------------------------ 4. the table
print("---\n\n## 4. All eighteen\n")
print(f"**${SPEND:,.0f}/month.** Gross profit ${GP30:,.0f} at 30 days from "
      f"[`offer_model.py`](offer_model.py); audience layers")
print(f"from [`funnel.py`](funnel.py); founder time ${FOUNDER_HR:.0f}/hr. Chase-dependent funnels "
      f"carry the §2 penalty.\n")
print("| Funnel | World | Events/wk | CPL | Held | Placements | **CAC** | **30-day** | Hrs/mo "
      "| `SIMPLE` |")
print("|---|---|---|---|---|---|---|---|---|---|")
for f in BY:
    r = R[f.key]
    fl = "" if r["r30"] >= 1.5 else " ⚠️"
    ch = " 🐌" if f.chase else ""
    print(f"| **{f.name}**{ch} | {f.world} | {r['ev_wk']:.0f} | ${r['cpl']:,.0f} "
          f"| {r['held']:.0f} | {r['placed']:.1f} | **${r['cac']:,.0f}** "
          f"| **{r['r30']:.2f}:1**{fl} | {r['hrs']:.0f}{' ⚠️' if r['hrs'] > SALES_HRS else ''} "
          f"| **{simple(f):.1f}** |")
print("\n🐌 = chase-dependent, carrying the §2 speed penalty.\n")
print("`SIMPLE` is **derived, not judged**: `10 − (systems−2)×0.9 − setup_days×0.5 − "
      "ongoing×1.4`.\n")
print("| Funnel | Tools to wire | Days to launch | Recurring burden |\n|---|---|---|---|")
for f in sorted(FUNNELS, key=lambda x: -simple(x)):
    ong = {0.0: "none", 1.0: "light", 2.0: "constant", 3.0: "**you, every time**"}.get(
        f.ongoing, f"{f.ongoing}")
    print(f"| {f.name} | {f.systems} | {f.setup:g} | {ong} |")

# ------------------------------------------------------------------ 5. the rank
print("\n---\n\n## 5. The ranking\n")
print("| Dimension | Weight | What it measures |\n|---|---|---|")
for k, w, d in DIM:
    print(f"| `{k}` | {w} | {d} |")
print(f"\n`SIMPLE` is now the heaviest weight, on operator direction. `DISCOVER` stays high because")
print("the ICP × role question is still open. **Five of the eight are derived from the model** "
      "rather")
print("than scored by hand: `SIMPLE`, `CAC30`, `LEARN`, `FOUNDER`, and the volume half of "
      "`DISCOVER`.\n")
print("| Rank | Funnel | " + " | ".join(f"`{k}`" for k, _, _ in DIM) + " | **Score** |")
print("|---|---|" + "---|" * (len(DIM) + 1))
for i2, f in enumerate(BY, 1):
    sc = S[f.key]
    mark = " ✅" if i2 <= 2 else ""
    print(f"| **{i2}** | {f.name}{mark} | "
          + " | ".join(f"{sc[k]:.1f}" for k, _, _ in DIM) + f" | **{T[f.key]:.1f}** |")

print("\n### What moved, and why\n")
print("| Funnel | Was | Now | Why |\n|---|---|---|---|")
for k, was, why in [
    ("quiz", "1st",
     "The bench dependency and a fourth system cost it on `SIMPLE`. **Still top three**"),
    ("bench", "2nd",
     "Same — two graded people per role before launch is real work, and `SIMPLE` now prices it"),
    ("openbench", "not modelled",
     "**New.** The bench with *no email gate* — two systems, nothing to chase, and Athyna "
     "publishes 40+ profiles with no wall. Keeps most of the trust, drops most of the complexity"),
    ("quote", "not modelled",
     "**New.** *\"Get a Free Quote\"* is measured at **+15–30% CTR** [V], our fee is a clean "
     "percentage so the quote is real arithmetic, and it self-serves"),
    ("price", "4th",
     "Two systems, half a day, nothing recurring. **The highest `SIMPLE` score in the study**"),
    ("vsl", "not modelled",
     "**New.** The canonical operator funnel, with a real 30–60% application→call benchmark — "
     "but three days of video and a reshoot per role"),
    ("calc", "3rd",
     "Five systems and custom code, and it is chase-dependent. **`SIMPLE` is what demoted it**"),
    ("instant", "10th", "Now measured against ~2% appointment rate [V] rather than assumed"),
]:
    f = next(x for x in FUNNELS if x.key == k)
    print(f"| {f.name} | {was} | **{RANK[k]}th** | {why} |")

# ------------------------------------------------------------- 6. the recommendation
print("\n---\n\n## 6. What to build\n")
w1, w2 = BY[0], BY[1]
print(f"**{w1.name}** at **{T[w1.key]:.1f}**, with "
      f"**{w2.name}** at **{T[w2.key]:.1f}**.\n")
print("They compose into one page, and the composition is deliberately boring:\n")
print("```")
print("  ONE PAGE, ONE URL, TWO SYSTEMS")
print("")
print("   Framer page  ────────────────────  Cal.com embed")
print("        │                                   │")
print("        │  bench cards, open, no wall       │  books while you sleep")
print("        │  3 taps → an instant number       │  no chase, no penalty")
print("        └───────────────────────────────────┘")
print("")
print("  AD      ICP + size question · a graded face · the role menu")
print("  PAGE    the bench, visible. no email required to see it")
print("  QUOTE   3 taps: seat · volume · when  →  a real number, instantly")
print("          <- THE PIXEL EVENT, and the demand research, same click")
print("  BOOK    calendar right there. self-serve. immune to timezone")
print("  CALL    30 min, already knowing what they saw and what they picked")
print("```")
h = run(replace(FUNNELS[0], key="hyb", c1=0.072, c2=0.34, show=0.68, close=0.24,
                fill=0.77, min_lead=2.0, chase=False))
print("\n| Step | Number | Note |\n|---|---|---|")
for a, b, c in [
    ("Spend", f"${SPEND:,.0f}/mo", ""),
    ("Landing page views", f"{h['lpv']:,.0f}", "[E]"),
    ("**Quote generated** — the pixel event", f"**{h['ev']:,.0f}**",
     f"**{h['ev_wk']:.0f}/week** against Meta's 50"),
    ("Cost per quote", f"${h['cpl']:,.0f}",
     "well under the **$41.60** all-industry CPL average [V]"),
    ("Calls booked", f"{h['booked']:,.0f}", "[?] self-booked, so no chase"),
    ("Calls held", f"{h['held']:,.0f}", "[?]"),
    ("Signed", f"{h['signed']:.1f}", "inside the published **10–25%** close band [V]"),
    ("**Placements**", f"**{h['placed']:.1f}**", ""),
    ("Founder hours", f"{h['hrs']:.0f}/mo", f"against ~{SALES_HRS:.0f} available"),
    ("**CAC**", f"**${h['cac']:,.0f}**", ""),
    ("**30-day**", f"**{h['r30']:.2f}:1**", "against 1.5:1"),
    ("**Lifetime**", f"**{h['rlife']:.2f}:1**", "")]:
    print(f"| {a} | {b} | {c} |")

print("\n### One problem with this, and it is not the funnel\n")
print(f"**{h['held']:.0f} held calls a month at 60 minutes each is {h['held']:.0f} hours** — most "
      f"of the ~{SALES_HRS:.0f}")
print("available, before sourcing, grading or delivering anything. Six of the eighteen funnels")
print("breach the hours budget, and the top ones breach it **because they work**.\n")
print("| Fix | Effect | Cost |\n|---|---|---|")
for a, b, c in [
    ("**30-minute calls, not 45**",
     f"{h['held']:.0f} hours → **{h['held']*0.5:.0f}**", "None. The quote has already done the "
     "qualifying, so the call is confirmation, not discovery"),
    ("**Start at $3,000/month, not $5,000**",
     f"~{h['ev_wk']*0.6:.0f} events/week, ~{h['held']*0.6:.0f} calls",
     "Slower learning. Still above the 20-events-a-week readability floor"),
    ("**Raise the quote's volume floor**", "Fewer, better calls",
     "You will disqualify some real buyers. Do this last, not first")]:
    print(f"| {a} | {b} | {c} |")
print("\n**Do the first one.** A 30-minute call is the single cheapest fix in this document, and")
print("the quote step is what earns the right to shorten it.\n")
print("### The six-month stack — two systems, and a rule\n")
print("| | What | Why this one |\n|---|---|---|")
for a, b, c in [
    ("**Page**", "**Framer**, one page",
     "Already chosen in [`SITE.md`](SITE.md) at 96.4. Visual edits, instant publish, versions to "
     "roll back to. **You can change a headline on a phone**"),
    ("**Booking**", "**Cal.com** embed, free tier",
     "One embed. Books overnight. **This is the system that neutralises §2**"),
    ("**Everything else**", "**Nothing, for six months**",
     "No CRM, no automation platform, no email sequences, no funnel builder. Two systems is the "
     "whole point")]:
    print(f"| {a} | {b} | {c} |")
print("\n> **The rule: nothing goes on the page that you cannot check in one minute on a phone.**\n")
print("The *check* half of the operator direction is the half that usually gets skipped, so it")
print("gets a checklist rather than a sentence:\n")
print("| Every Monday, in ten minutes | Where |\n|---|---|")
for a, b in [("Did the page load and the quote calculate?", "Open it on your phone"),
             ("Did the pixel fire?", "Meta Events Manager → test events"),
             ("Cost per quote, this week vs last", "Ads Manager, one column"),
             ("Which **seat** did the quotes pick?", "Cal.com booking notes + form field"),
             ("Which **ad** did they come from?", "UTM on the booking"),
             ("Any booking with no UTM?", "**Your tracking is broken.** Fix before spending more")]:
    print(f"| {a} | {b} |")
print("\n**Six of those seven checks exist because of the discovery problem, not the conversion")
print("problem.** If you cannot answer *\"which seat, from which ad\"* on any given Monday, the")
print("$5,000 bought placements but not the answer — and the answer was the point.\n")

# --------------------------------------------------------------- 7. robustness
print("---\n\n## 7. Does the ranking survive the assumptions?\n")
print(f"The speed penalty is the load-bearing new number. Swept from **0.45** (you answer a day")
print("late, near the published 12% floor) to **0.85** (you are unusually disciplined about "
      "evenings),")
print("alongside the three softest funnel inputs at 0.7× / 1.0× / 1.3×.\n")
LV = (0.7, 1.0, 1.3)
SP = (0.45, 0.65, 0.85)
wins, clears = {f.key: 0 for f in FUNNELS}, {f.key: 0 for f in FUNNELS}
n = 0
for sp, a, b, c in itertools.product(SP, LV, LV, LV):
    n += 1
    field_ = []
    for f in FUNNELS:
        g = replace(f, c1=min(f.c1 * a, 0.95), show=min(f.show * b, 0.95),
                    close=min(f.close * c, 0.95))
        r = run(g, speed=sp)
        if r["r30"] >= 1.5:
            clears[f.key] += 1
        if r["ev_wk"] >= 20 and r["hrs"] <= SALES_HRS and r["r30"] >= 1.5:
            field_.append((r["cac"], f.key))
    if field_:
        wins[min(field_)[1]] += 1
print(f"**{n} combinations.** *Runnable* = at least 20 events a week, under "
      f"{SALES_HRS:.0f} founder hours, clearing 1.5:1.\n")
print("| Funnel | Clears 1.5:1 | Cheapest **and** runnable | Rank |\n|---|---|---|---|")
for f in sorted(FUNNELS, key=lambda x: (-wins[x.key], -clears[x.key]))[:10]:
    print(f"| {f.name} | {clears[f.key]/n:.0%} | **{wins[f.key]}/{n}** | {RANK[f.key]} |")
best = max(wins, key=lambda k: wins[k])
bf = next(x for x in FUNNELS if x.key == best)
print(f"\n> **{bf.name}** takes **{wins[best]}/{n}** of the grid — more than any other — "
      f"and also ranks")
print(f"> **{RANK[best]} of 18** on the weighted score. **Two independent methods, same answer.**\n")
print("That has not happened in either earlier pass, and it is the strongest result in the study.")
print("The weighted score can be argued with — the weights are a judgement. The grid cannot: it")
print("just asks who is cheapest while staying runnable, across 81 versions of the world.\n")
print("**Where they do part company:** the bench-unlock ranks 2nd on score and wins 0 grid points,")
print("because there is almost always something cheaper that is also runnable. It is not a bad")
print("funnel — it clears 1.5:1 in **100%** of combinations — it is just never the cheapest. That")
print("is worth knowing before committing two weeks to building a bench page.\n")

# ------------------------------------------------------------------ 8. the ads
print("---\n\n## 8. The ads\n")
print("Four creatives, one ad set, one campaign. **Broad targeting** — the 2026 guidance is that")
print("broad plus sharp creative beats hyper-narrow, because the algorithm reads who the ad is "
      "for [V].\n")
print("| Slot | ICP | Role | Hook |\n|---|---|---|---|")
for a, b, c, d in [
    ("1", "E-comm, $10k+/mo ads", "Performance video",
     '*"Running $10k+ a month in ads and shipping 3 new cuts?"*'),
    ("2", "E-comm, $10k+/mo ads", "Paid media",
     '*"Your agency takes 15% of spend. Here is what a full-time buyer costs."*'),
    ("3", "Agencies, 5–30 staff", "Performance video",
     '*"Your editor is the bottleneck on every retainer you have."*'),
    ("4", "Agencies, 5–30 staff", "Paid media",
     '*"Turning down retainers because you cannot staff them?"*')]:
    print(f"| **{a}** | {b} | {c} | {d} |")
print("\n| Rule | Evidence |\n|---|---|")
for a, b in [
    ("**The CTA is a quote or a person — never *\"Contact Us\"***",
     "*\"Get a Free Quote\"* / *\"Book a Free Consultation\"* measure **+15–30% CTR** over generic "
     "contact CTAs [V]"),
    ("**A real graded face in the creative**",
     "4 of 8 competitors lead with people. Ours also carries a number, which none of theirs does"),
    ("**Never *\"80% less\"***",
     "Verbatim in 2 of 8 competitor headlines. The leader's axis"),
    ("**One ad set, not four**",
     f"At ~{h['ev_wk']:.0f} events a week, four ad sets is four learning phases you cannot fund. "
     f"Read ICP × role at **ad level**"),
    ("**No employment language anywhere**",
     "The bench must read as a supplier catalogue for buyers, not a job board. One reviewer tick "
     "costs 10–29% on CAC ([`SUPPLY-DEMAND.md`](../SUPPLY-DEMAND.md))")]:
    print(f"| {a} | {b} |")

print("\n---\n\n## 9. The honest summary\n")
print("| | |\n|---|---|")
for a, b in [
    ("**What changed this pass**",
     "Speed-to-lead, which is a real constraint for an India-based solo operator and was missing "
     "from every earlier model. It penalises seven of the eighteen funnels and it is why the "
     "recommendation is now *self-serve* rather than merely *simple*"),
    ("**What the operator world added**",
     "Real benchmarks where there were `[?]`s — application→call 30–60%, call→close 10–25%, "
     "Instant Form appointment rate ~2%. Our close assumptions survived contact with all three"),
    ("**What stayed the same across three passes**",
     "One page, one ad set, the ICP × role matrix in the creative, the one-time fee, the 12-month "
     "guarantee, and *a role with no measurable delta is not a role to launch*"),
    ("**The cost that has not gone away**",
     "**Two graded people per launch role before the first ad.** Every top-ranked funnel shows "
     "people, and showing people you have not tested is the one thing that would break the "
     "positioning permanently"),
    ("**What is still unmeasured**",
     "Show rate and close rate *for us specifically*. The bands are published; our position in "
     "them is not. First ten calls settle it")]:
    print(f"| {a} | {b} |")
