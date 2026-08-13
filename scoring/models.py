#!/usr/bin/env python3
"""
V1 vs V2 — scored against the criteria that accumulated across all ten screens.

Not a fresh opinion. Each dimension below is a finding some earlier screen already
produced, so this is a consolidation rather than a new judgement.

CLEARS30 is a GATE because it is the operator's own hard constraint, not a
preference. Note that V2 only clears it under Reading A of its own §7 — under
Reading B it scores 1 and the whole model fails.

Run:  python3 scoring/models.py > /dev/null   (output appended to MODEL-V2.md)
"""

DIM = [
    ("CLEARS30",   18, "**GATE.** Clears the 30-day LTGP:CAC ≥ 1.5:1 hard constraint",
                       "scoring/LTGP.md"),
    ("TRUECLAIM",  16, "Is the arbitrage claim **true against the buyer's actual "
                       "comparator** — the vendor invoice, not a US salary", "LENSES.md §1"),
    ("FOUNDERFIT", 14, "Can the operator **personally grade the work** and run the sale, "
                       "month one, with no team", "LAUNCH.md §1"),
    ("META",       13, "Ad legibility cold, and buyer reachable on **FB and IG**",
                       "MAP.md §5B-5C"),
    ("COMPOUND",   13, "Builds an asset over 24 months — spine, ladder, seats-per-client",
                       "COMPOUND.md"),
    ("DURABLE",     9, "Survives AI over 3-5 years", "SKILLS-INDIA.md · COMPOUND.md"),
    ("WHITE",       7, "Competitive whitespace", "COMPETITOR-DATA.md"),
    ("OPSLOAD",     5, "Low operational intensity — twice rejected as a constraint",
                       "SCALE.md §1"),
    ("EV",          5, "Quality of the enterprise-value story at exit", "SCALE.md §10"),
]
W = {k: w for k, w, _, _ in DIM}
GATE = ("CLEARS30", 3)

V1 = dict(CLEARS30=5, TRUECLAIM=2, FOUNDERFIT=2, META=5, COMPOUND=5,
          DURABLE=4, WHITE=2, OPSLOAD=4, EV=4)
V2 = dict(CLEARS30=4, TRUECLAIM=5, FOUNDERFIT=5, META=4, COMPOUND=4,
          DURABLE=3, WHITE=4, OPSLOAD=3, EV=4)
V2B = dict(V2); V2B["CLEARS30"] = 1        # V2 read as a monthly markup

WHY = {
 "CLEARS30":  ("**5** — 4.25:1, the best modelled",
               "**4** — 3.86-4.56:1 at the $18-21.6k band, **and only under Reading A**"),
 "TRUECLAIM": ("**2** — 0.4-1.1x against a bookkeeping firm, the vendor most $3-30M brands "
               "actually use",
               "**5** — **4.0-13.2x against the video vendor invoice, the largest true claim "
               "in the study**"),
 "FOUNDERFIT":("**2** — cannot grade a reconciliation. Fixable with one hired CA, but it is a "
               "month-one dependency",
               "**5** — hold rate, retention curve and CTR are the numbers he reads for a "
               "living. **His own trade**"),
 "META":      ("**5** — 96.0 Meta-sellability, the most legible role in the 179-role study",
               "**4** — \"video editor\" is clear, but not 96.0 clear"),
 "COMPOUND":  ("**5** — 95.6. Ledger spine, ladder to controller, every ICP runs QuickBooks",
               "**4** — 75.6. The ad account is a real spine and the creative ladder is real, "
               "but both are thinner"),
 "DURABLE":   ("**4** — ledger automation is real and slow",
               "**3** — **the weakest number in V2**, and nothing in V2 currently hedges it"),
 "WHITE":     ("**2** — Somewhere, Oceans, Entigrity and a dozen more",
               "**4** — nobody sells Indian performance editors to agencies as a direct hire"),
 "OPSLOAD":   ("**4** — pure handoff",
               "**3** — handoff plus a weekly newsletter and daily X during launch month"),
 "EV":        ("**4** — recurring EOR book, 32-36% EBITDA plan",
               "**4** — talent + demand intelligence and a **transferable** media asset, "
               "against SCALE.md's finding that founder-brand audiences are not"),
}

