#!/usr/bin/env python3
"""
HUNGRY BUYERS — where a world-class Indian seat is a REVENUE bottleneck, not a cost line.

The distinction this screen is built on, and the reason it produces different
answers from every other screen in the repo:

    A COST-CENTRE buyer negotiates price.   "How much cheaper?"
    A BOTTLENECK buyer asks how fast.       "When can they start?"

Bookkeeping is a cost centre. The buyer's felt problem is that it costs too much,
so the pitch is arbitrage and the conversation is about price. That is a fine
business and it is what MAP.md sells.

But where the same seat sits on a REVENUE constraint — where more of it means more
money, not less spend — the buyer stops negotiating. That is what "hungry" means,
and it is measurable: ask whether the absence of the seat caps the top line.

Supply premise comes from SKILLS-INDIA.md: place PRODUCTION and ANALYSIS, never
JUDGEMENT about American consumers, and never VOICE.

Evidence tags per MASTER §0.  Run:  python3 scoring/hungry.py > HUNGRY.md
"""

DIM = [
    ("BOTTLENECK", 24, "**GATE.** Does the absence of this seat cap REVENUE? If more of "
                       "it means more money rather than less spend, the buyer stops "
                       "negotiating price"),
    ("NOHIRE",     18, "Can they hire it locally at any price? A structural shortage is "
                       "what converts interest into urgency"),
    ("WORLDCLASS", 14, "**GATE.** Is India genuinely world-class at it (SKILLS-INDIA.md), "
                       "not merely cheaper?"),
    ("OWNER",      12, "Owner-led, decides same day, no procurement committee"),
    ("PRECEDENT",  10, "Is offshoring THIS work already normal here? The difference "
                       "between selling and evangelising"),
    ("META",       10, "**GATE.** Reachable on Facebook and Instagram — the only channel "
                       "in the plan"),
    ("AFFORD",      7, "Can they pay a $6-15k placement fee without flinching?"),
    ("WHITE",       5, "Uncontested, or already owned by a 10,000-person incumbent?"),
]
W = {k: w for k, w, _ in DIM}
GATES = [("BOTTLENECK", 4, "a cost centre, so the buyer negotiates instead of buying"),
         ("WORLDCLASS", 3, "India is not world-class at it, so the pitch reverts to price"),
         ("META", 3, "unreachable on the only channel in the plan")]

