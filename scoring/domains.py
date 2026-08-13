#!/usr/bin/env python3
"""
Domain ranking for MODEL V2 — premium creative talent for internet businesses.

The brief changed with the model, so the criteria did too. Two are new:

  SAYSPEOPLE — does the name say PEOPLE AND HIRING rather than PRODUCTION?
               V2's biggest misread risk is being taken for a video studio, which
               is a competitor category, not us. "Reel", "Cut", "Splice", "Frame"
               all fail here however good they sound.

  FALSIFIABLE — V2 sells PREMIUM with no track record. A claim we can PROVE beats
               a claim we ASSERT. "Graded" and "Vetted" point at the retention
               test we actually run; "Caliber", "Select", "Prime" and "Elite" are
               assertions a stranger has no reason to believe.

~4,400 candidates checked against Verisign RDAP. TLD carries only 6 points
because .com turned out to be available for every finalist — so there is no
trust trade-off left to make.

Run:  python3 scoring/domains.py > DOMAINS.md
"""

DIM = [
    ("AUDIO",       18, "**GATE.** Spellable from hearing it once in a Reel"),
    ("SAYSPEOPLE",  16, "Says **people and hiring**, not production. The video-studio "
                        "misread is the expensive one"),
    ("PREMIUM",     15, "Carries the premium positioning without hyperbole"),
    ("FALSIFIABLE", 12, "Is the claim **provable by the retention test**, or merely asserted?"),
    ("FIT",         12, "Boxes in neither video alone (the ladder runs to designer, motion, "
                        "UGC) nor placement alone (EOR sits underneath)"),
    ("CLEAN",       12, "**GATE.** No live collision, no broken register"),
    ("SOUND",        9, "Phonetics and the word junction"),
    ("TLD",          6, "`.com` availability"),
]
W = {k: w for k, w, _ in DIM}
GATES = [("AUDIO", 3, "cannot be spelled from audio — paid clicks leak"),
         ("CLEAN", 3, "a live collision or a broken register")]

