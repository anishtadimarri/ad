# Every Activity — Third Pass, and a Correction to the Ranking

**106 activities across 19 functions.** Up from 62, and the additions are not
detail — they are **whole functions the earlier passes never opened**: entity and banking, Indian
tax and export compliance, employment structure, security and account access, insurance,
attribution, win/loss, and risk.

---

## 1. Why things kept being missed

Every earlier pass ranked by **leverage**, and leverage-ranking has a systematic blind spot:

> **A blocker has modest *value added* and infinite *importance*, because nothing else happens
> until it exists.**

You cannot invoice a US client from India without an entity and a payment rail. You cannot be paid
without a **W-8BEN-E** on file. You cannot place a person without a contract that assigns IP. None
of those *add value* the way a teardown generator does — so a leverage ranking puts them mid-table,
where they sit quietly until the week they stop everything.

So: a `BLOCKER` flag, and **22 of 106 activities carry it.**

---

## 2. Tier 0 — blockers, in rough dependency order

**These are not ranked by score.** They are ranked by what unblocks what.

| # | Function | Blocker | Surface | Why nothing moves without it |
|---|---|---|---|---|
| 1 | Entity | **Choose the payment rail for client payments** | `Chat` | Stripe, Wise, Payoneer, Razorpay — availability depends on the entity decision above, which is why that one comes first |
| 2 | Entity | **Decide the entity structure — India Pvt Ltd, US LLC, or both** | `Chat` | **The first unopened question in this whole repo.** You are in India selling to US buyers. It determines how you invoice, how you are taxed, what a client's procurement will accept, and whether Stripe will take you at all. `FIT`=3 — draft the options, **a CA and a US attorney decide** |
| 3 | Entity | **Payout rail for paying Indian talent** | `Chat` | The other half of the flow, and the half with a monthly deadline |
| 4 | Entity | ****W-8BEN-E** and the US client tax-form pack** | `Cowork` | **A US company cannot pay a foreign entity without this on file.** It will be requested during onboarding of your very first client, and not having it delays cash |
| 5 | Entity | **GST registration and **LUT for export of services**** | `Cowork` | Service exports are zero-rated in India **only with the right filing in place**. Getting this wrong is a real cash cost on every invoice |
| 6 | Entity | **Register the entity and get the identifiers** | `Cowork` | PAN, TAN, incorporation certificate — or the US equivalent |
| 7 | Entity | **Business bank account that can receive USD** | `Cowork` | Nothing else in the model happens until money can land |
| 8 | Employment | ****Decide: are you the EOR, or do you partner with one?**** | `Chat` | **The single largest unanswered structural question left.** Being the EOR means payroll, PF, ESI, gratuity and TDS on your books at $477/employee/month margin. Partnering means sharing that margin but no compliance surface. **The model assumes the revenue and has never priced the obligation** |
| 9 | Employment | **Talent contract — IP assignment, confidentiality, non-solicit** | `Cowork` | **IP assignment is not optional** — you are selling creative output your client will own. Non-solicit is what stops a client hiring your placement directly |
| 10 | Employment | **Contractor vs employee classification for placed talent** | `Chat` | Misclassification is the standard way this category gets into trouble |
| 11 | Pricing | **Rate card and the fee definition** | `Code` | `MODEL-V2.md` gap 1: **the one-time-versus-monthly conflation breaks the model 8× if left ambiguous.** Write it down once, unambiguously |
| 12 | Pricing | **Guarantee terms — 12-month replacement** | `Cowork` | Modelled as **cheaper than the 6-month industry standard** while sounding stronger |
| 13 | Sales | ****Self-reported attribution on the form**** | `Code` | *"How did you hear about us?"* — **once you run two channels, platform-reported attribution will double-count and you will defund the wrong one.** One field, added before the second channel starts |
| 14 | Sales | **MSA and per-placement SOW** | `Cowork` | Draft only, lawyer-reviewed. **Nothing gets signed without it** |
| 15 | Website | **Pixel, CAPI and event verification** | `Code` | **Verify with test events before spending.** Every CAC number assumes attribution works |
| 16 | Measure | **UTM and naming discipline** | `Code` | **Set before the first click or the data is never clean.** Retrofitting is impossible |
| 17 | Outbound | **Cold-email infrastructure — domains, SPF/DKIM/DMARC, warm-up** | `Code` | **2–4 week lead time — the longest in the business.** Start week one even though it sends week four |
| 18 | Outbound | **Email verification and suppression** | `Code` | Bounce above ~2–3% damages the sending domain |
| 19 | Security | ****Client ad-account access protocol**** | `Cowork` | **You will be handed access to clients' Meta ad accounts.** That is the single most sensitive thing in the business. Partner access via Business Manager, never shared logins, 2FA everywhere, and documented revocation on exit |
| 20 | Risk | ****Meta Business Manager structure and ban resilience**** | `Code` | **The severe one, and it is inside your own expertise.** A new advertiser with a new domain and a new page in a scrutinised category is exactly the profile that gets restricted. Separate BM, verified domain, clean page history, a second ad account ready — build it *before* it is needed, because you cannot build it after |
| 21 | Demand | **LinkedIn company page and founder profile** | `Cowork` | **The first thing a Western buyer checks** on an operator with no track record. Free, and it ranks for your brand query |
| 22 | Finance | ****Cash-flow forecast**** | `Code` | **You pay talent monthly and get paid lumpily.** The failure mode that kills placement businesses |

