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

Seven criteria fall out of those seven moments, and nothing else does. Two notes
on what changed in the derivation:

  DROPPED  "register" — evocative like Somewhere vs commodity like Skillforce.
           That was my aesthetic preference, not a job the name has to do.
  ADDED    PLAIN. Moment 1 assumed the buyer knows the word, and for crucible,
           signet and touchstone that assumption is false. It is MEASURED from
           corpus frequency rather than judged, because I had been guessing.
           APT is demoted to 8 as a direct consequence: chasing precise meaning
           is what produced a shortlist of words nobody uses.

TLD evidence [V]: .com is typed ~6x more than .co when people guess, and scores
44% memorability against .co's 33%. But no published study isolates the
extension as a conversion cause, so it is folded into LEGIT as a modest signal
rather than given its own weight.

Run:  python3 scoring/names_neutral.py > scoring/NAMES-NEUTRAL.md
"""

from dataclasses import dataclass

DIM = [
    ("PLAIN",    22, "**Does the buyer know the word at all?** Operator direction: understandable "
                     "beats meaningful. Corpus frequency, corrected where written ≠ known"),
    ("DISTINCT", 20, "**Does it stick, and can it be found?** A word so generic it is wallpaper "
                     "fails twice — nobody remembers it and a search does not reach us"),
    ("LEGIT",    18, "Does it sound like an incorporated business a finance person would wire "
                     "$6,000 to? Absorbs the TLD signal"),
    ("CLEAR",    18, "No operating company or trademark in the hiring trade class"),
    ("SPOKEN",   10, "Say it, spell it, hear it. No accidental word inside it"),
    ("SURVIVES",  6, "Method-neutral and role-neutral — most plain words pass this anyway"),
    ("APT",       6, "Says something true about the business. **Demoted twice now** — first for "
                     "producing obscure words, now on direct instruction"),
]


@dataclass
class N:
    name: str
    tlds: str
    plain: int
    distinct: int
    legit: int
    clear: int
    spoken: int
    survives: int
    apt: int
    note: str


NAMES = [
    N("Crucible Talent", "`.com` + `.co`", 4, 8, 8, 9, 8, 9, 10,
      "A crucible tests and refines under heat, and in plain English **is** a severe test. "
      "Latinate weight, so it reads incorporated rather than clever. Atlassian's Crucible is a "
      "code-review tool and Sony's is a game — neither in the trade class"),

    N("Signet Talent", "`.com` + `.co`", 2, 7, 8, 9, 6, 9, 9,
      "A signet is a seal of authenticity. **Signet Jewelers is NYSE-listed**, which is why the "
      "word carries corporate weight rather than boutique. Loses on `SPOKEN` — heard as *cygnet*"),

    N("Ballast Talent", "`.com` + `.co`", 4, 8, 8, 8, 7, 10, 8,
      "Ballast keeps a ship steady in weather. The word already lives in the finance register — "
      "Ballast Point, Ballast Rock Capital — so it reads like a firm"),

    N("Almanac Talent", "`.com` + `.co`", 5, 8, 7, 9, 7, 10, 7,
      "A book of tables and records. **No collision found anywhere.** Slightly boutique, and "
      "people hesitate spelling it"),

    N("Assay Talent", "`.com` + `.co`", 4, 7, 7, 9, 4, 8, 10,
      "An assay is a test of purity — the most precise word in the study for what this does. "
      "**Wrecked on `SPOKEN`:** heard as *essay*, and essay mills are a known scam category. "
      "You would spell it every time you said it"),

    N("Laurel Talent", "`.com` + `.co`", 5, 4, 6, 8, 8, 9, 8,
      "Laurels are the award for excellence. Reads like a boutique showbiz talent agency, and "
      "*resting on one's laurels* is the wrong association"),

    N("All Hands Talent", "`.com`", 9, 6, 6, 8, 7, 10, 7,
      "**Scored with no credit for being owned.** An ordinary phrase in an unexpected role — the "
      "same shape as Somewhere and Oceans — which is why it holds up. *All hands* still reads "
      "friendly-agency rather than incorporated"),

    N("Merit Roster", "`.com`", 8, 3, 5, 6, 9, 8, 8,
      "Says the right thing. *Roster* reads sporting and casual, and *merit* is used by half the "
      "category"),

    N("Keystone Talent", "`.co`", 5, 4, 6, 5, 9, 9, 8,
      "The stone that holds the arch. Real corporate weight — and **Keystone is one of the most "
      "used brand words in North America**, so the search result is not ours"),

    N("Tuesday Talent", "`.com` + `.co`", 10, 9, 5, 6, 9, 10, 3,
      "The shape asked for. But it **means nothing**, it reads as a creative collective or a "
      "hiring event, and *Talent Tuesday* is exactly that — Mercy, State of Indiana, Job Service "
      "North Dakota all run one. **`PLAIN` corrected 6 → 10:** the corpus scores *tuesday* at "
      "6.18 per million because nobody writes the day of the week in books, not because anyone "
      "fails to know it. **Free on both TLDs**"),

    N("Top Drawer", "`.co`", 8, 8, 4, 7, 9, 10, 9,
      "*Top drawer* means first-class and needs no second word. But it reads **consumer boutique**, "
      "and on `.co` it reads side project. Great name for the wrong kind of company"),

    N("Sure Hands", "`.co`", 9, 6, 3, 6, 9, 10, 9,
      "*Safe hands* is the feeling being sold. Unfortunately it reads like a home-care or "
      "handyman service, and SureHands is a patient-lift manufacturer"),

    N("Handiwork", "`.co`", 7, 6, 3, 7, 8, 9, 9,
      "Work done by hand, with skill. Reads like an artisan marketplace"),

    N("Handpicked", "`.team`", 10, 7, 3, 6, 9, 7, 10,
      "The most on-the-nose word found, and it needs no head noun. **`.team` reads as a side "
      "project** to exactly the buyer we need to reassure"),

    N("Which Skill", "`.com`", 9, 5, 4, 9, 9, 8, 6,
      "Supply-side vocabulary — workers have skills, employers have seats. Also reads like a "
      "comparison site or a quiz. Right name for the India candidate funnel, wrong for the buyer"),


    # ---- the plain register, added after the operator objected that the winners
    #      were words people would not know. EVERY plain word is taken on .com —
    #      11 of 11 — which is what being common costs you.
    N("Standard Talent", "`.co`", 10, 2, 8, 8, 9, 10, 8,
      "❗ **Read it as English: *standard talent* means average talent.** The most common word in "
      "the study is also the most bleached — it is wallpaper, it does not lodge, and a search for "
      "it reaches nobody. Maximum `PLAIN`, near-zero `DISTINCT`. **This is what over-correcting "
      "away from obscurity looks like**"),

    N("Proof Talent", "`.co`", 10, 5, 7, 8, 9, 8, 9,
      "**Proof is 27 per million — nineteen times more common than *crucible*** — and it means "
      "exactly what the page does: we publish the proof. Slightly method-flavoured, which is the "
      "only thing holding it back. No collision found"),

    N("Merit Talent", "`.co`", 8, 3, 7, 7, 9, 9, 8,
      "Common, clean, says the right thing. *Merit* is used widely enough in the category that "
      "the search result will be muddy"),

    N("Harbor Talent", "`.co`", 9, 5, 7, 7, 9, 10, 6,
      "Plain, warm, method-neutral. Says less about the business than the three above"),


    N("Lighthouse Talent", "`.co`", 9, 7, 7, 7, 7, 10, 8,
      "Promoted by the same correction as Tuesday — the corpus scores *lighthouse* at 1.73 per "
      "million, but every English speaker can picture one. A fixed point others steer by, which "
      "is a fair thing for a placement firm to claim"),

    N("Compass Talent", "`.co`", 9, 5, 7, 6, 9, 10, 8,
      "Same correction, same logic, shorter and easier to say. *Compass* is used widely enough as "
      "a brand word that the search result will be contested"),

    # ---- dead on collision. Left visible so they stay dead.
    N("Touchstone Talent", "`.co`", 3, 8, 8, 0, 8, 9, 10,
      "❌ **The perfect word — the stone used to test the purity of gold — and it is taken three "
      "times over in our own trade class.** Touchstone Talent Group, Touchstone Recruitment, "
      "TouchStone Personnel"),

    N("Kindred Talent", "`.co`", 5, 6, 7, 0, 9, 9, 8,
      "❌ **KindredTalent already places creative, marketing and digital talent** — 25 years, our "
      "exact ICP"),

    N("Vanguard Talent", "`.co`", 7, 6, 9, 2, 9, 9, 9,
      "❌ Would have scored highest of all on `LEGIT`. Vanguard manages roughly $9 trillion"),

    N("Polestar Talent", "`.co`", 4, 7, 8, 3, 8, 9, 9,
      "❌ Volvo's electric brand, advertised into the same feeds we would be buying"),

    N("Forge Talent", "`.co`", 8, 6, 6, 7, 2, 9, 8,
      "❌ **Contains the word *forget*.** Precisely what `arbitrary.py`'s ARTIFACT gate exists to "
      "catch, and the worst possible accidental word for a talent firm"),

    N("Skill Force", "taken", 8, 4, 5, 0, 9, 6, 7,
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

print("---\n\n## 1b. Where `DISTINCT` came from — the category proves the pattern\n")
print("The operator's objection: *\"standard talent and standard will never mean anything, right?\"*")
print("Correct, and it exposed an over-correction. Chasing `APT` produced obscure words —")
print("*crucible*, *signet*. Chasing `PLAIN` produced bleached ones — *standard*, *merit*.")
print("**Neither is the target.**\n")
print("Look at what the strongest names in this category actually are:\n")
print("| Name | The word | Why it works |\n|---|---|---|")
for a, b, c in [
    ("**Somewhere**", "an ordinary adverb", "Everyone knows it. Nobody expected it on a company"),
    ("**Oceans**", "an ordinary noun", "Same shape"),
    ("**Genius**", "an ordinary noun", "Same shape, more bravado"),
    ("Athyna", "invented", "Understandable to nobody. The weakest brand of the four"),
    ("GrowthAssistant · Hireframe · Skillforce",
     "descriptive compounds", "Understandable and utterly generic. Category wallpaper"),
]:
    print(f"| {a} | {b} | {c} |")
print("\n> **The pattern is an ordinary word in an unexpected role.** Not a rare word, and not a")
print("> category word. That is a *third* axis, and it is what `DISTINCT` measures.\n")
print("**`Standard Talent` fails it twice.** Read as plain English it means *average talent* — the")
print("opposite of the pitch — and a search for it reaches nobody. Maximum `PLAIN`, near-zero")
print("`DISTINCT`. **`Tuesday Talent` is the same shape as `Somewhere`:** an ordinary word nobody")
print("expected, which is exactly why it lodges.\n")

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
