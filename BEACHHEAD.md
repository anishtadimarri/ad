# BEACHHEAD — Three Verticals, One Bench

Ranked on **switch cost**: how many weeks of retraining it takes to move a proven worker from one
vertical to another. Portability is now measured, not asserted.
Companion to [`OFFER.md`](OFFER.md), [`SCALE.md`](SCALE.md), [`MASTER.md`](MASTER.md).
Evidence tags per MASTER §0.

---

## The decision

| | |
|---|---|
| **Verticals** | **E-commerce/DTC · Marketing agencies · SaaS** |
| **Combined ICP** | ~66,000 US businesses |
| **Drop-in roles** (≤1 week to switch vertical) | **6 of 10** |
| **Launch role** | **AR & Collections** — not Ledger & Close. See §0 |
| **Every buyer already employs remote staff** | Non-negotiable gate. §1 |

---

## 0. Two corrections that change the launch plan

### 0.1 Staffing agencies are out — their work does not switch

Staffing had the joint-lowest *friction* of any vertical (4.68) and I recommended it on that
basis. But measured on **switch cost** it is the worst of the six survivors:

| Role | Switch cost into staffing |
|---|---|
| AR & Collections | **2.0 weeks** — VMS portals (Fieldglass, Beeline), weekly billing cycle |
| Payroll processing | **3.0 weeks** — multi-state contractor payroll |
| Ledger & Close | **3.0 weeks** — factoring entries, bill-vs-pay-rate margin |

Adding staffing drops drop-in roles from **6 to 3.** Its low friction is real, and it is bought
by having genuinely specialised back-office work — which is exactly what breaks a shared bench.
**Keep it as a later, standalone vertical. Do not put it in the founding trio.**

### 0.2 The launch role was wrong — Ledger & Close is the LEAST portable role in the set

Every earlier version of this plan said *"launch with Ledger & Close only, add AR later."*

> **Ledger & Close carries the highest fee ($9,300) and the highest switch cost (2.5 weeks). It is
> the one role that does not travel.** AP, bank reconciliation and AR are near-zero switch cost —
> and they are the cheapest roles in the set.

| | Mean fee | Roles |
|---|---|---|
| Drop-in (≤1 wk) | **$6,400** | 6 |
| Vertical-specific (>1.5 wk) | **$7,800** | 2 |

**Portability and fee size are inversely related.** That is a real trade-off, not a rounding error,
and it has to be chosen deliberately:

| Strategy | Launch role | Consequence |
|---|---|---|
| **Maximise fee** | Ledger & Close | $9,300/placement, but a separate bench per vertical |
| **Maximise portability** | **AR & Collections** | $6,000/placement — 35% less — but one bench serves all three verticals and utilisation pools |

**Recommendation: launch on AR & Collections.** At launch, bench utilisation matters more than fee
per placement, because an idle bench is what kills fill rate and fill rate is what kills the model
(OFFER §4). Add Ledger & Close per-vertical once each vertical has its own flow.

---

## 1. Two hard gates, not scored dimensions

Two things were being scored when they should have been filters. Both cost the analysis a wrong
answer before this correction.

### Gate 1 — the buyer must ALREADY be hiring remote

An earlier version of this document recommended **home services** (~70,000 businesses, the biggest
vertical available) on the strength of its size and an un-offshorable technician shortage to sell
against. It scored **`RR` = 3.**

> **`RR` = 3 means the buyer is not yet doing this.** The sale then contains a second, harder sale
> underneath it: convincing a tradesperson owner that remote hiring works at all. That is
> missionary selling — long cycles, high scepticism, and a first cohort of clients who need
> hand-holding you cannot afford to give at launch.

**`RR` must be 5: the buyer already employs offshore staff and needs no education.** Home services
is out, and so is dental, property management, veterinary, restaurants and auto — every vertical
whose owner would have to be converted first.

### Gate 2 — the vertical must keep its books on the same ledger

Ranking on quality × market size puts **medical practices** in every top trio — 90,000 businesses,
strong scores. Also a trap.

