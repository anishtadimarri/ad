#!/usr/bin/env python3
"""
THE LAUNCH SCREEN — which skill to start with, given one operator and one month.

Every other screen in this repo asks which skill is BEST. This asks which is
LAUNCHABLE, and they are different questions because the launch constraints are
not the steady-state constraints:

    one operator · no team · ~$2,000 of test budget · thirty days · no track record

Three criteria appear here that appear nowhere else, and they are the ones that
actually decide it:

  FOUNDERGRADE — can the operator PERSONALLY judge whether the output is good?
                 Month one there is no team, and the offer's core promise is a
                 graded work sample (OFFER.md §2.5). You cannot promise quality
                 you cannot personally verify. This is the criterion that most
                 changes the answer, and no earlier screen contains it.

  TRUE         — is the arbitrage claim true for the audience we can actually
                 BUY? LENSES.md found the bookkeeper claim is 3.75x against an
                 employer and 0.4-1.1x against a bookkeeping firm.

  FILL30       — can we source, grade and place this in thirty days with the
                 network we already have, which is India and nothing else.

Evidence tags per MASTER §0.  Run:  python3 scoring/launch.py > LAUNCH.md
"""

DIM = [
    ("LEGIBLE",      20, "**GATE.** Is the ad comprehensible cold, in three seconds, to a "
                         "buyer who has never heard of us? (MAP.md Meta-sellability)"),
    ("TRUE",         18, "Is the arbitrage claim **true for the audience we can buy**? "
                         "(LENSES.md §1 — vendor invoice vs US salary)"),
    ("FOUNDERGRADE", 16, "**Can the operator personally judge the output**, month one, "
                         "with no team? The promise is a graded work sample"),
    ("FILL30",       14, "Can we source, grade and place in **30 days** with the network "
                         "we have — India, and no other"),
    ("ECON",         12, "30-day LTGP:CAC at the funnel-derived $976 CAC"),
    ("BUYER",        10, "Buyer is FB **and** IG native, owner-led, decides same day"),
    ("FIRST",        10, "Is this a plausible **first** offshore hire, or does the client "
                         "have to be large already?"),
]
W = {k: w for k, w, _ in DIM}
GATES = [("LEGIBLE", 4, "the cold ad does not land, so there is no funnel to test"),
         ("FOUNDERGRADE", 2, "cannot judge the work, so cannot promise quality or grade a hire"),
         ("FILL30", 3, "cannot fill it inside the test window")]

