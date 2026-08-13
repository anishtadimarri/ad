#!/usr/bin/env python3
"""
Every function of a one-person company, across Claude Code, Cowork and Chat.

"I won't have employees" is the operative constraint. A solo operator is not running a
business with some functions -- they are running **all** of them, badly, in whatever
order the day imposes. So this enumerates the functions rather than the tasks, then
places each activity on the surface that actually fits it.

The assignment rule is by TASK SHAPE, not by product feature list, because feature
lists move and the shape does not:

  CODE    the output is a runnable tool, a data pipeline, or a VERIFIED FACT.
          Anything where being checkable matters more than being fast.
  COWORK  the output is a document, spreadsheet or deck -- or repeated operational
          work over a folder of business files.
  CHAT    the output is a judgement, a draft, or an answer you will use in the next
          ten minutes. Includes looking at things: creative, screenshots, a page.

Scored on the operator's own criteria, same weights as scoring/claude_code.py so the
two files are comparable:

  IMPORTANCE 24 · VALUE 22 · TIMESAVED 20 · FIT 16 · NOW 12 · REUSE 6

FIT again means "how well does an agent do this VERSUS the operator doing it" -- which
is why the sales call is absent from the ranking and sits in the do-not list instead.

Run:  python3 scoring/surfaces.py > /dev/null   (writes SURFACES.md)
"""

OUT = "SURFACES.md"
DIM = [("IMPORTANCE", 24), ("VALUE", 22), ("TIMESAVED", 20),
       ("FIT", 16), ("NOW", 12), ("REUSE", 6)]