> Medical runs on an EHR plus a clearinghouse with its own AR. Dental runs on Dentrix. Property
> management runs on AppFolio/Yardi with trust-accounting rules. Insurance runs on Applied Epic.
> RIAs run on Orion. **Each is a different ledger — a different test, a different bench, a
> different training track. Adding one is starting a second business wearing the same job title.**

**The rule: add verticals that share the ledger, never verticals that share only the role.**

### What survives both gates

Six verticals: e-comm/DTC · marketing agencies · staffing agencies · MSP/IT services · SaaS ·
freight/trucking. All `RR` = 5, all on a QuickBooks/Xero spine.

---

## 2. Friction across all three parties

With size deliberately demoted, the remaining question is friction. Scored 1–5 where **5 = lowest
friction**, across fifteen dimensions in three blocks.

| Vertical | Client | Us | Worker | **Weakest** | Mean | ICP |
|---|---|---|---|---|---|---|
| **E-comm/DTC** | 4.83 | 4.60 | 4.60 | **4.60** | **4.68** | 21,000 |
| **Staffing agency** | 4.83 | 4.60 | 4.60 | **4.60** | **4.68** | 10,000 |
| **Marketing agency** | 4.67 | 4.40 | 4.60 | **4.40** | 4.56 | 30,000 |
| MSP / IT services | 4.67 | 4.20 | 4.40 | 4.20 | 4.42 | 15,000 |
| Freight / trucking | 4.17 | 4.60 | 4.20 | 4.17 | 4.32 | 25,000 |
| SaaS | 4.33 | 3.60 | 4.60 | 3.60 | 4.18 | 15,000 |

**Client friction:** already remote · owner decides (no committee) · needs no education · easy
onboarding · no regulatory blocker · **can afford the fee**
**Our friction:** reachable · supply exists · gradeable · short cycle · simple delivery
**Worker friction:** supply already doing this work · no night shift · no licence needed · large
pay uplift · clear career path

**Trios ranked on the weakest party** — a trio is only as good as its worst friction:

| # | Trio | Weakest | Mean | ICP |
|---|---|---|---|---|
| **1** | **E-comm + Marketing agency + Staffing agency** | **4.53** | **4.64** | 61,000 |
| 2 | E-comm + Staffing agency + MSP | 4.47 | 4.59 | 46,000 |
| 3 | E-comm + Staffing agency + Freight | 4.47 | 4.56 | 56,000 |
| 4 | E-comm + Marketing agency + Freight | 4.47 | 4.52 | 76,000 |

### Why the two obvious candidates lost

**Freight/trucking — dropped on affordability.** It has the deepest existing offshore supply of
any vertical (`SUP` = 5; India and Pakistan already run US dispatch at scale) and 25,000 buyers.
But **92% of carriers run ten trucks or fewer** [V], so a $6,000 placement fee is a hard sell to a
business that size. Affordability is friction, and freight has the worst of any candidate.

**SaaS — dropped on decision speed and supply.** A SaaS company usually has a controller or CFO,
so the decision is a committee rather than an owner. Rev-rec and ASC 606 also raise the skill bar,
thinning supply. Our-side friction of 3.60 is the lowest score in the table.

---

## 3. The three verticals

| | E-commerce / DTC | Marketing agencies | SaaS |
|---|---|---|---|
| **ICP in band** | ~21,000 | **~30,000** | ~15,000 |
| **Who** | $3–30M Shopify/Amazon brands | $1M+ agencies, 10–80 staff | $2–50M ARR, 20–150 staff |
| **Ledger** | QBO/Xero | QBO/Xero | QBO/NetSuite |
| **Connector** | A2X — settlements | Harvest/Productive — WIP, retainers | Stripe/Chargebee — rev-rec |
| **Ad stack** | Meta · Google · GA4 · Klaviyo | Meta · Google · GA4 · Looker (for clients) | Google · LinkedIn · GA4 · HubSpot |
| **Already remote?** | ✅ offshore designers and VAs | ✅ often fully distributed | ✅ remote-native by default |
| **Decision** | Owner | Owner | ⚠️ Controller or CFO — the one committee in the trio |
| **Reachable via** | Storeleads, BuiltWith | Clutch, agency directories | BuiltWith, Crunchbase, job-post signals |

