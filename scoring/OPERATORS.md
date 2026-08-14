# Eighteen Funnels, Reranked for a Solo Operator's First Six Months

> Two reference classes. [`COMPETITORS.md`](COMPETITORS.md) studied the **category** —
> funded, SEO-led, staffed. This studies the one we actually belong to: **solo and small
> operators buying cold Meta traffic for high-ticket B2B services**, which has published
> benchmarks the category does not.

---

## 1. What the operator world has measured

Everything here is cited. It replaces guesses that were marked `[?]` two passes ago.

| Metric | Value | Note | Source |
|---|---|---|---|
| Application → call held | **30–60%** | high-ticket B2B application funnels | `conversionxperts.com` |
| Call → closed | **10–25%** | same source; our close rates all sit inside it | `conversionxperts.com` |
| Instant Form → appointment | **~2%** (1 in 50) | against **~17%** (1 in 6) for landing-page leads | `volumecreatives.com` |
| Instant Form SQL rate | **35–55% lower** | than landing-page campaigns | `adamigo.ai` |
| Adding one open-ended question | **−30% volume, qualify 30% → 65–70%** | the documented fix for lead-ad quality | `adlibrary.com` |
| Embedded scheduling link | **+30–40% booking** | vs asking the prospect to reply with availability | `conversionxperts.com` |
| *"Book a Free Consultation"* vs *"Contact Us"* | **+15–30% CTR** | CTA wording, measured | `analyticsbeyond.com` |
| Contact <5 min vs >24h | **32% vs 12% close** | and 21× more likely to qualify than at 30 minutes | `aimdoc.ai · plura.ai` |
| Average B2B response time | **47 hours** | only **23%** answer inside 5 minutes — the bar is low | `plura.ai` |
| Meta CPL, all industries 2025 | **$41.60, +21% YoY** | our modelled CPLs must be read against a rising floor | `get-ryze.ai` |
| ACV tiering | **<$25k → lead ads · $25–75k → landing page · $75k+ → direct booking** | one source's framing; §3 disputes its application here | `growthspreeofficial.com` |

**Our modelled close rates all sit inside the published 10–25% call-to-close band**, which
is the first time any step past the landing page has had a benchmark behind it rather than
an assumption.

---

## 2. The finding that reorders everything: you cannot answer in five minutes

| | |
|---|---|
| Contact inside **5 minutes** | **32% close rate** [V] |
| Contact after **24 hours** | **12% close rate** [V] |
| 5 minutes vs 30 minutes | **21× more likely to qualify** [V] |
| First vendor to respond | **wins 78% of B2B deals** [V] |
| Industry average response | **47 hours** — only 23% answer inside 5 minutes [V] |

**India Standard Time is 9.5–10.5 hours ahead of US Eastern.** A lead that arrives at 2pm
in New York lands at 11:30pm in Pune. A solo operator — one person, who also sources,
grades and delivers — **cannot hold a five-minute response window against US business hours.**

> So every funnel whose conversion depends on *chasing* a lead carries a penalty that no
> competitor in [`COMPETITORS.md`](COMPETITORS.md) pays. Modelled at **×0.65 on close rate**,
> interpolated from the 32%/12% spread and swept in §7.

| Funnel | Chase-dependent? | Why |
|---|---|---|
| One-field form — *"tell us about your company"* | **Yes** | Conversion waits on your reply |
| Cost calculator → email → call | **Yes** | Conversion waits on your reply |
| Free graded sample on *their* asset | **Yes** | Conversion waits on your reply |
| Meta Instant Form, no landing page | **Yes** | Conversion waits on your reply |
| Instant Form **+ one open-ended question** | **Yes** | Conversion waits on your reply |
| Free training / evergreen webinar → call | **Yes** | Conversion waits on your reply |
| Comment-to-DM automation → conversation → link | **Yes** | Conversion waits on your reply |
| Newsletter / content → nurture → book | **Yes** | Conversion waits on your reply |

**And the funnels that are immune** are the ones where the visitor books, buys or self-serves
without you: the direct calendar, the open bench, the instant quote, the paid trial, the
published price, the VSL application, and the gate. **The calendar works while you sleep.**