# (function, activity, surface, IMP, VAL, TIME, FIT, NOW, REUSE, note)
A = [
 # ---- 1. Strategy and the model ----------------------------------------
 ("Strategy", "Keep the model live on real numbers, monthly", "Code", 5,5,4,5,5,5,
  "`funnel.py` marks steps 6–9 as **assumptions, because no data existed**. From week "
  "three they are facts. Four real inputs re-derive CAC, both ratios, the audience split "
  "and the scale arithmetic **in one command**"),
 ("Strategy", "Scenario-test before committing spend", "Code", 4,4,4,5,5,3,
  "*\"What if deposit take-up is 12%?\"* is a one-line change, not a debate"),
 ("Strategy", "Weekly review — what changed, what it means, what to do", "Chat", 4,4,4,4,5,2,
  "Fifteen minutes with the numbers in front of you. The habit matters more than the tool"),
 ("Strategy", "Expansion screens — next role, next country, next ICP", "Code", 4,4,5,5,2,5,
  "`COUNTRIES.md` and `MAP.md` are the machinery. Re-run it, do not rebuild it"),
 ("Strategy", "Decision journal — what you decided and why", "Cowork", 3,4,2,4,4,5,
  "The repo does this for analysis. Do it for the calls you make between analyses"),

 # ---- 2. Website and brand ---------------------------------------------
 ("Website", "Landing-page copy for `/agencies`, `/ecommerce`, `/teardown`", "Chat", 5,4,4,4,5,3,
  "The words convert, not the layout. Draft in chat, paste into Framer"),
 ("Website", "`/proof` write-ups — recut ads with retention deltas", "Chat", 5,5,3,4,5,4,
  "**The most important page on the site.** Where *premium* stops being an adjective"),
 ("Website", "LP variants for each new angle", "Chat", 4,3,4,4,5,2,
  "Volume of variants, judged by you. §1 of `SITE.md`: iterate, do not split-test"),
 ("Website", "Design and mobile QA — screenshot in, problems out", "Chat", 3,3,4,4,4,2,
  "Chat because it needs **eyes on the actual page**"),
 ("Website", "Brand voice guide — one page, so every asset matches", "Cowork", 3,3,3,4,4,5,
  "Cheap, and it stops the site, the ads and the emails sounding like three companies"),
 ("Website", "Technical setup — pixel, CAPI, events, redirects", "Code", 4,4,4,5,5,4,
  "**Verify CAPI with test events before spending.** Every CAC number assumes attribution "
  "works"),

 # ---- 3. Meta ads -------------------------------------------------------
 ("Meta ads", "Build the intent-seed audience from scraped job postings", "Code", 5,5,5,5,5,5,
  "`TARGETING.md`'s thesis. **25% of spend at the best CAC in the model — $489, 9.07:1.** "
  "Scrape, dedupe, export. Rebuild monthly so the signal stays dated"),
 ("Meta ads", "Count job postings across every phrasing, before writing the ad", "Code", 4,4,4,5,5,2,
  "`MODEL-V2.md` gap 10. Free, one afternoon, and it decides the ad"),
 ("Meta ads", "Meta Ad Library sweep — who runs what, and for how long", "Code", 3,4,5,5,5,3,
  "Public data. **Long-running ads are the ones that work.** Structured into a table"),
 ("Meta ads", "Ad copy variants in volume", "Chat", 3,2,4,4,5,2,
  "The commodity use. **You are the media buyer** — the constraint is which to run"),
 ("Meta ads", "Creative concepts and video scripts", "Chat", 4,3,4,3,5,2,
  "`FIT`=3. You judge creative better than any agent can"),
 ("Meta ads", "Weekly account read — frequency, hook rate, CPM drift", "Code", 4,3,5,4,4,3,
  "You can do this yourself. The gain is doing it weekly without losing an evening"),
 ("Meta ads", "Policy pre-check before submitting", "Chat", 3,3,3,4,5,2,
  "Especially the **Employment Special Ad Category** trap in `SUPPLY-DEMAND.md` §1"),
 ("Meta ads", "Budget pacing and reallocation rules", "Code", 3,4,3,4,3,4,
  "A script that reads the export and says where the money should move"),

 # ---- 4. Cold email and outbound ---------------------------------------
 ("Outbound", "Build the prospect list — agencies and e-comm brands", "Code", 5,5,5,5,5,5,
  "Public sources: job boards, company sites, the Ad Library. **Respect each site's "
  "terms.** This is the same pipeline as the intent seed, pointed at contacts"),
 ("Outbound", "Deliverability setup — SPF, DKIM, DMARC, warm-up, domain choice", "Code", 5,4,4,5,5,5,
  "**Do not send from `allhandstalent.com`.** Use a separate sending domain so a "
  "deliverability problem never touches the domain your ads land on. This is exactly the "
  "kind of setup that is checkable, and expensive to get wrong quietly"),
 ("Outbound", "Sequence writing — first touch, follow-ups, breakup", "Chat", 4,4,4,4,5,4,
  "Draft fast, iterate on replies"),
 ("Outbound", "Per-prospect personalisation at volume", "Code", 4,4,5,4,4,4,
  "One line each, drawn from their live ads or their job postings. **This is what makes "
  "cold email work**, and it is the part that does not scale by hand"),
 ("Outbound", "Reply triage and routing", "Cowork", 3,3,4,4,4,3,
  "Interested / not now / never, and the right response to each"),
 ("Outbound", "LinkedIn outbound", "Chat", 3,3,3,4,4,2,
  "Message drafting only. **Do not automate or scrape it** — the terms forbid it and the "
  "account is your face"),

 # ---- 5. Sales ----------------------------------------------------------
 ("Sales", "Turn the paid teardown into a repeatable generator", "Code", 5,5,5,4,5,5,
  "The **money gate** (`OFFER.md` §9.1). Their ad export in, structured teardown out. "
  "**Turns a bespoke service into a 30-minute product**"),
 ("Sales", "Pre-call research brief on every prospect", "Code", 4,4,5,5,5,4,
  "Their site, live ads, job postings, current creative. One page, every time"),
 ("Sales", "Call script, discovery questions, objection handling", "Chat", 4,4,3,4,5,4,
  "Especially the **India objection** — `COUNTRIES.md` §9 already prices it"),
 ("Sales", "Proposal and follow-up from call notes", "Cowork", 3,3,4,4,4,4,
  "Same structure every time. **Same-day beats three-days-later**"),
 ("Sales", "Pipeline tracking", "Cowork", 3,3,3,4,4,4,
  "A sheet until roughly deal thirty. Not a CRM purchase"),
 ("Sales", "Pricing and negotiation prep", "Chat", 4,4,2,4,4,3,
  "Know your floor before the call. The model already tells you what it is"),

 # ---- 6. Supply and recruiting -----------------------------------------
 ("Supply", "Build the grading rubric as a scoring tool", "Code", 5,5,4,4,5,5,
  "`MODEL-V2.md` gap 6. **Recut an ad, measure 3s and 15s retention against the "
  "original.** Same computation every time — that consistency *is* the product"),
 ("Supply", "The graded directory, v0", "Code", 5,5,4,5,4,5,
  "`HUNGRY.md` §9's retention mechanism — worth **+$9,022 per client**. A sheet and a "
  "script until placement thirty"),
 ("Supply", "Sourcing lists from public portfolios and showreels", "Code", 4,4,5,4,5,4,
  "Where the terms permit it. The rest by hand"),
 ("Supply", "Design the take-home brief and its scoring sheet", "Cowork", 4,4,4,4,4,5,
  "One brief, one rubric, consistent scores"),
 ("Supply", "Screening — CVs and reels against the rubric", "Chat", 4,3,5,3,5,2,
  "`FIT`=3. It can sort and shortlist. **You watch the reel**"),
 ("Supply", "Interview structure and reference-check questions", "Cowork", 3,3,3,4,4,5,
  "Written once, used forever"),
 ("Supply", "Candidate outreach and nurture", "Chat", 3,3,4,4,4,3,
  "Volume with personalisation"),
 ("Supply", "Offer letters and candidate contracts", "Cowork", 4,3,4,3,4,5,
  "**Draft only** — see §4"),

 # ---- 7. Delivery and client success -----------------------------------
 ("Delivery", "Onboarding checklist and the 30/60/90 cadence", "Cowork", 5,4,3,4,4,5,
  "Protects **seat continuity, the largest single lever in the business**. Build it "
  "before placement one"),
 ("Delivery", "Check-in prompts and QBR packs", "Cowork", 3,3,4,4,3,5,
  "The mechanism that turns 9 EOR months into 30"),
 ("Delivery", "Replacement workflow under the 12-month guarantee", "Cowork", 3,3,3,4,3,4,
  "Cheapest differentiation you have. It has to be fast or it costs more than it should"),
 ("Delivery", "Expansion play — second and third seat in the same client", "Chat", 4,5,2,4,3,3,
  "Seats-per-client is where the economics actually live"),

 # ---- 8. Finance --------------------------------------------------------
 ("Finance", "Unit economics and the live dashboard", "Code", 4,4,4,5,4,5,
  "Placements, seats, MRR, churn, cash. **A script that reads your sheet**, not a SaaS"),
 ("Finance", "Cash-flow forecast — you pay talent before clients pay you", "Code", 5,5,3,5,5,4,
  "**The failure mode that kills placement businesses.** EOR means salaries leave "
  "monthly while fees arrive lumpily. Model it before it bites"),
 ("Finance", "Invoicing, collections and the EOR monthly run", "Cowork", 3,3,4,4,3,4,
  "$477/employee/month recurring. Small now; the process has to exist before it is twenty"),
 ("Finance", "FX exposure — INR cost base, USD revenue", "Code", 3,4,2,4,3,3,
  "A real margin variable that nothing in the repo currently models"),
 ("Finance", "Bookkeeping prep for an accountant", "Cowork", 2,2,4,4,3,4,
  "Categorise and reconcile. **The accountant still files**"),

 # ---- 9. Legal and compliance ------------------------------------------
 ("Legal", "Draft the placement agreement, guarantee and EOR schedule", "Cowork", 5,4,5,3,5,5,
  "**Draft only.** Arriving with a complete draft cuts the bill and the turnaround — "
  "that is the real saving, and it is large"),
 ("Legal", "USPTO Class 35 position on *All Hands*", "Code", 4,4,4,4,5,3,
  "Still outstanding, and **two live users of *All Hands* in talent services** were "
  "found. **Monitoring is agent work; the clearance opinion is not**"),
 ("Legal", "NDAs, IP assignment, contractor terms", "Cowork", 4,3,4,3,4,5,
  "Draft only. IP assignment matters — you are selling creative output"),
 ("Legal", "Privacy basics if you take EU or UK clients", "Chat", 3,3,3,3,3,3,
  "Know what you are walking into before you sell into it"),

 # ---- 10. Ops and admin -------------------------------------------------
 ("Ops", "SOPs for everything you do twice", "Cowork", 4,4,4,4,4,5,
  "**The substitute for employees.** Every SOP written now is what you hand a VA later "
  "instead of explaining it"),
 ("Ops", "Tool stack decisions and integrations", "Chat", 3,3,3,4,4,2,
  "You have already done four of these"),
 ("Ops", "Recurring monitors — competitor pricing, salary benchmarks", "Code", 3,3,5,5,3,5,
  "Scheduled diffs. **Runs without your attention**, which is the scarce input"),
 ("Ops", "Inbox and calendar triage", "Cowork", 2,2,4,3,4,2,
  "Low value while volume is low. Real by month six"),

 # ---- 11. Media and content --------------------------------------------
 ("Media", "Case studies from the first placements", "Cowork", 4,4,4,4,3,4,
  "**Only with real numbers.** A fabricated case study is worse than none when the "
  "positioning is *falsifiable*"),
 ("Media", "X during launch month", "Chat", 2,2,4,4,4,1,
  "`MODEL-V2.md` gap 11 caps this deliberately. **X only at launch**"),
 ("Media", "Newsletter from month three", "Cowork", 3,3,4,4,2,3,
  "First number from your **first ten placements**, not from research"),
 ("Media", "Your own LinkedIn presence", "Chat", 3,3,3,4,4,2,
  "For an unknown operator this is a real trust asset"),

 # ---- 12. Hiring your first person -------------------------------------
 ("Hiring", "Scope, JD and screening for the first VA or recruiter", "Cowork", 4,4,3,4,2,5,
  "Month four to six. **The SOPs above are what makes this hire cheap**"),
 ("Hiring", "Training material from your own SOPs", "Cowork", 3,4,4,4,2,5,
  "Written once, reused per hire"),
]

