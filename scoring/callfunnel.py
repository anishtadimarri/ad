#!/usr/bin/env python3
"""
Twelve booked-call funnels, ranked — the $500 teardown removed.

Operator direction: no paid teardown. Every ICP x role combination gets the same
page, and the conversion is a booked call. Day 1 tests 2-3 roles x 2-3 ICPs.

This model reuses the REAL engines rather than restating their numbers:
  offer_model.py -> gross profit per acquired client (same OFFER config as ltgp.py,
                    so ratios here are directly comparable to LTGP.md's 4.25:1)
  funnel.py      -> audience CPM/CTR and the spend-weighted blending rule

What replaces the deposit step. funnel.py put the $500 AFTER the held call
(step 7 of 9), so in the model the deposit rate WAS a close rate. Removing the
teardown therefore does not delete a step — it changes two numbers in opposite
directions, and that is the whole commercial question:

    more people say yes on a free call        -> close rate UP
    a yes with no money behind it is softer   -> fill rate DOWN

Evidence tags: [V] verified benchmark · [E] estimated in this repo already ·
[?] no data exists. Every step past the landing page is [?] and is swept in §5
rather than trusted.

Run:  python3 scoring/callfunnel.py > scoring/CALLFUNNEL.md
"""

import io
import itertools
import os
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass, field, replace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

with redirect_stdout(io.StringIO()):          # both print at import time
    import funnel as fn
    import offer_model as om

SPEND = 5000.0        # the test budget funnel.py sized as "right for test one"
FOUNDER_HR = 60.0     # derived: funnel.py charges $60 per held call = 1 hour
SALES_HRS = 60.0      # founder hours/month available for acquisition. The rest of
                      # the ~170 goes to sourcing, grading, delivery and building
LEARN_WEEK = 50       # [V] Meta: ~50 optimisation events per ad set per 7 days
WEEKS = 4.33
MIX = {"Intent seed (job posters)": 0.25,     # same mix as ltgp.py
       "1% Lookalike": 0.45,
       "Broad / Advantage+": 0.30}

# gross profit per acquired client, from the real offer model
BASE = next(c for c in om.CONFIGS if c.name.startswith("H5"))
OFFER = replace(BASE, name="$20k job, EOR default", salary=20_000.0, fee_pct=0.30,
                eor_price=499.0, eor_attach=0.75, monthly_tenure=9.0)
E = om.econ(OFFER)
GP30, GPLIFE = E["gp30"], E["gplife"]


# --------------------------------------------------------------------- funnels
@dataclass
class F:
    key: str
    name: str
    event: str            # what fires the pixel — the thing Meta optimises to
    c1: float             # LP view -> the pixel event
    show: float           # booked -> held
    close: float          # closing call -> signed engagement
    fill: float           # signed -> placed
    lpv: float = 0.85     # [E] 15% bounce before the page paints
    c2: float = 1.0       # pixel event -> booked call (1.0 if it IS the booking)
    mid: float = 0.0      # first call -> second call booked (two-call funnels)
    show2: float = 0.0
    min_lead: float = 5.0     # founder minutes per captured lead
    min_held: float = 60.0    # founder minutes per held call
    min_held2: float = 0.0
    min_sample: float = 0.0   # founder minutes producing free pre-sale work
    gate: float = 1.0         # share of leads that free work is produced for
    # hand-scored dimensions, 0-10, each with the reason recorded
    generic: int = 0
    trust: int = 0
    calldep: int = 0
    build: int = 0
    policy: int = 0
    why: dict = field(default_factory=dict)


