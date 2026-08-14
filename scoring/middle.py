#!/usr/bin/env python3
"""
The middle slot: what sits between the landing page and the self-serve calendar.

The enumeration in allfunnels.py fixed the two ends — a landing page, and a
self-serve calendar — on verified evidence:

  landing page   ~17% appointment rate vs ~2% on-platform [V]
  self-serve     32% close inside 5 min vs 12% after 24h [V], and we are
                 9.5-10.5 hours from the buyer, so we cannot chase

What it did NOT settle is the middle. Ranks 1-7 of that shape are three offers
and nothing else, but they sit inside 3.1 points of each other on a 100-point
scale whose weights are a judgement. THE MODEL CANNOT SEPARATE THEM.

What separates them is time. The operator's constraint is that this must work on
day 1 AND still be working on day 90, and the three have completely different
shapes over that window:

  calculator    works day 1, never improves, captures the most data
  quote         works day 1, never improves, cheapest to build, anchors on price
  bench         CANNOT work day 1, improves to day 60, then starts eating itself

This file states what each needs, what each produces, and what happens to each
at day 1, day 30 and day 90. No conversion rates are invented; every claim is
either a structural fact about the asset or a cited benchmark.

Run:  python3 scoring/middle.py > scoring/MIDDLE.md
"""

import io
import os
import sys
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with redirect_stdout(io.StringIO()):
    import allfunnels as A

SHAPE = [f for f in A.ALL if f.parts[0].key == "lp" and f.parts[3].key == "self"]
RANK = {id(f): A.ALL.index(f) + 1 for f in A.ALL}

print("# The Middle Slot — Calculator vs Quote vs Bench\n")
print("> `LP → ??? → self-serve calendar`. The two ends are settled on verified evidence.")
print("> **This is about the question mark**, over day 1 to day 90.\n")

# ---------------------------------------------------------------- 1. why three
print("---\n\n## 1. Why those three and not the other seven\n")
print(f"Of the **{len(SHAPE)}** funnels in [`ALLFUNNELS.md`](ALLFUNNELS.md) with this exact shape, "
      f"here is the top of the list —")
print("**ranks 1 through 7 are three offers and nothing else:**\n")
print("| Overall rank | Offer | Qualification | Build days | Min/lead | Fields | `PERSUADE` "
      "| Score |")
print("|---|---|---|---|---|---|---|---|")
for f in SHAPE[:9]:
    o, q = f.parts[1], f.parts[2]
    mk = " ←" if RANK[id(f)] == 8 else ""
    print(f"| {RANK[id(f)]}{mk} | **{o.label}** | {q.label} | {f.days:g} | {f.perlead:g} "
          f"| {f.fields} | {f.sc['PERSUADE']:.1f} | **{f.total:.1f}** |")
print("\n**The break comes at rank 8**, where *book a call* appears at 75.9. The reason is one")
print("column: `PERSUADE` drops from 8.8–10.0 to **5.0**, because *book a call* and *contact us*")
print("give the visitor nothing before asking for their time.\n")
print("### The four that were beaten, and by what\n")
print("| Offer | `PERSUADE` | Why it loses |\n|---|---|---|")
for a, b, c in [
    ("**Watch a video first**", "8.8",
     "Same persuasive power as a calculator, but **4.5–5 build days** and *a video per role* — "
     "so a second cell means a second shoot"),
    ("**Free document** — scorecard, salary guide", "7.5",
     "Needs an asset we do not have, persuades less, and captures fewer fields. Strictly dominated"),
    ("**Paid micro-trial**", "10.0",
     "Highest persuasion in the study and **100 minutes of your time per lead**. Ranks 28th on "
     "that alone"),
    ("**Free custom work on their asset**", "10.0",
     "**90 min/lead, forever.** Ranks **60th and 83rd**. The most persuasive thing you could do "
     "and the least survivable"),
]:
    print(f"| {a} | {b} | {c} |")
print("\n> The pattern: **the two things that persuade most are the two that cost your time per "
      "lead.**")
print("> Everything in the top 7 is self-serve at zero marginal minutes. That is the filter.\n")
print("**And the three finalists sit inside 3.1 points of each other.** The weights are my "
      "judgement,")
print("so that gap is noise. **The model has done what it can. The rest is §2.**\n")

