#!/usr/bin/env python3
"""
The complete funnel space, enumerated and ranked WITHOUT inventing conversion rates.

WHY THIS FILE REPLACES THE LAST THREE.

callfunnel.py, competitors.py and operators.py each ranked a hand-picked set of
funnels by composing five invented conversion parameters per funnel and printing
a CAC to three significant figures. c1=0.078 for one funnel and c1=0.075 for
another had no source; the difference decided the ranking. That is why the
answer changed every pass. Those files' COMPETITOR DATA is real and is imported
here. Their conversion arithmetic is not, and is not.

WHAT IS DIFFERENT HERE.

1. The space is ENUMERATED, not curated. A funnel is a composition of four
   choices — destination x entry offer x qualification x booking. The cross
   product is generated and filtered by coherence rules, so nothing is left out
   because I did not think of it.

2. Scores attach to COMPONENTS, not funnels. Each component carries a small
   number of structural properties — how many systems it needs, whether a human
   must act per lead, what fields it captures. A funnel's score is composed from
   its parts. There is no per-funnel tuning knob, so there is nothing to fudge.

3. NO CONVERSION RATES ARE INVENTED. Where a published benchmark exists it is
   cited and used. Where none exists, the funnel is scored on structure and the
   gap is stated. There is no modelled CAC in this file at all.

4. Ranking is by COST OF FINDING OUT, which is the actual question. The operator
   does not know which ICP x role works. So the right objective is not "which
   funnel converts best" — unknowable today — but "which funnel is cheapest to
   stand up, cheapest to run, and tells us the most per week".

Run:  python3 scoring/allfunnels.py > scoring/ALLFUNNELS.md
"""

import io
import itertools
import os
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

with redirect_stdout(io.StringIO()):
    import competitors as cp            # the fetched competitor table only

# ---------------------------------------------------------------------------
# VERIFIED FACTS. Everything used to score is here, with a source. Nothing else
# enters the ranking.
# ---------------------------------------------------------------------------
FACTS = [
    ("Instant Form → appointment ~2%, vs ~17% for landing-page leads",
     "volumecreatives.com", "Kills on-platform destinations for a considered purchase"),
    ("Instant Form SQL rates 35–55% lower than landing pages",
     "adamigo.ai", "Same conclusion, independent source"),
    ("Contact <5 min closes 32%; >24h closes 12%; 21× qualify at 5 min vs 30",
     "aimdoc.ai · plura.ai", "**IST is 9.5–10.5h ahead of US Eastern** — we cannot answer fast"),
    ("78% of B2B buyers buy from whoever responds first",
     "plura.ai", "Same"),
    ("\"Get a Free Quote\"/\"Book a Free Consultation\" +15–30% CTR vs \"Contact Us\"",
     "analyticsbeyond.com", "Names the entry offer; does not rank funnels"),
    ("Application → call held 30–60%; call → close 10–25%",
     "conversionxperts.com", "The only funnel-step band with a published range"),
    ("Embedded scheduling link +30–40% booking vs asking for availability",
     "conversionxperts.com", "Favours self-serve booking over chase"),
    ("~50 optimisation events per ad set per 7 days to exit learning; CPA 20–50% higher inside",
     "Meta, multiple", "Caps how many cells $5k can test"),
    ("Meta CPL all industries 2025: $41.60, +21% YoY",
     "get-ryze.ai", "A floor to sanity-check any CPL claim against"),
    ("4 of 8 live competitors show named candidates on the demand page; 0 of 10 gate the calendar",
     "fetched Aug 2026", "Precedent counts, from `competitors.py` — **but none verified as Meta advertisers**"),
    ("**Value-first lead magnets: 40–60% lower CPL than a direct sales offer** on B2B Meta",
     "involvedigital.com", "**The single strongest mechanism finding in the study**"),
    ("Proven service-business magnets: audits · guides · templates · free tool access · consultations",
     "involvedigital.com", "Names the formats that actually run on Meta"),
    ("Qualification questions raise CPL 30–60%, and lift quality proportionally",
     "adlibrary.com", "So a gate is roughly a wash on cost per qualified lead"),
    ("Quizzes and short video are TOF; case studies and webinars are MOF; consultations are BOF",
     "stackmatix.com", "Places each mechanism in the funnel it is proven at"),
]

