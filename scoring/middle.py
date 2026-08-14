#!/usr/bin/env python3
"""
The middle slot, decided on PORTABILITY — the dimension the enumeration missed.

Operator correction: "calculator and quote are only for video ads / we need
something that we can test across."

Correct, and worse than stated. The volume calculator asks "what does your
studio invoice PER AD". Every vendor in competitors.py bills MONTHLY, including
both video vendors — Vidpros at $1,000/$4,000 a month and Vidchops on monthly
credits. So the per-unit price it asks for does not exist even in the vertical
it was designed for.

The deeper error: allfunnels.py ranked 105 funnels with no portability dimension
at all. PORTABLE is now a component property, taken as the WEAKEST LINK across a
funnel's parts, and weighted at 22 — the heaviest. That single change moves the
volume calculator from 1st to 32nd and the graded bench from 5th to 25th.

Run:  python3 scoring/middle.py > scoring/MIDDLE.md
"""

import io
import os
import sys
from contextlib import redirect_stdout

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with redirect_stdout(io.StringIO()):
    import allfunnels as A

RANK = {id(f): i + 1 for i, f in enumerate(A.ALL)}
BEST = {}
for f in A.ALL:
    BEST.setdefault(f.parts[1].key, f)

print("# What Actually Ports Across ICP × Role\n")
print("> The middle slot of `LP → ??? → self-serve calendar`, decided on the dimension the")
print("> enumeration was missing: **does it work unchanged across every cell we need to test?**\n")

# ---------------------------------------------------------------- 1. the error
print("---\n\n## 1. The volume calculator was wrong, and for a worse reason than \"it's video-only\"\n")
print("It asks: *\"what does your studio invoice **per ad**?\"*\n")
print("**No vendor in the study bills per unit.** From [`COMPETITORS.md`](COMPETITORS.md), "
      "fetched:\n")
print("| Vendor | Billing |\n|---|---|")
for a, b in [("**Vidpros** — video", "**$1,000/mo** part-time · **$4,000/mo** full-time"),
             ("**Vidchops** — video", "**Monthly subscription**, credits per month"),
             ("Hireframe", "**$2,500/mo**"),
             ("GrowthAssistant", "**$3,500/mo**"),
             ("Athena · Oceans", "Monthly"),
             ("Design subscriptions, agency retainers, BPOs", "Monthly")]:
    print(f"| {a} | {b} |")
print("\n> **Both video vendors bill monthly.** So the per-unit number the calculator asks for does")
print("> not exist in the buyer's head even in the vertical it was designed for. They would have to")
print("> divide a retainer by an output count to answer, and most cannot.\n")
print("**And the structural error underneath it:** [`ALLFUNNELS.md`](ALLFUNNELS.md) ranked "
      f"**{len(A.ALL)}** funnels")
print("with **no portability dimension at all.** I optimised for build simplicity and discovery")
print("signal, and never scored the thing that was actually required.\n")
print("`PORTABLE` is now a component property, taken as the **weakest link** across a funnel's")
print(f"parts — because one non-porting component breaks the whole funnel — and weighted at "
      f"**{dict((k, w) for k, w, _ in A.W)['PORTABLE']}**,")
print("the heaviest. What that one change does:\n")
print("| Offer | Ports | Best rank **before** | Best rank **now** |\n|---|---|---|---|")
for k, before in [("calc", "**1st**"), ("quote", "3rd"), ("bench", "5th"), ("call", "8th"),
                  ("doc", "15th"), ("vsl", "24th"), ("trial", "28th"), ("work", "60th")]:
    f = BEST[k]
    print(f"| {f.parts[1].label} | **{f.parts[1].portable}** | {before} | "
          f"**{RANK[id(f)]}th** |")
print("\n**The four options that need an asset rebuilt per role — video, free document, paid trial,")
print("free custom work — were already losing. Portability just makes the reason explicit.**\n")

# ------------------------------------------------------------ 2. what survives
print("---\n\n## 2. What ports, ranked\n")
print("| Offer | Ports | Best rank | Build days | Fields | `DESIRE` | Score |")
print("|---|---|---|---|---|---|---|")
for k, f in sorted(BEST.items(), key=lambda x: RANK[id(x[1])]):
    o = f.parts[1]
    mk = " ✅" if RANK[id(f)] <= 4 else ""
    print(f"| **{o.label}**{mk} | **{o.portable}** | {RANK[id(f)]} | {f.days:g} | {f.fields} "
          f"| {f.sc['DESIRE']:.0f} | {f.total:.1f} |")
print("\n**Three role-agnostic offers take the top four places**, and two of them did not exist in")
print("the previous enumeration because I had not thought to look for them.\n")