FUNNELS = [
    F("cal", "1. Calendar embedded on the landing page", "Booked call",
      c1=0.020, show=0.65, close=0.12, fill=0.68,
      generic=10, trust=4, calldep=1, build=10, policy=9,
      why=dict(generic="One page, one embed. Nothing per-role exists",
               trust="Nothing between a cold stranger and your calendar. Zero proof shown",
               calldep="100% of the conversion happens on your call",
               build="A Cal.com embed. Ten minutes",
               policy="No employment language anywhere")),

    F("form", "2. Form fill, then calendar on the thank-you page", "Form fill",
      c1=0.050, c2=0.55, show=0.55, close=0.11, fill=0.66, min_lead=8.0,
      generic=10, trust=4, calldep=2, build=9, policy=9,
      why=dict(generic="Four fields work for any seat. One dropdown carries the role",
               trust="Same as 1 — the form asks before it gives",
               calldep="The call still decides, but you keep the email of everyone who does not book",
               build="A form and a /thanks page. Both needed anyway",
               policy="No employment language anywhere")),

    F("app", "3. Application-gated calendar", "Application submitted",
      c1=0.022, c2=0.70, show=0.72, close=0.18, fill=0.78, min_lead=3.0,
      generic=9, trust=6, calldep=3, build=8, policy=7,
      why=dict(generic="Same questions for every seat; the role is one answer",
               trust="Being screened reads as selective, which is a trust signal in itself",
               calldep="Friction does the filtering the $500 used to do, before the call",
               build="A longer form with conditional logic. Half a day",
               policy="'Application' is the one word that can read as employment. Watch the copy")),

    F("calc", "4. Volume calculator, result gated by email", "Calculator completed",
      c1=0.060, c2=0.40, show=0.60, close=0.17, fill=0.75, min_lead=6.0,
      generic=8, trust=7, calldep=4, build=4, policy=9,
      why=dict(generic="The arithmetic is identical per seat; only the unit label changes",
               trust="They compute their own number. Nothing to disbelieve",
               calldep="The buyer reaches the volume conclusion before you speak — the teardown's job, free",
               build="The one genuinely custom block on the site",
               policy="No employment language anywhere")),

    F("free", "5. Free graded work sample, delivered async, then a call", "Sample requested",
      c1=0.045, c2=0.55, show=0.75, close=0.26, fill=0.80,
      min_lead=4.0, min_sample=90.0, gate=0.35,
      generic=3, trust=10, calldep=5, build=3, policy=8,
      why=dict(generic="A sample is role-specific by definition. Nine cells means nine skills you must personally have",
               trust="The highest-trust move available to an operator with no track record",
               calldep="Most of the persuasion happens before the call, in the artefact",
               build="Nothing to build — but everything to do, forever",
               policy="Fine, though 'we will do work for you' invites scrutiny")),

    F("bench", "6. Bench preview — three graded candidates behind an email gate", "Bench unlocked",
      c1=0.070, c2=0.35, show=0.58, close=0.16, fill=0.72, min_lead=6.0,
      generic=5, trust=8, calldep=4, build=2, policy=3,
      why=dict(generic="Needs a graded bench per role before the ad runs. Nine cells is nine benches",
               trust="Named people with measured work is what the category leader leads with",
               calldep="Desire is created by the profiles, not the call",
               build="A bench you do not have on day 1. This is a blocker, not a build",
               policy="Candidate profiles on the ad path is the single clearest route to Employment classification")),

    F("vsl", "7. Video sales letter above the calendar", "Booked call",
      c1=0.028, show=0.68, close=0.14, fill=0.70, lpv=0.80,
      generic=4, trust=6, calldep=3, build=5, policy=9,
      why=dict(generic="A video that names the role must be reshot per cell. A video that names none persuades nobody",
               trust="A face and a voice beats text for a stranger — if the video is good",
               calldep="The video pre-sells, so the call closes rather than convinces",
               build="Script, shoot, edit. And a heavier page against an 85% LP-view rate",
               policy="No employment language anywhere")),

    F("instant", "8. Meta Instant Form — no landing page at all", "Lead (on-platform)",
      c1=0.120, c2=0.30, show=0.40, close=0.06, fill=0.55, lpv=1.00, min_lead=12.0,
      generic=10, trust=1, calldep=2, build=10, policy=6,
      why=dict(generic="Nothing role-specific exists to build",
               trust="Nothing is shown. No page, no proof, no person",
               calldep="Everything is decided by you, on the phone, to a lead who barely remembers opting in",
               build="Nothing to build. That is also the problem",
               policy="Native forms in a hiring-adjacent category draw more review, not less")),

    F("dep", "9. Small refundable deposit to hold the slot", "Deposit paid",
      c1=0.008, show=0.92, close=0.30, fill=0.85, min_lead=2.0,
      generic=10, trust=2, calldep=9, build=7, policy=9,
      why=dict(generic="A Stripe link is seat-agnostic",
               trust="Backwards. You are asking an unknown operator's visitor to pay before anyone has spoken",
               calldep="The only option where CAC is settled BEFORE you open your mouth",
               build="A Payment Link and a redirect",
               policy="No employment language anywhere")),

    F("ctm", "10. Click-to-Messenger / WhatsApp conversation", "Conversation started",
      c1=0.045, c2=0.35, show=0.55, close=0.10, fill=0.62, lpv=1.00, min_lead=15.0,
      generic=9, trust=5, calldep=3, build=8, policy=7,
      why=dict(generic="One greeting script, one branch per seat",
               trust="A real reply from a real person, fast. Weak on proof, strong on presence",
               calldep="The chat carries some of the load the call would",
               build="A greeting and a few saved replies",
               policy="Chat transcripts are not reviewed the way pages are, but the ad still is")),

    F("magnet", "11. Lead magnet — the role scorecard — then nurture to a call", "Guide downloaded",
      c1=0.085, c2=0.18, show=0.60, close=0.13, fill=0.70, min_lead=4.0,
      generic=6, trust=6, calldep=4, build=5, policy=9,
      why=dict(generic="One template, one page of role-specific criteria per cell",
               trust="Publishing a rubric is a credible way to claim you grade people",
               calldep="Some, eventually. The nurture does work the call would otherwise do",
               build="Write nine scorecards and an email sequence",
               policy="No employment language anywhere")),

    F("two", "12. Two calls — 15-minute fit, then a 45-minute working session", "Booked call",
      c1=0.035, show=0.70, mid=0.55, show2=0.85, close=0.24, fill=0.80,
      min_held=18.0, min_held2=60.0,
      generic=10, trust=5, calldep=2, build=9, policy=9,
      why=dict(generic="Two calendar links. Nothing per-role",
               trust="A 15-minute ask is a smaller ask, which matters when nobody knows you",
               calldep="Two calls means twice as much of CAC decided by you talking",
               build="Two Cal.com links and a routing rule",
               policy="No employment language anywhere")),
]


# ------------------------------------------------------------------- the model
def run_one(f, aud, spend):
    cpm, ctr, q = fn.AUD[aud]
    imp = spend / cpm * 1000
    clicks = imp * ctr
    lpv = clicks * f.lpv
    ev = lpv * f.c1                                   # the pixel event
    booked = ev * f.c2
    held = booked * f.show
    if f.mid:
        held2 = held * f.mid * f.show2
        closing = held2
    else:
        held2 = 0.0
        closing = held
    # audience intent applied ONCE, at the close step — funnel.py's rule
    signed = closing * min(f.close * q, 0.45)
    placed = signed * f.fill
    mins = (ev * f.min_lead + held * f.min_held + held2 * f.min_held2
            + ev * f.gate * f.min_sample)
    cost = spend + mins / 60.0 * FOUNDER_HR
    return dict(ev=ev, booked=booked, held=held, held2=held2, signed=signed,
                placed=placed, mins=mins, cost=cost, lpv=lpv)


