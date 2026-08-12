# MODEL V2 — Ingested, and compared against the repo

Operator's working version, received in full. **This document does three things: records what
changed, marks where V2 is better than what the repo had, and corrects two errors of mine that V2
exposes.** One item in V2 must be resolved before anything else can be sized — §2.

---

## 1. What V2 changes

| | Repo model (V1) | **V2** |
|---|---|---|
| **Wedge** | Bookkeeper → the finance spine ([`COMPOUND.md`](COMPOUND.md)) | **Premium performance video editors** |
| **Category** | Offshore talent placement | **Premium global direct-hire marketplace for internet companies** |
| **ICP** | 2 verticals — e-comm + agencies, the only two clearing FB **and** IG | **5, defined by properties:** internet businesses with revenue, Meta-reachable owner, recurring creative need |
| **Positioning** | **Price** — *"your bookkeeper costs $75k, ours is $20k"* | **Premium** — *"an excellent person who fits into your team,"* explicitly not cheap labour |
| **Salary band** | $20,000/yr | **$1,500–1,800/mo = $18,000–21,600/yr** |
| **Fee** | 30% of first-year salary, one-time | **"30–35% markup / fee economics"** — ambiguous, see §2 |
| **EOR** | Core to the model, 37–65% of lifetime GP | **Optional monetisation and retention layer** |
| **Media** | A byproduct idea ([`SCALE.md`](SCALE.md) §10) | **A first-class second engine** — X + weekly *Internet Business Brief* |
| **Moat** | Fill rate + guarantee + the India gap | **Demand intelligence + talent intelligence + distribution** |
| **Expansion** | Vertically up the finance ladder | **Horizontally across creative** — editor → designer → motion → UGC → performance creative |
| **Near-term goal** | Ten calls, measure the deposit rate | **Ten paid placements**, then let data pick the ICP × role |

---

## 2. Resolve this first: §7 conflates two pricing models, and one of them breaks

V2 §7 says *"30–35% markup / fee economics against the underlying talent compensation"* and then
*"$1,700/month talent cost → client pays a premium → your gross profit is the difference."*

**Those are two different businesses.** Run against the funnel-derived **$976 CAC**:

| Reading | What it means | Month-1 GP | **30-day LTGP:CAC** | Clears 1.5:1? |
|---|---|---|---|---|
| **A — one-time placement fee, 30% of *annual* comp** | $19,800 × 30% = **$5,940** | **$4,110** | **4.21:1** | ✅ |
| **B — 30–35% monthly markup on talent cost** | $1,650 × 32.5% = **$536/mo** | **$499** | **0.51:1** | ❌ **fails** |

**Reading A produces 8.2x the month-one cash of Reading B.** Reading B needs **2.9 months of billing
just to clear the 30-day gate once** — and the 30-day constraint is a *hard* one, not a preference.

This is the same finding as [`HUNGRY.md`](HUNGRY.md) §8: **every ongoing-margin model fails the
30-day constraint** unless the monthly ticket is very large. A 32.5% markup on $1,650 is not large.

> **V2 must state which one it is. If it is B, the model does not clear its own hard constraint and
> everything downstream — CAC tolerance, ad budget, cash cycle — is wrong by roughly 8x.**

Reading A is almost certainly what is meant, and it is the right answer. **Say it explicitly:
a one-time fee of 30–35% of first-year compensation, plus optional recurring EOR.**

---

## 3. Where V2 is better than what the repo had — three places, and they matter

### 3.1 The positioning flip is supported by the repo's own most recent evidence

V1 sold **price**. Two independent screens said that was the weaker choice, and V2 fixes it:

| | |
|---|---|
| [`SKILLS-INDIA.md`](SKILLS-INDIA.md) | A **quality** pitch answers both the price objection and the India objection; a **price** pitch invites both |
| [`LENSES.md`](LENSES.md) §1 | The bookkeeper claim is **0.4–1.1x against a bookkeeping firm** — the vendor most $3–30M brands actually use. **Video is 4.0–13.2x against its vendor**, the largest true claim found anywhere |

**V2's wedge has the strongest arbitrage in the study and V1's had close to none against the real
comparator.** That is not a small correction.

### 3.2 Defining the ICP by properties rather than by industry is a genuine upgrade

V1 named two industries. **V2 names four properties** — internet business, meaningful revenue,
Meta-reachable owner, recurring creative need. That is a *targeting rule*, and a rule generalises
where a list does not. It is also what [`MAP.md`](MAP.md) §5C was groping at when it found only
e-comm and agencies cleared FB+IG: the real filter was never the industry, it was **owner-led and
Meta-native**, which creators, coaches and digital media also satisfy.

### 3.3 The media design is right where [`SCALE.md`](SCALE.md) §10's was not

The four formats — **NUMBER, SIGNAL, EXPERIMENT, BENCHMARK, BET** — are **outputs of the recruiting
work**, not a separate content job. *"We looked at 500 job postings"* is the scrape already being
built. *"What a $10M e-commerce team looks like"* is placement data. **Content that is a byproduct
survives; content that is a second product does not**, and V2 is designed as the first kind.

It also solves something [`SCALE.md`](SCALE.md) flagged and could not answer: **founder-brand
audiences are non-transferable at exit.** An *Internet Business Brief* with proprietary compensation
and hiring data is a transferable asset. A personality is not.

---

## 4. Two corrections to my own analysis that V2 forces

### 4.1 I gated video out of [`COMPOUND.md`](COMPOUND.md) at 52.0. Under V2's framing it scores 75.6 and passes

Two specifics in V2 change scores I set, and both are legitimate:

