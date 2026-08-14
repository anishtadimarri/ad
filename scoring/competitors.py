#!/usr/bin/env python3
"""
What ten competitors actually run, and which Meta funnel that implies for us.

Operator direction: no teardown. Same content for every ICP x role, ending in a
booked call. Day 1 tests 2-3 roles x 2-3 ICPs. And the governing constraint:
"we don't have clarity yet as to what will work" — so the funnel is a DISCOVERY
instrument first and a conversion mechanism second.

Every competitor row below was fetched and read in August 2026. Where a field
could not be verified it says so rather than guessing. Meta Ad Library returned
HTTP 403 on two attempts, so NO claim is made about competitor Meta activity.

Funnel options are each anchored to a competitor precedent, or explicitly marked
as having none — because "nobody in the category does this" is information, and
it cuts both ways.

Run:  python3 scoring/competitors.py > scoring/COMPETITORS.md
"""

import io
import os
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass, field, replace

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

with redirect_stdout(io.StringIO()):
    import funnel as fn
    import offer_model as om

SPEND = 5000.0
FOUNDER_HR = 60.0
SALES_HRS = 60.0
LEARN_WEEK = 50            # [V] Meta: ~50 optimisation events per ad set / 7 days
WEEKS = 4.33
MIX = {"Intent seed (job posters)": 0.25, "1% Lookalike": 0.45,
       "Broad / Advantage+": 0.30}

BASE = next(c for c in om.CONFIGS if c.name.startswith("H5"))
OFFER = replace(BASE, name="$20k job, EOR default", salary=20_000.0, fee_pct=0.30,
                eor_price=499.0, eor_attach=0.75, monthly_tenure=9.0)
E = om.econ(OFFER)
GP30, GPLIFE = E["gp30"], E["gplife"]


# ------------------------------------------------------------- the competitors
@dataclass
class C:
    name: str
    url: str
    cta: str
    entry: str            # what the first click actually leads to
    gate: str             # any qualifying step with a real no
    price: str
    bench: str            # named candidate profiles on the demand-facing page
    model: str            # how they make money
    tool: str
    headline: str


COMPS = [
    C("GrowthAssistant", "growthassistant.com", '"Find My Match"',
      "**One-field form** — *\"Tell us about your company\"* — then a 15-minute intro call",
      "**None**", "**$3,500/mo**, published, month-to-month",
      "4 named, with accomplishments and tools",
      "**Monthly retainer**", "Cost-comparison table vs in-house, freelancer, contractor",
      '"The World\'s Best AI-Trained Marketing Talent. Built Into Your Team."'),

    C("Somewhere", "somewhere.com", '"Start Hiring Now"',
      "`/contact-flow/01`, then a free consult on a HubSpot calendar", "**None**",
      "Not published — *\"custom plans based on hires + services\"*",
      "**9 named, with country and prior employer**",
      "Placement fee 25–35%, one-time", "Salary comparison: role → region → get in touch",
      '"We recruit, vet, and place top 1% remote talent for 80% less than US equivalents."'),

    C("Athyna", "athyna.com", '"Start hiring"', "Contact form", "**None**",
      "Not published — candidate **hourly rates** shown, $11–80/hr",
      "**40+ named, with rates and skills**", "Hourly markup",
      "JD generator · LATAM salary tool · comparison tool",
      '"LATAM\'s best minds pushing the frontier of AI"'),

    C("Genius", "joingenius.com", '**"See Pre-vetted Candidates"**',
      "**1-minute form → a personalised candidate list.** *\"No commitment\"*", "**None**",
      "**25% one-time** of assumed first-year salary. *\"$0 monthly fees\"*",
      "9 named, with monthly salary $1.2–2.5k", "Placement fee 25%, one-time",
      "None found", '"Get Elite Global Talent for 80% Less"'),

    C("Hireframe", "hireframe.com", '"Start Hiring"', "Contact form", "**None**",
      "**$2,500/mo**, published, 30-day notice", "None — testimonials only",
      "**Monthly retainer**", "None", '"Global Talent that Moves the Needle"'),

    C("Athena", "athena.com", '"Find your EA match"',
      "**Role-select matching questionnaire** (founder / owner / C-suite / other)",
      "**None** — all levels invited", "Not on the landing page (a `/pricing` link exists)",
      "None", "Monthly", "None found",
      '"The relief is immediate. The ROI is real."'),

    C("Vidpros", "vidpros.com", '"Watch Demo" / **"Start $100 Trial"**',
      "**Self-serve paid trial** — $100 for 10 short edits or 1 long video, one week",
      "**The $100 itself**", "**$1,000/mo part-time · $4,000/mo full-time**", "None",
      "**Subscription**", "None", '"Video Editing Services on demand. Hire a Video Editor today!"'),

    C("Vidchops", "vidchops.com", '"Yes! Give Me An Editor Now"',
      "**15-minute consult call**", "**None**",
      "**Hidden behind an \"Unlock Pricing\" button.** 14-day money-back", "None",
      "**Subscription**, credits per month", "None",
      '"Add An Expert Video Editor To Your Team In Just A Few Clicks…"'),

    C("Oceans", "oceanstalent.co", "—", "Not re-verified this pass", "—",
      "Not published", "—", "Monthly, ~$3,000/mo, 3-month trial", "—",
      "— *(from [`COMPETITOR-DATA.md`](../COMPETITOR-DATA.md) §4, not re-fetched)*"),

    C("Near", "hirenear.com", "—", "**Domain parked on HugeDomains — 302 redirect**", "—",
      "—", "—", "**Dead or rebranded**", "—", "—"),
]


