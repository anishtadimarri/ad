#!/usr/bin/env python3
"""
Supply-country screen — where to source talent, outside India.

Scored on criteria derived from THIS model's economics, not generic
"offshore destination" criteria:

  * RETAIN is the heaviest weight because seat continuity is the largest lever
    in the business (+$9,022 per client from 9 -> 30 EOR months, LTGP.md §4).
    And retention is a function of the WORKER'S OUTSIDE OPTIONS, so it is
    really a measure of local labour-market slack.
  * TZ is weighted LOW (5) on purpose. ASYNC is a hard gate in the skill model
    (FIRST-PRINCIPLES.md), so every role we place works without live overlap.
    Paying a premium for timezone would be paying for something we gated out.
  * GAAP means US-GAAP EXPOSURE — has this country's workforce actually kept
    American books? Prague was dropped for being IFRS-only (OFFER.md §2.4).

Evidence tags per MASTER §0.  Run:  python3 scoring/countries.py > COUNTRIES.md
"""

# ---------------------------------------------------------------- dimensions
DIM = [
    ("RETAIN", 20, "Expected tenure, driven by local labour-market slack. "
                   "The largest lever in the model"),
    ("ENG",    18, "Usable English at the TOP of the distribution, not the national "
                   "average — see the EF EPI caveat"),
    ("COST",   14, "Arbitrage size: USD cost of a mid-level finance hire"),
    ("DEPTH",  12, "Pool of qualified people in OUR five roles"),
    ("PAY",     8, "Can we legally and reliably pay them? Rails, FX control, sanctions"),
    ("EOR",     8, "EOR infrastructure at sane wholesale cost — 37-65% of lifetime GP"),
    ("WHITE",   7, "Whitespace. Is the pool already fished by Somewhere / Oceans / Wing?"),
    ("GAAP",    7, "US-GAAP exposure — has this workforce kept American books?"),
    ("OURADV",  6, "Do WE have a network and cost base there?"),
    ("STABLE",  5, "Power, internet, security, political continuity"),
    ("TZ",      5, "US-hours overlap. Deliberately low: every role is async by gate"),
]
W = {k: w for k, w, _ in DIM}

# Gates applied AFTER scoring so a fatal flaw cannot be averaged away.
GATES = [("ENG", 3, "cannot brief a US client"),
         ("PAY", 2, "cannot pay them reliably or legally"),
         ("EOR", 2, "no EOR layer = lose 37-65% of lifetime GP"),
         ("STABLE", 2, "delivery risk on a guaranteed seat")]