GAPS = [
 (1, "**The pricing conflation**", "fatal if unresolved",
  "§7 reads as both a one-time fee and a monthly markup. **Reading A gives 4.21:1; Reading B "
  "gives 0.51:1 and fails the hard constraint.** 8.2x apart on month-one cash",
  "State it: **one-time, 30-35% of first-year compensation**, plus optional recurring EOR"),
 (2, "**No money step before placement**", "high",
  "V2 §10 runs ad → LP → qualification → call → matching → placement. **There is no paid gate.** "
  "V1's $500 funded the search, filtered tyre-kickers and produced the fill rate the whole model "
  "rests on. Removing it means unfunded searches and no commitment signal",
  "Re-insert it as a **paid ad-account and creative teardown** ([`OFFER.md`](OFFER.md) §9.1) — "
  "he can perform it himself, and it *is* the work sample"),
 (3, "**No guarantee specified**", "high",
  "V1's 12-month unlimited replacement with no cash refunds was modelled as **cheaper than the "
  "6-month industry standard** while sounding stronger. V2 does not mention a guarantee, which "
  "is the cheapest differentiation available",
  "Carry it over verbatim"),
 (4, "**EOR demoted to \"optional layer\"**", "high",
  "It is **37-65% of lifetime gross profit**. Attach at 40% instead of 75% takes lifetime from "
  "11.35:1 to 9.50:1. [`SCALE.md`](SCALE.md) §7 concluded: make it the default, not the upsell",
  "Present it as the default employment path, with direct hire as the alternative"),
 (5, "**No retention mechanism**", "high",
  "Seat continuity is worth **+$9,022 per client** (9 → 30 EOR months) — the largest lever in "
  "the business. V2 does not mention retention, replacement or the bench",
  "The graded directory from placement one ([`HUNGRY.md`](HUNGRY.md) §9): a Slack, a roster, and "
  "the score already being produced"),
 (6, "**\"Premium\" has no rubric**", "high",
  "Premium *is* the positioning, and it is currently an adjective. Without a measurable "
  "definition the promise is empty and the graded work sample has nothing to grade against",
  "Define it as one test: **recut an existing ad, measure 3-second and 15-second retention "
  "against the original.** Publishable, gradeable by him, and it doubles as the sales asset"),
 (7, "**Creators conflict with the fee model**", "medium",
  "[`HUNGRY.md`](HUNGRY.md) §7 — creators buy **per video or on a freelance retainer**, so there "
  "is no salary for a 30% fee to attach to. `AFFORD`=3 was pointing at exactly this",
  "Launch on **agencies + e-comm only**. Creators are expansion and need a different fee"),
 (8, "**Five ICPs starves Meta of signal**", "medium",
  "V2 says do not operationalise all five, which is right, and then lists five. Meta needs "
  "concentration to learn, and each ICP × role needs its own ad, LP and intake script",
  "Two ICPs, one role, two ads. Expand after the first ten placements"),
 (9, "**Philippines is the wrong country two**", "medium",
  "V2 names it. [`COUNTRIES.md`](COUNTRIES.md) scored it **61.6 with `WHITE`=1** — the most "
  "contested pool in the world — and it is Somewhere's **most expensive** region. **South Africa "
  "scored 74.5 and wins on retention**, which is the biggest lever",
  "South Africa as country two, for the retention mechanism"),
 (10, "**\"Performance video editor\" may not be a searched title**", "medium",
  "[`TARGETING.md`](TARGETING.md)'s intent seed depends on scraping job postings. If agencies "
  "post \"video editor\" or \"creative editor\" and never \"performance video editor\", the "
  "audience build misses them",
  "Free, one afternoon: **count postings across all three phrasings** before writing the ad"),
 (11, "**Media has no time budget**", "low",
  "A weekly newsletter plus daily X during a one-month launch is a real cost against the only "
  "scarce resource — his attention",
  "**X only at launch.** Newsletter at month three, with the first NUMBER drawn from the first "
  "ten placements rather than from research"),
 (12, "**AIDUR is unhedged**", "low now, high by month twelve",
  "`DURABLE`=3 is V2's weakest score and carries real weight. Generative video is the "
  "fastest-moving substitution risk in the study",
  "Declare the **finance spine as the month-six second leg** — it scores 95.6 on compounding and "
  "exists precisely to be the durable half"),
]