# ------------------------------------------------------------------ the funnels
@dataclass
class F:
    key: str
    name: str
    precedent: str
    event: str
    c1: float
    show: float
    close: float
    fill: float
    lpv: float = 0.85
    c2: float = 1.0
    min_lead: float = 5.0
    min_held: float = 60.0
    min_sample: float = 0.0
    gate_share: float = 1.0
    reveals: str = ""          # what the first click tells us
    discover: int = 0
    trust: int = 0
    generic: int = 0
    prec: int = 0
    build: int = 0
    why: dict = field(default_factory=dict)


FUNNELS = [
    F("bench", "A. See the bench — 3–6 graded people, teased then unlocked",
      "**Genius** leads with it as the CTA. **Athyna** shows 40+, **Somewhere** 9, "
      "**GrowthAssistant** 4",
      "Bench unlocked", c1=0.075, c2=0.28, show=0.62, close=0.24, fill=0.76, min_lead=2.0,
      reveals="**Role and ICP, plus which specific person appeals** — the richest first click "
              "available",
      discover=10, trust=9, generic=7, prec=10, build=3,
      why=dict(trust="Named people with measured work is what every scaled player in the category "
                     "leads with. It is also the only thing that makes *graded* concrete",
               generic="One page per role's bench, but the page frame is identical",
               build="**Needs 2 graded people per launch role before the first ad.** This is the "
                     "real cost, and it is work the business needs anyway",
               prec="Four of eight operating competitors do this. Nothing else in the study is "
                    "this well precedented")),

    F("match", "B. One-field form — *\"tell us about your company\"* — then a call",
      "**GrowthAssistant** exactly. One field, then a 15-minute intro call",
      "Form fill", c1=0.062, c2=0.34, show=0.56, close=0.17, fill=0.68, min_lead=9.0,
      reveals="**Almost nothing.** A free-text box and an email",
      discover=3, trust=4, generic=10, prec=9, build=10,
      why=dict(trust="Nothing is shown before the ask. GrowthAssistant can do this because they "
                     "have logos and a published price; you have neither",
               generic="Genuinely identical across every cell",
               build="A form. Ten minutes",
               prec="The closest competitor to our exact ICP x role runs precisely this")),

    F("quiz", "C. Role-select quiz → matched profiles → call",
      "**Athena**'s role-select questionnaire crossed with **Somewhere**'s role → region tool",
      "Quiz completed", c1=0.070, c2=0.30, show=0.64, close=0.25, fill=0.77, min_lead=2.0,
      reveals="**Role, ICP, size and urgency** — every answer is a field you chose",
      discover=10, trust=7, generic=9, prec=8, build=6,
      why=dict(trust="Being asked good questions reads as competence. It is the cheapest "
                     "credibility signal that does not require a track record",
               generic="Same question set for every cell; the role is the first answer",
               build="A multi-step form with branching. A day",
               prec="Athena and Somewhere both run a version of this")),

    F("trial", "D. Paid micro-trial that delivers real work — $100–250",
      "**Vidpros' $100 trial**: 10 short edits or 1 long video in a week. The only paid entry "
      "offer in the category",
      "Trial purchased", c1=0.011, show=0.90, close=0.52, fill=0.86, min_lead=3.0,
      min_sample=100.0, gate_share=1.0,
      reveals="**Role, ICP, and willingness to pay** — the highest-quality signal per event and "
              "the fewest events",
      discover=6, trust=10, generic=4, prec=7, build=5,
      why=dict(trust="Highest in the study. They see the actual work before any commitment, "
                     "which is the whole `TRUECLAIM` position made literal",
               generic="The deliverable is role-specific. Every launch role needs one you can "
                       "personally produce",
               build="A Stripe link and a delivery promise you can keep",
               prec="Vidpros proves a paid micro-offer works in the video wedge specifically")),

    F("calc", "E. Cost calculator → email → call",
      "**Somewhere** and **Athyna** both ship salary tools; **GrowthAssistant** ships a "
      "cost-comparison table",
      "Calculator completed", c1=0.060, c2=0.30, show=0.60, close=0.21, fill=0.75, min_lead=3.0,
      reveals="**Their volume and vendor spend, in their own numbers** — but not which person "
              "they want",
      discover=7, trust=7, generic=8, prec=9, build=5,
      why=dict(trust="They compute it themselves, so there is nothing to disbelieve. But it "
                     "proves nothing about whether *you* can judge talent",
               generic="Arithmetic is identical; only unit labels change",
               build="The one genuinely custom block on the site",
               prec="Three of eight ship a calculator or comparison tool")),

    F("price", "F. Publish the price, then book onboarding",
      "**GrowthAssistant** ($3,500/mo) and **Hireframe** ($2,500/mo) both publish. **Genius** "
      "publishes 25%",
      "Booked call", c1=0.024, show=0.74, close=0.24, fill=0.80, min_lead=4.0,
      reveals="**Nothing beyond role** — but it removes the price-shock objection from the call",
      discover=4, trust=6, generic=10, prec=10, build=9,
      why=dict(trust="Publishing is a confidence signal, and half the category does it. "
                     "**Vidchops actively hides theirs behind an \"Unlock Pricing\" button**, "
                     "which is the tell",
               generic="One number for every cell",
               build="A pricing block. Already needed",
               prec="Three of eight publish a real number")),

    F("free", "G. Free graded sample on *their* asset, then a call",
      "**None.** No competitor in the study gives away work on the prospect's own material",
      "Sample requested", c1=0.045, c2=0.42, show=0.75, close=0.30, fill=0.80,
      min_lead=4.0, min_sample=90.0, gate_share=0.35,
      reveals="Role and ICP, and unusually high intent",
      discover=6, trust=10, generic=3, prec=1, build=3,
      why=dict(trust="Tied highest. Nothing persuades like the work itself",
               generic="Role-specific by definition, and you must personally have every skill",
               build="Nothing to build, everything to do, forever",
               prec="**No precedent, and the absence is probably informative** — ten operating "
                    "companies all found a cheaper way to prove quality")),

    F("cal", "H. Free consult, calendar straight on the page",
      "**Vidchops** and **Somewhere** both do exactly this — no gate, no qualifier",
      "Booked call", c1=0.020, show=0.65, close=0.12, fill=0.68,
      reveals="Role only, and only if the ad was role-specific",
      discover=2, trust=4, generic=10, prec=10, build=10,
      why=dict(trust="Nothing between a cold stranger and your calendar",
               generic="A calendar embed is seat-agnostic",
               build="Ten minutes",
               prec="The most common pattern in the category — **and every company running it "
                    "has social proof you do not have**")),

    F("gate", "I. Qualifying gate with a real no, then the calendar",
      "**None.** Zero of ten competitors gates the calendar",
      "Application submitted", c1=0.022, c2=0.70, show=0.72, close=0.18, fill=0.78, min_lead=2.0,
      reveals="Spend, revenue and volume — but only from people willing to be screened",
      discover=6, trust=6, generic=9, prec=2, build=8,
      why=dict(trust="Screening reads as selective. It can also read as arrogant from an unknown",
               generic="Same three questions for every cell",
               build="A form with branching",
               prec="**Nobody does this**, which is either the edge or the warning. At ten out "
                    "of ten it is more likely the warning")),

    F("instant", "J. Meta Instant Form, no landing page",
      "None found in this category",
      "Lead (on-platform)", c1=0.120, c2=0.30, show=0.40, close=0.06, fill=0.55,
      lpv=1.00, min_lead=12.0,
      reveals="Whatever the form asks, from people who never saw a page",
      discover=4, trust=1, generic=10, prec=1, build=10,
      why=dict(trust="Nothing shown at all — no page, no people, no price",
               generic="Nothing role-specific exists",
               build="Nothing to build, which is also the problem",
               prec="No competitor found doing this")),
]