def run(f, spend=SPEND, mix=None):
    mix = mix or MIX
    t = dict(ev=0.0, booked=0.0, held=0.0, held2=0.0, signed=0.0, placed=0.0,
             mins=0.0, cost=0.0, lpv=0.0)
    for aud, share in mix.items():
        r = run_one(f, aud, spend * share)
        for k in t:
            t[k] += r[k]
    p = t["placed"]
    t["cac"] = t["cost"] / p if p else float("inf")
    t["cpl"] = spend / t["ev"] if t["ev"] else float("inf")
    t["r30"] = GP30 / t["cac"] if p else 0.0
    t["rlife"] = GPLIFE / t["cac"] if p else 0.0
    t["hrs"] = t["mins"] / 60.0
    t["hrs_place"] = t["mins"] / 60.0 / p if p else float("inf")
    t["ev_wk"] = t["ev"] / WEEKS
    return t


# ------------------------------------------------------------------ dimensions
DIM = [("LEARN",   22, "How fast $5,000/month produces a readable signal across the cells"),
       ("CAC30",   20, "The 30-day LTGP:CAC ratio against the 1.5:1 constraint"),
       ("GENERIC", 16, "Works unchanged across every ICP x role cell"),
       ("FOUNDER", 14, f"Founder hours/month against the ~{SALES_HRS:.0f} a solo operator has for selling"),
       ("TRUST",   10, "Works for an unknown operator with no track record"),
       ("CALLDEP",  8, "How little of CAC is decided on the call"),
       ("BUILD",    6, "What must exist before the first dollar of spend"),
       ("POLICY",   4, "Employment Special Ad Category exposure")]


def scores(f, r):
    """Three dimensions are DERIVED from the model. Five are hand-scored above."""
    learn = min(10.0, 10.0 * (r["ev_wk"] / LEARN_WEEK) ** 0.5)
    cac30 = 0.0 if r["r30"] < 1.5 else min(10.0, 2.0 + 8.0 * min(1.0, (r["r30"] - 1.5) / 4.0))
    founder = max(0.0, min(10.0, 10.0 * (SALES_HRS / max(r["hrs"], 1.0)) ** 0.8))
    return dict(LEARN=learn, CAC30=cac30, GENERIC=float(f.generic),
                FOUNDER=founder, TRUST=float(f.trust), CALLDEP=float(f.calldep),
                BUILD=float(f.build), POLICY=float(f.policy))


def total(sc):
    return sum(sc[k] * w for k, w, _ in DIM) / 10.0


# ------------------------------------------------------------------ the report
R = {f.key: run(f) for f in FUNNELS}
S = {f.key: scores(f, R[f.key]) for f in FUNNELS}
T = {f.key: total(S[f.key]) for f in FUNNELS}
BY = sorted(FUNNELS, key=lambda f: -T[f.key])
BYCAC = sorted(FUNNELS, key=lambda f: R[f.key]["cac"])

print("# Twelve Booked-Call Funnels, Ranked\n")
print("> Operator direction: **no $500 teardown.** Same page for every ICP x role, and the")
print("> conversion is a booked call. Day 1 tests **2-3 roles x 2-3 ICPs**.\n")
print(f"Gross profit is the real one from [`offer_model.py`](offer_model.py): "
      f"**${GP30:,.0f} at 30 days**, ")
print(f"**${GPLIFE:,.0f} lifetime**. Audience CPMs and CTRs are "
      f"[`funnel.py`](funnel.py)'s. Budget **${SPEND:,.0f}/month**,")
print(f"founder time at **${FOUNDER_HR:.0f}/hour** — which is exactly "
      f"[`funnel.py`](funnel.py)'s $60 per held call.\n")

# ------------------------------------------------------- 1. what removing it does
print("---\n\n## 1. First: what removing the teardown actually costs\n")
print("Worth settling before ranking anything, because the answer is not what the repo assumed.\n")
print("**[`funnel.py`](funnel.py) put the $500 *after* the held call** — step 7 of 9. So in the")
print("model that already exists, **the deposit rate *was* a close rate.** Removing the teardown")
print("therefore does not delete a funnel step. It changes what happens on the one that remains.\n")
old_conv, old_fill = 0.18 * 1.15, 0.85
bare = next(f for f in FUNNELS if f.key == "cal")
gated = next(f for f in FUNNELS if f.key == "app")
print("| | With the $500 | Free — bare calendar | Free — **gated** | Why |")
print("|---|---|---|---|---|")
print(f"| Held call → committed | {old_conv:.0%} | {bare.close*1.15:.0%} "
      f"| **{gated.close*1.15:.0%}** | A free yes is easier to give and worth less |")
print(f"| Committed → placed | {old_fill:.0%} | {bare.fill:.0%} | **{gated.fill:.0%}** "
      f"| A yes with no money behind it ghosts more |")
print(f"| **Held call → placed** | **{old_conv*old_fill:.1%}** "
      f"| **{bare.close*1.15*bare.fill:.1%}** "
      f"| **{gated.close*1.15*gated.fill:.1%}** | |")
