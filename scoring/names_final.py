#!/usr/bin/env python3
"""
Every name option considered, ranked once — so it stops being re-litigated.

The naming question has now been asked five times across this engagement. The
repo has run ~4,400 RDAP checks (domains.py, arbitrary.py, plain_sweep.py,
idioms.py, co_names.py) plus 2,662 more in the SkillForce sweep. This file
consolidates every survivor into one ranking and records WHY each one placed,
including the ones killed by company collision rather than by availability.

The collision test is the one that matters and it is applied consistently. It
killed SkillForce (three operating recruitment firms), Sterling (Sterling Talent
Solutions — 50,000 clients in background screening, the exact axis we claim) and
Caliber (four staffing firms). Availability is necessary and nowhere near
sufficient.

Availability verified August 2026: .com via Verisign RDAP (404 = free),
.co via the DoH proxy dns_probe.py calibrated at 82/82 with 0 false-frees,
.team via Identity Digital RDAP.

Run:  python3 scoring/names_final.py > scoring/NAMES-FINAL.md
"""

from dataclasses import dataclass

DIM = [("OWNED",    20, "Do we already own it? Switching costs real weeks, not dollars"),
       ("CLEAN",    20, "Trademark and operating-company collision in the hiring trade class"),
       ("REGISTER", 16, "Evocative like Somewhere/Oceans/Genius, or commodity like Skillforce"),
       ("NEUTRAL",  14, "Survives the positioning changing — it has changed eight times"),
       ("EXPAND",   12, "Works across every ICP x role, and for supply as well as demand"),
       ("SAY",      10, "Spell it on a call, hear it in an ad, type it without a hyphen"),
       ("TLD",       8, ".com > .co > .team")]


@dataclass
class N:
    domain: str
    status: str
    owned: int
    clean: int
    register: int
    neutral: int
    expand: int
    say: int
    tld: int
    note: str


NAMES = [
    N("allhandstalent.com", "**owned**", 10, 8, 6, 10, 10, 7, 10,
      "Idiom-led, which puts it nearer the Somewhere/Oceans register than the staffing "
      "compounds. *Talent* is the category's most generic noun and *all hands* collides with "
      "the meeting — but no company owns it, and it is method-neutral"),

    N("whichskill.com", "**owned**", 10, 9, 7, 8, 4, 9, 10,
      "**A different job.** *Skill* as a standalone noun is supply-side vocabulary — workers "
      "have skills, employers have seats. Excellent for the India candidate funnel, wrong for "
      "the buyer page. Keeping supply on a separate domain also removes the Employment "
      "Special Ad Category exposure, priced at 10–29% of CAC"),

    N("handpicked.team", "free", 0, 6, 9, 7, 9, 9, 5,
      "**The best name nobody owns.** A real English word that means exactly the positioning, "
      "and it was on the operator's own early shortlist. Held back by `.team` and by "
      "*handpicked* being widely used as a brand adjective elsewhere"),

    N("anchorroster.com", "free", 0, 8, 7, 9, 9, 8, 10,
      "*Anchor* is evocative rather than descriptive, which is the register that travels. "
      "Method-neutral. The strongest of the free `.com` options"),

    N("selectroster.com", "free", 0, 8, 5, 7, 9, 8, 10,
      "Clean, employer-facing, and completely forgettable"),

    N("meritroster.com", "free", 0, 9, 5, 6, 9, 8, 10,
      "*Merit* is genuinely on-thesis — we rank by merit and keep a roster. Reads slightly "
      "bureaucratic"),

    N("gradedbench.com", "free", 0, 9, 5, 4, 8, 8, 10,
      "**The most on-thesis name in the study** — the graded bench is literally the product. "
      "Also the most method-locked, and *graded* is school vocabulary"),

    N("gradedwork.com", "free", 0, 9, 6, 4, 7, 9, 10,
      "Real English phrase, exactly the mechanic, short. Same school-register problem, and "
      "it names the company after a method that has been revised repeatedly"),

    N("provenroster.com", "free", 0, 8, 5, 5, 9, 8, 10,
      "Fine. Nothing wrong with it and nothing to it"),

    N("gradedroster.com", "free", 0, 9, 4, 4, 9, 7, 10,
      "From the earlier `domains.py` sweep. Doubles down on both weaknesses"),

    # ---- killed by collision, not by availability. Recorded so they stay dead.
    N("skillforce.com", "**taken**", 0, 0, 5, 6, 9, 9, 10,
      "❌ **Three operating recruitment firms** — Skillforce Inc. (US construction staffing, "
      "since 2003), Skillforce Recruitment (Australia), SkillForce (Sweden). Suffix-padding it "
      "would be a knockoff of an incumbent in our own trade class"),

    N("sterlingguild.com", "free", 0, 2, 8, 8, 9, 7, 10,
      "❌ **Sterling Talent Solutions** — 50,000 clients, background screening, now First "
      "Advantage. Collides on the *vetting* axis, which is our entire claim. Would have ranked "
      "top three on every other dimension"),

    N("caliberroster.com", "free", 0, 3, 6, 8, 9, 6, 10,
      "❌ At least four staffing firms use *Caliber*. Also splits on British spelling"),

    N("hallmarktalent.com", "free", 0, 1, 7, 8, 9, 8, 10,
      "❌ *Hallmark* is literally a mark of quality and would be perfect — and it is one of the "
      "most defended trademarks in the US"),
]

