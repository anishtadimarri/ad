# THE OFFER — E-Commerce Bookkeeper Placement

**One skill. One supply geography. One demand ICP. Designed to survive 6-month attrition.**

**Headline economics: 4.01:1 at 30 days · 7.51:1 lifetime** — modelled in
[`scoring/offer_model.py`](scoring/offer_model.py) on a pessimistic 50% replacement rate.

Analysis, market data and the reasoning that selected this sit in [`MASTER.md`](MASTER.md).
This document is the buildable thing. Evidence tags per §0 of MASTER: **[V]** verified ·
**[E]** estimate · **[C]** company claim · **[?]** assumption.

---

## 1. Why this role, when it isn't the top-scored one

The model (MASTER §7) ranks Recruiter 1st and Bookkeeper 2nd. This offer picks bookkeeping, for
three reasons the score doesn't capture.

### 1.1 Satisfiability is not in the scoring model

"Easy to satisfy the client on" runs on different variables than role quality:

| Determinant | Why it decides satisfaction |
|---|---|
| **What the client's alternative is** | Baseline = *unfilled vacancy + growing backlog* → anything is a win. Baseline = *a good $95k person who just left* → high bar. **This dominates** |
| **Client-side SOP already exists** | Documented process → the worker plugs in. Disorganised client → their chaos becomes your quality problem |
| **Is "good" defined** | Reconciliation has a right answer. "Good EA" shifts weekly |
| **Time to first visible win** | One clean month-end close (week 2) vs. a quarter before a financial plan proves out |
| **Is failure recoverable** | A bad month of books gets fixed. A bad month of customer-facing work loses customers |
| **Does output depend on the client's own team** | If it does, you don't control your own performance review |

**Satisfiability ranking:**

| Role | Satisfiability | Why |
|---|---|---|
| **Insurance processing** (COI, policy check, endorsements) | **Easiest** | Most binary output in the taxonomy — the contract states what the COI must say. Existing workflow, permanent backlog baseline |
| **Bookkeeping / AP-AR / reconciliation** | **Easiest** | Binary, books already exist, first clean close lands week 2, failure recoverable |
| CAD drafting | Easy | Binary, short feedback cycle, low stakes per drawing |
| Medical coding | Easy-medium | Accuracy is a percentage — but compliance stakes make failure less recoverable |
| Steel detailing | Medium | Perfectly binary, but long feedback cycle and a fabrication error costs real money |
| Email/lifecycle · Amazon PPC | Medium-hard | Measurable, but baseline is "our current agency" and outcomes are multi-causal |
| **Recruiter** | **Medium-hard** | ⚠️ Output depends on the *client* running interviews and making competitive offers. Judged on a number you half-control |
| EA | Hardest | "Good" undefined, purely judgment, fully collaborative |

> **The tension:** Recruiter scores #1 and is mid-to-hard to satisfy. For a first business with no
> track record, **satisfiability should outrank score** — the first ten clients are the only proof
> that will ever exist, and they must be delighted rather than merely served.

### 1.2 The crowding is at the wrong buyer

Bookkeeping is the most contested lane — but TOA Global (4,180 professionals, 1,100+ firms [V])
and Entigrity (3,000+ professionals, 600+ CPA firms [V]) both sell to **accounting firms**. The
direct SMB buyer hiring its own in-house bookkeeper is far less served, and far more reachable on
paid social. Same delivery, different buyer, uncontested lane.

### 1.3 Narrowing to e-commerce is what makes it easy to satisfy

The same six platforms every time — Shopify, Amazon Seller Central, Stripe, QuickBooks Online,
A2X, Gusto. Standardised work is gradeable work, and gradeable work is satisfiable work. A
generalist SMB bookkeeper faces a different chart of accounts every engagement.

---

## 2. The two ICPs

### 2.1 Demand — who buys

| | |
|---|---|
| **Who** | US e-commerce brand, $2M–30M revenue, 10–60 staff |
| **Stack** | Shopify and/or Amazon, Stripe, QuickBooks Online or Xero |
| **The pain** | Month-end close takes three weeks · inventory and COGS are wrong · true per-product margin is invisible · cash forecasting is guesswork |
| **Their alternative today** | (a) a $75–95k in-house hire they can't justify, (b) a $1,500–3,000/mo outsourced firm that's slow and impersonal, or (c) the founder's spouse in QuickBooks at 11pm |
| **Why they're reachable** | The most paid-social-native buyer segment in existence. They self-identify, they're already on Meta, and they buy software and services online without a procurement process |
| **Why they're remote-ready** | `RR` = 5. This buyer already has a designer in Manila and a VA in Cebu |

