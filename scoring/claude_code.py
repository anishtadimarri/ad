#!/usr/bin/env python3
"""
What to use Claude Code for while building All Hands Talent, ranked by leverage.

The question was "tell me every activity" and "I want to use every last credit". So this
is deliberately exhaustive rather than a top-five, and it is scored rather than listed,
because **the ranking is the useful part** -- most of the obvious uses (writing copy,
drafting posts) are the low-leverage ones, and the highest-leverage use is invisible
until you look at what this repo already is.

Scored on the operator's own stated criteria -- "importance + time saved + value added":

  IMPORTANCE  24  does it matter to the business at all
  VALUE       22  dollars, or the quality of a decision
  TIMESAVED   20  founder-hours, which is the actually scarce input
  FIT         16  how well an agent does this *versus the operator doing it*
  NOW         12  "esp in first few months"
  REUSE        6  leaves a reusable asset, or evaporates after one use

FIT is what stops this being a wish list. An agent being *able* to do something is not
the same as it being the better tool for it.

GATE: FIT < 3 is dropped from the ranking and listed in section 4 instead. An agent
being *able* to do something is not the same as it being the right tool -- and the two
places that matter most here are creative judgement and anything with legal authority.

Run:  python3 scoring/claude_code.py > /dev/null   (writes CLAUDE-CODE.md)
"""

OUT = "CLAUDE-CODE.md"

# Scored on the operator's own criteria, in their words:
#   "importance + time saved + value added + etc"
DIM = [("IMPORTANCE", 24),   # does it matter to the business at all
       ("VALUE",      22),   # dollars, or the quality of a decision
       ("TIMESAVED",  20),   # founder-hours, the actually scarce input
       ("FIT",        16),   # how well an agent does it VERSUS the operator
       ("NOW",        12),   # "esp in first few months"
       ("REUSE",       6)]   # leaves a reusable asset, or evaporates

