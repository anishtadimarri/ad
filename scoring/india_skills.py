#!/usr/bin/env python3
"""
Where is Indian talent WORLD-CLASS, not merely cheaper — screened for a D2C buyer.

Every earlier screen in this repo asked a demand-side question: what is placeable,
sellable, legible in an ad. This asks a supply-side quality question, and it
matters because it changes the pitch:

    "Your bookkeeper costs $75k, ours is $20k"   -> a PRICE pitch
    "Mumbai is the largest VFX hub on earth"     -> a QUALITY pitch

A quality pitch defends against both the price objection and the India objection
(COUNTRIES.md §9), which a price pitch invites.

THE CENTRAL FILTER, and the finding this screen produces:

    India is world-class at PRODUCTION and ANALYSIS.
    It is not world-class at JUDGEMENT about American consumers, or at VOICE.

So `CULTFREE` is a gate, not a score: if the work requires knowing what makes a
US consumer buy, or sounds like an American on a phone, no amount of skill
arbitrage fixes it.

Evidence tags per MASTER §0.  Run:  python3 scoring/india_skills.py > SKILLS-INDIA.md
"""

DIM = [
    ("WORLDCLASS", 22, "Is the TOP of the Indian distribution genuinely equal to or "
                       "better than the US equivalent? Evidence: export share, global "
                       "rank, awards, size of the trained cohort"),
    ("CULTFREE",   20, "**GATE.** Does the work need American consumer intuition, "
                       "idiom or taste? Production and analysis score high; judgement "
                       "and copy score low"),
    ("D2C",        16, "Centrality to a D2C brand's P&L"),
    ("VERIFY",     12, "**GATE.** Can we grade it on a work sample before placing?"),
    ("ASYNC",      10, "**GATE.** Works with no live overlap"),
    ("ARB",         8, "Salary arbitrage size"),
    ("SUPPLY",      7, "Depth of the Indian pool"),
    ("AIDUR",       5, "Durability against AI over 3-5 years"),
]
W = {k: w for k, w, _ in DIM}
GATES = [("CULTFREE", 3, "needs American consumer intuition — skill arbitrage cannot fix taste"),
         ("VERIFY", 3, "ungradeable, so quality cannot be promised"),
         ("ASYNC", 3, "needs live overlap, and IST is the worst overlap of any major pool")]