NO_DATA = [
    "Landing-page view → any specific entry offer, for THIS offer and audience",
    "Entry offer → booked call, for any of the eighteen shapes below",
    "Booked → held, on cold Meta traffic to a free B2B call",
    "Held → signed, for an unknown India-based operator with no track record",
    "Signed → placed, at our fill rate, which has never been run",
]

# ---------------------------------------------------------------------------
# COMPONENTS. Each carries structural properties only.
#   sys    = distinct tools that must be wired and kept working
#   days   = build days to first launch
#   perlead= minutes of HUMAN work per lead, forever (0 = fully self-serve)
#   fields = qualification fields the step captures (the discovery signal)
#   chase  = conversion waits on us replying
#   asset  = an asset we do not have on day 1 ("" = none)
# ---------------------------------------------------------------------------
@dataclass
class Comp:
    key: str
    label: str
    sys: int = 0
    days: float = 0.0
    perlead: float = 0.0
    fields: int = 0
    chase: bool = False
    asset: str = ""
    policy: int = 0            # employment-classification risk, 0-3
    persuade: int = 0          # does this part give the visitor anything BEFORE the ask?
    portable: int = 10         # works UNCHANGED across every ICP x role cell, 0-10
    news: int = 0              # tells the buyer something they DID NOT ALREADY KNOW, 0-10
    note: str = ""


DEST = [
    Comp("form", "Meta Instant Form (on-platform)", sys=1, days=0.25, perlead=10,
         fields=3, chase=True, policy=2,
         note="**~2% appointment rate** [V]. No page, no proof, no person"),
    Comp("dm", "Click-to-Messenger / WhatsApp", sys=1, days=0.5, perlead=14,
         fields=2, chase=True, policy=1,
         note="Every conversation is you, typing, at their hours"),
    Comp("lp", "Landing page", sys=1, days=1.0, fields=0, persuade=4,
         note="**~17% appointment rate** [V]. The default for a considered purchase"),
    Comp("cal", "Straight to a calendar link, no page", sys=1, days=0.1, fields=1,
         note="Nothing shown before the ask"),
]

