#!/usr/bin/env python3
"""
The full activity map -- and a correction to how the earlier ones were ranked.

Three passes have now been made at this: CLAUDE-CODE.md (33 uses), SURFACES.md (62
activities), WORKFLOWS.md (25 systems). Each was ranked by leverage, and **that is why
things kept being missed**. Leverage-ranking systematically buries a whole class of
work:

    A BLOCKER has modest "value added" and infinite importance, because nothing else
    happens until it exists.

You cannot invoice a US client from India without an entity and a payment rail. You
cannot be paid without a W-8BEN-E on file. You cannot place a person without a contract
that assigns IP. None of those "add value" in the way a teardown generator does, so a
leverage ranking puts them mid-table -- where they sit until the week they stop
everything.

So this file adds a BLOCKER flag, surfaces those as Tier 0 regardless of score, and
widens the map to the functions the earlier passes never opened at all: entity and
banking, Indian tax and export compliance, employment structure, security and account
access, insurance, attribution, win/loss, and the risk register.

Scored on the same six weights as before, so the rankings are comparable:
  IMPORTANCE 24 · VALUE 22 · TIMESAVED 20 · FIT 16 · NOW 12 · REUSE 6

Run:  python3 scoring/activities.py > /dev/null   (writes ACTIVITIES.md)
"""

OUT = "ACTIVITIES.md"
DIM = [("IMPORTANCE", 24), ("VALUE", 22), ("TIMESAVED", 20),
       ("FIT", 16), ("NOW", 12), ("REUSE", 6)]

B = True   # blocker: nothing downstream happens until this exists
_ = False