| Dimension | I scored | V2 justifies | Why |
|---|---|---|---|
| **`SPINE`** | **1** | **4** | I scored Premiere and After Effects — *tools*, not a shared record. **A *performance* editor's work is judged in the ad account**, and [`MAP.md`](MAP.md) already names **Meta Ads Manager / GA4 as a spine**. Shared login, continuous visibility, the next gap visible. Same property as the ledger |
| **`LADDER`** | **2** | **4** | I scored editor → senior editor. **V2's ladder is horizontal**: editor → designer → motion → UGC → performance creative, all served by one bench |
| **`SEATS`** | **2** | **4** | Same reason — a client who buys an editor can buy a designer next |
| **`AIDUR24`** | **2** | **3** | Arguable both ways, and I was one-sided. **Cheaper AI variants mean *more* tests, which means more editing demand, not less.** The volume effect partly offsets the substitution effect |

**Net: 52.0 → 75.6, gates cleared.** It still loses to the finance spine at 95.6, but *"gated out"*
was wrong and I should not have scored a generic editor when the proposal was a performance editor.

### 4.2 The salary problem I raised does not exist at V2's band

I modelled a $15,000 editor and flagged that a percentage fee on a lower salary hurts. **V2's band is
$18,000–21,600** — essentially the bookkeeper band:

| Monthly comp | Annual | Fee @30% | 30-day GP | **30-day** | **Lifetime** |
|---|---|---|---|---|---|
| $1,500 | $18,000 | $5,400 | $3,764 | **3.86:1** | 10.67:1 |
| $1,650 | $19,800 | $5,940 | $4,110 | **4.21:1** | 11.28:1 |
| $1,800 | $21,600 | $6,480 | $4,454 | **4.56:1** | 11.89:1 |

**The economics are within noise of the bookkeeper's 4.25:1.** That objection is withdrawn.

---

## 5. Where V1 still wins, and it is one dimension

| | Finance spine | Performance creative |
|---|---|---|
| **Compounding score** | **95.6** | 75.6 |
| **`AIDUR24`** | **4** — ledger automation is real and slow | **3** — and it carries the **heaviest weight (22)** in that screen |
| **Ad legibility** | **96.0 — the most legible role in the 179-role study** | ~4 of 5. *"Video editor"* is clear but not *that* clear |
| **Serves all ICPs** | **5 of 5** — every internet business has books | 4 of 5 — every internet business has creative, but a coach may not hire an editor |
| **`FOUNDERGRADE`** | 2 — needs a hired CA | **5 — you grade it yourself on hold rate and CTR** |

**So the two models trade one dimension each: V1 wins durability and legibility, V2 wins arbitrage,
positioning and gradeability.** That is a much closer call than [`COMPOUND.md`](COMPOUND.md) made it,
and `FOUNDERGRADE` alone is a strong argument for V2 in month one — you cannot promise quality you
cannot personally verify, and with V2 you can.

---

## 6. Four things in V2 that are unresolved or risky

| | Issue | What to do |
|---|---|---|
| **1** | **Pricing conflation** (§2) | Resolve to Reading A explicitly. Highest priority — everything downstream depends on it |
| **2** | **Five ICPs** | V2 says do not operationalise all five, which is right. But **creators conflict with the fee model**: [`HUNGRY.md`](HUNGRY.md) §7 found they buy **per video or on a freelance retainer**, so there is no salary for a 30% fee to attach to. **Agencies and e-comm hire editors as employees; creators mostly do not.** Launch on the two that do |
| **3** | **The media burden** | The byproduct design is right, but a weekly newsletter plus daily X is a real time cost against a one-month launch. **Start with X only.** The newsletter is a month-three commitment once there is placement data worth publishing |
| **4** | **`AIDUR24` is still the weakest number in the model** | Not a reason to stop. It is a reason to **keep the finance spine as the declared month-six expansion**, so the company has a durable second leg before generative video matures |

---

## 7. What I would actually do with V2

**Take it. It is a better model than V1 on the things that decide whether anyone buys, and V1 was
better only on durability — which is a month-six problem, not a month-one problem.**

| | Action |
|---|---|
| **Fix now** | State the fee as **one-time, 30–35% of first-year compensation**, plus optional recurring EOR. Reading A |
| **Launch on two ICPs, not five** | **Marketing agencies + e-comm/DTC** — the two that clear FB **and** IG *and* hire editors as employees. Creators, coaches and digital media are expansion, and creators need a different fee model |
| **Keep from V1** | The **$500 as a paid audit rather than a refundable deposit** ([`OFFER.md`](OFFER.md) §9.1) — here it becomes a **paid ad-account and creative teardown**, which you can perform yourself and which *is* the work sample · the **free graded shortlist on the call** (§9.2) · the **12-month unlimited replacement, no cash refunds** · the **intent-seed scrape**, now pointed at *"remote video editor"* postings |
| **Keep the finance spine on the roadmap** | Declared month-six expansion. It scores 95.6 on compounding and it is the durability hedge against `AIDUR24`=3 |
| **Media: X now, newsletter at month three** | Formats are right. Publish the **first NUMBER from the first ten placements**, not from research |
| **Unchanged from the repo** | India first, South Africa as country two · direct hire not outsourcing · Meta as the only channel · **ten placements as the goal, and count how many buyers ask where the person is** |

### The one-line version of V2, tightened

> **The talent layer for internet businesses — starting with performance creative, sold to agencies
> and e-commerce brands on Meta, at a one-time fee of 30–35% of first-year comp, with optional EOR
> underneath and an *Internet Business Brief* built out of our own placement data.**

**And the honest summary of this comparison:** V2 moves the wedge to where the arbitrage actually is,
fixes a positioning error the repo's own last two screens had already identified, and hands the
operator a seat he can grade himself. **It costs durability, and the fix for that is keeping the
finance spine on the calendar rather than abandoning it.**