# (area, task, IMPORTANCE, VALUE, TIMESAVED, FIT, NOW, REUSE, note)
USES = [
    # --- keeping the model live -------------------------------------------
    ("Model", "**Replace the model's assumptions with real numbers, monthly**", 5, 5, 4, 5, 5, 5,
     "The single highest-leverage use, and the least obvious. [`funnel.py`](scoring/funnel.py) "
     "runs on **assumed** CPM, CTR, LP conversion, deposit take-up and fill rate — steps 6–9 "
     "are marked as assumptions because no data existed. After month one they are not "
     "assumptions any more. Feed the actuals in, re-run, and **every downstream number in "
     "[`LTGP.md`](LTGP.md) and [`MODEL-V2.md`](MODEL-V2.md) updates at once**"),
    ("Model", "Recompute CAC by audience and kill the losing leg", 5, 5, 4, 5, 5, 4,
     "The model splits spend 25/45/30 across intent seed, lookalike and broad at $489 / $817 / "
     "$1,070. **Those are predictions.** One month of real data tells you which to defund"),
    ("Model", "Weekly \"what changed and what it means\" report", 4, 3, 5, 5, 5, 4,
     "Export Meta and Stripe, run one command, get the deltas plus the second-order effect on "
     "the 30-day ratio. Ten minutes replacing an afternoon"),
    ("Model", "Cohort and payback analysis once placements exist", 4, 4, 4, 5, 3, 4,
     "Seat continuity is worth **+$9,022 per client** across 9→30 EOR months. You cannot "
     "manage that without cohorts, and cohorts are a scripting job"),
    ("Model", "Stress-test decisions before committing spend", 4, 4, 4, 5, 5, 3,
     "*\"What if deposit take-up is 12% not 24%?\"* is a one-line change and a re-run, not a "
     "guess. The repo is already built to answer that shape of question"),

    # --- demand ------------------------------------------------------------
    ("Demand", "**Build the intent-seed audience by scraping job postings**", 5, 5, 5, 5, 5, 5,
     "[`TARGETING.md`](TARGETING.md)'s whole thesis. It is **25% of spend at the best CAC in "
     "the model — $489, 9.07:1** — and it is a scraping, dedupe and CSV-export job, which is "
     "exactly agent work. Rebuild it monthly so the signal stays dated"),
    ("Demand", "Count job postings across every phrasing before writing the ad", 4, 4, 4, 5, 5, 2,
     "[`MODEL-V2.md`](MODEL-V2.md) gap 10: if agencies post *video editor* and never "
     "*performance video editor*, the audience build misses them. Flagged there as **free, one "
     "afternoon** — this is that afternoon"),
    ("Demand", "Pull competitor ads from the Meta Ad Library and map the angles", 3, 4, 5, 5, 5, 3,
     "Public data. Which competitors run what, for how long — long-running ads are the ones "
     "that work. Structured into a table you can actually act on"),
    ("Demand", "Generate ad copy variants in volume", 3, 2, 4, 4, 5, 2,
     "Useful and genuinely the *commodity* use. **You are the media buyer** — the constraint "
     "is your judgement of which to run, not the supply of lines"),
    ("Demand", "Landing-page copy for `/agencies`, `/ecommerce`, `/teardown`", 5, 4, 4, 4, 5, 3,
     "The words are what convert, and the model's specifics — the **$5,000–16,500/mo vendor "
     "invoice** comparator, the 12-month guarantee, the paid teardown — have to become "
     "sentences. Draft here, paste into Framer"),
    ("Demand", "Read the Meta export and tell you what to change", 4, 3, 5, 4, 4, 3,
     "Frequency, placement breakdown, hook rate, CPM drift. You can read this yourself — the "
     "gain is doing it every week without it costing an evening"),

    # --- the offer ---------------------------------------------------------
    ("Offer", "**Turn the paid teardown into a repeatable generator**", 5, 5, 5, 4, 5, 5,
     "The teardown is the **money gate** ([`OFFER.md`](OFFER.md) §9.1) and the thing that "
     "funds the search. Build a template that takes their ad export and produces a structured "
     "teardown. **It turns a bespoke service into a 30-minute product**, which is what makes "
     "it scale past ten clients"),
    ("Offer", "Pre-call research brief on every prospect", 4, 4, 5, 5, 5, 4,
     "Their site, their live ads, their job postings, their current creative — one page, "
     "before every call. Cheap, repeatable, and it is the difference between a cold call and "
     "an informed one"),
    ("Offer", "Proposal and follow-up generator off the call notes", 3, 3, 4, 4, 4, 4,
     "Same structure every time, filled from notes. Speed matters here — proposals sent same-"
     "day close better than ones sent in three days"),
    ("Offer", "Draft the placement agreement, guarantee terms and EOR schedule", 5, 4, 5, 3, 5, 5,
     "**Draft only.** A lawyer must review before anything is signed — but arriving with a "
     "complete draft cuts the bill and the turnaround substantially. See §4"),

    # --- supply ------------------------------------------------------------
    ("Supply", "**Build the grading rubric as an actual scoring tool**", 5, 5, 4, 4, 5, 5,
     "[`MODEL-V2.md`](MODEL-V2.md) gap 6: *premium* is currently an adjective. The fix is one "
     "test — **recut an existing ad, measure 3-second and 15-second retention against the "
     "original**. Turn that into a scoring sheet that computes the grade identically every "
     "time. **This is what makes the claim falsifiable**, and it doubles as the sales asset"),
    ("Supply", "Sourcing lists from public portfolios and showreels", 4, 4, 5, 4, 5, 4,
     "Public portfolio sites, showreel platforms, public communities. **Respect each site's "
     "terms** — some explicitly forbid scraping, and LinkedIn in particular. Build the list "
     "where it is permitted and do the rest by hand"),
    ("Supply", "Design and auto-score the take-home brief", 4, 4, 4, 4, 4, 5,
     "One brief, one rubric, consistent scoring. The consistency *is* the product — it is what "
     "you are selling to the buyer"),
    ("Supply", "The graded directory, v0 — a tracker, not a platform", 5, 5, 4, 5, 4, 5,
     "[`HUNGRY.md`](HUNGRY.md) §9's retention mechanism. **It is a spreadsheet and a script "
     "until roughly placement thirty**, not software. Build the cheap version now and it "
     "starts compounding immediately"),
    ("Supply", "Outreach sequences to graded candidates", 3, 3, 4, 4, 4, 3,
     "Volume with personalisation. Fine work for an agent, moderate leverage"),

    # --- delivery and ops --------------------------------------------------
    ("Ops", "Placement onboarding checklist and the 30/60/90 cadence", 5, 4, 3, 4, 4, 5,
     "The thing that protects **seat continuity — the largest single lever in the business**. "
     "Systematise it before placement one, not after placement five"),
    ("Ops", "Invoicing, payment tracking and the EOR monthly run", 3, 3, 4, 4, 3, 4,
     "EOR is $477/employee/month recurring. Small numbers now, but the tracking has to exist "
     "before it is twenty employees"),
    ("Ops", "A one-page internal dashboard", 4, 4, 4, 5, 4, 5,
     "Placements, seats per client, MRR, churn, cash. **Not a SaaS purchase** — a script that "
     "reads your sheet and prints the six numbers you actually steer by"),
    ("Ops", "Replacement-request workflow under the 12-month guarantee", 3, 3, 3, 4, 3, 4,
     "The guarantee is the cheapest differentiation you have; the process behind it has to be "
     "fast or the guarantee costs more than it should"),

    # --- media and content -------------------------------------------------
    ("Media", "The `/proof` page write-ups", 5, 5, 3, 4, 5, 4,
     "**The most important page on the site.** Each recut ad, with the retention delta stated. "
     "This is where *premium* stops being an adjective"),
    ("Media", "Case studies from the first placements", 4, 4, 4, 4, 3, 4,
     "Month two onward, and only with real numbers. A fabricated case study is worse than none "
     "when your entire positioning is *falsifiable*"),
    ("Media", "X posts during launch month", 2, 2, 4, 4, 4, 1,
     "[`MODEL-V2.md`](MODEL-V2.md) gap 11 caps this deliberately: **X only at launch**, "
     "newsletter at month three. Your attention is the scarce input, not your posting volume"),
    ("Media", "The newsletter, from month three", 3, 3, 4, 4, 2, 3,
     "Gap 11 again — and the first issue's number should come **from your first ten "
     "placements**, not from research"),

    # --- research and monitoring -------------------------------------------
    ("Research", "Monitor competitor pricing pages for changes", 3, 3, 5, 5, 3, 5,
     "[`COMPETITOR-DATA.md`](COMPETITOR-DATA.md) is a snapshot. A scheduled diff turns it into "
     "a live feed, and pricing moves are the ones that matter"),
    ("Research", "Refresh salary benchmarks before repricing", 4, 4, 4, 5, 2, 4,
     "The whole model rests on the **$1,650/mo talent cost** and the fee being 30% of "
     "first-year comp. Both drift"),
    ("Research", "Track the USPTO Class 35 position on *All Hands*", 4, 4, 4, 4, 5, 3,
     "Still outstanding, and **two live users of *All Hands* in talent services** were found. "
     "Monitoring is agent work; **the clearance opinion is not** — see §4"),
    ("Research", "Country and role expansion screens, when the time comes", 4, 4, 5, 5, 2, 5,
     "Exactly what [`COUNTRIES.md`](COUNTRIES.md) and [`MAP.md`](MAP.md) already are. Re-run "
     "the same machinery against new questions rather than starting over"),

    # --- the repo itself ---------------------------------------------------
    ("Repo", "Keep this repository as the decision record", 4, 5, 3, 5, 5, 5,
     "Every screen here is a **runnable model, not a memo**. That is why the recommendation "
     "could reverse three times in one conversation without losing the reasoning. Keep adding "
     "to it and the compounding is real"),
]

