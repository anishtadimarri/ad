#!/usr/bin/env python3
"""
THE COMPOUNDING SCREEN — what can we sell to the SAME few ICPs for 24 months?

This corrects LAUNCH.md, which optimised for month one and scored nothing about
whether the choice builds an asset. Operator direction: align with the top ICPs,
and pick something we can run for two years so it compounds.

That is a different objective, and it changes the answer.

THE CENTRAL IDEA: what compounds is not the SKILL, it is the SPINE.

A spine is a shared system of record between us and the client — the ledger
(QuickBooks / Xero) or the ad platform (Meta Ads Manager / GA4). A spine is what
lets ONE graded bench serve MANY clients and MANY roles, because the work is the
same everywhere and the next seat plugs into the same place.

    Ledger spine  -> bookkeeper, accountant, AR, AP, controller.
                     Shared login. We can see the work. The next seat is obvious.
    Video         -> Premiere and After Effects are TOOLS, not a shared system of
                     record. A rendered file is handed over a wall. Nothing
                     accumulates between us and the client except invoices.

That distinction is why the finance spine compounds and video does not, and it is
the thing LAUNCH.md missed.

Evidence tags per MASTER §0.  Run:  python3 scoring/compound.py > COMPOUND.md
"""

DIM = [
    ("AIDUR24",  22, "**GATE.** Will this seat still exist in 24 months? A skill with a "
                     "3-5 year horizon cannot be the thing you compound on"),
    ("ONEBENCH", 20, "Does **one graded bench** serve all the target ICPs, or does each "
                     "ICP need its own pool?"),
    ("LADDER",   16, "Is there a **career ladder** — can the same client buy a more "
                     "expensive version later, and the same person be promoted into it?"),
    ("SEATS",    14, "Can we sell a **2nd, 3rd, 4th seat** into the same client?"),
    ("SPINE",    12, "Is there a **shared system of record** with the client, or is the "
                     "work handed over a wall?"),
    ("EORFIT",    8, "Does the seat support the **EOR attach** — the recurring stock that "
                     "is 37-65% of lifetime GP?"),
    ("PROOF",     8, "Do case studies **transfer** to the next buyer in the same ICP?"),
]
W = {k: w for k, w, _ in DIM}
GATES = [("AIDUR24", 3, "will not survive the horizon we are compounding over"),
         ("ONEBENCH", 3, "a separate bench per ICP is a separate company per ICP")]

# The ICP set this must serve. MAP.md's two clear FB+IG; PI law is the deferred third.
ICP = [("E-commerce / DTC", "~21,000 in band · FB 5 / IG 5 · QuickBooks / Xero + A2X"),
       ("Marketing agencies", "~30,000 in band · FB 5 / IG 5 · QuickBooks / Xero + Harvest"),
       ("PI law firms *(deferred third)*",
        "Richest buyer, `AFFORD`=5 · FB 4 / IG 2 · QuickBooks / Xero + Clio")]