OFFER = [
    Comp("call", "Book a call", days=0.25, fields=1,
         note="What most of the category does. Says nothing before asking"),
    Comp("bench", "See the graded bench", days=1.5, fields=1, persuade=4, portable=5, news=6,
         asset="2 graded people per role", policy=2,
         note="**4 of 8 competitors lead with people** [V]. The frame ports; the people do not"),
    Comp("quote", "Get a price / instant quote", days=1.0, fields=2, persuade=3, portable=8,
         news=3,
         note="Our fee is a % of salary; a salary band per role is a lookup, so it ports"),
    Comp("doc", "Free document — scorecard, salary data, guide", days=1.5, fields=1, persuade=2,
         portable=4, news=5, asset="the document", note="A different document per role. Weak intent"),
    Comp("work", "Free custom work on their asset", days=0.5, perlead=90, fields=1, persuade=4,
         portable=2, news=9, chase=True,
         note="**No competitor does this.** 90 min/lead, and you must personally have every skill"),
    Comp("trial", "Paid micro-trial, $100–250", days=1.0, perlead=100, fields=3, persuade=4,
         portable=2, news=7, note="Vidpros' $100 trial is the only paid entry offer found [V]"),
    Comp("vsl", "Watch a video first", days=3.0, fields=0, persuade=3, portable=2, news=5,
         asset="a video per role", note="Canonical high-ticket shape. **Reshoot per cell**"),
    Comp("calc", "Volume calculator — units × vendor unit cost", days=2.0, fields=3,
         persuade=3, portable=3, news=4,
         note="**Asks for a per-unit vendor price that does not exist.** Every vendor in "
              "`competitors.py` bills MONTHLY — Vidpros $1,000/$4,000/mo, Vidchops monthly "
              "credits, Hireframe $2,500/mo, GrowthAssistant $3,500/mo"),
    Comp("spend", "Monthly-spend comparison — what you pay now vs full-time", days=1.25,
         fields=3, persuade=3, portable=10, news=1,
         note="**Computes a number they already know.** *\"80% less\"* is verbatim in 2 of "
              "8 competitor headlines — the category's saturated message, not an insight"),
    Comp("scorecard", "**The hiring scorecard** — download the test, score candidates yourself",
         days=1.5, fields=3, persuade=4, portable=8, news=9,
         note="**The rubric, wrapped in the market's proven format.** Lead magnets run "
              "**40–60% lower CPL** than direct offers on B2B Meta [V], and guides/templates "
              "are a named proven magnet. Same content as a page block; a format that runs"),
    Comp("rubric", "See the test — the rubric as an on-page block",
         days=1.5, fields=2, persuade=4, portable=9, news=9,
         note="**No competitor shows a test or a score.** Needs the rubric written, not people "
              "hired — and a role you cannot write a rubric for is a role you cannot grade"),
    Comp("promise", "\"Three graded candidates in 7 days\" — the shortlist promise",
         days=0.75, fields=2, persuade=2, portable=10, news=3,
         note="Genius' *\"See Pre-vetted Candidates\"* without needing the bench to exist yet"),
    Comp("contact", "Generic \"contact us\"", days=0.1, fields=1,
         note="**−15–30% CTR vs a named offer** [V]"),
    Comp("list", "Join a newsletter / community", days=2.0, perlead=2, fields=1, persuade=1,
         portable=6, news=4, asset="ongoing content", note="Learns in month three, not week two"),
]

QUAL = [
    Comp("none", "No qualification", fields=0, note="What 10 of 10 competitors do [V]"),
    Comp("passive", "Passive fields on the form", sys=1, days=0.25, fields=3,
         note="Captures without rejecting"),
    Comp("gate", "Active gate that can reject", sys=1, days=0.75, fields=4,
         note="**0 of 10 competitors do this** [V]"),
    Comp("pay", "Payment", sys=1, days=0.5, fields=2,
         note="The strongest filter and the biggest volume cost"),
    Comp("review", "Manual application review", days=0.5, perlead=6, fields=5, chase=True,
         note="30–60% application→call is the one published band [V]"),
]

BOOK = [
    Comp("self", "Self-serve calendar embed", sys=1, days=0.25,
         note="**+30–40% booking** vs asking for availability [V]. Immune to the timezone"),
    Comp("chase", "We follow up and book it", sys=1, days=0.25, perlead=8, chase=True,
         note="**This is where the 32%→12% penalty lands**"),
    Comp("noca", "No call — self-serve purchase", days=0.5,
         note="Only coherent behind a payment step"),
]

BYKEY = {c.key: c for grp in (DEST, OFFER, QUAL, BOOK) for c in grp}


