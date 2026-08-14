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
| **What is offered** | 13 — Book a call · See the graded bench · Get a price / instant quote · Free document — scorecard, salary data, guide · Free custom work on their asset · Paid micro-trial, $100–250 · Watch a video first · Volume calculator — units × vendor unit cost · Monthly-spend comparison — what you pay now vs full-time · See the test — the graded rubric for that role, and a scored sample · "Three graded candidates in 7 days" — the shortlist promise · Generic "contact us" · Join a newsletter / community |
| **How they are qualified** | 5 — No qualification · Passive fields on the form · Active gate that can reject · Payment · Manual application review |
| **How the call is booked** | 3 — Self-serve calendar embed · We follow up and book it · No call — self-serve purchase |

**4 × 13 × 5 × 3 = 780 combinations. 137 survive the coherence rules**
(643 are incoherent — an Instant Form cannot show a bench, a paid trial *is* the payment step,
a no-call close only works behind money, and so on. The rules are in the source.)

### The components, and the only properties that are scored

| Component | Systems | Build days | Human min/lead | Fields | Gives first | **Ports?** | Chase? | Needs |
|---|---|---|---|---|---|---|---|---|
| **DESTINATION** | | | | | | | | |
| Meta Instant Form (on-platform) | 1 | 0.25 | 10 | 3 | — | **10** | **yes** | — |
| Click-to-Messenger / WhatsApp | 1 | 0.5 | 14 | 2 | — | **10** | **yes** | — |
| Landing page | 1 | 1 | 0 | 0 | 4 | **10** | — | — |
| Straight to a calendar link, no page | 1 | 0.1 | 0 | 1 | — | **10** | — | — |
| **OFFER** | | | | | | | | |
| Book a call | 0 | 0.25 | 0 | 1 | — | **10** | — | — |
| See the graded bench | 0 | 1.5 | 0 | 1 | 4 | **5** | — | 2 graded people per role |
| Get a price / instant quote | 0 | 1 | 0 | 2 | 3 | **8** | — | — |
| Free document — scorecard, salary data, guide | 0 | 1.5 | 0 | 1 | 2 | **4** | — | the document |
| Free custom work on their asset | 0 | 0.5 | 90 | 1 | 4 | **2** | **yes** | — |
| Paid micro-trial, $100–250 | 0 | 1 | 100 | 3 | 4 | **2** | — | — |
| Watch a video first | 0 | 3 | 0 | 0 | 3 | **2** | — | a video per role |
| Volume calculator — units × vendor unit cost | 0 | 2 | 0 | 3 | 3 | **3** | — | — |
| Monthly-spend comparison — what you pay now vs full-time | 0 | 1.25 | 0 | 3 | 3 | **10** | — | — |
| See the test — the graded rubric for that role, and a scored sample | 0 | 1.5 | 0 | 2 | 4 | **9** | — | — |
| "Three graded candidates in 7 days" — the shortlist promise | 0 | 0.75 | 0 | 2 | 2 | **10** | — | — |
| Generic "contact us" | 0 | 0.1 | 0 | 1 | — | **10** | — | — |
| Join a newsletter / community | 0 | 2 | 2 | 1 | 1 | **6** | — | ongoing content |
| **QUALIFICATION** | | | | | | | | |
| No qualification | 0 | 0 | 0 | 0 | — | **10** | — | — |
| Passive fields on the form | 1 | 0.25 | 0 | 3 | — | **10** | — | — |
| Active gate that can reject | 1 | 0.75 | 0 | 4 | — | **10** | — | — |
| Payment | 1 | 0.5 | 0 | 2 | — | **10** | — | — |
| Manual application review | 0 | 0.5 | 6 | 5 | — | **10** | **yes** | — |
| **BOOKING** | | | | | | | | |
| Self-serve calendar embed | 1 | 0.25 | 0 | 0 | — | **10** | — | — |
| We follow up and book it | 1 | 0.25 | 8 | 0 | — | **10** | **yes** | — |
| No call — self-serve purchase | 0 | 0.5 | 0 | 0 | — | **10** | — | — |

**A funnel's score is composed from its parts.** There is no per-funnel constant in this
file, which is precisely what was wrong with the last three.

---

## 3. The objective

> The operator does not know which ICP × role works. So the question is not *which funnel
> converts best* — unknowable today, and the thing I was faking. It is **which funnel is
> cheapest to stand up, cheapest to run, and tells us the most per week.**

| Dimension | Weight | Derived from |
|---|---|---|
| `PORTABLE` | 22 | Works UNCHANGED across every ICP × role. We must test across, not down |
| `EASE` | 20 | Systems to wire × days to build. Operator direction: first six months |
| `HANDS` | 15 | Minutes of human work per lead, forever. The solo constraint |
| `SIGNAL` | 13 | Qualification fields captured — how fast we learn which ICP × role works |
| `PERSUADE` | 13 | Does it give the visitor anything before asking? Structural, not a rate |
| `TZ` | 12 | Immune to the 32%→12% speed-to-lead penalty? [V] |
| `PROVEN` | 3 | Do the fetched competitors run this shape, and does a benchmark exist? |
| `READY` | 2 | Can it launch with assets that exist today? |