# ---------------------------------------------------------- 3. the three
print("---\n\n## 3. The three that survive\n")
print("| | **A. Monthly-spend comparison** | **B. See the test** | **C. Shortlist promise** |")
print("|---|---|---|---|")
for r in [
    ("The question it asks",
     "*\"What do you spend on this function per month?\"*",
     "*\"Here is the test every one of these takes before you meet them\"*",
     "*\"Three graded candidates in 7 days\"*"),
    ("Why it ports",
     "**Every function has a monthly spend**, and it is the unit every vendor actually bills in",
     "**Every role has a test.** The rubric changes; the mechanism does not",
     "**Nothing in it is role-specific at all**"),
    ("What it needs on day 1",
     "A salary band per role — a lookup, published for 60+ titles",
     "**A written rubric per role** — which you must write anyway to grade anyone",
     "Nothing"),
    ("Build days", "**2.75**", "3.0", "**2.25** — the cheapest"),
    ("Fields captured", "**6**", "5", "5"),
    ("What it proves", "Their spend is bigger than they thought", "**We know how to judge this work**",
     "Nothing yet — it is a promise"),
    ("Precedent", "Somewhere and Athyna both ship salary tools", "**Nobody. Zero of ten**",
     "Genius' *\"See Pre-vetted Candidates\"*"),
]:
    print("| " + " | ".join(r) + " |")

print("\n### A. Monthly-spend comparison\n")
print("| ✅ | |\n|---|---|")
for a, b in [
    ("**Ports perfectly — 10**", "Video, media buying, ops, design, books, support. Every one has a "
     "monthly spend, and the buyer knows it without doing arithmetic"),
    ("**One input**", "*\"What do you spend on this per month?\"* — against three for the volume "
     "calculator, two of which they could not answer"),
    ("**The volume argument survives, in new units**",
     "[`TEARDOWN.md`](../TEARDOWN.md) §4 said the only conclusion that sells is a *volume* problem, "
     "because volume is solved by a person. **\"You are spending $4,000/month on this through a "
     "vendor\" is the same argument in dollars instead of cuts** — and dollars port"),
    ("**Precedented**", "Somewhere's role→region tool and Athyna's LATAM salary tool are both this "
     "shape, across 60+ titles each — which is the portability proof")]:
    print(f"| {a} | {b} |")
print("\n| ❌ | |\n|---|---|")
for a, b in [
    ("**It is the salary-arbitrage frame, and that was rejected on purpose**",
     "[`MODEL-V2.md`](../MODEL-V2.md) §8 moved this business from price to quality, and "
     "[`REFERENCE.md`](../REFERENCE.md) §3 said explicitly *do not* build Somewhere's salary "
     "calculator. **This walks that back**"),
    ("**It is a head-on collision with the category leader's axis**",
     "*\"80% less\"* appears verbatim in **2 of 8** competitor headlines. Entering on their axis "
     "with no track record is the losing side of that fight"),
    ("**It proves nothing about us**", "Anyone can publish a cost comparison. It does not answer "
     "*can this person judge talent*"),
]:
    print(f"| {a} | {b} |")

print("\n### B. See the test\n")
print("| ✅ | |\n|---|---|")
for a, b in [
    ("**It is the only differentiated thing on the list**",
     "**Zero of ten competitors shows a test or a score.** They show photos, titles and prices. "
     "This is [`MODEL-V2.md`](../MODEL-V2.md) §8's `TRUECLAIM` position made concrete"),
    ("**Needs a rubric, not a bench**",
     "The graded-bench option ranked 5th and now ranks 25th partly because it needs two hired, "
     "tested people per role before launch. **A rubric is a document you write in an afternoon** — "
     "and you must write it anyway"),
    ("**It enforces the role filter automatically**",
     "A role you cannot write a credible rubric for is a role you cannot grade. "
     "[`LAUNCH.md`](../LAUNCH.md)'s `FOUNDERGRADE`, applied by construction rather than by "
     "discipline"),
    ("**It survives the bench paradox**",
     "A placed candidate leaves the bench; **the test does not go anywhere.** The proof is in the "
     "method, not in the person"),
    ("**Ports at 9**", "The rubric differs per role; the page structure, the scoring format and "
     "the persuasion mechanism are identical")]:
    print(f"| {a} | {b} |")
print("\n| ❌ | |\n|---|---|")
for a, b in [
    ("**Zero precedent, and that cuts both ways**",
     "Ten operating companies all found other ways to prove quality. Either they are missing "
     "something or it does not work — and I cannot tell you which from here"),
    ("**It is about us, not about them**",
     "A rubric interests someone already considering. It may not stop a scroller the way *\"you "
     "are spending $4,000/month on this\"* does"),
    ("**A rubric can be copied**",
     "It is the one asset a competitor can lift in an afternoon. The defence is that they cannot "
     "copy *doing the grading*, but the page itself is not defensible"),
]:
    print(f"| {a} | {b} |")