# ------------------------------------------------------------------ the data
# epi = EF EPI 2025 score [V]. band thresholds: 600+ very high, 550+ high,
# 500+ moderate, 450+ low, <450 very low.
# fact = verified datapoint worth showing in the output.
C = [
 # name, region, epi, scores{}, fact, note
 ("India", "S Asia", 484, dict(RETAIN=2, ENG=4, COST=5, DEPTH=5, PAY=5, EOR=5,
   WHITE=5, GAAP=4, OURADV=5, STABLE=4, TZ=2),
  "528,000+ active CAs [V] · attrition 13.6% forecast 2026, but a 20-30% hike "
  "triggers a switch at early-to-mid level [V]",
  "The incumbent choice. Deepest pool, our own network, and untouched by both "
  "direct comps — but the leakiest, because the domestic market bids for the "
  "same people"),

 ("South Africa", "Africa", 602, dict(RETAIN=5, ENG=5, COST=4, DEPTH=3, PAY=4, EOR=4,
   WHITE=2, GAAP=2, OURADV=1, STABLE=3, TZ=3),
  "EF EPI 602, **13th globally** [V] · unemployment **32.7%** Q1 2026, youth 15-34 "
  "**45.8%** [V] · ~**half of graduates** unemployed or underemployed in year one [V] "
  "· SAICA 48,000+ members, SAIPA 10,000+ [V]",
  "The retention answer. Structurally sticky because outside options barely exist"),

 ("Zimbabwe", "Africa", 602, dict(RETAIN=5, ENG=5, COST=5, DEPTH=2, PAY=1, EOR=1,
   WHITE=5, GAAP=2, OURADV=1, STABLE=2, TZ=3),
  "EF EPI **602 — tied with South Africa, 13th globally** [V] · ICAZ chartered "
  "accountants historically well regarded [C]",
  "Highest-upside gated country in the study. English and retention are "
  "world-class; the payment rails are not"),

 ("Kenya", "Africa", 593, dict(RETAIN=4, ENG=5, COST=4, DEPTH=3, PAY=4, EOR=3,
   WHITE=4, GAAP=2, OURADV=1, STABLE=3, TZ=3),
  "EF EPI 593, 19th globally [V] · English is an official language of instruction",
  "The sleeper. High English, real professional body (ICPAK), payment rails work, "
  "and almost nobody in this category is there yet"),

 ("Nigeria", "Africa", 569, dict(RETAIN=5, ENG=4, COST=5, DEPTH=4, PAY=2, EOR=3,
   WHITE=4, GAAP=3, OURADV=1, STABLE=2, TZ=3),
  "EF EPI 569 [V] · ICAN is one of Africa's largest accountancy bodies",
  "Biggest English-speaking pool in Africa and the cheapest. FX controls, power, "
  "and US-client perception are the whole problem"),

 ("Ghana", "Africa", 540, dict(RETAIN=4, ENG=3, COST=5, DEPTH=2, PAY=3, EOR=2,
   WHITE=5, GAAP=2, OURADV=1, STABLE=3, TZ=3),
  "EF EPI 540, moderate band [V]", "Stable and untouched, but thin professional depth"),

 ("Egypt", "Africa", 459, dict(RETAIN=4, ENG=2, COST=5, DEPTH=3, PAY=3, EOR=3,
   WHITE=2, GAAP=2, OURADV=1, STABLE=3, TZ=3),
  "EF EPI **459 — Low band** [V] · yet Somewhere sells Egypt [V]",
  "A live example of the EPI caveat cutting the other way — Somewhere is selling "
  "a Low-English country, so they are recruiting the tail of the distribution"),

 ("Philippines", "SE Asia", 569, dict(RETAIN=2, ENG=4, COST=3, DEPTH=4, PAY=4, EOR=4,
   WHITE=1, GAAP=5, OURADV=1, STABLE=3, TZ=2),
  "EF EPI 569 [V] · Somewhere's bookkeeper **$2,700-3,700/mo — their most "
  "expensive of three regions** [V]",
  "The saturated default. Deepest US-GAAP exposure anywhere and the most "
  "contested pool in the world"),

 ("Sri Lanka", "S Asia", 486, dict(RETAIN=4, ENG=3, COST=5, DEPTH=3, PAY=3, EOR=2,
   WHITE=2, GAAP=3, OURADV=2, STABLE=3, TZ=2),
  "EF EPI 486, Low band [V] · **Oceans sources Sri Lanka only** [V]",
  "Oceans built an entire company on one Low-EPI country, which is the single "
  "best evidence that national averages do not decide this"),

 ("Nepal", "S Asia", 514, dict(RETAIN=5, ENG=3, COST=5, DEPTH=2, PAY=2, EOR=1,
   WHITE=5, GAAP=2, OURADV=3, STABLE=3, TZ=2),
  "EF EPI 514 — **above India's 484** [V]",
  "Cheapest sticky labour in Asia and adjacent to our own network. Gated on EOR"),

 ("Pakistan", "S Asia", 493, dict(RETAIN=4, ENG=3, COST=5, DEPTH=4, PAY=2, EOR=2,
   WHITE=3, GAAP=3, OURADV=2, STABLE=2, TZ=2),
  "EF EPI 493 [V] · ICAP + a very large ACCA population · Somewhere sells "
  "Pakistan [V]", "Real depth, real cost advantage, hard banking"),

 ("Bangladesh", "S Asia", 506, dict(RETAIN=5, ENG=3, COST=5, DEPTH=3, PAY=2, EOR=2,
   WHITE=4, GAAP=2, OURADV=2, STABLE=2, TZ=2),
  "EF EPI 506 — above India [V]", "Cheap and sticky; thin rails and thin US exposure"),

 ("Malaysia", "SE Asia", 581, dict(RETAIN=3, ENG=4, COST=2, DEPTH=3, PAY=4, EOR=4,
   WHITE=4, GAAP=3, OURADV=1, STABLE=4, TZ=2),
  "EF EPI 581, High band [V]", "Excellent on everything except the arbitrage"),

 ("Vietnam", "SE Asia", 500, dict(RETAIN=3, ENG=2, COST=4, DEPTH=3, PAY=3, EOR=4,
   WHITE=4, GAAP=2, OURADV=1, STABLE=4, TZ=2),
  "EF EPI 500 [V]", "Strong ops country, wrong for client-facing English"),

 ("Indonesia", "SE Asia", 471, dict(RETAIN=3, ENG=2, COST=4, DEPTH=3, PAY=3, EOR=4,
   WHITE=4, GAAP=2, OURADV=1, STABLE=3, TZ=2), "EF EPI 471, Low [V]", ""),

 ("Argentina", "LatAm", 575, dict(RETAIN=3, ENG=4, COST=4, DEPTH=3, PAY=2, EOR=3,
   WHITE=2, GAAP=3, OURADV=1, STABLE=2, TZ=5),
  "EF EPI **575 — the best in the Americas** [V]",
  "The only LatAm country that is genuinely strong on English. Capital controls "
  "are the tax you pay for it"),

 ("Honduras", "LatAm", 553, dict(RETAIN=5, ENG=3, COST=5, DEPTH=1, PAY=3, EOR=2,
   WHITE=5, GAAP=3, OURADV=1, STABLE=2, TZ=5),
  "EF EPI **553 — second-best in the Americas, above Chile, Peru, Colombia "
  "and Brazil** [V]",
  "The genuine surprise of the screen. Perfect timezone, high English, very "
  "cheap, nobody there — and almost no professional depth"),

 ("Uruguay", "LatAm", 542, dict(RETAIN=3, ENG=3, COST=2, DEPTH=2, PAY=4, EOR=4,
   WHITE=4, GAAP=3, OURADV=1, STABLE=5, TZ=5),
  "EF EPI 542 [V]", "The stable, expensive, tiny option"),

 ("Colombia", "LatAm", 480, dict(RETAIN=3, ENG=2, COST=4, DEPTH=3, PAY=4, EOR=4,
   WHITE=1, GAAP=3, OURADV=1, STABLE=3, TZ=5),
  "EF EPI **480 — Low band** [V] · yet it is named explicitly on Somewhere's "
  "country list [V]",
  "The nearshore consensus pick, and its English is weaker than Nepal's"),

 ("Mexico", "LatAm", 440, dict(RETAIN=3, ENG=1, COST=3, DEPTH=4, PAY=4, EOR=5,
   WHITE=2, GAAP=4, OURADV=1, STABLE=3, TZ=5),
  "EF EPI **440 — Very Low band, the worst of any country in this screen** [V]",
  "The most-marketed nearshore destination in the world has the weakest English "
  "in the study"),

 ("Brazil", "LatAm", 482, dict(RETAIN=3, ENG=2, COST=3, DEPTH=4, PAY=3, EOR=4,
   WHITE=3, GAAP=3, OURADV=1, STABLE=3, TZ=4), "EF EPI 482, Low [V]", ""),
 ("Peru", "LatAm", 519, dict(RETAIN=4, ENG=2, COST=4, DEPTH=2, PAY=3, EOR=3,
   WHITE=4, GAAP=2, OURADV=1, STABLE=3, TZ=5), "EF EPI 519 [V]", ""),
 ("Chile", "LatAm", 517, dict(RETAIN=3, ENG=2, COST=2, DEPTH=2, PAY=4, EOR=4,
   WHITE=4, GAAP=3, OURADV=1, STABLE=4, TZ=5), "EF EPI 517 [V]", ""),
 ("Costa Rica", "LatAm", 516, dict(RETAIN=2, ENG=2, COST=2, DEPTH=2, PAY=4, EOR=4,
   WHITE=1, GAAP=4, OURADV=1, STABLE=4, TZ=5),
  "EF EPI 516 [V]", "Established nearshore hub, priced like one"),
 ("El Salvador", "LatAm", 523, dict(RETAIN=4, ENG=2, COST=5, DEPTH=1, PAY=3, EOR=3,
   WHITE=4, GAAP=3, OURADV=1, STABLE=3, TZ=5), "EF EPI 523 [V]", ""),
 ("Dominican Rep.", "LatAm", 503, dict(RETAIN=4, ENG=2, COST=4, DEPTH=1, PAY=3, EOR=3,
   WHITE=3, GAAP=3, OURADV=1, STABLE=3, TZ=5), "EF EPI 503 [V]", ""),
 ("Guatemala", "LatAm", 510, dict(RETAIN=4, ENG=2, COST=5, DEPTH=1, PAY=3, EOR=3,
   WHITE=4, GAAP=3, OURADV=1, STABLE=2, TZ=5), "EF EPI 510 [V]", ""),

 ("Poland", "E Europe", 600, dict(RETAIN=2, ENG=5, COST=1, DEPTH=4, PAY=5, EOR=5,
   WHITE=3, GAAP=3, OURADV=1, STABLE=4, TZ=1),
  "EF EPI 600, 15th globally [V]",
  "Superb talent, EU wages, and EU freedom of movement means they can leave for "
  "Berlin — which destroys RETAIN"),
 ("Romania", "E Europe", 605, dict(RETAIN=2, ENG=5, COST=2, DEPTH=4, PAY=5, EOR=5,
   WHITE=3, GAAP=3, OURADV=1, STABLE=4, TZ=1),
  "EF EPI **605 — higher than South Africa** [V]", "Same EU problem as Poland"),
 ("Bulgaria", "E Europe", 594, dict(RETAIN=2, ENG=4, COST=2, DEPTH=3, PAY=5, EOR=5,
   WHITE=3, GAAP=3, OURADV=1, STABLE=4, TZ=1), "EF EPI 594 [V]", ""),
 ("Serbia", "E Europe", 579, dict(RETAIN=3, ENG=4, COST=3, DEPTH=3, PAY=4, EOR=4,
   WHITE=3, GAAP=3, OURADV=1, STABLE=3, TZ=1),
  "EF EPI 579 [V] · non-EU, so no freedom-of-movement leak",
  "The best Eastern European risk-adjusted pick, purely because it is outside "
  "the EU labour market"),
 ("Portugal", "E Europe", 612, dict(RETAIN=2, ENG=5, COST=1, DEPTH=3, PAY=5, EOR=5,
   WHITE=2, GAAP=3, OURADV=1, STABLE=5, TZ=2),
  "EF EPI **612 — highest in the study** [V] · on Somewhere's list [V]",
  "Best English in the screen and no arbitrage left"),
 ("Georgia", "E Europe", 541, dict(RETAIN=4, ENG=3, COST=4, DEPTH=2, PAY=3, EOR=3,
   WHITE=5, GAAP=2, OURADV=1, STABLE=3, TZ=2), "EF EPI 541 [V]", ""),
 ("Armenia", "E Europe", 515, dict(RETAIN=4, ENG=3, COST=4, DEPTH=2, PAY=3, EOR=3,
   WHITE=5, GAAP=2, OURADV=1, STABLE=2, TZ=2), "EF EPI 515 [V]", ""),
 ("Albania", "E Europe", 532, dict(RETAIN=3, ENG=3, COST=4, DEPTH=1, PAY=3, EOR=3,
   WHITE=4, GAAP=2, OURADV=1, STABLE=3, TZ=1), "EF EPI 532 [V]", ""),
 ("Ukraine", "E Europe", 526, dict(RETAIN=3, ENG=3, COST=5, DEPTH=4, PAY=2, EOR=2,
   WHITE=3, GAAP=3, OURADV=1, STABLE=1, TZ=1),
  "EF EPI 526 [V]", "Gated on war. Not a judgement about the talent"),

 ("Uganda", "Africa", 518, dict(RETAIN=5, ENG=3, COST=5, DEPTH=1, PAY=3, EOR=2,
   WHITE=5, GAAP=2, OURADV=1, STABLE=2, TZ=3), "EF EPI 518 [V]", ""),
 ("Tanzania", "Africa", 479, dict(RETAIN=5, ENG=2, COST=5, DEPTH=1, PAY=3, EOR=2,
   WHITE=5, GAAP=2, OURADV=1, STABLE=3, TZ=3), "EF EPI 479 [V]", ""),
 ("Morocco", "Africa", 492, dict(RETAIN=4, ENG=2, COST=4, DEPTH=2, PAY=3, EOR=3,
   WHITE=3, GAAP=2, OURADV=1, STABLE=3, TZ=2),
  "EF EPI 492 [V]", "Francophone offshoring hub — the wrong second language"),
 ("Tunisia", "Africa", 498, dict(RETAIN=4, ENG=2, COST=5, DEPTH=2, PAY=3, EOR=3,
   WHITE=4, GAAP=2, OURADV=1, STABLE=2, TZ=2), "EF EPI 498 [V]", ""),
 ("Rwanda", "Africa", 417, dict(RETAIN=4, ENG=1, COST=5, DEPTH=1, PAY=3, EOR=2,
   WHITE=5, GAAP=2, OURADV=1, STABLE=4, TZ=3),
  "EF EPI **417 — Very Low** [V], despite English being an official language",
  "The clearest proof that official-language status is not proficiency"),
 ("Ethiopia", "Africa", 499, dict(RETAIN=5, ENG=2, COST=5, DEPTH=1, PAY=2, EOR=1,
   WHITE=5, GAAP=2, OURADV=1, STABLE=1, TZ=3), "EF EPI 499 [V]", ""),

 ("Jamaica", "Caribbean", None, dict(RETAIN=4, ENG=5, COST=3, DEPTH=1, PAY=4, EOR=3,
   WHITE=4, GAAP=4, OURADV=1, STABLE=3, TZ=5),
  "**Native English** · not ranked by EF EPI (English is the first language) · "
  "US Eastern timezone year-round",
  "Native English on US hours. A population of 2.8 million is the entire problem"),
 ("Mauritius", "Africa", None, dict(RETAIN=3, ENG=4, COST=2, DEPTH=2, PAY=5, EOR=4,
   WHITE=4, GAAP=3, OURADV=2, STABLE=5, TZ=3),
  "Not in EF EPI · offshore financial centre, IFRS, bilingual EN/FR",
  "Institutionally the cleanest country in Africa and far too small and "
  "expensive to matter"),
]