# --------------------------------------------------------- 2. the time shapes
print("---\n\n## 2. The only thing that actually separates them: time\n")
print("| | **Calculator** | **Instant quote** | **Graded bench** |\n|---|---|---|---|")
rows = [
    ("What the visitor does",
     "Enters *their* volume and *their* vendor invoice",
     "Answers 3 questions, sees *our* price",
     "Looks at real people with test scores"),
    ("What it proves",
     "**Their problem is real** — in their own numbers",
     "**We are not hiding anything**",
     "**We can actually judge talent**"),
    ("What it does NOT prove",
     "That *we* can do anything", "That the work is any good", "That the price works for them"),
    ("**Can it exist on day 1?**",
     "**Yes** — needs nothing from us but arithmetic",
     "**Yes** — our fee is 30–35% of comp, and salary bands are published "
     "([`COMPETITOR-DATA.md`](../COMPETITOR-DATA.md) §2)",
     "**No.** Needs 2+ graded people *per role* first"),
    ("Build days", "3.5", "**2.5** — the cheapest", "3.0 *plus 2 weeks of sourcing and grading*"),
    ("Fields captured", "**6** — the most", "5", "4 — the fewest"),
    ("Improves over 90 days?", "**No.** Same arithmetic on day 90", "**No.** Same price",
     "**Yes** — 2 people becomes 15"),
    ("Precedent among the 10 fetched",
     "3 of 8 ship a calculator or comparison table",
     "3 of 8 publish a real price",
     "**4 of 8 show named candidates** — the most-precedented single element"),
]
for r in rows:
    print("| " + " | ".join(r) + " |")

print("\n---\n\n## 3. Day 1 · Day 30 · Day 90\n")
print("The column that matters, because an asset that is strong on day 1 and weak on day 90 is a")
print("different decision from one that is the reverse.\n")
print("### Calculator\n")
print("| | State | Note |\n|---|---|---|")
for a, b, c in [
    ("**Day 1**", "**Fully working**",
     "It only needs *their* inputs. Nothing about us has to exist yet — which is exactly why it "
     "survives a launch with no track record"),
    ("**Day 30**", "Unchanged, but **you now know the shape of the market**",
     "Every completion recorded their volume and their vendor spend. That is the demand map you "
     "do not currently have"),
    ("**Day 90**", "Unchanged",
     "**No decay and no compounding.** It works exactly as well and no better. The value it "
     "generated is in the data you collected, not in the asset")]:
    print(f"| {a} | {b} | {c} |")
print("\n### Instant quote\n")
print("| | State | Note |\n|---|---|---|")
for a, b, c in [
    ("**Day 1**", "**Fully working**",
     "30–35% of a published salary band is arithmetic. Somewhere publishes bands for 60+ titles"),
    ("**Day 30**", "Unchanged", "Removes the price objection from every call, from the first one"),
    ("**Day 90**", "Unchanged — **but now harder to change**",
     "**A published price is a commitment.** If close rate is low and price is the reason, you are "
     "revising a number strangers have already seen")]:
    print(f"| {a} | {b} | {c} |")
print("\n### Graded bench\n")
print("| | State | Note |\n|---|---|---|")
for a, b, c in [
    ("**Day 1**", "**Does not exist**",
     "2 weeks of sourcing and grading *per role* before the first ad. This is the whole cost"),
    ("**Day 30**", "4–6 people, and **it is now the strongest thing on the page**",
     "It answers the objection the other two cannot: *can this person judge talent?*"),
    ("**Day 90**", "**It starts eating itself**", "See §4 — this is the part nobody says out loud")]:
    print(f"| {a} | {b} | {c} |")

# ---------------------------------------------------- 4. the bench paradox
print("\n---\n\n## 4. The problem with the bench that only shows up around day 90\n")
print("> **A bench that works is a bench that empties.**\n")
print("Every placement removes your best proof from the page. The editor with the "
      "**41% → 68%**")