### 2.2 Supply — who we place

| | |
|---|---|
| **Who** | Indian B.Com / M.Com / CA-Inter, 2–5 years on US books in a KPO or Indian CA firm |
| **Skills** | QuickBooks Online or Xero fluent, strong written English, US GAAP basics |
| **Current earnings** | ₹35,000–60,000/month ≈ **$5,000–8,600/year** [E] |
| **Why they want this** | A direct US employer instead of a KPO seat where the agency keeps 60% of the billing. PH/India workers earn **2–5x local rates** working internationally [V] |
| **Why supply is deep** | India = bookkeeping, accounting, legal, technical [V]. India ITeS attrition is **11–18%** [V] — the best in the dataset for async back-office work |
| **The gap to close** | They know QuickBooks. They mostly **don't** know Shopify/A2X inventory and COGS mechanics. ~2 weeks. This is the *named gap blocking a named role* that MASTER §9.6.3 permits a conversion course for — not a school |

### 2.3 ICP size — and the revenue ceiling this niche imposes

**The hiring trigger is the headcount curve, not revenue itself.** Below ~$3M a brand's G&A is
1–2 people and a $1,500/mo bookkeeping firm covers it. Above ~$30M they hire a US controller and
you are selling to a CFO.

| Revenue | Total FTEs [V] | Finance situation |
|---|---|---|
| $1M | 3–6 | Founder or spouse in QuickBooks. **Too small** |
| **$3–5M** | **8–15** | **First dedicated finance hire — the trigger** |
| $10M | 15–25 | Has finance, wants a second seat |
| $25M | 30–45 | US controller, offshore staff beneath |
| $50M+ | 60–80 | In-house team. **Too big** |

*"The curve flexes between $5M and $25M. Revenue per FTE roughly doubles in that band."* [V]

**Sizing:**

| | Count |
|---|---|
| Shopify Plus merchants, global | **47,000 live sites / 50,644 merchants** [V] |
| US share at ~45% | ~21,600 [E] |
| Amazon sellers at $1M+, global | **100,000+**; 30,000 FBA crossed $1M in 2026 [V] |
| US share at ~50% | ~50,000 [E] |
| Union, netting ~35% overlap | ~46,500 [E] |
| **In the $3–30M band (~45%)** | **~21,000** ← the ICP [E] |

*Context: 75% of US DTC brands do under $1M in online sales [V], which is why the band is narrow.*

**Stock is not demand.** At ~1.5 finance seats per brand turning over every 2.5 years [?]:

| | Per year |
|---|---|
| Finance hiring events across the ICP | ~12,600 [E] |
| Offshore-willing today (30–35% adoption [V]) | **~4,100** |
| Offshore-willing by 2028 (50%+ [V]) | ~6,300 |

**Share required, at $8,829 blended revenue per placement:**

| Target | Placements/yr | Per month | Share of offshore-willing demand |
|---|---|---|---|
| $1M | 113 | 9 | 2.8% |
| **$3M** | **340** | **28** | **8.3%** ✅ |
| $5M | 566 | 47 | 13.9% ⚠️ |
| **$10M** | **1,133** | **94** | **27.7%** ❌ |

> ⚠️ **E-comm accountants alone caps at $3–5M.** $10M would require capturing 28% of every
> offshore-willing finance hire in the entire US e-commerce mid-market — a monopoly, not a niche.
> This is the right **wedge** and the wrong **ceiling**. Reaching $10M requires a second role
> (e-comm ops, Amazon PPC) or a second vertical (agencies, SaaS), added once the first is proven.
> Do not build the org for a number the niche cannot produce.

### 2.4 Country selection