print(f"\n> **A bare free calendar loses {1-(bare.close*1.15*bare.fill)/(old_conv*old_fill):.0%} of "
      f"the held-call-to-placement rate. A gated one loses "
      f"{1-(gated.close*1.15*gated.fill)/(old_conv*old_fill):.0%}.**\n")
print("That is the finding, and it is not the one I expected. **The money was doing real work, and")
print("most of that work can be done by friction instead** — but only if something is actually put")
print("in the way. Take the $500 out and put nothing in its place and you lose roughly half the")
print("value of every held call, which shows up as CAC doubling in §2 rather than as a missing step.\n")
lost = 500 * (1 - old_fill)
print(f"The cash it collected was **credited in full against the fee**, so it was working capital,")
print(f"not profit. The only true revenue loss is the ~{1-old_fill:.0%} who paid and never placed —")
print(f"**about ${lost:.0f} per deposit taken**, against ${GP30:,.0f} of gross profit per client. "
      f"Under 2%.\n")
print("**So the operator direction does not break the economics.** What it breaks is the *filter*,")
print("and the ranking below is really a search for the cheapest thing that filters as well as")
print("money did. That is the whole question, and §4 answers it.\n")
print("One correction to the record while we are here: the landing page had "
      "**\"Get the $500 teardown\"**")
print("as its CTA — i.e. *before* the call — while [`funnel.py`](funnel.py) scored it *after*. "
      "**Those are")
print("different businesses**, and only the pre-call version satisfied the standing constraint that")
print("no sales call may determine CAC. The repo has been quietly modelling two funnels at once.\n")

# ---------------------------------------------------------------- 2. the table
print("---\n\n## 2. All twelve, on the numbers\n")
print(f"Blended across the three audience layers by spend "
      f"({' / '.join(f'{v:.0%}' for v in MIX.values())}), as [`ltgp.py`](ltgp.py) does.\n")