# ------------------------------------------------------------------- the engine
def run_one(f, aud, spend):
    cpm, ctr, q = fn.AUD[aud]
    imp = spend / cpm * 1000
    clicks = imp * ctr
    lpv = clicks * f.lpv
    ev = lpv * f.c1
    booked = ev * f.c2
    held = booked * f.show
    signed = held * min(f.close * q, 0.45)
    placed = signed * f.fill
    mins = ev * f.min_lead + held * f.min_held + ev * f.gate_share * f.min_sample
    return dict(ev=ev, booked=booked, held=held, signed=signed, placed=placed,
                mins=mins, cost=spend + mins / 60.0 * FOUNDER_HR, lpv=lpv)


def run(f, spend=SPEND, gp30=None):
    gp30 = GP30 if gp30 is None else gp30
    t = dict(ev=0.0, booked=0.0, held=0.0, signed=0.0, placed=0.0, mins=0.0,
             cost=0.0, lpv=0.0)
    for aud, share in MIX.items():
        r = run_one(f, aud, spend * share)
        for k in t:
            t[k] += r[k]
    p = t["placed"]
    t["cac"] = t["cost"] / p if p else float("inf")
    t["cpl"] = spend / t["ev"] if t["ev"] else float("inf")
    t["r30"] = gp30 / t["cac"] if p else 0.0
    t["rlife"] = GPLIFE / t["cac"] if p else 0.0
    t["hrs"] = t["mins"] / 60.0
    t["ev_wk"] = t["ev"] / WEEKS
    return t


DIM = [("DISCOVER", 22, "How much the first click reveals about which ICP x role works"),
       ("CAC30",    16, "30-day LTGP:CAC against the 1.5:1 constraint"),
       ("LEARN",    14, "Optimisation events per week against Meta's 50"),
       ("TRUST",    14, "Works for an unknown India-based solo operator"),
       ("GENERIC",  12, "Same content across every ICP x role cell"),
       ("FOUNDER",  10, "Founder hours/month against the ~60 available for selling"),
       ("PRECEDENT", 8, "Does an operating competitor actually run this"),
       ("BUILD",     4, "What must exist before the first dollar of spend")]

R = {f.key: run(f) for f in FUNNELS}


def scores(f):
    r = R[f.key]
    learn = min(10.0, 10.0 * (r["ev_wk"] / LEARN_WEEK) ** 0.5)
    cac30 = 0.0 if r["r30"] < 1.5 else min(10.0, 2.0 + 8.0 * min(1.0, (r["r30"] - 1.5) / 4.0))
    founder = max(0.0, min(10.0, 10.0 * (SALES_HRS / max(r["hrs"], 1.0)) ** 0.8))
    # DISCOVER is half judgement (what the click reveals) and half arithmetic
    # (how many clicks there are to read). A rich signal nobody sends is useless.
    vol = min(1.0, r["ev_wk"] / 40.0) ** 0.5
    disc = f.discover * (0.45 + 0.55 * vol)
    return dict(DISCOVER=disc, CAC30=cac30, LEARN=learn, TRUST=float(f.trust),
                GENERIC=float(f.generic), FOUNDER=founder,
                PRECEDENT=float(f.prec), BUILD=float(f.build))