**Read the first six rows as a single chain.** Entity → identifiers → bank → payment rail → payout
rail → W-8BEN-E → GST/LUT. **Every one of them gates the one after it**, and the whole chain gates
your first invoice being paid. In India-to-US services this sequence commonly takes weeks, not
days — which puts it alongside cold-email warm-up as a lead-time item that has to start now.

---

## 3. The full ranking

`IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · `FIT` 16 · `NOW` 12 · `REUSE` 6. **🔒 = blocker.**

| # | Function | Activity | Surface | 🔒 | Imp | Val | Time | Fit | Now | Re | Score | Why |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Meta ads | Build the intent-seed audience from scraped job postings | **Code** |  | 5 | 5 | 5 | 5 | 5 | 5 | **100** | **25% of spend at the best CAC in the model — $489, 9.07:1** |
| 2 | Outbound | Prospect list pipeline | **Code** |  | 5 | 5 | 5 | 5 | 5 | 5 | **100** | Job postings, Ad Library, directories. **Respect each site's terms** |
| 3 | Sales | Teardown generator | **Code** |  | 5 | 5 | 5 | 4 | 5 | 5 | **97** | The money gate. **A product, not a bespoke job** |
| 4 | Strategy | Keep the model live on real numbers, monthly | **Code** |  | 5 | 5 | 4 | 5 | 5 | 5 | **96** | `funnel.py` marks steps 6–9 as assumptions. From week three they are facts, and four inputs re-derive everything downstream in one command |
| 5 | Supply | The graded directory, v0 | **Code** |  | 5 | 5 | 4 | 5 | 4 | 5 | **94** | The retention mechanism — **+$9,022 per client** |
| 6 | Measure | Monthly model re-run and decision memo | **Code** |  | 5 | 5 | 4 | 5 | 4 | 5 | **94** | **Replace assumptions with actuals and re-derive everything** |
| 7 | Risk | **Meta Business Manager structure and ban resilience** | **Code** | 🔒 | 5 | 5 | 4 | 4 | 5 | 5 | **93** | **The severe one, and it is inside your own expertise.** A new advertiser with a new domain and a new page in a scrutinised category is exactly the profile that gets restricted. Separate BM, verified domain, clean page history, a second ad account ready — build it *before* it is needed, because you cannot build it after |
| 8 | Supply | Grading rubric as a scoring tool | **Code** |  | 5 | 5 | 4 | 4 | 5 | 5 | **93** | **Recut an ad, measure 3s and 15s retention against the original.** What makes premium falsifiable |
| 9 | Outbound | Cold-email infrastructure — domains, SPF/DKIM/DMARC, warm-up | **Code** | 🔒 | 5 | 4 | 4 | 5 | 5 | 5 | **92** | **2–4 week lead time — the longest in the business.** Start week one even though it sends week four |
| 10 | Finance | **Cash-flow forecast** | **Code** | 🔒 | 5 | 5 | 3 | 5 | 5 | 4 | **91** | **You pay talent monthly and get paid lumpily.** The failure mode that kills placement businesses |
| 11 | Website | Pixel, CAPI and event verification | **Code** | 🔒 | 5 | 4 | 4 | 5 | 5 | 4 | **90** | **Verify with test events before spending.** Every CAC number assumes attribution works |
| 12 | Sales | Pre-call research brief | **Code** |  | 4 | 4 | 5 | 5 | 5 | 4 | **90** | One page, every call |
| 13 | Pricing | Rate card and the fee definition | **Code** | 🔒 | 5 | 5 | 3 | 4 | 5 | 5 | **89** | `MODEL-V2.md` gap 1: **the one-time-versus-monthly conflation breaks the model 8× if left ambiguous.** Write it down once, unambiguously |
| 14 | Security | **Client ad-account access protocol** | **Cowork** | 🔒 | 5 | 4 | 4 | 4 | 5 | 5 | **88** | **You will be handed access to clients' Meta ad accounts.** That is the single most sensitive thing in the business. Partner access via Business Manager, never shared logins, 2FA everywhere, and documented revocation on exit |
| 15 | Pricing | Guarantee terms — 12-month replacement | **Cowork** | 🔒 | 5 | 4 | 4 | 4 | 5 | 5 | **88** | Modelled as **cheaper than the 6-month industry standard** while sounding stronger |
| 16 | Employment | **Decide: are you the EOR, or do you partner with one?** | **Chat** | 🔒 | 5 | 5 | 3 | 4 | 5 | 4 | **88** | **The single largest unanswered structural question left.** Being the EOR means payroll, PF, ESI, gratuity and TDS on your books at $477/employee/month margin. Partnering means sharing that margin but no compliance surface. **The model assumes the revenue and has never priced the obligation** |
| 17 | Website | `/proof` write-ups — recut ads with retention deltas | **Chat** |  | 5 | 5 | 3 | 4 | 5 | 4 | **88** | **The most important page on the site** |
| 18 | Sales | **Self-reported attribution on the form** | **Code** | 🔒 | 4 | 5 | 3 | 5 | 5 | 5 | **87** | *"How did you hear about us?"* — **once you run two channels, platform-reported attribution will double-count and you will defund the wrong one.** One field, added before the second channel starts |
| 19 | Measure | UTM and naming discipline | **Code** | 🔒 | 4 | 4 | 4 | 5 | 5 | 5 | **87** | **Set before the first click or the data is never clean.** Retrofitting is impossible |
| 20 | Supply | Sourcing pipeline from public portfolios | **Code** |  | 4 | 4 | 5 | 4 | 5 | 4 | **86** | Where the terms permit |
| 21 | Entity | Choose the payment rail for client payments | **Chat** | 🔒 | 5 | 4 | 4 | 4 | 5 | 3 | **86** | Stripe, Wise, Payoneer, Razorpay — availability depends on the entity decision above, which is why that one comes first |
| 22 | Website | Landing-page copy for `/agencies`, `/ecommerce`, `/teardown` | **Chat** |  | 5 | 4 | 4 | 4 | 5 | 3 | **86** | The words convert, not the layout |
| 23 | Supply | Client brief → shortlist of three | **Cowork** |  | 4 | 5 | 4 | 4 | 4 | 5 | **86** | Where the bench turns into revenue |
| 24 | Ops | **SOP capture on anything done twice** | **Cowork** |  | 4 | 5 | 4 | 4 | 4 | 5 | **86** | **The substitute for employees.** What you hand a first hire instead of explaining |
| 25 | Employment | Talent contract — IP assignment, confidentiality, non-solicit | **Cowork** | 🔒 | 5 | 4 | 4 | 3 | 5 | 5 | **85** | **IP assignment is not optional** — you are selling creative output your client will own. Non-solicit is what stops a client hiring your placement directly |
| 26 | Sales | MSA and per-placement SOW | **Cowork** | 🔒 | 5 | 4 | 4 | 3 | 5 | 5 | **85** | Draft only, lawyer-reviewed. **Nothing gets signed without it** |
| 27 | Measure | Weekly metrics review | **Code** |  | 4 | 3 | 5 | 5 | 5 | 4 | **85** | One command, six numbers |
| 28 | Strategy | Scenario-test before committing spend | **Code** |  | 4 | 4 | 4 | 5 | 5 | 3 | **84** | A one-line change, not a debate |
| 29 | Finance | Unit-economics dashboard | **Code** |  | 4 | 4 | 4 | 5 | 4 | 5 | **84** | Six numbers you steer by. A script, not a SaaS |
| 30 | Outbound | Per-prospect personalisation at volume | **Code** |  | 4 | 4 | 5 | 4 | 4 | 4 | **84** | **The part that makes cold email work and does not scale by hand** |
| 31 | Strategy | Expansion screens — next role, next country, next ICP | **Code** |  | 4 | 4 | 5 | 5 | 2 | 5 | **84** | `COUNTRIES.md` and `MAP.md` are the machinery. Re-run, do not rebuild |
| 32 | Meta ads | Meta Ad Library sweep | **Code** |  | 3 | 4 | 5 | 5 | 5 | 3 | **84** | **Long-running ads are the ones that work.** Public data |
| 33 | Entity | Decide the entity structure — India Pvt Ltd, US LLC, or both | **Chat** | 🔒 | 5 | 5 | 3 | 3 | 5 | 3 | **83** | **The first unopened question in this whole repo.** You are in India selling to US buyers. It determines how you invoice, how you are taxed, what a client's procurement will accept, and whether Stripe will take you at all. `FIT`=3 — draft the options, **a CA and a US attorney decide** |
| 34 | Meta ads | Count job postings across every phrasing first | **Code** |  | 4 | 4 | 4 | 5 | 5 | 2 | **83** | `MODEL-V2.md` gap 10. Free, one afternoon, and it decides the ad |
| 35 | Outbound | Email verification and suppression | **Code** | 🔒 | 4 | 3 | 4 | 5 | 5 | 5 | **82** | Bounce above ~2–3% damages the sending domain |
| 36 | Outbound | Sequence writing | **Chat** |  | 4 | 4 | 4 | 4 | 5 | 4 | **82** | Short. One ask. The ask is the paid teardown |
| 37 | Demand | **Brand-defence search campaign** | **Code** |  | 4 | 4 | 4 | 4 | 5 | 4 | **82** | `ARBITRARY.md` §13: searching *all hands talent* returns **three other organisations and not you.** A few dollars a month fixes it. Nobody else bids on your name |
| 38 | Entity | Payout rail for paying Indian talent | **Chat** | 🔒 | 5 | 4 | 3 | 4 | 5 | 3 | **82** | The other half of the flow, and the half with a monthly deadline |
| 39 | Delivery | Onboarding day 0–30 | **Cowork** |  | 5 | 4 | 3 | 4 | 4 | 5 | **82** | Protects **seat continuity, the largest single lever** |
| 40 | Supply | Take-home brief and its scoring sheet | **Cowork** |  | 4 | 4 | 4 | 4 | 4 | 5 | **81** | Consistency *is* the product |
| 41 | Entity | **W-8BEN-E** and the US client tax-form pack | **Cowork** | 🔒 | 5 | 3 | 4 | 3 | 5 | 5 | **81** | **A US company cannot pay a foreign entity without this on file.** It will be requested during onboarding of your very first client, and not having it delays cash |
| 42 | Measure | Cohort and payback analysis | **Code** |  | 4 | 4 | 4 | 5 | 3 | 4 | **81** | Cannot manage seat continuity without it |
| 43 | Entity | GST registration and **LUT for export of services** | **Cowork** | 🔒 | 5 | 4 | 3 | 3 | 5 | 4 | **80** | Service exports are zero-rated in India **only with the right filing in place**. Getting this wrong is a real cash cost on every invoice |
| 44 | Employment | Contractor vs employee classification for placed talent | **Chat** | 🔒 | 5 | 4 | 3 | 3 | 5 | 4 | **80** | Misclassification is the standard way this category gets into trouble |
| 45 | Strategy | Weekly review ritual | **Chat** |  | 4 | 4 | 4 | 4 | 5 | 2 | **80** | Fifteen minutes. The habit matters more than the tool |
| 46 | Sales | **Win/loss analysis** | **Cowork** |  | 4 | 5 | 3 | 4 | 3 | 5 | **79** | **The most-skipped high-value activity in any young business.** Ten lost deals tell you more than a hundred impressions |
| 47 | Delivery | 30/60/90 check-in cadence | **Cowork** |  | 4 | 5 | 3 | 4 | 3 | 5 | **79** | Turns 9 EOR months into 30 |
| 48 | Meta ads | Weekly account read | **Code** |  | 4 | 3 | 5 | 4 | 4 | 3 | **78** | The gain is doing it weekly without losing an evening |
| 49 | Sales | Call script and objection handling | **Chat** |  | 4 | 4 | 3 | 4 | 5 | 4 | **78** | Especially the India objection — `COUNTRIES.md` §9 prices it |
| 50 | Legal | **USPTO Class 35 clearance on *All Hands*** | **Chat** |  | 4 | 4 | 4 | 3 | 5 | 3 | **78** | Outstanding for four rounds. **Two live users of *All Hands* exist in talent services.** Monitoring is agent work; **the opinion is not** |
| 51 | Entity | Register the entity and get the identifiers | **Cowork** | 🔒 | 5 | 4 | 3 | 3 | 5 | 2 | **78** | PAN, TAN, incorporation certificate — or the US equivalent |
| 52 | Entity | Business bank account that can receive USD | **Cowork** | 🔒 | 5 | 4 | 3 | 3 | 5 | 2 | **78** | Nothing else in the model happens until money can land |
| 53 | Content | Case studies with real numbers | **Cowork** |  | 4 | 4 | 4 | 4 | 3 | 4 | **78** | **Only with real numbers.** A fabricated one is worse than none when the positioning is *falsifiable* |
| 54 | Meta ads | **Special Ad Category pre-check** | **Chat** |  | 4 | 4 | 3 | 4 | 5 | 3 | **77** | `SUPPLY-DEMAND.md` §1 prices this at a **10–29% CAC tax** if a B2B ad gets reclassified as employment |
| 55 | Demand | LinkedIn company page and founder profile | **Cowork** | 🔒 | 4 | 4 | 3 | 4 | 5 | 3 | **77** | **The first thing a Western buyer checks** on an operator with no track record. Free, and it ranks for your brand query |
| 56 | Delivery | Time-zone overlap and comms norms | **Cowork** |  | 4 | 4 | 3 | 4 | 4 | 5 | **77** | `COUNTRIES.md` gates ASYNC. Agree the overlap window in writing at kickoff |
| 57 | Finance | Runway and personal burn | **Code** |  | 4 | 4 | 3 | 4 | 5 | 3 | **77** | How many months of no revenue you can absorb. Decide before spending on ads |
| 58 | Measure | Competitor and salary monitor | **Code** |  | 3 | 3 | 5 | 5 | 3 | 5 | **77** | Scheduled diffs. Runs without you |
| 59 | Supply | Screening reels against the rubric | **Chat** |  | 4 | 3 | 5 | 3 | 5 | 2 | **76** | `FIT`=3. It shortlists. **You watch the reel** |
| 60 | Pricing | Payment terms, deposits, late fees | **Cowork** |  | 4 | 4 | 3 | 4 | 4 | 4 | **76** | You pay talent monthly. Terms are a cash-flow instrument, not admin |
| 61 | Supply | English and communication assessment | **Chat** |  | 4 | 4 | 3 | 4 | 4 | 4 | **76** | `COUNTRIES.md` gates on this for a reason — it is the failure mode buyers fear most about India |
| 62 | Website | LP variants per angle | **Chat** |  | 4 | 3 | 4 | 4 | 5 | 2 | **76** | Iterate, do not split-test — `SITE.md` §1 |
| 63 | Delivery | Escalation path for underperformance | **Cowork** |  | 4 | 4 | 3 | 4 | 3 | 5 | **75** | **Before it happens.** Mid-month failure is the moment that decides whether a client renews |
| 64 | Employment | Payroll calendar, payslips, TDS | **Cowork** |  | 4 | 3 | 4 | 4 | 3 | 5 | **74** | Monthly and unforgiving. People leave over late pay |
| 65 | Risk | Client concentration monitor | **Code** |  | 4 | 4 | 3 | 5 | 2 | 4 | **74** | At five clients, one leaving is 20% of revenue |
| 66 | Finance | Invoicing and the monthly EOR run | **Cowork** |  | 4 | 3 | 4 | 4 | 3 | 5 | **74** | $477/employee/month recurring |
| 67 | Ops | Weekly planning and time budgeting | **Chat** |  | 4 | 4 | 3 | 3 | 5 | 3 | **74** | **Attention is the binding constraint in every model in this repo.** Budget it explicitly |
| 68 | Legal | NDAs and mutual confidentiality | **Cowork** |  | 4 | 3 | 4 | 3 | 4 | 5 | **74** | Draft only |
| 69 | Delivery | Seat expansion play | **Chat** |  | 4 | 5 | 2 | 4 | 3 | 3 | **73** | Seats-per-client is where the economics live |
| 70 | Meta ads | Creative concepts and scripts | **Chat** |  | 4 | 3 | 4 | 3 | 5 | 2 | **72** | `FIT`=3. You judge creative better than any agent |
| 71 | Demand | Partnership and referral outreach to adjacent vendors | **Chat** |  | 4 | 4 | 3 | 4 | 3 | 3 | **72** | Agencies that do media buying but not editing are a warm channel |
| 72 | Demand | Referral request loop after a 90-day check-in | **Cowork** |  | 4 | 4 | 3 | 4 | 2 | 5 | **72** | Systematically, not when you remember |
| 73 | Hiring | First VA or recruiter — scope, JD, screening | **Cowork** |  | 4 | 4 | 3 | 4 | 2 | 5 | **72** | Month four to six. **The SOPs are what make this hire cheap** |
| 74 | Measure | Cross-channel lead dedupe | **Code** |  | 3 | 4 | 3 | 5 | 3 | 4 | **72** | Same company from Meta and cold email is one lead, not two |
| 75 | Security | Password manager and device hygiene, for you and every placement | **Cowork** |  | 4 | 3 | 3 | 4 | 4 | 4 | **72** | One compromised placement account is a client-losing event |
| 76 | Hiring | Training material from your own SOPs | **Cowork** |  | 3 | 4 | 4 | 4 | 2 | 5 | **72** | Written once, reused per hire |
| 77 | Sales | Proposal → contract → invoice → kickoff | **Cowork** |  | 3 | 3 | 4 | 4 | 4 | 4 | **71** | Templated so no deal stalls on paperwork |
| 78 | Risk | Written risk register with triggers | **Cowork** |  | 3 | 4 | 3 | 4 | 3 | 5 | **70** | Ad account ban, payment freeze, a bad placement going public, AI substitution. **`DURABLE`=3 is already the model's weakest score** |
| 79 | Outbound | Reply triage and routing | **Cowork** |  | 3 | 3 | 4 | 4 | 4 | 3 | **70** | Four buckets, four responses, none left overnight |
| 80 | Finance | **FX policy — INR cost base, USD revenue** | **Code** |  | 4 | 4 | 2 | 4 | 3 | 4 | **70** | A real margin variable the model does not carry. A 5% move is 5% of gross margin |
| 81 | Meta ads | Budget pacing rules | **Code** |  | 3 | 4 | 3 | 4 | 3 | 4 | **69** | A script that says where money should move |
| 82 | Supply | Bench nurture | **Cowork** |  | 3 | 4 | 3 | 4 | 3 | 4 | **69** | Graded people go cold |
| 83 | Delivery | Client feedback loop | **Cowork** |  | 3 | 4 | 3 | 4 | 3 | 4 | **69** | The input to the grading rubric |
| 84 | Entity | FEMA / FIRC handling for inbound forex | **Cowork** |  | 4 | 3 | 3 | 3 | 4 | 4 | **68** | Your bank will want it. Set the process up once |
| 85 | Strategy | Decision journal | **Cowork** |  | 3 | 4 | 2 | 4 | 4 | 5 | **68** | The repo does this for analysis. Do it for the calls between analyses |
| 86 | Website | Design and mobile QA | **Chat** |  | 3 | 3 | 4 | 4 | 4 | 2 | **68** | Chat, because it needs eyes on the actual page |
| 87 | Finance | Collections chase | **Cowork** |  | 3 | 3 | 4 | 4 | 3 | 4 | **68** | Polite, automatic, escalating |
| 88 | Website | Brand voice guide | **Cowork** |  | 3 | 3 | 3 | 4 | 4 | 5 | **68** | Stops the site, ads and emails sounding like three companies |
| 89 | Supply | Interview structure and reference checks | **Cowork** |  | 3 | 3 | 3 | 4 | 4 | 5 | **68** | Written once |
| 90 | Sales | Pipeline tracking | **Cowork** |  | 3 | 3 | 3 | 4 | 4 | 4 | **67** | A sheet until deal thirty |
| 91 | Website | Legal pages — privacy, terms, cookie notice | **Cowork** |  | 3 | 2 | 4 | 4 | 4 | 4 | **66** | Meta review looks for them, and EU or UK buyers expect them |
| 92 | Meta ads | Ad copy variants in volume | **Chat** |  | 3 | 2 | 4 | 4 | 5 | 2 | **66** | The commodity use |
| 93 | Content | Newsletter from month three | **Cowork** |  | 3 | 3 | 4 | 4 | 2 | 3 | **65** | First number from your first ten placements |
| 94 | Employment | Equipment and software policy for placed talent | **Cowork** |  | 3 | 3 | 3 | 4 | 3 | 4 | **64** | Who buys the laptop and the Adobe licence, and who owns it after |
| 95 | Security | Handling client creative and brand assets | **Cowork** |  | 3 | 3 | 3 | 4 | 3 | 4 | **64** | Where files live, who can see them, what happens at the end |
| 96 | Outbound | LinkedIn outbound — manual | **Chat** |  | 3 | 3 | 3 | 4 | 4 | 2 | **64** | Drafting only. **Do not automate or scrape it** |
| 97 | Demand | Directory listings — Clutch and category directories | **Cowork** |  | 3 | 3 | 3 | 4 | 3 | 4 | **64** | Cheap credibility and a live backlink |
| 98 | Delivery | Replacement request handling | **Cowork** |  | 3 | 3 | 3 | 4 | 3 | 4 | **64** | The guarantee only differentiates if it is fast |
| 99 | Ops | Tool stack and integration decisions | **Chat** |  | 3 | 3 | 3 | 4 | 4 | 2 | **64** | You have already made five |
| 100 | Pricing | Annual increase policy | **Chat** |  | 3 | 4 | 2 | 4 | 2 | 4 | **62** | Decide before the first renewal, not during it |
| 101 | Employment | Talent exit and offboarding | **Cowork** |  | 3 | 3 | 3 | 4 | 2 | 4 | **62** | Access revoked, IP confirmed, client told first |
| 102 | Risk | Professional indemnity / E&O insurance | **Chat** |  | 3 | 3 | 3 | 3 | 3 | 3 | **60** | Larger clients ask. Cheap relative to losing the deal |
| 103 | Legal | Data-protection basics for EU/UK clients | **Chat** |  | 3 | 3 | 3 | 3 | 3 | 3 | **60** | Know it before selling into it |
| 104 | Finance | Bookkeeping prep for the accountant | **Cowork** |  | 2 | 2 | 4 | 4 | 3 | 4 | **59** | Categorise and reconcile. **The accountant still files** |
| 105 | Content | X during launch month | **Chat** |  | 2 | 2 | 4 | 4 | 4 | 1 | **58** | `MODEL-V2.md` gap 11 caps this deliberately |
| 106 | Ops | Inbox and calendar triage | **Cowork** |  | 2 | 2 | 4 | 3 | 4 | 2 | **56** | Real by month six |

### Top 15

1. **Build the intent-seed audience from scraped job postings** — Meta ads · `Code` · 100
2. **Prospect list pipeline** — Outbound · `Code` · 100
3. **Teardown generator** — Sales · `Code` · 97
4. **Keep the model live on real numbers, monthly** — Strategy · `Code` · 96
5. **The graded directory, v0** — Supply · `Code` · 94
6. **Monthly model re-run and decision memo** — Measure · `Code` · 94
7. 🔒 ****Meta Business Manager structure and ban resilience**** — Risk · `Code` · 93
8. **Grading rubric as a scoring tool** — Supply · `Code` · 93
9. 🔒 **Cold-email infrastructure — domains, SPF/DKIM/DMARC, warm-up** — Outbound · `Code` · 92
10. 🔒 ****Cash-flow forecast**** — Finance · `Code` · 91
11. 🔒 **Pixel, CAPI and event verification** — Website · `Code` · 90
12. **Pre-call research brief** — Sales · `Code` · 90
13. 🔒 **Rate card and the fee definition** — Pricing · `Code` · 89
14. 🔒 ****Client ad-account access protocol**** — Security · `Cowork` · 88
15. 🔒 **Guarantee terms — 12-month replacement** — Pricing · `Cowork` · 88

---

## 4. What this pass added that the earlier ones missed

| Missed | Why it matters |
|---|---|
| **The entity and payment chain** | You are in India selling to US buyers and **nothing in this repo had addressed how you get paid.** Seven blockers in sequence |
| **Whether you are the EOR or partner with one** | The model books **$477/employee/month** of EOR margin and has **never priced the compliance obligation** behind it. PF, ESI, gratuity and TDS are not free |
| **Meta account-ban resilience** | A new advertiser, new domain, new page, scrutinised category. **This is the profile that gets restricted** — and it is inside your own expertise, so it is inexcusable to leave to chance |
| **Client ad-account access protocol** | You will hold access to clients' ad accounts. **The most sensitive thing in the business**, and it had never appeared |
| **Self-reported attribution** | The moment you run Meta *and* cold email, platform-reported numbers double-count. **One form field, added before the second channel — or you defund the wrong one** |
| **UTM discipline** | Set before the first click or the data is never clean. Retrofitting is impossible |
| **Win/loss analysis** | The most-skipped high-value activity in any young business. Ten lost deals teach more than a hundred thousand impressions |
| **Escalation path for underperformance** | Mid-month failure is the moment that decides renewal, and there was no process for it |
| **Brand-defence search** | *All hands talent* currently returns three other organisations. A few dollars a month |
| **Runway and personal burn** | How many months of no revenue you can absorb — decided **before** ad spend, not during it |

---

## 5. The split, recomputed

| Surface | Activities | Share | Share of value | Avg |
|---|---|---|---|---|
| **Code** | 33 | 31% | **34%** | 85.7 |
| **Cowork** | 46 | 43% | **41%** | 73.3 |
| **Chat** | 27 | 25% | **25%** | 74.5 |

**Cowork moves up on this pass** — from 21 activities to 46. The reason is the whole
category that was missing: **entity, contracts, compliance, access protocols and SOPs are all
document work.** Of the 22 blockers, 14 are Cowork or Chat.

> **The corrected shape: Code is where the leverage is, Cowork is where the *blockers* are.**
> The earlier passes measured the first and never looked at the second.