S = [
 ("Finance spine — bookkeeper → accountant → AR/AP → controller",
  dict(AIDUR24=4, ONEBENCH=5, LADDER=5, SEATS=5, SPINE=5, EORFIT=5, PROOF=5),
  "**Every one of the three ICPs runs QuickBooks or Xero** [V] · MAP.md already "
  "documents the tier-up: bookkeeper $20k → accountant $31k, **a 41% higher fee on "
  "the same ad** [V] · AP and AR are **0-0.5 week switch cost** from the same bench [V] "
  "· 528,000+ Indian CAs [V]",
  "**The only candidate that scores 5 on five dimensions.** One bench, one spine, a "
  "real ladder, obvious second seats, and the client gives us a login — so we can see "
  "the work, spot the next gap, and refill a seat without renegotiating. **Ledger "
  "automation is real but slow; a bookkeeper placed today is a decade-long asset**"),

 ("Data & analytics — LTV, cohort, margin reporting",
  dict(AIDUR24=4, ONEBENCH=4, LADDER=4, SEATS=3, SPINE=4, EORFIT=5, PROOF=4),
  "GCC-trained cohort, attrition ~12.6% [V] · sits on the same ledger plus GA4",
  "**The natural senior end of the finance spine**, which is why it compounds well "
  "even though it launches badly (gated on legibility in LAUNCH.md). Reporting is a "
  "ladder step above the controller, not a separate business"),

 ("Paid media operations",
  dict(AIDUR24=3, ONEBENCH=4, LADDER=3, SEATS=3, SPINE=4, EORFIT=4, PROOF=4),
  "Ad-platform spine — Meta Ads Manager and GA4 [V] · the operator's own trade",
  "**A genuine second spine**, and the only other one in the study. Weaker ladder, "
  "and Advantage+ is automating the technical half of the job, which is exactly the "
  "half we place"),

 ("Video editing & motion graphics",
  dict(AIDUR24=2, ONEBENCH=4, LADDER=2, SEATS=2, SPINE=1, EORFIT=4, PROOF=4),
  "**Strongest world-class evidence in the repo** [V] · **4.0x-13.2x against the "
  "vendor invoice, the largest true claim found** [V] · and `AIDUR`=2: generative "
  "video is the fastest-moving AI risk in the study",
  "**LAUNCH.md's #1, and it fails this screen.** No shared system of record — a "
  "rendered file is handed over a wall, so nothing accumulates. Thin ladder (editor → "
  "senior editor), weak second seat, and a 3-5 year horizon against a 24-month "
  "compounding requirement. **A great first sale and a poor foundation**"),

 ("3D / product & architectural visualisation",
  dict(AIDUR24=2, ONEBENCH=3, LADDER=2, SEATS=2, SPINE=1, EORFIT=4, PROOF=4),
  "Same VFX cohort [V] · highest AI-generation exposure in the set",
  "Same structural problem as video, with a narrower buyer"),

 ("Construction estimating & takeoffs",
  dict(AIDUR24=4, ONEBENCH=2, LADDER=4, SEATS=3, SPINE=4, EORFIT=5, PROOF=5),
  "**#1 on the bottleneck screen at 94.8** [V] · Procore is a real spine [E]",
  "**Compounds beautifully and serves none of our ICPs.** A separate bench, a "
  "separate ad, a separate grading capability. `ONEBENCH`=2 is the whole story: this "
  "is a second company, and the right time for it is after the first one works"),

 ("PI medical record review",
  dict(AIDUR24=3, ONEBENCH=2, LADDER=3, SEATS=3, SPINE=4, EORFIT=5, PROOF=5),
  "Clio is a real spine [E] · richest buyer in the set [V]",
  "Serves ICP three only, and needs its own bench and its own domain grading. **The "
  "finance spine reaches the same law firms — every PI firm also has books**"),

 ("Customer support — chat & tickets",
  dict(AIDUR24=1, ONEBENCH=5, LADDER=2, SEATS=4, SPINE=3, EORFIT=4, PROOF=3),
  "Two decades of BPO precedent [V] · **`AIDUR`=1, the most AI-exposed function in "
  "the study** [E]",
  "One bench serves everyone, and the seat is being deleted. **Compounding on a "
  "shrinking function is the worst possible foundation**"),

 ("AI workflow & automation operations",
  dict(AIDUR24=5, ONEBENCH=4, LADDER=4, SEATS=4, SPINE=3, EORFIT=4, PROOF=3),
  "**AI Engineer was LinkedIn's #1 fastest-growing US title, +143% YoY** [V] · AI "
  "skills in 2.5% of all US postings, +297% in a decade [V]",
  "**The highest `AIDUR24` in the table by definition** — it is the only seat that "
  "gets *larger* as AI improves. Gated out of launch on legibility, and the right "
  "answer is to hold it as the **month-18 expansion**, by which point SMBs will be "
  "searching for it by name"),
]


def sc(x):
    return sum(x[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def fails(x):
    return [f"{k}={x[k]}" for k, mn, _ in GATES if x[k] < mn]


R = [dict(n=n, x=x, ev=e, note=t, sc=sc(x), f=fails(x)) for n, x, e, t in S]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])