**All three share both spines** — the same ledger *and* the same ad platforms. That is what makes
six of ten roles drop-in.

**SaaS is the weakest of the three and worth naming why:** the decision usually involves a
controller or CFO rather than an owner, so the cycle is longer, and rev-rec raises the skill bar.
It earns its slot on switch cost — its AP, bank rec and AR are near-identical to e-comm's — not on
sales friction. **Sequence it third.**

---

## 4. Roles ranked by switch cost

Switch cost = weeks of conversion training to move a **proven** worker into a new vertical.

| Role | Max switch | Fee at 30% | Verdict |
|---|---|---|---|
| **AP & Invoice Processing** | **0.0 wk** | $5,400 | **Drop-in** — bills, coding, approval routing are identical |
| **AR & Collections** | **0.5 wk** | **$6,000** | **Drop-in · LAUNCH HERE** |
| **Bank & card reconciliation** | **0.5 wk** | $5,400 | **Drop-in** |
| **Financial reporting pack** | **1.0 wk** | $7,200 | **Drop-in** |
| **Payroll processing** | **1.0 wk** | $6,600 | **Drop-in** |
| **Reporting & Analytics (GA4/Looker)** | **1.0 wk** | **$7,800** | **Drop-in · highest-fee portable role · bridges both spines** |
| Email / Lifecycle Ops | 1.5 wk | $6,600 | Near-drop-in |
| Paid Media Operations | 1.5 wk | $7,200 | Near-drop-in — **the founder can grade this personally** (§5A) |
| Compliance & Document Ops | 2.0 wk | $6,300 | ⚠️ **Vertical-specific.** Sales-tax nexus vs W-9s vs SOC 2 are different bodies of knowledge — earlier drafts wrongly called this portable |
| Ledger & Close (senior) | 2.5 wk | $9,300 | ⚠️ **Vertical-specific.** Highest fee, least portable |

**Reporting & Analytics is the standout.** Highest fee of any drop-in role, spans the finance and
marketing spines, gradeable by the founder, and zero escape risk. If one role had to carry the
business, that is the one — not Ledger & Close.

---

## 5. The skill spec — what you screen and test for

### 5.1 The shared core (every role, every vertical)

This is the floor. Common in India, cheap to verify, **not** a differentiator.

| Skill | How you test it |
|---|---|
| **QuickBooks Online** (or Xero) — navigation, journal entries, class/location tracking | Live task in a sandbox file |
| Bank and credit-card reconciliation | Reconcile a deliberately broken month |
| Chart-of-accounts discipline, accrual vs cash | Recode a mis-posted transaction set |
| Month-end close checklist discipline | Close a period against a checklist; note what they skip |
| **Written English** — async, no supervision | Written exception memo, unedited |
| Excel / Sheets — lookups, pivots, basic reconciliation logic | Timed sheet task |

### 5.2 Role 1 — Ledger & Close

**Shared core:** close the month, reconcile everything, accruals/prepaids/deferrals, produce the
financial pack, write variance commentary.

| Vertical | Delta skills — the part nobody else screens for | Rarity |
|---|---|---|
| **E-comm/DTC** | **A2X** or Link My Books · Shopify payout reconciliation · Amazon settlement reports (FBA fees, **reserves**, reimbursements) · **inventory valuation and landed cost** · COGS by SKU · gift cards and deferred revenue · multi-channel | **Rare** |
| **Marketing agency** | **WIP and unbilled revenue** · retainer vs project revenue recognition · **pass-through media spend — gross vs net reporting** · Harvest / Productive / Float time data · contractor cost allocation · project profitability | **Rare** |
| **Staffing agency** | **Bullhorn timesheet → invoice** · gross margin per placement · bill rate vs pay rate · accrued contractor payroll · **AR factoring entries** · perm vs contract revenue recognition | **Very rare** |

