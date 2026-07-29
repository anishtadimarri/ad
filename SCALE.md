# SCALE — $20M on Two Products

Companion to [`OFFER.md`](OFFER.md) (the wedge) and [`MASTER.md`](MASTER.md) (the analysis).
Evidence tags per MASTER §0: **[V]** verified · **[E]** estimate · **[C]** company claim ·
**[?]** assumption.

**Decision: two products. Placement fee + EOR. Nothing else.**
Target **$20M revenue at 32–36% EBITDA**, reached with **82 placements/month — 33% of Somewhere's
current volume** [V].

---

## 1. What was rejected, and why

An earlier version of this document laid out a $100M path built on a **managed service** — selling
the outcome (we do your close) rather than the seat, running one accountant across three clients
at 65% margin.

**Rejected on operational intensity.** That model means owning:

| | |
|---|---|
| Delivery quality | for 1,500 clients' financial statements |
| Utilisation | hire ahead of demand and you carry idle accountants |
| SLAs on work product | month-end close deadlines you are contractually on the hook for |
| 500+ accountants | managed, reviewed, promoted, replaced |
| A mid-build pivot | from "hire your own person" to "buy an outcome" — two pitches in tension |

The analysis was right that it produces higher margin. It was wrong to treat that as decisive.
**A 34% EBITDA business you can actually run beats a 36% EBITDA business that requires becoming a
different company.**

The $100M analysis is preserved in git history if it is ever wanted. It is not the plan.

---

## 2. The mechanic that makes $20M work without a managed service

> **Placement is a flow. EOR is a stock.**
>
> Place P per month → the EOR book stabilises at **P × attach × seat-life** employees.
> At 82/month, 75% attach and a 30-month seat life, that is **~1,850 employees on payroll.**
>
> Once the book exists it bills whether or not you place anyone new.

This is what breaks the transaction-count ceiling **without owning delivery.** A placement-only
business at $6,000 a placement needs 3,300 placements a year to reach $20M. Placement + EOR needs
**989** — because each placement seeds an annuity.

**Note what "seat life" means:** it is how long the *client* keeps the role filled, not how long
the *worker* stays. A free replacement keeps the seat filled and the EOR fee running. Client seat
life is far more durable than 9-month worker tenure, which is why this is the strongest number in
the model.

---

## 3. Sizing

| | |
|---|---|
| Placed salary | **$30,000** — senior e-comm accountant, mid of the useful band |
| Placement fee | 30% = **$9,000** |
| EOR price | **$499/mo** — undercuts Deel and Remote at $599 [V], above India-focused wholesale at $99–200 [V] |
| EOR attach | **75%** [?] |
| Client seat life | **30 months** [?] |
| **EOR lifetime per placement** | **$11,228** |
| **Annual revenue per placement-per-month of capacity** | **$242,730** |
| **Placements required for $20M** | **82/month · 989/year** |
| EOR book at steady state | **~1,850 employees** |

| Line | Revenue | Share |
|---|---|---|
| Placement | $8.9M | 44% |
| **EOR** | **$11.1M** | **56%** |

**The majority of revenue is recurring, and it arrives without a managed service.**

---

## 4. P&L

| | |
|---|---|
| Revenue | **$20,000,000** |
| Placement gross profit @ 54% | $4,805,000 |
| EOR gross profit @ 72% | $7,993,000 |
| **Gross profit** | **$12,798,000 — 64%** |
| EBITDA at 28% SG&A | **$7,198,000 — 36%** |
| EBITDA at 32% SG&A | **$6,398,000 — 32%** |
| **Enterprise value at 8–10x** | **$54–68M** |

The 8–10x is defensible because 56% of revenue is recurring EOR with enormous switching cost —
not the 4–8x a pure placement business earns (MASTER §14).

---

## 5. Headcount — the whole point

| Function | People |
|---|---|
| Recruiters (4 searches/mo, 143 searches/mo needed) | 36 |
| Sourcers | 12 |
| Payroll & compliance (1 per 150 employees) | 12 |
| Client success (1 per 200 clients) | 10 |
| Sales & intake | 8 |
| Leadership, finance, legal, ops | 10 |
| **Total** | **~88** |

**Revenue per head: $228,000.** The managed-service path needed 500+ accountants *on top of all
of this*.

**Two operational systems, and only two:**

| System | Character |
|---|---|
| **Recruiting** | Real ops. Throughput, fill rate, bench, quality grading. This is the hard one |
| **Payroll & compliance** | Batch ops. Runs monthly, scales sublinearly, systematises well, no work-product risk |

There is no third system. No utilisation planning, no delivery SLAs, no work-product quality
function, no capacity forecasting.

---

## 6. Why this is higher likelihood