| Country | For e-comm finance specifically | Verdict |
|---|---|---|
| **India** | **528,000+ active Chartered Accountants** · 30-year US GAAP/IRS ecosystem · most mature ISO 27001/SOC 2 infrastructure globally [V]. Cheapest. Worst timezone | **Primary** |
| **Philippines** | **US GAAP trained into the education system** · near-native American English · QuickBooks/Xero standard · up to 80% savings [V]. Manila attrition 40–60% [V] — recruit Cebu/provincial | **Overlap option** |
| South Africa | Native English, partial US overlap, attrition 20–30% [V]. Thinner accounting pipeline | Reserve |
| LatAm | Real-time overlap for month-end close, lower error rates, familiar tax structures [V]. **But 50–60% savings vs Asia's 65–75%** [V] — materially more expensive | Only on demand |
| **Prague / CEE** | ❌ **Wrong expertise** — Poland/Czech depth is **IFRS and European regulatory**, not US GAAP [V]. Also the most expensive. Somewhere uses Eastern Europe for tech and creative, not US bookkeeping | **Drop** |

**India primary** — 528,000 CAs and a 30-year US GAAP ecosystem is an unmatchable pool, it is the
cheapest, and it is the operator's home market, which makes sourcing, grading and the EOR line
(§4) structurally cheaper for us than for any competitor.

**Expect timezone to be the most common objection and expect clients to ask for LatAm.** The
honest counter is that month-end close is async and the 4-hour IST window covers their morning.
Having a Philippines option is cheaper than losing the deal.

### 2.5 Why a client picks us over Somewhere or Oceans

| | Somewhere | Oceans | **Us** |
|---|---|---|---|
| Focus | 18+ countries, dozens of roles [V] | EA-first, Sri Lanka only [V] | **E-comm finance only** |
| Price | 25–35% one-time [V] | $3,000/mo managed [V] | 30% one-time |
| Recruiter knows what A2X is | ❌ | ❌ | ✅ |
| Candidates who have closed Shopify books | Maybe | Unlikely | **Every one** |

**Their structural weakness: a generalist recruiter cannot screen for domain skill they do not
have.** Somewhere sends "an accountant"; the client discovers in month two that the person has
never seen a Shopify payout reconciliation or a landed-cost calculation.

**The move that wins the deal:**

> *"Send us last month's Shopify payout file and your inventory sheet. Three of our candidates
> will reconcile it. Compare their actual work — not their résumés — then decide."*

Nobody in this market does this. It costs two bench-candidate hours, it is the strongest proof
mechanism available to a company with no track record, and it is **structurally unavailable to a
generalist** because their bench is not domain-specific.

### 2.6 Channels for this ICP

Their tech stack is public — Storeleads, BuiltWith and the Shopify app store yield a **named list
of every US Shopify Plus merchant running A2X and Gusto.** That is a cold-email and LinkedIn list,
not an ad audience. Meta is not the best channel for this ICP.

| Channel | Why | Expected CAC [E] |
|---|---|---|
| **Stack-scraped cold email** | You can name every A2X user in the US. Perfect targeting, near-zero media cost | **$400–800** |
| Meta | Most paid-social-native buyer alive, but B2B targeting is imprecise. Needs broad targeting plus a self-qualifying hook | $600–1,200 |
| Newsletter / podcast sponsorship | 2X eCommerce, DTC Newsletter, eCommerceFuel. **How Somewhere and Oceans actually grew** [V] | $500–1,000 |
| Communities | eCommerceFuel (vetted $1M+ owners), Amazon seller groups, ops Slacks | Low, slow |
| **Partnerships** | E-comm accounting firms turning away work because they cannot hire · 3PLs · Shopify agencies · A2X · fractional CFO shops | **$200–500** |

**Partnerships are the highest-leverage and slowest line.** An e-comm accounting firm whose
constraint is hiring is the best referral partner in this market — their bottleneck is your
product.

---

## 3. The offer

Two tiers. **Lead with the accountant** — §4.3 shows placed salary is the single biggest lever on
LTGP:CAC, and the fee scales with it while COGS does not.

> ### Your next e-commerce accountant. $34,000 a year, not $120,000.
>
> Owns your close, your inventory and COGS, and your real product margin.
> Knows Shopify, Amazon and A2X. **Three graded candidates in 48 hours — interview them free.**

| Tier | Role | Placed salary | Fee (30% + 5%) | Replaces a US hire at |
|---|---|---|---|---|
| **Lead** | E-comm **accountant** — owns the close | **$34,000** | $10,200 + $1,700 | $79,172 base → **$110–135k loaded** [V/E] |
| Entry | E-comm **bookkeeper** — reconciliation, AP-AR | $22,000 | $6,600 + $1,100 | $55,893 base → **~$75k loaded** [V/E] |