> **The three delta skills that are genuinely scarce and genuinely valuable:** inventory and landed
> cost (e-comm), pass-through media plus WIP (agency), and factoring plus multi-state contractor
> payroll (staffing). These are the reason a two-week conversion course is justified, and the
> reason a generalist recruiter cannot screen against you — they do not know these words.

### 5.3 Role 2 — AR & Collections

**Shared core:** invoice, chase, apply cash, aging analysis, dunning sequences, short-pay and
dispute handling, credit memos, DSO tracking.

| Vertical | Delta skills | Note |
|---|---|---|
| **E-comm/DTC** | Chargeback handling · marketplace deductions · wholesale/B2B terms (Faire, Shopify B2B) | Low delta |
| **Marketing agency** | Retainer invoicing · milestone billing · client PO tracking · **media pre-billing** · over-servicing flags | Low delta |
| **Staffing agency** | **Weekly or biweekly invoicing at volume** · timesheet-approval chasing · **VMS/MSP portals — SAP Fieldglass, Beeline, Coupa** · factoring coordination | **Highest-value AR seat of the three** |

**Why staffing AR is the strongest single seat in this trio:** the billing cycle is **weekly, not
monthly**, so transaction volume is 4–5x an e-comm brand's, the work is unambiguous, and VMS portal
invoicing is a genuine specialist pain that firms actively want off their desk. Highest volume,
clearest need, least competition.

### 5.4 Role 3 — AP & Invoice Processing

**Shared core:** bill capture, GL coding, approval routing, vendor master maintenance, payment
runs, 1099 prep, vendor statement recs.

| Vertical | Delta skills |
|---|---|
| **E-comm/DTC** | 3PL invoices · freight and duty reconciliation · supplier PO vs receipt matching · inventory GRN matching |
| **Marketing agency** | Contractor and freelancer payments · **platform invoices (Meta, Google) matched to client pass-through** · software subscription sprawl |
| **Staffing agency** | **Contractor payroll processing** · **multi-state payroll tax** · per-diem and expense · sub-vendor payments |

### 5.5 Role 4 — Compliance & Document Ops

**Shared core:** work a checklist against a rule set, flag exceptions, collect and chase documents,
maintain an audit trail, track expiries.

| Vertical | The rule set |
|---|---|
| **E-comm/DTC** | Sales-tax registrations and nexus tracking · resale certificates · marketplace tax documents · product compliance files |
| **Marketing agency** | Contractor W-9s and W-8BENs · MSAs and SOWs · insurance certificates · 1099 filing |
| **Staffing agency** | **I-9 and E-Verify** · state registrations · workers-comp certificates · background-check tracking · **certification and licence expiry** · client-required compliance packets · ACA reporting |

**Most AI-durable role of the four**, because it is liability-bearing — someone has to be
accountable for an expired certificate, and nobody delegates that to a model.

### 5.6 Hiring bands

| Role | Level | Placed salary [E] | Fee at 30% | Replaces US at [E] |
|---|---|---|---|---|
| **Ledger & Close** | Senior (owns the close) | **$28–34k** | $8.4–10.2k | $85–110k loaded |
| Ledger & Close | Bookkeeper | $20–24k | $6–7.2k | $70–78k loaded |
| **AR & Collections** | Specialist | $18–22k | $5.4–6.6k | $60–70k loaded |
| AP & Invoice Processing | Clerk/specialist | $16–20k | $4.8–6k | $55–65k loaded |
| **Compliance & Document Ops** | Specialist | $18–24k | $5.4–7.2k | $60–72k loaded |

### 5.7 What to recruit against, in order

| Priority | Skill | Why |
|---|---|---|
| 1 | **QBO/Xero + reconciliation + written English** | The floor. No delta skill saves a candidate who fails this |
| 2 | **One vertical delta, deeply** | This is what you sell. Depth in one beats shallowness in three |
| 3 | Excel reconciliation logic | Predicts everything else |
| 4 | Second vertical delta | Add after 6 months on the bench — this is how you build portability |

