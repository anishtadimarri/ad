#!/usr/bin/env python3
"""
Names ranked on criteria derived from what the name actually has to survive.

Operator direction: rank neutral (ownership excluded), rebuild the criteria from
first principles, and add "sounds like a legit business".

THE DERIVATION. Not a list of nice properties — a list of the specific moments
this name has to survive, given this operator's actual position: unknown,
India-based, solo, no track record, selling a $6,000 one-time fee to US and UK
buyers off cold Meta ads.

  1. It appears in a Meta feed for about a second and a half.
  2. A stranger has to be comfortable wiring $6,000 to an Indian company they
     had never heard of that morning.                      <- the binding one
  3. They google it before paying.
  4. It gets said on a call and spelled into a voicemail.
  5. It must not force a rebrand at month 18.
  6. The business will change. The positioning has already changed eight times.
  7. It has to be buyable today.

Six criteria fall out of those seven moments, and nothing else does. Note what
did NOT survive the derivation: "register" — whether a name sounds evocative
like Somewhere or commodity like Skillforce — was my aesthetic preference, not
a job the name has to do. Where it matters, it matters through LEGIT.

TLD evidence [V]: .com is typed ~6x more than .co when people guess, and scores
44% memorability against .co's 33%. But no published study isolates the
extension as a conversion cause, so it is folded into LEGIT as a modest signal
rather than given its own weight.

Run:  python3 scoring/names_neutral.py > scoring/NAMES-NEUTRAL.md
"""

from dataclasses import dataclass

DIM = [
    ("LEGIT",    26, "Moment 2. **Does it sound like an incorporated business a finance person "
                     "would wire $6,000 to** — or like a side project? Absorbs the TLD signal"),
    ("CLEAR",    24, "Moments 3 and 5. No operating company or trademark in the hiring trade "
                     "class, and a search finds *us*"),
    ("SURVIVES", 18, "Moment 6. Method-neutral and role-neutral — the business will move"),
    ("SPOKEN",   16, "Moments 1 and 4. Say it, spell it, hear it. No accidental word inside it"),
    ("APT",      10, "Does it say something true about the business? Useful, not load-bearing"),
    ("BUYABLE",   6, "Moment 7. Can it be registered today"),
]


@dataclass
class N:
    name: str
    tlds: str
    legit: int
    clear: int
    survives: int
    spoken: int
    apt: int
    buyable: int
    note: str