# (task, why not, what to do instead)
DONT = [
    ("**Grading the creative work itself**",
     "[`LAUNCH.md`](LAUNCH.md) introduced `FOUNDERGRADE` for exactly this: **can the operator "
     "personally judge the output with no team.** Video *was chosen* because you can. An agent "
     "cannot tell you whether a recut is actually better",
     "Use it to build the scoring sheet. **You supply the score**"),
    ("**The sales call**",
     "The whole model rests on a buyer trusting an unknown operator. That is bought in "
     "conversation",
     "Pre-call brief and post-call follow-up — the parts either side"),
    ("**Legal and tax authority**",
     "India EOR compliance, US contract enforceability, the Class 35 trademark opinion. **A "
     "confident wrong answer here is expensive and slow to unwind**",
     "Draft everything so the professional is reviewing rather than writing. That is the real "
     "saving, and it is large"),
    ("**Scraping anything whose terms forbid it**",
     "LinkedIn is the obvious one. Convenience is not a defence, and your business depends on "
     "the account",
     "Public job boards, public portfolios, the Meta Ad Library, company sites. There is "
     "plenty that is permitted"),
    ("**Inventing a number to fill a gap**",
     "This repo's rule throughout. Two of the worst errors in it came from exactly that — a "
     "hand-written `SAYS` dictionary and a `CLEAR` score inferred by regexing my own prose",
     "Mark it `[?]`, and go and measure it"),
    ("**Deciding what to do**",
     "Every screen here narrows options and prices trade-offs. **It has been wrong and "
     "reversed itself repeatedly** — on the domain, on the platform, on whether All Hands was "
     "clean",
     "Use it to make the choice legible. You still make it"),
]