N = [
 ("Graded Cast", "gradedcast.com",
  dict(AUDIO=5, SAYSPEOPLE=4, PREMIUM=4, FALSIFIABLE=5, FIT=5, CLEAN=4, SOUND=5, TLD=5),
  "**Casting is the act of choosing creative talent** — a hiring word from the creative "
  "world, not a production word, so it never reads as a studio. And **\"graded\" names the "
  "one thing that makes the premium claim provable**: every candidate carries a retention "
  "score. Faint podcast echo on \"cast\" is the only cost"),
 ("Graded Crew", "gradedcrew.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=3, FALSIFIABLE=5, FIT=5, CLEAN=5, SOUND=4, TLD=5),
  "Warmest of the provable set, and the cleanest register of any candidate. \"Crew\" is "
  "unambiguously people. Weaker on premium — a crew sounds capable rather than exceptional"),
 ("Caliber Hires", "caliberhires.com",
  dict(AUDIO=4, SAYSPEOPLE=5, PREMIUM=5, FALSIFIABLE=3, FIT=3, CLEAN=5, SOUND=5, TLD=5),
  "**The strongest premium word available**, because \"caliber\" is used specifically of "
  "people. Best sound in the set. Two costs: it is an *assertion*, not a proof; and "
  "\"Hires\" foregrounds placement, which makes EOR a non-sequitur. "
  "**`calibrehires.com` is also free — buy both spellings for $24**"),
 ("Vetted Cast", "vettedcast.com",
  dict(AUDIO=5, SAYSPEOPLE=4, PREMIUM=4, FALSIFIABLE=5, FIT=5, CLEAN=4, SOUND=4, TLD=5),
  "\"Vetted\" is more everyday than \"graded\" and equally provable. Slightly more generic — "
  "every staffing firm claims vetting, and few can show a score"),
 ("Graded Roster", "gradedroster.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=3, FALSIFIABLE=5, FIT=5, CLEAN=4, SOUND=4, TLD=5),
  "\"Roster\" is the client's word for their own team, which is the right side of the "
  "table. Faint shift-scheduling echo"),
 ("Caliber Roster", "caliberroster.com",
  dict(AUDIO=4, SAYSPEOPLE=5, PREMIUM=5, FALSIFIABLE=3, FIT=5, CLEAN=5, SOUND=4, TLD=5),
  "**Caliber's premium with Roster's better fit** — no placement-only problem, so EOR "
  "sits naturally underneath. Four syllables is the cost"),
 ("Graded Talent", "gradedtalent.com",
  dict(AUDIO=5, SAYSPEOPLE=4, PREMIUM=3, FALSIFIABLE=5, FIT=5, CLEAN=4, SOUND=4, TLD=5),
  "Safest and most generic. \"Talent\" is the category's most-used word — legible and "
  "undifferentiated at once"),
 ("Select Hires", "selecthires.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=4, FALSIFIABLE=2, FIT=3, CLEAN=4, SOUND=4, TLD=5),
  "Clean and premium-adjacent, and **\"select\" is the weakest kind of claim** — it asserts "
  "curation without describing any test"),
 ("Chosen Hires", "chosenhires.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=3, FALSIFIABLE=2, FIT=3, CLEAN=4, SOUND=4, TLD=5),
  "Same shape as Select Hires with a faint religious echo"),
 ("Merit Roster", "meritroster.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=4, FALSIFIABLE=4, FIT=5, CLEAN=4, SOUND=4, TLD=5),
  "**Underrated.** \"Merit\" implies a standard was applied rather than asserted, which is "
  "most of what \"graded\" buys, in a warmer word"),
 ("Sterling Guild", "sterlingguild.com",
  dict(AUDIO=4, SAYSPEOPLE=4, PREMIUM=5, FALSIFIABLE=2, FIT=5, CLEAN=5, SOUND=5, TLD=5),
  "Most institutional-sounding option and the best pure *sound*. \"Guild\" is niche and "
  "\"sterling\" is an assertion"),
 ("Marked Crew", "markedcrew.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=2, FALSIFIABLE=4, FIT=5, CLEAN=2, SOUND=4, TLD=5),
  "\"Marked\" means graded in British school usage — and to an American ear a *marked man* "
  "is in trouble. **Gated on register**"),
 ("Scored Crew", "scoredcrew.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=2, FALSIFIABLE=5, FIT=5, CLEAN=2, SOUND=4, TLD=5),
  "Most literally provable word in the set, and \"scored\" carries a sexual slang reading "
  "in US English applied to people. **Gated**"),
 ("Rated Crew", "ratedcrew.com",
  dict(AUDIO=5, SAYSPEOPLE=5, PREMIUM=2, FALSIFIABLE=4, FIT=5, CLEAN=3, SOUND=4, TLD=5),
  "Reads as a review site — the buyer expects to *see* the ratings, which we do not publish"),
 ("Hallmark Talent", "hallmarktalent.com",
  dict(AUDIO=5, SAYSPEOPLE=4, PREMIUM=5, FALSIFIABLE=4, FIT=5, CLEAN=1, SOUND=4, TLD=5),
  "A hallmark is literally a struck mark certifying purity — perfect meaning. **And "
  "Hallmark is one of the most recognised consumer brands in America.** Gated"),
 ("Yardstick Talent", "yardsticktalent.com",
  dict(AUDIO=5, SAYSPEOPLE=4, PREMIUM=4, FALSIFIABLE=5, FIT=5, CLEAN=2, SOUND=4, TLD=5),
  "**Yardstick Management** is a US consultancy doing *\"talent search and acquisitions\"*. "
  "Gated, again"),
 ("World Class Crew", "worldclasscrew.com",
  dict(AUDIO=4, SAYSPEOPLE=5, PREMIUM=5, FALSIFIABLE=1, FIT=5, CLEAN=4, SOUND=3, TLD=5),
  "States the claim outright, which is exactly why it is the least believable name here. "
  "**An unprovable superlative from an unknown company reads as marketing**"),
 ("Gumption Talent", "gumptiontalent.com",
  dict(AUDIO=5, SAYSPEOPLE=4, PREMIUM=3, FALSIFIABLE=2, FIT=5, CLEAN=5, SOUND=4, TLD=5),
  "Carried over from the earlier round. Warm and characterful, and it makes a claim about "
  "*grit* rather than *quality* — which is a weaker fit for a premium creative positioning"),
]


def sc(x): return sum(x[k]*W[k] for k in W) / (5*sum(W.values())) * 100
def fails(x): return [f"{k}={x[k]}" for k, mn, _ in GATES if x[k] < mn]

R = [dict(n=n, d=d, x=x, note=t, sc=sc(x), f=fails(x)) for n, d, x, t in N]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])


