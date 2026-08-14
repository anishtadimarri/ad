# Every Funnel, Enumerated and Ranked

> **This file replaces the rankings in [`CALLFUNNEL.md`](CALLFUNNEL.md), [`COMPETITORS.md`](COMPETITORS.md)**
> **and [`OPERATORS.md`](OPERATORS.md).** Their competitor research stands and is imported
> here. Their conversion arithmetic does not.

---

## 0. Why the last three rankings disagreed with each other

Three passes produced three different winners — the calculator, then the quiz, then the
instant quote. That was not new evidence changing my mind. **It was arithmetic built on
invented numbers.**

Each pass assigned every funnel five conversion parameters and multiplied them together:

```
  landing-page view -> entry offer   c1     invented
  entry offer       -> booked call   c2     invented
  booked            -> held          show   invented
  held              -> signed        close  invented
  signed            -> placed        fill   invented
```

Eighteen funnels × five parameters is **ninety invented numbers**, compounded, and printed
as `CAC $725 · 5.73:1`. The difference between `c1=0.078` and `c1=0.075` has no source, and
it decided the order. **The `[?]` tags and the sensitivity sweep made it look audited. It
was not.**

> So this file contains **no modelled CAC and no invented conversion rate.** If that means
> a question cannot be answered today, it says so instead.

---

## 1. What is actually known

Everything below that enters the ranking, and its source:

| Fact | Source | What it decides |
|---|---|---|
| Instant Form → appointment ~2%, vs ~17% for landing-page leads | `volumecreatives.com` | Kills on-platform destinations for a considered purchase |
| Instant Form SQL rates 35–55% lower than landing pages | `adamigo.ai` | Same conclusion, independent source |
| Contact <5 min closes 32%; >24h closes 12%; 21× qualify at 5 min vs 30 | `aimdoc.ai · plura.ai` | **IST is 9.5–10.5h ahead of US Eastern** — we cannot answer fast |
| 78% of B2B buyers buy from whoever responds first | `plura.ai` | Same |
| "Get a Free Quote"/"Book a Free Consultation" +15–30% CTR vs "Contact Us" | `analyticsbeyond.com` | Names the entry offer; does not rank funnels |
| Application → call held 30–60%; call → close 10–25% | `conversionxperts.com` | The only funnel-step band with a published range |
| Embedded scheduling link +30–40% booking vs asking for availability | `conversionxperts.com` | Favours self-serve booking over chase |
| ~50 optimisation events per ad set per 7 days to exit learning; CPA 20–50% higher inside | `Meta, multiple` | Caps how many cells $5k can test |
| Meta CPL all industries 2025: $41.60, +21% YoY | `get-ryze.ai` | A floor to sanity-check any CPL claim against |
| 4 of 8 live competitors show named candidates on the demand page; 0 of 10 gate the calendar | `fetched Aug 2026` | Precedent counts, from `competitors.py` |

### And what is not known — for us, specifically

- Landing-page view → any specific entry offer, for THIS offer and audience
- Entry offer → booked call, for any of the eighteen shapes below
- Booked → held, on cold Meta traffic to a free B2B call
- Held → signed, for an unknown India-based operator with no track record
- Signed → placed, at our fill rate, which has never been run

**Every one of those is a conversion rate, and every one is unmeasurable until the first
campaign runs.** That is not a gap to be modelled around. It is the reason the objective
below is *cost of finding out* rather than *predicted CAC*.

---

## 2. The enumeration

A funnel is four choices. The cross product is generated and filtered by coherence rules,
so nothing is missing because I did not think of it:

| Stage | Options |
|---|---|
| **Where the click lands** | 4 — Meta Instant Form (on-platform) · Click-to-Messenger / WhatsApp · Landing page · Straight to a calendar link, no page |
| **What is offered** | 10 — Book a call · See the graded bench · Get a price / instant quote · Free document — scorecard, salary data, guide · Free custom work on their asset · Paid micro-trial, $100–250 · Watch a video first · Use a calculator · Generic "contact us" · Join a newsletter / community |
| **How they are qualified** | 5 — No qualification · Passive fields on the form · Active gate that can reject · Payment · Manual application review |
| **How the call is booked** | 3 — Self-serve calendar embed · We follow up and book it · No call — self-serve purchase |