S = [
 ("Video editor → marketing agencies",
  dict(LEGIBLE=4, TRUE=5, FOUNDERGRADE=5, FILL30=5, ECON=4, BUYER=5, FIRST=4),
  "$5,000-16,500/mo vendor invoice vs $1,250/mo hire — **4.0x-13.2x, the largest "
  "true claim in the repo** [V] · Mumbai is the largest VFX hub on earth, DNEG holds "
  "8 Academy Awards [V] · agency owners score **FB 5 / IG 5** [V] · 3.26:1 at a "
  "$15k salary",
  "**The operator can grade this himself.** An ad editor's work is scored on hold "
  "rate and CTR — the numbers he reads for a living. Every other seat needs a hired "
  "expert to judge candidates, and month one there is nobody to hire them"),

 ("Bookkeeper → e-comm (MAP.md's pick)",
  dict(LEGIBLE=5, TRUE=4, FOUNDERGRADE=2, FILL30=5, ECON=5, BUYER=5, FIRST=5),
  "**96.0 Meta-sellability — the most legible role in the entire study** [V] · "
  "**528,000+ Indian CAs** [V] · 4.25:1 on 30 days, the best economics modelled · "
  "**but 0.4-1.1x against a bookkeeping firm** [V], true only against employers",
  "**Best ad, best economics, and the operator cannot grade a reconciliation.** "
  "Fixable for a few hundred dollars by paying one Indian CA to score work samples "
  "— but it is a real month-one dependency that the video seat does not have"),

 ("Paid media ops → e-comm + agencies",
  dict(LEGIBLE=4, TRUE=3, FOUNDERGRADE=5, FILL30=5, ECON=4, BUYER=5, FIRST=3),
  "Agency management fees $1,500-5,000/mo vs $2,000/mo hire — **0.8x-2.5x, thin** "
  "[V] · India's own D2C market is $108.76B in 2026 [V]",
  "The operator's own trade, so `FOUNDERGRADE`=5. Held back by a thin vendor "
  "arbitrage and by `FIRST`=3 — **paid media is the last function an owner hands to "
  "a stranger**, because the account holds the money"),

 ("3D / product renders → e-comm + architecture",
  dict(LEGIBLE=4, TRUE=4, FOUNDERGRADE=4, FILL30=4, ECON=4, BUYER=4, FIRST=3),
  "$1,500-5,000 per asset vs $1,250/mo [V] · same VFX cohort [V]",
  "Renders are visually gradeable by anyone with taste, so `FOUNDERGRADE` is high "
  "without domain training. Narrower buyer and a harder first hire"),

 ("Data & analytics → e-comm",
  dict(LEGIBLE=3, TRUE=3, FOUNDERGRADE=4, FILL30=5, ECON=4, BUYER=5, FIRST=2),
  "GCC-trained cohort, attrition ~12.6% [V]",
  "**Gated on legibility.** *\"Cohort analysis\"* does not survive three seconds in "
  "a feed, and it is nobody's first offshore hire"),

 ("AP / AR → e-comm + agencies",
  dict(LEGIBLE=4, TRUE=4, FOUNDERGRADE=2, FILL30=5, ECON=4, BUYER=5, FIRST=4),
  "0-0.5 week switch cost from bookkeeper [V] · AR is the agency vertical's #1 felt "
  "pain [V]",
  "**The natural second seat, not a launch seat.** Same bench, same spine — it "
  "exists to raise seats-per-client after the first placement lands"),

 ("Construction estimating → trade contractors",
  dict(LEGIBLE=4, TRUE=4, FOUNDERGRADE=1, FILL30=2, ECON=4, BUYER=5, FIRST=4),
  "**#1 on the bottleneck screen at 94.8** [V] · *\"structurally limited in how much "
  "work it can chase\"* [V] · best Facebook buyer in the study",
  "**The best business in the repo and the worst launch.** The operator cannot read "
  "a takeoff, has no estimator network in India, and cannot evaluate the expert he "
  "would hire to evaluate candidates. **That is the who-grades-the-grader problem, "
  "and month one is the worst possible time to have it**"),

 ("PI medical record review → law firms",
  dict(LEGIBLE=3, TRUE=4, FOUNDERGRADE=1, FILL30=2, ECON=5, BUYER=4, FIRST=4),
  "#3 on the bottleneck screen · richest buyer in the set [V] · Indian LPOs already "
  "sell it [V]",
  "Same problem, plus UPL exposure and a buyer weak on Instagram. **A year-two "
  "business with a hired domain lead**"),

 ("RCM / medical coding → practices",
  dict(LEGIBLE=3, TRUE=4, FOUNDERGRADE=1, FILL30=2, ECON=4, BUYER=4, FIRST=4),
  "Indian RCM is a multi-billion export industry [V] · `WHITE`=1, the most contested "
  "offshore category there is [V]",
  "Domain grading, HIPAA, and entrenched incumbents at once"),

 ("AI workflow ops → SMBs",
  dict(LEGIBLE=3, TRUE=4, FOUNDERGRADE=4, FILL30=3, ECON=4, BUYER=4, FIRST=2),
  "**AI Engineer was LinkedIn's #1 fastest-growing US title, +143% YoY** [V]",
  "**Gated on legibility, and it is the right call for now.** No SMB owner is "
  "searching for this seat by name yet. Revisit in twelve months — the demand curve "
  "is the steepest in the study"),
]


def sc(x):
    return sum(x[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def fails(x):
    return [f"{k}={x[k]}" for k, mn, _ in GATES if x[k] < mn]


R = [dict(n=n, x=x, ev=e, note=t, sc=sc(x), f=fails(x)) for n, x, e, t in S]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])