# industry × bottleneck seat
H = [
 ("Specialty trade contractors", "Estimating & quantity takeoffs",
  dict(BOTTLENECK=5, NOHIRE=5, WORLDCLASS=4, OWNER=5, PRECEDENT=5, META=5, AFFORD=4, WHITE=4),
  "*\"When estimating capacity is thin, the company is **structurally limited in how "
  "much work it can chase**, and that ceiling is invisible until someone counts the "
  "invitations that got declined\"* [V] · *\"estimating talent remains scarce and "
  "expensive\"* [V] · a US-to-India virtual-estimator industry already exists [V]",
  "**The cleanest bottleneck found.** Every declined bid invitation is revenue that "
  "never existed, and the contractor can name the number. Also the **best Facebook "
  "buyer in the entire study** — MAP.md scored home services 89.2 on Meta workability"),

 ("Personal injury law firms", "Medical record review, chronologies & demand packages",
  dict(BOTTLENECK=5, NOHIRE=4, WORLDCLASS=4, OWNER=5, PRECEDENT=5, META=4, AFFORD=5, WHITE=3),
  "*\"Law firms experience backlogs due to manual document review\"* · outsourcing "
  "chronology, summary and billing review is *\"particularly common in high-volume "
  "personal injury and mass tort practices\"* · providers support firms handling "
  "*\"hundreds of cases a week\"* [all V] · Indian LPOs (Neural IT, HazenTech) already "
  "sell exactly this [V]",
  "**The demand package *is* the settlement.** A case sitting in a records backlog is "
  "capital parked, and the firm knows the per-case value precisely. **Richest buyer in "
  "MAP.md's whole set** (`AFFORD`=5) and owner-led. Weakness: Instagram — PI is FB 4 / IG 2"),

 ("Architecture & interior design firms", "Architectural visualisation — 3D renders, walkthroughs",
  dict(BOTTLENECK=5, NOHIRE=4, WORLDCLASS=5, OWNER=5, PRECEDENT=5, META=4, AFFORD=3, WHITE=3),
  "Same trained cohort as the VFX industry: **Mumbai is the largest VFX hub on earth "
  "by headcount, 70% of Indian VFX revenue is export, DNEG holds 8 Academy Awards** "
  "[V] · mature Indian archviz industry [E]",
  "**The render wins the pitch.** Visualisation is not overhead for an architecture "
  "practice — it is the sales asset, so capacity converts directly into won work. "
  "`AFFORD`=3 is the limit: small practices are not rich"),

 ("Marketing agencies & video production", "Video editing & motion graphics at volume",
  dict(BOTTLENECK=5, NOHIRE=3, WORLDCLASS=5, OWNER=5, PRECEDENT=5, META=5, AFFORD=4, WHITE=3),
  "Strongest world-class evidence in the study [V] · **agency owners score FB 5 / IG 5 "
  "— one of only two verticals clearing both** (MAP.md §5C)",
  "For an agency, production capacity **is** the deliverable and the margin. Already "
  "vertical two in [`MAP.md`](MAP.md), so this needs no new outbound motion — it "
  "changes which *seat* is sold, not who is targeted"),

 ("New-build developers & luxury brokerages", "Renders, virtual staging, listing video",
  dict(BOTTLENECK=5, NOHIRE=3, WORLDCLASS=5, OWNER=5, PRECEDENT=5, META=5, AFFORD=4, WHITE=2),
  "Same VFX cohort [V] · real-estate photo editing is already offshored at scale [E]",
  "Pre-sale renders move units, and realtors are the most Meta-native buyers alive. "
  "**But `WHITE`=2 — this is already a commoditised offshore category**, so we would "
  "arrive as the twentieth vendor"),

 ("Creator, podcast & YouTube businesses", "Long-form and short-form video editing",
  dict(BOTTLENECK=5, NOHIRE=3, WORLDCLASS=5, OWNER=5, PRECEDENT=4, META=4, AFFORD=3, WHITE=4),
  "Same VFX cohort [V]",
  "Publishing cadence is the entire growth model, and editing is the constraint on "
  "cadence. Owner-led to the point of being one person. `AFFORD`=3 — they pay per "
  "video, not per hire, so the fee model has to change"),

 ("Small & mid CPA firms", "Tax prep, workpapers & audit support",
  dict(BOTTLENECK=5, NOHIRE=5, WORLDCLASS=5, OWNER=5, PRECEDENT=5, META=3, AFFORD=4, WHITE=1),
  "**340,000 accountants left the profession in five years, a 17% decline** · "
  "**recruiting difficulty the highest in the study's 15-year history** · undergraduate "
  "accounting enrolment down 9.4% in two years [all V] · **528,000+ Indian CAs** [V]",
  "**The textbook hungry buyer: busy season is a hard ceiling on billable revenue**, "
  "and it arrives on a known date. But `WHITE`=1 — **Entigrity and a dozen others "
  "already are this business**, at scale, with a decade of case studies"),

 ("Medical & dental practices", "RCM — coding, prior auth, denial follow-up",
  dict(BOTTLENECK=5, NOHIRE=4, WORLDCLASS=5, OWNER=5, PRECEDENT=5, META=4, AFFORD=4, WHITE=1),
  "Indian RCM is a multi-billion-dollar export industry [V]",
  "**A denied claim is revenue already earned and not collected** — the purest "
  "bottleneck economics in the table. And `WHITE`=1: this is the most contested "
  "offshore category in existence, plus HIPAA"),

 ("Insurance agencies", "Policy servicing, COIs, endorsements, renewals",
  dict(BOTTLENECK=4, NOHIRE=5, WORLDCLASS=4, OWNER=5, PRECEDENT=5, META=3, AFFORD=4, WHITE=2),
  "**~400,000 workers lost to attrition by 2026 · 1.4M retirements · only 4% of "
  "millennials would consider an insurance career** [all V] · ReSource Pro runs "
  "~10,000 employees on exactly this [V]",
  "The **worst talent shortage of any offshorable US occupation** ([`PATTERN.md`](PATTERN.md) "
  "§3). Servicing capacity caps book growth. Fails on channel: **FB 4 / IG 1**, and "
  "ReSource Pro owns the category"),

 ("Freight brokerages", "Carrier vetting, track-and-trace, settlements",
  dict(BOTTLENECK=4, NOHIRE=4, WORLDCLASS=4, OWNER=5, PRECEDENT=5, META=4, AFFORD=3, WHITE=3),
  "Third on TARGETING's intent-flow screen [E]",
  "Load coverage is revenue, so capacity is a real constraint — but margins are thin "
  "and the work is drifting toward automation"),

 # ---- gated
 ("Structural steel fabricators & MEP", "Steel detailing, BIM, shop drawings",
  dict(BOTTLENECK=5, NOHIRE=5, WORLDCLASS=5, OWNER=4, PRECEDENT=5, META=2, AFFORD=4, WHITE=3),
  "**High-skilled manufacturing workers average age 57; 97% of firms worry about "
  "brain drain, half \"very concerned\"** [V] · mature Indian detailing industry — "
  "Outsource2India, IndiaCADWorks and dozens more, decades old [V]",
  "**On talent and shortage this is the strongest entry in the table.** It fails only "
  "on channel: the buyer is not on Instagram and barely on Facebook. Reachable by "
  "cold email and trade associations — a different company, not a different campaign"),

 ("Pharma & CRO", "Pharmacovigilance, clinical data management, regulatory affairs",
  dict(BOTTLENECK=4, NOHIRE=4, WORLDCLASS=5, OWNER=2, PRECEDENT=5, META=1, AFFORD=5, WHITE=3),
  "**India is the global hub with the largest concentration of this capability "
  "worldwide** [V]",
  "World-class supply and a real bottleneck — and an enterprise buyer with a "
  "procurement function, unreachable on Meta. Wrong company shape entirely"),

 ("Title & escrow", "Title examination and abstracting",
  dict(BOTTLENECK=4, NOHIRE=4, WORLDCLASS=4, OWNER=4, PRECEDENT=5, META=3, AFFORD=3, WHITE=3),
  "Aging workforce, thin pipeline [V]",
  "**Rate-cyclical, so it fails PATTERN condition 1** — the volume disappears exactly "
  "when we need revenue"),

 ("E-commerce / DTC brands", "Bookkeeping & reconciliation",
  dict(BOTTLENECK=2, NOHIRE=3, WORLDCLASS=5, OWNER=5, PRECEDENT=5, META=5, AFFORD=4, WHITE=5),
  "The current beachhead ([`MAP.md`](MAP.md)) [V]",
  "**Included as the control, and it gates out — deliberately.** Bookkeeping is a "
  "**cost centre**: no D2C founder sells more product because the ledger is current. "
  "That is not an argument against the beachhead, which was chosen on ad legibility "
  "and Meta reach. It is an explanation of *why the conversation is about price*"),
]