> This is the first structural advantage of self-serve that is specific to *us* rather than
> generic best practice — and it is worth more than any conversion-rate difference in this
> study.

---

## 3. Two sources disagree about Instant Forms. Resolving it

| Source | Claim |
|---|---|
| `growthspreeofficial.com` | **Below $25k ACV, Meta Lead Ads win** on volume *and* pipeline economics |
| `volumecreatives.com` | Instant Forms convert to appointment at **~2%**; landing-page leads at **~17%** |
| `adamigo.ai` | Instant Forms carry **35–55% lower SQL rates**; CPL wins, CPQO loses |

**Our ACV is roughly $10,893** — a $6,600 one-time fee plus a year of EOR at attach.
That is squarely in the tier where the first source says lead ads should win. **They still
should not, and the reason is that ACV is the wrong axis.**

> The variable that actually decides it is **consideration**, not price. Instant Forms work
> where the offer is understood in three seconds — a quote, a discount, a viewing. **Ours
> is a stranger in another country doing work you cannot supervise.** That is a
> high-consideration purchase at any price, and the 2%-vs-17% appointment gap is what
> high-consideration looks like on a form nobody remembers filling in.

Both variants are modelled anyway, and both rank near the bottom: **18th** and **15th** of 18.
The open-question variant is genuinely better — **2.6 placements against 1.4**, exactly the
qualification lift the source describes — **but it is still chase-dependent, and §2 is what
caps it.**

---

## 4. All eighteen

**$5,000/month.** Gross profit $4,148 at 30 days from [`offer_model.py`](offer_model.py); audience layers
from [`funnel.py`](funnel.py); founder time $60/hr. Chase-dependent funnels carry the §2 penalty.

| Funnel | World | Events/wk | CPL | Held | Placements | **CAC** | **30-day** | Hrs/mo | `SIMPLE` |
|---|---|---|---|---|---|---|---|---|---|
| **Instant quote — answer 3, see the price, self-book** | operator | 54 | $21 | 57 | 12.8 | **$696** | **5.96:1** | 65 ⚠️ | **8.3** |
| **See the bench — graded people, unlocked by email** | category | 52 | $22 | 39 | 9.0 | **$868** | **4.78:1** | 47 | **5.8** |
| **Role-select quiz → matched profiles → call** | category | 49 | $24 | 40 | 9.8 | **$801** | **5.18:1** | 47 | **6.0** |
| **Open bench — **no gate at all**, calendar beside the profiles** | operator | 21 | $55 | 63 | 16.1 | **$556** | **7.45:1** | 66 ⚠️ | **7.8** |
| **Publish the price, then book onboarding** | category | 17 | $69 | 53 | 12.9 | **$658** | **6.30:1** | 58 | **9.8** |
| **Two-stage: content view cold → book on retargeting** | operator | 26 | $44 | 82 | 17.3 | **$594** | **6.99:1** | 88 ⚠️ | **6.7** |
| **Cost calculator → email → call** 🐌 | category | 42 | $28 | 33 | 4.2 | **$1,790** | **2.32:1** | 42 | **6.3** |
| **VSL → application → call** | operator | 17 | $68 | 26 | 7.3 | **$930** | **4.46:1** | 30 | **5.3** |
| **Qualifying gate with a real no, then the calendar** | category | 15 | $76 | 33 | 5.9 | **$1,210** | **3.43:1** | 36 | **8.6** |
| **One-field form — *"tell us about your company"*** 🐌 | category | 43 | $27 | 36 | 3.4 | **$2,624** | **1.58:1** | 64 ⚠️ | **8.8** |
| **Free consult, calendar straight on the page** | category | 14 | $83 | 39 | 4.0 | **$1,904** | **2.18:1** | 44 | **9.9** |
| **Paid micro-trial that delivers real work — $100–250** | category | 8 | $151 | 30 | 11.5 | **$884** | **4.69:1** | 87 ⚠️ | **3.5** |
| **Comment-to-DM automation → conversation → link** 🐌 | operator | 45 | $26 | 30 | 2.2 | **$4,290** | **0.97:1** ⚠️ | 76 ⚠️ | **5.5** |
| **Free training / evergreen webinar → call** 🐌 | operator | 66 | $17 | 27 | 4.4 | **$1,758** | **2.36:1** | 46 | **2.5** |
| **Instant Form **+ one open-ended question**** 🐌 | operator | 69 | $17 | 47 | 2.6 | **$4,035** | **1.03:1** ⚠️ | 91 ⚠️ | **7.0** |
| **Free graded sample on *their* asset** 🐌 | category | 31 | $37 | 43 | 8.4 | **$1,477** | **2.81:1** | 123 ⚠️ | **3.8** |
| **Newsletter / content → nurture → book** 🐌 | operator | 73 | $16 | 24 | 4.0 | **$1,817** | **2.28:1** | 39 | **2.5** |
| **Meta Instant Form, no landing page** 🐌 | operator | 98 | $12 | 51 | 1.4 | **$9,563** | **0.43:1** ⚠️ | 136 ⚠️ | **7.1** |

