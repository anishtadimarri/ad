# MASTERLIST — All Hands Talent

**One page. Everything else defers to this.**

106 activities · 22 blockers · 25 workflows · 19 functions.
Generated from [`activities.py`](scoring/activities.py) and [`workflows.py`](scoring/workflows.py), so it **cannot drift**
out of sync with them.

> **Read §1 and §2. That is the operating document.** §3 onward is reference for when you need it.

---

## 1. The critical path

**Ranked by what unblocks what, not by value.** A blocker has modest value added and infinite
importance — nothing downstream happens until it exists, which is exactly why leverage-ranked lists
bury them.

| # | Blocker | Function | Surface |
|---|---|---|---|
| 1 | **Decide the entity structure — India Pvt Ltd, US LLC, or both** | Entity | `Chat` |
| 2 | **Register the entity and get the identifiers** | Entity | `Cowork` |
| 3 | **Business bank account that can receive USD** | Entity | `Cowork` |
| 4 | **Choose the payment rail for client payments** | Entity | `Chat` |
| 5 | **Payout rail for paying Indian talent** | Entity | `Chat` |
| 6 | **W-8BEN-E and the US client tax-form pack** | Entity | `Cowork` |
| 7 | **GST registration and LUT for export of services** | Entity | `Cowork` |
| 8 | **Decide: are you the EOR, or do you partner with one?** | Employment | `Chat` |
| 9 | **Contractor vs employee classification for placed talent** | Employment | `Chat` |
| 10 | **Talent contract — IP assignment, confidentiality, non-solicit** | Employment | `Cowork` |
| 11 | **Rate card and the fee definition** | Pricing | `Code` |
| 12 | **Guarantee terms — 12-month replacement** | Pricing | `Cowork` |
| 13 | **MSA and per-placement SOW** | Sales | `Cowork` |
| 14 | **LinkedIn company page and founder profile** | Demand | `Cowork` |
| 15 | **Pixel, CAPI and event verification** | Website | `Code` |
| 16 | **UTM and naming discipline** | Measure | `Code` |
| 17 | **Self-reported attribution on the form** | Sales | `Code` |
| 18 | **Meta Business Manager structure and ban resilience** | Risk | `Code` |
| 19 | **Client ad-account access protocol** | Security | `Cowork` |
| 20 | **Cold-email infrastructure — domains, SPF/DKIM/DMARC, warm-up** | Outbound | `Code` |
| 21 | **Email verification and suppression** | Outbound | `Code` |
| 22 | **Cash-flow forecast** | Finance | `Code` |

**Rows 1–7 are one chain and they gate your first paid invoice:** entity structure → identifiers →
bank → client payment rail → talent payout rail → **W-8BEN-E** → GST/LUT. In India-to-US services
this commonly takes weeks. **Start it in week zero.**

---

## 2. The calendar

### **Week 0 — start the long clocks**

*Two things here have lead times measured in weeks. **Everything else can be compressed; these cannot.** Left until they feel urgent, each costs a month*

- **Entity decision → registration → bank → payment rails.** The India→US chain, and nothing gets paid until it is done
- **Cold-email infrastructure**: domains, SPF/DKIM/DMARC, mailboxes, **warm-up begins**
- Decide **EOR yourself or partner** — it changes what you are building
- Runway and personal burn: how many months of zero revenue you can absorb

### **Week 1 — the things you cannot sell without**

*Supply must lead demand, and the offer must be unambiguous before anyone reads it*

- Sourcing → screen → take-home → **grade** → bench
- **Rate card and fee definition** — one-time, 30–35% of first-year comp. `MODEL-V2.md` gap 1 breaks the model 8× if this stays ambiguous
- Guarantee terms — 12-month replacement, no cash refunds
- Talent contract with **IP assignment** and non-solicit; MSA and SOW drafts
- **Count job postings across all three phrasings** — free, one afternoon, decides the ad

### **Week 2 — the assets that do the selling**

*Each of these is reused on every deal for the life of the business*

- **Teardown generator** — the money gate as a product, not a bespoke job
- **Grading rubric as a scoring tool** — 3s and 15s retention vs the original
- Intent-seed audience built from scraped job postings
- `/proof` write-ups · landing-page copy for `/agencies`, `/ecommerce`, `/teardown`
- LinkedIn company page — the first thing a Western buyer checks
- **Meta Business Manager structure and a spare ad account**, before you need it