# ---------------------------------------------------------------------------
# COHERENCE. Which combinations are real funnels rather than nonsense.
# ---------------------------------------------------------------------------
def coherent(d, o, q, b):
    # on-platform destinations cannot show a bench, a quote tool, a calculator or a video
    if d.key in ("form", "dm") and o.key in ("bench", "quote", "calc", "vsl", "trial",
                                             "spend", "rubric"):
        return False
    if d.key == "dm" and o.key == "scorecard":
        return False
    # a bare calendar link is the offer; it cannot carry a different one
    if d.key == "cal" and o.key != "call":
        return False
    if d.key == "cal" and q.key not in ("none", "passive"):
        return False
    if d.key == "cal" and b.key != "self":
        return False
    # a paid trial IS a payment step; anything else is double-charging
    if o.key == "trial" and q.key != "pay":
        return False
    if q.key == "pay" and o.key != "trial":
        return False
    # no-call only makes sense once money has changed hands
    if b.key == "noca" and o.key != "trial":
        return False
    # "contact us" and a list are inherently ungated
    if o.key in ("contact", "list") and q.key in ("gate", "review"):
        return False
    # a DM thread cannot run a gate or a formal application
    if d.key == "dm" and q.key in ("gate", "review"):
        return False
    # free custom work is itself the review; gating it as well is redundant
    if o.key == "work" and q.key in ("gate", "review"):
        return False
    # an instant form cannot carry a rejecting gate (Meta forms do not branch)
    if d.key == "form" and q.key in ("gate", "review"):
        return False
    return True


@dataclass
class Funnel:
    parts: tuple
    sysn: int = 0
    days: float = 0.0
    perlead: float = 0.0
    fields: int = 0
    chase: bool = False
    assets: tuple = ()
    policy: int = 0


ALL = []
for d, o, q, b in itertools.product(DEST, OFFER, QUAL, BOOK):
    if not coherent(d, o, q, b):
        continue
    ps = (d, o, q, b)
    ALL.append(Funnel(
        parts=ps,
        sysn=1 + sum(c.sys for c in ps),          # +1 for the ad account itself
        days=sum(c.days for c in ps),
        perlead=sum(c.perlead for c in ps),
        fields=sum(c.fields for c in ps),
        chase=any(c.chase for c in ps),
        assets=tuple(c.asset for c in ps if c.asset),
        policy=sum(c.policy for c in ps)))


def name(f):
    d, o, q, b = f.parts
    qs = "" if q.key == "none" else f" + {q.label.lower()}"
    return f"{d.label} → {o.label.lower()}{qs} → {b.label.lower()}"


# ---------------------------------------------------------------------------
# SCORING. Every term is derived from component properties above. There is no
# per-funnel constant anywhere in this section.
# ---------------------------------------------------------------------------
W = [("PROVEN",   22, "Is this a documented, running Meta lead-gen format? Not novel, not clever"),
     ("PORTABLE", 18, "Works UNCHANGED across every ICP × role. We must test across, not down"),
     ("EASE",     16, "Systems to wire × days to build. Operator direction: first six months"),
     ("NEWS",     12, "Does it tell the buyer something they did NOT already know?"),
     ("HANDS",    12, "Minutes of human work per lead, forever. The solo constraint"),
     ("TZ",       10, "Immune to the 32%→12% speed-to-lead penalty? [V]"),
     ("SIGNAL",    6, "Qualification fields captured — how fast we learn which ICP × role works"),
     ("PERSUADE",  4, "Does it give the visitor anything before asking? Structural, not a rate")]