def report():
    print("# DOMAIN RANKING — Model V2\n")
    print("**~4,400 candidates generated and checked against Verisign RDAP.** The brief changed "
          "with the model,")
    print("so two criteria are new. Generated by [`scoring/domains.py`](scoring/domains.py).\n")

    print("---\n\n## 1. The two new criteria, and why they decide it\n")
    print("### `SAYSPEOPLE` — the video-studio misread is the expensive one\n")
    print("V2 sells **people**. A production studio is a **competitor category.** So every "
          "name that sounds")
    print("like a studio is disqualified however well it reads — which kills the entire "
          "film-craft register")
    print("that a creative-talent business would otherwise reach for first:\n")
    print("| Tempting | Why it fails |\n|---|---|")
    for a, b in [("Reel · Cut · Splice · Frame · Render · Footage",
                  "All name the **output**. A buyer hearing them expects to buy video, not hire a person"),
                 ("**Cast · Casting · Callback · Slate · Lineup**",
                  "**All name the act of choosing people.** Creative-world vocabulary that is "
                  "about *hiring*, which is the half we want")]:
        print(f"| {a} | {b} |")

    print("\n### `FALSIFIABLE` — a claim you can prove beats a claim you assert\n")
    print("V2's positioning is **premium**, from a company with no track record. That makes the "
          "*kind* of claim")
    print("matter more than its strength:\n")
    print("| | Words | The buyer's reaction |\n|---|---|---|")
    for a, b, c in [("**Provable**", "Graded · Vetted · Merit · Tested",
                     "*\"Graded how?\"* — and we answer with the retention test. **The name "
                     "creates the sales conversation we want**"),
                    ("Asserted", "Caliber · Select · Chosen · Sterling · Prime",
                     "*\"Says you.\"* Credible from an incumbent, thin from a stranger"),
                    ("Superlative", "World Class · Elite · Best",
                     "**Reads as marketing.** The least believable option is the one that "
                     "states the claim outright")]:
        print(f"| {a} | {b} | {c} |")

    print("\n---\n\n## 2. On TLDs: the question turned out to be moot\n")
    print("`.com` is **available for every finalist** — so there is no trust trade-off to make, "
          "and `TLD` carries")
    print("only 6 of 100 points. For reference, the ordering that would have applied:\n")
    print("| TLD | Trust for a US B2B buyer | Verdict |\n|---|---|---|")
    for a, b, c in [(".com", "**5** — the only one that needs no explanation", "**Take it**"),
                    (".co", "4 — reads as a company abbreviation", "Buy defensively, ~$30"),
                    (".net", "3 — trusted and dated", "Skip"),
                    (".io", "3 — reads as dev tools, plus the Chagos sovereignty question", "Skip"),
                    (".ai", "3 in tech circles — and **it misrepresents a business that sells "
                            "humans**", "Actively wrong here"),
                    (".studio", "2 — and it says *studio*, the one thing we are not", "Never"),
                    (".team · .work · .agency", "2 — reads as the domain you bought because the "
                     "`.com` was gone", "Skip")]:
        print(f"| **{a}** | {b} | {c} |")

    print("\n---\n\n## 3. THE RANKING\n")
    print("| # | Name | Domain | Score | AUD | PPL | PREM | PROV | FIT | CLN | SND |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        x = r["x"]; star = " ⭐" if i <= 3 else ""
        print(f"| **{i}** | **{r['n']}**{star} | `{r['d']}` | **{r['sc']:.1f}** | {x['AUDIO']} "
              f"| {x['SAYSPEOPLE']} | {x['PREMIUM']} | {x['FALSIFIABLE']} | {x['FIT']} "
              f"| {x['CLEAN']} | {x['SOUND']} |")
    print("\n### Gated out\n")
    print("| Name | Domain | Score | Failed | Why |\n|---|---|---|---|---|")
    for r in DEAD:
        print(f"| {r['n']} | `{r['d']}` | {r['sc']:.1f} | {', '.join(r['f'])} | {r['note']} |")

    print("\n---\n\n## 4. The top four, with the argument\n")
    for i, r in enumerate(LIVE[:4], 1):
        print(f"**{i}. {r['n']}** · `{r['d']}` · **{r['sc']:.1f}**  \n{r['note']}.\n")

    print("---\n\n## 5. What to buy\n")
    a, b = LIVE[0], LIVE[1]
    print(f"| | Domain | Why |\n|---|---|---|")
    print(f"| **Primary** | **`{a['d']}`** | Top of the ranking. **The only name that is "
          f"simultaneously a hiring word, a creative-world word, and a provable claim** |")
    print(f"| **Runner-up, buy it too** | `{b['d']}` | Warmer and cleaner register, one point "
          f"behind. Worth $12 to hold |")
    print("| **If premium matters more than provable** | `caliberhires.com` **and** "
          "`calibrehires.com` | Best sound and the strongest premium word. **Buy both spellings** "
          "— the American/British split is a real audio leak, and both are free |")
    print("| **Defensive** | the matching `.co` for whichever you pick | ~$30. Not for launching on |")
    print(f"\n**Total to hold the field: about $60.**\n")
    print("**And the test is unchanged.** A name is a 5% variable; the first line of the ad is a "
          "50% one. These")
    print("are cheap enough to hold two and let the first campaign decide — the same two-brand "
          "split already")
    print("budgeted inside the $1,500 demand test.\n")
    print("---\n\n*Availability checked against Verisign RDAP. Re-verify before purchase; "
          "domains move.*\n")


if __name__ == "__main__":
    report()