S = {f.key: scores(f) for f in FUNNELS}
T = {f.key: sum(S[f.key][k] * w for k, w, _ in DIM) / 10.0 for f in FUNNELS}
BY = sorted(FUNNELS, key=lambda f: -T[f.key])

# ------------------------------------------------------------------ the report
print("# What Ten Competitors Actually Run — and the Funnel That Follows\n")
print("> All ten fetched and read in **August 2026**. Where something could not be verified it")
print("> says so. **Meta Ad Library returned HTTP 403 on two attempts**, so this study makes")
print("> **no claim about any competitor's Meta activity** — see §3.\n")

print("---\n\n## 1. The ten, side by side\n")
print("| | CTA | What the first click leads to | Gate | Price |")
print("|---|---|---|---|---|")
for c in COMPS:
    print(f"| **{c.name}**<br>`{c.url}` | {c.cta} | {c.entry} | {c.gate} | {c.price} |")
print("\n| | Named candidates shown | Model | Tool | Headline |")
print("|---|---|---|---|---|")
for c in COMPS:
    print(f"| **{c.name}** | {c.bench} | {c.model} | {c.tool} | {c.headline} |")

print("\n---\n\n## 2. Five patterns, and four of them contradict what I told you last time\n")
print("### 2.1 The category's CTA is a *person*, not a call\n")
print("| Competitor | CTA |\n|---|---|")
for a, b in [("Genius", '**"See Pre-vetted Candidates"**'),
             ("GrowthAssistant", '**"Find My Match"**'),
             ("Athena", '**"Find your EA match"**'),
             ("Vidchops", '**"Yes! Give Me An Editor Now"**'),
             ("Somewhere / Athyna / Hireframe", '"Start Hiring"')]:
    print(f"| {a} | {b} |")
print("\n**Not one of them asks for a call in the button.** The call exists — Somewhere, "
      "GrowthAssistant and")
print("Vidchops all route to one — but it is never the promise. **The promise is a person.**\n")
print("> The buyer's question is not *\"should I talk to this company?\"* It is *\"who would I "
      "get?\"*\n")

print("### 2.2 Nobody gates. Zero of ten\n")
print("Not one competitor puts a qualifying question with a real *no* in front of the calendar.")
print("**GrowthAssistant asks one field** — *\"tell us about your company\"* — and Genius "
      "advertises")
print("*\"takes 1 minute\"* and *\"no commitment\"*. The category competes on **removing** "
      "friction.\n")
print("I recommended a qualifying gate last time and ranked it first. **Ten out of ten operating")
print("companies disagree.** That is not proof they are right — none of them is a solo unknown")
print("operator, and friction is exactly how an unknown compensates for having no logos. But a")
print("unanimous category is evidence, and §5 prices it rather than dismissing it.\n")

print("### 2.3 The bench is the lead magnet, and it is on the *homepage*\n")
print("| Competitor | Named profiles on the demand page | With |\n|---|---|---|")
for a, b, c in [("**Athyna**", "**40+**", "photo, location, role, **hourly rate**, skills"),
                ("**Somewhere**", "**9**", "photo, country flag, **prior employer**"),
                ("**Genius**", "**9**", "photo, specialisation, **monthly salary**"),
                ("**GrowthAssistant**", "**4**", "accomplishments and tool proficiency"),
                ("Hireframe · Athena · Vidpros · Vidchops", "0", "testimonials or nothing")]:
    print(f"| {a} | {b} | {c} |")
print("\n**Four of the eight live competitors put named, priced humans on the page before any "
      "form.**")
print("The four that do not are the two subscription video shops and the two that sell a *service*")
print("rather than a *person* — which is the distinction that matters, because **we sell a "
      "person.**\n")

print("### 2.4 Two pricing models, and the closest competitor uses the one our constraint forbids\n")
print("| Model | Who | Price |\n|---|---|---|")
print("| **Monthly retainer** | GrowthAssistant · Hireframe · Vidpros · Vidchops · Athena · Oceans "
      "| $1,000–4,000/mo |")
print("| **One-time placement fee** | Somewhere · Genius | 25–35% of first-year |")
print("\n**GrowthAssistant is the closest competitor in the study** — offshore *marketing and "
      "creative*")
print("talent, sold to *DTC/e-comm, agencies and SaaS*, placing *paid social, video editors, "
      "designers,")
print("email, SEO, data* — which is our ICP list and our role list. **And they charge "
      "$3,500/month.**\n")
mo_price, mo_salary = 3500.0, 1650.0
mo_gp = mo_price - mo_salary - om.EOR_COST
print("§6 does the arithmetic on copying that, and the answer is that **it breaks the 30-day "
      "constraint**")
print(f"— ${mo_gp:,.0f}/month of gross profit cannot clear 1.5:1 against any CAC in this study "
      f"except two.\n")