`EASE` and `HANDS` together carry **52%**, on the operator direction that the first six
months must be simple. `TZ` at 14 is the speed-to-lead penalty, which is a **fact about
where the operator lives**, not a parameter.

---

## 4. The ranking — all 137

| # | Funnel | Sys | Days | Min/lead | Fields | `PORTABLE` | `EASE` | `HANDS` | `SIGNAL` | `PERSUADE` | `TZ` | `PROVEN` | `READY` | **Score** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Landing page → monthly-spend comparison — what you pay now vs full-time + passive fields on the form → self-serve calendar embed ✅ | 4 | 2.75 | 0 | 6 | 10.0 | 5.5 | 10.0 | 9.6 | 8.8 | 10.0 | 4.2 | 10.0 | **87.1** |
| 2 | Landing page → monthly-spend comparison — what you pay now vs full-time + active gate that can reject → self-serve calendar embed ✅ | 4 | 3.25 | 0 | 7 | 10.0 | 5.1 | 10.0 | 10.0 | 8.8 | 10.0 | 0.2 | 10.0 | **85.7** |
| 3 | Landing page → see the test — the graded rubric for that role, and a scored sample + active gate that can reject → self-serve calendar embed ✅ | 4 | 3.5 | 0 | 6 | 9.0 | 5.0 | 10.0 | 9.6 | 10.0 | 10.0 | 0.0 | 10.0 | **84.2** |
| 4 | Landing page → "three graded candidates in 7 days" — the shortlist promise + active gate that can reject → self-serve calendar embed | 4 | 2.75 | 0 | 6 | 10.0 | 5.5 | 10.0 | 9.6 | 7.5 | 10.0 | 0.0 | 10.0 | **84.2** |
| 5 | Landing page → monthly-spend comparison — what you pay now vs full-time → self-serve calendar embed | 3 | 2.5 | 0 | 3 | 10.0 | 6.9 | 10.0 | 4.8 | 8.8 | 10.0 | 4.2 | 10.0 | **83.8** |
| 6 | Landing page → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → self-serve calendar embed | 4 | 2.25 | 0 | 5 | 10.0 | 5.8 | 10.0 | 8.0 | 7.5 | 10.0 | 2.8 | 10.0 | **83.6** |
| 7 | Landing page → see the test — the graded rubric for that role, and a scored sample + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 5 | 9.0 | 5.3 | 10.0 | 8.0 | 10.0 | 10.0 | 0.0 | 10.0 | **82.8** |
| 8 | Landing page → get a price / instant quote + active gate that can reject → self-serve calendar embed | 4 | 3 | 0 | 6 | 8.0 | 5.3 | 10.0 | 9.6 | 8.8 | 10.0 | 0.0 | 10.0 | **81.1** |
| 9 | Landing page → book a call + active gate that can reject → self-serve calendar embed | 4 | 2.25 | 0 | 5 | 10.0 | 5.8 | 10.0 | 8.0 | 5.0 | 10.0 | 4.4 | 10.0 | **80.9** |
| 10 | Landing page → book a call + passive fields on the form → self-serve calendar embed | 4 | 1.75 | 0 | 4 | 10.0 | 6.2 | 10.0 | 6.4 | 5.0 | 10.0 | 8.4 | 10.0 | **80.7** |
| 11 | Landing page → "three graded candidates in 7 days" — the shortlist promise → self-serve calendar embed | 3 | 2 | 0 | 2 | 10.0 | 7.3 | 10.0 | 3.2 | 7.5 | 10.0 | 2.8 | 10.0 | **80.3** |
| 12 | Landing page → get a price / instant quote + passive fields on the form → self-serve calendar embed | 4 | 2.5 | 0 | 5 | 8.0 | 5.7 | 10.0 | 8.0 | 8.8 | 10.0 | 1.4 | 10.0 | **80.1** |
| 13 | Landing page → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 1.6 | 0 | 4 | 10.0 | 6.3 | 10.0 | 6.4 | 5.0 | 10.0 | 4.2 | 10.0 | **79.6** |
| 14 | Landing page → see the test — the graded rubric for that role, and a scored sample → self-serve calendar embed | 3 | 2.75 | 0 | 2 | 9.0 | 6.8 | 10.0 | 3.2 | 10.0 | 10.0 | 0.0 | 10.0 | **79.5** |
| 15 | Straight to a calendar link, no page → book a call + passive fields on the form → self-serve calendar embed | 4 | 0.85 | 0 | 5 | 10.0 | 6.8 | 10.0 | 8.0 | 0.0 | 10.0 | 8.4 | 10.0 | **77.5** |
| 16 | Landing page → book a call → self-serve calendar embed | 3 | 1.5 | 0 | 1 | 10.0 | 7.6 | 10.0 | 1.6 | 5.0 | 10.0 | 8.4 | 10.0 | **77.4** |
| 17 | Landing page → monthly-spend comparison — what you pay now vs full-time + manual application review → self-serve calendar embed | 3 | 3 | 6 | 8 | 10.0 | 6.6 | 7.3 | 10.0 | 8.8 | 2.0 | 7.2 | 10.0 | **77.1** |
| 18 | Landing page → get a price / instant quote → self-serve calendar embed | 3 | 2.25 | 0 | 2 | 8.0 | 7.1 | 10.0 | 3.2 | 8.8 | 10.0 | 1.4 | 10.0 | **76.8** |
| 19 | Landing page → generic "contact us" → self-serve calendar embed | 3 | 1.35 | 0 | 1 | 10.0 | 7.8 | 10.0 | 1.6 | 5.0 | 10.0 | 4.2 | 10.0 | **76.3** |
| 20 | Landing page → "three graded candidates in 7 days" — the shortlist promise + manual application review → self-serve calendar embed | 3 | 2.5 | 6 | 7 | 10.0 | 6.9 | 7.3 | 10.0 | 7.5 | 2.0 | 5.8 | 10.0 | **75.8** |
| 21 | Landing page → see the test — the graded rubric for that role, and a scored sample + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 7 | 9.0 | 6.4 | 7.3 | 10.0 | 10.0 | 2.0 | 3.0 | 10.0 | **74.9** |
| 22 | Straight to a calendar link, no page → book a call → self-serve calendar embed | 3 | 0.6 | 0 | 2 | 10.0 | 8.3 | 10.0 | 3.2 | 0.0 | 10.0 | 8.4 | 10.0 | **74.2** |
| 23 | Landing page → book a call + manual application review → self-serve calendar embed | 3 | 2 | 6 | 6 | 10.0 | 7.3 | 7.3 | 9.6 | 5.0 | 2.0 | 10.0 | 10.0 | **74.0** |
| 24 | Landing page → monthly-spend comparison — what you pay now vs full-time + manual application review → we follow up and book it | 3 | 3 | 14 | 8 | 10.0 | 6.6 | 5.0 | 10.0 | 8.8 | 2.0 | 7.2 | 10.0 | **73.6** |
| 25 | Landing page → see the graded bench + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 5 | 5.0 | 5.0 | 10.0 | 8.0 | 10.0 | 10.0 | 1.6 | 6.5 | **73.1** |
| 26 | Landing page → see the graded bench + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 4 | 5.0 | 5.3 | 10.0 | 6.4 | 10.0 | 10.0 | 5.6 | 6.5 | **72.9** |
| 27 | Landing page → "three graded candidates in 7 days" — the shortlist promise + manual application review → we follow up and book it | 3 | 2.5 | 14 | 7 | 10.0 | 6.9 | 5.0 | 10.0 | 7.5 | 2.0 | 5.8 | 10.0 | **72.3** |
| 28 | Landing page → get a price / instant quote + manual application review → self-serve calendar embed | 3 | 2.75 | 6 | 7 | 8.0 | 6.8 | 7.3 | 10.0 | 8.8 | 2.0 | 4.4 | 10.0 | **72.2** |
| 29 | Landing page → monthly-spend comparison — what you pay now vs full-time + passive fields on the form → we follow up and book it | 4 | 2.75 | 8 | 6 | 10.0 | 5.5 | 6.4 | 9.6 | 8.8 | 2.0 | 4.2 | 10.0 | **72.1** |
| 30 | Landing page → see the test — the graded rubric for that role, and a scored sample + manual application review → we follow up and book it | 3 | 3.25 | 14 | 7 | 9.0 | 6.4 | 5.0 | 10.0 | 10.0 | 2.0 | 3.0 | 10.0 | **71.4** |
| 31 | Landing page → monthly-spend comparison — what you pay now vs full-time + active gate that can reject → we follow up and book it | 4 | 3.25 | 8 | 7 | 10.0 | 5.1 | 6.4 | 10.0 | 8.8 | 2.0 | 0.2 | 10.0 | **70.7** |
| 32 | Landing page → volume calculator — units × vendor unit cost + passive fields on the form → self-serve calendar embed | 4 | 3.5 | 0 | 6 | 3.0 | 5.0 | 10.0 | 9.6 | 8.8 | 10.0 | 4.2 | 10.0 | **70.6** |
| 33 | Landing page → book a call + manual application review → we follow up and book it | 3 | 2 | 14 | 6 | 10.0 | 7.3 | 5.0 | 9.6 | 5.0 | 2.0 | 10.0 | 10.0 | **70.5** |
| 34 | Landing page → see the graded bench → self-serve calendar embed | 3 | 2.75 | 0 | 1 | 5.0 | 6.8 | 10.0 | 1.6 | 10.0 | 10.0 | 5.6 | 6.5 | **69.6** |
| 35 | Landing page → volume calculator — units × vendor unit cost + active gate that can reject → self-serve calendar embed | 4 | 4 | 0 | 7 | 3.0 | 4.6 | 10.0 | 10.0 | 8.8 | 10.0 | 0.2 | 10.0 | **69.2** |
| 36 | Landing page → see the test — the graded rubric for that role, and a scored sample + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 6 | 9.0 | 5.0 | 6.4 | 9.6 | 10.0 | 2.0 | 0.0 | 10.0 | **69.2** |
| 37 | Landing page → "three graded candidates in 7 days" — the shortlist promise + active gate that can reject → we follow up and book it | 4 | 2.75 | 8 | 6 | 10.0 | 5.5 | 6.4 | 9.6 | 7.5 | 2.0 | 0.0 | 10.0 | **69.2** |
| 38 | Landing page → monthly-spend comparison — what you pay now vs full-time → we follow up and book it | 3 | 2.5 | 8 | 3 | 10.0 | 6.9 | 6.4 | 4.8 | 8.8 | 2.0 | 4.2 | 10.0 | **68.8** |
| 39 | Landing page → get a price / instant quote + manual application review → we follow up and book it | 3 | 2.75 | 14 | 7 | 8.0 | 6.8 | 5.0 | 10.0 | 8.8 | 2.0 | 4.4 | 10.0 | **68.7** |
| 40 | Landing page → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → we follow up and book it | 4 | 2.25 | 8 | 5 | 10.0 | 5.8 | 6.4 | 8.0 | 7.5 | 2.0 | 2.8 | 10.0 | **68.7** |
| 41 | Landing page → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 3.5 | 2 | 4 | 6.0 | 5.0 | 10.0 | 6.4 | 6.2 | 10.0 | 2.8 | 6.5 | **68.7** |
| 42 | Landing page → see the test — the graded rubric for that role, and a scored sample + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 5 | 9.0 | 5.3 | 6.4 | 8.0 | 10.0 | 2.0 | 0.0 | 10.0 | **67.8** |
| 43 | Landing page → volume calculator — units × vendor unit cost → self-serve calendar embed | 3 | 3.25 | 0 | 3 | 3.0 | 6.4 | 10.0 | 4.8 | 8.8 | 10.0 | 4.2 | 10.0 | **67.3** |
| 44 | Landing page → free document — scorecard, salary data, guide + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 5 | 4.0 | 5.0 | 10.0 | 8.0 | 7.5 | 10.0 | 0.0 | 6.5 | **67.2** |
| 45 | Landing page → see the graded bench + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 6 | 5.0 | 6.4 | 7.3 | 9.6 | 10.0 | 2.0 | 8.6 | 6.5 | **66.6** |
| 46 | Landing page → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 4 | 4.0 | 5.3 | 10.0 | 6.4 | 7.5 | 10.0 | 1.4 | 6.5 | **66.2** |
| 47 | Landing page → get a price / instant quote + active gate that can reject → we follow up and book it | 4 | 3 | 8 | 6 | 8.0 | 5.3 | 6.4 | 9.6 | 8.8 | 2.0 | 0.0 | 10.0 | **66.1** |
| 48 | Landing page → book a call + active gate that can reject → we follow up and book it | 4 | 2.25 | 8 | 5 | 10.0 | 5.8 | 6.4 | 8.0 | 5.0 | 2.0 | 4.4 | 10.0 | **65.9** |
| 49 | Landing page → book a call + passive fields on the form → we follow up and book it | 4 | 1.75 | 8 | 4 | 10.0 | 6.2 | 6.4 | 6.4 | 5.0 | 2.0 | 8.4 | 10.0 | **65.7** |
| 50 | Landing page → "three graded candidates in 7 days" — the shortlist promise → we follow up and book it | 3 | 2 | 8 | 2 | 10.0 | 7.3 | 6.4 | 3.2 | 7.5 | 2.0 | 2.8 | 10.0 | **65.4** |
| 51 | Landing page → join a newsletter / community → self-serve calendar embed | 3 | 3.25 | 2 | 1 | 6.0 | 6.4 | 10.0 | 1.6 | 6.2 | 10.0 | 2.8 | 6.5 | **65.4** |
| 52 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise → self-serve calendar embed | 3 | 1.25 | 10 | 5 | 10.0 | 7.8 | 5.8 | 8.0 | 2.5 | 2.0 | 3.0 | 10.0 | **65.3** |
| 53 | Landing page → get a price / instant quote + passive fields on the form → we follow up and book it | 4 | 2.5 | 8 | 5 | 8.0 | 5.7 | 6.4 | 8.0 | 8.8 | 2.0 | 1.4 | 10.0 | **65.1** |
| 54 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → self-serve calendar embed | 4 | 1.5 | 10 | 8 | 10.0 | 6.4 | 5.8 | 10.0 | 2.5 | 2.0 | 3.0 | 10.0 | **65.0** |
| 55 | Landing page → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 1.6 | 8 | 4 | 10.0 | 6.3 | 6.4 | 6.4 | 5.0 | 2.0 | 4.2 | 10.0 | **64.7** |
| 56 | Landing page → see the test — the graded rubric for that role, and a scored sample → we follow up and book it | 3 | 2.75 | 8 | 2 | 9.0 | 6.8 | 6.4 | 3.2 | 10.0 | 2.0 | 0.0 | 10.0 | **64.6** |
| 57 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → self-serve calendar embed | 4 | 1.75 | 14 | 7 | 10.0 | 6.2 | 5.0 | 10.0 | 2.5 | 2.0 | 2.8 | 10.0 | **63.3** |
| 58 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise → we follow up and book it | 3 | 1.25 | 18 | 5 | 10.0 | 7.8 | 4.5 | 8.0 | 2.5 | 2.0 | 3.0 | 10.0 | **63.3** |
| 59 | Landing page → see the graded bench + manual application review → we follow up and book it | 3 | 3.25 | 14 | 6 | 5.0 | 6.4 | 5.0 | 9.6 | 10.0 | 2.0 | 8.6 | 6.5 | **63.1** |
| 60 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → we follow up and book it | 4 | 1.5 | 18 | 8 | 10.0 | 6.4 | 4.5 | 10.0 | 2.5 | 2.0 | 3.0 | 10.0 | **62.9** |
| 61 | Landing page → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2.75 | 0 | 1 | 4.0 | 6.8 | 10.0 | 1.6 | 7.5 | 10.0 | 1.4 | 6.5 | **62.9** |
| 62 | Meta Instant Form (on-platform) → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 0.85 | 10 | 7 | 10.0 | 6.8 | 5.8 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **62.6** |
| 63 | Landing page → book a call → we follow up and book it | 3 | 1.5 | 8 | 1 | 10.0 | 7.6 | 6.4 | 1.6 | 5.0 | 2.0 | 8.4 | 10.0 | **62.4** |
| 64 | Meta Instant Form (on-platform) → book a call + passive fields on the form → self-serve calendar embed | 4 | 1 | 10 | 7 | 10.0 | 6.7 | 5.8 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **62.4** |
| 65 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → we follow up and book it | 4 | 1.75 | 22 | 7 | 10.0 | 6.2 | 4.1 | 10.0 | 2.5 | 2.0 | 2.8 | 10.0 | **62.0** |
| 66 | Landing page → get a price / instant quote → we follow up and book it | 3 | 2.25 | 8 | 2 | 8.0 | 7.1 | 6.4 | 3.2 | 8.8 | 2.0 | 1.4 | 10.0 | **61.9** |
| 67 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise → self-serve calendar embed | 3 | 1.5 | 14 | 4 | 10.0 | 7.6 | 5.0 | 6.4 | 2.5 | 2.0 | 2.8 | 10.0 | **61.6** |
| 68 | Landing page → generic "contact us" → we follow up and book it | 3 | 1.35 | 8 | 1 | 10.0 | 7.8 | 6.4 | 1.6 | 5.0 | 2.0 | 4.2 | 10.0 | **61.4** |
| 69 | Meta Instant Form (on-platform) → generic "contact us" → self-serve calendar embed | 3 | 0.6 | 10 | 4 | 10.0 | 8.3 | 5.8 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **60.9** |
| 70 | Meta Instant Form (on-platform) → book a call → self-serve calendar embed | 3 | 0.75 | 10 | 4 | 10.0 | 8.2 | 5.8 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **60.7** |
| 71 | Landing page → volume calculator — units × vendor unit cost + manual application review → self-serve calendar embed | 3 | 3.75 | 6 | 8 | 3.0 | 6.1 | 7.3 | 10.0 | 8.8 | 2.0 | 7.2 | 10.0 | **60.7** |
| 72 | Meta Instant Form (on-platform) → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 0.85 | 18 | 7 | 10.0 | 6.8 | 4.5 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **60.6** |
| 73 | Click-to-Messenger / WhatsApp → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 1.1 | 14 | 6 | 10.0 | 6.6 | 5.0 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **60.5** |
| 74 | Meta Instant Form (on-platform) → book a call + passive fields on the form → we follow up and book it | 4 | 1 | 18 | 7 | 10.0 | 6.7 | 4.5 | 10.0 | 0.0 | 2.0 | 3.0 | 10.0 | **60.4** |
| 75 | Click-to-Messenger / WhatsApp → book a call + passive fields on the form → self-serve calendar embed | 4 | 1.25 | 14 | 6 | 10.0 | 6.5 | 5.0 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **60.3** |
| 76 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise → we follow up and book it | 3 | 1.5 | 22 | 4 | 10.0 | 7.6 | 4.1 | 6.4 | 2.5 | 2.0 | 2.8 | 10.0 | **60.2** |
| 77 | Landing page → watch a video first + active gate that can reject → self-serve calendar embed | 4 | 5 | 0 | 4 | 2.0 | 3.9 | 10.0 | 6.4 | 8.8 | 10.0 | 0.0 | 6.5 | **60.2** |
| 78 | Landing page → free document — scorecard, salary data, guide + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 6 | 4.0 | 6.4 | 7.3 | 9.6 | 7.5 | 2.0 | 4.4 | 6.5 | **59.9** |
| 79 | Landing page → paid micro-trial, $100–250 + payment → no call — self-serve purchase | 3 | 3 | 100 | 5 | 2.0 | 6.6 | 2.1 | 8.0 | 10.0 | 10.0 | 4.4 | 10.0 | **59.4** |
| 80 | Landing page → watch a video first + passive fields on the form → self-serve calendar embed | 4 | 4.5 | 0 | 3 | 2.0 | 4.2 | 10.0 | 4.8 | 8.8 | 10.0 | 1.4 | 6.5 | **59.2** |
| 81 | Click-to-Messenger / WhatsApp → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 1.1 | 22 | 6 | 10.0 | 6.6 | 4.1 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **59.2** |
| 82 | Click-to-Messenger / WhatsApp → book a call + passive fields on the form → we follow up and book it | 4 | 1.25 | 22 | 6 | 10.0 | 6.5 | 4.1 | 9.6 | 0.0 | 2.0 | 3.0 | 10.0 | **58.9** |
| 83 | Meta Instant Form (on-platform) → generic "contact us" → we follow up and book it | 3 | 0.6 | 18 | 4 | 10.0 | 8.3 | 4.5 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **58.9** |
| 84 | Meta Instant Form (on-platform) → book a call → we follow up and book it | 3 | 0.75 | 18 | 4 | 10.0 | 8.2 | 4.5 | 6.4 | 0.0 | 2.0 | 3.0 | 10.0 | **58.7** |
| 85 | Landing page → see the graded bench + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 5 | 5.0 | 5.0 | 6.4 | 8.0 | 10.0 | 2.0 | 1.6 | 6.5 | **58.1** |
| 86 | Landing page → see the graded bench + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 4 | 5.0 | 5.3 | 6.4 | 6.4 | 10.0 | 2.0 | 5.6 | 6.5 | **57.9** |
| 87 | Click-to-Messenger / WhatsApp → generic "contact us" → self-serve calendar embed | 3 | 0.85 | 14 | 3 | 10.0 | 8.1 | 5.0 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **57.2** |
| 88 | Landing page → volume calculator — units × vendor unit cost + manual application review → we follow up and book it | 3 | 3.75 | 14 | 8 | 3.0 | 6.1 | 5.0 | 10.0 | 8.8 | 2.0 | 7.2 | 10.0 | **57.2** |
| 89 | Landing page → paid micro-trial, $100–250 + payment → self-serve calendar embed | 4 | 2.75 | 100 | 5 | 2.0 | 5.5 | 2.1 | 8.0 | 10.0 | 10.0 | 4.4 | 10.0 | **57.2** |
| 90 | Click-to-Messenger / WhatsApp → book a call → self-serve calendar embed | 3 | 1 | 14 | 3 | 10.0 | 8.0 | 5.0 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **57.0** |
| 91 | Landing page → free document — scorecard, salary data, guide + manual application review → we follow up and book it | 3 | 3.25 | 14 | 6 | 4.0 | 6.4 | 5.0 | 9.6 | 7.5 | 2.0 | 4.4 | 6.5 | **56.4** |
| 92 | Landing page → watch a video first → self-serve calendar embed | 3 | 4.25 | 0 | 0 | 2.0 | 5.7 | 10.0 | 0.0 | 8.8 | 10.0 | 1.4 | 6.5 | **55.9** |
| 93 | Click-to-Messenger / WhatsApp → generic "contact us" → we follow up and book it | 3 | 0.85 | 22 | 3 | 10.0 | 8.1 | 4.1 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **55.9** |
| 94 | Landing page → volume calculator — units × vendor unit cost + passive fields on the form → we follow up and book it | 4 | 3.5 | 8 | 6 | 3.0 | 5.0 | 6.4 | 9.6 | 8.8 | 2.0 | 4.2 | 10.0 | **55.7** |
| 95 | Click-to-Messenger / WhatsApp → book a call → we follow up and book it | 3 | 1 | 22 | 3 | 10.0 | 8.0 | 4.1 | 4.8 | 0.0 | 2.0 | 3.0 | 10.0 | **55.7** |
| 96 | Landing page → see the graded bench → we follow up and book it | 3 | 2.75 | 8 | 1 | 5.0 | 6.8 | 6.4 | 1.6 | 10.0 | 2.0 | 5.6 | 6.5 | **54.7** |
| 97 | Landing page → volume calculator — units × vendor unit cost + active gate that can reject → we follow up and book it | 4 | 4 | 8 | 7 | 3.0 | 4.6 | 6.4 | 10.0 | 8.8 | 2.0 | 0.2 | 10.0 | **54.3** |
| 98 | Landing page → watch a video first + manual application review → self-serve calendar embed | 3 | 4.75 | 6 | 5 | 2.0 | 5.4 | 7.3 | 8.0 | 8.8 | 2.0 | 4.4 | 6.5 | **52.9** |
| 99 | Landing page → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 3.5 | 10 | 4 | 6.0 | 5.0 | 5.8 | 6.4 | 6.2 | 2.0 | 2.8 | 6.5 | **52.8** |
| 100 | Landing page → volume calculator — units × vendor unit cost → we follow up and book it | 3 | 3.25 | 8 | 3 | 3.0 | 6.4 | 6.4 | 4.8 | 8.8 | 2.0 | 4.2 | 10.0 | **52.4** |
| 101 | Landing page → free document — scorecard, salary data, guide + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 5 | 4.0 | 5.0 | 6.4 | 8.0 | 7.5 | 2.0 | 0.0 | 6.5 | **52.2** |
| 102 | Meta Instant Form (on-platform) → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 2.75 | 12 | 7 | 6.0 | 5.5 | 5.4 | 10.0 | 1.2 | 2.0 | 3.0 | 6.5 | **51.4** |
| 103 | Landing page → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 4 | 4.0 | 5.3 | 6.4 | 6.4 | 7.5 | 2.0 | 1.4 | 6.5 | **51.2** |
| 104 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 2.25 | 10 | 7 | 4.0 | 5.8 | 5.8 | 10.0 | 2.5 | 2.0 | 3.0 | 6.5 | **50.0** |
| 105 | Meta Instant Form (on-platform) → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 2.75 | 20 | 7 | 6.0 | 5.5 | 4.3 | 10.0 | 1.2 | 2.0 | 3.0 | 6.5 | **49.8** |
| 106 | Meta Instant Form (on-platform) → join a newsletter / community → self-serve calendar embed | 3 | 2.5 | 12 | 4 | 6.0 | 6.9 | 5.4 | 6.4 | 1.2 | 2.0 | 3.0 | 6.5 | **49.7** |
| 107 | Landing page → join a newsletter / community → we follow up and book it | 3 | 3.25 | 10 | 1 | 6.0 | 6.4 | 5.8 | 1.6 | 6.2 | 2.0 | 2.8 | 6.5 | **49.5** |
| 108 | Click-to-Messenger / WhatsApp → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 3 | 16 | 6 | 6.0 | 5.3 | 4.7 | 9.6 | 1.2 | 2.0 | 2.8 | 6.5 | **49.5** |
| 109 | Landing page → watch a video first + manual application review → we follow up and book it | 3 | 4.75 | 14 | 5 | 2.0 | 5.4 | 5.0 | 8.0 | 8.8 | 2.0 | 4.4 | 6.5 | **49.4** |
| 110 | Click-to-Messenger / WhatsApp → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 3 | 24 | 6 | 6.0 | 5.3 | 3.9 | 9.6 | 1.2 | 2.0 | 2.8 | 6.5 | **48.3** |
| 111 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2 | 10 | 4 | 4.0 | 7.3 | 5.8 | 6.4 | 2.5 | 2.0 | 3.0 | 6.5 | **48.3** |
| 112 | Meta Instant Form (on-platform) → join a newsletter / community → we follow up and book it | 3 | 2.5 | 20 | 4 | 6.0 | 6.9 | 4.3 | 6.4 | 1.2 | 2.0 | 3.0 | 6.5 | **48.0** |
| 113 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 2.25 | 18 | 7 | 4.0 | 5.8 | 4.5 | 10.0 | 2.5 | 2.0 | 3.0 | 6.5 | **48.0** |
| 114 | Landing page → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2.75 | 8 | 1 | 4.0 | 6.8 | 6.4 | 1.6 | 7.5 | 2.0 | 1.4 | 6.5 | **47.9** |
| 115 | Landing page → paid micro-trial, $100–250 + payment → we follow up and book it | 4 | 2.75 | 108 | 5 | 2.0 | 5.5 | 2.0 | 8.0 | 10.0 | 2.0 | 4.4 | 10.0 | **47.5** |
| 116 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 2.5 | 14 | 6 | 4.0 | 5.7 | 5.0 | 9.6 | 2.5 | 2.0 | 1.4 | 6.5 | **47.4** |
| 117 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2 | 18 | 4 | 4.0 | 7.3 | 4.5 | 6.4 | 2.5 | 2.0 | 3.0 | 6.5 | **46.3** |
| 118 | Click-to-Messenger / WhatsApp → join a newsletter / community → self-serve calendar embed | 3 | 2.75 | 16 | 3 | 6.0 | 6.8 | 4.7 | 4.8 | 1.2 | 2.0 | 2.8 | 6.5 | **46.2** |
| 119 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 2.5 | 22 | 6 | 4.0 | 5.7 | 4.1 | 9.6 | 2.5 | 2.0 | 1.4 | 6.5 | **46.1** |
| 120 | Landing page → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 2 | 90 | 4 | 2.0 | 6.0 | 2.2 | 6.4 | 10.0 | 2.0 | 0.0 | 10.0 | **45.4** |
| 121 | Meta Instant Form (on-platform) → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 1.25 | 100 | 7 | 2.0 | 6.5 | 2.1 | 10.0 | 5.0 | 2.0 | 3.0 | 10.0 | **45.3** |
| 122 | Landing page → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 2 | 98 | 4 | 2.0 | 6.0 | 2.1 | 6.4 | 10.0 | 2.0 | 0.0 | 10.0 | **45.2** |
| 123 | Landing page → watch a video first + active gate that can reject → we follow up and book it | 4 | 5 | 8 | 4 | 2.0 | 3.9 | 6.4 | 6.4 | 8.8 | 2.0 | 0.0 | 6.5 | **45.2** |
| 124 | Meta Instant Form (on-platform) → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 1.25 | 108 | 7 | 2.0 | 6.5 | 2.0 | 10.0 | 5.0 | 2.0 | 3.0 | 10.0 | **45.2** |
| 125 | Click-to-Messenger / WhatsApp → join a newsletter / community → we follow up and book it | 3 | 2.75 | 24 | 3 | 6.0 | 6.8 | 3.9 | 4.8 | 1.2 | 2.0 | 2.8 | 6.5 | **45.0** |
| 126 | Landing page → watch a video first + passive fields on the form → we follow up and book it | 4 | 4.5 | 8 | 3 | 2.0 | 4.2 | 6.4 | 4.8 | 8.8 | 2.0 | 1.4 | 6.5 | **44.3** |
| 127 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2.25 | 14 | 3 | 4.0 | 7.1 | 5.0 | 4.8 | 2.5 | 2.0 | 1.4 | 6.5 | **44.2** |
| 128 | Meta Instant Form (on-platform) → free custom work on their asset → self-serve calendar embed | 3 | 1 | 100 | 4 | 2.0 | 8.0 | 2.1 | 6.4 | 5.0 | 2.0 | 3.0 | 10.0 | **43.6** |
| 129 | Click-to-Messenger / WhatsApp → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 1.5 | 104 | 6 | 2.0 | 6.4 | 2.0 | 9.6 | 5.0 | 2.0 | 0.0 | 10.0 | **43.5** |
| 130 | Meta Instant Form (on-platform) → free custom work on their asset → we follow up and book it | 3 | 1 | 108 | 4 | 2.0 | 8.0 | 2.0 | 6.4 | 5.0 | 2.0 | 3.0 | 10.0 | **43.5** |
| 131 | Click-to-Messenger / WhatsApp → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 1.5 | 112 | 6 | 2.0 | 6.4 | 2.0 | 9.6 | 5.0 | 2.0 | 0.0 | 10.0 | **43.4** |
| 132 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2.25 | 22 | 3 | 4.0 | 7.1 | 4.1 | 4.8 | 2.5 | 2.0 | 1.4 | 6.5 | **42.8** |
| 133 | Landing page → free custom work on their asset → self-serve calendar embed | 3 | 1.75 | 90 | 1 | 2.0 | 7.5 | 2.2 | 1.6 | 10.0 | 2.0 | 0.0 | 10.0 | **42.1** |
| 134 | Landing page → free custom work on their asset → we follow up and book it | 3 | 1.75 | 98 | 1 | 2.0 | 7.5 | 2.1 | 1.6 | 10.0 | 2.0 | 0.0 | 10.0 | **42.0** |
| 135 | Landing page → watch a video first → we follow up and book it | 3 | 4.25 | 8 | 0 | 2.0 | 5.7 | 6.4 | 0.0 | 8.8 | 2.0 | 1.4 | 6.5 | **41.0** |
| 136 | Click-to-Messenger / WhatsApp → free custom work on their asset → self-serve calendar embed | 3 | 1.25 | 104 | 3 | 2.0 | 7.8 | 2.0 | 4.8 | 5.0 | 2.0 | 0.0 | 10.0 | **40.2** |
| 137 | Click-to-Messenger / WhatsApp → free custom work on their asset → we follow up and book it | 3 | 1.25 | 112 | 3 | 2.0 | 7.8 | 2.0 | 4.8 | 5.0 | 2.0 | 0.0 | 10.0 | **40.1** |