def sc(x):
    return sum(x[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def fails(x):
    return [f"{k}={x[k]}" for k, mn, _ in GATES if x[k] < mn]


R = [dict(v=v, s=s, x=x, ev=e, note=t, sc=sc(x), f=fails(x)) for v, s, x, e, t in H]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])


def report():
    print("# HUNGRY BUYERS — Bottlenecks, Not Cost Centres\n")
    print(f"**{len(R)} industry × seat pairs scored on {len(DIM)} weighted dimensions plus "
          f"{len(GATES)} gates.** Generated by")
    print("[`scoring/hungry.py`](scoring/hungry.py). Supply premise from "
          "[`SKILLS-INDIA.md`](SKILLS-INDIA.md).\n")

    print("---\n\n## 1. The distinction the whole screen rests on\n")
    print("| | Cost centre | **Bottleneck** |\n|---|---|---|")
    for a, b, c in [
        ("The buyer's felt problem", "*\"This costs too much\"*", "*\"I am turning work away\"*"),
        ("What they ask", "**\"How much cheaper?\"**", "**\"When can they start?\"**"),
        ("What you are selling", "Arbitrage", "**Capacity**"),
        ("Price elasticity", "High — they will shop you", "**Low — the seat pays for itself in won work**"),
        ("Example", "Bookkeeper for a DTC brand", "Estimator for a contractor"),
    ]:
        print(f"| **{a}** | {b} | {c} |")
    print("\n**The test is one question: does the absence of this seat cap the top line?** If yes, "
          "the buyer can")
    print("usually name the number — declined bid invitations, cases stuck in a records backlog, "
          "pitches lost")
    print("for want of a render. **That number is the offer.**\n")
    print("This is the same idea as Hormozi's starving crowd, made measurable: hunger is not a "
          "mood, it is a")
    print("**revenue constraint the buyer can count.**\n")

    print("---\n\n## 2. The criteria\n")
    print("| Dimension | Weight | What it measures |\n|---|---|---|")
    for k, w, d in DIM:
        print(f"| **{k}** | {w} | {d} |")
    print("\n| Gate | Fails below | Why |\n|---|---|---|")
    for k, mn, why in GATES:
        print(f"| **{k}** | {mn} | {why} |")

    print("\n---\n\n## 3. The ranking\n")
    print("| # | Industry | The bottleneck seat | Score | BTL | NOH | WC | OWN | META | AFF | WHT |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        x = r["x"]; star = " ⭐" if i <= 3 else ""
        print(f"| {i} | **{r['v']}**{star} | {r['s']} | **{r['sc']:.1f}** | {x['BOTTLENECK']} "
              f"| {x['NOHIRE']} | {x['WORLDCLASS']} | {x['OWNER']} | {x['META']} | {x['AFFORD']} "
              f"| {x['WHITE']} |")

    print("\n### Gated out\n")
    print("| Industry | Seat | Score | Failed | Why |\n|---|---|---|---|---|")
    for r in DEAD:
        print(f"| **{r['v']}** | {r['s']} | {r['sc']:.1f} | {', '.join(r['f'])} | {r['note']} |")

    print("\n---\n\n## 4. The top three, with the evidence\n")
    for i, r in enumerate(LIVE[:3], 1):
        print(f"### {i}. {r['v']} — {r['s']} · {r['sc']:.1f}\n")
        print(f"{r['ev']}\n")
        print(f"**{r['note']}.**\n")

    print("---\n\n## 5. What this changes about the economics\n")
    print("A bottleneck buyer is not price-sensitive in the way the whole model has assumed, and "
          "that touches")
    print("the fee directly.\n")
    print("| | |\n|---|---|")
    print("| **The current fee logic** | 30% of salary. It is priced against *what the worker "
          "costs*, which is the arbitrage frame |")
    print("| **What a bottleneck permits** | Pricing against *what the constraint costs them*. A "
          "contractor who can chase 30% more bid invitations is not comparing our fee to a salary — "
          "**they are comparing it to the jobs they declined** |")
    print("| **Why this matters more than a fee increase** | It is the **only** framing found so far "
          "that answers the price objection and the India objection ([`COUNTRIES.md`](COUNTRIES.md) "
          "§9) **with the same sentence** — because \"can start Monday, clears your bid backlog\" "
          "never invites *where are they from* |")
    print("\n**Do not raise the fee before the funnel is measured.** The point is that a bottleneck "
          "seat has")
    print("headroom a cost-centre seat does not, and that headroom is where the 30-day LTGP:CAC of "
          "4.25:1")
    print("([`scoring/LTGP.md`](scoring/LTGP.md)) has room to improve **without touching CAC at "
          "all.**\n")

    print("---\n\n## 6. How this sits against MAP.md\n")
    top = LIVE[0]
    print("**It does not overturn it, and the control row in the table is the proof.** "
          "E-comm × bookkeeping was")
    print("scored alongside everything else and **gates out on `BOTTLENECK`=2** — a DTC founder "
          "sells no more")
    print("product because the ledger is current.\n")
    print("| | [`MAP.md`](MAP.md) | This screen |\n|---|---|---|")
    for a, b, c in [
        ("Optimises", "**Ad legibility and Meta reach** — can we get a cold click at all",
         "**Buyer urgency** — will they haggle or hire"),
        ("Winner", "E-comm × Bookkeeper", f"**{top['v']} × {top['s']}**"),
        ("Fee logic", "Arbitrage — 30% of a salary", "Capacity — priced against declined work"),
        ("Risk", "The conversation is about price, forever",
         "Narrower verticals, and no proof the ad works yet"),
    ]:
        print(f"| **{a}** | {b} | {c} |")
    print(f"\n**The cheap reconciliation:** [`MAP.md`](MAP.md)'s test 1 is already funded at ~$1,500 "
          f"and tests one")
    print("ad to one vertical. **Run a second ad set at the same time to "
          f"{top['v'].lower()}**, same budget split, and")
    print("read the difference in cost per held call. If a bottleneck buyer converts materially "
          "better, that is")
    print("the whole thesis validated for the price of splitting a budget that is already "
          "committed.\n")
    print("**The honest limit:** `BOTTLENECK` is verified by direct quotation for contractors and "
          "PI firms, and")
    print("is `[E]` elsewhere. `NOHIRE` is `[V]` for accounting, insurance and steel detailing "
          "(hard shortage")
    print("data exists) and `[E]` otherwise. **Nothing here has been tested on a buyer.**\n")




def extras():
    """Two operator questions: video editors as a beachhead, and the collective model."""
    import io, os, sys
    from contextlib import redirect_stdout
    from dataclasses import replace
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    with redirect_stdout(io.StringIO()):
        import ltgp
    O = ltgp.OFFER
    cac, _ = ltgp.blended()

    # ---------------------------------------------------------------- video
    print("---\n\n## 7. Video editors — the economics, and the one real objection\n")
    print("Video ranks **3rd on supply quality** ([`SKILLS-INDIA.md`](SKILLS-INDIA.md), 92.4) and "
          "**5th here** (89.4).")
    print("It has the strongest world-class evidence in the whole repo and the best sentence "
          "anyone in this")
    print("category can say. So the question is whether the *money* works, and there is a reason "
          "to doubt it:")
    print("**a good Indian editor costs less than a bookkeeper, and our fee is a percentage of "
          "salary.**\n")
    print("| Placed salary | Fee @ 30% | 30-day GP | **30-day** | **Lifetime** |")
    print("|---|---|---|---|---|")
    for sal in (20_000, 18_000, 15_000, 12_000, 10_000):
        e, _ = ltgp.parts(replace(O, salary=float(sal)))
        mark = " ← typical editor" if sal == 15_000 else ""
        print(f"| ${sal:,}{mark} | ${sal*0.30:,.0f} | ${e['gp30']:,.0f} "
              f"| **{e['gp30']/cac:.2f}:1** | {e['gplife']/cac:.2f}:1 |")
    e15, _ = ltgp.parts(replace(O, salary=15_000.0))
    e10, _ = ltgp.parts(replace(O, salary=10_000.0))
    print(f"\n**The salary problem is real and not fatal.** At $15,000 the ratio is "
          f"{e15['gp30']/cac:.2f}:1; even at $10,000 it")
    print(f"is {e10['gp30']/cac:.2f}:1, still clearing the 1.5:1 constraint. **Lower salary costs "
          f"margin, not viability.**\n")
    print("### What actually decides it: who hires an editor as an *employee*\n")
    print("| Buyer | Buys editing how | Does a placement fee attach? |\n|---|---|---|")
    for a, b, c in [
        ("**Marketing agencies & production cos**", "**Full-time staff editors** — production "
         "capacity is their deliverable and their margin", "✅ **Yes.** This is the buyer"),
        ("Creators, podcasts, YouTube channels", "**Per video, or a monthly retainer with a "
         "freelancer**", "❌ **No.** There is no salary to take 30% of — which is what `AFFORD`=3 "
         "in the table above was really pointing at"),
        ("D2C brands", "Usually an agency or a freelancer; a full-time editor starts around "
         "$5-10M revenue", "~ Sometimes, and later than the bookkeeper"),
    ]:
        print(f"| {a} | {b} | {c} |")
    print("\n**So video editing is an agency seat, not a creator seat** — and agencies are "
          "already vertical two in")
    print("[`MAP.md`](MAP.md), so it needs no new outbound motion. The creator market is bigger "
          "and hungrier and")
    print("**structurally incompatible with a placement fee.**\n")
    print("### Two things unique to this seat\n")
    print("| | |\n|---|---|")
    print("| **The founder can grade it personally** | An ad editor's work is judged by hold rate "
          "and CTR — numbers the operator reads fluently. Of all five roles this is the one where "
          "the graded work sample can be scored by the founder rather than outsourced |")
    print("| **It is the fastest-moving AI risk in the set** | `AIDUR`=3 and falling. Generative "
          "video is improving faster than ledger automation. **A bookkeeper placed today is safe "
          "for a decade; an editor is a 3-5 year asset** |")

    # ---------------------------------------------------------- the collective
    print("\n---\n\n## 8. The talent-collective model — it fails on the operator's own constraint\n")
    print("*(`growths.club` does not resolve; `growth.club` is a Substack community. The category "
          "is curated\ntalent collectives: **Toptal, MarketerHire, Growth Collective, Right Side "
          "Up, A.Team**.)*\n")
    print("**What they actually charge** [V]:\n")
    print("| | Model |\n|---|---|")
    print("| **MarketerHire** | Published subscriptions: **$5,000 / $10,000 / $15,000 per month** |")
    print("| **Toptal** | Undisclosed markup, third-party estimates **up to ~50%**; blended "
          "**$60-200+/hour** |")
    print("| **Growth Collective** | Hourly or monthly retainer — **acquired by Toptal in June "
          "2024** |")
    print("| Vetting as positioning | Toptal **top 3%**, MarketerHire **top 5%** of applicants |")
    print("\nRun each revenue shape against the same funnel-derived CAC:\n")
    SAL_MO = 20_000 / 12
    print(f"| Revenue model | Month-1 GP | **30-day** | Lifetime GP | **Lifetime** | Clears 1.5:1? |")
    print("|---|---|---|---|---|---|")
    e, _ = ltgp.parts(O)
    rows = [("**Placement fee — current model**", e["gp30"], e["gplife"]),
            ("Thin take-rate, 20% markup", 0.20*SAL_MO*0.93, 0.20*SAL_MO*0.93*9),
            ("Toptal-style 50% markup", 0.50*SAL_MO*0.93, 0.50*SAL_MO*0.93*9),
            ("Managed seat, $800/mo spread", 800*0.93, 800*0.93*9),
            ("**MarketerHire-style $5,000/mo**", 3000*0.93, 3000*0.93*9)]
    for name, g1, life in rows:
        ok = "✅" if g1/cac >= 1.5 else "❌"
        print(f"| {name} | ${g1:,.0f} | **{g1/cac:.2f}:1** | ${life:,.0f} | {life/cac:.2f}:1 | {ok} |")
    print("\n**Every ongoing-margin model fails the 30-day constraint except the high-ticket "
          "subscription.** A")
    print(f"20% take-rate returns **{0.20*SAL_MO*0.93/cac:.2f}:1** in month one — you would be "
          f"spending ${cac:,.0f} to buy $310. That")
    print("is not a pricing detail, it is a different company with a different balance sheet.\n")
    print("### And the one version that clears is the one already rejected\n")
    print("| The $5,000/mo subscription requires | Which collides with |\n|---|---|")
    for a, b in [
        ("A 3x markup on the salary you pay",
         "**The salary-transparency positioning** — the explicit reason EOR beat a salary markup "
         "([`MASTER.md`](MASTER.md) §9). You cannot publish the salary and charge 3x it"),
        ("A real sales cycle for a $60k/yr commitment",
         "**\"No sales call may determine CAC\"** — a hard constraint from the start"),
        ("Matching, QA and dispute handling on every engagement",
         "*\"Operationally very intensive\"* — the stated reason the managed-service path was "
         "killed ([`SCALE.md`](SCALE.md) §1)"),
    ]:
        print(f"| {a} | {b} |")
    print(f"\n**Its lifetime economics are genuinely better** — {3000*0.93*9/cac:.1f}:1 against "
          f"{e['gplife']/cac:.1f}:1, more than double. So this")
    print("is a real fork, not a bad idea. It is just **a different business**: fewer, bigger, "
          "higher-touch")
    print("accounts sold by a person, against many, smaller, self-serve placements sold by an ad.\n")
    print("### What to steal from them instead\n")
    print("> **Toptal's \"top 3%\" and MarketerHire's \"top 5%\" are positioning claims, not "
          "revenue models.**\n")
    print("The curation claim is the valuable half of the collective idea and it is **free** — "
          "it attaches to a")
    print("placement fee just as well as to a subscription. We already have the mechanism: the "
          "**graded work")
    print("sample on the client's own books** ([`OFFER.md`](OFFER.md) §2.5). That is a *stronger* "
          "curation claim")
    print("than a percentage, because it is evidence about one named person rather than a "
          "statistic about a")
    print("funnel nobody can audit.\n")
    print("**And note the consolidation signal: Toptal bought Growth Collective in June 2024** "
          "[V]. Standalone")
    print("collectives are being absorbed, which is what a category with thin unit economics and "
          "high ops cost")
    print("looks like from the outside.\n")


if __name__ == "__main__":
    report()
    extras()