print("### 2.5 Half the category leads on price, and the same number twice\n")
print("| Competitor | Headline |\n|---|---|")
for c in COMPS:
    if c.headline not in ("—", "— *(from [`COMPETITOR-DATA.md`](../COMPETITOR-DATA.md) §4, "
                          "not re-fetched)*"):
        print(f"| **{c.name}** | {c.headline} |")
print("\n**\"80% less\" appears verbatim in two of eight headlines** — Somewhere and Genius. It is")
print("the category's default claim, and [`MODEL-V2.md`](../MODEL-V2.md) §8 already decided not to")
print("compete there. **This confirms that decision rather than challenging it:** entering a "
      "category")
print("on the leader's own axis, with no track record, is the losing side of that fight.\n")
print("The two most interesting headlines are the ones that do *not* mention cost. "
      "**Athena's \"The relief**")
print("**is immediate. The ROI is real.\"** sells a feeling, and **GrowthAssistant's \"Built Into "
      "Your Team\"**")
print("sells integration. Both are available to us. *\"80% less\"* is not.\n")

print("---\n\n## 3. What I could not verify, stated plainly\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Whether any competitor runs Meta ads**",
     "Ad Library returned **HTTP 403 twice**. No claim is made either way. What *is* visible is "
     "heavy **SEO and content** infrastructure — GrowthAssistant ships articles and reporting "
     "templates, Athyna a JD generator and salary tool, Genius recruiting guides, Somewhere a "
     "blog and salary guides. That is an inbound-led category, which matches "
     "[`REFERENCE.md`](../REFERENCE.md) §4"),
    ("**Their actual conversion rates**",
     "Nobody publishes them. Every conversion number in §4 is `[?]` and swept accordingly"),
    ("**Genius's and GrowthAssistant's full form flows**",
     "Both truncated before the field list. GrowthAssistant's visible portion was **one field**; "
     "there may be more below the fold"),
    ("**Somewhere's scale numbers**",
     "This pass read **4,500+ companies / 8,500+ hires / 1.2M+ pool**. "
     "[`COMPETITOR-DATA.md`](../COMPETITOR-DATA.md) recorded **5,000+ / 11,000+ / 1.5M+**. The "
     "numbers went *down*, which means one of the two readings is a different page or a different "
     "claim. **Not resolved — do not cite either as firm**"),
    ("**Wing Assistant**", "Page truncated on fetch. Excluded rather than guessed"),
    ("**Oceans**", "Not re-fetched this pass; carried from the earlier study and marked as such"),
]:
    print(f"| {a} | {b} |")
print("\nAnd one live finding: **`hirenear.com` now 302-redirects to HugeDomains.** Near is parked.")
print("A competitor in this exact category is **for sale as a domain name** — worth remembering "
      "when")
print("reading anyone's growth claims, including ours.\n")

print("---\n\n## 4. Ten funnels for our case, each anchored to what somebody actually runs\n")
print(f"Gross profit from [`offer_model.py`](offer_model.py): **${GP30:,.0f} at 30 days**, "
      f"**${GPLIFE:,.0f} lifetime**.")
print(f"Audience layers from [`funnel.py`](funnel.py). **${SPEND:,.0f}/month**, founder time at "
      f"**${FOUNDER_HR:.0f}/hr**.\n")
print("| Funnel | Precedent | Events/mo | Events/wk | CPL | Placements | **CAC** | **30-day** "
      "| Hrs/mo |")
print("|---|---|---|---|---|---|---|---|---|")
for f in FUNNELS:
    r = R[f.key]
    flag = "" if r["r30"] >= 1.5 else " ⚠️"
    pr = (f.precedent[:60] + "…") if len(f.precedent) > 60 else f.precedent
    print(f"| **{f.name}** | {pr} | {r['ev']:,.0f} | {r['ev_wk']:.0f} | ${r['cpl']:,.0f} "
          f"| {r['placed']:.1f} | **${r['cac']:,.0f}** | **{r['r30']:.2f}:1**{flag} "
          f"| {r['hrs']:.0f}{' ⚠️' if r['hrs'] > SALES_HRS else ''} |")
over = [f for f in FUNNELS if R[f.key]["hrs"] > SALES_HRS]
print(f"\n**{len(over)} of the ten exceed the ~{SALES_HRS:.0f} founder hours a month available "
      f"for selling**, and the")
print("reason is almost always the same one: **held calls at 60 minutes each.** A funnel that "
      "produces")
print("40 held calls has consumed 40 hours before anything else happens. **The funnels that survive")
print("this are the ones where the lead step is *automated*** — an unlock that serves profiles by")
print("itself costs nothing per lead, while a free-text box you must read and answer costs nine")
print("minutes every time.\n")
print("**What the first click tells you** — the column that matters most, given that the whole")
print("point of month one is finding out which ICP x role works:\n")
print("| Funnel | What you learn from one click |\n|---|---|")
for f in FUNNELS:
    print(f"| {f.name.split('. ',1)[1]} | {f.reveals} |")

print("\n---\n\n## 5. The ranking\n")
print("| Dimension | Weight | What it measures |\n|---|---|---|")
for k, w, d in DIM:
    print(f"| `{k}` | {w} | {d} |")
print("\n`DISCOVER` carries the most weight because it is the operator's stated problem — **no")
print("clarity yet on what will work.** It is scored as *what the click reveals* × *how many "
      "clicks")