---

## 5. Reading the ranking

**35 of 137 funnels are immune to the timezone penalty**, and they take
**15 of the top 15 places.** That is the single strongest pattern, and it is
driven by a verified fact rather than a modelled one.

| What the ranking says | Why |
|---|---|
| **Landing page beats on-platform, everywhere** | The measured appointment gap is **~2% vs ~17%** [V]. Two independent sources. This is the one place where evidence, not judgement, does the work |
| **Self-serve booking beats chasing, everywhere** | **32% vs 12% close** by response time [V], and we are 9.5–10.5 hours from the buyer. Nothing else in the study is this decisive |
| **Fewer systems wins** | `EASE` is 20% of the weight because that is the operator direction. Every extra tool is a thing that breaks silently at 2am in a timezone where nobody is awake to notice |
| **Active gates rank badly** | **0 of 10 competitors gate** [V], and a gate is an extra system for an unknown operator to add friction with. Scored down, not gated out |
| **Anything needing an asset we lack is pushed down, not excluded** | `READY` is only 2 points. A bench is two weeks of real work — that is a *schedule* problem, not a disqualification, and the business needs it regardless |

### The top three, and what separates them


**1. Landing page → monthly-spend comparison — what you pay now vs full-time + passive fields on the form → self-serve calendar embed** — 87.1