# name, scores, evidence, note
S = [
 ("Video ad editing & motion graphics",
  dict(WORLDCLASS=5, CULTFREE=4, D2C=5, VERIFY=5, ASYNC=5, ARB=4, SUPPLY=5, AIDUR=3),
  "**Mumbai is the largest VFX hub in the world by headcount** · **6 of the 10 "
  "fastest-growing VFX/animation hubs globally are Indian** · **70% of Indian VFX "
  "studio revenue is export** (Hollywood, Netflix, Amazon) · **DNEG has 8 Academy "
  "Awards for Best VFX since 2011** — Dune, Inception, Interstellar · more Indians "
  "work on VFX in Hollywood films than in Indian films [all V]",
  "**The strongest world-class claim available, and it happens to be the single "
  "largest recurring creative need of a D2C brand.** Editing to a brief is "
  "culture-free; choosing the *hook* is not — so place the editor, not the creative "
  "director"),

 ("Bookkeeping & e-comm accounting",
  dict(WORLDCLASS=5, CULTFREE=5, D2C=4, VERIFY=5, ASYNC=5, ARB=5, SUPPLY=5, AIDUR=3),
  "**528,000+ active chartered accountants** [V] · 30 years of US accounting "
  "outsourcing (Entigrity and the whole CPA-offshoring industry) · Somewhere's own "
  "published savings 75-78% [V]",
  "Fully rules-based, so `CULTFREE` is maximal — GAAP does not care who is reading "
  "it. **The current beachhead ([`MAP.md`](MAP.md)), and it wins on arbitrage rather "
  "than on being world-leading**"),

 ("Data & analytics — LTV, cohort, attribution",
  dict(WORLDCLASS=5, CULTFREE=5, D2C=4, VERIFY=5, ASYNC=5, ARB=4, SUPPLY=5, AIDUR=3),
  "Every Fortune 500 GCC in India trained this cohort; GCC attrition is at a historic "
  "low of ~12.6% [V]",
  "Numbers are numbers. **The most under-sold capability in the set** — a D2C founder "
  "who cannot see contribution margin by cohort is flying blind, and does not know "
  "they can hire for it at this price"),

 ("Amazon / marketplace operations",
  dict(WORLDCLASS=4, CULTFREE=4, D2C=5, VERIFY=5, ASYNC=5, ARB=4, SUPPLY=4, AIDUR=4),
  "India's own Amazon seller ecosystem is one of the largest in the world, with a "
  "whole domestic agency industry behind it [E]",
  "Listing mechanics, PPC structure, inventory health and case management are "
  "technical and verifiable. **US listing copy is not** — split the role"),

 ("Demand planning & inventory",
  dict(WORLDCLASS=4, CULTFREE=5, D2C=5, VERIFY=4, ASYNC=5, ARB=4, SUPPLY=4, AIDUR=4),
  "Deep industrial-engineering and supply-chain training base [E]",
  "**Inventory is the number one cash killer in D2C** and almost nobody offers this "
  "seat offshore. Fully culture-free — a stockout is a stockout in any country"),

 ("3D product visualisation / CGI product shots",
  dict(WORLDCLASS=5, CULTFREE=4, D2C=4, VERIFY=5, ASYNC=5, ARB=5, SUPPLY=4, AIDUR=2),
  "Same trained cohort as the VFX industry above [V]",
  "Replaces a physical photoshoot with a render. World-class supply, real D2C need — "
  "and the AI-generation risk is the highest in the set"),

 ("Performance marketing — technical media buying",
  dict(WORLDCLASS=4, CULTFREE=3, D2C=5, VERIFY=4, ASYNC=4, ARB=4, SUPPLY=5, AIDUR=3),
  "**India's own D2C e-commerce market is $108.76B in 2026, heading to $322.1B by "
  "2031 at 24.3% CAGR** [V] — so there is a large native cohort that has actually run "
  "paid acquisition on thin margins, not merely studied it",
  "**The split matters more here than anywhere.** Account structure, feed management, "
  "bid strategy, tracking and QA are world-class and culture-free. **Creative "
  "strategy, hooks and offer angles are culture-bound and score 1.** This is the "
  "founder's own skill, so it is also the one role he can grade personally "
  "([`MASTER.md`](MASTER.md) §7.6)"),

 ("Shopify build & CRO implementation",
  dict(WORLDCLASS=4, CULTFREE=4, D2C=4, VERIFY=5, ASYNC=5, ARB=4, SUPPLY=5, AIDUR=3),
  "Enormous and commoditised Indian web-development base [E]",
  "*Implementing* a test is culture-free; *deciding what to test* is not"),

 ("Process documentation & SOP building",
  dict(WORLDCLASS=5, CULTFREE=5, D2C=3, VERIFY=4, ASYNC=5, ARB=4, SUPPLY=5, AIDUR=3),
  "The IT-services industry (TCS, Infosys, Wipro) built genuinely world-class process "
  "discipline — CMMI-level delivery method as a national competence [E]",
  "**The most overlooked item here.** A $10M D2C brand is usually held together by "
  "the founder's memory. India is world-class at turning that into documented process, "
  "and nobody sells it as a seat"),

 ("Graphic design — static ads & versioning",
  dict(WORLDCLASS=3, CULTFREE=3, D2C=4, VERIFY=5, ASYNC=5, ARB=4, SUPPLY=5, AIDUR=2),
  "Large pool; the top end is globally contested [E]",
  "Versioning and resizing at volume is production work and works well. Original "
  "brand taste is culture-bound and the AI risk is severe"),

 ("Customer support — chat, email, tickets",
  dict(WORLDCLASS=4, CULTFREE=3, D2C=3, VERIFY=4, ASYNC=4, ARB=5, SUPPLY=5, AIDUR=1),
  "Two decades of BPO heritage [V]",
  "Works today. **`AIDUR`=1 — tier-one support is the single most AI-exposed function "
  "in this table**, so it is a declining asset to build a company on"),

 # ---- the honest exclusions
 ("Copywriting for US consumers",
  dict(WORLDCLASS=2, CULTFREE=1, D2C=5, VERIFY=4, ASYNC=5, ARB=4, SUPPLY=4, AIDUR=2),
  "No evidence of world-class capability; the arbitrage is real but the output is not",
  "**The clearest exclusion in the screen.** Selling to a US consumer in their own "
  "idiom is exactly the thing 15 years of practice in another market does not buy. "
  "Do not place it, and do not let a media buyer quietly own it"),

 ("Email / SMS retention copy & flows",
  dict(WORLDCLASS=3, CULTFREE=2, D2C=4, VERIFY=4, ASYNC=5, ARB=4, SUPPLY=4, AIDUR=2),
  "Klaviyo mechanics are learnable; the words are the product",
  "The *flow architecture* is technical and placeable. The *copy inside it* is the "
  "same failure as above, and it is 30% of D2C revenue — so splitting this seat is "
  "not optional"),

 ("Influencer / UGC sourcing",
  dict(WORLDCLASS=2, CULTFREE=1, D2C=4, VERIFY=3, ASYNC=4, ARB=4, SUPPLY=3, AIDUR=3),
  "Requires live knowledge of the US creator landscape",
  "Needs taste in a market you do not live in"),

 ("Customer support — voice / phone",
  dict(WORLDCLASS=3, CULTFREE=2, D2C=3, VERIFY=4, ASYNC=1, ARB=5, SUPPLY=5, AIDUR=1),
  "The 25-year consumer association that drives the India objection "
  "([`COUNTRIES.md`](COUNTRIES.md) §9)",
  "Fails on accent, on live overlap and on AI simultaneously. **This is the role the "
  "India objection is actually about** — which is why placing it would confirm the "
  "stereotype the rest of the offer has to overcome"),
]