print("there are to read*, so a rich signal nobody sends scores badly. `CAC30`, `LEARN` and")
print("`FOUNDER` are derived from §4. `PRECEDENT` is new, and it is what this study was for.\n")
print("| Rank | Funnel | " + " | ".join(f"`{k}`" for k, _, _ in DIM) + " | **Score** |")
print("|---|---|" + "---|" * (len(DIM) + 1))
for i, f in enumerate(BY, 1):
    sc = S[f.key]
    mark = " ✅" if i == 1 else ""
    print(f"| **{i}** | {f.name.split('. ',1)[1]}{mark} | "
          + " | ".join(f"{sc[k]:.1f}" for k, _, _ in DIM) + f" | **{T[f.key]:.1f}** |")
top, second = BY[0], BY[1]
print(f"\n**{top.name.split('. ',1)[1]}** wins, and **{second.name.split('. ',1)[1]}** is "
      f"{T[top.key]-T[second.key]:.1f} behind.")
print("The two are complements rather than alternatives — §7 combines them.\n")
print("### What the gate and the free sample cost themselves\n")
for k in ("gate", "free"):
    f = next(x for x in FUNNELS if x.key == k)
    print(f"- **{f.name.split('. ',1)[1]}** — rank "
          f"{[x.key for x in BY].index(k)+1} of 10, score {T[k]:.1f}. "
          f"`PRECEDENT` {f.prec}/10: {f.why['prec']}")
print("\nBoth were in my previous top three. **Both fall on the same finding**: they are the two")
print("options nobody in a ten-company category runs, and neither buys enough extra conversion to")
print("pay for being novel while also being unknown.\n")

# ------------------------------------------------------- 6. the pricing finding
print("---\n\n## 6. The pricing test — can we copy GrowthAssistant?\n")
print("They are the closest competitor in the study and they charge **$3,500/month**. Our model is")
print("a **one-time 30% fee**. This matters to the funnel because it sets the CAC budget.\n")
print(f"| | Monthly retainer | One-time placement fee |\n|---|---|---|")
print(f"| Price | **$3,500/mo** (GrowthAssistant's number) | ~$6,000 one-time |")
print(f"| Cost of the seat | ${mo_salary:,.0f} salary + ${om.EOR_COST:.0f} admin | — |")
print(f"| **Gross profit inside 30 days** | **${mo_gp:,.0f}** | **${GP30:,.0f}** |")
print(f"| Max CAC at 1.5:1 | **${mo_gp/1.5:,.0f}** | **${GP30/1.5:,.0f}** |")
mo_ok = [f for f in FUNNELS if run(f, gp30=mo_gp)["r30"] >= 1.5]
print(f"| Funnels that clear it | **{len(mo_ok)} of 10** | "
      f"**{len([f for f in FUNNELS if R[f.key]['r30'] >= 1.5])} of 10** |")
print(f"\n> **The monthly model fails the operator's own 30-day constraint at almost any CAC.**")
print(f"> ${mo_gp:,.0f} of month-one gross profit needs CAC under **${mo_gp/1.5:,.0f}**, and only")
print(f"> {len(mo_ok)} of the ten funnels get there.\n")
print("That is not an argument that monthly is a worse business — over a 30-month seat it is worth")
print("far more, and it is why every subscription competitor in the study prices that way. It is an")
print("argument that **monthly is unaffordable to *acquire* on paid media until something else "
      "funds")
print("the gap.** The one-time fee is what makes Meta viable at all, and Somewhere and Genius — "
      "the")
print("two placement-fee players — are also the two with the largest published scale.\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Keep the one-time fee as the acquisition offer**",
     "It is the only thing that clears 1.5:1 on cold paid traffic"),
    ("**Sell the monthly line as the attachment**",
     "EOR at $477/employee/month, exactly as [`LTGP.md`](LTGP.md) models it. Same revenue shape as "
     "GrowthAssistant, acquired on a fee that pays for the click"),
    ("**Do not match $3,500/mo**",
     "It is a competitor's *whole* price against our *attachment* price. Matching it means "
     "competing on the axis where they have logos, a published price and a 92% first-match claim")]:
    print(f"| {a} | {b} |")

# ------------------------------------------------------------ 7. the funnel spec
print("\n---\n\n## 7. The recommended funnel\n")
print(f"**{BY[0].name.split('. ',1)[1]}** at **{T[BY[0].key]:.1f}** and "
      f"**{BY[1].name.split('. ',1)[1]}** at **{T[BY[1].key]:.1f}**.")
print(f"They are **{T[BY[0].key]-T[BY[1].key]:.1f} apart, which this model cannot resolve** — and "
      f"they should not be")
print("resolved, because they are the same funnel seen from two ends:\n")
print("> **The bench is the offer. The quiz is how you route to it.**\n")
print("The quiz asks role, ICP and size in three taps; the bench is what those taps unlock. Run")
print("either alone and you lose something: a quiz with nothing behind it is a form, and a bench")
print("with no routing shows an e-comm owner a bookkeeper. **The numbers below are the hybrid.**\n")
print("```")
print("  AD        qualifies on ICP + size · names the roles as a menu")
print("            one campaign · one ad set · 4 creatives")
print("     |")
print("     v")
print("  PAGE      3 graded people, FACE UP, above the fold")
print("            name · country · the test they passed · the number they hit")
print("     |")
print("     v")
print("  QUIZ      3 taps: which seat · your size · when")
print("            \"Show me who I'd get\"                    <-- THE PIXEL EVENT")
print("     |")
print("     v")
print("  PROFILES  the matched bench for that role, each with the actual work")
print("            sample and the measured number. Email to save or share it.")
print("            Calendar embedded beside them")
print("     |")
print("     v")
print("  CALL      45 min. They have already seen who they would get")
print("     |")
print("     v")
print("  SIGNED    one-time fee. EOR offered at signature, not before")
print("```")
# The recommendation is the hybrid the top two describe: the quiz is the pixel
# event and the routing mechanism, the bench is what it routes TO.
HYB = F("hybrid", "Quiz-routed bench", "Athena's role-select + Genius's candidate list",
        "Quiz completed", c1=0.070, c2=0.30, show=0.63, close=0.25, fill=0.77, min_lead=2.0)