| | |
|---|---|
| Systems | **4** — ad account, page, passive fields on the form, self-serve calendar embed |
| Build | **2.75 days** |
| Human work per lead | **0 min** |
| Fields captured | **6** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| Monthly-spend comparison — what you pay now vs full-time | **One input every buyer knows**, in the unit every vendor actually bills in. Somewhere and Athyna both ship this shape |
| Passive fields on the form | Captures without rejecting |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

**2. Landing page → monthly-spend comparison — what you pay now vs full-time + active gate that can reject → self-serve calendar embed** — 85.7

| | |
|---|---|
| Systems | **4** — ad account, page, active gate that can reject, self-serve calendar embed |
| Build | **3.25 days** |
| Human work per lead | **0 min** |
| Fields captured | **7** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| Monthly-spend comparison — what you pay now vs full-time | **One input every buyer knows**, in the unit every vendor actually bills in. Somewhere and Athyna both ship this shape |
| Active gate that can reject | **0 of 10 competitors do this** [V] |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

**3. Landing page → see the test — the graded rubric for that role, and a scored sample + active gate that can reject → self-serve calendar embed** — 84.2

| | |
|---|---|
| Systems | **4** — ad account, page, active gate that can reject, self-serve calendar embed |
| Build | **3.5 days** |
| Human work per lead | **0 min** |
| Fields captured | **6** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| See the test — the graded rubric for that role, and a scored sample | **No competitor shows a test or a score.** Needs the rubric written, not people hired — and a role you cannot write a rubric for is a role you cannot grade |
| Active gate that can reject | **0 of 10 competitors do this** [V] |
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