def sc(x):
    return sum(x[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def fails(x):
    return [f"{k}={x[k]}" for k, mn, _ in GATES if x[k] < mn]


R = [dict(n=n, x=x, ev=e, note=t, sc=sc(x), f=fails(x)) for n, x, e, t in S]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])


def report():
    print("# WORLD-CLASS INDIAN SKILLS FOR A D2C BUYER\n")
    print(f"**{len(R)} skills scored on {len(DIM)} weighted dimensions plus {len(GATES)} gates.** "
          f"Generated by")
    print("[`scoring/india_skills.py`](scoring/india_skills.py). Evidence tags per "
          "[`MASTER.md`](MASTER.md) §0.\n")
    print("> **This screen asks a different question from every other one in the repo.** The rest "
          "ask what is\n> *placeable and sellable* — demand-side. This asks **where Indian talent "
          "is genuinely world-class\n> rather than merely cheaper** — supply-side quality. It "
          "matters because it changes the pitch:\n>\n> | | |\n> |---|---|\n> | *\"Your bookkeeper "
          "costs \\$75k, ours is \\$20k\"* | a **price** pitch — invites the price objection and "
          "the India objection |\n> | *\"Mumbai is the largest VFX hub on earth\"* | a **quality** "
          "pitch — answers both |\n")

    print("---\n\n## 1. The finding, before the table\n")
    print("### India is world-class at PRODUCTION and ANALYSIS.")
    print("### It is not world-class at JUDGEMENT about American consumers, or at VOICE.\n")
    print("That single distinction sorts this entire list, and it cuts *through* roles rather than "
          "between")
    print("them — which is why the answer is not \"hire a marketer\" but **\"split the marketer.\"**\n")
    print("| Same function, split | Placeable in India | Keep in the US |")
    print("|---|---|---|")
    for a, b, c in [
        ("Paid media", "Account structure · feeds · bid strategy · tracking · QA · reporting",
         "**Hooks, angles, offer** — what makes a US consumer stop scrolling"),
        ("Creative", "Editing · motion graphics · versioning · 3D renders",
         "**The concept** and which hook to test"),
        ("Retention", "Klaviyo flow architecture · segmentation · deliverability",
         "**The words in the email** — 30% of D2C revenue"),
        ("Marketplace", "Listing mechanics · PPC · inventory health · case management",
         "**US listing copy**"),
        ("CRO", "Building and shipping the test", "**Deciding what to test**"),
    ]:
        print(f"| **{a}** | {b} | {c} |")
    print("\n**A seat defined as \"production and analysis\" is world-class and gradeable. The same "
          "seat defined")
    print("as \"own the channel\" fails on taste, and the failure gets blamed on the country.**\n")

    print("---\n\n## 2. The criteria\n")
    print("| Dimension | Weight | What it measures |\n|---|---|---|")
    for k, w, d in DIM:
        print(f"| **{k}** | {w} | {d} |")
    print("\n| Gate | Fails below | Why |\n|---|---|---|")
    for k, mn, why in GATES:
        print(f"| **{k}** | {mn} | {why} |")

    print("\n---\n\n## 3. The ranking\n")
    print("| # | Skill | Score | WC | CF | D2C | VER | ARB | AI |")
    print("|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        x = r["x"]; star = " ⭐" if i <= 4 else ""
        print(f"| {i} | **{r['n']}**{star} | **{r['sc']:.1f}** | {x['WORLDCLASS']} "
              f"| {x['CULTFREE']} | {x['D2C']} | {x['VERIFY']} | {x['ARB']} | {x['AIDUR']} |")

    print("\n### Gated out\n")
    print("| Skill | Score before gate | Failed | Why it matters |\n|---|---|---|---|")
    for r in DEAD:
        print(f"| **{r['n']}** | {r['sc']:.1f} | {', '.join(r['f'])} | {r['note']} |")

    print("\n---\n\n## 4. The top four, with the evidence\n")
    for i, r in enumerate(LIVE[:4], 1):
        print(f"### {i}. {r['n']} — {r['sc']:.1f}\n")
        print(f"{r['ev']}\n")
        print(f"**{r['note']}.**\n")

    print("---\n\n## 5. Bookkeeping wins by 2.4 points, which is noise — and the two win differently\n")
    bk  = next(r for r in LIVE if r["n"].startswith("Bookkeeping"))
    vid = next(r for r in LIVE if r["n"].startswith("Video"))
    print(f"| | Bookkeeping — {bk['sc']:.1f} | Video editing — {vid['sc']:.1f} |\n|---|---|---|")
    for a, b, c in [
        ("Why it scores", "**Arbitrage.** 5 on `ARB`, 5 on `CULTFREE` — GAAP does not care who reads it",
         "**World leadership.** 5 on `D2C` — it is the largest recurring creative need a D2C brand has"),
        ("Strength of the world-class claim",
         "`[V]` — 528,000 CAs, 30 years of US outsourcing",
         "`[V]` and stronger — **largest hub on earth, 8 Academy Awards, 70% export**"),
        ("What the pitch becomes", "*\"Cheaper than your $75k hire\"* — a **price** claim",
         "*\"From the industry that cuts Dune\"* — a **quality** claim"),
        ("Who else offers it", "Somewhere, Oceans, Entigrity, and a dozen more",
         "**Nobody in this category sells an Indian video editor to a D2C brand**"),
        ("AI exposure", "3 — ledger automation is real but slow", "3 — AI video is moving fast"),
    ]:
        print(f"| **{a}** | {b} | {c} |")
    print("\n**2.4 points is inside this model's noise, so read them as tied and pick on kind, not "
          "rank.** And")
    print("they are not competitors — [`MAP.md`](MAP.md) already separates the *advertised* role from "
          "the *placed*")
    print("seat. What this screen changes is the **second** seat:\n")
    print("| | [`MAP.md`](MAP.md)'s answer | What this screen suggests |\n|---|---|---|")
    print("| **Ad-facing role** | \"Bookkeeper\" — 96.0 Meta-sellability, the most legible role in "
          "English | *unchanged* |")
    print("| **Second seat into the same client** | AP or AR — 0-0.5 week switch cost | **Video "
          "editor** — because it is the seat where the pitch stops being about price, and the "
          "client already trusts you by then |")
    print("\n**And it produces one offer line no competitor can say, both halves verifiable:**\n")
    print("> *\"The people who cut your ads come from the industry that cuts Dune. Mumbai is the "
          "largest\n> visual-effects hub in the world by headcount, and 70% of what it makes is "
          "exported.\"*\n")
    print("Compare that with *\"our bookkeeper is $20k.\"* Same company — and only one of the two "
          "makes the buyer")
    print("want the **better** thing rather than the **cheaper** thing. That distinction is worth "
          "more than 2.4")
    print("points, because it is the only defence found so far against both the price objection and "
          "the India")
    print("objection ([`COUNTRIES.md`](COUNTRIES.md) §9) at the same time.\n")
    print("---\n\n## 6. The three no-go seats, and why they are the expensive mistakes\n")
    print("| Never place | The trap |\n|---|---|")
    print("| **US consumer copywriting** | It is the one skill that *looks* like production and is "
          "actually judgement. It will be graded by the client as a country failure, not a role "
          "failure |")
    print("| **Voice support** | Fails accent, live overlap and AI at once — and **it is the exact "
          "role the India objection is about**, so placing it confirms the stereotype the rest of "
          "the offer exists to overcome |")
    print("| **Anything sold as \"own the channel\"** | Ownership implies judgement. Sell "
          "*execution against a brief* and the same person succeeds |")
    print("\n**The honest limit of this screen:** `WORLDCLASS` is `[V]` for VFX/animation and for "
          "accounting, and")
    print("`[E]` everywhere else — the export-share and award evidence simply does not exist for "
          "demand planning")
    print("or SOP building the way it does for visual effects. `CULTFREE` is a judgement "
          "throughout. **The")
    print("cheap test is the same graded work sample already in the plan, run once per skill.**\n")


if __name__ == "__main__":
    report()