### **Week 3 — first spend**

*Nothing here is reversible once money is moving, so the measurement scaffolding goes first*

- **UTM discipline and the self-reported attribution field** — impossible to retrofit
- **Pixel and CAPI verified with test events** — every CAC number assumes attribution works
- Inbound: form → Stripe payment link → calendar → confirmation
- Meta ads live. Special Ad Category pre-check first
- Pre-call research brief, running before the first call

### **Week 4 — close and count**

*Cold email sends now because warm-up started in week 0*

- Cold email stages B–D go live
- Proposal → contract → invoice → kickoff, templated
- **Cash-flow forecast** — you pay talent monthly and get paid lumpily
- Weekly metrics review, one command

### **Before placement one**

*Both are promises already made in the offer. Making them true after the fact is expensive*

- Onboarding day 0–30 · 30/60/90 cadence
- Replacement handling · escalation path for mid-month underperformance
- **Client ad-account access protocol** — partner access, 2FA, documented revocation
- Time-zone overlap and comms norms agreed in writing at kickoff

### **Month 2 — the recurring machine**

*Everything that has to happen every month*

- Monthly EOR run · invoicing · collections
- **Monthly model re-run** — replace assumptions with actuals and re-derive everything
- Bench nurture · competitor and salary monitors
- **Win/loss analysis** on every dead deal

### **Month 3–6 — compounding**

*Only possible once placements exist*

- Case studies with real numbers · referral loop after each 90-day check-in
- Seat expansion · cohort and payback analysis
- `/talent` page, footer-only and `noindex`, with the pass rate on it
- First VA or recruiter — **the SOPs are what make this hire cheap**

---

## 3. The full list, by function

`IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · `FIT` 16 · `NOW` 12 · `REUSE` 6. **🔒 = blocker.**  
`FIT` scores how well an agent does it **versus you doing it** — which is why screening reels scores
3 and building the scraper scores 5.

### Entity — 8 activities, 7 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Choose the payment rail for client payments | `Chat` | 🔒 | **86** | Stripe, Wise, Payoneer, Razorpay — availability depends on the entity decision above, which is why that one comes first |
| Decide the entity structure — India Pvt Ltd, US LLC, or both | `Chat` | 🔒 | **83** | **The first unopened question in this whole repo.** You are in India selling to US buyers. It determines how you invoice, how you are taxed, what a client's procurement will accept, and whether Stripe will take you at all. `FIT`=3 — draft the options, **a CA and a US attorney decide** |
| Payout rail for paying Indian talent | `Chat` | 🔒 | **82** | The other half of the flow, and the half with a monthly deadline |
| **W-8BEN-E** and the US client tax-form pack | `Cowork` | 🔒 | **81** | **A US company cannot pay a foreign entity without this on file.** It will be requested during onboarding of your very first client, and not having it delays cash |
| GST registration and **LUT for export of services** | `Cowork` | 🔒 | **80** | Service exports are zero-rated in India **only with the right filing in place**. Getting this wrong is a real cash cost on every invoice |
| Register the entity and get the identifiers | `Cowork` | 🔒 | **78** | PAN, TAN, incorporation certificate — or the US equivalent |
| Business bank account that can receive USD | `Cowork` | 🔒 | **78** | Nothing else in the model happens until money can land |
| FEMA / FIRC handling for inbound forex | `Cowork` |  | **68** | Your bank will want it. Set the process up once |

### Employment — 6 activities, 3 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **Decide: are you the EOR, or do you partner with one?** | `Chat` | 🔒 | **88** | **The single largest unanswered structural question left.** Being the EOR means payroll, PF, ESI, gratuity and TDS on your books at $477/employee/month margin. Partnering means sharing that margin but no compliance surface. **The model assumes the revenue and has never priced the obligation** |
| Talent contract — IP assignment, confidentiality, non-solicit | `Cowork` | 🔒 | **85** | **IP assignment is not optional** — you are selling creative output your client will own. Non-solicit is what stops a client hiring your placement directly |
| Contractor vs employee classification for placed talent | `Chat` | 🔒 | **80** | Misclassification is the standard way this category gets into trouble |
| Payroll calendar, payslips, TDS | `Cowork` |  | **74** | Monthly and unforgiving. People leave over late pay |
| Equipment and software policy for placed talent | `Cowork` |  | **64** | Who buys the laptop and the Adobe licence, and who owns it after |
| Talent exit and offboarding | `Cowork` |  | **62** | Access revoked, IP confirmed, client told first |

### Security — 3 activities, 1 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **Client ad-account access protocol** | `Cowork` | 🔒 | **88** | **You will be handed access to clients' Meta ad accounts.** That is the single most sensitive thing in the business. Partner access via Business Manager, never shared logins, 2FA everywhere, and documented revocation on exit |
| Password manager and device hygiene, for you and every placement | `Cowork` |  | **72** | One compromised placement account is a client-losing event |
| Handling client creative and brand assets | `Cowork` |  | **64** | Where files live, who can see them, what happens at the end |

### Risk — 4 activities, 1 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **Meta Business Manager structure and ban resilience** | `Code` | 🔒 | **93** | **The severe one, and it is inside your own expertise.** A new advertiser with a new domain and a new page in a scrutinised category is exactly the profile that gets restricted. Separate BM, verified domain, clean page history, a second ad account ready — build it *before* it is needed, because you cannot build it after |
| Client concentration monitor | `Code` |  | **74** | At five clients, one leaving is 20% of revenue |
| Written risk register with triggers | `Cowork` |  | **70** | Ad account ban, payment freeze, a bad placement going public, AI substitution. **`DURABLE`=3 is already the model's weakest score** |
| Professional indemnity / E&O insurance | `Chat` |  | **60** | Larger clients ask. Cheap relative to losing the deal |

### Strategy — 5 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Keep the model live on real numbers, monthly | `Code` |  | **96** | `funnel.py` marks steps 6–9 as assumptions. From week three they are facts, and four inputs re-derive everything downstream in one command |
| Scenario-test before committing spend | `Code` |  | **84** | A one-line change, not a debate |
| Expansion screens — next role, next country, next ICP | `Code` |  | **84** | `COUNTRIES.md` and `MAP.md` are the machinery. Re-run, do not rebuild |
| Weekly review ritual | `Chat` |  | **80** | Fifteen minutes. The habit matters more than the tool |
| Decision journal | `Cowork` |  | **68** | The repo does this for analysis. Do it for the calls between analyses |

### Website — 7 activities, 1 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Pixel, CAPI and event verification | `Code` | 🔒 | **90** | **Verify with test events before spending.** Every CAC number assumes attribution works |
| `/proof` write-ups — recut ads with retention deltas | `Chat` |  | **88** | **The most important page on the site** |
| Landing-page copy for `/agencies`, `/ecommerce`, `/teardown` | `Chat` |  | **86** | The words convert, not the layout |
| LP variants per angle | `Chat` |  | **76** | Iterate, do not split-test — `SITE.md` §1 |
| Design and mobile QA | `Chat` |  | **68** | Chat, because it needs eyes on the actual page |
| Brand voice guide | `Cowork` |  | **68** | Stops the site, ads and emails sounding like three companies |
| Legal pages — privacy, terms, cookie notice | `Cowork` |  | **66** | Meta review looks for them, and EU or UK buyers expect them |

### Meta ads — 8 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Build the intent-seed audience from scraped job postings | `Code` |  | **100** | **25% of spend at the best CAC in the model — $489, 9.07:1** |
| Meta Ad Library sweep | `Code` |  | **84** | **Long-running ads are the ones that work.** Public data |
| Count job postings across every phrasing first | `Code` |  | **83** | `MODEL-V2.md` gap 10. Free, one afternoon, and it decides the ad |
| Weekly account read | `Code` |  | **78** | The gain is doing it weekly without losing an evening |
| **Special Ad Category pre-check** | `Chat` |  | **77** | `SUPPLY-DEMAND.md` §1 prices this at a **10–29% CAC tax** if a B2B ad gets reclassified as employment |
| Creative concepts and scripts | `Chat` |  | **72** | `FIT`=3. You judge creative better than any agent |
| Budget pacing rules | `Code` |  | **69** | A script that says where money should move |
| Ad copy variants in volume | `Chat` |  | **66** | The commodity use |

### Outbound — 7 activities, 2 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Prospect list pipeline | `Code` |  | **100** | Job postings, Ad Library, directories. **Respect each site's terms** |
| Cold-email infrastructure — domains, SPF/DKIM/DMARC, warm-up | `Code` | 🔒 | **92** | **2–4 week lead time — the longest in the business.** Start week one even though it sends week four |
| Per-prospect personalisation at volume | `Code` |  | **84** | **The part that makes cold email work and does not scale by hand** |
| Email verification and suppression | `Code` | 🔒 | **82** | Bounce above ~2–3% damages the sending domain |
| Sequence writing | `Chat` |  | **82** | Short. One ask. The ask is the paid teardown |
| Reply triage and routing | `Cowork` |  | **70** | Four buckets, four responses, none left overnight |
| LinkedIn outbound — manual | `Chat` |  | **64** | Drafting only. **Do not automate or scrape it** |

### Demand — 5 activities, 1 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **Brand-defence search campaign** | `Code` |  | **82** | `ARBITRARY.md` §13: searching *all hands talent* returns **three other organisations and not you.** A few dollars a month fixes it. Nobody else bids on your name |
| LinkedIn company page and founder profile | `Cowork` | 🔒 | **77** | **The first thing a Western buyer checks** on an operator with no track record. Free, and it ranks for your brand query |
| Partnership and referral outreach to adjacent vendors | `Chat` |  | **72** | Agencies that do media buying but not editing are a warm channel |
| Referral request loop after a 90-day check-in | `Cowork` |  | **72** | Systematically, not when you remember |
| Directory listings — Clutch and category directories | `Cowork` |  | **64** | Cheap credibility and a live backlink |

### Sales — 8 activities, 2 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Teardown generator | `Code` |  | **97** | The money gate. **A product, not a bespoke job** |
| Pre-call research brief | `Code` |  | **90** | One page, every call |
| **Self-reported attribution on the form** | `Code` | 🔒 | **87** | *"How did you hear about us?"* — **once you run two channels, platform-reported attribution will double-count and you will defund the wrong one.** One field, added before the second channel starts |
| MSA and per-placement SOW | `Cowork` | 🔒 | **85** | Draft only, lawyer-reviewed. **Nothing gets signed without it** |
| **Win/loss analysis** | `Cowork` |  | **79** | **The most-skipped high-value activity in any young business.** Ten lost deals tell you more than a hundred impressions |
| Call script and objection handling | `Chat` |  | **78** | Especially the India objection — `COUNTRIES.md` §9 prices it |
| Proposal → contract → invoice → kickoff | `Cowork` |  | **71** | Templated so no deal stalls on paperwork |
| Pipeline tracking | `Cowork` |  | **67** | A sheet until deal thirty |

### Pricing — 4 activities, 2 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Rate card and the fee definition | `Code` | 🔒 | **89** | `MODEL-V2.md` gap 1: **the one-time-versus-monthly conflation breaks the model 8× if left ambiguous.** Write it down once, unambiguously |
| Guarantee terms — 12-month replacement | `Cowork` | 🔒 | **88** | Modelled as **cheaper than the 6-month industry standard** while sounding stronger |
| Payment terms, deposits, late fees | `Cowork` |  | **76** | You pay talent monthly. Terms are a cash-flow instrument, not admin |
| Annual increase policy | `Chat` |  | **62** | Decide before the first renewal, not during it |

### Supply — 9 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| The graded directory, v0 | `Code` |  | **94** | The retention mechanism — **+$9,022 per client** |
| Grading rubric as a scoring tool | `Code` |  | **93** | **Recut an ad, measure 3s and 15s retention against the original.** What makes premium falsifiable |
| Sourcing pipeline from public portfolios | `Code` |  | **86** | Where the terms permit |
| Client brief → shortlist of three | `Cowork` |  | **86** | Where the bench turns into revenue |
| Take-home brief and its scoring sheet | `Cowork` |  | **81** | Consistency *is* the product |
| Screening reels against the rubric | `Chat` |  | **76** | `FIT`=3. It shortlists. **You watch the reel** |
| English and communication assessment | `Chat` |  | **76** | `COUNTRIES.md` gates on this for a reason — it is the failure mode buyers fear most about India |
| Bench nurture | `Cowork` |  | **69** | Graded people go cold |
| Interview structure and reference checks | `Cowork` |  | **68** | Written once |

### Delivery — 7 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Onboarding day 0–30 | `Cowork` |  | **82** | Protects **seat continuity, the largest single lever** |
| 30/60/90 check-in cadence | `Cowork` |  | **79** | Turns 9 EOR months into 30 |
| Time-zone overlap and comms norms | `Cowork` |  | **77** | `COUNTRIES.md` gates ASYNC. Agree the overlap window in writing at kickoff |
| Escalation path for underperformance | `Cowork` |  | **75** | **Before it happens.** Mid-month failure is the moment that decides whether a client renews |
| Seat expansion play | `Chat` |  | **73** | Seats-per-client is where the economics live |
| Client feedback loop | `Cowork` |  | **69** | The input to the grading rubric |
| Replacement request handling | `Cowork` |  | **64** | The guarantee only differentiates if it is fast |

### Finance — 7 activities, 1 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **Cash-flow forecast** | `Code` | 🔒 | **91** | **You pay talent monthly and get paid lumpily.** The failure mode that kills placement businesses |
| Unit-economics dashboard | `Code` |  | **84** | Six numbers you steer by. A script, not a SaaS |
| Runway and personal burn | `Code` |  | **77** | How many months of no revenue you can absorb. Decide before spending on ads |
| Invoicing and the monthly EOR run | `Cowork` |  | **74** | $477/employee/month recurring |
| **FX policy — INR cost base, USD revenue** | `Code` |  | **70** | A real margin variable the model does not carry. A 5% move is 5% of gross margin |
| Collections chase | `Cowork` |  | **68** | Polite, automatic, escalating |
| Bookkeeping prep for the accountant | `Cowork` |  | **59** | Categorise and reconcile. **The accountant still files** |

### Measure — 6 activities, 1 blockers

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Monthly model re-run and decision memo | `Code` |  | **94** | **Replace assumptions with actuals and re-derive everything** |
| UTM and naming discipline | `Code` | 🔒 | **87** | **Set before the first click or the data is never clean.** Retrofitting is impossible |
| Weekly metrics review | `Code` |  | **85** | One command, six numbers |
| Cohort and payback analysis | `Code` |  | **81** | Cannot manage seat continuity without it |
| Competitor and salary monitor | `Code` |  | **77** | Scheduled diffs. Runs without you |
| Cross-channel lead dedupe | `Code` |  | **72** | Same company from Meta and cold email is one lead, not two |

### Legal — 3 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **USPTO Class 35 clearance on *All Hands*** | `Chat` |  | **78** | Outstanding for four rounds. **Two live users of *All Hands* exist in talent services.** Monitoring is agent work; **the opinion is not** |
| NDAs and mutual confidentiality | `Cowork` |  | **74** | Draft only |
| Data-protection basics for EU/UK clients | `Chat` |  | **60** | Know it before selling into it |

### Content — 3 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| Case studies with real numbers | `Cowork` |  | **78** | **Only with real numbers.** A fabricated one is worse than none when the positioning is *falsifiable* |
| Newsletter from month three | `Cowork` |  | **65** | First number from your first ten placements |
| X during launch month | `Chat` |  | **58** | `MODEL-V2.md` gap 11 caps this deliberately |

### Ops — 4 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| **SOP capture on anything done twice** | `Cowork` |  | **86** | **The substitute for employees.** What you hand a first hire instead of explaining |
| Weekly planning and time budgeting | `Chat` |  | **74** | **Attention is the binding constraint in every model in this repo.** Budget it explicitly |
| Tool stack and integration decisions | `Chat` |  | **64** | You have already made five |
| Inbox and calendar triage | `Cowork` |  | **56** | Real by month six |

### Hiring — 2 activities

| Activity | Surface | 🔒 | Score | Note |
|---|---|---|---|---|
| First VA or recruiter — scope, JD, screening | `Cowork` |  | **72** | Month four to six. **The SOPs are what make this hire cheap** |
| Training material from your own SOPs | `Cowork` |  | **72** | Written once, reused per hire |

---

## 4. The 25 workflows

An activity is a thing you do. **A workflow is trigger → steps → output, built once, that then runs
without you deciding anything.** With no employees that is the only leverage there is.

| Workflow | Must exist | Lead time | Steps | Surface |
|---|---|---|---|---|
| **Cold email pipeline** | Week 1 setup, Week 4 send | **3–4 weeks** | 22 | Code |
| **SOP capture** | Continuous | 0 | 4 | Cowork |
| **Intent-seed audience refresh** | Week 2, monthly after | 3 days | 7 | Code |
| **Teardown production** | Week 2 | 1 week | 7 | Code |
| **Sourcing → screen → take-home → grade → bench** | Week 2 | 1 week | 10 | Code |
| **Proof-page production** | Week 2 | ongoing | 6 | Chat |
| **Trademark and brand monitor** | Week 2 | 1 day | 3 | Code |
| **Placement onboarding, day 0–30** | Before placement 1 | 3 days | 9 | Cowork |
| **Replacement request handling** | Before placement 1 | 1 day | 6 | Cowork |
| **Meta ads loop** | Week 3 | 1 week | 9 | Code |
| **Inbound lead → teardown → call** | Week 3 | 3 days | 8 | Code |
| **Pre-call → call → follow-up** | Week 3 | 2 days | 6 | Code |
| **Proposal → contract → invoice → kickoff** | Week 4 | 3 days | 7 | Cowork |
| **Client brief → shortlist of three** | Week 4 | 2 days | 6 | Cowork |
| **Cash-flow forecast** | Week 4 | 2 days | 6 | Code |
| **Weekly metrics review** | Week 4 | 1 day | 5 | Code |
| **Bench nurture** | Month 2 | 2 days | 5 | Cowork |
| **30 / 60 / 90 check-in cadence** | Month 2 | 2 days | 6 | Cowork |
| **Monthly EOR run** | Month 2 | 3 days | 8 | Cowork |
| **Collections chase** | Month 2 | 1 day | 5 | Cowork |
| **Monthly model re-run + decision memo** | Month 2 | 2 days | 6 | Code |
| **Competitor and market monitor** | Month 2 | 1 day | 4 | Code |
| **Seat expansion play** | Month 3 | 2 days | 5 | Chat |
| **Case-study production** | Month 3 | 2 days | 6 | Cowork |
| **Referral request loop** | Month 3 | 1 day | 5 | Cowork |

**171 discrete steps.** Cold email alone is 23, decomposed in [`WORKFLOWS.md`](WORKFLOWS.md) §2.

---

## 5. Where an agent is the wrong tool

| Do not | Why | Instead |
|---|---|---|
| **Grading the creative** | `FOUNDERGRADE` is *why video was chosen* — you can judge it with no team | Build the scoring sheet. **You score** |
| **The sales call** | Trust is bought in conversation, and you have no track record | Brief before, follow-up after |
| **Legal, tax and entity authority** | The India→US structure, EOR compliance, the Class 35 opinion. **A confident wrong answer here is expensive and slow to unwind** | Draft so the CA or attorney reviews rather than writes |
| **LinkedIn automation or scraping** | The terms forbid it and the account is your face in a trust business | Draft messages; send them yourself |
| **Cold email from `allhandstalent.com`** | One deliverability incident damages the domain your ads land on | A separate sending domain, warmed properly |
| **Inventing a number** | The two worst errors in this repo came from exactly that | Mark it `[?]` and go measure it |
| **Deciding** | **This repo has reversed itself five times** — the domain, the platform, code-vs-Framer, the unbreakability re-weight, and whether *All Hands* was clean | Use it to make the choice legible. You still make it |

---

## 6. What supersedes what

| Document | What it is | Status |
|---|---|---|
| [`ACTIVITIES.md`](ACTIVITIES.md) | 106 activities, 22 blockers, 18 functions | **Still the reference table.** This file is its front page |
| [`WORKFLOWS.md`](WORKFLOWS.md) | 25 systems, cold email in 23 steps, cold-email CAC model | **Still authoritative on cold email** and on the channel comparison |
| [`SURFACES.md`](SURFACES.md) | 62 activities across three surfaces | **Superseded** — ACTIVITIES.md contains it and adds the blockers it missed |
| [`CLAUDE-CODE.md`](CLAUDE-CODE.md) | 33 uses of Claude Code | **Superseded** — first pass, kept for the reasoning in its §1 |

**The business model itself is elsewhere and unaffected:** [`MODEL-V2.md`](MODEL-V2.md) is the current model, [`OFFER.md`](OFFER.md) the buildable thing,
[`LTGP.md`](LTGP.md) and [`funnel.py`](scoring/funnel.py) the economics, [`MAP.md`](MAP.md) the ICP and role decision, [`SITE.md`](SITE.md) the
website build, [`ARBITRARY.md`](ARBITRARY.md) the name.

**Surface split:** Code 33 · Cowork 46 · Chat 27. **Code is where the leverage
is; Cowork is where the blockers are.**
