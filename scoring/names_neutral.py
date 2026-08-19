#!/usr/bin/env python3
"""
Every name ranked on merit alone — ownership deliberately excluded.

Operator direction: "forget whether we have it or not. lets rank neutral."

So the OWNED dimension that put allhandstalent.com and whichskill.com at the top
of NAMES-FINAL.md is gone. Nothing here gets credit for being paid for. What is
left is whether the name is any good.

Sweeps behind this file:
  2,622  [quality]+[people] compounds, the SkillForce shape          .com
  1,071  arbitrary word x 9 people-nouns                             .com + .co
    242  [word]talent, drawn from ten meaning registers              .com + .co
     33  strong names already dead on .com, recovered                .co
  ~4,400 earlier, in domains.py / arbitrary.py / plain_sweep.py / idioms.py

.com via Verisign RDAP (404 = free). .co via the DoH NXDOMAIN proxy that
dns_probe.py calibrated at 82/82 with zero false-frees — good, but NOT
registrar-authoritative. Verify before buying.

Run:  python3 scoring/names_neutral.py > scoring/NAMES-NEUTRAL.md
"""

from dataclasses import dataclass

DIM = [("CLEAN",    24, "No operating company or trademark in the hiring trade class. "
                        "**The test that killed most of the good ones**"),
       ("MEANING",  20, "Does the word mean something apt — or is it just a pleasant noise?"),
       ("REGISTER", 18, "Evocative like Somewhere/Oceans/Genius, not commodity like Skillforce"),
       ("SAY",      16, "Spell it on a call, hear it in an ad, no accidental word inside it"),
       ("NEUTRAL",  12, "Survives the positioning changing — it has changed eight times"),
       ("TLD",      10, "Both `.com` and `.co` free = 10 · `.co` only = 8 · `.team` = 5")]


@dataclass
class N:
    domain: str
    tlds: str
    clean: int
    meaning: int
    register: int
    say: int
    neutral: int
    tld: int
    note: str