h = run(HYB)
print("\n| Step | Number | Note |\n|---|---|---|")
for a, b, c in [
    ("Spend", f"${SPEND:,.0f}/mo", "the size [`FUNNEL.md`](FUNNEL.md) argued for test one"),
    ("Landing page views", f"{h['lpv']:,.0f}", "[E] blended CPM/CTR, 15% pre-paint bounce"),
    ("**Quiz completed** — the pixel event", f"**{h['ev']:,.0f}**",
     f"**{h['ev_wk']:.0f}/week** against Meta's 50. The highest of any high-intent event here"),
    ("Cost per completion", f"${h['cpl']:,.0f}",
     "**below** the verified $30–80 B2B CPL band [V] — a quiz is a smaller ask than a form"),
    ("Calls booked", f"{h['booked']:,.0f}", "[?] 30% of completions book"),
    ("Calls held", f"{h['held']:,.0f}", "[?]"),
    ("Signed", f"{h['signed']:.1f}", "[?] the softest number in the model"),
    ("**Placements**", f"**{h['placed']:.1f}**", "76% fill"),
    ("Founder hours", f"{h['hrs']:.0f}/mo", f"against ~{SALES_HRS:.0f} available"),
    ("**CAC**", f"**${h['cac']:,.0f}**", "spend + founder time ÷ placements"),
    ("**30-day**", f"**{h['r30']:.2f}:1**", "against the 1.5:1 constraint"),
    ("**Lifetime**", f"**{h['rlife']:.2f}:1**", "")]:
    print(f"| {a} | {b} | {c} |")
print("\n### What this costs you before the first ad\n")
print("> **Two graded people per launch role.** Four creatives means two roles, so **four humans")
print("> sourced, tested and written up.** That is the entry price, and it is the one thing on the")
print("> list that cannot be bought or shortcut.\n")
print("It is also work the business needs regardless — [`MINIMUM.md`](../MINIMUM.md) §6 already "
      "said")
print("the proof block *is* the business. This funnel makes that block the whole page.\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Why not the gate**",
     "Zero of ten competitors gates, and it ranked "
     f"{[x.key for x in BY].index('gate')+1} of 10 here. An unknown operator adding friction "
     "in a category built on removing it is the wrong trade — **show them a person instead of "
     "interviewing them**"),
    ("**Why the bench also qualifies**",
     "Someone who unlocks profiles for a $1,650/month editor has told you their budget by "
     "clicking. The sizing question on the unlock form does the rest"),
    ("**Why it satisfies the discovery problem**",
     "Every unlock carries a **role**, and every ad carries an **ICP**. Four weeks of unlocks is "
     "a demand map you currently do not have, bought with the same money that buys placements"),
    ("**Where it is weakest**",
     "`GENERIC` 7 of 10 — each role needs its own bench, so adding a role is not free the way "
     "adding a calculator label is. **This is the real cost of the recommendation** and it is why "
     "two roles, not three")]:
    print(f"| {a} | {b} |")

# --------------------------------------------------------------- 8. the ad
print("\n---\n\n## 8. The Meta ads\n")
print("Four creatives, one ad set — because at "
      f"**{h['ev_wk']:.0f} events a week** against Meta's 50, splitting into separate ad sets")
print("means no ad set ever leaves the learning phase, where CPA runs **20–50% higher** [V].\n")
print("| Slot | ICP | Role | Hook |\n|---|---|---|---|")
for a, b, c, d in [
    ("1", "E-comm, $10k+/mo ads", "Performance video",
     '*"Running $10k+ a month in Meta ads and shipping 3 new cuts?"*'),
    ("2", "E-comm, $10k+/mo ads", "Paid media",
     '*"Your agency charges 15% of spend. Here is what a full-time buyer costs."*'),
    ("3", "Agencies, 5–30 staff", "Performance video",
     '*"Your editor is the bottleneck on every retainer you have."*'),
    ("4", "Agencies, 5–30 staff", "Paid media",
     '*"You are turning down retainers because you cannot staff them."*')]:
    print(f"| **{a}** | {b} | {c} | {d} |")
print("\n**The creative shape**, and it is taken from what works in the category rather than "
      "invented:\n")
