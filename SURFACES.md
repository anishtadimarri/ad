# Every Function, Across Code, Cowork and Chat

> *"All the things — website to ads to cold email to whatever else. I won't have employees."*

**62 activities across 12 functions**, each placed on a surface and scored on
your criteria: `IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · `FIT` 16 · `NOW` 12 · `REUSE` 6.

**`FIT` is what keeps this honest** — it scores how well an agent does the task *versus you doing
it*. It is why screening reels scores 3 and building the scraper scores 5, and why the sales call
is not in the table at all.

---

## 1. Which surface, and why

Assignment is by **task shape**, not by feature list — feature lists move, shapes do not.

| Surface | Use when the output is | Because |
|---|---|---|
| **Code** | a runnable tool, a data pipeline, or a **verified fact** | It can *check* rather than assert — RDAP calls, corpus frequencies, HTTP fetches, a sample-size calculation. It leaves a script that keeps paying |
| **Cowork** | a document, sheet or deck — or repeated ops work over business files | The output is the artefact itself, and it lives in a folder you keep, not a chat you lose |
| **Chat** | a judgement, a draft, or an answer you use in ten minutes | Fastest loop, and the only one where you can **show it something and ask what it sees** |

---

## 2. Ranked — all 62

| # | Function | Activity | Surface | Imp | Val | Time | Fit | Now | Re | Score | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Meta ads | Build the intent-seed audience from scraped job postings | **Code** | 5 | 5 | 5 | 5 | 5 | 5 | **100** | `TARGETING.md`'s thesis. **25% of spend at the best CAC in the model — $489, 9.07:1.** Scrape, dedupe, export. Rebuild monthly so the signal stays dated |
| 2 | Outbound | Build the prospect list — agencies and e-comm brands | **Code** | 5 | 5 | 5 | 5 | 5 | 5 | **100** | Public sources: job boards, company sites, the Ad Library. **Respect each site's terms.** This is the same pipeline as the intent seed, pointed at contacts |
| 3 | Sales | Turn the paid teardown into a repeatable generator | **Code** | 5 | 5 | 5 | 4 | 5 | 5 | **97** | The **money gate** (`OFFER.md` §9.1). Their ad export in, structured teardown out. **Turns a bespoke service into a 30-minute product** |
| 4 | Strategy | Keep the model live on real numbers, monthly | **Code** | 5 | 5 | 4 | 5 | 5 | 5 | **96** | `funnel.py` marks steps 6–9 as **assumptions, because no data existed**. From week three they are facts. Four real inputs re-derive CAC, both ratios, the audience split and the scale arithmetic **in one command** |
| 5 | Supply | The graded directory, v0 | **Code** | 5 | 5 | 4 | 5 | 4 | 5 | **94** | `HUNGRY.md` §9's retention mechanism — worth **+$9,022 per client**. A sheet and a script until placement thirty |
| 6 | Supply | Build the grading rubric as a scoring tool | **Code** | 5 | 5 | 4 | 4 | 5 | 5 | **93** | `MODEL-V2.md` gap 6. **Recut an ad, measure 3s and 15s retention against the original.** Same computation every time — that consistency *is* the product |
| 7 | Outbound | Deliverability setup — SPF, DKIM, DMARC, warm-up, domain choice | **Code** | 5 | 4 | 4 | 5 | 5 | 5 | **92** | **Do not send from `allhandstalent.com`.** Use a separate sending domain so a deliverability problem never touches the domain your ads land on. This is exactly the kind of setup that is checkable, and expensive to get wrong quietly |
| 8 | Finance | Cash-flow forecast — you pay talent before clients pay you | **Code** | 5 | 5 | 3 | 5 | 5 | 4 | **91** | **The failure mode that kills placement businesses.** EOR means salaries leave monthly while fees arrive lumpily. Model it before it bites |
| 9 | Sales | Pre-call research brief on every prospect | **Code** | 4 | 4 | 5 | 5 | 5 | 4 | **90** | Their site, live ads, job postings, current creative. One page, every time |
| 10 | Legal | Draft the placement agreement, guarantee and EOR schedule | **Cowork** | 5 | 4 | 5 | 3 | 5 | 5 | **89** | **Draft only.** Arriving with a complete draft cuts the bill and the turnaround — that is the real saving, and it is large |
| 11 | Website | `/proof` write-ups — recut ads with retention deltas | **Chat** | 5 | 5 | 3 | 4 | 5 | 4 | **88** | **The most important page on the site.** Where *premium* stops being an adjective |
| 12 | Supply | Sourcing lists from public portfolios and showreels | **Code** | 4 | 4 | 5 | 4 | 5 | 4 | **86** | Where the terms permit it. The rest by hand |
| 13 | Website | Landing-page copy for `/agencies`, `/ecommerce`, `/teardown` | **Chat** | 5 | 4 | 4 | 4 | 5 | 3 | **86** | The words convert, not the layout. Draft in chat, paste into Framer |
| 14 | Website | Technical setup — pixel, CAPI, events, redirects | **Code** | 4 | 4 | 4 | 5 | 5 | 4 | **86** | **Verify CAPI with test events before spending.** Every CAC number assumes attribution works |
| 15 | Strategy | Scenario-test before committing spend | **Code** | 4 | 4 | 4 | 5 | 5 | 3 | **84** | *"What if deposit take-up is 12%?"* is a one-line change, not a debate |
| 16 | Finance | Unit economics and the live dashboard | **Code** | 4 | 4 | 4 | 5 | 4 | 5 | **84** | Placements, seats, MRR, churn, cash. **A script that reads your sheet**, not a SaaS |
| 17 | Outbound | Per-prospect personalisation at volume | **Code** | 4 | 4 | 5 | 4 | 4 | 4 | **84** | One line each, drawn from their live ads or their job postings. **This is what makes cold email work**, and it is the part that does not scale by hand |
| 18 | Strategy | Expansion screens — next role, next country, next ICP | **Code** | 4 | 4 | 5 | 5 | 2 | 5 | **84** | `COUNTRIES.md` and `MAP.md` are the machinery. Re-run it, do not rebuild it |
| 19 | Meta ads | Meta Ad Library sweep — who runs what, and for how long | **Code** | 3 | 4 | 5 | 5 | 5 | 3 | **84** | Public data. **Long-running ads are the ones that work.** Structured into a table |
| 20 | Meta ads | Count job postings across every phrasing, before writing the ad | **Code** | 4 | 4 | 4 | 5 | 5 | 2 | **83** | `MODEL-V2.md` gap 10. Free, one afternoon, and it decides the ad |
| 21 | Outbound | Sequence writing — first touch, follow-ups, breakup | **Chat** | 4 | 4 | 4 | 4 | 5 | 4 | **82** | Draft fast, iterate on replies |
| 22 | Delivery | Onboarding checklist and the 30/60/90 cadence | **Cowork** | 5 | 4 | 3 | 4 | 4 | 5 | **82** | Protects **seat continuity, the largest single lever in the business**. Build it before placement one |
| 23 | Supply | Design the take-home brief and its scoring sheet | **Cowork** | 4 | 4 | 4 | 4 | 4 | 5 | **81** | One brief, one rubric, consistent scores |
| 24 | Legal | USPTO Class 35 position on *All Hands* | **Code** | 4 | 4 | 4 | 4 | 5 | 3 | **81** | Still outstanding, and **two live users of *All Hands* in talent services** were found. **Monitoring is agent work; the clearance opinion is not** |
| 25 | Ops | SOPs for everything you do twice | **Cowork** | 4 | 4 | 4 | 4 | 4 | 5 | **81** | **The substitute for employees.** Every SOP written now is what you hand a VA later instead of explaining it |
| 26 | Strategy | Weekly review — what changed, what it means, what to do | **Chat** | 4 | 4 | 4 | 4 | 5 | 2 | **80** | Fifteen minutes with the numbers in front of you. The habit matters more than the tool |
| 27 | Meta ads | Weekly account read — frequency, hook rate, CPM drift | **Code** | 4 | 3 | 5 | 4 | 4 | 3 | **78** | You can do this yourself. The gain is doing it weekly without losing an evening |
| 28 | Sales | Call script, discovery questions, objection handling | **Chat** | 4 | 4 | 3 | 4 | 5 | 4 | **78** | Especially the **India objection** — `COUNTRIES.md` §9 already prices it |
| 29 | Media | Case studies from the first placements | **Cowork** | 4 | 4 | 4 | 4 | 3 | 4 | **78** | **Only with real numbers.** A fabricated case study is worse than none when the positioning is *falsifiable* |
| 30 | Ops | Recurring monitors — competitor pricing, salary benchmarks | **Code** | 3 | 3 | 5 | 5 | 3 | 5 | **77** | Scheduled diffs. **Runs without your attention**, which is the scarce input |
| 31 | Supply | Screening — CVs and reels against the rubric | **Chat** | 4 | 3 | 5 | 3 | 5 | 2 | **76** | `FIT`=3. It can sort and shortlist. **You watch the reel** |
| 32 | Website | LP variants for each new angle | **Chat** | 4 | 3 | 4 | 4 | 5 | 2 | **76** | Volume of variants, judged by you. §1 of `SITE.md`: iterate, do not split-test |
| 33 | Supply | Offer letters and candidate contracts | **Cowork** | 4 | 3 | 4 | 3 | 4 | 5 | **74** | **Draft only** — see §4 |
| 34 | Legal | NDAs, IP assignment, contractor terms | **Cowork** | 4 | 3 | 4 | 3 | 4 | 5 | **74** | Draft only. IP assignment matters — you are selling creative output |
| 35 | Delivery | Expansion play — second and third seat in the same client | **Chat** | 4 | 5 | 2 | 4 | 3 | 3 | **73** | Seats-per-client is where the economics actually live |
| 36 | Meta ads | Creative concepts and video scripts | **Chat** | 4 | 3 | 4 | 3 | 5 | 2 | **72** | `FIT`=3. You judge creative better than any agent can |
| 37 | Hiring | Scope, JD and screening for the first VA or recruiter | **Cowork** | 4 | 4 | 3 | 4 | 2 | 5 | **72** | Month four to six. **The SOPs above are what makes this hire cheap** |
| 38 | Hiring | Training material from your own SOPs | **Cowork** | 3 | 4 | 4 | 4 | 2 | 5 | **72** | Written once, reused per hire |
| 39 | Sales | Proposal and follow-up from call notes | **Cowork** | 3 | 3 | 4 | 4 | 4 | 4 | **71** | Same structure every time. **Same-day beats three-days-later** |
| 40 | Sales | Pricing and negotiation prep | **Chat** | 4 | 4 | 2 | 4 | 4 | 3 | **71** | Know your floor before the call. The model already tells you what it is |
| 41 | Outbound | Reply triage and routing | **Cowork** | 3 | 3 | 4 | 4 | 4 | 3 | **70** | Interested / not now / never, and the right response to each |
| 42 | Supply | Candidate outreach and nurture | **Chat** | 3 | 3 | 4 | 4 | 4 | 3 | **70** | Volume with personalisation |
| 43 | Delivery | Check-in prompts and QBR packs | **Cowork** | 3 | 3 | 4 | 4 | 3 | 5 | **70** | The mechanism that turns 9 EOR months into 30 |
| 44 | Meta ads | Budget pacing and reallocation rules | **Code** | 3 | 4 | 3 | 4 | 3 | 4 | **69** | A script that reads the export and says where the money should move |
| 45 | Strategy | Decision journal — what you decided and why | **Cowork** | 3 | 4 | 2 | 4 | 4 | 5 | **68** | The repo does this for analysis. Do it for the calls you make between analyses |
| 46 | Website | Design and mobile QA — screenshot in, problems out | **Chat** | 3 | 3 | 4 | 4 | 4 | 2 | **68** | Chat because it needs **eyes on the actual page** |
| 47 | Finance | Invoicing, collections and the EOR monthly run | **Cowork** | 3 | 3 | 4 | 4 | 3 | 4 | **68** | $477/employee/month recurring. Small now; the process has to exist before it is twenty |
| 48 | Website | Brand voice guide — one page, so every asset matches | **Cowork** | 3 | 3 | 3 | 4 | 4 | 5 | **68** | Cheap, and it stops the site, the ads and the emails sounding like three companies |
| 49 | Supply | Interview structure and reference-check questions | **Cowork** | 3 | 3 | 3 | 4 | 4 | 5 | **68** | Written once, used forever |
| 50 | Meta ads | Policy pre-check before submitting | **Chat** | 3 | 3 | 3 | 4 | 5 | 2 | **67** | Especially the **Employment Special Ad Category** trap in `SUPPLY-DEMAND.md` §1 |
| 51 | Sales | Pipeline tracking | **Cowork** | 3 | 3 | 3 | 4 | 4 | 4 | **67** | A sheet until roughly deal thirty. Not a CRM purchase |
| 52 | Meta ads | Ad copy variants in volume | **Chat** | 3 | 2 | 4 | 4 | 5 | 2 | **66** | The commodity use. **You are the media buyer** — the constraint is which to run |
| 53 | Media | Newsletter from month three | **Cowork** | 3 | 3 | 4 | 4 | 2 | 3 | **65** | First number from your **first ten placements**, not from research |
| 54 | Outbound | LinkedIn outbound | **Chat** | 3 | 3 | 3 | 4 | 4 | 2 | **64** | Message drafting only. **Do not automate or scrape it** — the terms forbid it and the account is your face |
| 55 | Delivery | Replacement workflow under the 12-month guarantee | **Cowork** | 3 | 3 | 3 | 4 | 3 | 4 | **64** | Cheapest differentiation you have. It has to be fast or it costs more than it should |
| 56 | Ops | Tool stack decisions and integrations | **Chat** | 3 | 3 | 3 | 4 | 4 | 2 | **64** | You have already done four of these |
| 57 | Media | Your own LinkedIn presence | **Chat** | 3 | 3 | 3 | 4 | 4 | 2 | **64** | For an unknown operator this is a real trust asset |
| 58 | Finance | FX exposure — INR cost base, USD revenue | **Code** | 3 | 4 | 2 | 4 | 3 | 3 | **64** | A real margin variable that nothing in the repo currently models |
| 59 | Legal | Privacy basics if you take EU or UK clients | **Chat** | 3 | 3 | 3 | 3 | 3 | 3 | **60** | Know what you are walking into before you sell into it |
| 60 | Finance | Bookkeeping prep for an accountant | **Cowork** | 2 | 2 | 4 | 4 | 3 | 4 | **59** | Categorise and reconcile. **The accountant still files** |
| 61 | Media | X during launch month | **Chat** | 2 | 2 | 4 | 4 | 4 | 1 | **58** | `MODEL-V2.md` gap 11 caps this deliberately. **X only at launch** |
| 62 | Ops | Inbox and calendar triage | **Cowork** | 2 | 2 | 4 | 3 | 4 | 2 | **56** | Low value while volume is low. Real by month six |

### The top ten, and what they have in common

1. **Build the intent-seed audience from scraped job postings** — Meta ads · `Code` · 100
1. **Build the prospect list — agencies and e-comm brands** — Outbound · `Code` · 100
1. **Turn the paid teardown into a repeatable generator** — Sales · `Code` · 97
1. **Keep the model live on real numbers, monthly** — Strategy · `Code` · 96
1. **The graded directory, v0** — Supply · `Code` · 94
1. **Build the grading rubric as a scoring tool** — Supply · `Code` · 93
1. **Deliverability setup — SPF, DKIM, DMARC, warm-up, domain choice** — Outbound · `Code` · 92
1. **Cash-flow forecast — you pay talent before clients pay you** — Finance · `Code` · 91
1. **Pre-call research brief on every prospect** — Sales · `Code` · 90
1. **Draft the placement agreement, guarantee and EOR schedule** — Legal · `Cowork` · 89

**9 of the top 10 are Code**, and the pattern is consistent: the highest-value work is
**building something that runs repeatedly** — the audience pipeline, the teardown generator, the
grading tool, the model itself. Writing copy sits mid-table. **The obvious uses are the
low-leverage ones.**

---

## 3. By function

**Strategy** — 5 activities, top: *Keep the model live on real numbers, monthly* (`Code`, 96)  
**Website** — 6 activities, top: *`/proof` write-ups — recut ads with retention deltas* (`Chat`, 88)  
**Meta ads** — 8 activities, top: *Build the intent-seed audience from scraped job postings* (`Code`, 100)  
**Outbound** — 6 activities, top: *Build the prospect list — agencies and e-comm brands* (`Code`, 100)  
**Sales** — 6 activities, top: *Turn the paid teardown into a repeatable generator* (`Code`, 97)  
**Supply** — 8 activities, top: *The graded directory, v0* (`Code`, 94)  
**Delivery** — 4 activities, top: *Onboarding checklist and the 30/60/90 cadence* (`Cowork`, 82)  
**Finance** — 5 activities, top: *Cash-flow forecast — you pay talent before clients pay you* (`Code`, 91)  
**Legal** — 4 activities, top: *Draft the placement agreement, guarantee and EOR schedule* (`Cowork`, 89)  
**Ops** — 4 activities, top: *SOPs for everything you do twice* (`Cowork`, 81)  
**Media** — 4 activities, top: *Case studies from the first placements* (`Cowork`, 78)  
**Hiring** — 2 activities, top: *Scope, JD and screening for the first VA or recruiter* (`Cowork`, 72)  

---

## 4. What not to use any of them for

| Do not | Why | Instead |
|---|---|---|
| **The sales call itself** | Trust is bought in conversation, and you have no track record to lean on | Brief before, follow-up after |
| **Grading the creative** | `FOUNDERGRADE` is *why video was chosen* — you can judge it with no team. An agent cannot | Build the scoring sheet. **You score** |
| **Legal, tax and immigration authority** | India EOR compliance, contract enforceability, the trademark opinion. A confident wrong answer is expensive and slow to unwind | Draft so the professional reviews rather than writes |
| **LinkedIn automation or scraping** | The terms forbid it and the account is your face in a trust business | Draft messages; send them yourself |
| **Sending cold email from your main domain** | One deliverability incident and the domain your ads land on is damaged | A separate sending domain, warmed properly |
| **Inventing a number** | The two worst errors in this repo came from exactly that — a hand-written `SAYS` dict and a `CLEAR` score inferred from my own prose | Mark it `[?]` and go measure it |
| **Deciding** | Every screen here narrows options. **It has reversed itself four times** — the domain, the platform, the code-vs-Framer score, whether *All Hands* was clean | Use it to make the choice legible. You still make it |

---

## 5. The split

| Surface | Activities | Share of activities | Share of total score | Avg score |
|---|---|---|---|---|
| **Code** | 22 | **35%** | **40%** | 86.1 |
| **Cowork** | 21 | **34%** | **31%** | 71.3 |
| **Chat** | 19 | **31%** | **29%** | 71.8 |

> **Roughly 35% Code · 34% Cowork · 31% Chat by count — but 40% / 31% / 29% by weighted value.**

Read the averages, not the counts. **Code carries the highest average score** because the things
worth doing more than once end up there. Chat has the most *moments* and the least accumulated
value — it is where you think, not where you build. Cowork sits between: it is where the
**documents that substitute for employees** live — SOPs, contracts, onboarding, case studies.

### How to actually run it

| | |
|---|---|
| **Code, in this repo, once or twice a week** | Long sessions. Build pipelines and tools, and re-run the model against real numbers. This is where the compounding is |
| **Cowork, as the filing cabinet that does work** | Every SOP, contract, checklist and case study. **These are what you hand your first hire instead of explaining** |
| **Chat, many times a day** | Copy, judgement calls, *look at this and tell me what is wrong*. Cheapest loop, lowest half-life |

**The one habit worth more than the split:** ask it to argue with you. The four most useful
moments in this project were reversals — the `.com` namespace, the code-vs-Framer score, the
unbreakability re-weight, and finding *All Hands* was not clean in recruiting after I had said it
was.