**4 × 10 × 5 × 3 = 600 combinations. 105 survive the coherence rules**
(495 are incoherent — an Instant Form cannot show a bench, a paid trial *is* the payment step,
a no-call close only works behind money, and so on. The rules are in the source.)

### The components, and the only properties that are scored

| Component | Systems | Build days | Human min/lead | Fields | Gives first | Chase? | Needs |
|---|---|---|---|---|---|---|---|
| **DESTINATION** | | | | | | | |
| Meta Instant Form (on-platform) | 1 | 0.25 | 10 | 3 | — | **yes** | — |
| Click-to-Messenger / WhatsApp | 1 | 0.5 | 14 | 2 | — | **yes** | — |
| Landing page | 1 | 1 | 0 | 0 | 4 | — | — |
| Straight to a calendar link, no page | 1 | 0.1 | 0 | 1 | — | — | — |
| **OFFER** | | | | | | | |
| Book a call | 0 | 0.25 | 0 | 1 | — | — | — |
| See the graded bench | 0 | 1.5 | 0 | 1 | 4 | — | 2 graded people per role |
| Get a price / instant quote | 0 | 1 | 0 | 2 | 3 | — | — |
| Free document — scorecard, salary data, guide | 0 | 1.5 | 0 | 1 | 2 | — | the document |
| Free custom work on their asset | 0 | 0.5 | 90 | 1 | 4 | **yes** | — |
| Paid micro-trial, $100–250 | 0 | 1 | 100 | 3 | 4 | — | — |
| Watch a video first | 0 | 3 | 0 | 0 | 3 | — | a video per role |
| Use a calculator | 0 | 2 | 0 | 3 | 3 | — | — |
| Generic "contact us" | 0 | 0.1 | 0 | 1 | — | — | — |
| Join a newsletter / community | 0 | 2 | 2 | 1 | 1 | — | ongoing content |
| **QUALIFICATION** | | | | | | | |
| No qualification | 0 | 0 | 0 | 0 | — | — | — |
| Passive fields on the form | 1 | 0.25 | 0 | 3 | — | — | — |
| Active gate that can reject | 1 | 0.75 | 0 | 4 | — | — | — |
| Payment | 1 | 0.5 | 0 | 2 | — | — | — |
| Manual application review | 0 | 0.5 | 6 | 5 | — | **yes** | — |
| **BOOKING** | | | | | | | |
| Self-serve calendar embed | 1 | 0.25 | 0 | 0 | — | — | — |
| We follow up and book it | 1 | 0.25 | 8 | 0 | — | **yes** | — |
| No call — self-serve purchase | 0 | 0.5 | 0 | 0 | — | — | — |

**A funnel's score is composed from its parts.** There is no per-funnel constant in this
file, which is precisely what was wrong with the last three.

---

## 3. The objective

> The operator does not know which ICP × role works. So the question is not *which funnel
> converts best* — unknowable today, and the thing I was faking. It is **which funnel is
> cheapest to stand up, cheapest to run, and tells us the most per week.**

| Dimension | Weight | Derived from |
|---|---|---|
| `EASE` | 24 | Systems to wire × days to build. Operator direction: first six months |
| `HANDS` | 18 | Minutes of human work per lead, forever. The solo constraint |
| `SIGNAL` | 16 | Qualification fields captured — how fast we learn which ICP × role works |
| `PERSUADE` | 16 | Does it give the visitor anything before asking? Structural, not a rate |
| `TZ` | 14 | Immune to the 32%→12% speed-to-lead penalty? [V] |
| `PROVEN` | 7 | Do the fetched competitors run this shape, and does a benchmark exist? |
| `READY` | 5 | Can it launch with assets that exist today? |

`EASE` and `HANDS` together carry **52%**, on the operator direction that the first six
months must be simple. `TZ` at 14 is the speed-to-lead penalty, which is a **fact about
where the operator lives**, not a parameter.

---

## 4. The ranking — all 105