def sc(x):
    return sum(x[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def report():
    print("\n---\n\n## 8. Rated: V1 vs V2, on the criteria the repo already produced\n")
    print("Not a fresh opinion — **every dimension below is a finding from an earlier screen**, so "
          "this is a")
    print("consolidation. `CLEARS30` is a gate because it is the operator's own hard constraint.\n")
    print("| Dimension | Wt | V1 — finance spine | V2 — performance creative | Source |")
    print("|---|---|---|---|---|")
    for k, w, _, src in DIM:
        a, b = WHY[k]
        print(f"| **{k}** | {w} | {a} | {b} | [`{src.split()[0]}`]({src.split()[0]}) |")
    s1, s2, s2b = sc(V1), sc(V2), sc(V2B)
    print(f"| **TOTAL** | | **{s1:.1f}** | **{s2:.1f}** | |")

    print(f"\n### The verdict\n")
    print(f"| | Score | |\n|---|---|---|")
    print(f"| **V2 — performance creative, Reading A** | **{s2:.1f}** | ✅ **Winner** |")
    print(f"| V1 — finance spine | {s1:.1f} | Loses by {s2-s1:.1f} |")
    print(f"| **V2 — Reading B (monthly markup)** | **{s2b:.1f}** | ❌ **Gated out on `CLEARS30`** |")
    print(f"\n**V2 wins by {s2-s1:.1f} points, which is real but not overwhelming — and the entire "
          f"margin comes from")
    print("three dimensions:** `TRUECLAIM` (+3), `FOUNDERFIT` (+3) and `WHITE` (+2). Those are the "
          "three things")
    print("that decide whether a stranger with no track record can get a first sale at all.\n")
    print(f"**V1 wins on `COMPOUND`, `DURABLE` and `META` — all by one point each.** Those decide "
          f"whether the")
    print("business is still good in year three. **So the honest reading is not \"V2 is better\" "
          "but:**\n")
    print("> **V2 is the better way to start. V1 is the better thing to own.** The plan should be "
          "V2 now with\n> V1 declared as the month-six second leg — which is gap 12 below, and the "
          "single most important\n> structural addition to V2.\n")
    print(f"**And note the third row.** Read as a monthly markup, V2 scores {s2b:.1f} and gates "
          f"out. **The pricing")
    print("sentence is not a detail — it is the difference between the best model produced so far "
          "and one that")
    print("fails the operator's own constraint.**\n")

    print("---\n\n## 9. The gaps, prioritised\n")
    print("| # | Gap | Severity | Why it matters | Fix |")
    print("|---|---|---|---|---|")
    for n, g, sev, why, fix in GAPS:
        print(f"| **{n}** | {g} | {sev} | {why} | {fix} |")

    print("\n### The six that change the numbers\n")
    print("**Gaps 1-6 are not polish.** Each one either breaks the model or removes a lever the "
          "repo has already")
    print("quantified:\n")
    print("| Gap | What it costs if unfixed |\n|---|---|")
    for a, b in [
        ("1 — pricing", "**8.2x of month-one cash**, and the hard constraint"),
        ("2 — no paid gate", "Unfunded searches, no commitment filter, and the fill rate the "
         "model rests on"),
        ("3 — no guarantee", "The cheapest differentiation available, given away"),
        ("4 — EOR optional", "**37-65% of lifetime gross profit** demoted to an upsell"),
        ("5 — no retention", "**+$9,022 per client** — the largest single lever in the business"),
        ("6 — \"premium\" undefined", "The whole positioning, and the work sample has no rubric"),
    ]:
        print(f"| **{a}** | {b} |")
    print("\n**Fix those six and V2 is straightforwardly the strongest version of this business "
          "produced so far.**")
    print("Five of the six are carried over from V1 verbatim — **V2's gaps are mostly things it "
          "dropped, not")
    print("things it got wrong.**\n")


if __name__ == "__main__":
    report()