**Do not recruit for all three verticals at once.** Hire for e-comm depth, then cross-train the
proven performers onto the agency and staffing connectors. A person who has closed twelve e-comm
months is a safe bet on an agency month; a person hired to know all three knows none of them.

---

## 5A. The second spine — marketing operations

The four roles in §4 are all finance and compliance. **That is an artefact of how the gate was
written, not a finding.** Once "shared QuickBooks ledger" became the portability test, only ledger
roles could survive it. A second spine exists and was excluded by construction.

### 5A.1 The ad-platform stack is equally portable

| Vertical | Marketing stack |
|---|---|
| **E-comm/DTC** | Meta Ads Manager · Google Ads · GA4 · Klaviyo · Shopify |
| **Marketing agency** | Meta · Google Ads · GA4 · Looker Studio — **for clients** |
| **Staffing agency** | Meta · Google · LinkedIn/Indeed job ads · HubSpot nurture |

**Meta Ads Manager is Meta Ads Manager. GA4 is GA4.** The platform does not change by vertical —
only the objective does. That is exactly the portability argument made for QuickBooks, and it holds
just as well here.

### 5A.2 The correction — strategy is not execution

Earlier passes scored **"media buyer" at `RET` = 1** on escape risk (a good one goes direct to
clients at 3–5x) and let the gate kill the entire marketing function.

> **That risk belongs to the strategy layer only** — the person who owns the client relationship
> and could leave with it. It does not apply to campaign operations, reporting, or email build and
> QA, where there is no client relationship to take and no book of business to walk out with.
>
> Placing into an **agency** reduces it further: an agency is a media buyer's career ladder, so the
> seat is a promotion path rather than a dead end.

Splitting the function properly:

| Vertical | Role | Score | Verdict |
|---|---|---|---|
| **Marketing agency** | **Reporting & analytics (client dashboards)** | **81.2** | Highest-scoring pair in the entire study |
| E-comm/DTC | Reporting & analytics (GA4/Looker) | 80.4 | |
| Marketing agency | Email / marketing automation ops | 80.0 | |
| Marketing agency | Paid media **operations** (client campaigns) | 79.2 | |
| E-comm/DTC | Paid media **operations** (build/traffic/QA/pace) | 78.8 | |
| E-comm/DTC | Email / lifecycle ops (Klaviyo build + QA) | 78.8 | |
| Staffing agency | Recruiting analytics & pipeline reporting | 77.6 | |
| Staffing agency | Candidate nurture & CRM ops | 76.8 | |
| Staffing agency | Recruitment media ops (job ads, nurture) | 76.0 | |
| Marketing agency | ~~Media BUYER (owns strategy + client)~~ | 73.4 | ⛔ `RET` — gate stands |
| Marketing agency | ~~Designer / video editor~~ | 64.8 | ⛔ `RET` — gate stands |

*Reference: e-comm Ledger & Close scores 81.6.* **Marketing operations roles are not a
consolation prize — they score level with the finance roles.**

### 5A.3 The three marketing roles, specified

| Role | Shared core | Vertical delta |
|---|---|---|
| **Reporting & Analytics** | GA4, Looker Studio, platform reporting APIs, dashboard build, data QA, anomaly flagging | E-comm: ROAS/MER, cohort and LTV · Agency: client-facing dashboards, multi-account · Staffing: source-of-hire, req pipeline, time-to-fill |
| **Paid Media Operations** | Campaign build, audience and creative trafficking, naming conventions, budget pacing, QA checklists, platform hygiene. **Never strategy** | E-comm: catalogue/feed, Advantage+ · Agency: multi-client under one BM, approvals · Staffing: job-ad campaigns, geo/role targeting |
| **Email / Lifecycle Ops** | Template build, segmentation, flow QA, deliverability hygiene, send-and-report | E-comm: Klaviyo flows, abandoned cart · Agency: HubSpot/Marketo automation · Staffing: candidate nurture sequences |

