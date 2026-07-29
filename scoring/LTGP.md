# LTGP:CAC on a $20,000 Job

Gross profit from [`offer_model.py`](offer_model.py). CAC from [`funnel.py`](funnel.py) — **not** from the offer model, whose internal CAC uses a flat
$75 CPL and an assumed funnel. Where the two disagree, the funnel one is built from benchmarked steps and wins.

**Placed salary $20,000 · fee 30% = $6,000 · EOR $499/mo at 75% attach · 30-month client seat.**

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
| **Lifetime gross profit** | **$20,095** | of which **$13,068 (65%) is recurring** |

**The placement fee is no longer the business.** $13,068 of the $20,095 lifetime gross
profit is the recurring EOR layer — $499/mo at 89% margin, plus the 2% FX spread and
equipment margin, running for as long as the client keeps the seat filled. The fee is the entry price; the seat is the asset.

---

## 2. The CAC, by audience layer

| Audience | CPL | Cost per held call | **CAC** | **30-day** | **Lifetime** |
|---|---|---|---|---|---|
| Intent seed (job posters) | $65 | $160 | **$652** | **6.36:1** | **30.83:1** |
| 1% Lookalike | $86 | $192 | **$1,089** | **3.81:1** | **18.45:1** |
| Broad / Advantage+ | $103 | $218 | **$1,427** | **2.91:1** | **14.08:1** |
| **Blended** (25% Intent seed / 45% 1% Lookalike / 30% Broad) | | | **$976** | **4.25:1** | **20.60:1** |

Blended by **spend**, not by averaging the three CACs — the intent seed has the lowest
CAC but the smallest audience, so it cannot absorb the budget its CAC would earn it.

> **$4,148 of 30-day gross profit against a $976 CAC = 4.25:1 inside month one.**
> Over the life of the client, **20.60:1**.

---

## 3. What moves it

| Change | CAC | 30-day GP | **30-day** | **Lifetime** |
|---|---|---|---|---|
| **Base** | $976 | $4,148 | **4.25:1** | **20.60:1** |
| Deposit rate 8% not 18% | $2,195 | $4,148 | **1.89:1** | **9.15:1** |
| EOR attach 40% not 75% | $976 | $4,148 | **4.25:1** | **14.43:1** |
| Client seat 12 months not 30 | $976 | $4,148 | **4.25:1** | **12.67:1** |
| Both bad — 8% deposit, 40% attach | $2,195 | $4,148 | **1.89:1** | **6.41:1** |
| Deposit 30%, EOR attach 90% | $585 | $4,148 | **7.09:1** | **38.73:1** |

**The deposit rate is the one fragile input.** It is the step with no data behind it —
18% of held calls paying a $500 refundable deposit on cold traffic is an assumption, not
a benchmark. Halve it and the 30-day ratio halves with it. Everything else — EOR attach,
seat length, fill rate — moves the lifetime number a lot and the 30-day number barely,
because the 30-day number is almost entirely the placement fee.

Both of the two things that could go wrong at once still clears the 1.5:1 constraint, which is the actual test.