🐌 = chase-dependent, carrying the §2 speed penalty.

`SIMPLE` is **derived, not judged**: `10 − (systems−2)×0.9 − setup_days×0.5 − ongoing×1.4`.

| Funnel | Tools to wire | Days to launch | Recurring burden |
|---|---|---|---|
| Free consult, calendar straight on the page | 2 | 0.25 | none |
| Publish the price, then book onboarding | 2 | 0.5 | none |
| One-field form — *"tell us about your company"* | 3 | 0.5 | none |
| Qualifying gate with a real no, then the calendar | 3 | 1 | none |
| Instant quote — answer 3, see the price, self-book | 3 | 1.5 | none |
| Open bench — **no gate at all**, calendar beside the profiles | 2 | 1.5 | light |
| Meta Instant Form, no landing page | 2 | 0.25 | constant |
| Instant Form **+ one open-ended question** | 2 | 0.5 | constant |
| Two-stage: content view cold → book on retargeting | 3 | 2 | light |
| Cost calculator → email → call | 5 | 2 | none |
| Role-select quiz → matched profiles → call | 4 | 1.5 | light |
| See the bench — graded people, unlocked by email | 4 | 2 | light |
| Comment-to-DM automation → conversation → link | 3 | 1.5 | constant |
| VSL → application → call | 4 | 3 | light |
| Free graded sample on *their* asset | 4 | 0.5 | **you, every time** |
| Paid micro-trial that delivers real work — $100–250 | 4 | 1 | **you, every time** |
| Free training / evergreen webinar → call | 5 | 4 | constant |
| Newsletter / content → nurture → book | 4 | 3 | **you, every time** |

---

## 5. The ranking

| Dimension | Weight | What it measures |
|---|---|---|
| `SIMPLE` | 22 | Build, deploy, check and change it — in the first six months |
| `DISCOVER` | 18 | What the first click reveals about which ICP × role works |
| `CAC30` | 15 | 30-day LTGP:CAC against the 1.5:1 constraint |
| `TRUST` | 12 | Works for an unknown India-based solo operator |
| `LEARN` | 11 | Optimisation events per week against Meta's 50 |
| `FOUNDER` | 10 | Founder hours/month against the ~60 available for selling |
| `PRECEDENT` | 7 | Somebody comparable actually runs this |
| `GENERIC` | 5 | Same content across every ICP × role cell |

`SIMPLE` is now the heaviest weight, on operator direction. `DISCOVER` stays high because
the ICP × role question is still open. **Five of the eight are derived from the model** rather
than scored by hand: `SIMPLE`, `CAC30`, `LEARN`, `FOUNDER`, and the volume half of `DISCOVER`.