| Term | Spec |
|---|---|
| **Fee** | **30% at start + 5% at month 12** if still employed |
| **Salary transparency** | Client sees the exact figure the worker receives. No hidden spread |
| **Stay Bonus escrow** | **$2,500** (~7% of salary), funded by the client, held and disbursed by us |
| **Engagement deposit** | **$500**, credited in full against the fee |
| **Shortlist** | 3 graded candidates in 48 hours. Free, no commitment |
| **Time to start** | 7–21 days [V — matches Somewhere] |
| **Guarantee** | 6-month conditional free replacement (§5.3) |
| **Overlap** | 4 hours, IST afternoon → US morning. **Never a night shift** |
| **Employment** | Client employs directly. We are the recruiting intermediary, not the employer |

### 3.1 The fee structure is a priced choice, not a free win

§4.3 prices it: splitting 35% into 30%+5% surrenders $1,700 of certain cash to gain **$680
expected** (5% × $34k × 40% survival at 12 months). That is a **~$1,020 expected loss per
placement.**

It buys three things — the client sees our incentive aligned to retention on the term sheet, it
de-risks them at peak scepticism of an unknown vendor, and retention becomes revenue rather than
only cost. For a founder with no track record that is worth buying.

| Stage | Structure | Why |
|---|---|---|
| **First ~20 placements** | **30% + 5%** | No case studies exist. Buy the trust; it costs ~$1,020/placement |
| **After case studies land** | **35% single-stage** | §4.1 C5 — best 30-day ratio of any configuration at 4.17:1 |

The 30% upfront must clear the 30-day payback **on its own**, and it does (§4.1). The month-12
tail is upside, never load-bearing — this respects the hard constraint in MASTER §3.1.

### 3.2 What the front end is, and what it is not

**It is not a paid attraction offer.** §4.3 shows a $297 SLO costs −0.64 on the 30-day ratio: the
back end generates ~$612 of revenue per lead, an SLO recovers ~$24, and it discards 92% of the
funnel to do it. **The free graded shortlist is the attraction offer** — ~$170 to deliver, and its
job is throughput, not spend recovery.

## 4. Unit economics

Modelled in [`scoring/offer_model.py`](scoring/offer_model.py); full output in
[`scoring/OFFER-MODEL.md`](scoring/OFFER-MODEL.md). Ten configurations share one funnel and cost
engine and differ only in offer terms.