PHASES = [
    ("Weeks 0–2 · before a dollar is spent", [
        "Landing-page copy for `/agencies`, `/ecommerce`, `/teardown`",
        "**Count job postings across all three phrasings** — this decides the ad, and it is free",
        "**Build the intent-seed audience** from job postings and export the CSV",
        "Meta Ad Library sweep — who is running what, and for how long",
        "The teardown generator, so the money gate is a product on day one",
        "The grading rubric as a scoring sheet",
        "Draft the placement agreement and guarantee for a lawyer to review",
    ]),
    ("Weeks 2–8 · first spend, first placements", [
        "**Feed real CPM, CTR, LP conversion and deposit take-up into `funnel.py`** and re-run "
        "everything downstream",
        "Weekly what-changed report",
        "Pre-call research brief before every single call",
        "`/proof` write-ups as the first recuts land",
        "Placement onboarding checklist and the 30/60/90 cadence",
        "Graded directory v0 — a sheet and a script",
    ]),
    ("Months 3–6 · does it compound", [
        "Cohort and payback analysis; **defund the losing audience leg**",
        "Case studies with real numbers",
        "`/talent` page, footer-only and `noindex`, with the pass rate on it",
        "Newsletter, first number drawn from the first ten placements",
        "The internal dashboard",
        "Scheduled competitor-pricing diffs",
        "Second-role and second-country screens, reusing the existing machinery",
    ]),
]

HOW = [
    ("**Work inside this repo**",
     "It already holds the model, the funnel, the offer, the countries and every decision with "
     "its reasoning. An agent with that context gives a different quality of answer than one "
     "starting cold — most of what makes this useful is the context, not the model"),
    ("**Build scripts, not answers**",
     "Ask for a *runnable screen* rather than a reply. Every file in `scoring/` was written "
     "once and re-run many times as inputs changed. **An answer is spent when you read it; a "
     "script keeps paying**"),
    ("**Batch into long sessions**",
     "One two-hour session on \"build the intent-seed pipeline\" produces far more than "
     "twenty scattered questions, because context accumulates within a session and resets "
     "between them"),
    ("**Make it check rather than assert**",
     "The most valuable things in this repo came from *checking*: RDAP calls, Datamuse corpus "
     "frequencies, HTTP fetches of competitor sites, a two-proportion sample-size calculation. "
     "**\"Go and verify\" beats \"what do you think\"** almost every time"),
    ("**Schedule the recurring ones**",
     "Competitor pricing diffs, posting-count refreshes, the weekly model re-run. Set them up "
     "once as scheduled jobs and they run without your attention, which is the scarce input"),
    ("**Ask it to argue with you**",
     "The three most useful moments in this whole engagement were reversals: the `.com` "
     "namespace, the Claude-Code-vs-Framer score, and finding that *All Hands* is not clean in "
     "recruiting after I had said it was. **Ask what would have to be true for the opposite to "
     "be right**"),
]