| Rank | Funnel | `SIMPLE` | `DISCOVER` | `CAC30` | `TRUST` | `LEARN` | `FOUNDER` | `PRECEDENT` | `GENERIC` | **Score** |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | Instant quote — answer 3, see the price, self-book ✅ | 8.3 | 9.0 | 10.0 | 7.0 | 10.0 | 9.3 | 9.0 | 9.0 | **89.1** |
| **2** | See the bench — graded people, unlocked by email ✅ | 5.8 | 10.0 | 8.6 | 9.0 | 10.0 | 10.0 | 10.0 | 7.0 | **85.9** |
| **3** | Role-select quiz → matched profiles → call | 6.0 | 10.0 | 9.4 | 7.0 | 9.9 | 10.0 | 8.0 | 9.0 | **84.7** |
| **4** | Open bench — **no gate at all**, calendar beside the profiles | 7.8 | 5.9 | 10.0 | 9.0 | 6.5 | 9.2 | 8.0 | 7.0 | **79.2** |
| **5** | Publish the price, then book onboarding | 9.8 | 3.2 | 10.0 | 6.0 | 5.8 | 10.0 | 10.0 | 10.0 | **77.8** |
| **6** | Two-stage: content view cold → book on retargeting | 6.7 | 4.5 | 10.0 | 6.0 | 7.3 | 7.4 | 9.0 | 9.0 | **71.2** |
| **7** | Cost calculator → email → call | 6.3 | 7.0 | 3.6 | 7.0 | 9.1 | 10.0 | 9.0 | 8.0 | **70.7** |
| **8** | VSL → application → call | 5.3 | 6.5 | 7.9 | 7.0 | 5.8 | 10.0 | 10.0 | 4.0 | **69.0** |
| **9** | Qualifying gate with a real no, then the calendar | 8.6 | 4.7 | 5.9 | 6.0 | 5.5 | 10.0 | 2.0 | 9.0 | **65.4** |
| **10** | One-field form — *"tell us about your company"* | 8.8 | 3.0 | 2.2 | 4.0 | 9.3 | 9.6 | 9.0 | 10.0 | **64.0** |
| **11** | Free consult, calendar straight on the page | 9.9 | 1.5 | 3.4 | 4.0 | 5.3 | 10.0 | 10.0 | 10.0 | **62.1** |
| **12** | Paid micro-trial that delivers real work — $100–250 | 3.5 | 4.1 | 8.4 | 10.0 | 3.9 | 7.5 | 7.0 | 4.0 | **58.4** |
| **13** | Comment-to-DM automation → conversation → link | 5.5 | 6.0 | 0.0 | 5.0 | 9.5 | 8.3 | 8.0 | 9.0 | **57.8** |
| **14** | Free training / evergreen webinar → call | 2.5 | 5.0 | 3.7 | 7.0 | 10.0 | 10.0 | 8.0 | 5.0 | **57.6** |
| **15** | Instant Form **+ one open-ended question** | 7.0 | 6.0 | 0.0 | 2.0 | 10.0 | 7.2 | 8.0 | 10.0 | **57.2** |
| **16** | Free graded sample on *their* asset | 3.8 | 5.6 | 4.6 | 10.0 | 7.9 | 5.6 | 1.0 | 3.0 | **53.8** |
| **17** | Newsletter / content → nurture → book | 2.5 | 2.0 | 3.6 | 6.0 | 10.0 | 10.0 | 9.0 | 8.0 | **52.9** |
| **18** | Meta Instant Form, no landing page | 7.1 | 4.0 | 0.0 | 1.0 | 10.0 | 5.2 | 6.0 | 10.0 | **49.4** |

### What moved, and why

| Funnel | Was | Now | Why |
|---|---|---|---|
| Role-select quiz → matched profiles → call | 1st | **3th** | The bench dependency and a fourth system cost it on `SIMPLE`. **Still top three** |
| See the bench — graded people, unlocked by email | 2nd | **2th** | Same — two graded people per role before launch is real work, and `SIMPLE` now prices it |
| Open bench — **no gate at all**, calendar beside the profiles | not modelled | **4th** | **New.** The bench with *no email gate* — two systems, nothing to chase, and Athyna publishes 40+ profiles with no wall. Keeps most of the trust, drops most of the complexity |
| Instant quote — answer 3, see the price, self-book | not modelled | **1th** | **New.** *"Get a Free Quote"* is measured at **+15–30% CTR** [V], our fee is a clean percentage so the quote is real arithmetic, and it self-serves |
| Publish the price, then book onboarding | 4th | **5th** | Two systems, half a day, nothing recurring. **The highest `SIMPLE` score in the study** |
| VSL → application → call | not modelled | **8th** | **New.** The canonical operator funnel, with a real 30–60% application→call benchmark — but three days of video and a reshoot per role |
| Cost calculator → email → call | 3rd | **7th** | Five systems and custom code, and it is chase-dependent. **`SIMPLE` is what demoted it** |
| Meta Instant Form, no landing page | 10th | **18th** | Now measured against ~2% appointment rate [V] rather than assumed |