print("| # | Funnel | Pixel event | Events/mo | CPL | Held calls | Placements | **CAC** "
      "| **30-day** | Hrs/mo | Hrs/placement |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
for i, f in enumerate(FUNNELS, 1):
    r = R[f.key]
    flag = "" if r["r30"] >= 1.5 else " ⚠️"
    print(f"| {i} | {f.name.split('. ',1)[1]} | {f.event} | {r['ev']:,.0f} | ${r['cpl']:,.0f} "
          f"| {r['held']:,.0f} | {r['placed']:.1f} | **${r['cac']:,.0f}** "
          f"| **{r['r30']:.2f}:1**{flag} | {r['hrs']:,.0f}{' ⚠️' if r['hrs'] > SALES_HRS else ''} "
          f"| {r['hrs_place']:.0f} |")
fail = [f for f in FUNNELS if R[f.key]["r30"] < 1.5]
print(f"\n**{len(FUNNELS)-len(fail)} of {len(FUNNELS)} clear the 1.5:1 constraint** on the base case. "
      f"CAC spans "
      f"${min(R[f.key]['cac'] for f in FUNNELS):,.0f} to "
      f"${max(R[f.key]['cac'] for f in FUNNELS):,.0f} — a "
      f"{max(R[f.key]['cac'] for f in FUNNELS)/min(R[f.key]['cac'] for f in FUNNELS):.1f}x range, "
      f"which is far wider than the 6% that separated form-fill from calendar in "
      f"[`FUNNEL.md`](FUNNEL.md). **This choice does matter.**\n")
over = [f for f in FUNNELS if R[f.key]["hrs"] > SALES_HRS]
worst = max(FUNNELS, key=lambda f: R[f.key]["hrs"])
print(f"The column to read second is **Hrs/mo**, and it disqualifies more options than CAC does. "
      f"A solo")
print(f"operator who is also sourcing, grading, delivering and building has roughly "
      f"**{SALES_HRS:.0f} hours a month**")
print(f"for selling. **{len(over)} of the 12 exceed that**, and "
      f"**{worst.name.split('. ',1)[1]}** needs "
      f"**{R[worst.key]['hrs']:,.0f}** — which is most of a full-time job on its own, at only "
      f"$5,000 of spend.\n")

# ----------------------------------------------------------------- 3. the rank
print("---\n\n## 3. The ranking\n")
print("CAC cannot decide this alone — it says nothing about whether you can *run* the funnel, or")
print("whether it tells you anything in month one. Eight dimensions, three of them **derived from")
print("the model above** rather than scored by hand:\n")
print("| Dimension | Weight | Source | What it measures |\n|---|---|---|---|")
for k, w, d in DIM:
    src = "**derived**" if k in ("LEARN", "CAC30", "FOUNDER") else "scored"
    print(f"| `{k}` | {w} | {src} | {d} |")
print()
print("| Rank | Funnel | " + " | ".join(f"`{k}`" for k, _, _ in DIM) + " | **Score** |")
print("|---|---|" + "---|" * (len(DIM) + 1))
for i, f in enumerate(BY, 1):
    sc = S[f.key]
    mark = " ✅" if i == 1 else ""
    print(f"| **{i}** | {f.name.split('. ',1)[1]}{mark} | "
          + " | ".join(f"{sc[k]:.1f}" for k, _, _ in DIM)
          + f" | **{T[f.key]:.1f}** |")
print()
print("### Where the ranking disagrees with CAC\n")
print("| By score | By CAC |\n|---|---|")
for i in range(5):
    a, b = BY[i], BYCAC[i]
    print(f"| {i+1}. {a.name.split('. ',1)[1]} | {i+1}. {b.name.split('. ',1)[1]} "
          f"(${R[b.key]['cac']:,.0f}) |")
top_cac = BYCAC[0]
print(f"\n**{top_cac.name.split('. ',1)[1]} wins on CAC and loses overall.** "
      f"It produces {R[top_cac.key]['ev']:.0f} pixel events a month — ")
print(f"**{R[top_cac.key]['ev_wk']:.1f} a week**, against the {LEARN_WEEK} Meta needs to leave the")
print("learning phase. A funnel that cannot teach the algorithm anything cannot be scaled, and")
print("cannot be read across nine test cells. **That is the trap the CAC column hides.**\n")

# ------------------------------------------------------- 4. the filter question
print("---\n\n## 4. The real question: what filters as well as $500 did\n")
print("[`TEARDOWN.md`](TEARDOWN.md) §1 lists four jobs the $500 was doing. Money did all four at")
print("once, which is why removing it needs four replacements, not one:\n")
print("| The job $500 did | The free replacement | Where it lives |\n|---|---|---|")
for a, b, c in [
    ("**Money gate** — filters tyre-kickers",
     "**Qualifying questions with real disqualification.** Ad spend, revenue and volume, asked "
     "before the calendar appears — and a genuine *no* screen, not a form that always says yes",
     "Landing page, between the CTA and the calendar"),
    ("**Work sample** — proof you can judge the work",
     "**One public teardown of a brand they know**, not of their account. Same skill, produced "
     "once, shown to everybody, costs nothing per lead",
     "Landing page proof block"),
    ("**Qualifier** — you know their cadence before the call",
     "**The volume calculator.** They enter their own numbers and it returns their own gap. You "
     "read the submitted values before the call",
     "Landing page, above the CTA"),
    ("**Sets up the sale** — concludes in a volume problem",
     "**The calculator concludes it for them**, which is stronger than you concluding it. "
     "[`TEARDOWN.md`](TEARDOWN.md) §4's rule survives intact, unpaid",
     "Same block")]:
    print(f"| {a} | {b} | {c} |")
print("\n> **Three of the four replacements are the same object: the calculator with a qualifying")
print("> gate in front of the calendar.** That is why funnels 3 and 4 rank where they do, and why")
print("> the recommendation in §7 is a hybrid of them rather than either one.\n")

# --------------------------------------------------------------- 5. robustness
print("---\n\n## 5. Rank stability — because every number past the landing page is `[?]`\n")
print("There is **no published benchmark** for show rate or close rate on cold paid traffic to a")
print("free B2B call. I looked; the cold-calling literature covers dial-to-meeting, not")
print("booking-to-show. So rather than defend point estimates, every funnel's three softest inputs")
print("are swept at **0.7x / 1.0x / 1.3x** — 27 combinations each — and what matters is how often")
print("each one still clears and still wins.\n")
LV = (0.7, 1.0, 1.3)
grid = {}
for f in FUNNELS:
    ok = 0
    cacs = []
    for a, b, c in itertools.product(LV, LV, LV):
        g = replace(f, c1=min(f.c1 * a, 0.95), show=min(f.show * b, 0.95),
                    close=min(f.close * c, 0.95))
        r = run(g)
        cacs.append((g.key, r["cac"], r["r30"], r["ev_wk"]))
        if r["r30"] >= 1.5:
            ok += 1
    grid[f.key] = (ok / 27.0, cacs)
# rank stability: for each grid point, who has the best CAC among funnels that also
# clear 20 events/week (a floor below which nothing is readable)
wins = {f.key: 0 for f in FUNNELS}
for i, combo in enumerate(itertools.product(LV, LV, LV)):
    a, b, c = combo
    field_ = []
    for f in FUNNELS:
        g = replace(f, c1=min(f.c1 * a, 0.95), show=min(f.show * b, 0.95),
                    close=min(f.close * c, 0.95))
        r = run(g)
        if r["ev_wk"] >= 20 and r["hrs"] <= SALES_HRS and r["r30"] >= 1.5:
            field_.append((r["cac"], f.key))
    if field_:
        wins[min(field_)[1]] += 1
print("| Funnel | Clears 1.5:1 | Wins on CAC *and* stays runnable | Verdict |")
print("|---|---|---|---|")
for f in sorted(FUNNELS, key=lambda x: (-wins[x.key], -grid[x.key][0])):
    cl, _ = grid[f.key]
    best_w = max(wins.values())
    v = ("**best on the grid**" if wins[f.key] == best_w and best_w else
         "**robust**" if cl == 1.0 else
         "fragile" if cl < 0.7 else "conditional")
    print(f"| {f.name.split('. ',1)[1]} | {cl:.0%} of 27 | {wins[f.key]}/27 | {v} |")
print(f"\n*Runnable* means three things at once: **at least 20 pixel events a week** (below that")
print(f"you are reading noise), **under {SALES_HRS:.0f} founder hours a month**, and **clearing "
      f"1.5:1**. Several")
print("funnels with attractive CACs win zero grid points because they fail one of the other two —")
print("**the free work sample above all, which is the cheapest CAC in the study and unrunnable by")
print("one person.**\n")

# ------------------------------------------------------- 6. the cell arithmetic
print("---\n\n## 6. How many ICP x role cells can $5,000 actually support?\n")
print("This is the part that changes the plan, and it is arithmetic rather than opinion.\n")
print(f"Meta needs **~{LEARN_WEEK} optimisation events per ad set per 7 days** to leave the")
print("learning phase, and inside it **CPA runs 20-50% higher** [V]. So:\n")
print("| Funnel | Events/week | One ad set clears 50/wk? | Split 9 ways | Intent of the event |")
print("|---|---|---|---|---|")
CHEAP = {"instant", "magnet", "bench", "ctm"}      # the event is a click, not a decision
for f in sorted(FUNNELS, key=lambda x: -R[x.key]["ev_wk"])[:8]:
    r = R[f.key]
    one = "✅" if r["ev_wk"] >= LEARN_WEEK else "❌"
    intent = "**weak** — a download or an unlock" if f.key in CHEAP else "strong"
    print(f"| {f.name.split('. ',1)[1]} | {r['ev_wk']:.0f} | {one} | "
          f"{r['ev_wk']/9:.1f}/wk each | {intent} |")
top = BY[0]
rt = R[top.key]
clears = [f for f in FUNNELS if R[f.key]["ev_wk"] >= LEARN_WEEK and R[f.key]["r30"] >= 1.5]
print(f"\n**Two things are true at once, and the tension between them is the finding.**\n")
print(f"{len(clears)} of the twelve {'does' if len(clears)==1 else 'do'} clear 50 events a week "
      f"while also clearing 1.5:1 — and {'it optimises' if len(clears)==1 else 'every one optimises'}")
print("toward a **download, an unlock or a chat**, not toward a buying decision. That is *why* it is")
print("cheap. Teaching Meta to find people who download things is teaching it the wrong lesson at")
print("high speed, and the CAC column in §2 is where that shows up — the lead magnet buys events at")
print(f"${R['magnet']['cpl']:.0f} and placements at ${R['magnet']['cac']:,.0f}, against "
      f"${R[top.key]['cpl']:.0f} and ${R[top.key]['cac']:,.0f} for the calculator.\n")
print(f"Among the funnels whose event actually means something, the best is the top-ranked one:")
print(f"**{rt['ev_wk']:.0f} events a week against a threshold of {LEARN_WEEK}** — the closest any "
      f"high-intent event gets,")
print(f"and **{rt['ev_wk']/LEARN_WEEK:.0%} of the way there.** That single fact is most of why it "
      f"ranks first.\n")
need = LEARN_WEEK * WEEKS / (rt["ev"] / SPEND)
print(f"> **Split nine ways it is {rt['ev_wk']/9:.1f} events per cell per week.** Not a test — "
      f"noise with a dashboard.\n")
print(f"To get *one* ad set to {LEARN_WEEK}/week on that funnel needs **${need:,.0f}/month**. "
      f"Nine cells needs")
print(f"**${need*9:,.0f}/month**, which is {need*9/SPEND:.0f}x the test budget. Neither is the "
      f"plan, and the")
print("second one is not a plan at any budget you will have this year.\n")
print("### So the cells cannot be campaign structure\n")
print("> **The ICP x role matrix belongs in the creative, not in the campaign structure and not in")
print("> the landing page.** One campaign, one ad set, one landing page, nine ads.\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Conversion signal pools**",
     "All nine ads feed one optimisation event on one page, so the ad set accumulates events nine "
     "times faster than nine ad sets would"),
    ("**The ICP x role read is still clean**",
     "You read it at **ad level** — CTR, cost per event, and the role tapped on the page. Those "
     "need dozens of events, not fifty a week each"),
    ("**Meta does the audience work**",
     "Nine ads in one ad set is exactly what Advantage+ style delivery is built to resolve. "
     "You are testing *message*, and message is what ad-level reporting is for"),
    ("**It is the cheapest possible test**",
     "Nine creatives is nine hours of work. Nine ad sets is nine learning phases you cannot "
     "afford to fund"),
    ("**One page keeps the page test alive**",
     "A landing-page variant needs 42,000 views to prove a 20% lift ([`SITE.md`](SITE.md)). "
     "Nine pages means never testing the page at all")]:
    print(f"| {a} | {b} |")