def main():
    W = dict(DIM)

    def sc(imp, val, ts, fit, now, reuse):
        d = {"IMPORTANCE": imp, "VALUE": val, "TIMESAVED": ts, "FIT": fit,
             "NOW": now, "REUSE": reuse}
        return sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100

    rows = [(sc(i, v, t2, f, n, r), a, t, i, v, t2, f, n, r, why)
            for a, t, i, v, t2, f, n, r, why in USES]
    rows.sort(key=lambda x: (-x[0], x[1]))

    L = []
    A = L.append
    A("# Claude Code, Applied to All Hands Talent\n")
    A("> *\"Tell me all the activities. I want to use every last credit.\"*\n")
    A(f"**{len(USES)} uses, scored and ranked**, plus {len(DONT)} things not to use it for. The "
      "ranking is the point:\n**most of the obvious uses are the low-leverage ones.** Writing "
      "ad copy scores mid-table. The\nhighest-scoring use is one that only becomes visible "
      "once you notice what this repository already\nis.\n")

    A("---\n\n## 1. The one that matters most\n")
    A("**Everything in this repo runs on assumptions.** [`funnel.py`](scoring/funnel.py) says "
      "so explicitly —\nsteps 1–5 are benchmarked against real Meta data, **steps 6–9 are "
      "assumptions, because no data\nexisted until the first campaign ran**. Deposit take-up, "
      "fill rate, hold rate: all marked `[?]`.\n")
    A("From week three, they are not assumptions any more. And because every screen is a "
      "**runnable\nmodel rather than a memo**, feeding four real numbers into one file "
      "re-derives the CAC, the 30-day\nratio, the lifetime ratio, the audience split and the "
      "scale arithmetic **in one command**.\n")
    A("> **That is the compounding use.** Not writing copy — copy is a commodity and you are "
      "the media\n> buyer. The compounding use is that the model gets *more true every month*, "
      "and it tells you which\n> audience to defund and which lever to pull while the answer "
      "still matters.\n")

    A("---\n\n## 2. Everything, ranked\n")
    A("Your criteria, weighted: **`IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · "
      "`FIT` 16 · `NOW` 12 · `REUSE` 6.**\n`FIT` is what stops this being a wish list — it scores **how well an agent does the task *versus\nyou* doing it**, which is why drafting contracts scores 3 and generating ad copy scores 4.\n")
    A("| # | Area | Use | Imp | Value | Time | Fit | Now | Reuse | Score | Why |")
    A("|---|---|---|---|---|---|---|---|---|---|---|")
    for k, (sv, a, t, i, v, t2, f, n, r, why) in enumerate(rows, 1):
        A(f"| {k} | {a} | {t} | {i} | {v} | {t2} | {f} | {n} | {r} | **{sv:.0f}** | {why} |")
    A("")
    top = rows[:6]
    A("### The six that carry it\n")
    for sv, a, t, *_ in top:
        A(f"- **{t}** — {a} · {sv:.0f}")
    A("")
    A("Note the shape: **three of the six are about measuring rather than making.** Building "
      "the intent-seed\naudience, turning the teardown into a product, and keeping the model "
      "honest all beat every content\ntask on the board.\n")

    A("---\n\n## 3. By phase\n")
    for title, items in PHASES:
        A(f"### {title}\n")
        for it in items:
            A(f"- {it}")
        A("")

    A("---\n\n## 4. What not to use it for\n")
    A("| Do not | Why | Instead |\n|---|---|---|")
    for t, why, instead in DONT:
        A(f"| {t} | {why} | {instead} |")
    A("")

    A("---\n\n## 5. How to actually spend the plan\n")
    A("| | |\n|---|---|")
    for t, why in HOW:
        A(f"| {t} | {why} |")
    A("")
    A("*One caveat on the plan itself: usage allowances change, and I have not verified the "
      "current limits\nfor your tier — so nothing above assumes a specific quota. The advice "
      "is about **what produces the\nmost per session**, which holds regardless.*\n")
    open(OUT, "w").write("\n".join(L))
    print(f"{len(USES)} uses scored")
    for sv, a, t, *_ in rows[:10]:
        print(f"  {sv:5.1f}  {a:9s} {t[:66]}")


if __name__ == "__main__":
    main()