| # | Funnel | Sys | Days | Min/lead | Fields | `EASE` | `HANDS` | `SIGNAL` | `TZ` | `PROVEN` | `READY` | **Score** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Landing page → use a calculator + passive fields on the form → self-serve calendar embed ✅ | 4 | 3.5 | 0 | 6 | 5.0 | 10.0 | 9.6 | 8.8 | 10.0 | 4.2 | 10.0 | **81.2** |
| 2 | Landing page → get a price / instant quote + active gate that can reject → self-serve calendar embed ✅ | 4 | 3 | 0 | 6 | 5.3 | 10.0 | 9.6 | 8.8 | 10.0 | 0.0 | 10.0 | **79.1** |
| 3 | Landing page → get a price / instant quote + passive fields on the form → self-serve calendar embed ✅ | 4 | 2.5 | 0 | 5 | 5.7 | 10.0 | 8.0 | 8.8 | 10.0 | 1.4 | 10.0 | **78.3** |
| 4 | Landing page → use a calculator + active gate that can reject → self-serve calendar embed | 4 | 4 | 0 | 7 | 4.6 | 10.0 | 10.0 | 8.8 | 10.0 | 0.2 | 10.0 | **78.2** |
| 5 | Landing page → see the graded bench + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 4 | 5.3 | 10.0 | 6.4 | 10.0 | 10.0 | 5.6 | 6.5 | **78.1** |
| 6 | Landing page → see the graded bench + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 5 | 5.0 | 10.0 | 8.0 | 10.0 | 10.0 | 1.6 | 6.5 | **77.0** |
| 7 | Landing page → use a calculator → self-serve calendar embed | 3 | 3.25 | 0 | 3 | 6.4 | 10.0 | 4.8 | 8.8 | 10.0 | 4.2 | 10.0 | **77.0** |
| 8 | Landing page → book a call + passive fields on the form → self-serve calendar embed | 4 | 1.75 | 0 | 4 | 6.2 | 10.0 | 6.4 | 5.0 | 10.0 | 8.4 | 10.0 | **75.9** |
| 9 | Landing page → book a call + active gate that can reject → self-serve calendar embed | 4 | 2.25 | 0 | 5 | 5.8 | 10.0 | 8.0 | 5.0 | 10.0 | 4.4 | 10.0 | **74.9** |
| 10 | Landing page → get a price / instant quote → self-serve calendar embed | 3 | 2.25 | 0 | 2 | 7.1 | 10.0 | 3.2 | 8.8 | 10.0 | 1.4 | 10.0 | **74.2** |
| 11 | Landing page → see the graded bench → self-serve calendar embed | 3 | 2.75 | 0 | 1 | 6.8 | 10.0 | 1.6 | 10.0 | 10.0 | 5.6 | 6.5 | **74.0** |
| 12 | Landing page → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 1.6 | 0 | 4 | 6.3 | 10.0 | 6.4 | 5.0 | 10.0 | 4.2 | 10.0 | **73.3** |
| 13 | Landing page → see the graded bench + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 6 | 6.4 | 7.3 | 9.6 | 10.0 | 2.0 | 8.6 | 6.5 | **72.0** |
| 14 | Straight to a calendar link, no page → book a call + passive fields on the form → self-serve calendar embed | 4 | 0.85 | 0 | 5 | 6.8 | 10.0 | 8.0 | 0.0 | 10.0 | 8.4 | 10.0 | **72.0** |
| 15 | Landing page → free document — scorecard, salary data, guide + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 5 | 5.0 | 10.0 | 8.0 | 7.5 | 10.0 | 0.0 | 6.5 | **71.9** |
| 16 | Landing page → book a call → self-serve calendar embed | 3 | 1.5 | 0 | 1 | 7.6 | 10.0 | 1.6 | 5.0 | 10.0 | 8.4 | 10.0 | **71.8** |
| 17 | Landing page → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 4 | 5.3 | 10.0 | 6.4 | 7.5 | 10.0 | 1.4 | 6.5 | **71.2** |
| 18 | Landing page → use a calculator + manual application review → self-serve calendar embed | 3 | 3.75 | 6 | 8 | 6.1 | 7.3 | 10.0 | 8.8 | 2.0 | 7.2 | 10.0 | **70.6** |
| 19 | Landing page → paid micro-trial, $100–250 + payment → no call — self-serve purchase | 3 | 3 | 100 | 5 | 6.6 | 2.1 | 8.0 | 10.0 | 10.0 | 4.4 | 10.0 | **70.4** |
| 20 | Landing page → get a price / instant quote + manual application review → self-serve calendar embed | 3 | 2.75 | 6 | 7 | 6.8 | 7.3 | 10.0 | 8.8 | 2.0 | 4.4 | 10.0 | **70.3** |
| 21 | Landing page → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 3.5 | 2 | 4 | 5.0 | 10.0 | 6.4 | 6.2 | 10.0 | 2.8 | 6.5 | **69.3** |
| 22 | Landing page → generic "contact us" → self-serve calendar embed | 3 | 1.35 | 0 | 1 | 7.8 | 10.0 | 1.6 | 5.0 | 10.0 | 4.2 | 10.0 | **69.1** |
| 23 | Landing page → book a call + manual application review → self-serve calendar embed | 3 | 2 | 6 | 6 | 7.3 | 7.3 | 9.6 | 5.0 | 2.0 | 10.0 | 10.0 | **68.9** |
| 24 | Landing page → watch a video first + active gate that can reject → self-serve calendar embed | 4 | 5 | 0 | 4 | 3.9 | 10.0 | 6.4 | 8.8 | 10.0 | 0.0 | 6.5 | **68.8** |
| 25 | Landing page → watch a video first + passive fields on the form → self-serve calendar embed | 4 | 4.5 | 0 | 3 | 4.2 | 10.0 | 4.8 | 8.8 | 10.0 | 1.4 | 6.5 | **68.1** |
| 26 | Straight to a calendar link, no page → book a call → self-serve calendar embed | 3 | 0.6 | 0 | 2 | 8.3 | 10.0 | 3.2 | 0.0 | 10.0 | 8.4 | 10.0 | **67.9** |
| 27 | Landing page → see the graded bench + manual application review → we follow up and book it | 3 | 3.25 | 14 | 6 | 6.4 | 5.0 | 9.6 | 10.0 | 2.0 | 8.6 | 6.5 | **67.8** |
| 28 | Landing page → paid micro-trial, $100–250 + payment → self-serve calendar embed | 4 | 2.75 | 100 | 5 | 5.5 | 2.1 | 8.0 | 10.0 | 10.0 | 4.4 | 10.0 | **67.7** |
| 29 | Landing page → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2.75 | 0 | 1 | 6.8 | 10.0 | 1.6 | 7.5 | 10.0 | 1.4 | 6.5 | **67.0** |
| 30 | Landing page → use a calculator + manual application review → we follow up and book it | 3 | 3.75 | 14 | 8 | 6.1 | 5.0 | 10.0 | 8.8 | 2.0 | 7.2 | 10.0 | **66.4** |
| 31 | Landing page → get a price / instant quote + manual application review → we follow up and book it | 3 | 2.75 | 14 | 7 | 6.8 | 5.0 | 10.0 | 8.8 | 2.0 | 4.4 | 10.0 | **66.1** |
| 32 | Landing page → join a newsletter / community → self-serve calendar embed | 3 | 3.25 | 2 | 1 | 6.4 | 10.0 | 1.6 | 6.2 | 10.0 | 2.8 | 6.5 | **65.2** |
| 33 | Landing page → free document — scorecard, salary data, guide + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 6 | 6.4 | 7.3 | 9.6 | 7.5 | 2.0 | 4.4 | 6.5 | **65.1** |
| 34 | Landing page → book a call + manual application review → we follow up and book it | 3 | 2 | 14 | 6 | 7.3 | 5.0 | 9.6 | 5.0 | 2.0 | 10.0 | 10.0 | **64.7** |
| 35 | Landing page → watch a video first → self-serve calendar embed | 3 | 4.25 | 0 | 0 | 5.7 | 10.0 | 0.0 | 8.8 | 10.0 | 1.4 | 6.5 | **64.0** |
| 36 | Landing page → use a calculator + passive fields on the form → we follow up and book it | 4 | 3.5 | 8 | 6 | 5.0 | 6.4 | 9.6 | 8.8 | 2.0 | 4.2 | 10.0 | **63.6** |
| 37 | Landing page → watch a video first + manual application review → self-serve calendar embed | 3 | 4.75 | 6 | 5 | 5.4 | 7.3 | 8.0 | 8.8 | 2.0 | 4.4 | 6.5 | **62.0** |
| 38 | Landing page → get a price / instant quote + active gate that can reject → we follow up and book it | 4 | 3 | 8 | 6 | 5.3 | 6.4 | 9.6 | 8.8 | 2.0 | 0.0 | 10.0 | **61.5** |
| 39 | Landing page → free document — scorecard, salary data, guide + manual application review → we follow up and book it | 3 | 3.25 | 14 | 6 | 6.4 | 5.0 | 9.6 | 7.5 | 2.0 | 4.4 | 6.5 | **60.9** |
| 40 | Landing page → get a price / instant quote + passive fields on the form → we follow up and book it | 4 | 2.5 | 8 | 5 | 5.7 | 6.4 | 8.0 | 8.8 | 2.0 | 1.4 | 10.0 | **60.7** |
| 41 | Landing page → use a calculator + active gate that can reject → we follow up and book it | 4 | 4 | 8 | 7 | 4.6 | 6.4 | 10.0 | 8.8 | 2.0 | 0.2 | 10.0 | **60.6** |
| 42 | Landing page → see the graded bench + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 4 | 5.3 | 6.4 | 6.4 | 10.0 | 2.0 | 5.6 | 6.5 | **60.5** |
| 43 | Landing page → see the graded bench + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 5 | 5.0 | 6.4 | 8.0 | 10.0 | 2.0 | 1.6 | 6.5 | **59.4** |
| 44 | Landing page → use a calculator → we follow up and book it | 3 | 3.25 | 8 | 3 | 6.4 | 6.4 | 4.8 | 8.8 | 2.0 | 4.2 | 10.0 | **59.4** |
| 45 | Landing page → book a call + passive fields on the form → we follow up and book it | 4 | 1.75 | 8 | 4 | 6.2 | 6.4 | 6.4 | 5.0 | 2.0 | 8.4 | 10.0 | **58.3** |
| 46 | Landing page → watch a video first + manual application review → we follow up and book it | 3 | 4.75 | 14 | 5 | 5.4 | 5.0 | 8.0 | 8.8 | 2.0 | 4.4 | 6.5 | **57.8** |
| 47 | Landing page → book a call + active gate that can reject → we follow up and book it | 4 | 2.25 | 8 | 5 | 5.8 | 6.4 | 8.0 | 5.0 | 2.0 | 4.4 | 10.0 | **57.2** |
| 48 | Landing page → get a price / instant quote → we follow up and book it | 3 | 2.25 | 8 | 2 | 7.1 | 6.4 | 3.2 | 8.8 | 2.0 | 1.4 | 10.0 | **56.6** |
| 49 | Landing page → paid micro-trial, $100–250 + payment → we follow up and book it | 4 | 2.75 | 108 | 5 | 5.5 | 2.0 | 8.0 | 10.0 | 2.0 | 4.4 | 10.0 | **56.4** |
| 50 | Landing page → see the graded bench → we follow up and book it | 3 | 2.75 | 8 | 1 | 6.8 | 6.4 | 1.6 | 10.0 | 2.0 | 5.6 | 6.5 | **56.4** |
| 51 | Landing page → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 1.6 | 8 | 4 | 6.3 | 6.4 | 6.4 | 5.0 | 2.0 | 4.2 | 10.0 | **55.6** |
| 52 | Landing page → free document — scorecard, salary data, guide + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 5 | 5.0 | 6.4 | 8.0 | 7.5 | 2.0 | 0.0 | 6.5 | **54.3** |
| 53 | Landing page → book a call → we follow up and book it | 3 | 1.5 | 8 | 1 | 7.6 | 6.4 | 1.6 | 5.0 | 2.0 | 8.4 | 10.0 | **54.2** |
| 54 | Landing page → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 4 | 5.3 | 6.4 | 6.4 | 7.5 | 2.0 | 1.4 | 6.5 | **53.6** |
| 55 | Meta Instant Form (on-platform) → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 1.25 | 100 | 7 | 6.5 | 2.1 | 10.0 | 5.0 | 2.0 | 3.0 | 10.0 | **53.3** |
| 56 | Meta Instant Form (on-platform) → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 1.25 | 108 | 7 | 6.5 | 2.0 | 10.0 | 5.0 | 2.0 | 3.0 | 10.0 | **53.1** |
| 57 | Meta Instant Form (on-platform) → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 0.85 | 10 | 7 | 6.8 | 5.8 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **52.7** |
| 58 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 2.25 | 10 | 7 | 5.8 | 5.8 | 10.0 | 2.5 | 2.0 | 3.0 | 6.5 | **52.6** |
| 59 | Meta Instant Form (on-platform) → book a call + passive fields on the form → self-serve calendar embed | 4 | 1 | 10 | 7 | 6.7 | 5.8 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **52.5** |
| 60 | Landing page → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 2 | 90 | 4 | 6.0 | 2.2 | 6.4 | 10.0 | 2.0 | 0.0 | 10.0 | **52.3** |
| 61 | Landing page → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 2 | 98 | 4 | 6.0 | 2.1 | 6.4 | 10.0 | 2.0 | 0.0 | 10.0 | **52.2** |
| 62 | Landing page → generic "contact us" → we follow up and book it | 3 | 1.35 | 8 | 1 | 7.8 | 6.4 | 1.6 | 5.0 | 2.0 | 4.2 | 10.0 | **51.5** |
| 63 | Landing page → watch a video first + active gate that can reject → we follow up and book it | 4 | 5 | 8 | 4 | 3.9 | 6.4 | 6.4 | 8.8 | 2.0 | 0.0 | 6.5 | **51.2** |
| 64 | Meta Instant Form (on-platform) → free custom work on their asset → self-serve calendar embed | 3 | 1 | 100 | 4 | 8.0 | 2.1 | 6.4 | 5.0 | 2.0 | 3.0 | 10.0 | **51.1** |
| 65 | Meta Instant Form (on-platform) → free custom work on their asset → we follow up and book it | 3 | 1 | 108 | 4 | 8.0 | 2.0 | 6.4 | 5.0 | 2.0 | 3.0 | 10.0 | **50.9** |
| 66 | Landing page → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 3.5 | 10 | 4 | 5.0 | 5.8 | 6.4 | 6.2 | 2.0 | 2.8 | 6.5 | **50.6** |
| 67 | Landing page → watch a video first + passive fields on the form → we follow up and book it | 4 | 4.5 | 8 | 3 | 4.2 | 6.4 | 4.8 | 8.8 | 2.0 | 1.4 | 6.5 | **50.5** |
| 68 | Meta Instant Form (on-platform) → generic "contact us" → self-serve calendar embed | 3 | 0.6 | 10 | 4 | 8.3 | 5.8 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **50.5** |
| 69 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2 | 10 | 4 | 7.3 | 5.8 | 6.4 | 2.5 | 2.0 | 3.0 | 6.5 | **50.4** |
| 70 | Meta Instant Form (on-platform) → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 0.85 | 18 | 7 | 6.8 | 4.5 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **50.3** |
| 71 | Meta Instant Form (on-platform) → book a call → self-serve calendar embed | 3 | 0.75 | 10 | 4 | 8.2 | 5.8 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **50.2** |
| 72 | Click-to-Messenger / WhatsApp → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 1.1 | 14 | 6 | 6.6 | 5.0 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **50.2** |
| 73 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 2.25 | 18 | 7 | 5.8 | 4.5 | 10.0 | 2.5 | 2.0 | 3.0 | 6.5 | **50.2** |
| 74 | Click-to-Messenger / WhatsApp → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 1.5 | 104 | 6 | 6.4 | 2.0 | 9.6 | 5.0 | 2.0 | 0.0 | 10.0 | **50.1** |
| 75 | Meta Instant Form (on-platform) → book a call + passive fields on the form → we follow up and book it | 4 | 1 | 18 | 7 | 6.7 | 4.5 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **50.0** |
| 76 | Click-to-Messenger / WhatsApp → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 1.5 | 112 | 6 | 6.4 | 2.0 | 9.6 | 5.0 | 2.0 | 0.0 | 10.0 | **49.9** |
| 77 | Click-to-Messenger / WhatsApp → book a call + passive fields on the form → self-serve calendar embed | 4 | 1.25 | 14 | 6 | 6.5 | 5.0 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **49.9** |
| 78 | Landing page → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2.75 | 8 | 1 | 6.8 | 6.4 | 1.6 | 7.5 | 2.0 | 1.4 | 6.5 | **49.4** |
| 79 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 2.5 | 14 | 6 | 5.7 | 5.0 | 9.6 | 2.5 | 2.0 | 1.4 | 6.5 | **48.9** |
| 80 | Meta Instant Form (on-platform) → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 2.75 | 12 | 7 | 5.5 | 5.4 | 10.0 | 1.2 | 2.0 | 3.0 | 6.5 | **48.9** |
| 81 | Click-to-Messenger / WhatsApp → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 1.1 | 22 | 6 | 6.6 | 4.1 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **48.5** |
| 82 | Click-to-Messenger / WhatsApp → book a call + passive fields on the form → we follow up and book it | 4 | 1.25 | 22 | 6 | 6.5 | 4.1 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **48.3** |
| 83 | Landing page → free custom work on their asset → self-serve calendar embed | 3 | 1.75 | 90 | 1 | 7.5 | 2.2 | 1.6 | 10.0 | 2.0 | 0.0 | 10.0 | **48.2** |
| 84 | Meta Instant Form (on-platform) → generic "contact us" → we follow up and book it | 3 | 0.6 | 18 | 4 | 8.3 | 4.5 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **48.0** |
| 85 | Landing page → free custom work on their asset → we follow up and book it | 3 | 1.75 | 98 | 1 | 7.5 | 2.1 | 1.6 | 10.0 | 2.0 | 0.0 | 10.0 | **48.0** |
| 86 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2 | 18 | 4 | 7.3 | 4.5 | 6.4 | 2.5 | 2.0 | 3.0 | 6.5 | **47.9** |
| 87 | Meta Instant Form (on-platform) → book a call → we follow up and book it | 3 | 0.75 | 18 | 4 | 8.2 | 4.5 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **47.8** |
| 88 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 2.5 | 22 | 6 | 5.7 | 4.1 | 9.6 | 2.5 | 2.0 | 1.4 | 6.5 | **47.3** |
| 89 | Meta Instant Form (on-platform) → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 2.75 | 20 | 7 | 5.5 | 4.3 | 10.0 | 1.2 | 2.0 | 3.0 | 6.5 | **47.0** |
| 90 | Meta Instant Form (on-platform) → join a newsletter / community → self-serve calendar embed | 3 | 2.5 | 12 | 4 | 6.9 | 5.4 | 6.4 | 1.2 | 2.0 | 3.0 | 6.5 | **46.7** |
| 91 | Click-to-Messenger / WhatsApp → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 3 | 16 | 6 | 5.3 | 4.7 | 9.6 | 1.2 | 2.0 | 2.8 | 6.5 | **46.6** |
| 92 | Landing page → join a newsletter / community → we follow up and book it | 3 | 3.25 | 10 | 1 | 6.4 | 5.8 | 1.6 | 6.2 | 2.0 | 2.8 | 6.5 | **46.5** |
| 93 | Landing page → watch a video first → we follow up and book it | 3 | 4.25 | 8 | 0 | 5.7 | 6.4 | 0.0 | 8.8 | 2.0 | 1.4 | 6.5 | **46.3** |
| 94 | Click-to-Messenger / WhatsApp → generic "contact us" → self-serve calendar embed | 3 | 0.85 | 14 | 3 | 8.1 | 5.0 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **46.0** |
| 95 | Click-to-Messenger / WhatsApp → free custom work on their asset → self-serve calendar embed | 3 | 1.25 | 104 | 3 | 7.8 | 2.0 | 4.8 | 5.0 | 2.0 | 0.0 | 10.0 | **45.9** |
| 96 | Click-to-Messenger / WhatsApp → free custom work on their asset → we follow up and book it | 3 | 1.25 | 112 | 3 | 7.8 | 2.0 | 4.8 | 5.0 | 2.0 | 0.0 | 10.0 | **45.8** |
| 97 | Click-to-Messenger / WhatsApp → book a call → self-serve calendar embed | 3 | 1 | 14 | 3 | 8.0 | 5.0 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **45.8** |
| 98 | Click-to-Messenger / WhatsApp → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 3 | 24 | 6 | 5.3 | 3.9 | 9.6 | 1.2 | 2.0 | 2.8 | 6.5 | **45.2** |
| 99 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2.25 | 14 | 3 | 7.1 | 5.0 | 4.8 | 2.5 | 2.0 | 1.4 | 6.5 | **44.8** |
| 100 | Meta Instant Form (on-platform) → join a newsletter / community → we follow up and book it | 3 | 2.5 | 20 | 4 | 6.9 | 4.3 | 6.4 | 1.2 | 2.0 | 3.0 | 6.5 | **44.7** |
| 101 | Click-to-Messenger / WhatsApp → generic "contact us" → we follow up and book it | 3 | 0.85 | 22 | 3 | 8.1 | 4.1 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **44.4** |
| 102 | Click-to-Messenger / WhatsApp → book a call → we follow up and book it | 3 | 1 | 22 | 3 | 8.0 | 4.1 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **44.1** |
| 103 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2.25 | 22 | 3 | 7.1 | 4.1 | 4.8 | 2.5 | 2.0 | 1.4 | 6.5 | **43.2** |
| 104 | Click-to-Messenger / WhatsApp → join a newsletter / community → self-serve calendar embed | 3 | 2.75 | 16 | 3 | 6.8 | 4.7 | 4.8 | 1.2 | 2.0 | 2.8 | 6.5 | **42.4** |
| 105 | Click-to-Messenger / WhatsApp → join a newsletter / community → we follow up and book it | 3 | 2.75 | 24 | 3 | 6.8 | 3.9 | 4.8 | 1.2 | 2.0 | 2.8 | 6.5 | **41.0** |