print("retention delta is the reason someone booked — and the moment you place them, they are")
print("someone's employee and their profile comes down.\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Why the competitors do not have this problem**",
     "Scale. Somewhere claims a **1.2M+ candidate pool**; Athyna publishes **40+** profiles. "
     "Placing ten people does not dent that. **At 6 people it is catastrophic**"),
    ("**What it costs**",
     "Continuous sourcing and grading, forever, at your personal hourly rate — and grading is the "
     "one task you cannot delegate, because *you doing the grading* is the entire claim"),
    ("**When it bites**",
     "Exactly when things are going well. **Success is what breaks it**, which is the worst "
     "possible failure mode to design in"),
    ("**The mitigation**",
     "Show the **test and the score**, not only the person. A retired profile can stay up as "
     "*\"placed — here is what they scored\"*, which keeps the proof and loses only the "
     "availability. **No competitor does this, because none of them shows scores at all**")]:
    print(f"| {a} | {b} |")

# ------------------------------------------------------------- 5. pros / cons
print("\n---\n\n## 5. Pros and cons, straight\n")
for title, pros, cons in [
    ("Calculator",
     [("**Works on day 1 with nothing from us**", "No asset, no track record, no bench"),
      ("**Captures the most data — 6 fields**", "Volume, vendor spend, role, size. This is the "
       "discovery instrument, and discovery is the day-1 job"),
      ("**It argues *their* problem, not our price**",
       "The buyer reaches the volume conclusion themselves, which is stronger than us asserting it"),
      ("**Zero minutes per lead**", "Fully self-serve, so the timezone cannot touch it"),
      ("**Precedented**", "Somewhere and Athyna both ship salary tools; GrowthAssistant ships a "
       "cost-comparison table")],
     [("**Proves nothing about us**",
       "Anyone can build a calculator. It does not answer *can you judge talent* — which is the "
       "objection that actually stops the sale"),
      ("**The most build days of the three — 3.5**", "And the only one that is genuinely custom "
       "code, so it is the one most likely to break silently"),
      ("**Garbage in**", "If they do not know their own vendor spend, the output is meaningless "
       "and the page has wasted its one moment"),
      ("**No compounding**", "Identical on day 90")]),

    ("Instant quote",
     [("**Cheapest to build — 2.5 days**", "The simplest of the three, and simplicity is the "
       "stated constraint"),
      ("**Works on day 1**", "30–35% of a published salary band. Pure arithmetic"),
      ("**Removes the price objection before the call**",
       "For an unknown operator this is the largest silent killer — people assume the worst and "
       "never ask"),
      ("**Publishing signals confidence**",
       "3 of 8 competitors publish. **Vidchops hides theirs behind an \"Unlock Pricing\" button**, "
       "which tells you what hiding reads as"),
      ("**+15–30% CTR on the ad**", "*\"Get a Free Quote\"* over *\"Contact Us\"*, measured [V]")],
     [("**It anchors the conversation on cost**",
       "[`MODEL-V2.md`](../MODEL-V2.md) §8 deliberately moved this business from price to quality. "
       "A quote-first page walks it back toward the axis where Somewhere and Genius already say "
       "*\"80% less\"*"),
      ("**A number from a stranger lands cold**",
       "$6,600 from an unknown India-based operator, before any proof, is a very different message "
       "from $6,600 after a work sample"),
      ("**Fewer fields — 5**", "Less discovery than the calculator"),
      ("**Hard to walk back**", "A published price seen by strangers is a commitment, and month-3 "
       "is exactly when you will want to test a different one")]),

    ("Graded bench",
     [("**Highest persuasion in the study — 10.0**",
       "Tied only with the two options that cost 90–100 minutes per lead"),
      ("**It answers the real objection**",
       "*Can this one person actually judge talent?* Nothing else on the page does"),
      ("**The most-precedented single element**",
       "**4 of 8 live competitors** put named candidates on the demand page"),
      ("**It compounds**", "2 people become 15. The only one of the three that is worth more on "
       "day 90 than day 1"),
      ("**It is the business**",
       "[`MINIMUM.md`](../MINIMUM.md) §6 — if you cannot produce one graded work sample with a "
       "measured delta, there is no business. **This work is not optional, only its timing is**")],
     [("**Cannot launch day 1**",
       "2 weeks of sourcing and grading per role. **The single biggest reason not to start here**"),
      ("**Fewest fields — 4**", "Weakest discovery instrument of the three, and discovery is the "
       "day-1 job"),
      ("**§4 — success empties it**", "The failure mode arrives exactly when it is working"),
      ("**Employment-classification exposure**",
       "Candidate profiles on the ad path is the clearest route to Meta reading this as an "
       "employment ad. **10–29% CAC tax** if it lands "
       "([`SUPPLY-DEMAND.md`](../SUPPLY-DEMAND.md))"),
      ("**Ongoing burden**", "The only one of the three with recurring work attached")]),
]:
    print(f"### {title}\n")
    print("| ✅ | |\n|---|---|")
    for a, b in pros:
        print(f"| {a} | {b} |")
    print("\n| ❌ | |\n|---|---|")
    for a, b in cons:
        print(f"| {a} | {b} |")
    print()

