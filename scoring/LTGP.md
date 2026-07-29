# LTGP:CAC on a $20,000 Job

Gross profit from [`offer_model.py`](offer_model.py). CAC from [`funnel.py`](funnel.py) — **not** from the offer model, whose internal CAC uses a flat
$75 CPL and an assumed funnel. Where the two disagree, the funnel one is built from benchmarked steps and wins.

Placed salary **$20,000** · fee **30%** = **$6,000** · EOR **$499/mo** at **75% attach** · **9 months of EOR per employee**.

---

## 0. The EOR line, per month

| | Per employee / month |
|---|---|
| EOR price charged to the client | $499 |
| Marginal cost — payroll, filings, HR support, insurance admin | ($55) |
| **Fee gross profit** | **$444** |
| FX spread at 2% on $1,667/mo of salary moved | $33 |
| **Total gross profit per employee per month** | **$477** |
| × 75% attach × 1.2 seats | **$430/mo per acquired client** |

**$477/month per employee, 89% margin on the fee line.** Over 9 months that is
**$4,296 per employee**, or **$3,866 per acquired client** once attach and second seats are counted.

The cost side is the reason the margin holds: an India-domiciled operator's marginal cost of employing one more person is ~$55/mo, against the $499 the client would pay Deel or Remote for the *same* India employment. **You are not discounting; you are pricing at the global comparison with a local cost base.**

---

## 1. The gross profit per acquired client

| | | |
|---|---|---|
| Placement fee | $6,000 | 30% of $20,000 |
| Seats per acquired client | 1.20 | 20% of clients hire two at once |
| Screening billed on | $336 | cost × 1.6, market-standard pass-through |
| **30-day revenue** | **$7,536** |  |
| **30-day gross profit** | **$4,148** | **55% margin** |
| Repeat seats over the life | 0.80 | 35% expand + 45% paid replacement |
| **Lifetime gross profit** | **$11,074** | of which **$4,046 (37%) is recurring** |

**At 9 months the placement fee is back to being the business.** $4,046 of the $11,074
lifetime gross profit is recurring — 37%, down from 65% when the EOR line was assumed to run for a 30-month client seat. **The fee is 63% of the value again**, which changes what the company is: a placement business with a useful attachment, not an EOR business with a placement front end.

---

## 2. The CAC, by audience layer

| Audience | CPL | Cost per held call | **CAC** | **30-day** | **Lifetime** |
|---|---|---|---|---|---|
| Intent seed (job posters) | $65 | $160 | **$652** | **6.36:1** | **16.99:1** |
| 1% Lookalike | $86 | $192 | **$1,089** | **3.81:1** | **10.17:1** |
| Broad / Advantage+ | $103 | $218 | **$1,427** | **2.91:1** | **7.76:1** |
| **Blended** (25% Intent seed / 45% 1% Lookalike / 30% Broad) | | | **$976** | **4.25:1** | **11.35:1** |

Blended by **spend**, not by averaging the three CACs — the intent seed has the lowest
CAC but the smallest audience, so it cannot absorb the budget its CAC would earn it.

> **$4,148 of 30-day gross profit against a $976 CAC = 4.25:1 inside month one.**
> Over the life of the client, **11.35:1**.

---

## 3. What moves it

| Change | CAC | 30-day GP | **30-day** | **Lifetime** |
|---|---|---|---|---|
| **Base** | $976 | $4,148 | **4.25:1** | **11.35:1** |
| Deposit rate 8% not 18% | $2,195 | $4,148 | **1.89:1** | **5.04:1** |
| EOR attach 40% not 75% | $976 | $4,148 | **4.25:1** | **9.50:1** |
| Both bad — 8% deposit, 40% attach | $2,195 | $4,148 | **1.89:1** | **4.22:1** |
| Deposit 30%, EOR attach 90% | $585 | $4,148 | **7.09:1** | **20.24:1** |

**The deposit rate is the one input that can break it.** It is the step with no data
behind it — 18% of held calls paying a $500 refundable deposit on cold traffic is an
assumption, not a benchmark. Halve it and the 30-day ratio halves with it. EOR attach and
EOR months move the lifetime number a lot and the 30-day number **not at all**, because
the 30-day number is the placement fee and nothing else.

Both of the things that could go wrong at once still clears the 1.5:1 constraint, which is the actual test.

---

## 4. How many months of EOR — and why this is the biggest lever left

The base case above assumes **9 months**, which is the average *worker* tenure. That is the
**floor**, not the expected value, because it assumes the seat dies with the worker.
It should not: a replacement under the 12-month guarantee refills the same seat, and the
EOR fee keeps billing across the handover. **Placement is a flow; the EOR book is a stock** ([`SCALE.md`](SCALE.md) §2).

| EOR months | Lifetime GP | Recurring share | **30-day** | **Lifetime** |
|---|---|---|---|---|
| **6** | $9,785 | 28% | **4.25:1** | **10.03:1** |
| **9** ← **base** | $11,074 | 37% | **4.25:1** | **11.35:1** |
| **12** | $12,362 | 43% | **4.25:1** | **12.67:1** |
| **18** | $14,940 | 53% | **4.25:1** | **15.31:1** |
| **24** | $17,518 | 60% | **4.25:1** | **17.95:1** |
| **30** | $20,095 | 65% | **4.25:1** | **20.60:1** |

**Each extra month of EOR is worth $430 of gross profit per acquired client** — about
44% of a whole CAC, every month, at zero incremental acquisition cost. Going from 9 months
to 30 adds **$9,022** and takes lifetime from 11.35:1 to 20.60:1.

### Seat continuity vs halving CAC

These are the two big levers left, and on the *ratio* they look about the same size:

| Lever | Lifetime ratio | Absolute GP per client | What it costs |
|---|---|---|---|
| Base — 9 months, $976 CAC | 11.35:1 | $11,074 | — |
| **Halve CAC** to $488 | **22.70:1** | $11,074 — *unchanged* | A channel breakthrough. Not available on demand |
| **Seat to 30 months** | 20.60:1 | **$20,095** — **+$9,022** | A contract clause and bench discipline |

**The ratio is the wrong scoreboard for this comparison.** Halving CAC wins on the ratio and adds
**$488** of profit per client. Extending the seat loses on the ratio and adds **$9,022** — about
18x more actual money. A ratio can be improved by shrinking the denominator, which is why it should
never be optimised alone.

**So build seat continuity, and it is the same mechanism as the guarantee** — the thing
that makes a replacement painless is the thing that keeps the EOR fee billing.

The three things that keep a seat alive across a worker exit, in order of cost:

| Mechanism | Cost |
|---|---|
| EOR contract is with the **seat**, not the person — replacement is a novation, not a new contract | Free. A drafting decision, made once |
| A bench candidate already graded for that client's stack, so the gap is days not weeks | Standing capital in the bench |
| Provident fund and gratuity, which the state enforces — gratuity vests at 5 years, so the worker's own incentive lengthens tenure | Already inside the $55 cost |

The first one is free and is the one that matters. **If the EOR contract names the person, every worker exit is a resale. If it names the seat, it is an operational event.**