DONT = [
 ("**The sales call itself**", "Trust is bought in conversation, and you have no track "
  "record to lean on", "Brief before, follow-up after"),
 ("**Grading the creative**", "`FOUNDERGRADE` is *why video was chosen* — you can judge "
  "it with no team. An agent cannot", "Build the scoring sheet. **You score**"),
 ("**Legal, tax and immigration authority**", "India EOR compliance, contract "
  "enforceability, the trademark opinion. A confident wrong answer is expensive and slow "
  "to unwind", "Draft so the professional reviews rather than writes"),
 ("**LinkedIn automation or scraping**", "The terms forbid it and the account is your "
  "face in a trust business", "Draft messages; send them yourself"),
 ("**Sending cold email from your main domain**", "One deliverability incident and the "
  "domain your ads land on is damaged", "A separate sending domain, warmed properly"),
 ("**Inventing a number**", "The two worst errors in this repo came from exactly that — "
  "a hand-written `SAYS` dict and a `CLEAR` score inferred from my own prose",
  "Mark it `[?]` and go measure it"),
 ("**Deciding**", "Every screen here narrows options. **It has reversed itself four "
  "times** — the domain, the platform, the code-vs-Framer score, whether *All Hands* was "
  "clean", "Use it to make the choice legible. You still make it"),
]