print("\n### C. Shortlist promise\n")
print("| ✅ | |\n|---|---|")
for a, b in [
    ("**Cheapest to build — 2.25 days**", "It is a sentence and a form"),
    ("**Ports at 10**", "Nothing in it is role-specific"),
    ("**Precedented**", "Genius leads with *\"See Pre-vetted Candidates\"* and it is their CTA")]:
    print(f"| {a} | {b} |")
print("\n| ❌ | |\n|---|---|")
for a, b in [
    ("**It is a promise, not a proof**",
     "From a named operator with a track record it is credible. **From an unknown, an unbacked "
     "promise is the weakest thing on this page**"),
    ("**It carries a delivery cost the model does not see**",
     "The page needs no human, so it scores `perlead = 0`. **But if sixty people request a "
     "shortlist you owe sixty shortlists.** The obligation is real and arrives later — which in "
     "practice forces it back to *\"book a call and then I'll shortlist\"*, which is what Genius "
     "does"),
    ("**7 days is a promise you have not tested**",
     "Somewhere quotes 3 days to candidates and 7–21 to filled. You have never run it once")]:
    print(f"| {a} | {b} |")

# ------------------------------------------------------------- 4. the answer
print("\n---\n\n## 4. The answer: A then B, on one page\n")
print("**A gives the reason to care. B gives the reason to trust.** They compose, they both port,")
print("and the composition fixes A's worst problem.\n")
print("```")
print("  1.  Which seat is open?                     [ 6 buttons ]")
print("")
print("  2.  What do you spend on it per month?      [ $4,000    ]")
print("      Includes agency, freelancer, subscription, or your own time")
print("           |")
print("           v")
print("      You spend            $48,000/yr")
print("      Full-time, all-in    $19,800/yr")
print("      Our fee, one-time     $5,940")
print("      ----------------------------------")
print("      Year one difference  $22,260")
print("")
print("  3.  \"But can you judge a good one?\"          <- THE OBJECTION")
print("")
print("      Here is the test every performance editor takes before you")
print("      meet them, and a real scored submission:")
print("        - recut one of the client's live ads, 48h")
print("        - scored on 3-sec retention, 15-sec retention, brief adherence")
print("        - sample: 41% -> 68% on 3-sec.  Score 8.1/10")
print("")
print("  4.  [ See available times ]                  <- self-serve calendar")
print("```")
print("\n### Why the order matters\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Cost first, then quality, never the reverse**",
     "The cost line is what stops the scroll — it is about them. The test is what closes the "
     "objection the cost line creates, which is *\"cheap offshore labour, and how would you know "
     "if they were any good?\"*"),
    ("**This is how the price frame gets neutralised**",
     "Stating a cost gap and then immediately proving the grading is **not** competing on price — "
     "it is using price to earn attention and quality to earn the call. "
     "[`MODEL-V2.md`](../MODEL-V2.md) §8's objection was to *leading and ending* on price. "
     "**Ending on the test is the whole difference**"),
    ("**Both blocks port**", "Six seats change six labels, one salary band and one rubric. "
     "**No block is rebuilt, ever** — which is the requirement"),
    ("**And it stays testable across, not down**",
     "One page serves every ICP × role. The ICP lives in the ad, the role lives in button 1, and "
     "the conversion event is identical in all of them — so the cells are comparable")]:
    print(f"| {a} | {b} |")

print("\n### What each cell costs to add\n")
print("| To add a role | Work |\n|---|---|")
for a, b in [
    ("One button", "Five minutes"),
    ("One salary band", "A lookup — Somewhere publishes bands for 60+ titles"),
    ("**One rubric**", "**An afternoon, and it is the only real cost.** A role you cannot write "
     "one for is a role you should not launch — which is the filter doing its job"),
    ("One scored sample", "One graded candidate for that role. **This is the gating item**, and it "
     "is one person, not the two-per-role a bench needs"),
]:
    print(f"| {a} | {b} |")
print("\n**One graded person per role instead of two, and a rubric instead of a bench.** That is")
print("roughly half the day-1 asset cost of the bench option, for most of the trust.\n")

print("---\n\n## 5. What I got wrong, in order\n")
print("| Pass | Claim | Why it was wrong |\n|---|---|---|")
for a, b, c in [
    ("1–3", "Ranked funnels on modelled CAC",
     "Ninety invented conversion parameters compounded into three-significant-figure answers"),
    ("4", f"Enumerated {len(A.ALL)} funnels with no portability dimension",
     "Optimised for build simplicity and discovery signal. **Never scored the requirement**"),
    ("5", "Recommended a volume calculator",
     "It asks for a per-unit vendor price that **no vendor in my own competitor file charges**"),
]:
    print(f"| {a} | {b} | {c} |")
print("\n**What survives all five passes:** the landing page over on-platform (~17% vs ~2% "
      "appointment")
print("rate), the self-serve calendar over any chase (32% vs 12% close, against a 10-hour gap), one")
print("page and one ad set, and *a role with no measurable delta is not a role to launch.* Those")
print("four have never moved, because each rests on a verified fact rather than on a model.\n")