def report():
    print("# THE COMPOUNDING SCREEN — What To Run For Two Years\n")
    print("**This corrects [`LAUNCH.md`](LAUNCH.md).** That screen optimised for month one — can "
          "you grade it, can")
    print("you fill it in thirty days — and **scored nothing about whether the choice builds an "
          "asset.** With a")
    print("24-month compounding requirement the objective changes, and so does the answer.\n")
    print("Generated by [`scoring/compound.py`](scoring/compound.py).\n")

    print("---\n\n## 1. The idea: what compounds is the SPINE, not the skill\n")
    print("A **spine** is a shared system of record between us and the client. It is what lets "
          "**one graded bench")
    print("serve many clients and many roles**, because the work is the same everywhere and the "
          "next seat plugs")
    print("into the same place.\n")
    print("| | Ledger spine | Video |\n|---|---|---|")
    for a, b, c in [
        ("What it is", "**QuickBooks / Xero** — a shared login", "Premiere and After Effects — "
         "*tools*, not a shared record"),
        ("Can we see the work?", "✅ **Yes, continuously**", "❌ Only the file they receive"),
        ("Does the next seat suggest itself?", "✅ We can see the gap — unreconciled AP, ageing AR",
         "❌ We would have to ask"),
        ("What accumulates between us?", "**Access, history, visibility, switching cost**",
         "Invoices"),
        ("Refilling a seat", "Operational — the replacement logs into the same place",
         "A renegotiation"),
    ]:
        print(f"| **{a}** | {b} | {c} |")
    print("\n**A rendered file is handed over a wall. A ledger login is a position inside the "
          "business.** That is the")
    print("difference between a sale and a foothold, and it is what [`LAUNCH.md`](LAUNCH.md) "
          "missed.\n")

    print("---\n\n## 2. The ICPs this has to serve\n")
    print("| ICP | Why it is in the set |\n|---|---|")
    for a, b in ICP:
        print(f"| **{a}** | {b} |")
    print("\n> **Note what the third column shows: all three run QuickBooks or Xero.** The ledger "
          "is the only\n> thing the three ICPs have in common — so it is the only spine that "
          "serves all of them. Video\n> serves two of the three, and construction estimating "
          "serves none.\n")

    print("---\n\n## 3. The criteria\n")
    print("| Dimension | Weight | What it measures |\n|---|---|---|")
    for k, w, d in DIM:
        print(f"| **{k}** | {w} | {d} |")
    print("\n| Gate | Fails below | Why |\n|---|---|---|")
    for k, mn, why in GATES:
        print(f"| **{k}** | {mn} | {why} |")

    print("\n---\n\n## 4. THE RANKING\n")
    print("| # | Seat / spine | Score | AI24 | BENCH | LADR | SEATS | SPINE | EOR | PROOF |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        x = r["x"]; star = " ⭐" if i == 1 else ""
        print(f"| **{i}** | **{r['n']}**{star} | **{r['sc']:.1f}** | {x['AIDUR24']} "
              f"| {x['ONEBENCH']} | {x['LADDER']} | {x['SEATS']} | {x['SPINE']} | {x['EORFIT']} "
              f"| {x['PROOF']} |")
    print("\n### Does not compound\n")
    print("| Seat | Score | Failed | Why |\n|---|---|---|---|")
    for r in DEAD:
        print(f"| {r['n']} | {r['sc']:.1f} | {', '.join(r['f'])} | {r['note']} |")

    print("\n---\n\n## 5. The correction to LAUNCH.md\n")
    fin = next(r for r in R if r["n"].startswith("Finance"))
    vid = next(r for r in R if r["n"].startswith("Video"))
    print(f"| | Video editor | Finance spine |\n|---|---|---|")
    for q, v, f in [
        ("**[`LAUNCH.md`](LAUNCH.md) rank**", "**1st — 91.6**", "2nd — 86.8"),
        ("**This screen**", f"**{[r['n'] for r in LIVE].index(vid['n'])+1 if vid in LIVE else 'GATED'}"
         f"** — {vid['sc']:.1f}", f"**1st — {fin['sc']:.1f}**"),
        ("Serves how many of the three ICPs?", "2 of 3", "**3 of 3**"),
        ("Shared system of record", "❌ none", "✅ **the ledger**"),
        ("Career ladder", "editor → senior editor", "**bookkeeper → accountant → controller → "
         "reporting.** MAP.md already prices the first step at **+41% fee on the same ad**"),
        ("Still exists in 24 months?", "⚠️ **`AIDUR`=2 — the fastest-moving AI risk in the study**",
         "✅ ledger automation is real and slow"),
        ("Second seat into the same client", "Weak", "**AP and AR at 0-0.5 week switch cost**"),
    ]:
        print(f"| {q} | {v} | {f} |")
    print(f"\n**I got this wrong, and the reason is worth naming: I scored *launchability* and "
          f"called it the")
    print("answer.** Video is genuinely the better *first sale* — bigger true claim, gradeable by "
          "you, "
          "uncontested,")
    print("a better story. **It is a poor foundation**, because nothing accumulates between you "
          "and the client and")
    print("the seat has a 3-5 year horizon against a 24-month requirement.\n")
    print("> **Video is a customer-acquisition asset. The ledger is the compounding asset.** Those "
          "are different\n> jobs, and the mistake was asking one seat to do both.\n")

    print("---\n\n## 6. So: the plan that satisfies both\n")
    print("**Finance spine is the two-year business. Video is the way in.** They are not "
          "competing — video is the")
    print("cheapest known route to a first conversation with an agency owner, and the ledger is "
          "what you sell them")
    print("second and keep selling for two years.\n")
    print("| Phase | Sell | Into | Why then |\n|---|---|---|---|")
    for p, s2, i2, w2 in [
        ("**Month 1-2**", "**Bookkeeper** (ad-facing), scope the seat on the call",
         "E-comm + agencies",
         "96.0 Meta-sellability, best 30-day economics, and it puts you on the spine from the "
         "first placement. **Pay one Indian CA a few hundred dollars to grade work samples** — "
         "that is the whole fix for the one thing you cannot judge"),
        ("**Month 1-2, same $1,500**", "**Video editor** as the A/B ad",
         "Marketing agencies",
         "Biggest true claim, you can grade it yourself, and it is the cheapest way to find out "
         "whether a quality pitch beats a price pitch. **Run it as an acquisition test, not as the "
         "foundation**"),
        ("**Month 3-6**", "**AP, then AR**", "Existing clients",
         "0-0.5 week switch cost, same bench, same login. This is where seats-per-client — and "
         "therefore CAC efficiency — actually moves"),
        ("**Month 6-12**", "**Accountant / full close**", "Existing + new",
         "**+41% fee on the same ad**, and the same bench member can be promoted into it. The "
         "ladder is the compounding"),
        ("**Month 12-18**", "**Controller and margin reporting**", "The best existing clients",
         "The senior end of the spine. Highest fee, deepest lock-in, and by now there is outcome "
         "data to sell it with"),
        ("**Month 18-24**", "**AI workflow ops**", "Same ICPs",
         "**Highest `AIDUR24` in the table** — the only seat that grows as AI improves. Gated out "
         "today on legibility, and in 18 months SMBs will search for it by name"),
    ]:
        print(f"| {p} | {s2} | {i2} | {w2} |")

    print("\n### What this makes the company, in one line\n")
    print("> **The offshore finance department for e-commerce brands and marketing agencies** — "
          "one bench on\n> one ledger spine, sold five ways up a ladder, with EOR underneath it.\n")
    print("That sentence survives two years. *\"We place video editors\"* does not, because in "
          "two years the")
    print("editors may be software — and even if they are not, **you would have spent two years "
          "handing files")
    print("over a wall instead of building a position inside 200 businesses.**\n")
    print("**Honest limits:** `AIDUR24` is `[E]` for every row — nobody knows the AI curve, and "
          "the video score of")
    print("2 is a judgement that could be wrong in either direction. `ONEBENCH`, `LADDER` and "
          "`SPINE` are")
    print("structural and defensible. **Nothing here is a reason to skip the ten calls** — the "
          "compounding")
    print("argument decides what to *build*, and the funnel test still decides whether anyone "
          "buys.\n")


if __name__ == "__main__":
    report()