def main():
    W = dict(DIM)

    def sc(i, v, t, f, n, r):
        d = {"IMPORTANCE": i, "VALUE": v, "TIMESAVED": t, "FIT": f, "NOW": n, "REUSE": r}
        return sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100

    rows = sorted([(sc(i, v, t, f, n, r), fn_, act, sur, i, v, t, f, n, r, why)
                   for fn_, act, sur, i, v, t, f, n, r, why in A], key=lambda x: -x[0])

    L = []
    P = L.append
    P("# Every Function, Across Code, Cowork and Chat\n")
    P("> *\"All the things — website to ads to cold email to whatever else. I won't have "
      "employees.\"*\n")
    P(f"**{len(A)} activities across {len(set(x[0] for x in A))} functions**, each placed on a "
      "surface and scored on\nyour criteria: `IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · "
      "`FIT` 16 · `NOW` 12 · `REUSE` 6.\n")
    P("**`FIT` is what keeps this honest** — it scores how well an agent does the task *versus "
      "you doing\nit*. It is why screening reels scores 3 and building the scraper scores 5, "
      "and why the sales call\nis not in the table at all.\n")

    P("---\n\n## 1. Which surface, and why\n")
    P("Assignment is by **task shape**, not by feature list — feature lists move, shapes do "
      "not.\n")
    P("| Surface | Use when the output is | Because |")
    P("|---|---|---|")
    P("| **Code** | a runnable tool, a data pipeline, or a **verified fact** | It can *check* "
      "rather than assert — RDAP calls, corpus frequencies, HTTP fetches, a sample-size "
      "calculation. It leaves a script that keeps paying |")
    P("| **Cowork** | a document, sheet or deck — or repeated ops work over business files | "
      "The output is the artefact itself, and it lives in a folder you keep, not a chat you "
      "lose |")
    P("| **Chat** | a judgement, a draft, or an answer you use in ten minutes | Fastest loop, "
      "and the only one where you can **show it something and ask what it sees** |")
    P("")

    P("---\n\n## 2. Ranked — all " + str(len(A)) + "\n")
    P("| # | Function | Activity | Surface | Imp | Val | Time | Fit | Now | Re | Score | Why |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for k, (s, fn_, act, sur, i, v, t, f, n, r, why) in enumerate(rows, 1):
        P(f"| {k} | {fn_} | {act} | **{sur}** | {i} | {v} | {t} | {f} | {n} | {r} | "
          f"**{s:.0f}** | {why} |")
    P("")

    P("### The top ten, and what they have in common\n")
    for s, fn_, act, sur, *_ in rows[:10]:
        P(f"1. **{act}** — {fn_} · `{sur}` · {s:.0f}")
    P("")
    top10 = rows[:10]
    code10 = sum(1 for x in top10 if x[3] == "Code")
    P(f"**{code10} of the top 10 are Code**, and the pattern is consistent: the highest-value "
      "work is\n**building something that runs repeatedly** — the audience pipeline, the "
      "teardown generator, the\ngrading tool, the model itself. Writing copy sits mid-table. "
      "**The obvious uses are the\nlow-leverage ones.**\n")

    P("---\n\n## 3. By function\n")
    order = []
    for fn_, *_ in A:
        if fn_ not in order:
            order.append(fn_)
    for fn_ in order:
        items = sorted([x for x in rows if x[1] == fn_], key=lambda x: -x[0])
        best = items[0]
        P(f"**{fn_}** — {len(items)} activities, top: *{best[2]}* (`{best[3]}`, {best[0]:.0f})  ")
    P("")

    P("---\n\n## 4. What not to use any of them for\n")
    P("| Do not | Why | Instead |\n|---|---|---|")
    for t, why, instead in DONT:
        P(f"| {t} | {why} | {instead} |")
    P("")

    P("---\n\n## 5. The split\n")
    tot = {}
    val = {}
    for s, fn_, act, sur, *rest in rows:
        tot[sur] = tot.get(sur, 0) + 1
        val[sur] = val.get(sur, 0) + s
    n = len(rows)
    vsum = sum(val.values())
    P("| Surface | Activities | Share of activities | Share of total score | Avg score |")
    P("|---|---|---|---|---|")
    for sur in ("Code", "Cowork", "Chat"):
        P(f"| **{sur}** | {tot[sur]} | **{tot[sur]/n:.0%}** | **{val[sur]/vsum:.0%}** | "
          f"{val[sur]/tot[sur]:.1f} |")
    P("")
    P(f"> **Roughly {tot['Code']/n:.0%} Code · {tot['Cowork']/n:.0%} Cowork · "
      f"{tot['Chat']/n:.0%} Chat by count — but "
      f"{val['Code']/vsum:.0%} / {val['Cowork']/vsum:.0%} / {val['Chat']/vsum:.0%} by "
      f"weighted value.**\n")
    P("Read the averages, not the counts. **Code carries the highest average score** because "
      "the things\nworth doing more than once end up there. Chat has the most *moments* and "
      "the least accumulated\nvalue — it is where you think, not where you build. Cowork sits "
      "between: it is where the\n**documents that substitute for employees** live — SOPs, "
      "contracts, onboarding, case studies.\n")
    P("### How to actually run it\n")
    P("| | |\n|---|---|")
    P("| **Code, in this repo, once or twice a week** | Long sessions. Build pipelines and "
      "tools, and re-run the model against real numbers. This is where the compounding is |")
    P("| **Cowork, as the filing cabinet that does work** | Every SOP, contract, checklist and "
      "case study. **These are what you hand your first hire instead of explaining** |")
    P("| **Chat, many times a day** | Copy, judgement calls, *look at this and tell me what is "
      "wrong*. Cheapest loop, lowest half-life |")
    P("")
    P("**The one habit worth more than the split:** ask it to argue with you. The four most "
      "useful\nmoments in this project were reversals — the `.com` namespace, the code-vs-"
      "Framer score, the\nunbreakability re-weight, and finding *All Hands* was not clean in "
      "recruiting after I had said it\nwas.\n")
    open(OUT, "w").write("\n".join(L))
    print(f"{len(A)} activities")
    for sur in ("Code", "Cowork", "Chat"):
        print(f"  {sur:7s} {tot[sur]:2d} ({tot[sur]/n:.0%})  value share {val[sur]/vsum:.0%}  "
              f"avg {val[sur]/tot[sur]:.1f}")
    print("\ntop 10:")
    for s, fn_, act, sur, *_ in rows[:10]:
        print(f"  {s:5.1f} {sur:7s} {fn_:9s} {act[:56]}")


if __name__ == "__main__":
    main()