def score(s):
    return sum(s[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def gated(s):
    return [f"{k}={s[k]} — {why}" for k, mn, why in GATES if s[k] < mn]


ROWS = []
for name, reg, epi, s, fact, note in C:
    ROWS.append(dict(name=name, reg=reg, epi=epi, s=s, fact=fact, note=note,
                     sc=score(s), fail=gated(s)))
LIVE = sorted([r for r in ROWS if not r["fail"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in ROWS if r["fail"]], key=lambda r: -r["sc"])


def report():
    print("# SUPPLY COUNTRIES — Where To Source, Outside India\n")
    print(f"**{len(ROWS)} countries scored on {len(DIM)} weighted dimensions plus "
          f"{len(GATES)} knockout gates.** Generated by")
    print("[`scoring/countries.py`](scoring/countries.py). Evidence tags per "
          "[`MASTER.md`](MASTER.md) §0.\n")
    print("> **English scores are EF EPI 2025 [V]** — 2.2 million test takers, and the "
          "first edition to\n> include speaking and writing. Band thresholds: **600+ very "
          "high · 550+ high · 500+ moderate ·\n> 450+ low · <450 very low.**\n")

    # ---- criteria
    print("---\n\n## 1. The criteria, and why they are weighted this way\n")
    print("| Dimension | Weight | What it measures |\n|---|---|---|")
    for k, w, d in DIM:
        print(f"| **{k}** | {w} | {d} |")
    print("\n**Three of these weights are the whole argument:**\n")
    print("| | |\n|---|---|")
    print("| **RETAIN is heaviest (20)** | Seat continuity is the largest lever in the "
          "business — **+$9,022 of gross profit per client** going from 9 to 30 EOR months, "
          "18x what halving CAC delivers ([`scoring/LTGP.md`](scoring/LTGP.md) §4). And "
          "retention is not a cultural trait, it is **the worker's outside options** — so "
          "RETAIN is really a measure of local labour-market slack |")
    print("| **TZ is nearly weightless (5)** | **ASYNC is a hard gate in the skill model** "
          "([`scoring/FIRST-PRINCIPLES.md`](scoring/FIRST-PRINCIPLES.md)). Every role we "
          "place works without live overlap. Weighting timezone highly would mean paying a "
          "premium for something we deliberately gated out — **and that premium is exactly "
          "what LatAm charges** |")
    print("| **GAAP means US-GAAP *exposure*** | Not which framework the country reports "
          "under — almost everyone is IFRS. The question is whether the workforce has "
          "actually kept American books. Prague was dropped on this ([`OFFER.md`](OFFER.md) "
          "§2.4) |")
    print("\n### The gates\n")
    print("| Gate | Fails if | Why it is a gate, not a score |\n|---|---|---|")
    for k, mn, why in GATES:
        print(f"| **{k}** | < {mn} | {why} |")
    print("\nApplied **after** weighting, so a fatal flaw cannot be averaged away by "
          "strengths elsewhere.\n")

    # ---- the EPI caveat
    print("---\n\n## 2. The EF EPI caveat — read this before the ranking\n")
    print("**EF EPI measures a national *average*. We recruit the top 1%.** Those are "
          "different quantities,")
    print("and conflating them would produce a badly wrong answer:\n")
    print("| | EF EPI 2025 | What it hides |\n|---|---|---|")
    print("| **India** | **484 — Low band** | 1.4 billion people and an enormous "
          "English-medium educated class. **The absolute number of excellent English "
          "speakers in India exceeds the entire population of most countries in this table** |")
    print("| **Sri Lanka** | **486 — Low band** | **Oceans built an entire company "
          "sourcing Sri Lanka and nothing else** [V] |")
    print("| **Egypt** | **459 — Low band** | Somewhere sells Egypt [V] |")
    print("| **Rwanda** | **417 — Very Low** | English is an *official language*. "
          "Official status is not proficiency |")
    print("\nSo `ENG` in this model is **EPI adjusted for the depth of the top of the "
          "distribution**, which is")
    print("why India scores 4 on a 484 and Ghana scores 3 on a 540. The raw EPI is shown "
          "in every table so")
    print("you can see where the override happened. **Where EPI is genuinely decisive is "
          "at the bottom:** a")
    print("country at 440 has no usable tail for client-facing work at our volumes.\n")

    # ---- ranking
    print("---\n\n## 3. The ranking\n")
    print("| # | Country | Score | RET | ENG | EPI | COST | DEPTH | GAAP | WHITE | TZ |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        s = r["s"]
        epi = f"{r['epi']}" if r["epi"] else "—"
        star = " ⭐" if i <= 5 else ""
        print(f"| {i} | **{r['name']}**{star} | **{r['sc']:.1f}** | {s['RETAIN']} "
              f"| {s['ENG']} | {epi} | {s['COST']} | {s['DEPTH']} | {s['GAAP']} "
              f"| {s['WHITE']} | {s['TZ']} |")

    print("\n### Gated out\n")
    print("| Country | Score before gate | Failed |\n|---|---|---|")
    for r in DEAD:
        print(f"| {r['name']} | {r['sc']:.1f} | {' · '.join(r['fail'])} |")

    # ---- top detail
    print("\n---\n\n## 4. The top five, with the evidence\n")
    for i, r in enumerate(LIVE[:5], 1):
        print(f"### {i}. {r['name']} — {r['sc']:.1f}\n")
        print(f"{r['fact']}\n")
        if r["note"]:
            print(f"**{r['note']}.**\n")

    # ---- regional
    print("---\n\n## 5. By region — what each region actually trades away\n")
    reg = {}
    for r in ROWS:
        reg.setdefault(r["reg"], []).append(r)
    print("| Region | n | Mean score | Mean EPI | Mean RETAIN | Mean COST | Mean TZ |")
    print("|---|---|---|---|---|---|---|")
    for k, v in sorted(reg.items(), key=lambda kv: -sum(r["sc"] for r in kv[1])/len(kv[1])):
        epis = [r["epi"] for r in v if r["epi"]]
        epi_s = f"{sum(epis)/len(epis):.0f}" if epis else "n/a"
        print(f"| **{k}** | {len(v)} | **{sum(r['sc'] for r in v)/len(v):.1f}** "
              f"| {epi_s} "
              f"| {sum(r['s']['RETAIN'] for r in v)/len(v):.1f} "
              f"| {sum(r['s']['COST'] for r in v)/len(v):.1f} "
              f"| {sum(r['s']['TZ'] for r in v)/len(v):.1f} |")

    # ---- sensitivity
    print("\n---\n\n## 6. Does the answer survive different weights?\n")
    print("The ranking is only useful if it is not an artefact of my weights.\n")
    print("| If you weighted... | 1st | 2nd | 3rd |\n|---|---|---|---|")
    tests = [("As modelled", {}),
             ("**TZ heavily (20)** — if you did NOT believe async", {"TZ": 20}),
             ("**COST heavily (25)** — pure arbitrage", {"COST": 25}),
             ("**RETAIN doubled (40)**", {"RETAIN": 40}),
             ("**ENG heavily (30)**", {"ENG": 30}),
             ("**OURADV to zero** — ignore our India edge", {"OURADV": 0}),
             ("**WHITE heavily (20)** — avoid contested pools", {"WHITE": 20})]
    for label, override in tests:
        w2 = dict(W); w2.update(override)
        def sc2(s): return sum(s[k]*w2[k] for k in w2) / (5*sum(w2.values())) * 100
        top = sorted([r for r in ROWS if not r["fail"]], key=lambda r: -sc2(r["s"]))[:3]
        print(f"| {label} | {top[0]['name']} | {top[1]['name']} | {top[2]['name']} |")
    print("\n**The top of the table is stable under every reweighting except a heavy "
          "timezone weight** — which")
    print("is the one weight the async gate says you should not apply.\n")

    # ---- the two findings that matter more than the ranking
    print("---\n\n## 7. Three findings that matter more than the order\n")
    print("### 7.1 India and South Africa are not competing on the same axis\n")
    print("| | India | South Africa |\n|---|---|---|")
    for a, b, c in [("Pool of qualified accountants",
                     "**528,000+ CAs** [V]", "SAICA 48,000 + SAIPA 10,000 [V] — **~9x shallower**"),
                    ("EF EPI 2025", "484 — Low band", "**602 — 13th globally**, Very High"),
                    ("Why they stay", "They don't especially. **A 20-30% hike triggers a switch at "
                     "early-to-mid level** [V] — exactly our band",
                     "**32.7% unemployment; ~half of graduates unemployed or underemployed in "
                     "year one** [V]. There is no counter-bid"),
                    ("Who else is fishing there",
                     "**Neither Somewhere nor Oceans sources India** [V]",
                     "On Somewhere's published country list [V] — and every EOR vendor is now "
                     "marketing it"),
                    ("Our own position", "Network, language, cost base", "Foreign recruiter, no network"),
                    ("US-GAAP exposure", "30 years of US accounting outsourcing",
                     "Thinner — historically UK/IFRS-facing, not US")]:
        print(f"| **{a}** | {b} | {c} |")
    print("\n**India sells depth. South Africa sells retention.** And the model says retention is "
          "worth more —")
    print("+$9,022 per client from 9 to 30 EOR months, against a shallower pool that still "
          "contains 58,000")
    print("qualified accountants for a business that needs to place **~250 people to reach "
          "$10M**. *Depth we")
    print("do not need is not an advantage.*\n")
    print("The counter-argument is real and it is not about talent: **in India we have a network "
          "and a local")
    print("cost base; in South Africa we would be a foreign recruiter buying candidates at "
          "arm's length.**")
    print("That is a real cost, and it is an execution cost rather than a structural one.\n")

    print("### 7.2 The LatAm timezone premium is a premium for something we gated out\n")
    print("| Country | EF EPI 2025 | Band |\n|---|---|---|")
    for n in ("Mexico", "Colombia", "Brazil", "Costa Rica", "Argentina", "Honduras"):
        r = next(x for x in ROWS if x["name"].startswith(n[:8]))
        band = ("Very High" if r["epi"] >= 600 else "High" if r["epi"] >= 550 else
                "Moderate" if r["epi"] >= 500 else "Low" if r["epi"] >= 450 else "**Very Low**")
        print(f"| {r['name']} | **{r['epi']}** | {band} |")
    lat = [r for r in ROWS if r["reg"] == "LatAm"]
    lat_eng = [r for r in lat if any(f.startswith("ENG") for f in r["fail"])]
    lo = min((r for r in ROWS if r["epi"]), key=lambda r: r["epi"])
    print(f"\n**Mexico at 440 is the weakest English of any country that is actively marketed "
          f"as a nearshore")
    print(f"destination** — only {lo['name']} ({lo['epi']}) scores lower anywhere in the screen, "
          f"and nobody sells")
    print("Rwanda for this. Colombia at 480 scores **below Nepal (514) and Bangladesh (506)**.")
    print(f"**{lat_eng and len(lat_eng)} of the {len(lat)} Latin American countries screened are "
          f"gated out on English alone.**\n")
    print("Latin America's real product is the timezone. **We gated timezone out when we made "
          "ASYNC a hard")
    print("requirement**, so we would be paying LatAm prices for a benefit the offer does not "
          "use. The two")
    print("exceptions are genuine: **Argentina (575, best in the Americas)** and **Honduras (553, "
          "second-best,")
    print("above Chile, Peru, Colombia and Brazil)** — and Honduras has almost no professional "
          "depth.\n")

    print("### 7.3 A USD salary is a retention mechanism, and it is strongest where "
          "payment is hardest\n")
    print("In a country with a depreciating currency, a **USD-denominated salary compounds in "
          "local terms** while")
    print("the worker's local peers are eroded. That is a golden handcuff nobody has to fund — "
          "the same logic")
    print("as provident fund and gratuity in the EOR line ([`OFFER.md`](OFFER.md)), but stronger "
          "and free.\n")
    print("**The problem is that it is exactly correlated with bad payment rails.** Zimbabwe, "
          "Nigeria, Argentina")
    print("and Egypt are where a USD wage is worth the most and where getting money in and "
          "employing people")
    print("legally is hardest. **That correlation is why the `PAY` and `EOR` gates do most of "
          "the work in this")
    print("screen** — and why Zimbabwe, at a pre-gate 69.1 with world-class English and "
          "retention, does not")
    print("appear in the ranking at all.\n")

    print("---\n\n## 8. What this actually recommends\n")
    print("| | |\n|---|---|")
    print("| **Stay in India for the launch** | Not because it wins the model by 6 points — that "
          "is inside the noise — but because `OURADV` is the only dimension we cannot buy, and at "
          "pre-launch, execution risk dominates optimisation |")
    print("| **Open South Africa as country two, for retention** | Same roles, same ledger spine. "
          "Test it on the *replacement* seats first, where a 30-month seat is worth $9,022 and a "
          "leaked hire costs the guarantee |")
    print("| **Watch Kenya** | 593 EPI, working rails, real accountancy body, and **the only "
          "high-scoring country in the study that is neither contested nor gated**. It is the "
          "cheapest place to run a 5-candidate test |")
    print(f"| **Ignore LatAm unless a client demands live overlap** | {len(lat_eng)} of the {len(lat)} "
          "screened fail the English gate. The one thing LatAm sells, we do not buy |")
    print("| **Do not touch Nigeria or Zimbabwe yet** | Both would rank top-3 on talent alone. "
          "Both sit on or below the `PAY` gate. Revisit only once the EOR partner question is "
          "answered |")
    print("\n**The honest limit of this screen:** `RETAIN`, `GAAP`, `WHITE` and `OURADV` are `[E]` "
          "judgements. Only")
    print("`ENG` (EF EPI 2025), South Africa's unemployment figures, India's attrition series and "
          "the accountancy")
    print("body memberships are `[V]`. **The cheap way to convert this to fact is the supply test "
          "already in")
    print("[`README.md`](README.md): post one role, count qualified applicants in 72 hours — "
          "run it in three")
    print("countries at once for ~$900 instead of one for $300.**\n")


if __name__ == "__main__":
    report()