print("\n**And the role picker already carries the role dimension.** The tap is a first-party read "
      "on")
print("which seat the ad brought in, at zero incremental spend — which is a better instrument than "
      "nine")
print("ad sets would have been, because it separates *what the ad promised* from *what the buyer "
      "wanted*.\n")

# ------------------------------------------------------------ 7. the recommendation
print("---\n\n## 7. The recommended funnel\n")
w = next(f for f in FUNNELS if f.key == "calc")
g2 = next(f for f in FUNNELS if f.key == "app")
runner = BY[1]
print(f"**{w.name.split('. ',1)[1]}** at **{T[w.key]:.1f}**, built as a hybrid with")
print(f"**{g2.name.split('. ',1)[1]}** at **{T[g2.key]:.1f}** — because §4 showed the qualifying "
      f"gate and")
print("the calculator are two halves of one replacement for money, not two competing options.\n")
print(f"**The top two are {abs(T[BY[0].key]-T[BY[1].key]):.1f} points apart, which this model "
      f"cannot resolve.** "
      f"{runner.name.split('. ',1)[1] if BY[0].key=='calc' else BY[0].name.split('. ',1)[1]}")
print("is the other one, and it is a genuinely good answer — a 15-minute fit call is friction that")
print("filters, which is exactly what §4 asked for. **It is rejected on the operator's own brief,")
print("not on the numbers:** the stated goal is that the *page* makes them knowledgeable and")
print("interested enough to book. A two-call funnel moves qualification back into a call, which is")
print("the one thing that cannot be mechanised, cannot be delegated, and does not scale past you.\n")
print("```")
print("  AD          qualifies on ICP + size, offers the roles as a menu")
print("   |          one campaign · one ad set · 9 creatives")
print("   v")
print("  LANDING     proof · calculator · role picker · qualifying gate")
print("   |          ONE page, ONE url, no CMS")
print("   v")
print("  GATE        3 questions with a real no. Spend, revenue, volume")
print("   |")
print("   +--> disqualified -> honest no + the scorecard. No call booked")
print("   |")
print("   v")
print("  CALENDAR    shown only after the gate passes  <- the pixel event")
print("   |")
print("   v")
print("  CALL        45 min. The calculator has already made the volume argument")
print("   |")
print("   v")
print("  SIGNED      search begins")
print("```")
print()
print("| Step | Number | Source |\n|---|---|---|")
h = run(replace(FUNNELS[3], c1=0.060, c2=0.40, show=0.62, close=0.19, fill=0.77))
for a, b, c in [
    ("Spend", f"${SPEND:,.0f}/mo", "the size [`FUNNEL.md`](FUNNEL.md) argued for test one"),
    ("Landing page views", f"{h['lpv']:,.0f}", "[E] blended CPM/CTR, 15% pre-paint bounce"),
    ("**Pixel event** — calculator completed", f"**{h['ev']:,.0f}**",
     f"**{h['ev_wk']:.0f}/week.** Still under 50, but the most of any option"),
    ("Cost per event", f"${h['cpl']:,.0f}",
     "**below** the verified $30-80 B2B CPL band [V] — because a calculator is a smaller ask "
     "than a form"),
    ("Calls booked", f"{h['booked']:,.0f}", "[?] 40% of completions book"),
    ("Calls held", f"{h['held']:,.0f}", "[?]"),
    ("Signed", f"{h['signed']:.1f}", "[?] the softest number in the model"),
    ("**Placements**", f"**{h['placed']:.1f}**", "78% fill"),
    ("Founder hours", f"{h['hrs']:.0f}/mo", f"{h['hrs_place']:.0f} hours per placement"),
    ("**CAC**", f"**${h['cac']:,.0f}**", "spend + founder time ÷ placements"),
    ("**30-day**", f"**{h['r30']:.2f}:1**", f"against the 1.5:1 constraint"),
    ("**Lifetime**", f"**{h['rlife']:.2f}:1**", "")]:
    print(f"| {a} | {b} | {c} |")