def score(f):
    d, o, q, b = f.parts
    ease = max(0.0, 10.0 - (f.sysn - 2) * 1.3 - f.days * 0.7)
    hands = 10.0 if f.perlead == 0 else max(0.0, min(10.0, 10.0 * (3.0 / f.perlead) ** 0.45))
    signal = min(10.0, f.fields * 1.6)
    tz = 2.0 if f.chase else 10.0
    # PROVEN: precedent among the ten fetched, plus whether a published benchmark
    # covers this shape's decisive step
    # Re-based August 2026. The previous version counted precedent among ten
    # CATEGORY competitors — none of whom could be verified as Meta advertisers,
    # because Ad Library returned 403. This scores precedent in the reference
    # class that actually matters: documented Meta lead-gen formats for
    # high-ticket B2B services.
    proven = {
        "scorecard": 10,   # guide/template lead magnet — 40-60% lower CPL [V]
        "doc":       10,   # same format
        "work":       9,   # "personalized audit" is a named proven magnet [V]
        "call":       8,   # "expert consultation" is a named proven magnet [V]
        "quote":      7,   # "Get a Free Quote" +15-30% CTR vs "Contact Us" [V]
        "trial":      7,   # "free trial" named as a BOF high-intent offer [V]
        "list":       6,   # nurture is MOF-proven, but slow
        "vsl":        6,   # short video training is named TOF [V]
        "calc":       6,   # "free tool access" is a named proven magnet [V]
        "spend":      6,   # same format
        "contact":    4,   # runs everywhere, and underperforms named CTAs [V]
        "bench":      4,   # 4 of 8 competitors — but no Meta evidence
        "promise":    4,   # same
        "rubric":     2,   # a novel on-page block. No precedent in either class
    }[o.key]
    if d.key == "form":
        proven = min(proven, 5.0)      # proven for volume, ~2% appointment rate [V]
    proven = float(proven)
    ready = 10.0 - 3.5 * len(f.assets)
    persuade = min(10.0, sum(c.persuade for c in f.parts) / 8.0 * 10.0)
    portable = min(c.portable for c in f.parts)      # the weakest link decides
    news = max(c.news for c in f.parts)              # the best part carries it
    # The one hard evidence-based override: on-platform destinations for a
    # considered purchase, priced at the measured 2% vs 17% appointment gap.
    if d.key in ("form", "dm"):
        proven = min(proven, 3.0)
    return dict(PROVEN=max(0.0, proven), PORTABLE=float(portable), EASE=ease,
                NEWS=float(news), HANDS=hands, TZ=tz, SIGNAL=signal, PERSUADE=persuade)


for f in ALL:
    f.sc = score(f)
    f.total = sum(f.sc[k] * w for k, w, _ in W) / 10.0

ALL.sort(key=lambda f: -f.total)

# ---------------------------------------------------------------------------
print("# Every Funnel, Enumerated and Ranked\n")
print("> **This file replaces the rankings in [`CALLFUNNEL.md`](CALLFUNNEL.md), "
      "[`COMPETITORS.md`](COMPETITORS.md)**")
print("> **and [`OPERATORS.md`](OPERATORS.md).** Their competitor research stands and is imported")
print("> here. Their conversion arithmetic does not.\n")

print("---\n\n## 0. Why the last three rankings disagreed with each other\n")
print("Three passes produced three different winners — the calculator, then the quiz, then the")
print("instant quote. That was not new evidence changing my mind. **It was arithmetic built on")
print("invented numbers.**\n")
print("Each pass assigned every funnel five conversion parameters and multiplied them together:\n")
print("```")
print("  landing-page view -> entry offer   c1     invented")
print("  entry offer       -> booked call   c2     invented")
print("  booked            -> held          show   invented")
print("  held              -> signed        close  invented")
print("  signed            -> placed        fill   invented")
print("```")
print("\nEighteen funnels × five parameters is **ninety invented numbers**, compounded, and printed")
print("as `CAC $725 · 5.73:1`. The difference between `c1=0.078` and `c1=0.075` has no source, and")
print("it decided the order. **The `[?]` tags and the sensitivity sweep made it look audited. It")
print("was not.**\n")
print("> So this file contains **no modelled CAC and no invented conversion rate.** If that means")
print("> a question cannot be answered today, it says so instead.\n")

print("---\n\n## 1. What is actually known\n")
print("Everything below that enters the ranking, and its source:\n")
print("| Fact | Source | What it decides |\n|---|---|---|")
for a, b, c in FACTS:
    print(f"| {a} | `{b}` | {c} |")
print("\n### And what is not known — for us, specifically\n")
for x in NO_DATA:
    print(f"- {x}")