---

## 5. Reading the ranking

**26 of 105 funnels are immune to the timezone penalty**, and they take
**14 of the top 15 places.** That is the single strongest pattern, and it is
driven by a verified fact rather than a modelled one.

| What the ranking says | Why |
|---|---|
| **Landing page beats on-platform, everywhere** | The measured appointment gap is **~2% vs ~17%** [V]. Two independent sources. This is the one place where evidence, not judgement, does the work |
| **Self-serve booking beats chasing, everywhere** | **32% vs 12% close** by response time [V], and we are 9.5–10.5 hours from the buyer. Nothing else in the study is this decisive |
| **Fewer systems wins** | `EASE` is 24% of the weight because that is the operator direction. Every extra tool is a thing that breaks silently at 2am in a timezone where nobody is awake to notice |
| **Active gates rank badly** | **0 of 10 competitors gate** [V], and a gate is an extra system for an unknown operator to add friction with. Scored down, not gated out |
| **Anything needing an asset we lack is pushed down, not excluded** | `READY` is only 5 points. A bench is two weeks of real work — that is a *schedule* problem, not a disqualification, and the business needs it regardless |

### The top three, and what separates them


**1. Landing page → use a calculator + passive fields on the form → self-serve calendar embed** — 81.2

| | |
|---|---|
| Systems | **4** — ad account, page, passive fields on the form, self-serve calendar embed |
| Build | **3.5 days** |
| Human work per lead | **0 min** |
| Fields captured | **6** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| Use a calculator | Custom code. Captures their real volume and spend |
| Passive fields on the form | Captures without rejecting |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