NAMES = [
    # ---------------------------------------------- the testing/proof register
    N("crucibletalent", "`.co` **+ `.com`**", 9, 10, 9, 8, 9, 10,
      "**A crucible is where metal is tested and refined under heat** — and in plain English a "
      "crucible *is* a severe test. Exactly the positioning, arrived at metaphorically rather "
      "than by describing the method. No staffing collision: Atlassian's Crucible is a code-review "
      "tool and Sony's is a game, both far outside the trade class. Eight letters, spells clean, "
      "hears clean"),

    N("assaytalent", "`.co` **+ `.com`**", 9, 10, 8, 4, 8, 10,
      "**An assay is a test of purity** — the single most precise word for what this business "
      "does, and no collision found. **Wrecked on `SAY`:** spoken aloud it is heard as *essay*, "
      "and essay mills are a known scam category. A name you have to spell every time you say it"),

    N("signettalent", "`.co` **+ `.com`**", 9, 9, 8, 6, 9, 10,
      "A signet is a **seal of authenticity**. Clean, on-thesis, evocative. Docked because it is "
      "heard as *cygnet* — a baby swan"),

    N("touchstonetalent", "`.co`", 0, 10, 9, 8, 9, 8,
      "❌ **The perfect word, and it is taken.** A touchstone is the stone used to test the purity "
      "of gold. But **Touchstone Talent Group is a live company**, alongside Touchstone Recruitment "
      "(mining and energy, 20+ years) and TouchStone Personnel. Three collisions in our trade class"),

    # ---------------------------------------------- steadfast / merit
    N("ballasttalent", "`.co` **+ `.com`**", 8, 8, 8, 7, 10, 10,
      "Ballast is what keeps a ship steady in weather — a good, quiet metaphor for a hire, and "
      "entirely method-neutral"),

    N("keystonetalent", "`.co`", 5, 8, 7, 9, 9, 8,
      "The stone that holds the arch up. Says the right thing, but **Keystone is one of the most "
      "used brand words in North America** — insurance, energy, logistics, staffing"),

    N("laureltalent", "`.co` **+ `.com`**", 8, 8, 7, 8, 9, 10,
      "Laurels are the award for excellence. Undercut by *resting on one's laurels*, and Laurel is "
      "a common first name"),

    N("merittalent", "`.co`", 6, 8, 5, 9, 8, 8,
      "Says exactly the right thing and sounds like every third staffing firm. *Merit* is heavily "
      "used in the category"),

    # ---------------------------------------------- arbitrary / register-only
    N("almanactalent", "`.co` **+ `.com`**", 9, 7, 8, 7, 10, 10,
      "A book of tables and records — quietly apt without claiming a method. **No collision found "
      "anywhere**, and it surfaced independently in the earlier `names.py` sweep"),

    N("tuesdaytalent", "`.co` **+ `.com`**", 6, 3, 8, 9, 10, 10,
      "The shape asked for, and the right day — Monday dreads, Friday clocks off. But it **means "
      "nothing**, and *Talent Tuesday* is a common hiring-event name (Mercy, State of Indiana, "
      "Job Service ND) with a small *Tuesday Talent* creative community already using it"),

    N("kindredtalent", "`.co`", 0, 8, 8, 9, 9, 8,
      "❌ **KindredTalent already places creative, marketing and digital talent** — 25 years, and "
      "our exact ICP. The most direct collision found in this sweep"),

    N("forgetalent", "`.co`", 7, 8, 8, 2, 9, 8,
      "❌ **Contains the word *forget*.** Exactly what `arbitrary.py`'s ARTIFACT gate exists to "
      "catch — an accidental word straddling the join, and this one is the opposite of what a "
      "talent firm wants read"),

    N("vanguardtalent", "`.co`", 2, 9, 8, 9, 9, 8,
      "❌ Vanguard is a $9-trillion asset manager. Nothing survives that"),

    N("polestartalent", "`.co`", 3, 9, 8, 8, 9, 8,
      "❌ Polestar is Volvo's electric-car brand, heavily advertised to the same feeds we would buy"),

    # ---------------------------------------------- non-talent shapes, for comparison
    N("allhandstalent", "`.com`", 8, 7, 6, 7, 10, 10,
      "Ranked here **with no credit for being owned.** Idiom-led, method-neutral, expands "
      "everywhere. *Talent* is generic and *all hands* collides with the meeting"),

    N("topdrawer", "`.co`", 7, 9, 9, 9, 10, 8,
      "*Top drawer* means first-class. **The strongest register score of anything available**, and "
      "it needs no second word at all"),

    N("surehands", "`.co`", 6, 9, 9, 9, 10, 8,
      "*Safe hands* is the feeling being sold. SureHands is a patient-lift manufacturer — wrong "
      "trade class, but it holds the `.com`"),

    N("handiwork", "`.co`", 7, 9, 9, 8, 9, 8,
      "Work done by hand, with skill. `.com` occupant is a Cloudflare-protected page per "
      "[`CO.md`](CO.md)"),

    N("handpicked", "`.team`", 6, 10, 9, 9, 7, 5,
      "The most on-the-nose word in the study and it needs no head noun. Only `.team` is free, and "
      "*handpicked* is a widely used brand adjective"),

    N("whichskill", "`.com`", 9, 6, 7, 9, 8, 10,
      "**Supply-side vocabulary.** Workers have skills; employers have seats. A strong name for "
      "the India candidate funnel and the wrong one for the buyer page"),
]

for n in NAMES:
    n.total = sum(getattr(n, k.lower()) * w for k, w, _ in DIM) / 10.0
NAMES.sort(key=lambda n: -n.total)