### 5A.4 Why this spine matters more than its score

**It is the only place the founder's own skill converts into an unfair advantage.**

Nothing in the finance spine uses it. But a media buyer can grade a paid-media-ops candidate in
twenty minutes — read their campaign structure, spot the naming chaos, see whether they understand
pacing — and **no competitor in this category can do that** (MASTER §7.6, the founder-as-academy
exception). The assessment is free for us and impossible for them.

### 5A.5 But do not run both spines at once

Two spines means two benches, two tests, two training tracks and two outbound narratives. That is
precisely the operational intensity being pruned everywhere else in this plan.

| Phase | Spine | Why this order |
|---|---|---|
| **1** | **Finance** — Ledger & Close, then AR | The client's pain is quantified and unambiguous, the buyer's alternative is an unfilled vacancy, and the work is binary right/wrong. Easiest to satisfy, easiest to guarantee |
| **2** | **Marketing ops** — Reporting & Analytics first | Add once finance is proven. Start with reporting, not paid media: it is the highest-scoring role available, the most gradeable, and has no escape risk at all |

**Reporting & Analytics is the right bridge role** — it sits between both spines (it is data work,
not creative work), it scores 80.4–81.2, it is fully portable across all three verticals, and the
founder can grade it personally.

---

## 6. What this does to the numbers

| | E-comm only | **Three verticals** |
|---|---|---|
| ICP | ~21,000 | **~61,000** |
| Offshore-willing finance hires/yr [E] | ~4,100 | **~11,900** |
| Share needed for $20M (989 placements) | 24% ❌ | **8.3%** ✅ |
| Share needed for $5M | 14% ⚠️ | **4.9%** ✅ |

**This still fixes the ceiling problem in OFFER §2.3**, just less dramatically than the
home-services version. $20M needs **8.3%** of annual offshore-willing hiring across the three —
a demanding but normal competitive share, against 24% for e-comm alone.

**And note the quality of that 8.3%:** every one of those hires is at a company that already
employs someone remote. There is no education cost buried in the CAC.

---

## 7. Sequencing

| Stage | Vertical | Why this order |
|---|---|---|
| **1** | **E-commerce/DTC** | Best reachability of the three — Storeleads and BuiltWith name every US Shopify Plus merchant running A2X. Prove fill rate and CAC where targeting is easiest |
| **2** | **Staffing agencies** | Zero education needed, shortest cycle, dense referral network, and you understand the buyer natively. Smallest ICP, so it is a margin and proof play rather than a volume play |
| **3** | **Marketing agencies** | Largest of the three at 30,000 and the most whitespace, but supply for agency WIP/retainer accounting is thinner — go once the bench has depth |

**Roles within each vertical:** launch **Ledger & Close** only. Add **AR & Collections** once the
bench has depth — it is the easiest second seat to sell into an existing client, and
seats-per-client is what makes CAC efficient.

---

## 8. What could break this

| Risk | Severity | Note |
|---|---|---|
| **Three verticals dilutes the narrowness that made the offer work** | **High** | Narrowness is the moat — the free graded shortlist from a warm bench. Mitigation: the *spine* stays narrow. One ledger, one test. Never add a vertical on a different ledger |
| Staffing agencies disintermediate us | Medium | Their recruiters are US-market specialists with no Indian sourcing capability. Many already buy offshore support |
| Three outbound motions instead of one | Medium | Each needs its own list source and creative. Real cost, paid for by the ICP multiple |
| Positioning becomes generic | Medium | Three vertical landing pages, three lists, one delivery engine. Never *"we place accountants"* — always *"we place e-comm accountants"* on one page and *"we place agency finance"* on another |
| Combined ICP is only 2.9x, not 5.8x | Low-medium | Deliberate. Bought with the remote-readiness gate |
| Bench specialisation erodes | Low | Roles 2 and 3 need no delta; only role 1 does |

**The discipline in one line:** *never sell to a buyer who has to be convinced that remote works,
and never add a vertical that keeps its books somewhere else.*