| Reason | |
|---|---|
| **Both products are proven by others** | Somewhere does placement at 250/month [V]; Deel, Remote and Oyster do EOR at $599–699 [V]. Nothing here is novel |
| **No delivery-quality risk** | You never owe an outcome. If the accountant underperforms, the client manages them or you replace them |
| **No utilisation risk** | The managed service's worst failure mode — carrying idle accountants — does not exist here |
| **No pivot** | The pitch is identical at $1M and $20M: *"hire your own person; we'll employ them for you."* No repositioning, no two-pitch tension |
| **Only 33% of Somewhere's volume** | Not a category-dominating share |
| **EOR is exceptionally sticky** | Payroll switching cost is among the highest in B2B. Churn is structurally low once the book exists |

---

## 7. The single dependency — make EOR the default, not the upsell

Everything rests on EOR attach. The highest-leverage decision in the whole plan is to stop
treating it as an upsell:

> **"We find them, and we employ them. One invoice, one vendor. You never touch Indian
> employment law."**

At the moment of hire the client *must* solve "how do I actually pay someone in India?" You are
standing there with the answer, and their alternatives are Deel at $599 or a contractor agreement
with misclassification risk. This is the best upsell moment in the business — so don't make it
an upsell.

**Sensitivity — placements/month needed for $20M:**

| EOR attach | Placements/mo |
|---|---|
| 40% | 111 |
| 60% | 93 |
| **75%** | **82** |
| 90% | 74 |

| Client seat life | Placements/mo |
|---|---|
| 18 months | 106 |
| **30 months** | **82** |
| 48 months | 62 |

**The model is robust to attach and sensitive to seat life.** Even at 40% attach it works, just
with 35% more recruiting. Seat life is the number to protect — and it is protected by honouring
replacements, which you were doing anyway.

---

## 8. Build path

| Stage | Years | Revenue | EOR book | Recurring | Proof point |
|---|---|---|---|---|---|
| 1 | 0–1 | $0.5–1.5M | 100–250 | 15–25% | Fill rate >60%, CAC <$900, **EOR attach >60%** |
| 2 | 1–2.5 | $1.5–5M | 250–700 | 35–45% | EOR churn <1.5%/mo, own-entity decision made |
| 3 | 2.5–4.5 | $5–12M | 700–1,300 | 50% | Recruiting throughput at 50+/mo |
| 4 | 4.5–7 | $12–20M | 1,300–1,850 | 56% | 88-person org running without founder in delivery |

Self-funded throughout. The only capital event is the own-entity EOR decision in stage 2 — and
white-label (50–75% margin, zero employment liability) is the correct answer until the line is
proven (OFFER §4).

---

## 9. What would kill it

| Risk | Severity | Mitigation |
|---|---|---|
| **EOR attach below 40%** | **High** | Make it the default. Price against Deel's $599, not against wholesale |
| Fill rate below 40% | **High** | Deposit gates the search, bench, narrow role |
| CPL above $414 | High | Partnerships and stack-scraped cold email are cheaper than Meta for this ICP (OFFER §2.6) |
| Client seat life under 18 months | Medium | Honour replacements. Seat life ≠ worker tenure |
| India wage inflation at 9.5%/yr [V] | Medium | The EOR fee is flat per employee, so it is **unaffected by wage inflation** — a second reason to weight EOR |
| Own-entity employment liability | Medium | White-label until volume justifies counsel |
| A funded competitor bundles placement + EOR | Medium | Nobody currently does. Assume ~3 years of clear air |
| AI compresses bookkeeping demand | Medium | Real, but slower than a 7-year build. Placement is role-agnostic — the same machine places other roles |

**One structural advantage worth naming:** the EOR fee is **flat per employee**, so it is immune
to the wage-inflation compression that erodes the placement pitch (MASTER §4.5). As the arbitrage
narrows over ten years, the EOR half of the business does not care.

---

## 10. The media angle — one asset, not a content strategy

Asked whether media adds meaningfully to deal flow *and* enterprise value, without forcing it.
**It does, for one specific reason — but the obvious version of it destroys value.**

### 10.1 The empirical case is unusually strong

| | |
|---|---|
| Somewhere | Grew on Nick Huber's ~400k audience [V] |
| Oceans | Grew on Austin Rief / Nik Sharma audiences [V] |
| Referral economics | **$25/lead vs $497 industry average** [V] |
| Sub-$5M agencies | **60–80% of revenue from referral** [V] |

**Every scaled player in this category was built on a media asset, and neither founder was a media
buyer — they were audience owners.** Media isn't a bolt-on here; it is the category's proven
go-to-market. What nobody has done is enter with media as a *deliberate build* rather than a
pre-existing accident.

### 10.2 The asset: a proprietary compensation and hiring benchmark