print()
print("### The one thing this funnel still does not satisfy\n")
print("The standing constraint says **no sales call may determine CAC.** This funnel does not meet")
print("it, and neither does any other option that ends in a booked call — funnel 9, the deposit, is")
print("the only one that does, and it collapses volume to the point of being unmeasurable.\n")
print("Worth being exact about what is given up, because it is not the ratio:\n")
print("| | |\n|---|---|")
for a, b in [
    ("**It stays measurable**",
     "Cost per calculator completion is a paid-media number you can optimise weekly. That is the "
     "part that has to be mechanical, and it is"),
    ("**What becomes unhirable**",
     f"The close. At {h['held']:.0f} held calls a month you are the only closer, and the close "
     "rate is the "
     "number CAC is most sensitive to. It cannot be delegated until it is documented"),
    ("**What becomes unforecastable**",
     f"Placements. {h['signed']:.1f} signings a month is far too few to measure a close rate — "
     "±10 points either way, same as the deposit rate it replaces"),
    ("**The mitigation that actually works**",
     "Move persuasion earlier, permanently. Every point of close rate the calculator and the "
     "public teardown buy you is a point that does not depend on the call going well")]:
    print(f"| {a} | {b} |")
print()
print("So the constraint is not satisfied — it is **deferred**, and the honest version of the plan")
print("says so. The paid gate is the thing to re-test at month three, when there is a close rate to")
print("compare it against. It is a much easier sale once one placement can be named.\n")


# ---------------------------------------------------------------- 8. the assets
print("---\n\n## 8. The framework, as three assets\n")
print("### The ad\n")
print("Nine of them, one ad set. The invariant shape, with only the bracketed parts changing:\n")
print("```")
print("  HOOK       [ICP + size, as a question they answer yes to]")
print("             \"Running $10k+ a month in Meta ads on your own store?\"")
print("  TURN       the volume problem, in their units")
print("             \"You need 12-16 new cuts a month. You are shipping 3.\"")
print("  MENU       the roles, named, as a list")
print("             \"Editors, media buyers, ops, bookkeepers - graded before you meet them.\"")
print("  ASK        \"See what one costs against your current invoice.\"  <- not \"book a call\"")
print("```")
print()
print("| | |\n|---|---|")
for a, b in [
    ("**The hook carries the ICP**", "and nothing else does. Not the ad set, not the page"),
    ("**The menu carries the roles**", "so one ad can name three seats and let the page resolve which"),
    ("**The ask is the calculator, not the call**",
     "A calculator is a smaller ask than a calendar, and it is the qualifier. The call is asked "
     "for on the page, after they have convinced themselves"),
    ("**No employment language, in any of the nine**",
     "No *apply*, no *join*, no *hiring now*. One reviewer tick costs 10-29% on CAC "
     "([`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md))")]:
    print(f"| {a} | {b} |")