NAMES = [
    N("Crucible Talent", "`.com` + `.co`", 8, 9, 9, 8, 10, 10,
      "A crucible tests and refines under heat, and in plain English **is** a severe test. "
      "Latinate weight, so it reads incorporated rather than clever. Atlassian's Crucible is a "
      "code-review tool and Sony's is a game — neither in the trade class"),

    N("Signet Talent", "`.com` + `.co`", 8, 9, 9, 6, 9, 10,
      "A signet is a seal of authenticity. **Signet Jewelers is NYSE-listed**, which is why the "
      "word carries corporate weight rather than boutique. Loses on `SPOKEN` — heard as *cygnet*"),

    N("Ballast Talent", "`.com` + `.co`", 8, 8, 10, 7, 8, 10,
      "Ballast keeps a ship steady in weather. The word already lives in the finance register — "
      "Ballast Point, Ballast Rock Capital — so it reads like a firm"),

    N("Almanac Talent", "`.com` + `.co`", 7, 9, 10, 7, 7, 10,
      "A book of tables and records. **No collision found anywhere.** Slightly boutique, and "
      "people hesitate spelling it"),

    N("Assay Talent", "`.com` + `.co`", 7, 9, 8, 4, 10, 10,
      "An assay is a test of purity — the most precise word in the study for what this does. "
      "**Wrecked on `SPOKEN`:** heard as *essay*, and essay mills are a known scam category. "
      "You would spell it every time you said it"),

    N("Laurel Talent", "`.com` + `.co`", 6, 8, 9, 8, 8, 10,
      "Laurels are the award for excellence. Reads like a boutique showbiz talent agency, and "
      "*resting on one's laurels* is the wrong association"),

    N("All Hands Talent", "`.com`", 6, 8, 10, 7, 7, 10,
      "**Scored with no credit for being owned.** Method-neutral and expands everywhere, but "
      "*all hands* is a casual idiom — it reads friendly-agency rather than incorporated, which "
      "is the wrong direction for moment 2"),

    N("Merit Roster", "`.com`", 5, 6, 8, 9, 8, 10,
      "Says the right thing. *Roster* reads sporting and casual, and *merit* is used by half the "
      "category"),

    N("Keystone Talent", "`.co`", 6, 5, 9, 9, 8, 8,
      "The stone that holds the arch. Real corporate weight — and **Keystone is one of the most "
      "used brand words in North America**, so the search result is not ours"),

    N("Tuesday Talent", "`.com` + `.co`", 4, 6, 10, 9, 3, 10,
      "The shape asked for. But it **means nothing**, it reads as a creative collective or a "
      "hiring event, and *Talent Tuesday* is exactly that — Mercy, State of Indiana, Job Service "
      "North Dakota all run one"),

    N("Top Drawer", "`.co`", 4, 7, 10, 9, 9, 8,
      "*Top drawer* means first-class and needs no second word. But it reads **consumer boutique**, "
      "and on `.co` it reads side project. Great name for the wrong kind of company"),

    N("Sure Hands", "`.co`", 3, 6, 10, 9, 9, 8,
      "*Safe hands* is the feeling being sold. Unfortunately it reads like a home-care or "
      "handyman service, and SureHands is a patient-lift manufacturer"),

    N("Handiwork", "`.co`", 3, 7, 9, 8, 9, 8,
      "Work done by hand, with skill. Reads like an artisan marketplace"),

    N("Handpicked", "`.team`", 3, 6, 7, 9, 10, 5,
      "The most on-the-nose word found, and it needs no head noun. **`.team` reads as a side "
      "project** to exactly the buyer we need to reassure"),

    N("Which Skill", "`.com`", 4, 9, 8, 9, 6, 10,
      "Supply-side vocabulary — workers have skills, employers have seats. Also reads like a "
      "comparison site or a quiz. Right name for the India candidate funnel, wrong for the buyer"),

    # ---- dead on collision. Left visible so they stay dead.
    N("Touchstone Talent", "`.co`", 8, 0, 9, 8, 10, 8,
      "❌ **The perfect word — the stone used to test the purity of gold — and it is taken three "
      "times over in our own trade class.** Touchstone Talent Group, Touchstone Recruitment, "
      "TouchStone Personnel"),

    N("Kindred Talent", "`.co`", 7, 0, 9, 9, 8, 8,
      "❌ **KindredTalent already places creative, marketing and digital talent** — 25 years, our "
      "exact ICP"),

    N("Vanguard Talent", "`.co`", 9, 2, 9, 9, 9, 8,
      "❌ Would have scored highest of all on `LEGIT`. Vanguard manages roughly $9 trillion"),

    N("Polestar Talent", "`.co`", 8, 3, 9, 8, 9, 8,
      "❌ Volvo's electric brand, advertised into the same feeds we would be buying"),

    N("Forge Talent", "`.co`", 6, 7, 9, 2, 8, 8,
      "❌ **Contains the word *forget*.** Precisely what `arbitrary.py`'s ARTIFACT gate exists to "
      "catch, and the worst possible accidental word for a talent firm"),

    N("Skill Force", "taken", 5, 0, 6, 9, 7, 0,
      "❌ Three operating recruitment firms — US construction staffing since 2003, Australia, "
      "Sweden"),
]

for n in NAMES:
    n.total = sum(getattr(n, k.lower()) * w for k, w, _ in DIM) / 10.0
NAMES.sort(key=lambda n: -n.total)

print("# Names, Ranked on What the Name Has to Survive\n")
print("> Criteria rebuilt from first principles, ownership excluded, and **\"sounds like a legit")
print("> business\" added — which turns out to be the heaviest weight, because it is the operator's")
print("> actual binding constraint.**\n")

print("---\n\n## 1. Where the criteria come from\n")
print("Not a list of nice properties. A list of the moments this name has to survive, given the")
print("real position: **unknown, India-based, solo, no track record, selling a $6,000 one-time fee")
print("to US and UK buyers off cold Meta ads.**\n")
print("| | The moment | The criterion it forces |\n|---|---|---|")
for a, b, c in [
    ("1", "It appears in a Meta feed for about a second and a half", "`SPOKEN`"),
    ("2", "**A stranger wires $6,000 to an Indian company they had not heard of that morning**",
     "**`LEGIT`**"),
    ("3", "They google it before paying", "`CLEAR`"),
    ("4", "It gets said on a call and spelled into a voicemail", "`SPOKEN`"),
    ("5", "It must not force a rebrand at month 18", "`CLEAR`"),
    ("6", "The business changes — the positioning has already changed **eight times**", "`SURVIVES`"),
    ("7", "It has to be buyable today", "`BUYABLE`"),
]:
    print(f"| {a} | {b} | {c} |")