**Assume the pessimistic attrition case is true** — median offshore tenure ~6 months
[C — Oceans' claim, self-serving, modelled as if true], giving a **50% replacement rate**.

### 4.0 Corrections made to the first version of this model

Recorded because the first run produced 12.6:1, which was wrong.

| Error | Fix |
|---|---|
| Lead → intake call held at **40%** | That is an inbound referral rate. A cold Meta B2B lead is low-intent: **20%** |
| COGS **flat** at ~$538/placement regardless of salary | A $34k senior search is not a $22k bookkeeper search. Now scales: search labour 3.5% of salary, candidate ads 1.5%, shortlist grading 0.5% per *search* |
| Guarantee reserve flat at $700 × rate | A refund on a $10,200 fee is not a $700 event. Now includes refund exposure at 15% of claims |
| No sales labour in CAC | Intake calls are held by a human. $60/call, ~3.4 calls per placement |

### 4.1 Configurations

| Config | Salary | Fee | 30-day GP | GM | CAC | **30-day** | Lifetime GP | **Lifetime** |
|---|---|---|---|---|---|---|---|---|
| C1 as originally written | $22k | 25%+5% | $3,045 | 55% | $1,867 | **1.63:1** | $5,908 | 3.16:1 |
| C2 + $500 deposit | $22k | 25%+5% | $3,087 | 56% | $1,889 | 1.63:1 | $5,984 | 3.17:1 |
| C3 senior tier | $26k | 25%+5% | $3,607 | 55% | $1,867 | 1.93:1 | $6,998 | 3.75:1 |
| C4 senior tier | $34k | 25%+5% | $4,733 | 56% | $1,867 | 2.54:1 | $9,179 | 4.92:1 |
| **C5 single-stage fee** | **$34k** | **35%** | **$7,779** | **65%** | $1,867 | **4.17:1** | $14,002 | 7.50:1 |
| C6 split fee + deposit | $34k | 30%+5% | $6,321 | 62% | $1,889 | 3.35:1 | $12,039 | 6.37:1 |
| C7 + protection 30% | $34k | 30%+5% | $6,321 | 62% | $1,889 | 3.35:1 | $12,787 | 6.77:1 |
| **C8 + 20% two-seat** | **$34k** | **30%+5%** | **$7,586** | **62%** | $1,889 | **4.01:1** | **$14,183** | **7.51:1** |
| C9 with $297 SLO | $34k | 30%+5% | $6,256 | 61% | $3,066 | 2.04:1 | $11,921 | 3.89:1 |
| C10 heavy deferral | $34k | 20%+20% | $3,209 | 47% | $1,867 | 1.72:1 | $8,418 | 4.51:1 |

### 4.2 Which lever actually moves the ratio

Each row changes exactly one thing from C1.

| Lever | 30-day | vs C1 | Lifetime | vs C1 |
|---|---|---|---|---|
| **Placed salary $22k → $34k** | 2.54:1 | **+0.90** | 4.92:1 | **+1.75** |
| **Fee 25% → 35% upfront** | 2.69:1 | **+1.06** | 4.84:1 | **+1.67** |
| 20% take two seats | 1.96:1 | +0.33 | 3.54:1 | +0.37 |
| Protection attach 30% | 1.63:1 | +0.00 | 3.57:1 | +0.40 |
| Add $500 deposit | 1.63:1 | −0.01 | 3.17:1 | −0.02 |
| **Add a $297 SLO** | **0.99:1** | **−0.64** | 1.93:1 | **−1.24** |

### 4.3 Four findings

**Salary tier is the single biggest lever.** The fee scales linearly with salary; COGS scales
sub-linearly. Same funnel, same CAC, 55% more gross profit. **Place accountants, not bookkeepers.**
The supply exists — MASTER §4.3 has senior offshore accountants at $24–48k [V].

**An SLO is wrong for this business, and this contradicts the original brief.** The back end pays
$10,200 at ~6% of leads = **$612 of revenue per lead**. An SLO at 8% take × $297 = **$24 per
lead**, and it discards 92% of the funnel to collect it. When the back end is this large the front
end's job is *throughput*, not spend recovery. The free graded shortlist **is** the attraction
offer: it costs ~$170 and it converts.

**The tenure-split fee is cash-negative, and §3.1 did not price it.** C5 (35% upfront) beats C6
(30%+5%) on *both* horizons. You surrender $1,700 of certain cash to gain 5% × $34k × 40% survival
= **$680 expected** — a **~$1,020 expected loss per placement.**

> It remains defensible as a *trust purchase* for a founder with no track record. But it is a
> purchase, not alignment for free. **Recommendation: run 30%+5% for the first ~20 placements
> while you have no case studies, then move to 35% single-stage.**

**CPL is ~6x more dangerous than attrition.** Replacement rate 15%→70% moves the ratio 4.73 →
3.60 (−1.13). CPL $50→$250 moves it 8.55 → 2.02 (−6.53). Much of the design effort in §5 targets
attrition; the model says media cost is the larger risk.

### 4.4 Sensitivity — C8

**CPL × replacement rate** (⚠️ = below the 1.5:1 constraint)

| | repl 15% | repl 30% | repl 50% | repl 70% |
|---|---|---|---|---|
| **CPL $50** | 8.55:1 | 7.99:1 | 7.25:1 | 6.51:1 |
| **CPL $100** | 4.73:1 | 4.43:1 | **4.01:1** | 3.60:1 |
| **CPL $150** | 3.27:1 | 3.06:1 | 2.78:1 | 2.49:1 |
| **CPL $200** | 2.50:1 | 2.34:1 | 2.12:1 | 1.90:1 |
| **CPL $250** | 2.02:1 | 1.89:1 | 1.72:1 | 1.54:1 |

**Breakeven at 1.5:1 sits near CPL $255** at a 50% replacement rate. Real headroom — but CPL is
the number to watch weekly.

**Fill rate**

| Fill rate | CAC | 30-day | Lifetime |
|---|---|---|---|
| 80% | $1,551 | 4.92:1 | 9.19:1 |
| **60%** | **$1,889** | **4.01:1** | **7.51:1** |
| 40% | $2,834 | 2.63:1 | 4.93:1 |
| 30% | $3,779 | 1.94:1 | 3.64:1 |

**The two unmeasured funnel rates** — lead→intake × intake→search

| | search 30% | search 40% | search 50% | search 60% |
|---|---|---|---|---|
| **intake 25%** | 2.93:1 | 3.91:1 | 4.89:1 | 5.87:1 |
| **intake 20%** *(modelled)* | — | — | **4.01:1** | — |
| **intake 30%** | 3.43:1 | 4.57:1 | 5.72:1 | 6.86:1 |
| **intake 40%** | 4.35:1 | 5.80:1 | 7.25:1 | 8.70:1 |

### 4.5 The moral hazard in the lifetime number

Lifetime assumes **45% of clients buy a paid replacement** once the guarantee lapses [?]. So
roughly **a fifth of lifetime gross profit is funded by the attrition we promise to prevent.**

This is a real conflict, not a rhetorical one. Two mechanisms push against it deliberately: the
Stay Bonus (§5) and the month-12 tail fee — which is a second, non-economic argument for keeping
the tail despite §4.3 showing it is cash-negative. **Never build a growth plan that requires
churn.** If lifetime economics ever depend on replacements, the offer has stopped being
win-win-win.

### 4.6 On the 62% gross margin vs 28% EBITDA

MASTER §13.1 models 28% EBITDA at $5M revenue. Both are right: LTGP:CAC counts only COGS and
CAC. Delivery management, leadership, finance, legal, tooling and unbilled recruiter capacity all
sit below the gross line. A 4:1 gross ratio and a 28% net margin are consistent.

## 5. The retention architecture

In a handoff model there is no post-placement lever on the worker. Every mechanism must therefore
be built into the offer *at signature*. Ranked by actual force:

| # | Mechanism | How it works | Attacks |
|---|---|---|---|
| **1** | **Stay Bonus — client-funded, we escrow** | Client escrows $2,500 at placement. Worker receives $800 at month 6, $800 at 12, $900 at 18, disbursed by us. Costs the client ~7% of one year's salary against ~$11,900 to re-hire | Everything. **The only mechanism with direct financial force** |
| **2** | **Fee split by tenure** (§3.1) | Our 5% tail at month 12 | Our own incentive misalignment |
| **3** | **Published 9% annual raise**, we administer | Worker's pay tracks the market without them leaving to get it | India BPO wage inflation of **9.5%/yr** [V] |
| **4** | **Async by design — 4h overlap, never nights** | IST afternoon covers US morning | The largest attrition split in the dataset: Manila 40–60% vs India ITeS 11–18% [V] |
| **5** | **Named ladder agreed at intake** | Client commits to Bookkeeper → Senior → Accounting Lead with salary bands. Costs the client nothing to promise | Dead-end perception |
| **6** | **Monthly peer cohort call** across all placed workers | 45 minutes, we host | Isolation of the solo embedded seat |
| **7** | **Client onboarding contract** | Named manager, documented SOP handover, 30/60/90 check-ins | Client neglect — a leading cause we must not underwrite |

### 5.1 Honest assessment of the retention stack

**Mechanism 1 has real force. The rest are friction reduction.** Every one attacks a driver with
evidence behind it, but only the Stay Bonus changes the worker's arithmetic. Whether this moves
median tenure from 6 months to 18 is **[?]** — unknown and unknowable before ~30 placements have
aged 12 months.

**Design consequence:** the offer must be profitable *assuming the stack fails*. §4 models exactly
that. If the stack works, the ratio improves from 1.5:1 to 2.4:1 — treat that as upside, never as
the plan.

### 5.2 Why the Stay Bonus is funded by the client, not us

The client is the party who loses from attrition, and their cost of re-hiring (~$11,900 plus
disruption) is 4.8x the escrow. Funding it ourselves would take $2,500 out of a $7,586 gross
profit — a third of it. Framing it as *"you're pre-paying a fraction of what turnover would
cost you"* is both true and easy to sell.

### 5.3 Guarantee conditions

Free replacement within 6 months, **provided**:

1. The client completed documented onboarding (checklist signed in week 1)
2. The worker was paid on time, every cycle
3. Role scope did not materially change from the intake spec
4. The issue was raised within 14 days of arising
5. The 30/60/90 check-ins were held

Without these, a handoff guarantee is unpriced insurance on someone else's management quality.

---

## 6. The three-way win, in numbers

At the lead tier — accountant placed at $34,000.

| Party | Gets | Gives | Net |
|---|---|---|---|
| **Client** | Saves **~$76,000 in year one** ($110–135k loaded [V/E] vs $34k salary + $10.2k fee + $2.5k escrow) and **~$90,000/year thereafter**. A named person, not a firm. 4-hour overlap. Someone financially incentivised to stay | $10,200 fee + $2,500 escrow + $34,000 salary | **Wins in month one** |
| **Worker** | **2.4–4.7x income** (₹6–12 LPA ≈ $7,200–14,400 [E] → $34,000). Works from home. Direct US employer, not a KPO seat. 9% annual raise. $2,500 in tenure bonuses. Named ladder. No night shift | Full-time commitment | **Life-changing** |
| **Us** | $11,900 total fee · **$7,586 GP in 30 days** at a pessimistic 50% replacement reserve · **4.01:1 / 7.51:1** | Sourcing, grading, guarantee exposure, escrow admin | **Clears the constraint with headroom** |

**Why this is genuinely win-win-win rather than extraction:** the salary is fully transparent, so
the worker cannot later discover the agency was keeping 60% of the billing — the single largest
grievance in the seat-rental model. The client's saving and the worker's raise both come from the
*same* arbitrage rather than from each other. We take a one-time slice and are paid again only if
the placement lasts.

**The one place this could stop being win-win-win** is §4.5: if lifetime economics ever come to
depend on paid replacements, we would be profiting from the churn we promise to prevent. That is
why the Stay Bonus is mechanism #1 and why the month-12 tail survives despite being cash-negative.

## 7. What must be true, and what it costs to find out

| # | Assumption | Modelled | Test | Cost |
|---|---|---|---|---|
| 1 | **Meta CPL** — the dominant risk (§4.3) | $100 [E] | Run the ad | ~$1,500 |
| 2 | **Guarantee replacement rate** | **50%** [?] | 10 placements aged 6 months | Time only — **the number that decides the model** |
| 3 | Fill rate | 60% [?] | 3 real intakes | — |
| 3b | **Lead → intake call held** — v1 of the model got this badly wrong | 20% [?] | First 50 leads | Included in test 1 |
| 4 | Indian supply with Shopify/A2X knowledge | [?] | Post one role | ~$300 |
| 5 | Client accepts the $2,500 escrow | [?] | First 5 pitches | Free |
| 6 | Client accepts the 5% month-12 tail | [?] | First 5 pitches | Free |
| 7 | 2-week conversion course closes the A2X gap | [?] | One cohort of 5 | ~$300 |

**Tests 1 and 4 cost under $2,000 and resolve both sides of the marketplace. Tests 5 and 6 cost
nothing and can be run in conversation this week.** Test 2 cannot be accelerated, which is why
§4 models it pessimistically rather than waiting for it.

---

## 8. Known weaknesses of this offer

| Weakness | Severity |
|---|---|
| **CPL is the dominant risk — ~6x more dangerous than attrition** (§4.3) | **High.** Breakeven near CPL $255. Watch it weekly; it is the one number that can kill the model outright |
| The $2,500 escrow is a novel ask from an unknown vendor | Medium. It is also the strongest differentiator and the only retention mechanism with real force, so test the objection before removing it |
| Two-part fee complicates the pitch **and costs ~$1,020/placement** (§4.3) | Medium. A deliberate trust purchase for the first ~20 deals, then switch to 35% single-stage |
| **The niche caps at \$3–5M revenue** (§2.3) | **High for a \$10M ambition.** Right wedge, wrong ceiling — needs a second role or vertical bolted on once proven |
| E-commerce is itself cyclical | Medium. Broader SMB is the fallback ICP with the same delivery |
| Bookkeeping is the most crowded category | Medium. Mitigated by buyer choice (§1.2) and by leading with the accountant tier, not by role choice |
| We hold client money in escrow | Medium. Needs clean segregation and a written escrow term. Not a trust account — get this drafted properly |
| AI is compressing bookkeeping | Medium. `AI` scored 2. This is a 5–7 year business in its current form, not a 15-year one |