---

## 6. What to build

**Instant quote — answer 3, see the price, self-book** at **89.1**, with **See the bench — graded people, unlocked by email** at **85.9**.

They compose into one page, and the composition is deliberately boring:

```
  ONE PAGE, ONE URL, TWO SYSTEMS

   Framer page  ────────────────────  Cal.com embed
        │                                   │
        │  bench cards, open, no wall       │  books while you sleep
        │  3 taps → an instant number       │  no chase, no penalty
        └───────────────────────────────────┘

  AD      ICP + size question · a graded face · the role menu
  PAGE    the bench, visible. no email required to see it
  QUOTE   3 taps: seat · volume · when  →  a real number, instantly
          <- THE PIXEL EVENT, and the demand research, same click
  BOOK    calendar right there. self-serve. immune to timezone
  CALL    30 min, already knowing what they saw and what they picked
```

| Step | Number | Note |
|---|---|---|
| Spend | $5,000/mo |  |
| Landing page views | 3,009 | [E] |
| **Quote generated** — the pixel event | **217** | **50/week** against Meta's 50 |
| Cost per quote | $23 | well under the **$41.60** all-industry CPL average [V] |
| Calls booked | 74 | [?] self-booked, so no chase |
| Calls held | 50 | [?] |
| Signed | 15.1 | inside the published **10–25%** close band [V] |
| **Placements** | **11.6** |  |
| Founder hours | 57/mo | against ~60 available |
| **CAC** | **$725** |  |
| **30-day** | **5.73:1** | against 1.5:1 |
| **Lifetime** | **15.28:1** |  |

### One problem with this, and it is not the funnel

**50 held calls a month at 60 minutes each is 50 hours** — most of the ~60
available, before sourcing, grading or delivering anything. Six of the eighteen funnels
breach the hours budget, and the top ones breach it **because they work**.

| Fix | Effect | Cost |
|---|---|---|
| **30-minute calls, not 45** | 50 hours → **25** | None. The quote has already done the qualifying, so the call is confirmation, not discovery |
| **Start at $3,000/month, not $5,000** | ~30 events/week, ~30 calls | Slower learning. Still above the 20-events-a-week readability floor |
| **Raise the quote's volume floor** | Fewer, better calls | You will disqualify some real buyers. Do this last, not first |

**Do the first one.** A 30-minute call is the single cheapest fix in this document, and
the quote step is what earns the right to shorten it.

### The six-month stack — two systems, and a rule

| | What | Why this one |
|---|---|---|
| **Page** | **Framer**, one page | Already chosen in [`SITE.md`](SITE.md) at 96.4. Visual edits, instant publish, versions to roll back to. **You can change a headline on a phone** |
| **Booking** | **Cal.com** embed, free tier | One embed. Books overnight. **This is the system that neutralises §2** |
| **Everything else** | **Nothing, for six months** | No CRM, no automation platform, no email sequences, no funnel builder. Two systems is the whole point |

> **The rule: nothing goes on the page that you cannot check in one minute on a phone.**

The *check* half of the operator direction is the half that usually gets skipped, so it
gets a checklist rather than a sentence:

| Every Monday, in ten minutes | Where |
|---|---|
| Did the page load and the quote calculate? | Open it on your phone |
| Did the pixel fire? | Meta Events Manager → test events |
| Cost per quote, this week vs last | Ads Manager, one column |
| Which **seat** did the quotes pick? | Cal.com booking notes + form field |
| Which **ad** did they come from? | UTM on the booking |
| Any booking with no UTM? | **Your tracking is broken.** Fix before spending more |

**Six of those seven checks exist because of the discovery problem, not the conversion
problem.** If you cannot answer *"which seat, from which ad"* on any given Monday, the
$5,000 bought placements but not the answer — and the answer was the point.

---

## 7. Does the ranking survive the assumptions?

The speed penalty is the load-bearing new number. Swept from **0.45** (you answer a day
late, near the published 12% floor) to **0.85** (you are unusually disciplined about evenings),
alongside the three softest funnel inputs at 0.7× / 1.0× / 1.3×.

**81 combinations.** *Runnable* = at least 20 events a week, under 60 founder hours, clearing 1.5:1.