Not a podcast. Not thought leadership. Not a founder newsletter. **One report, published
quarterly, built as a byproduct of placements you are making anyway.**

> **The E-Commerce Operator Comp Report** — what brands at $1M / $5M / $10M / $25M actually pay
> for every operating role, US versus offshore, with time-to-fill and attrition by role.

Why this specific asset and not another:

| Test | Why it passes |
|---|---|
| **The ICP already wants it** | Every founder at $3–30M wonders whether they are paying market. Comp is the most-searched, least-answered question in e-comm ops |
| **You are uniquely positioned** | You will hold thousands of real salary points at the e-comm × offshore intersection. Nobody else has that data |
| **It compounds** | Every placement improves the report; a better report drives more placements. A genuine flywheel, not a funnel |
| **It IS the sales tool** | *"Here's what this role costs in the US versus India"* is literally the pitch. The lead magnet and the offer are the same object |
| **Near-zero marginal cost** | A byproduct of operations, not a separate function |
| **It is an enterprise-value asset** | A proprietary dataset plus a distribution list carries its own multiple |

Secondary, in support: a **gated true-cost-of-hire calculator** (continuous inbound, compounds on
search) and a **narrow benchmarks newsletter** for e-comm finance and ops — not a hiring
newsletter, which would attract recruiters rather than buyers.

### 10.3 The deal-flow effect

| Media share of deal flow | Blended CAC | 30-day | Lifetime |
|---|---|---|---|
| 0% | $587 | 10.14:1 | 35.51:1 |
| 15% | $511 | 11.64:1 | 40.80:1 |
| **30%** | **$435** | **13.68:1** | **47.93:1** |
| 45% | $359 | 16.58:1 | 58.09:1 |

*(At ~$80 marginal cost per media-sourced deal. Base case is $30k placed salary, 75% EOR attach,
30-month seat.)*

### 10.4 The enterprise-value effect

| | EBITDA | Multiple | Enterprise value |
|---|---|---|---|
| No media — single-channel dependency | $6.80M | 8.0x | **$54M** |
| Media at 30% of deal flow | $6.95M | 9.0x | **$63M** |
| Media + proprietary comp dataset | $7.03M | 9.5x | **$67M** |

**The value is in the multiple, not the EBITDA.** Two diligence items move it: channel
concentration risk removed, and a dataset a competitor cannot replicate without doing the
placements. Roughly **$13M of enterprise value for a report produced as a byproduct.**

### 10.5 The trap — and it is the opposite of what the incumbents did

> **A founder-brand audience is not transferable, and in diligence it is a discount, not a
> premium.** A buyer asks "what happens when you leave?" Nick Huber's audience is worth a great
> deal to Somewhere and it belongs to Nick.

So the asset must be **brand-owned, not founder-owned.** *The E-Commerce Comp Report by
[Company]*, with a named research author who is an employee — not *[Founder]'s newsletter*. That
is a deliberate design choice with a direct valuation consequence, and it is the reverse of how
both Somewhere and Oceans built theirs.

### 10.6 The discipline

Media is the most common founder distraction in this category, so bound it:

| Rule | |
|---|---|
| **It must be a byproduct** | If you are hiring a content team in year 1, the thread is lost |
| **One asset, not a strategy** | The report. The calculator and newsletter only exist to distribute it |
| **Brand-owned bylines** | No founder-personality dependency |
| **Data before publication** | Needs ~100 placements before the numbers are credible. **This is a year-2 asset.** Year 1 seeds it with market research and the first cohort |
| **No media hire until stage 3** | One analyst, and only once the dataset justifies one |

**Verdict: worth building, second.** It does not change stage 1 — nothing beats getting ten
placements done. But the data model should be designed from placement one, because retrofitting
comp data you failed to capture is the one part of this that cannot be bought later.

---

## 11. Summary

| | Placement only | **Placement + EOR** | Managed service |
|---|---|---|---|
| Revenue ceiling | $3–5M in this niche | **$20M** | $100M |
| Gross margin | 54% | **64%** | 67% |
| EBITDA | 25–30% | **32–36%** | 32–37% |
| Recurring | <10% | **56%** | 88% |
| Headcount at target | ~40 | **~88** | 600+ |
| Operational systems | 1 | **2** | 4 |
| Owns delivery quality | No | **No** | Yes |
| Requires a pivot | No | **No** | Yes |
| Exit multiple | 4–8x | **8–10x** | 8–12x |
| **Likelihood** | High | **High** | Low-medium |

**Two products, 88 people, $20M, ~$6.4–7.2M EBITDA, $54–68M enterprise value, and no month where
you owe anyone a financial statement.**

Nothing in [`OFFER.md`](OFFER.md) changes. What changes is that **EOR stops being an upsell and
becomes half the business** — decided now, so stage 1 is built to attach it from the first
placement.