for n in NAMES:
    n.total = sum(getattr(n, k.lower()) * w for k, w, _ in DIM) / 10.0
NAMES.sort(key=lambda n: -n.total)

print("# Every Name Considered, Ranked Once\n")
print("> The naming question has been asked five times. This is the consolidated answer, so it")
print("> does not need asking again. **Availability was never the binding constraint — collision")
print("> was.**\n")
print(f"Checked across the whole engagement: **~4,400 RDAP checks** in "
      f"[`domains.py`](domains.py), [`arbitrary.py`](arbitrary.py),")
print("[`plain_sweep.py`](plain_sweep.py), [`idioms.py`](idioms.py) and "
      "[`co_names.py`](co_names.py), plus **2,662 more**")
print("in the SkillForce-shape sweep. Verified August 2026.\n")

print("---\n\n## The ranking\n")
print("| # | Domain | Status | " + " | ".join(f"`{k}`" for k, _, _ in DIM) + " | **Score** |")
print("|---|---|---|" + "---|" * (len(DIM) + 1))
for i, n in enumerate(NAMES, 1):
    dead = n.clean <= 3
    mark = " 🥇" if i == 1 else (" ❌" if dead else "")
    print(f"| {i} | `{n.domain}`{mark} | {n.status} | "
          + " | ".join(str(getattr(n, k.lower())) for k, _, _ in DIM)
          + f" | **{n.total:.0f}** |")

print("\n| Dimension | Weight | |\n|---|---|---|")
for k, w, d in DIM:
    print(f"| `{k}` | {w} | {d} |")

print("\n---\n\n## Why each one placed\n")
for i, n in enumerate(NAMES, 1):
    print(f"**{i}. `{n.domain}`** — {n.total:.0f}\n")
    print(f"{n.note}\n")

live = [n for n in NAMES if n.clean > 3]
dead = [n for n in NAMES if n.clean <= 3]
best_free = next(n for n in live if n.owned == 0)
print("---\n\n## What this settles\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Keep `allhandstalent.com`**",
     f"It wins on {DIM[0][0]} and {DIM[3][0]} — owned, and method-neutral. It is a B+ name, and "
     f"no A name is available that is also clean"),
    ("**Keep `whichskill.com` for supply**",
     "Not a demotion. It is the India candidate funnel, and separating the two domains removes "
     "an Employment-classification exposure worth 10–29% of CAC"),
    (f"**The best free option is `{best_free.domain}`**",
     f"at {best_free.total:.0f} against "
     f"{NAMES[0].total:.0f}. **Not enough to justify a rebrand**, and that gap is entirely the "
     f"cost of switching rather than any quality of the name"),
    ("**Three good names are dead on collision**",
     "Sterling, Caliber and Hallmark would all have ranked highly. Each is occupied by an "
     "operating firm in the hiring trade class. **This is the test that matters, and it is not "
     "the same as checking availability**"),
]:
    print(f"| {a} | {b} |")
print(f"\n**{len(dead)} of {len(NAMES)} candidates here are available and unusable.** That ratio is "
      f"the whole lesson of the")
print("naming work: a free domain in a crowded trade class tells you almost nothing until you have "
      "looked for the incumbent.\n")
print("> **The blocker is not the name. It is four graded people** — two roles, two each, roughly")
print("> two weeks of sourcing. Every claim on the landing page depends on those existing, and")
print("> none of it can be tested until they do.\n")
