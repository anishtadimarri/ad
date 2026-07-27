# Financial Model

Every number below is an **estimate, not evidence.** The four assumptions that actually decide the
outcome are flagged in [Sensitivities](#sensitivities). Nothing here has met a customer.

---

## Funnel math — base case at $5,000/month spend

| Stage | Rate | Result |
|---|---|---|
| Ad spend | | $5,000 |
| Cost per calculator completion | $45 | **111 leads** |
| Lead → $297 SLO purchase | 8% | **8.9 SLO buyers** |
| SLO revenue | 8.9 × $297 | **+$2,643** |
| SLO delivery cost (3 ghost calls + scoring) | 8.9 × $40 | **−$356** |
| **Net acquisition cost** | | **$2,713** |
| SLO buyer → booked review call | 85% | 7.6 calls |
| Review call → closed client | 25% | **1.9 clients** |
| **CAC** | $2,713 ÷ 1.9 | **$1,428** |

### The SLO is doing the heavy lifting

| | No SLO | **With SLO** |
|---|---|---|
| Net acquisition cost | $5,000 | **$2,713** |
| CAC | $2,632 | **$1,428** |
| 30-day LTGP:CAC | 3.9:1 | **7.1:1** |

Same offer, same traffic. The SLO nearly doubles the ratio by recovering ~55% of ad spend and
raising call show-rate from ~40% (free lead) to ~85% (paid buyer).

---

## 30-day collected per client

| | Standard (85%) | Annual prepay (15%) |
|---|---|---|
| Install ($4,750 signature + $4,750 day 21) | $9,500 | $9,500 |
| Month 1 management | $2,500 | — |
| 12-month prepay (12-for-10) | — | $25,000 |
| Partial performance fees | ~$750 | ~$750 |
| **30-day collected** | **$12,750** | **$34,500** |
| **Blended** | | **$16,013** |

## The headline ratio

| | Standard client | Blended |
|---|---|---|
| 30-day collected | $12,750 | $16,013 |
| Gross margin | 80% | 80% |
| **30-day gross profit** | **$10,200** | **$12,810** |
| CAC | $1,428 | $1,428 |
| **30-day LTGP:CAC** | **7.1:1** ✅ | **9.0:1** |

### On the 80% margin assumption

Realized margin should be **85–92%**:

| | Month 1 | Ongoing |
|---|---|---|
| Install labor (~55 hrs, India build team) | $650 | — |
| Account management (India, 8 clients per AM) | $190 | $190 |
| Tooling (n8n, GHL, reporting, hosting) | $150 | $150 |
| **Total** | **$990** | **$340** |
| On collected | $12,750 | $3,700 |
| **Margin** | **92%** | **91%** |

**80% is used throughout as the planning number.** The 11-point gap is deliberate buffer for scope
creep, failed installs, guarantee remediation, and refunds. Do not model on 92%.

---

## 12-month model

Ad spend scales with collected cash. Client growth is paced to delivery hiring, not to demand —
demand is not the constraint. Churn modeled at 4%/month (~25-month tenure), **unvalidated.**

| Mo | Ad spend | New | Active | Front-end | Recurring | SLO | **Collected** |
|---|---|---|---|---|---|---|---|
| 1 | $5,000 | 1.0 | 1.0 | $16,013 | $0 | $2,643 | **$18,656** |
| 2 | $5,000 | 1.9 | 2.9 | $30,425 | $3,325 | $2,643 | **$36,393** |
| 3 | $5,000 | 1.9 | 4.7 | $30,425 | $9,510 | $2,643 | **$42,578** |
| 4 | $7,500 | 2.9 | 7.4 | $46,438 | $15,461 | $3,965 | **$65,864** |
| 5 | $10,000 | 3.8 | 10.9 | $60,849 | $24,472 | $5,286 | **$90,607** |
| 6 | $10,000 | 3.8 | 14.2 | $60,849 | $36,143 | $5,286 | **$102,278** |
| 7 | $12,500 | 4.6 | 18.3 | $73,660 | $47,348 | $6,608 | **$127,616** |
| 8 | $12,500 | 4.6 | 22.1 | $73,660 | $60,748 | $6,608 | **$141,016** |
| 9 | $15,000 | 5.3 | 26.6 | $84,869 | $73,616 | $7,929 | **$166,414** |
| 10 | $15,000 | 5.3 | 30.8 | $84,869 | $88,279 | $7,929 | **$181,077** |
| 11 | $15,000 | 5.3 | 34.9 | $84,869 | $102,377 | $7,929 | **$195,175** |
| 12 | $15,000 | 5.3 | **38.8** | $84,869 | $115,910 | $7,929 | **$208,708** |
| | **$127,500** | **45.7** | | | | | **$1,376,382** |

Recurring per active client blends $2,500 management + ~$1,200 average performance fees, adjusted
for prepay clients who pay performance only.

### Milestones

| | |
|---|---|
| Cross **$20,000/month** | **Month 1** |
| Cross $100,000/month | Month 6 |
| **Year 1 collected** | **~$1.38M** |
| Month 12 run-rate | **~$2.5M annualized** |
| Active clients at exit | ~39 |
| Market penetration | **~4% of the 1,000 addressable** |

I quoted "$1.5–1.8M" in conversation. The detailed model comes in at **$1.38M** — the difference
is the month-1 partial cycle and paced hiring. Use $1.38M.

---

## P&L

| | Year 1 |
|---|---|
| Collected | $1,376,382 |
| Ad spend | ($127,500) |
| SLO delivery (ghost calls) | ($5,500) |
| Automation build team (2 × $1,800/mo from M2) | ($39,600) |
| Account management (ramp to 5 AMs @ $1,500/mo) | ($45,000) |
| Sales (closer from M6 + 5% commission) | ($62,500) |
| Tooling | ($9,600) |
| Legal, BAA, attorney review | ($15,000) |
| Accounting, admin, misc | ($25,000) |
| **Modeled pre-tax** | **~$1,047,000** |
| **After 25% reality haircut** | **~$785,000** |

The haircut covers failed installs, guarantee remediation work, refunds, worse-than-modeled churn,
and dead ad tests. Assume it will be needed.

---

## Working capital

| Month | Peak cash need |
|---|---|
| 1 | $5,000 ads + $15,000 legal/tooling setup |
| 2–3 | Ad spend + first build hires before collections land |
| **Peak requirement** | **~$30,000, around month 2–3** |

From month 4 the business self-funds and the only question is how hard to push. But you need that
$30,000 available or growth stalls precisely when it starts working.

---

## Sensitivities

Four assumptions carry the model. Everything else is noise.

### 1. Review call → close rate (modeled 25%)

| Close rate | CAC | Ratio | Verdict |
|---|---|---|---|
| 35% | $1,020 | 10.0:1 | |
| **25%** | **$1,428** | **7.1:1** | Base |
| 15% | $2,380 | 4.3:1 | Still fine |
| 10% | $3,570 | 2.9:1 | Thin |
| **7%** | **$5,100** | **2.0:1** | **Floor** |

**You can be wrong by 3.5x and still hit 2:1.** This is the model's real strength. You'll know
after ~15 calls, which is week 4.

### 2. Lead → SLO conversion (modeled 8%)

| Conversion | Net acq. cost | CAC | Ratio |
|---|---|---|---|
| 12% | $1,935 | $1,018 | 10.0:1 |
| **8%** | **$2,713** | **$1,428** | **7.1:1** |
| 5% | $3,315 | $1,745 | 5.8:1 |
| 2% | $4,113 | $2,165 | 4.7:1 |
| 0% (SLO fails entirely) | $5,000 | $2,632 | 3.9:1 |

**Even total SLO failure leaves you at 3.9:1.** The SLO is upside, not load-bearing.

### 3. Churn (modeled 4%/month)

| Churn | Exit active | Exit run-rate |
|---|---|---|
| 3% | 41 | ~$2.7M |
| **4%** | **39** | **~$2.5M** |
| 7% | 32 | ~$2.1M |
| 10% | 27 | ~$1.8M |

Does not affect the 30-day ratio at all. Affects everything about what you own in year three.

### 4. Cost per booked review call (modeled $357)

This is the single number the $400 test measures.

| Cost/booked call | CAC @ 25% close | Ratio |
|---|---|---|
| $200 | $800 | 12.8:1 |
| **$357** | **$1,428** | **7.1:1** |
| $600 | $2,400 | 4.3:1 |
| $1,000 | $4,000 | 2.6:1 |
| **$1,275** | **$5,100** | **2.0:1 — stop** |

---

## Everything-40%-worse stress case

Close rate 15%, SLO conversion 5%, churn 7%, CPL $63, ad spend held at $10,000/month.

| | |
|---|---|
| CAC | ~$2,900 |
| **30-day LTGP:CAC** | **3.5:1** ✅ |
| New clients, year 1 | ~19 |
| Year 1 collected | **~$560,000** |
| Exit run-rate | ~$1.0M |
| Pre-tax | ~$220,000 |

**The model survives being wrong about everything simultaneously.** That is the actual case for
this business — not the $1.38M base.

---

## What to measure, in order

| Week | Number | Threshold |
|---|---|---|
| 1 | Cost per calculator completion | <$90 |
| 2 | Lead → SLO conversion | >3% |
| 3 | **Cost per booked review call** | **<$600** |
| 4–6 | **Review call → close rate** | **>7%** |
| 8 | SLO buyer → call show rate | >60% |
| 12–16 | Guarantee deliverability (consults sat +5) | 85% of clients |
| 24+ | Monthly churn | <7% |

The first three cost $600 and two weeks. Everything after that requires real clients — so don't
model past week 3 until week 3 is done.