# ------------------------------------------------------------- 6. the answer
print("---\n\n## 6. The answer, and it is a sequence rather than a pick\n")
print("The three are not competing for one slot. **Two of them are the same object, and the third")
print("is a different phase.**\n")
print("### Calculator and quote are one block, not two\n")
print("> A calculator that ends in a price **is** a quote.\n")
print("They are enumerated separately because they are separately choosable. On a page they")
print("compose into one flow:\n")
print("```")
print("  How many ads a month do you ship?          ->  their volume")
print("  What does your studio/freelancer invoice?  ->  their spend")
print("  What would you ship if capacity were free? ->  their ceiling")
print("       |")
print("       v")
print("  Your cost per ad today          $1,333      <- the calculator")
print("  At 16/mo your vendor bills      $21,333")
print("  One full-time, all-in           $1,650")
print("  Our fee, one-time, 30%          $5,940      <- the quote")
print("  ------------------------------------------")
print("  The gap, year one               $228,056")
print("```")
print("\n**Marginal cost of adding the quote to the calculator: roughly zero.** The fee is one more")
print("line of arithmetic on a page that is already doing arithmetic. You get **6 fields**, both")
print("persuasion mechanisms, and one system.\n")
print("And it resolves the quote's worst con: **the price arrives *after* their own number**, not")
print("before it. $5,940 read directly after *$228,056 of gap* is a different sentence from "
      "$5,940")
print("read cold.\n")
print("### The bench is phase two, and its date is set by sourcing, not by the page\n")
print("| Phase | Middle slot | Why |\n|---|---|---|")
for a, b, c in [
    ("**Day 1–30**", "**Calculator + quote as one block**",
     "It is the only option that exists on day 1, and it is the strongest discovery instrument. "
     "Month one's job is finding out which ICP × role converts — not closing"),
    ("**Day 30–60**", "**Add the bench above it**",
     "By then you have graded people because you have been sourcing for the first placements "
     "anyway. The bench becomes the hero block; the calculator stays as the conversion event "
     "underneath"),
    ("**Day 60–90**", "**Bench leads, calculator converts, quote stays published**",
     "The bench answers *can you judge talent*; the calculator answers *is my problem big enough*. "
     "They are different objections and the page has room for both"),
]:
    print(f"| {a} | {b} | {c} |")
print("\n> **Nothing gets rebuilt.** The calculator block never moves and never changes. The bench")
print("> is added above it when it exists. That is one build, then one addition — which is the")
print("> whole point of choosing the day-1 option that needs nothing from us.\n")

print("### What would make me wrong\n")
print("| If this turns out to be true | Then |\n|---|---|")
for a, b in [
    ("**Buyers do not know their vendor spend**",
     "The calculator produces nothing and the block is dead weight. **Check this on the first five "
     "calls** — ask what they currently pay per ad. If they cannot answer, drop the calculator and "
     "run the quote alone, which needs no input from them"),
    ("**The volume argument does not land for agencies**",
     "The whole calculator premise fails for that ICP. It will show up as agencies completing the "
     "calculator and not booking — visible by day 21"),
    ("**Sourcing takes longer than two weeks**",
     "The bench slips to day 60–90. Nothing else changes, because nothing was built on it"),
    ("**Meta reads the bench as an employment ad**",
     "**10–29% on CAC.** Mitigation is to keep the bench as a *supplier catalogue for buyers* — "
     "no *apply*, no *join*, no availability language aimed at candidates"),
]:
    print(f"| {a} | {b} |")
print("\n---\n\n## 7. One thing to be clear about\n")
print("The 3.1-point spread between these three is **inside the noise of my own weighting.** I am")
print("not claiming the calculator beats the bench on the model — it does not, meaningfully.\n")
print("> **The sequencing argument is what decides it, and it rests on one hard fact: the bench")
print("> cannot exist on day 1 and the calculator can.** Everything else here is a tie-break.\n")