**2. Landing page → get a price / instant quote + active gate that can reject → self-serve calendar embed** — 79.1

| | |
|---|---|
| Systems | **4** — ad account, page, active gate that can reject, self-serve calendar embed |
| Build | **3 days** |
| Human work per lead | **0 min** |
| Fields captured | **6** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| Get a price / instant quote | Our fee is a % of salary, so a quote is arithmetic not a range |
| Active gate that can reject | **0 of 10 competitors do this** [V] |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

**3. Landing page → get a price / instant quote + passive fields on the form → self-serve calendar embed** — 78.3

| | |
|---|---|
| Systems | **4** — ad account, page, passive fields on the form, self-serve calendar embed |
| Build | **2.5 days** |
| Human work per lead | **0 min** |
| Fields captured | **5** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| Get a price / instant quote | Our fee is a % of salary, so a quote is arithmetic not a range |
| Passive fields on the form | Captures without rejecting |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

---

## 6. What this ranking cannot tell you

Stated plainly, because the last three files did not.

| | |
|---|---|
| **It does not predict CAC** | No conversion rate for this offer, this audience or this operator exists. Any CAC I printed would be five invented numbers multiplied together — which is exactly what I did three times |
| **It does not say which funnel converts best** | It says which is cheapest to *try*. Those are different questions, and only the second one is answerable before spending money |
| **The weights are a judgement** | `EASE` at 30 comes from operator direction. Move it and the order moves. The *inputs* are facts; the *priorities* are yours |
| **Two components are estimates** | Build days and minutes-per-lead. Both are things you can check against your own experience in about a minute, which is the point of listing them separately rather than burying them |

### What would change the answer, and when you will know

| Question | Answered by | When |
|---|---|---|
| Does the page convert at all? | Cost per entry-offer completion, week one | **Day 7** |
| Which ICP × role? | Which seat the captured fields say | **Day 14–21** |
| Do booked calls show up? | Cal.com no-show rate | **Day 21** |
| Do held calls close? | First ten calls | **Day 30–45** |
| Was the timezone penalty real? | Compare self-booked vs any lead you chased | **Day 30**, and it settles the biggest assumption here |

**Only the last two are conversion rates, and both arrive within six weeks of spending.**
That is the honest reason not to model them now: **the campaign is cheaper than the model,**
**and it is right.**