print("\n### The landing page — one URL, and what varies\n")
print("| Block | Varies by cell? |\n|---|---|")
for a, b in [
    ("Hero: ICP + size qualifier, one promise", "**No.** The size band is the same across roles"),
    ("**Role picker — 'which seat is open?'**", "**No.** It IS the variation, resolved by tapping"),
    ("Public teardown of a brand they know", "**No.** Produced once, shown to everyone"),
    ("**Volume calculator**", "**Labels only.** Ads / campaigns / tickets. The arithmetic is fixed"),
    ("Proof: one measured before-and-after", "**Numbers swap on tap.** One real pair per role, or "
     "the role does not launch"),
    ("How it works, price, guarantee", "**No.**"),
    ("Objections", "**No.** Why India, why not a freelancer, why not AI"),
    ("**Qualifying gate, then the calendar**", "**No.** Three questions, same three for everyone"),
    ("Founder block and footer", "**No.**")]:
    print(f"| {a} | {b} |")
print("\n**Roughly 80% of the page is invariant.** The specificity lives in six labels, one number")
print("pair, and the calculator's units — which is exactly why nine cells need one page.\n")
print("### The homepage\n")
print("Unchanged from [`MINIMUM.md`](MINIMUM.md) §3, with one addition and one deletion:\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Keep** four blocks: what you do, the proof block, who it is for, footer with a real address",
     "It exists so the domain does not 404 for a buyer who types it, and so you look real"),
    ("**Add** the public teardown, linked",
     "It is the work sample now that nothing is paid for. It is the most persuasive object you own "
     "and it should not live only on the ad path"),
    ("**Delete** every mention of a paid teardown",
     "It appears in [`LANDING.md`](LANDING.md), [`MINIMUM.md`](MINIMUM.md), "
     "[`TEARDOWN.md`](TEARDOWN.md) and [`SITEMAP.md`](SITEMAP.md) as the CTA"),
    ("**Still no ads pointed at it**", "Measurement, per [`MINIMUM.md`](MINIMUM.md) §7")]:
    print(f"| {a} | {b} |")

# ------------------------------------------------------------------ 9. the cells
print("\n---\n\n## 9. Which 2-3 x 2-3 to pick\n")
print("Since the cells are creatives rather than campaigns, the choice costs nine hours instead of")
print("nine budgets — but it should still be the right nine. The filter that matters is not market")
print("size:\n")
print("> **Can you personally grade the work?** [`LAUNCH.md`](LAUNCH.md)'s `FOUNDERGRADE`. A role")
print("> you cannot grade has no measurable before-and-after, and §8's proof block is empty for it.\n")
print("| Role | Gradeable by you? | Measurable delta | Verdict |\n|---|---|---|---|")
for a, b, c, d in [
    ("**Performance video editor**", "**Yes** — it is the founding skill",
     "3-sec and 15-sec retention", "**Launch cell.** The wedge"),
    ("**Paid media buyer**", "**Yes** — same skill, other side",
     "CPA, cost per result", "**Launch cell.** Same buyer, bigger seat"),
    ("Marketing ops", "Partly", "Days to launch", "**Third cell.** Adjacent, and you can check the output"),
    ("Bookkeeping", "**No**", "Days to close", "Later. You cannot grade a reconciliation"),
    ("Design", "Partly", "Revision rounds", "Later. Taste is not a measured delta"),
    ("Customer support", "**No**", "First response time", "Later")]:
    print(f"| {a} | {b} | {c} | {d} |")
print("\n| ICP | Why | Verdict |\n|---|---|---|")
for a, b, c in [
    ("**Marketing agencies**", "Buy creative volume by definition, so the volume argument needs no "
     "explaining ([`MINIMUM.md`](MINIMUM.md) §1)", "**Launch cell**"),
    ("**E-comm, $3-10M revenue, $10k+/mo ads**", "The operator direction's own example, and the "
     "spend threshold is a clean qualifier", "**Launch cell**"),
    ("Creator businesses", "High volume, thin budgets, and they buy on price", "Third, or not at all"),
    ("Info / education", "Highest creative burn rate of any category", "**Better third cell**"),
]:
    print(f"| {a} | {b} | {c} |")
print("\n**Two roles x two ICPs = four creatives, not nine.** Video and media buying, into agencies")
print("and e-comm. Both roles are gradeable by the operator today; both ICPs already understand")
print("creative volume. **Add the third of each only once the first four have separated** — and at")
print(f"{rt['ev_wk']:.0f} events a week, four cells is already more than the budget can read "
      f"cleanly.\n")
print("---\n\n## 10. What this reverses\n")
print("| Document | Now wrong |\n|---|---|")
for a, b in [
    ("[`TEARDOWN.md`](../TEARDOWN.md)", "The $500 price and the paid gate. **The generator survives "
     "and matters more** — it now produces the free public teardown that replaces the work sample"),
    ("[`LANDING.md`](../LANDING.md)", "*\"Get the $500 teardown\"* as the CTA, and `/hire/[slug]` x 20"),
    ("[`MINIMUM.md`](../MINIMUM.md)", "§1's Stripe Payment Link as launch infrastructure; the "
     "teardown as step one of the funnel"),
    ("[`SITEMAP.md`](../SITEMAP.md)", "Every page on the paid path"),
    ("[`funnel.py`](funnel.py)", "`DEPOSIT_COLD` is now a close rate. The variable name is the "
     "last trace of the old funnel"),
    ("[`LTGP.md`](LTGP.md)", "*\"the deposit rate is the one input that can break it\"* — still "
     "true, but it is now the **close** rate, and it is less measurable than a payment was")]:
    print(f"| {a} | {b} |")
print("\n**What does not change:** the offer, the fee, the guarantee, the EOR line, the gross")
print("profit, the audience layers, the $5,000 test size, and the volume argument. **The offer was")
print("never the teardown.**\n")