def report():
    print("# THE LAUNCH SCREEN — What To Start With\n")
    print("Every other screen asks which skill is **best**. This asks which is **launchable**, and "
          "they are")
    print("different questions, because the launch constraints are not the steady-state ones:\n")
    print("> **one operator · no team · ~$2,000 of test budget · thirty days · no track record**\n")
    print("Generated by [`scoring/launch.py`](scoring/launch.py). Inputs from all six earlier "
          "screens.\n")

    print("---\n\n## 1. The criterion that changes the answer\n")
    print("### `FOUNDERGRADE` — can *you* tell whether the work is any good?\n")
    print("The offer's core promise is a **graded work sample on the client's own books** "
          "([`OFFER.md`](OFFER.md) §2.5).")
    print("Month one there is no team. **You cannot promise quality you cannot personally "
          "verify** — and if you")
    print("hire someone to verify it, you have a second problem: **you cannot evaluate the "
          "evaluator either.**\n")
    print("| Seat | Can the operator grade it? |\n|---|---|")
    for a, b in [
        ("**Video editor**", "✅ **Yes, natively.** Hold rate, retention curve, CTR — the numbers "
         "he reads for a living"),
        ("**Paid media ops**", "✅ **Yes, natively.** It is his own trade"),
        ("3D renders", "✅ Mostly — visual work is judged by looking"),
        ("Bookkeeper / AP / AR", "⚠️ **No** — but cheaply fixed. Pay one Indian CA a few hundred "
         "dollars to score work samples"),
        ("**Estimating · PI records · RCM**", "❌ **No, and not cheaply.** He cannot read a "
         "takeoff, and cannot judge the expert he would hire to read one. **The who-grades-the-"
         "grader problem**"),
    ]:
        print(f"| {a} | {b} |")
    print("\n**No earlier screen contains this criterion, and it is the reason the bottleneck "
          "winners are not the")
    print("launch winners.** Construction estimating is the best business found in this repo and "
          "close to the")
    print("worst possible thing to launch alone in thirty days.\n")

    print("---\n\n## 2. The criteria\n")
    print("| Dimension | Weight | What it measures |\n|---|---|---|")
    for k, w, d in DIM:
        print(f"| **{k}** | {w} | {d} |")
    print("\n| Gate | Fails below | Why |\n|---|---|---|")
    for k, mn, why in GATES:
        print(f"| **{k}** | {mn} | {why} |")

    print("\n---\n\n## 3. THE RANKING\n")
    print("| # | Seat → buyer | Score | LEG | TRUE | GRADE | FILL | ECON | BUY | 1st |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        x = r["x"]; star = " ⭐" if i <= 2 else ""
        print(f"| **{i}** | **{r['n']}**{star} | **{r['sc']:.1f}** | {x['LEGIBLE']} | {x['TRUE']} "
              f"| {x['FOUNDERGRADE']} | {x['FILL30']} | {x['ECON']} | {x['BUYER']} | {x['FIRST']} |")
    print("\n### Not at launch\n")
    print("| Seat | Score | Failed | Why |\n|---|---|---|---|")
    for r in DEAD:
        print(f"| {r['n']} | {r['sc']:.1f} | {', '.join(r['f'])} | {r['note']} |")

    print("\n---\n\n## 4. The top two, and the honest tension between them\n")
    a, b = LIVE[0], LIVE[1]
    print(f"**{a['n']} — {a['sc']:.1f}** vs **{b['n']} — {b['sc']:.1f}**. "
          f"{a['sc']-b['sc']:.1f} points apart, which is")
    print("inside the noise. They differ on exactly two axes, and the trade is clean:\n")
    print("| | Video editor → agencies | Bookkeeper → e-comm |\n|---|---|---|")
    for q, v, bk in [
        ("Ad legibility", "4 — *\"video editor\"* is clear", "**5 — the most legible role in the "
         "entire 179-role study**"),
        ("Is the claim true?", "**5 — 4-13x against a real invoice**", "4 — 3.75x, **but only "
         "against employers**"),
        ("**Can you grade it?**", "**5 — natively, month one**", "**2 — you need a hired CA**"),
        ("30-day economics", "4 — 3.26:1 at $15k", "**5 — 4.25:1 at $20k**"),
        ("Competitive whitespace", "**Nobody sells Indian editors to agencies**",
         "Somewhere, Oceans, Entigrity and a dozen more"),
        ("The pitch", "**Quality** — *\"from the industry that cuts Dune\"*",
         "**Price** — *\"yours costs $75k, ours is $20k\"*"),
    ]:
        print(f"| **{q}** | {v} | {bk} |")
    print("\n**Bookkeeper wins the ad. Video wins everything downstream of the click.**\n")
    print("And the deciding argument is the one the whole business turns on: "
          "[`scoring/LTGP.md`](scoring/LTGP.md) §3 says")
    print("**the deposit rate is the single fragile input** — the step where a stranger decides to "
          "trust you.")
    print("**A graded work sample you produced yourself, on their own material, is the strongest "
          "thing that can")
    print("happen at that step — and month one you can only produce it for video and paid media.**\n")

    print("---\n\n## 5. What to actually do\n")
    print("### Launch with ONE seat, not five\n")
    print("[`MAP.md`](MAP.md) specifies five sellable seats. **That is the right steady state and "
          "the wrong month one.**")
    print("Each seat needs its own bench, its own grading rubric, its own ad and its own intake "
          "script. With one")
    print("operator, **five seats is five half-built funnels.**\n")
    print("| When | Seat | Why then |\n|---|---|---|")
    for w2, s2, y2 in [
        ("**Month 1**", "**Video editor → marketing agencies**",
         "You can grade it, the claim is true against a real invoice, the buyer is FB 5 / IG 5, "
         "and nobody else sells it"),
        ("**Month 1, same spend**", "**Bookkeeper → e-comm, as the A/B**",
         "Best ad in the study and best economics. **Run both — the $1,500 test splits two ways "
         "at no extra cost**, and cost-per-held-call settles it in ten days"),
        ("**Month 3**", "AP or AR into existing clients",
         "Zero switch cost, same bench. This is what makes CAC efficient"),
        ("**Month 6**", "3D renders, or paid media ops",
         "Once there is a grading process that is not just you"),
        ("**Year 2**", "Construction estimating",
         "**The best business found.** It needs a hired domain lead first, which needs revenue"),
    ]:
        print(f"| {w2} | {s2} | {y2} |")

    print("\n### The order of the next three actions\n")
    print("| | Action | Cost |\n|---|---|---|")
    print("| **1** | **Count postings** — \"remote video editor\" vs \"remote bookkeeper\", both "
          "into the enrichment pipeline | Free, one afternoon |")
    print("| **2** | **Match-rate test** — 2,000 enriched companies → Meta Custom Audience → read "
          "matched size | ~$200, same day |")
    print("| **3** | **Split the $1,500** — two ad sets, two seats, one landing page each; measure "
          "**cost per held call** and count how many ask where the person is | ~$1,500, ten days |")
    print("\n**Everything above is a judgement. Those three steps cost under $2,000 and convert "
          "the top of this")
    print("table into fact.** The ranking exists to decide *what to test first*, not to be right.\n")

    print("---\n\n## 6. What this screen overturns, and what it leaves alone\n")
    print("| | |\n|---|---|")
    for a3, b3 in [
        ("**Leaves alone**", "[`MAP.md`](MAP.md)'s verticals — e-comm and marketing agencies are "
         "still the only two clearing FB **and** IG. Nothing here changes the audience"),
        ("**Leaves alone**", "The offer, the fee, the guarantee, the EOR attach. All unchanged"),
        ("**Sharpens**", "**Five seats becomes one seat plus an A/B.** Concentration is the "
         "month-one asset; breadth is a month-six asset"),
        ("**Overturns**", "**The launch seat.** MAP.md picked bookkeeper on ad legibility alone. "
         "Adding *can you grade it*, *is the claim true against a vendor*, and *is the category "
         "contested* promotes the video editor into a coin-flip with it — **and the coin-flip is "
         "cheap to resolve, so resolve it rather than argue it**"),
        ("**Flags**", "The bookkeeper claim is **0.4-1.1x against a bookkeeping firm**. If you "
         "launch it, the intent seed is not optional — it is the only audience the headline is "
         "true for"),
    ]:
        print(f"| {a3} | {b3} |")
    print()


if __name__ == "__main__":
    report()