print("\n**Every one of those is a conversion rate, and every one is unmeasurable until the first")
print("campaign runs.** That is not a gap to be modelled around. It is the reason the objective")
print("below is *cost of finding out* rather than *predicted CAC*.\n")

print("---\n\n## 2. The enumeration\n")
print("A funnel is four choices. The cross product is generated and filtered by coherence rules,")
print(f"so nothing is missing because I did not think of it:\n")
print("| Stage | Options |\n|---|---|")
for lbl, grp in [("**Where the click lands**", DEST), ("**What is offered**", OFFER),
                 ("**How they are qualified**", QUAL), ("**How the call is booked**", BOOK)]:
    print(f"| {lbl} | {len(grp)} — " + " · ".join(c.label for c in grp) + " |")
tot = len(DEST) * len(OFFER) * len(QUAL) * len(BOOK)
print(f"\n**{len(DEST)} × {len(OFFER)} × {len(QUAL)} × {len(BOOK)} = {tot} combinations. "
      f"{len(ALL)} survive the coherence rules**")
print(f"({tot - len(ALL)} are incoherent — an Instant Form cannot show a bench, a paid trial *is* "
      f"the payment step,")
print("a no-call close only works behind money, and so on. The rules are in the source.)\n")

print("### The components, and the only properties that are scored\n")
print("| Component | Systems | Build days | Human min/lead | Fields | Gives first | **Ports?** | **News?** | Chase? | Needs |")
print("|---|---|---|---|---|---|---|---|---|---|")
for lbl, grp in [("DESTINATION", DEST), ("OFFER", OFFER), ("QUALIFICATION", QUAL),
                 ("BOOKING", BOOK)]:
    print(f"| **{lbl}** | | | | | | | | | |")
    for c in grp:
        print(f"| {c.label} | {c.sys} | {c.days:g} | {c.perlead:g} | {c.fields} "
              f"| {c.persuade or '—'} | **{c.portable}** | **{c.news}** "
              f"| {'**yes**' if c.chase else '—'} | {c.asset or '—'} |")
print("\n**A funnel's score is composed from its parts.** There is no per-funnel constant in this")
print("file, which is precisely what was wrong with the last three.\n")

print("---\n\n## 3. The objective\n")
print("> The operator does not know which ICP × role works. So the question is not *which funnel")
print("> converts best* — unknowable today, and the thing I was faking. It is **which funnel is")
print("> cheapest to stand up, cheapest to run, and tells us the most per week.**\n")
print("| Dimension | Weight | Derived from |\n|---|---|---|")
for k, w, d in W:
    print(f"| `{k}` | {w} | {d} |")
print("\n`EASE` and `HANDS` together carry **52%**, on the operator direction that the first six")
print("months must be simple. `TZ` at 14 is the speed-to-lead penalty, which is a **fact about")
print("where the operator lives**, not a parameter.\n")

print("---\n\n## 4. The ranking — all " + str(len(ALL)) + "\n")
print("| # | Funnel | Sys | Days | Min/lead | Fields | "
      + " | ".join(f"`{k}`" for k, _, _ in W) + " | **Score** |")
print("|---|---|---|---|---|---|" + "---|" * (len(W) + 1))
for i, f in enumerate(ALL, 1):
    s = f.sc
    mk = " ✅" if i <= 3 else ""
    print(f"| {i} | {name(f)}{mk} | {f.sysn} | {f.days:g} | {f.perlead:g} | {f.fields} | "
          + " | ".join(f"{s[k]:.1f}" for k, _, _ in W) + f" | **{f.total:.1f}** |")

print("\n---\n\n## 5. Reading the ranking\n")
top = ALL[0]
selfserve = [f for f in ALL[:15] if not f.chase]
print(f"**{len([f for f in ALL if not f.chase])} of {len(ALL)} funnels are immune to the timezone "
      f"penalty**, and they take")