# (function, activity, surface, blocker, IMP, VAL, TIME, FIT, NOW, REUSE, note)
A = [
 # ===== 1. ENTITY, BANKING, PAYMENTS =====================================
 ("Entity", "Decide the entity structure — India Pvt Ltd, US LLC, or both", "Chat", B,
  5,5,3,3,5,3, "**The first unopened question in this whole repo.** You are in India selling "
  "to US buyers. It determines how you invoice, how you are taxed, what a client's "
  "procurement will accept, and whether Stripe will take you at all. `FIT`=3 — draft the "
  "options, **a CA and a US attorney decide**"),
 ("Entity", "Register the entity and get the identifiers", "Cowork", B,
  5,4,3,3,5,2, "PAN, TAN, incorporation certificate — or the US equivalent"),
 ("Entity", "Business bank account that can receive USD", "Cowork", B,
  5,4,3,3,5,2, "Nothing else in the model happens until money can land"),
 ("Entity", "Choose the payment rail for client payments", "Chat", B,
  5,4,4,4,5,3, "Stripe, Wise, Payoneer, Razorpay — availability depends on the entity "
  "decision above, which is why that one comes first"),
 ("Entity", "Payout rail for paying Indian talent", "Chat", B,
  5,4,3,4,5,3, "The other half of the flow, and the half with a monthly deadline"),
 ("Entity", "**W-8BEN-E** and the US client tax-form pack", "Cowork", B,
  5,3,4,3,5,5, "**A US company cannot pay a foreign entity without this on file.** It will "
  "be requested during onboarding of your very first client, and not having it delays cash"),
 ("Entity", "GST registration and **LUT for export of services**", "Cowork", B,
  5,4,3,3,5,4, "Service exports are zero-rated in India **only with the right filing in "
  "place**. Getting this wrong is a real cash cost on every invoice"),
 ("Entity", "FEMA / FIRC handling for inbound forex", "Cowork", _,
  4,3,3,3,4,4, "Your bank will want it. Set the process up once"),

 # ===== 2. EMPLOYMENT STRUCTURE ==========================================
 ("Employment", "**Decide: are you the EOR, or do you partner with one?**", "Chat", B,
  5,5,3,4,5,4, "**The single largest unanswered structural question left.** Being the EOR "
  "means payroll, PF, ESI, gratuity and TDS on your books at $477/employee/month margin. "
  "Partnering means sharing that margin but no compliance surface. **The model assumes the "
  "revenue and has never priced the obligation**"),
 ("Employment", "Contractor vs employee classification for placed talent", "Chat", B,
  5,4,3,3,5,4, "Misclassification is the standard way this category gets into trouble"),
 ("Employment", "Talent contract — IP assignment, confidentiality, non-solicit", "Cowork", B,
  5,4,4,3,5,5, "**IP assignment is not optional** — you are selling creative output your "
  "client will own. Non-solicit is what stops a client hiring your placement directly"),
 ("Employment", "Payroll calendar, payslips, TDS", "Cowork", _,
  4,3,4,4,3,5, "Monthly and unforgiving. People leave over late pay"),
 ("Employment", "Equipment and software policy for placed talent", "Cowork", _,
  3,3,3,4,3,4, "Who buys the laptop and the Adobe licence, and who owns it after"),
 ("Employment", "Talent exit and offboarding", "Cowork", _,
  3,3,3,4,2,4, "Access revoked, IP confirmed, client told first"),

 # ===== 3. SECURITY AND ACCESS ===========================================
 ("Security", "**Client ad-account access protocol**", "Cowork", B,
  5,4,4,4,5,5, "**You will be handed access to clients' Meta ad accounts.** That is the "
  "single most sensitive thing in the business. Partner access via Business Manager, never "
  "shared logins, 2FA everywhere, and documented revocation on exit"),
 ("Security", "Password manager and device hygiene, for you and every placement", "Cowork", _,
  4,3,3,4,4,4, "One compromised placement account is a client-losing event"),
 ("Security", "Handling client creative and brand assets", "Cowork", _,
  3,3,3,4,3,4, "Where files live, who can see them, what happens at the end"),

 # ===== 4. RISK ==========================================================
 ("Risk", "**Meta Business Manager structure and ban resilience**", "Code", B,
  5,5,4,4,5,5, "**The severe one, and it is inside your own expertise.** A new advertiser "
  "with a new domain and a new page in a scrutinised category is exactly the profile that "
  "gets restricted. Separate BM, verified domain, clean page history, a second ad account "
  "ready — build it *before* it is needed, because you cannot build it after"),
 ("Risk", "Client concentration monitor", "Code", _,
  4,4,3,5,2,4, "At five clients, one leaving is 20% of revenue"),
 ("Risk", "Written risk register with triggers", "Cowork", _,
  3,4,3,4,3,5, "Ad account ban, payment freeze, a bad placement going public, AI "
  "substitution. **`DURABLE`=3 is already the model's weakest score**"),
 ("Risk", "Professional indemnity / E&O insurance", "Chat", _,
  3,3,3,3,3,3, "Larger clients ask. Cheap relative to losing the deal"),

 # ===== 5. STRATEGY AND MODEL ============================================
 ("Strategy", "Keep the model live on real numbers, monthly", "Code", _,
  5,5,4,5,5,5, "`funnel.py` marks steps 6–9 as assumptions. From week three they are facts, "
  "and four inputs re-derive everything downstream in one command"),
 ("Strategy", "Scenario-test before committing spend", "Code", _,
  4,4,4,5,5,3, "A one-line change, not a debate"),
 ("Strategy", "Expansion screens — next role, next country, next ICP", "Code", _,
  4,4,5,5,2,5, "`COUNTRIES.md` and `MAP.md` are the machinery. Re-run, do not rebuild"),
 ("Strategy", "Weekly review ritual", "Chat", _, 4,4,4,4,5,2,
  "Fifteen minutes. The habit matters more than the tool"),
 ("Strategy", "Decision journal", "Cowork", _, 3,4,2,4,4,5,
  "The repo does this for analysis. Do it for the calls between analyses"),

 # ===== 6. WEBSITE =======================================================
 ("Website", "Landing-page copy for `/agencies`, `/ecommerce`, `/teardown`", "Chat", _,
  5,4,4,4,5,3, "The words convert, not the layout"),
 ("Website", "`/proof` write-ups — recut ads with retention deltas", "Chat", _,
  5,5,3,4,5,4, "**The most important page on the site**"),
 ("Website", "Pixel, CAPI and event verification", "Code", B,
  5,4,4,5,5,4, "**Verify with test events before spending.** Every CAC number assumes "
  "attribution works"),
 ("Website", "LP variants per angle", "Chat", _, 4,3,4,4,5,2,
  "Iterate, do not split-test — `SITE.md` §1"),
 ("Website", "Legal pages — privacy, terms, cookie notice", "Cowork", _,
  3,2,4,4,4,4, "Meta review looks for them, and EU or UK buyers expect them"),
 ("Website", "Design and mobile QA", "Chat", _, 3,3,4,4,4,2,
  "Chat, because it needs eyes on the actual page"),
 ("Website", "Brand voice guide", "Cowork", _, 3,3,3,4,4,5,
  "Stops the site, ads and emails sounding like three companies"),

 # ===== 7. META ADS ======================================================
 ("Meta ads", "Build the intent-seed audience from scraped job postings", "Code", _,
  5,5,5,5,5,5, "**25% of spend at the best CAC in the model — $489, 9.07:1**"),
 ("Meta ads", "Count job postings across every phrasing first", "Code", _,
  4,4,4,5,5,2, "`MODEL-V2.md` gap 10. Free, one afternoon, and it decides the ad"),
 ("Meta ads", "Meta Ad Library sweep", "Code", _, 3,4,5,5,5,3,
  "**Long-running ads are the ones that work.** Public data"),
 ("Meta ads", "Creative concepts and scripts", "Chat", _, 4,3,4,3,5,2,
  "`FIT`=3. You judge creative better than any agent"),
 ("Meta ads", "Ad copy variants in volume", "Chat", _, 3,2,4,4,5,2,
  "The commodity use"),
 ("Meta ads", "Weekly account read", "Code", _, 4,3,5,4,4,3,
  "The gain is doing it weekly without losing an evening"),
 ("Meta ads", "**Special Ad Category pre-check**", "Chat", _, 4,4,3,4,5,3,
  "`SUPPLY-DEMAND.md` §1 prices this at a **10–29% CAC tax** if a B2B ad gets "
  "reclassified as employment"),
 ("Meta ads", "Budget pacing rules", "Code", _, 3,4,3,4,3,4,
  "A script that says where money should move"),

 # ===== 8. OUTBOUND ======================================================
 ("Outbound", "Cold-email infrastructure — domains, SPF/DKIM/DMARC, warm-up", "Code", B,
  5,4,4,5,5,5, "**2–4 week lead time — the longest in the business.** Start week one even "
  "though it sends week four"),
 ("Outbound", "Prospect list pipeline", "Code", _, 5,5,5,5,5,5,
  "Job postings, Ad Library, directories. **Respect each site's terms**"),
 ("Outbound", "Email verification and suppression", "Code", B,
  4,3,4,5,5,5, "Bounce above ~2–3% damages the sending domain"),
 ("Outbound", "Per-prospect personalisation at volume", "Code", _,
  4,4,5,4,4,4, "**The part that makes cold email work and does not scale by hand**"),
 ("Outbound", "Sequence writing", "Chat", _, 4,4,4,4,5,4, "Short. One ask. The ask is the "
  "paid teardown"),
 ("Outbound", "Reply triage and routing", "Cowork", _, 3,3,4,4,4,3,
  "Four buckets, four responses, none left overnight"),
 ("Outbound", "LinkedIn outbound — manual", "Chat", _, 3,3,3,4,4,2,
  "Drafting only. **Do not automate or scrape it**"),

 # ===== 9. OTHER DEMAND ==================================================
 ("Demand", "**Brand-defence search campaign**", "Code", _, 4,4,4,4,5,4,
  "`ARBITRARY.md` §13: searching *all hands talent* returns **three other organisations "
  "and not you.** A few dollars a month fixes it. Nobody else bids on your name"),
 ("Demand", "LinkedIn company page and founder profile", "Cowork", B,
  4,4,3,4,5,3, "**The first thing a Western buyer checks** on an operator with no track "
  "record. Free, and it ranks for your brand query"),
 ("Demand", "Directory listings — Clutch and category directories", "Cowork", _,
  3,3,3,4,3,4, "Cheap credibility and a live backlink"),
 ("Demand", "Partnership and referral outreach to adjacent vendors", "Chat", _,
  4,4,3,4,3,3, "Agencies that do media buying but not editing are a warm channel"),
 ("Demand", "Referral request loop after a 90-day check-in", "Cowork", _,
  4,4,3,4,2,5, "Systematically, not when you remember"),

 # ===== 10. SALES ========================================================
 ("Sales", "Teardown generator", "Code", _, 5,5,5,4,5,5,
  "The money gate. **A product, not a bespoke job**"),
 ("Sales", "Pre-call research brief", "Code", _, 4,4,5,5,5,4, "One page, every call"),
 ("Sales", "Call script and objection handling", "Chat", _, 4,4,3,4,5,4,
  "Especially the India objection — `COUNTRIES.md` §9 prices it"),
 ("Sales", "**Self-reported attribution on the form**", "Code", B,
  4,5,3,5,5,5, "*\"How did you hear about us?\"* — **once you run two channels, "
  "platform-reported attribution will double-count and you will defund the wrong one.** "
  "One field, added before the second channel starts"),
 ("Sales", "Proposal → contract → invoice → kickoff", "Cowork", _,
  3,3,4,4,4,4, "Templated so no deal stalls on paperwork"),
 ("Sales", "MSA and per-placement SOW", "Cowork", B,
  5,4,4,3,5,5, "Draft only, lawyer-reviewed. **Nothing gets signed without it**"),
 ("Sales", "Pipeline tracking", "Cowork", _, 3,3,3,4,4,4, "A sheet until deal thirty"),
 ("Sales", "**Win/loss analysis**", "Cowork", _, 4,5,3,4,3,5,
  "**The most-skipped high-value activity in any young business.** Ten lost deals tell you "
  "more than a hundred impressions"),

 # ===== 11. PRICING ======================================================
 ("Pricing", "Rate card and the fee definition", "Code", B,
  5,5,3,4,5,5, "`MODEL-V2.md` gap 1: **the one-time-versus-monthly conflation breaks the "
  "model 8× if left ambiguous.** Write it down once, unambiguously"),
 ("Pricing", "Guarantee terms — 12-month replacement", "Cowork", B,
  5,4,4,4,5,5, "Modelled as **cheaper than the 6-month industry standard** while sounding "
  "stronger"),
 ("Pricing", "Payment terms, deposits, late fees", "Cowork", _,
  4,4,3,4,4,4, "You pay talent monthly. Terms are a cash-flow instrument, not admin"),
 ("Pricing", "Annual increase policy", "Chat", _, 3,4,2,4,2,4,
  "Decide before the first renewal, not during it"),

 # ===== 12. SUPPLY =======================================================
 ("Supply", "Grading rubric as a scoring tool", "Code", _, 5,5,4,4,5,5,
  "**Recut an ad, measure 3s and 15s retention against the original.** What makes premium "
  "falsifiable"),
 ("Supply", "The graded directory, v0", "Code", _, 5,5,4,5,4,5,
  "The retention mechanism — **+$9,022 per client**"),
 ("Supply", "Sourcing pipeline from public portfolios", "Code", _,
  4,4,5,4,5,4, "Where the terms permit"),
 ("Supply", "Take-home brief and its scoring sheet", "Cowork", _,
  4,4,4,4,4,5, "Consistency *is* the product"),
 ("Supply", "Screening reels against the rubric", "Chat", _, 4,3,5,3,5,2,
  "`FIT`=3. It shortlists. **You watch the reel**"),
 ("Supply", "Interview structure and reference checks", "Cowork", _,
  3,3,3,4,4,5, "Written once"),
 ("Supply", "Client brief → shortlist of three", "Cowork", _, 4,5,4,4,4,5,
  "Where the bench turns into revenue"),
 ("Supply", "Bench nurture", "Cowork", _, 3,4,3,4,3,4,
  "Graded people go cold"),
 ("Supply", "English and communication assessment", "Chat", _,
  4,4,3,4,4,4, "`COUNTRIES.md` gates on this for a reason — it is the failure mode buyers "
  "fear most about India"),

 # ===== 13. DELIVERY =====================================================
 ("Delivery", "Onboarding day 0–30", "Cowork", _, 5,4,3,4,4,5,
  "Protects **seat continuity, the largest single lever**"),
 ("Delivery", "30/60/90 check-in cadence", "Cowork", _, 4,5,3,4,3,5,
  "Turns 9 EOR months into 30"),
 ("Delivery", "Replacement request handling", "Cowork", _, 3,3,3,4,3,4,
  "The guarantee only differentiates if it is fast"),
 ("Delivery", "Escalation path for underperformance", "Cowork", _,
  4,4,3,4,3,5, "**Before it happens.** Mid-month failure is the moment that decides "
  "whether a client renews"),
 ("Delivery", "Time-zone overlap and comms norms", "Cowork", _,
  4,4,3,4,4,5, "`COUNTRIES.md` gates ASYNC. Agree the overlap window in writing at kickoff"),
 ("Delivery", "Seat expansion play", "Chat", _, 4,5,2,4,3,3,
  "Seats-per-client is where the economics live"),
 ("Delivery", "Client feedback loop", "Cowork", _, 3,4,3,4,3,4,
  "The input to the grading rubric"),

 # ===== 14. FINANCE ======================================================
 ("Finance", "**Cash-flow forecast**", "Code", B, 5,5,3,5,5,4,
  "**You pay talent monthly and get paid lumpily.** The failure mode that kills placement "
  "businesses"),
 ("Finance", "Unit-economics dashboard", "Code", _, 4,4,4,5,4,5,
  "Six numbers you steer by. A script, not a SaaS"),
 ("Finance", "Invoicing and the monthly EOR run", "Cowork", _,
  4,3,4,4,3,5, "$477/employee/month recurring"),
 ("Finance", "Collections chase", "Cowork", _, 3,3,4,4,3,4,
  "Polite, automatic, escalating"),
 ("Finance", "**FX policy — INR cost base, USD revenue**", "Code", _,
  4,4,2,4,3,4, "A real margin variable the model does not carry. A 5% move is 5% of gross "
  "margin"),
 ("Finance", "Bookkeeping prep for the accountant", "Cowork", _,
  2,2,4,4,3,4, "Categorise and reconcile. **The accountant still files**"),
 ("Finance", "Runway and personal burn", "Code", _, 4,4,3,4,5,3,
  "How many months of no revenue you can absorb. Decide before spending on ads"),

 # ===== 15. MEASUREMENT ==================================================
 ("Measure", "UTM and naming discipline", "Code", B, 4,4,4,5,5,5,
  "**Set before the first click or the data is never clean.** Retrofitting is impossible"),
 ("Measure", "Weekly metrics review", "Code", _, 4,3,5,5,5,4, "One command, six numbers"),
 ("Measure", "Monthly model re-run and decision memo", "Code", _,
  5,5,4,5,4,5, "**Replace assumptions with actuals and re-derive everything**"),
 ("Measure", "Cohort and payback analysis", "Code", _, 4,4,4,5,3,4,
  "Cannot manage seat continuity without it"),
 ("Measure", "Cross-channel lead dedupe", "Code", _, 3,4,3,5,3,4,
  "Same company from Meta and cold email is one lead, not two"),
 ("Measure", "Competitor and salary monitor", "Code", _, 3,3,5,5,3,5,
  "Scheduled diffs. Runs without you"),

 # ===== 16. LEGAL AND IP =================================================
 ("Legal", "**USPTO Class 35 clearance on *All Hands***", "Chat", _,
  4,4,4,3,5,3, "Outstanding for four rounds. **Two live users of *All Hands* exist in "
  "talent services.** Monitoring is agent work; **the opinion is not**"),
 ("Legal", "NDAs and mutual confidentiality", "Cowork", _, 4,3,4,3,4,5,
  "Draft only"),
 ("Legal", "Data-protection basics for EU/UK clients", "Chat", _,
  3,3,3,3,3,3, "Know it before selling into it"),

 # ===== 17. CONTENT ======================================================
 ("Content", "Case studies with real numbers", "Cowork", _, 4,4,4,4,3,4,
  "**Only with real numbers.** A fabricated one is worse than none when the positioning is "
  "*falsifiable*"),
 ("Content", "X during launch month", "Chat", _, 2,2,4,4,4,1,
  "`MODEL-V2.md` gap 11 caps this deliberately"),
 ("Content", "Newsletter from month three", "Cowork", _, 3,3,4,4,2,3,
  "First number from your first ten placements"),

 # ===== 18. OPS AND FOUNDER ==============================================
 ("Ops", "**SOP capture on anything done twice**", "Cowork", _,
  4,5,4,4,4,5, "**The substitute for employees.** What you hand a first hire instead of "
  "explaining"),
 ("Ops", "Tool stack and integration decisions", "Chat", _, 3,3,3,4,4,2,
  "You have already made five"),
 ("Ops", "Inbox and calendar triage", "Cowork", _, 2,2,4,3,4,2,
  "Real by month six"),
 ("Ops", "Weekly planning and time budgeting", "Chat", _, 4,4,3,3,5,3,
  "**Attention is the binding constraint in every model in this repo.** Budget it "
  "explicitly"),
 ("Hiring", "First VA or recruiter — scope, JD, screening", "Cowork", _,
  4,4,3,4,2,5, "Month four to six. **The SOPs are what make this hire cheap**"),
 ("Hiring", "Training material from your own SOPs", "Cowork", _,
  3,4,4,4,2,5, "Written once, reused per hire"),
]