print("```")
print("  1. HOOK     the ICP + size question they answer yes to")
print("  2. FACE     a real graded person, named, with the number they hit")
print("              <- this is the category's actual mechanic. Genius, Athyna,")
print("                 Somewhere and GrowthAssistant all lead with people")
print("  3. TURN     the volume problem in their units")
print("  4. MENU     the other roles, named, one line")
print("  5. ASK      \"See who you'd get\"   <- not \"book a call\"")
print("```")
print()
print("| | |\n|---|---|")
for a, b in [
    ("**The ask is a person, never a call**",
     "Zero of ten competitors puts a call in the button. **\"See who you'd get\"** is the "
     "category's grammar"),
    ("**Never \"80% less\"**",
     "Two of eight headlines already say it verbatim. It is the leader's axis and we have no "
     "track record to win it with"),
    ("**No employment language, in any of the four**",
     "No *apply*, no *join*, no *hiring now*, and the bench page must read as a **supplier "
     "catalogue for buyers**, not a job board. One reviewer tick costs 10–29% on CAC "
     "([`SUPPLY-DEMAND.md`](../SUPPLY-DEMAND.md))"),
    ("**The face in the ad must be the face on the page**",
     "Message match is the largest silent conversion killer, and here it is literal — the same "
     "person, the same number")]:
    print(f"| {a} | {b} |")

# ------------------------------------------------------- 9. the landing page
print("\n---\n\n## 9. The landing page\n")
print("One URL. What varies by cell, and what does not:\n")
print("| # | Block | Taken from | Varies? |\n|---|---|---|---|")
for a, b, c, d in [
    ("1", "**Three graded people, face up, above the fold** — name, country, the test they "
          "passed, the measured number",
     "Somewhere (9 with prior employers) · Athyna (40+ with rates) · Genius (9 with salaries)",
     "**Per role.** This is the cost"),
    ("2", "Hero line above them: the ICP + size qualifier", "our ad, matched", "**No**"),
    ("3", "**Role picker — \"which seat is open?\"**", "Athena's role-select entry", "**No** — it *is* the variation"),
    ("4", "The volume calculator", "Somewhere's salary tool · GrowthAssistant's comparison table",
     "**Labels only**"),
    ("5", "**Unlock form** — email, role, one sizing question", "Genius's 1-minute form",
     "**No**"),
    ("6", "How it works — three steps, no paid gate", "GrowthAssistant's intro-call flow", "**No**"),
    ("7", "**Published price** — 30–35% one-time, EOR at $477/mo",
     "GrowthAssistant $3,500/mo · Hireframe $2,500/mo · Genius 25%", "**No**"),
    ("8", "**12-month unlimited replacement**", "Genius's 6-month guarantee — **we double it**",
     "**No**"),
    ("9", "Objections: why India · why not a freelancer · why not AI", "—", "**No**"),
    ("10", "Founder block — named human, face, registered address",
     "nobody does this, and it is the one advantage of being one person", "**No**"),
]:
    print(f"| {a} | {b} | {c} | {d} |")
print("\n### The three things the competitors do that we should copy exactly\n")
print("| | |\n|---|---|")
for a, b in [
    ("**People above the fold, with numbers attached**",
     "Four of eight do it. Ours is stronger because a **measured before/after on a real test** is "
     "falsifiable and a headshot with a prior employer is not"),
    ("**Publish the price**",
     "Three of eight publish. **Vidchops hides theirs behind an \"Unlock Pricing\" button**, which "
     "tells you what hiding it signals. An unknown operator cannot afford to look evasive"),
    ("**Beat the guarantee, since it is the cheapest differentiator on the page**",
     "Genius offers **6-month** replacement and *\"100% refund if you don't hire\"*. **12 months "
     "unlimited** is strictly better and costs nothing until it is used")]:
    print(f"| {a} | {b} |")
print("\n### And the one thing to do that none of them does\n")
print("> **Show the test, not just the person.** Every competitor shows a photo, a title and a")
print("> price. **None shows the work sample or the score.** That is the entire `TRUECLAIM`")
print("> position from [`MODEL-V2.md`](../MODEL-V2.md) §8, and on this page it is one extra line")
print("> per profile: *the test they were given, and the number they hit.*\n")

print("---\n\n## 10. What this changes from the last pass\n")
print("| Last time | Now | Why |\n|---|---|---|")
for a, b, c in [
    ("Qualifying gate ranked **1st**", f"**{[x.key for x in BY].index('gate')+1}th**",
     "Zero of ten competitors gates. Friction is how a *known* brand filters; an unknown one has "
     "to give before it asks"),
    ("Calculator was the conversion event",
     f"**Supporting block ({[x.key for x in BY].index('calc')+1}rd on its own); the quiz is the "
     f"event**",
     "The calculator proves the volume problem. **It does not prove you can judge talent** — and "
     "that is the objection that actually stops the sale"),
    ("Free sample on their asset ranked 3rd", f"**{[x.key for x in BY].index('free')+1}th**",
     "No competitor does it, and at 136 founder hours a month it was never runnable by one person"),
    ("Bench preview ranked 6th and was penalised",
     f"**{[x.key for x in BY].index('bench')+1}nd**, and the quiz that routes to it is "
     f"**{[x.key for x in BY].index('quiz')+1}st**",
     "I scored it down for needing a bench and for Employment-category risk. The bench is work the "
     "business needs anyway, and **four operating competitors show candidates to buyers without "
     "apparent issue**"),
    ("Pricing was not examined", "**Examined, and it constrains the funnel**",
     "GrowthAssistant's $3,500/mo cannot clear the 30-day 1.5:1 test. §6")]:
    print(f"| {a} | {b} | {c} |")
print("\n**What has not changed:** one page and one ad set, the ICP x role matrix living in the")
print("creative, the one-time fee, the 12-month guarantee, the EOR attachment, and the rule that")
print("**a role with no measurable delta is not a role to launch.**\n")