print("# Every Name, Ranked on Merit Alone\n")
print("> **Ownership deliberately excluded.** Nothing here gets credit for being paid for —")
print("> `allhandstalent` and `whichskill` are scored as if we were buying them today.\n")
print("Behind this: **8,335 domain checks** — 2,622 SkillForce-shape compounds, 1,071 "
      "arbitrary-word")
print("names on both TLDs, 242 `[word]talent` drawn from ten meaning registers, 33 `.co` "
      "recoveries,")
print("and ~4,400 earlier in [`domains.py`](domains.py), [`arbitrary.py`](arbitrary.py), "
      "[`plain_sweep.py`](plain_sweep.py)")
print("and [`idioms.py`](idioms.py).\n")

live = [n for n in NAMES if n.clean >= 5]
dead = [n for n in NAMES if n.clean < 5]

print("---\n\n## The ranking\n")
print("| # | Name | Free on | " + " | ".join(f"`{k}`" for k, _, _ in DIM) + " | **Score** |")
print("|---|---|---|" + "---|" * (len(DIM) + 1))
r = 0
for n in NAMES:
    d = n.clean < 5
    if not d:
        r += 1
    num = "❌" if d else str(r)
    mark = " 🥇" if r == 1 and not d else ""
    print(f"| {num} | **{n.domain}**{mark} | {n.tlds} | "
          + " | ".join(str(getattr(n, k.lower())) for k, _, _ in DIM)
          + f" | **{n.total:.0f}** |")
print("\n❌ = killed on collision. Left in the table so they stay dead.\n")

print("| Dimension | Weight | |\n|---|---|---|")
for k, w, d in DIM:
    print(f"| `{k}` | {w} | {d} |")

print("\n---\n\n## The top of the list, in full\n")
for i, n in enumerate([x for x in live][:6], 1):
    print(f"### {i}. `{n.domain}.co`" + ("  ·  `.com` also free" if "com" in n.tlds else "")
          + f"  —  {n.total:.0f}\n")
    print(f"{n.note}\n")

print("---\n\n## What the sweep actually showed\n")
print("| | |\n|---|---|")
for a, b in [
    ("**The `[word]talent` shape is the best-yielding one tried**",
     f"**214 of 242 free on `.co`**, and 104 of those also free on `.com`. Against the "
     f"SkillForce shape, where 72% were gone and *zero* free ones were real English"),
    ("**Grouping by meaning is what surfaced the winner**",
     "Ten registers — testing, merit, guidance, steadfast, trust-roles, craft, nature, mineral, "
     "bird, time. **The testing register is the one that matters**, because it is the only one "
     "that says what the business does"),
    ("**And that register is nearly picked clean**",
     "*Touchstone* — the perfect word, the stone used to test gold — is taken three times over in "
     "our trade class. *Assay* survives and is unsayable. **Crucible is what is left**"),
    ("**Collision killed five of twenty**",
     "Touchstone, Kindred, Vanguard, Polestar, and Forge on an artifact. Availability was never "
     "the constraint"),
]:
    print(f"| {a} | {b} |")

top = live[0]
own = next(n for n in NAMES if n.domain == "allhandstalent")
print(f"\n---\n\n## The honest comparison\n")
print(f"On merit alone, **`{top.domain}`** scores **{top.total:.0f}** against "
      f"**{own.total:.0f}** for `allhandstalent`.\n")
print("| | `crucibletalent` | `allhandstalent` |\n|---|---|---|")
for k, _, _ in DIM:
    print(f"| `{k}` | {getattr(top, k.lower())} | {getattr(own, k.lower())} |")
print(f"\nThe gap is **{top.total - own.total:.0f} points**, and it is almost all `MEANING` and "
      f"`REGISTER` — *crucible*")
print("says something true about the business, *all hands* says something generic about "
      "teamwork.\n")
print("> **That is a real difference, not a rounding error.** Whether it is worth a rebrand is a")
print("> question about switching cost, which this ranking deliberately does not price.\n")