print("\n**What did not survive the derivation:** *register* — whether a name sounds evocative like")
print("Somewhere or commodity like Skillforce. That was my aesthetic preference, not a job the name")
print("has to do. Where it genuinely matters, it matters **through** `LEGIT`.\n")
print("| Criterion | Weight | |\n|---|---|---|")
for k, w, d in DIM:
    print(f"| `{k}` | {w} | {d} |")
print("\n**The TLD is folded into `LEGIT` rather than scored separately.** Evidence: `.com` is typed")
print("**~6x more** than `.co` when people guess, and scores **44% memorability against 33%** [V] —")
print("but **no published study isolates the extension as a conversion cause**, so it is a modest")
print("signal inside legitimacy, not a line of its own.\n")

live = [n for n in NAMES if n.clear >= 5]
dead = [n for n in NAMES if n.clear < 5]

print("---\n\n## 2. The ranking\n")
print("| # | Name | Free on | " + " | ".join(f"`{k}`" for k, _, _ in DIM) + " | **Score** |")
print("|---|---|---|" + "---|" * (len(DIM) + 1))
r = 0
for n in NAMES:
    d = n.clear < 5
    if not d:
        r += 1
    num = "❌" if d else str(r)
    mark = " 🥇" if r == 1 and not d else ""
    print(f"| {num} | **{n.name}**{mark} | {n.tlds} | "
          + " | ".join(str(getattr(n, k.lower())) for k, _, _ in DIM)
          + f" | **{n.total:.0f}** |")
print("\n❌ = dead on collision, kept visible so they stay dead.\n")

print("---\n\n## 3. The top five, in full\n")
for i, n in enumerate(live[:5], 1):
    print(f"### {i}. **{n.name}** — {n.total:.0f}  ·  {n.tlds}\n")
    print(f"{n.note}\n")

print("---\n\n## 4. What adding `LEGIT` did\n")
print("It reordered the middle of the table, and the reason is worth stating.\n")
print("| Name | Before | Now | Why |\n|---|---|---|---|")
for a, b, c, dd in [
    ("**Top Drawer**", "2nd", f"{[n.name for n in live].index('Top Drawer')+1}th",
     "A lovely idiom that reads **consumer boutique**, on a `.co`. Wrong signal for someone about "
     "to send money abroad"),
    ("**Sure Hands** · **Handiwork**", "5th · 7th",
     f"{[n.name for n in live].index('Sure Hands')+1}th · "
     f"{[n.name for n in live].index('Handiwork')+1}th",
     "Both read as artisan or home-service brands. Charming, and not what a CFO wires to"),
    ("**Handpicked**", "11th", f"{[n.name for n in live].index('Handpicked')+1}th",
     "The most apt single word found, on the TLD that most says *side project*"),
    ("**Crucible Talent**", "1st", "**1st**",
     "Unchanged. It was already the only name scoring well on both meaning and weight"),
]:
    print(f"| {a} | {b} | {c} | {dd} |")

top, own = live[0], next(n for n in NAMES if n.name == "All Hands Talent")
print(f"\n---\n\n## 5. Against what is already owned\n")
print(f"| | **{top.name}** | {own.name} |\n|---|---|---|")
for k, _, _ in DIM:
    print(f"| `{k}` | {getattr(top, k.lower())} | {getattr(own, k.lower())} |")
print(f"| | **{top.total:.0f}** | **{own.total:.0f}** |")
print(f"\nThe gap is **{top.total - own.total:.0f} points**, and it is concentrated in `APT` and "
      f"`LEGIT`. *All Hands*")
print("is a casual idiom that reads friendly-agency; *Crucible* has Latinate weight and says "
      "something")
print("true. On the criterion that matters most for a stranger sending money abroad, it is a "
      "**two-point**")
print("**difference on a 26-weight dimension** — the largest single swing in the table.\n")
print("> **This ranking still does not price switching cost.** That was excluded on instruction,")
print("> and it is the one number that decides whether a 15-point gap is worth acting on.\n")