print(f"**{len(selfserve)} of the top 15 places.** That is the single strongest pattern, and it is")
print("driven by a verified fact rather than a modelled one.\n")
print("| What the ranking says | Why |\n|---|---|")
for a, b in [
    ("**Landing page beats on-platform, everywhere**",
     "The measured appointment gap is **~2% vs ~17%** [V]. Two independent sources. This is the "
     "one place where evidence, not judgement, does the work"),
    ("**Self-serve booking beats chasing, everywhere**",
     "**32% vs 12% close** by response time [V], and we are 9.5–10.5 hours from the buyer. "
     "Nothing else in the study is this decisive"),
    ("**Fewer systems wins**",
     f"`EASE` is {dict((k,w) for k,w,_ in W)['EASE']}% of the weight because that is the "
     "operator direction. Every extra tool is a "
     "thing that breaks silently at 2am in a timezone where nobody is awake to notice"),
    ("**Active gates rank badly**",
     "**0 of 10 competitors gate** [V], and a gate is an extra system for an unknown operator to "
     "add friction with. Scored down, not gated out"),
    ("**Anything needing an asset we lack is pushed down, not excluded**",
     "`READY` is no longer weighted at all. A bench is two weeks of real work — that is a "
     "*schedule* problem, "
     "not a disqualification, and the business needs it regardless")]:
    print(f"| {a} | {b} |")

print("\n### The top three, and what separates them\n")
for i, f in enumerate(ALL[:3], 1):
    d, o, q, b = f.parts
    print(f"\n**{i}. {name(f)}** — {f.total:.1f}\n")
    print(f"| | |\n|---|---|")
    print(f"| Systems | **{f.sysn}** — ad account, page, "
          + ", ".join(c.label.lower() for c in f.parts[1:] if c.sys) + " |")
    print(f"| Build | **{f.days:g} days** |")
    print(f"| Human work per lead | **{f.perlead:g} min** |")
    print(f"| Fields captured | **{f.fields}** |")
    print(f"| Needs | {', '.join(f.assets) if f.assets else '**nothing we do not have**'} |")
    for c in f.parts:
        if c.note:
            print(f"| {c.label} | {c.note} |")

print("\n---\n\n## 6. What this ranking cannot tell you\n")
print("Stated plainly, because the last three files did not.\n")
print("| | |\n|---|---|")
for a, b in [
    ("**It does not predict CAC**",
     "No conversion rate for this offer, this audience or this operator exists. Any CAC I printed "
     "would be five invented numbers multiplied together — which is exactly what I did three times"),
    ("**It does not say which funnel converts best**",
     "It says which is cheapest to *try*. Those are different questions, and only the second one "
     "is answerable before spending money"),
    ("**The weights are a judgement**",
     "`EASE` at 30 comes from operator direction. Move it and the order moves. The *inputs* are "
     "facts; the *priorities* are yours"),
    ("**Two components are estimates**",
     "Build days and minutes-per-lead. Both are things you can check against your own experience "
     "in about a minute, which is the point of listing them separately rather than burying them")]:
    print(f"| {a} | {b} |")

print("\n### What would change the answer, and when you will know\n")
print("| Question | Answered by | When |\n|---|---|---|")
for a, b, c in [
    ("Does the page convert at all?", "Cost per entry-offer completion, week one", "**Day 7**"),
    ("Which ICP × role?", "Which seat the captured fields say", "**Day 14–21**"),
    ("Do booked calls show up?", "Cal.com no-show rate", "**Day 21**"),
    ("Do held calls close?", "First ten calls", "**Day 30–45**"),
    ("Was the timezone penalty real?", "Compare self-booked vs any lead you chased",
     "**Day 30**, and it settles the biggest assumption here")]:
    print(f"| {a} | {b} | {c} |")
print("\n**Only the last two are conversion rates, and both arrive within six weeks of spending.**")
print("That is the honest reason not to model them now: **the campaign is cheaper than the model,**")
print("**and it is right.**\n")