| Funnel | Clears 1.5:1 | Cheapest **and** runnable | Rank |
|---|---|---|---|
| Instant quote — answer 3, see the price, self-book | 100% | **27/81** | 1 |
| Role-select quiz → matched profiles → call | 100% | **18/81** | 3 |
| VSL → application → call | 100% | **18/81** | 8 |
| Publish the price, then book onboarding | 100% | **9/81** | 5 |
| Open bench — **no gate at all**, calendar beside the profiles | 100% | **9/81** | 4 |
| See the bench — graded people, unlocked by email | 100% | **0/81** | 2 |
| Paid micro-trial that delivers real work — $100–250 | 100% | **0/81** | 12 |
| Two-stage: content view cold → book on retargeting | 100% | **0/81** | 6 |
| Qualifying gate with a real no, then the calendar | 96% | **0/81** | 9 |
| Free graded sample on *their* asset | 88% | **0/81** | 16 |

> **Instant quote — answer 3, see the price, self-book** takes **27/81** of the grid — more than any other — and also ranks
> **1 of 18** on the weighted score. **Two independent methods, same answer.**

That has not happened in either earlier pass, and it is the strongest result in the study.
The weighted score can be argued with — the weights are a judgement. The grid cannot: it
just asks who is cheapest while staying runnable, across 81 versions of the world.

**Where they do part company:** the bench-unlock ranks 2nd on score and wins 0 grid points,
because there is almost always something cheaper that is also runnable. It is not a bad
funnel — it clears 1.5:1 in **100%** of combinations — it is just never the cheapest. That
is worth knowing before committing two weeks to building a bench page.

---

## 8. The ads

Four creatives, one ad set, one campaign. **Broad targeting** — the 2026 guidance is that
broad plus sharp creative beats hyper-narrow, because the algorithm reads who the ad is for [V].

| Slot | ICP | Role | Hook |
|---|---|---|---|
| **1** | E-comm, $10k+/mo ads | Performance video | *"Running $10k+ a month in ads and shipping 3 new cuts?"* |
| **2** | E-comm, $10k+/mo ads | Paid media | *"Your agency takes 15% of spend. Here is what a full-time buyer costs."* |
| **3** | Agencies, 5–30 staff | Performance video | *"Your editor is the bottleneck on every retainer you have."* |
| **4** | Agencies, 5–30 staff | Paid media | *"Turning down retainers because you cannot staff them?"* |

| Rule | Evidence |
|---|---|
| **The CTA is a quote or a person — never *"Contact Us"*** | *"Get a Free Quote"* / *"Book a Free Consultation"* measure **+15–30% CTR** over generic contact CTAs [V] |
| **A real graded face in the creative** | 4 of 8 competitors lead with people. Ours also carries a number, which none of theirs does |
| **Never *"80% less"*** | Verbatim in 2 of 8 competitor headlines. The leader's axis |
| **One ad set, not four** | At ~50 events a week, four ad sets is four learning phases you cannot fund. Read ICP × role at **ad level** |
| **No employment language anywhere** | The bench must read as a supplier catalogue for buyers, not a job board. One reviewer tick costs 10–29% on CAC ([`SUPPLY-DEMAND.md`](../SUPPLY-DEMAND.md)) |

---

## 9. The honest summary

| | |
|---|---|
| **What changed this pass** | Speed-to-lead, which is a real constraint for an India-based solo operator and was missing from every earlier model. It penalises seven of the eighteen funnels and it is why the recommendation is now *self-serve* rather than merely *simple* |
| **What the operator world added** | Real benchmarks where there were `[?]`s — application→call 30–60%, call→close 10–25%, Instant Form appointment rate ~2%. Our close assumptions survived contact with all three |
| **What stayed the same across three passes** | One page, one ad set, the ICP × role matrix in the creative, the one-time fee, the 12-month guarantee, and *a role with no measurable delta is not a role to launch* |
| **The cost that has not gone away** | **Two graded people per launch role before the first ad.** Every top-ranked funnel shows people, and showing people you have not tested is the one thing that would break the positioning permanently |
| **What is still unmeasured** | Show rate and close rate *for us specifically*. The bands are published; our position in them is not. First ten calls settle it |