def main():
    W = dict(DIM)

    def sc(i, v, t, f, n, r):
        d = {"IMPORTANCE": i, "VALUE": v, "TIMESAVED": t, "FIT": f, "NOW": n, "REUSE": r}
        return sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100

    rows = sorted([(sc(i, v, t, f, n, r), fn_, act, sur, blk, i, v, t, f, n, r, why)
                   for fn_, act, sur, blk, i, v, t, f, n, r, why in A], key=lambda x: -x[0])
    blockers = [x for x in rows if x[4]]

    L = []
    P = L.append
    P("# Every Activity — Third Pass, and a Correction to the Ranking\n")
    P(f"**{len(A)} activities across {len(set(x[0] for x in A))} functions.** Up from 62, and "
      "the additions are not\ndetail — they are **whole functions the earlier passes never "
      "opened**: entity and banking, Indian\ntax and export compliance, employment structure, "
      "security and account access, insurance,\nattribution, win/loss, and risk.\n")

    P("---\n\n## 1. Why things kept being missed\n")
    P("Every earlier pass ranked by **leverage**, and leverage-ranking has a systematic blind "
      "spot:\n")
    P("> **A blocker has modest *value added* and infinite *importance*, because nothing else "
      "happens\n> until it exists.**\n")
    P("You cannot invoice a US client from India without an entity and a payment rail. You "
      "cannot be paid\nwithout a **W-8BEN-E** on file. You cannot place a person without a "
      "contract that assigns IP. None\nof those *add value* the way a teardown generator does "
      "— so a leverage ranking puts them mid-table,\nwhere they sit quietly until the week "
      "they stop everything.\n")
    P(f"So: a `BLOCKER` flag, and **{len(blockers)} of {len(A)} activities carry it.**\n")

    P("---\n\n## 2. Tier 0 — blockers, in rough dependency order\n")
    P("**These are not ranked by score.** They are ranked by what unblocks what.\n")
    P("| # | Function | Blocker | Surface | Why nothing moves without it |")
    P("|---|---|---|---|---|")
    # explicit dependency sequence -- score order is wrong here by construction
    DEP = [
        "Decide the entity structure", "Register the entity", "Business bank account",
        "Choose the payment rail", "Payout rail", "W-8BEN-E", "GST registration",
        "Decide: are you the EOR", "Contractor vs employee", "Talent contract",
        "Rate card and the fee definition", "Guarantee terms", "MSA and per-placement SOW",
        "LinkedIn company page", "Pixel, CAPI and event", "UTM and naming",
        "Self-reported attribution", "Meta Business Manager structure",
        "Client ad-account access", "Cold-email infrastructure", "Email verification",
        "Cash-flow forecast",
    ]

    def dep_rank(x):
        for i, frag in enumerate(DEP):
            if frag.lower() in x[2].lower():
                return i
        return 99

    for k, (sv, fn_, act, sur, blk, *rest, why) in enumerate(
            sorted(blockers, key=dep_rank), 1):
        clean = act.replace("**", "")
        P(f"| {k} | {fn_} | **{clean}** | `{sur}` | {why} |")
    P("")
    P("**Read the first six rows as a single chain.** Entity → identifiers → bank → payment "
      "rail → payout\nrail → W-8BEN-E → GST/LUT. **Every one of them gates the one after it**, "
      "and the whole chain gates\nyour first invoice being paid. In India-to-US services this "
      "sequence commonly takes weeks, not\ndays — which puts it alongside cold-email warm-up "
      "as a lead-time item that has to start now.\n")

    P("---\n\n## 3. The full ranking\n")
    P("`IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · `FIT` 16 · `NOW` 12 · `REUSE` 6. "
      "**🔒 = blocker.**\n")
    P("| # | Function | Activity | Surface | 🔒 | Imp | Val | Time | Fit | Now | Re | Score | "
      "Why |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for k, (s, fn_, act, sur, blk, i, v, t, f, n, r, why) in enumerate(rows, 1):
        P(f"| {k} | {fn_} | {act} | **{sur}** | {'🔒' if blk else ''} | {i} | {v} | {t} | {f} | "
          f"{n} | {r} | **{s:.0f}** | {why} |")
    P("")

    P("### Top 15\n")
    for k, (s, fn_, act, sur, blk, *_) in enumerate(rows[:15], 1):
        P(f"{k}. {'🔒 ' if blk else ''}**{act}** — {fn_} · `{sur}` · {s:.0f}")
    P("")

    P("---\n\n## 4. What this pass added that the earlier ones missed\n")
    P("| Missed | Why it matters |\n|---|---|")
    for a, b in [
        ("**The entity and payment chain**", "You are in India selling to US buyers and "
         "**nothing in this repo had addressed how you get paid.** Seven blockers in "
         "sequence"),
        ("**Whether you are the EOR or partner with one**", "The model books **$477/employee/"
         "month** of EOR margin and has **never priced the compliance obligation** behind it. "
         "PF, ESI, gratuity and TDS are not free"),
        ("**Meta account-ban resilience**", "A new advertiser, new domain, new page, "
         "scrutinised category. **This is the profile that gets restricted** — and it is "
         "inside your own expertise, so it is inexcusable to leave to chance"),
        ("**Client ad-account access protocol**", "You will hold access to clients' ad "
         "accounts. **The most sensitive thing in the business**, and it had never appeared"),
        ("**Self-reported attribution**", "The moment you run Meta *and* cold email, "
         "platform-reported numbers double-count. **One form field, added before the second "
         "channel — or you defund the wrong one**"),
        ("**UTM discipline**", "Set before the first click or the data is never clean. "
         "Retrofitting is impossible"),
        ("**Win/loss analysis**", "The most-skipped high-value activity in any young "
         "business. Ten lost deals teach more than a hundred thousand impressions"),
        ("**Escalation path for underperformance**", "Mid-month failure is the moment that "
         "decides renewal, and there was no process for it"),
        ("**Brand-defence search**", "*All hands talent* currently returns three other "
         "organisations. A few dollars a month"),
        ("**Runway and personal burn**", "How many months of no revenue you can absorb — "
         "decided **before** ad spend, not during it"),
    ]:
        P(f"| {a} | {b} |")
    P("")

    P("---\n\n## 5. The split, recomputed\n")
    tot, val = {}, {}
    for s, fn_, act, sur, *rest in rows:
        tot[sur] = tot.get(sur, 0) + 1
        val[sur] = val.get(sur, 0) + s
    n = len(rows)
    vs = sum(val.values())
    P("| Surface | Activities | Share | Share of value | Avg |")
    P("|---|---|---|---|---|")
    for sur in ("Code", "Cowork", "Chat"):
        P(f"| **{sur}** | {tot[sur]} | {tot[sur]/n:.0%} | **{val[sur]/vs:.0%}** | "
          f"{val[sur]/tot[sur]:.1f} |")
    P("")
    bl = {}
    for x in blockers:
        bl[x[3]] = bl.get(x[3], 0) + 1
    P(f"**Cowork moves up on this pass** — from {21} activities to {tot['Cowork']}. The reason "
      "is the whole\ncategory that was missing: **entity, contracts, compliance, access "
      "protocols and SOPs are all\ndocument work.** Of the {} blockers, {} are Cowork or "
      "Chat.\n".format(len(blockers), sum(v for k, v in bl.items() if k != "Code")))
    P("> **The corrected shape: Code is where the leverage is, Cowork is where the *blockers* "
      "are.**\n> The earlier passes measured the first and never looked at the second.\n")
    open(OUT, "w").write("\n".join(L))
    print(f"{len(A)} activities, {len(blockers)} blockers")
    for sur in ("Code", "Cowork", "Chat"):
        print(f"  {sur:7s} {tot[sur]:2d} ({tot[sur]/n:.0%}) value {val[sur]/vs:.0%} "
              f"avg {val[sur]/tot[sur]:.1f}")
    print("\ntop 15:")
    for s, fn_, act, sur, blk, *_ in rows[:15]:
        print(f"  {s:5.1f} {'LOCK' if blk else '    '} {sur:7s} {fn_:10s} {act[:52]}")


if __name__ == "__main__":
    main()
