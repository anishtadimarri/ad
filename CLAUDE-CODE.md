# Claude Code, Applied to All Hands Talent

> *"Tell me all the activities. I want to use every last credit."*

**33 uses, scored and ranked**, plus 6 things not to use it for. The ranking is the point:
**most of the obvious uses are the low-leverage ones.** Writing ad copy scores mid-table. The
highest-scoring use is one that only becomes visible once you notice what this repository already
is.

---

## 1. The one that matters most

**Everything in this repo runs on assumptions.** [`funnel.py`](scoring/funnel.py) says so explicitly —
steps 1–5 are benchmarked against real Meta data, **steps 6–9 are assumptions, because no data
existed until the first campaign ran**. Deposit take-up, fill rate, hold rate: all marked `[?]`.

From week three, they are not assumptions any more. And because every screen is a **runnable
model rather than a memo**, feeding four real numbers into one file re-derives the CAC, the 30-day
ratio, the lifetime ratio, the audience split and the scale arithmetic **in one command**.

> **That is the compounding use.** Not writing copy — copy is a commodity and you are the media
> buyer. The compounding use is that the model gets *more true every month*, and it tells you which
> audience to defund and which lever to pull while the answer still matters.

---

## 2. Everything, ranked

Your criteria, weighted: **`IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · `FIT` 16 · `NOW` 12 · `REUSE` 6.**
`FIT` is what stops this being a wish list — it scores **how well an agent does the task *versus
you* doing it**, which is why drafting contracts scores 3 and generating ad copy scores 4.

| # | Area | Use | Imp | Value | Time | Fit | Now | Reuse | Score | Why |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Demand | **Build the intent-seed audience by scraping job postings** | 5 | 5 | 5 | 5 | 5 | 5 | **100** | [`TARGETING.md`](TARGETING.md)'s whole thesis. It is **25% of spend at the best CAC in the model — $489, 9.07:1** — and it is a scraping, dedupe and CSV-export job, which is exactly agent work. Rebuild it monthly so the signal stays dated |
| 2 | Offer | **Turn the paid teardown into a repeatable generator** | 5 | 5 | 5 | 4 | 5 | 5 | **97** | The teardown is the **money gate** ([`OFFER.md`](OFFER.md) §9.1) and the thing that funds the search. Build a template that takes their ad export and produces a structured teardown. **It turns a bespoke service into a 30-minute product**, which is what makes it scale past ten clients |
| 3 | Model | **Replace the model's assumptions with real numbers, monthly** | 5 | 5 | 4 | 5 | 5 | 5 | **96** | The single highest-leverage use, and the least obvious. [`funnel.py`](scoring/funnel.py) runs on **assumed** CPM, CTR, LP conversion, deposit take-up and fill rate — steps 6–9 are marked as assumptions because no data existed. After month one they are not assumptions any more. Feed the actuals in, re-run, and **every downstream number in [`LTGP.md`](LTGP.md) and [`MODEL-V2.md`](MODEL-V2.md) updates at once** |
| 4 | Model | Recompute CAC by audience and kill the losing leg | 5 | 5 | 4 | 5 | 5 | 4 | **95** | The model splits spend 25/45/30 across intent seed, lookalike and broad at $489 / $817 / $1,070. **Those are predictions.** One month of real data tells you which to defund |
| 5 | Supply | The graded directory, v0 — a tracker, not a platform | 5 | 5 | 4 | 5 | 4 | 5 | **94** | [`HUNGRY.md`](HUNGRY.md) §9's retention mechanism. **It is a spreadsheet and a script until roughly placement thirty**, not software. Build the cheap version now and it starts compounding immediately |
| 6 | Supply | **Build the grading rubric as an actual scoring tool** | 5 | 5 | 4 | 4 | 5 | 5 | **93** | [`MODEL-V2.md`](MODEL-V2.md) gap 6: *premium* is currently an adjective. The fix is one test — **recut an existing ad, measure 3-second and 15-second retention against the original**. Turn that into a scoring sheet that computes the grade identically every time. **This is what makes the claim falsifiable**, and it doubles as the sales asset |
| 7 | Offer | Pre-call research brief on every prospect | 4 | 4 | 5 | 5 | 5 | 4 | **90** | Their site, their live ads, their job postings, their current creative — one page, before every call. Cheap, repeatable, and it is the difference between a cold call and an informed one |
| 8 | Offer | Draft the placement agreement, guarantee terms and EOR schedule | 5 | 4 | 5 | 3 | 5 | 5 | **89** | **Draft only.** A lawyer must review before anything is signed — but arriving with a complete draft cuts the bill and the turnaround substantially. See §4 |
| 9 | Media | The `/proof` page write-ups | 5 | 5 | 3 | 4 | 5 | 4 | **88** | **The most important page on the site.** Each recut ad, with the retention delta stated. This is where *premium* stops being an adjective |
| 10 | Repo | Keep this repository as the decision record | 4 | 5 | 3 | 5 | 5 | 5 | **87** | Every screen here is a **runnable model, not a memo**. That is why the recommendation could reverse three times in one conversation without losing the reasoning. Keep adding to it and the compounding is real |
| 11 | Supply | Sourcing lists from public portfolios and showreels | 4 | 4 | 5 | 4 | 5 | 4 | **86** | Public portfolio sites, showreel platforms, public communities. **Respect each site's terms** — some explicitly forbid scraping, and LinkedIn in particular. Build the list where it is permitted and do the rest by hand |
| 12 | Demand | Landing-page copy for `/agencies`, `/ecommerce`, `/teardown` | 5 | 4 | 4 | 4 | 5 | 3 | **86** | The words are what convert, and the model's specifics — the **$5,000–16,500/mo vendor invoice** comparator, the 12-month guarantee, the paid teardown — have to become sentences. Draft here, paste into Framer |
| 13 | Model | Weekly "what changed and what it means" report | 4 | 3 | 5 | 5 | 5 | 4 | **85** | Export Meta and Stripe, run one command, get the deltas plus the second-order effect on the 30-day ratio. Ten minutes replacing an afternoon |
| 14 | Model | Stress-test decisions before committing spend | 4 | 4 | 4 | 5 | 5 | 3 | **84** | *"What if deposit take-up is 12% not 24%?"* is a one-line change and a re-run, not a guess. The repo is already built to answer that shape of question |
| 15 | Ops | A one-page internal dashboard | 4 | 4 | 4 | 5 | 4 | 5 | **84** | Placements, seats per client, MRR, churn, cash. **Not a SaaS purchase** — a script that reads your sheet and prints the six numbers you actually steer by |
| 16 | Demand | Pull competitor ads from the Meta Ad Library and map the angles | 3 | 4 | 5 | 5 | 5 | 3 | **84** | Public data. Which competitors run what, for how long — long-running ads are the ones that work. Structured into a table you can actually act on |
| 17 | Research | Country and role expansion screens, when the time comes | 4 | 4 | 5 | 5 | 2 | 5 | **84** | Exactly what [`COUNTRIES.md`](COUNTRIES.md) and [`MAP.md`](MAP.md) already are. Re-run the same machinery against new questions rather than starting over |
| 18 | Demand | Count job postings across every phrasing before writing the ad | 4 | 4 | 4 | 5 | 5 | 2 | **83** | [`MODEL-V2.md`](MODEL-V2.md) gap 10: if agencies post *video editor* and never *performance video editor*, the audience build misses them. Flagged there as **free, one afternoon** — this is that afternoon |
| 19 | Ops | Placement onboarding checklist and the 30/60/90 cadence | 5 | 4 | 3 | 4 | 4 | 5 | **82** | The thing that protects **seat continuity — the largest single lever in the business**. Systematise it before placement one, not after placement five |
| 20 | Research | Track the USPTO Class 35 position on *All Hands* | 4 | 4 | 4 | 4 | 5 | 3 | **81** | Still outstanding, and **two live users of *All Hands* in talent services** were found. Monitoring is agent work; **the clearance opinion is not** — see §4 |
| 21 | Supply | Design and auto-score the take-home brief | 4 | 4 | 4 | 4 | 4 | 5 | **81** | One brief, one rubric, consistent scoring. The consistency *is* the product — it is what you are selling to the buyer |
| 22 | Model | Cohort and payback analysis once placements exist | 4 | 4 | 4 | 5 | 3 | 4 | **81** | Seat continuity is worth **+$9,022 per client** across 9→30 EOR months. You cannot manage that without cohorts, and cohorts are a scripting job |
| 23 | Demand | Read the Meta export and tell you what to change | 4 | 3 | 5 | 4 | 4 | 3 | **78** | Frequency, placement breakdown, hook rate, CPM drift. You can read this yourself — the gain is doing it every week without it costing an evening |
| 24 | Research | Refresh salary benchmarks before repricing | 4 | 4 | 4 | 5 | 2 | 4 | **78** | The whole model rests on the **$1,650/mo talent cost** and the fee being 30% of first-year comp. Both drift |
| 25 | Media | Case studies from the first placements | 4 | 4 | 4 | 4 | 3 | 4 | **78** | Month two onward, and only with real numbers. A fabricated case study is worse than none when your entire positioning is *falsifiable* |
| 26 | Research | Monitor competitor pricing pages for changes | 3 | 3 | 5 | 5 | 3 | 5 | **77** | [`COMPETITOR-DATA.md`](COMPETITOR-DATA.md) is a snapshot. A scheduled diff turns it into a live feed, and pricing moves are the ones that matter |
| 27 | Offer | Proposal and follow-up generator off the call notes | 3 | 3 | 4 | 4 | 4 | 4 | **71** | Same structure every time, filled from notes. Speed matters here — proposals sent same-day close better than ones sent in three days |
| 28 | Supply | Outreach sequences to graded candidates | 3 | 3 | 4 | 4 | 4 | 3 | **70** | Volume with personalisation. Fine work for an agent, moderate leverage |
| 29 | Ops | Invoicing, payment tracking and the EOR monthly run | 3 | 3 | 4 | 4 | 3 | 4 | **68** | EOR is $477/employee/month recurring. Small numbers now, but the tracking has to exist before it is twenty employees |
| 30 | Demand | Generate ad copy variants in volume | 3 | 2 | 4 | 4 | 5 | 2 | **66** | Useful and genuinely the *commodity* use. **You are the media buyer** — the constraint is your judgement of which to run, not the supply of lines |
| 31 | Media | The newsletter, from month three | 3 | 3 | 4 | 4 | 2 | 3 | **65** | Gap 11 again — and the first issue's number should come **from your first ten placements**, not from research |
| 32 | Ops | Replacement-request workflow under the 12-month guarantee | 3 | 3 | 3 | 4 | 3 | 4 | **64** | The guarantee is the cheapest differentiation you have; the process behind it has to be fast or the guarantee costs more than it should |
| 33 | Media | X posts during launch month | 2 | 2 | 4 | 4 | 4 | 1 | **58** | [`MODEL-V2.md`](MODEL-V2.md) gap 11 caps this deliberately: **X only at launch**, newsletter at month three. Your attention is the scarce input, not your posting volume |

### The six that carry it

- ****Build the intent-seed audience by scraping job postings**** — Demand · 100
- ****Turn the paid teardown into a repeatable generator**** — Offer · 97
- ****Replace the model's assumptions with real numbers, monthly**** — Model · 96
- **Recompute CAC by audience and kill the losing leg** — Model · 95
- **The graded directory, v0 — a tracker, not a platform** — Supply · 94
- ****Build the grading rubric as an actual scoring tool**** — Supply · 93

Note the shape: **three of the six are about measuring rather than making.** Building the intent-seed
audience, turning the teardown into a product, and keeping the model honest all beat every content
task on the board.

---

## 3. By phase

### Weeks 0–2 · before a dollar is spent

- Landing-page copy for `/agencies`, `/ecommerce`, `/teardown`
- **Count job postings across all three phrasings** — this decides the ad, and it is free
- **Build the intent-seed audience** from job postings and export the CSV
- Meta Ad Library sweep — who is running what, and for how long
- The teardown generator, so the money gate is a product on day one
- The grading rubric as a scoring sheet
- Draft the placement agreement and guarantee for a lawyer to review

### Weeks 2–8 · first spend, first placements

- **Feed real CPM, CTR, LP conversion and deposit take-up into `funnel.py`** and re-run everything downstream
- Weekly what-changed report
- Pre-call research brief before every single call
- `/proof` write-ups as the first recuts land
- Placement onboarding checklist and the 30/60/90 cadence
- Graded directory v0 — a sheet and a script

### Months 3–6 · does it compound

- Cohort and payback analysis; **defund the losing audience leg**
- Case studies with real numbers
- `/talent` page, footer-only and `noindex`, with the pass rate on it
- Newsletter, first number drawn from the first ten placements
- The internal dashboard
- Scheduled competitor-pricing diffs
- Second-role and second-country screens, reusing the existing machinery

---

## 4. What not to use it for

| Do not | Why | Instead |
|---|---|---|
| **Grading the creative work itself** | [`LAUNCH.md`](LAUNCH.md) introduced `FOUNDERGRADE` for exactly this: **can the operator personally judge the output with no team.** Video *was chosen* because you can. An agent cannot tell you whether a recut is actually better | Use it to build the scoring sheet. **You supply the score** |
| **The sales call** | The whole model rests on a buyer trusting an unknown operator. That is bought in conversation | Pre-call brief and post-call follow-up — the parts either side |
| **Legal and tax authority** | India EOR compliance, US contract enforceability, the Class 35 trademark opinion. **A confident wrong answer here is expensive and slow to unwind** | Draft everything so the professional is reviewing rather than writing. That is the real saving, and it is large |
| **Scraping anything whose terms forbid it** | LinkedIn is the obvious one. Convenience is not a defence, and your business depends on the account | Public job boards, public portfolios, the Meta Ad Library, company sites. There is plenty that is permitted |
| **Inventing a number to fill a gap** | This repo's rule throughout. Two of the worst errors in it came from exactly that — a hand-written `SAYS` dictionary and a `CLEAR` score inferred by regexing my own prose | Mark it `[?]`, and go and measure it |
| **Deciding what to do** | Every screen here narrows options and prices trade-offs. **It has been wrong and reversed itself repeatedly** — on the domain, on the platform, on whether All Hands was clean | Use it to make the choice legible. You still make it |

---

## 5. How to actually spend the plan

| | |
|---|---|
| **Work inside this repo** | It already holds the model, the funnel, the offer, the countries and every decision with its reasoning. An agent with that context gives a different quality of answer than one starting cold — most of what makes this useful is the context, not the model |
| **Build scripts, not answers** | Ask for a *runnable screen* rather than a reply. Every file in `scoring/` was written once and re-run many times as inputs changed. **An answer is spent when you read it; a script keeps paying** |
| **Batch into long sessions** | One two-hour session on "build the intent-seed pipeline" produces far more than twenty scattered questions, because context accumulates within a session and resets between them |
| **Make it check rather than assert** | The most valuable things in this repo came from *checking*: RDAP calls, Datamuse corpus frequencies, HTTP fetches of competitor sites, a two-proportion sample-size calculation. **"Go and verify" beats "what do you think"** almost every time |
| **Schedule the recurring ones** | Competitor pricing diffs, posting-count refreshes, the weekly model re-run. Set them up once as scheduled jobs and they run without your attention, which is the scarce input |
| **Ask it to argue with you** | The three most useful moments in this whole engagement were reversals: the `.com` namespace, the Claude-Code-vs-Framer score, and finding that *All Hands* is not clean in recruiting after I had said it was. **Ask what would have to be true for the opposite to be right** |

*One caveat on the plan itself: usage allowances change, and I have not verified the current limits
for your tier — so nothing above assumes a specific quota. The advice is about **what produces the
most per session**, which holds regardless.*
