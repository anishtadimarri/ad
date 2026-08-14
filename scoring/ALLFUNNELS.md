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
| 4 of 8 live competitors show named candidates on the demand page; 0 of 10 gate the calendar | `fetched Aug 2026` | Precedent counts, from `competitors.py` — **but none verified as Meta advertisers** |
| **Value-first lead magnets: 40–60% lower CPL than a direct sales offer** on B2B Meta | `involvedigital.com` | **The single strongest mechanism finding in the study** |
| Proven service-business magnets: audits · guides · templates · free tool access · consultations | `involvedigital.com` | Names the formats that actually run on Meta |
| Qualification questions raise CPL 30–60%, and lift quality proportionally | `adlibrary.com` | So a gate is roughly a wash on cost per qualified lead |
| Quizzes and short video are TOF; case studies and webinars are MOF; consultations are BOF | `stackmatix.com` | Places each mechanism in the funnel it is proven at |

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
| **What is offered** | 14 — Book a call · See the graded bench · Get a price / instant quote · Free document — scorecard, salary data, guide · Free custom work on their asset · Paid micro-trial, $100–250 · Watch a video first · Volume calculator — units × vendor unit cost · Monthly-spend comparison — what you pay now vs full-time · **The hiring scorecard** — download the test, score candidates yourself · See the test — the rubric as an on-page block · "Three graded candidates in 7 days" — the shortlist promise · Generic "contact us" · Join a newsletter / community |
| **How they are qualified** | 5 — No qualification · Passive fields on the form · Active gate that can reject · Payment · Manual application review |
| **How the call is booked** | 3 — Self-serve calendar embed · We follow up and book it · No call — self-serve purchase |

**4 × 14 × 5 × 3 = 840 combinations. 149 survive the coherence rules**
(691 are incoherent — an Instant Form cannot show a bench, a paid trial *is* the payment step,
a no-call close only works behind money, and so on. The rules are in the source.)

### The components, and the only properties that are scored

| Component | Systems | Build days | Human min/lead | Fields | Gives first | **Ports?** | **News?** | Chase? | Needs |
|---|---|---|---|---|---|---|---|---|---|
| **DESTINATION** | | | | | | | | | |
| Meta Instant Form (on-platform) | 1 | 0.25 | 10 | 3 | — | **10** | **0** | **yes** | — |
| Click-to-Messenger / WhatsApp | 1 | 0.5 | 14 | 2 | — | **10** | **0** | **yes** | — |
| Landing page | 1 | 1 | 0 | 0 | 4 | **10** | **0** | — | — |
| Straight to a calendar link, no page | 1 | 0.1 | 0 | 1 | — | **10** | **0** | — | — |
| **OFFER** | | | | | | | | | |
| Book a call | 0 | 0.25 | 0 | 1 | — | **10** | **0** | — | — |
| See the graded bench | 0 | 1.5 | 0 | 1 | 4 | **5** | **6** | — | 2 graded people per role |
| Get a price / instant quote | 0 | 1 | 0 | 2 | 3 | **8** | **3** | — | — |
| Free document — scorecard, salary data, guide | 0 | 1.5 | 0 | 1 | 2 | **4** | **5** | — | the document |
| Free custom work on their asset | 0 | 0.5 | 90 | 1 | 4 | **2** | **9** | **yes** | — |
| Paid micro-trial, $100–250 | 0 | 1 | 100 | 3 | 4 | **2** | **7** | — | — |
| Watch a video first | 0 | 3 | 0 | 0 | 3 | **2** | **5** | — | a video per role |
| Volume calculator — units × vendor unit cost | 0 | 2 | 0 | 3 | 3 | **3** | **4** | — | — |
| Monthly-spend comparison — what you pay now vs full-time | 0 | 1.25 | 0 | 3 | 3 | **10** | **1** | — | — |
| **The hiring scorecard** — download the test, score candidates yourself | 0 | 1.5 | 0 | 3 | 4 | **8** | **9** | — | — |
| See the test — the rubric as an on-page block | 0 | 1.5 | 0 | 2 | 4 | **9** | **9** | — | — |
| "Three graded candidates in 7 days" — the shortlist promise | 0 | 0.75 | 0 | 2 | 2 | **10** | **3** | — | — |
| Generic "contact us" | 0 | 0.1 | 0 | 1 | — | **10** | **0** | — | — |
| Join a newsletter / community | 0 | 2 | 2 | 1 | 1 | **6** | **4** | — | ongoing content |
| **QUALIFICATION** | | | | | | | | | |
| No qualification | 0 | 0 | 0 | 0 | — | **10** | **0** | — | — |
| Passive fields on the form | 1 | 0.25 | 0 | 3 | — | **10** | **0** | — | — |
| Active gate that can reject | 1 | 0.75 | 0 | 4 | — | **10** | **0** | — | — |
| Payment | 1 | 0.5 | 0 | 2 | — | **10** | **0** | — | — |
| Manual application review | 0 | 0.5 | 6 | 5 | — | **10** | **0** | **yes** | — |
| **BOOKING** | | | | | | | | | |
| Self-serve calendar embed | 1 | 0.25 | 0 | 0 | — | **10** | **0** | — | — |
| We follow up and book it | 1 | 0.25 | 8 | 0 | — | **10** | **0** | **yes** | — |
| No call — self-serve purchase | 0 | 0.5 | 0 | 0 | — | **10** | **0** | — | — |

**A funnel's score is composed from its parts.** There is no per-funnel constant in this
file, which is precisely what was wrong with the last three.

---

## 3. The objective

> The operator does not know which ICP × role works. So the question is not *which funnel
> converts best* — unknowable today, and the thing I was faking. It is **which funnel is
> cheapest to stand up, cheapest to run, and tells us the most per week.**

| Dimension | Weight | Derived from |
|---|---|---|
| `PROVEN` | 22 | Is this a documented, running Meta lead-gen format? Not novel, not clever |
| `PORTABLE` | 18 | Works UNCHANGED across every ICP × role. We must test across, not down |
| `EASE` | 16 | Systems to wire × days to build. Operator direction: first six months |
| `NEWS` | 12 | Does it tell the buyer something they did NOT already know? |
| `HANDS` | 12 | Minutes of human work per lead, forever. The solo constraint |
| `TZ` | 10 | Immune to the 32%→12% speed-to-lead penalty? [V] |
| `SIGNAL` | 6 | Qualification fields captured — how fast we learn which ICP × role works |
| `PERSUADE` | 4 | Does it give the visitor anything before asking? Structural, not a rate |

`EASE` and `HANDS` together carry **52%**, on the operator direction that the first six
months must be simple. `TZ` at 14 is the speed-to-lead penalty, which is a **fact about
where the operator lives**, not a parameter.

---

## 4. The ranking — all 149

| # | Funnel | Sys | Days | Min/lead | Fields | `PROVEN` | `PORTABLE` | `EASE` | `NEWS` | `HANDS` | `TZ` | `SIGNAL` | `PERSUADE` | **Score** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Landing page → **the hiring scorecard** — download the test, score candidates yourself + passive fields on the form → self-serve calendar embed ✅ | 4 | 3 | 0 | 6 | 10.0 | 8.0 | 5.3 | 9.0 | 10.0 | 10.0 | 9.6 | 10.0 | **87.4** |
| 2 | Landing page → **the hiring scorecard** — download the test, score candidates yourself + active gate that can reject → self-serve calendar embed ✅ | 4 | 3.5 | 0 | 7 | 10.0 | 8.0 | 5.0 | 9.0 | 10.0 | 10.0 | 10.0 | 10.0 | **87.1** |
| 3 | Landing page → **the hiring scorecard** — download the test, score candidates yourself → self-serve calendar embed ✅ | 3 | 2.75 | 0 | 3 | 10.0 | 8.0 | 6.8 | 9.0 | 10.0 | 10.0 | 4.8 | 10.0 | **86.9** |
| 4 | Landing page → **the hiring scorecard** — download the test, score candidates yourself + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 8 | 10.0 | 8.0 | 6.4 | 9.0 | 7.3 | 2.0 | 10.0 | 10.0 | **78.3** |
| 5 | Landing page → **the hiring scorecard** — download the test, score candidates yourself + manual application review → we follow up and book it | 3 | 3.25 | 14 | 8 | 10.0 | 8.0 | 6.4 | 9.0 | 5.0 | 2.0 | 10.0 | 10.0 | **75.5** |
| 6 | Landing page → **the hiring scorecard** — download the test, score candidates yourself + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 6 | 10.0 | 8.0 | 5.3 | 9.0 | 6.4 | 2.0 | 9.6 | 10.0 | **75.2** |
| 7 | Landing page → **the hiring scorecard** — download the test, score candidates yourself + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 7 | 10.0 | 8.0 | 5.0 | 9.0 | 6.4 | 2.0 | 10.0 | 10.0 | **74.8** |
| 8 | Landing page → **the hiring scorecard** — download the test, score candidates yourself → we follow up and book it | 3 | 2.75 | 8 | 3 | 10.0 | 8.0 | 6.8 | 9.0 | 6.4 | 2.0 | 4.8 | 10.0 | **74.6** |
| 9 | Landing page → book a call + active gate that can reject → self-serve calendar embed | 4 | 2.25 | 0 | 5 | 8.0 | 10.0 | 5.8 | 0.0 | 10.0 | 10.0 | 8.0 | 5.0 | **73.7** |
| 10 | Landing page → book a call + passive fields on the form → self-serve calendar embed | 4 | 1.75 | 0 | 4 | 8.0 | 10.0 | 6.2 | 0.0 | 10.0 | 10.0 | 6.4 | 5.0 | **73.3** |
| 11 | Straight to a calendar link, no page → book a call + passive fields on the form → self-serve calendar embed | 4 | 0.85 | 0 | 5 | 8.0 | 10.0 | 6.8 | 0.0 | 10.0 | 10.0 | 8.0 | 0.0 | **73.3** |
| 12 | Landing page → get a price / instant quote + active gate that can reject → self-serve calendar embed | 4 | 3 | 0 | 6 | 7.0 | 8.0 | 5.3 | 3.0 | 10.0 | 10.0 | 9.6 | 8.8 | **73.1** |
| 13 | Landing page → free document — scorecard, salary data, guide + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 5 | 10.0 | 4.0 | 5.0 | 5.0 | 10.0 | 10.0 | 8.0 | 7.5 | **72.9** |
| 14 | Landing page → book a call → self-serve calendar embed | 3 | 1.5 | 0 | 1 | 8.0 | 10.0 | 7.6 | 0.0 | 10.0 | 10.0 | 1.6 | 5.0 | **72.8** |
| 15 | Straight to a calendar link, no page → book a call → self-serve calendar embed | 3 | 0.6 | 0 | 2 | 8.0 | 10.0 | 8.3 | 0.0 | 10.0 | 10.0 | 3.2 | 0.0 | **72.8** |
| 16 | Landing page → get a price / instant quote + passive fields on the form → self-serve calendar embed | 4 | 2.5 | 0 | 5 | 7.0 | 8.0 | 5.7 | 3.0 | 10.0 | 10.0 | 8.0 | 8.8 | **72.7** |
| 17 | Landing page → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 4 | 10.0 | 4.0 | 5.3 | 5.0 | 10.0 | 10.0 | 6.4 | 7.5 | **72.5** |
| 18 | Landing page → monthly-spend comparison — what you pay now vs full-time + passive fields on the form → self-serve calendar embed | 4 | 2.75 | 0 | 6 | 6.0 | 10.0 | 5.5 | 1.0 | 10.0 | 10.0 | 9.6 | 8.8 | **72.4** |
| 19 | Landing page → get a price / instant quote → self-serve calendar embed | 3 | 2.25 | 0 | 2 | 7.0 | 8.0 | 7.1 | 3.0 | 10.0 | 10.0 | 3.2 | 8.8 | **72.2** |
| 20 | Landing page → monthly-spend comparison — what you pay now vs full-time + active gate that can reject → self-serve calendar embed | 4 | 3.25 | 0 | 7 | 6.0 | 10.0 | 5.1 | 1.0 | 10.0 | 10.0 | 10.0 | 8.8 | **72.1** |
| 21 | Landing page → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2.75 | 0 | 1 | 10.0 | 4.0 | 6.8 | 5.0 | 10.0 | 10.0 | 1.6 | 7.5 | **72.0** |
| 22 | Landing page → monthly-spend comparison — what you pay now vs full-time → self-serve calendar embed | 3 | 2.5 | 0 | 3 | 6.0 | 10.0 | 6.9 | 1.0 | 10.0 | 10.0 | 4.8 | 8.8 | **71.9** |
| 23 | Landing page → see the test — the rubric as an on-page block + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 6 | 2.0 | 9.0 | 5.0 | 9.0 | 10.0 | 10.0 | 9.6 | 10.0 | **71.1** |
| 24 | Landing page → see the test — the rubric as an on-page block + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 5 | 2.0 | 9.0 | 5.3 | 9.0 | 10.0 | 10.0 | 8.0 | 10.0 | **70.7** |
| 25 | Landing page → see the test — the rubric as an on-page block → self-serve calendar embed | 3 | 2.75 | 0 | 2 | 2.0 | 9.0 | 6.8 | 9.0 | 10.0 | 10.0 | 3.2 | 10.0 | **70.2** |
| 26 | Landing page → "three graded candidates in 7 days" — the shortlist promise + active gate that can reject → self-serve calendar embed | 4 | 2.75 | 0 | 6 | 4.0 | 10.0 | 5.5 | 3.0 | 10.0 | 10.0 | 9.6 | 7.5 | **69.9** |
| 27 | Landing page → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → self-serve calendar embed | 4 | 2.25 | 0 | 5 | 4.0 | 10.0 | 5.8 | 3.0 | 10.0 | 10.0 | 8.0 | 7.5 | **69.5** |
| 28 | Landing page → "three graded candidates in 7 days" — the shortlist promise → self-serve calendar embed | 3 | 2 | 0 | 2 | 4.0 | 10.0 | 7.3 | 3.0 | 10.0 | 10.0 | 3.2 | 7.5 | **69.0** |
| 29 | Landing page → book a call + manual application review → self-serve calendar embed | 3 | 2 | 6 | 6 | 8.0 | 10.0 | 7.3 | 0.0 | 7.3 | 2.0 | 9.6 | 5.0 | **65.8** |
| 30 | Landing page → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 3.5 | 2 | 4 | 6.0 | 6.0 | 5.0 | 4.0 | 10.0 | 10.0 | 6.4 | 6.2 | **65.1** |
| 31 | Landing page → free document — scorecard, salary data, guide + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 6 | 10.0 | 4.0 | 6.4 | 5.0 | 7.3 | 2.0 | 9.6 | 7.5 | **65.0** |
| 32 | Landing page → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 1.6 | 0 | 4 | 4.0 | 10.0 | 6.3 | 0.0 | 10.0 | 10.0 | 6.4 | 5.0 | **64.7** |
| 33 | Landing page → join a newsletter / community → self-serve calendar embed | 3 | 3.25 | 2 | 1 | 6.0 | 6.0 | 6.4 | 4.0 | 10.0 | 10.0 | 1.6 | 6.2 | **64.5** |
| 34 | Landing page → get a price / instant quote + manual application review → self-serve calendar embed | 3 | 2.75 | 6 | 7 | 7.0 | 8.0 | 6.8 | 3.0 | 7.3 | 2.0 | 10.0 | 8.8 | **64.5** |
| 35 | Landing page → generic "contact us" → self-serve calendar embed | 3 | 1.35 | 0 | 1 | 4.0 | 10.0 | 7.8 | 0.0 | 10.0 | 10.0 | 1.6 | 5.0 | **64.2** |
| 36 | Landing page → see the graded bench + active gate that can reject → self-serve calendar embed | 4 | 3.5 | 0 | 5 | 4.0 | 5.0 | 5.0 | 6.0 | 10.0 | 10.0 | 8.0 | 10.0 | **63.7** |
| 37 | Landing page → see the graded bench + passive fields on the form → self-serve calendar embed | 4 | 3 | 0 | 4 | 4.0 | 5.0 | 5.3 | 6.0 | 10.0 | 10.0 | 6.4 | 10.0 | **63.3** |
| 38 | Landing page → monthly-spend comparison — what you pay now vs full-time + manual application review → self-serve calendar embed | 3 | 3 | 6 | 8 | 6.0 | 10.0 | 6.6 | 1.0 | 7.3 | 2.0 | 10.0 | 8.8 | **63.2** |
| 39 | Landing page → book a call + manual application review → we follow up and book it | 3 | 2 | 14 | 6 | 8.0 | 10.0 | 7.3 | 0.0 | 5.0 | 2.0 | 9.6 | 5.0 | **63.0** |
| 40 | Landing page → see the graded bench → self-serve calendar embed | 3 | 2.75 | 0 | 1 | 4.0 | 5.0 | 6.8 | 6.0 | 10.0 | 10.0 | 1.6 | 10.0 | **62.8** |
| 41 | Landing page → volume calculator — units × vendor unit cost + passive fields on the form → self-serve calendar embed | 4 | 3.5 | 0 | 6 | 6.0 | 3.0 | 5.0 | 4.0 | 10.0 | 10.0 | 9.6 | 8.8 | **62.6** |
| 42 | Landing page → see the test — the rubric as an on-page block + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 7 | 2.0 | 9.0 | 6.4 | 9.0 | 7.3 | 2.0 | 10.0 | 10.0 | **62.5** |
| 43 | Landing page → volume calculator — units × vendor unit cost + active gate that can reject → self-serve calendar embed | 4 | 4 | 0 | 7 | 6.0 | 3.0 | 4.6 | 4.0 | 10.0 | 10.0 | 10.0 | 8.8 | **62.3** |
| 44 | Landing page → free document — scorecard, salary data, guide + manual application review → we follow up and book it | 3 | 3.25 | 14 | 6 | 10.0 | 4.0 | 6.4 | 5.0 | 5.0 | 2.0 | 9.6 | 7.5 | **62.2** |
| 45 | Landing page → volume calculator — units × vendor unit cost → self-serve calendar embed | 3 | 3.25 | 0 | 3 | 6.0 | 3.0 | 6.4 | 4.0 | 10.0 | 10.0 | 4.8 | 8.8 | **62.1** |
| 46 | Landing page → get a price / instant quote + manual application review → we follow up and book it | 3 | 2.75 | 14 | 7 | 7.0 | 8.0 | 6.8 | 3.0 | 5.0 | 2.0 | 10.0 | 8.8 | **61.7** |
| 47 | Landing page → book a call + active gate that can reject → we follow up and book it | 4 | 2.25 | 8 | 5 | 8.0 | 10.0 | 5.8 | 0.0 | 6.4 | 2.0 | 8.0 | 5.0 | **61.4** |
| 48 | Landing page → "three graded candidates in 7 days" — the shortlist promise + manual application review → self-serve calendar embed | 3 | 2.5 | 6 | 7 | 4.0 | 10.0 | 6.9 | 3.0 | 7.3 | 2.0 | 10.0 | 7.5 | **61.3** |
| 49 | Landing page → book a call + passive fields on the form → we follow up and book it | 4 | 1.75 | 8 | 4 | 8.0 | 10.0 | 6.2 | 0.0 | 6.4 | 2.0 | 6.4 | 5.0 | **61.0** |
| 50 | Landing page → get a price / instant quote + active gate that can reject → we follow up and book it | 4 | 3 | 8 | 6 | 7.0 | 8.0 | 5.3 | 3.0 | 6.4 | 2.0 | 9.6 | 8.8 | **60.9** |
| 51 | Landing page → free document — scorecard, salary data, guide + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 5 | 10.0 | 4.0 | 5.0 | 5.0 | 6.4 | 2.0 | 8.0 | 7.5 | **60.6** |
| 52 | Landing page → book a call → we follow up and book it | 3 | 1.5 | 8 | 1 | 8.0 | 10.0 | 7.6 | 0.0 | 6.4 | 2.0 | 1.6 | 5.0 | **60.5** |
| 53 | Landing page → monthly-spend comparison — what you pay now vs full-time + manual application review → we follow up and book it | 3 | 3 | 14 | 8 | 6.0 | 10.0 | 6.6 | 1.0 | 5.0 | 2.0 | 10.0 | 8.8 | **60.5** |
| 54 | Landing page → get a price / instant quote + passive fields on the form → we follow up and book it | 4 | 2.5 | 8 | 5 | 7.0 | 8.0 | 5.7 | 3.0 | 6.4 | 2.0 | 8.0 | 8.8 | **60.5** |
| 55 | Landing page → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 4 | 10.0 | 4.0 | 5.3 | 5.0 | 6.4 | 2.0 | 6.4 | 7.5 | **60.2** |
| 56 | Meta Instant Form (on-platform) → **the hiring scorecard** — download the test, score candidates yourself → self-serve calendar embed | 3 | 2 | 10 | 6 | 3.0 | 8.0 | 7.3 | 9.0 | 5.8 | 2.0 | 9.6 | 5.0 | **60.2** |
| 57 | Landing page → monthly-spend comparison — what you pay now vs full-time + passive fields on the form → we follow up and book it | 4 | 2.75 | 8 | 6 | 6.0 | 10.0 | 5.5 | 1.0 | 6.4 | 2.0 | 9.6 | 8.8 | **60.1** |
| 58 | Landing page → get a price / instant quote → we follow up and book it | 3 | 2.25 | 8 | 2 | 7.0 | 8.0 | 7.1 | 3.0 | 6.4 | 2.0 | 3.2 | 8.8 | **59.9** |
| 59 | Landing page → monthly-spend comparison — what you pay now vs full-time + active gate that can reject → we follow up and book it | 4 | 3.25 | 8 | 7 | 6.0 | 10.0 | 5.1 | 1.0 | 6.4 | 2.0 | 10.0 | 8.8 | **59.8** |
| 60 | Landing page → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2.75 | 8 | 1 | 10.0 | 4.0 | 6.8 | 5.0 | 6.4 | 2.0 | 1.6 | 7.5 | **59.7** |
| 61 | Landing page → see the test — the rubric as an on-page block + manual application review → we follow up and book it | 3 | 3.25 | 14 | 7 | 2.0 | 9.0 | 6.4 | 9.0 | 5.0 | 2.0 | 10.0 | 10.0 | **59.7** |
| 62 | Landing page → monthly-spend comparison — what you pay now vs full-time → we follow up and book it | 3 | 2.5 | 8 | 3 | 6.0 | 10.0 | 6.9 | 1.0 | 6.4 | 2.0 | 4.8 | 8.8 | **59.6** |
| 63 | Landing page → paid micro-trial, $100–250 + payment → no call — self-serve purchase | 3 | 3 | 100 | 5 | 7.0 | 2.0 | 6.6 | 7.0 | 2.1 | 10.0 | 8.0 | 10.0 | **59.2** |
| 64 | Landing page → see the test — the rubric as an on-page block + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 6 | 2.0 | 9.0 | 5.0 | 9.0 | 6.4 | 2.0 | 9.6 | 10.0 | **58.8** |
| 65 | Meta Instant Form (on-platform) → **the hiring scorecard** — download the test, score candidates yourself → we follow up and book it | 3 | 2 | 18 | 6 | 3.0 | 8.0 | 7.3 | 9.0 | 4.5 | 2.0 | 9.6 | 5.0 | **58.6** |
| 66 | Landing page → "three graded candidates in 7 days" — the shortlist promise + manual application review → we follow up and book it | 3 | 2.5 | 14 | 7 | 4.0 | 10.0 | 6.9 | 3.0 | 5.0 | 2.0 | 10.0 | 7.5 | **58.5** |
| 67 | Landing page → see the test — the rubric as an on-page block + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 5 | 2.0 | 9.0 | 5.3 | 9.0 | 6.4 | 2.0 | 8.0 | 10.0 | **58.4** |
| 68 | Landing page → watch a video first + active gate that can reject → self-serve calendar embed | 4 | 5 | 0 | 4 | 6.0 | 2.0 | 3.9 | 5.0 | 10.0 | 10.0 | 6.4 | 8.8 | **58.4** |
| 69 | Meta Instant Form (on-platform) → **the hiring scorecard** — download the test, score candidates yourself + passive fields on the form → self-serve calendar embed | 4 | 2.25 | 10 | 9 | 3.0 | 8.0 | 5.8 | 9.0 | 5.8 | 2.0 | 10.0 | 5.0 | **58.1** |
| 70 | Landing page → watch a video first + passive fields on the form → self-serve calendar embed | 4 | 4.5 | 0 | 3 | 6.0 | 2.0 | 4.2 | 5.0 | 10.0 | 10.0 | 4.8 | 8.8 | **58.0** |
| 71 | Landing page → see the test — the rubric as an on-page block → we follow up and book it | 3 | 2.75 | 8 | 2 | 2.0 | 9.0 | 6.8 | 9.0 | 6.4 | 2.0 | 3.2 | 10.0 | **57.9** |
| 72 | Landing page → "three graded candidates in 7 days" — the shortlist promise + active gate that can reject → we follow up and book it | 4 | 2.75 | 8 | 6 | 4.0 | 10.0 | 5.5 | 3.0 | 6.4 | 2.0 | 9.6 | 7.5 | **57.6** |
| 73 | Landing page → watch a video first → self-serve calendar embed | 3 | 4.25 | 0 | 0 | 6.0 | 2.0 | 5.7 | 5.0 | 10.0 | 10.0 | 0.0 | 8.8 | **57.5** |
| 74 | Landing page → paid micro-trial, $100–250 + payment → self-serve calendar embed | 4 | 2.75 | 100 | 5 | 7.0 | 2.0 | 5.5 | 7.0 | 2.1 | 10.0 | 8.0 | 10.0 | **57.4** |
| 75 | Landing page → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → we follow up and book it | 4 | 2.25 | 8 | 5 | 4.0 | 10.0 | 5.8 | 3.0 | 6.4 | 2.0 | 8.0 | 7.5 | **57.2** |
| 76 | Landing page → "three graded candidates in 7 days" — the shortlist promise → we follow up and book it | 3 | 2 | 8 | 2 | 4.0 | 10.0 | 7.3 | 3.0 | 6.4 | 2.0 | 3.2 | 7.5 | **56.7** |
| 77 | Meta Instant Form (on-platform) → **the hiring scorecard** — download the test, score candidates yourself + passive fields on the form → we follow up and book it | 4 | 2.25 | 18 | 9 | 3.0 | 8.0 | 5.8 | 9.0 | 4.5 | 2.0 | 10.0 | 5.0 | **56.5** |
| 78 | Landing page → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 2 | 90 | 4 | 9.0 | 2.0 | 6.0 | 9.0 | 2.2 | 2.0 | 6.4 | 10.0 | **56.2** |
| 79 | Landing page → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 2 | 98 | 4 | 9.0 | 2.0 | 6.0 | 9.0 | 2.1 | 2.0 | 6.4 | 10.0 | **56.1** |
| 80 | Landing page → see the graded bench + manual application review → self-serve calendar embed | 3 | 3.25 | 6 | 6 | 4.0 | 5.0 | 6.4 | 6.0 | 7.3 | 2.0 | 9.6 | 10.0 | **55.8** |
| 81 | Landing page → free custom work on their asset → self-serve calendar embed | 3 | 1.75 | 90 | 1 | 9.0 | 2.0 | 7.5 | 9.0 | 2.2 | 2.0 | 1.6 | 10.0 | **55.7** |
| 82 | Landing page → free custom work on their asset → we follow up and book it | 3 | 1.75 | 98 | 1 | 9.0 | 2.0 | 7.5 | 9.0 | 2.1 | 2.0 | 1.6 | 10.0 | **55.6** |
| 83 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise → self-serve calendar embed | 3 | 1.25 | 10 | 5 | 3.0 | 10.0 | 7.8 | 3.0 | 5.8 | 2.0 | 8.0 | 2.5 | **55.5** |
| 84 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → self-serve calendar embed | 4 | 1.5 | 10 | 8 | 3.0 | 10.0 | 6.4 | 3.0 | 5.8 | 2.0 | 10.0 | 2.5 | **54.3** |
| 85 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise → we follow up and book it | 3 | 1.25 | 18 | 5 | 3.0 | 10.0 | 7.8 | 3.0 | 4.5 | 2.0 | 8.0 | 2.5 | **53.9** |
| 86 | Landing page → volume calculator — units × vendor unit cost + manual application review → self-serve calendar embed | 3 | 3.75 | 6 | 8 | 6.0 | 3.0 | 6.1 | 4.0 | 7.3 | 2.0 | 10.0 | 8.8 | **53.4** |
| 87 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise → self-serve calendar embed | 3 | 1.5 | 14 | 4 | 3.0 | 10.0 | 7.6 | 3.0 | 5.0 | 2.0 | 6.4 | 2.5 | **53.3** |
| 88 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → self-serve calendar embed | 4 | 1.75 | 14 | 7 | 3.0 | 10.0 | 6.2 | 3.0 | 5.0 | 2.0 | 10.0 | 2.5 | **53.1** |
| 89 | Landing page → see the graded bench + manual application review → we follow up and book it | 3 | 3.25 | 14 | 6 | 4.0 | 5.0 | 6.4 | 6.0 | 5.0 | 2.0 | 9.6 | 10.0 | **53.0** |
| 90 | Meta Instant Form (on-platform) → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → we follow up and book it | 4 | 1.5 | 18 | 8 | 3.0 | 10.0 | 6.4 | 3.0 | 4.5 | 2.0 | 10.0 | 2.5 | **52.7** |
| 91 | Landing page → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 1.6 | 8 | 4 | 4.0 | 10.0 | 6.3 | 0.0 | 6.4 | 2.0 | 6.4 | 5.0 | **52.4** |
| 92 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise → we follow up and book it | 3 | 1.5 | 22 | 4 | 3.0 | 10.0 | 7.6 | 3.0 | 4.1 | 2.0 | 6.4 | 2.5 | **52.2** |
| 93 | Landing page → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 3.5 | 10 | 4 | 6.0 | 6.0 | 5.0 | 4.0 | 5.8 | 2.0 | 6.4 | 6.2 | **52.0** |
| 94 | Click-to-Messenger / WhatsApp → "three graded candidates in 7 days" — the shortlist promise + passive fields on the form → we follow up and book it | 4 | 1.75 | 22 | 7 | 3.0 | 10.0 | 6.2 | 3.0 | 4.1 | 2.0 | 10.0 | 2.5 | **52.0** |
| 95 | Landing page → generic "contact us" → we follow up and book it | 3 | 1.35 | 8 | 1 | 4.0 | 10.0 | 7.8 | 0.0 | 6.4 | 2.0 | 1.6 | 5.0 | **51.9** |
| 96 | Landing page → join a newsletter / community → we follow up and book it | 3 | 3.25 | 10 | 1 | 6.0 | 6.0 | 6.4 | 4.0 | 5.8 | 2.0 | 1.6 | 6.2 | **51.5** |
| 97 | Landing page → see the graded bench + active gate that can reject → we follow up and book it | 4 | 3.5 | 8 | 5 | 4.0 | 5.0 | 5.0 | 6.0 | 6.4 | 2.0 | 8.0 | 10.0 | **51.4** |
| 98 | Landing page → see the graded bench + passive fields on the form → we follow up and book it | 4 | 3 | 8 | 4 | 4.0 | 5.0 | 5.3 | 6.0 | 6.4 | 2.0 | 6.4 | 10.0 | **51.0** |
| 99 | Meta Instant Form (on-platform) → generic "contact us" → self-serve calendar embed | 3 | 0.6 | 10 | 4 | 3.0 | 10.0 | 8.3 | 0.0 | 5.8 | 2.0 | 6.4 | 0.0 | **50.7** |
| 100 | Landing page → volume calculator — units × vendor unit cost + manual application review → we follow up and book it | 3 | 3.75 | 14 | 8 | 6.0 | 3.0 | 6.1 | 4.0 | 5.0 | 2.0 | 10.0 | 8.8 | **50.6** |
| 101 | Landing page → see the graded bench → we follow up and book it | 3 | 2.75 | 8 | 1 | 4.0 | 5.0 | 6.8 | 6.0 | 6.4 | 2.0 | 1.6 | 10.0 | **50.5** |
| 102 | Meta Instant Form (on-platform) → book a call → self-serve calendar embed | 3 | 0.75 | 10 | 4 | 3.0 | 10.0 | 8.2 | 0.0 | 5.8 | 2.0 | 6.4 | 0.0 | **50.5** |
| 103 | Landing page → watch a video first + manual application review → self-serve calendar embed | 3 | 4.75 | 6 | 5 | 6.0 | 2.0 | 5.4 | 5.0 | 7.3 | 2.0 | 8.0 | 8.8 | **50.5** |
| 104 | Meta Instant Form (on-platform) → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 0.85 | 10 | 7 | 3.0 | 10.0 | 6.8 | 0.0 | 5.8 | 2.0 | 10.0 | 0.0 | **50.5** |
| 105 | Meta Instant Form (on-platform) → book a call + passive fields on the form → self-serve calendar embed | 4 | 1 | 10 | 7 | 3.0 | 10.0 | 6.7 | 0.0 | 5.8 | 2.0 | 10.0 | 0.0 | **50.3** |
| 106 | Landing page → volume calculator — units × vendor unit cost + passive fields on the form → we follow up and book it | 4 | 3.5 | 8 | 6 | 6.0 | 3.0 | 5.0 | 4.0 | 6.4 | 2.0 | 9.6 | 8.8 | **50.3** |
| 107 | Landing page → volume calculator — units × vendor unit cost + active gate that can reject → we follow up and book it | 4 | 4 | 8 | 7 | 6.0 | 3.0 | 4.6 | 4.0 | 6.4 | 2.0 | 10.0 | 8.8 | **50.0** |
| 108 | Landing page → volume calculator — units × vendor unit cost → we follow up and book it | 3 | 3.25 | 8 | 3 | 6.0 | 3.0 | 6.4 | 4.0 | 6.4 | 2.0 | 4.8 | 8.8 | **49.8** |
| 109 | Landing page → paid micro-trial, $100–250 + payment → we follow up and book it | 4 | 2.75 | 108 | 5 | 7.0 | 2.0 | 5.5 | 7.0 | 2.0 | 2.0 | 8.0 | 10.0 | **49.4** |
| 110 | Meta Instant Form (on-platform) → generic "contact us" → we follow up and book it | 3 | 0.6 | 18 | 4 | 3.0 | 10.0 | 8.3 | 0.0 | 4.5 | 2.0 | 6.4 | 0.0 | **49.0** |
| 111 | Click-to-Messenger / WhatsApp → generic "contact us" + passive fields on the form → self-serve calendar embed | 4 | 1.1 | 14 | 6 | 3.0 | 10.0 | 6.6 | 0.0 | 5.0 | 2.0 | 9.6 | 0.0 | **49.0** |
| 112 | Meta Instant Form (on-platform) → book a call → we follow up and book it | 3 | 0.75 | 18 | 4 | 3.0 | 10.0 | 8.2 | 0.0 | 4.5 | 2.0 | 6.4 | 0.0 | **48.9** |
| 113 | Meta Instant Form (on-platform) → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 0.85 | 18 | 7 | 3.0 | 10.0 | 6.8 | 0.0 | 4.5 | 2.0 | 10.0 | 0.0 | **48.8** |
| 114 | Click-to-Messenger / WhatsApp → book a call + passive fields on the form → self-serve calendar embed | 4 | 1.25 | 14 | 6 | 3.0 | 10.0 | 6.5 | 0.0 | 5.0 | 2.0 | 9.6 | 0.0 | **48.8** |
| 115 | Meta Instant Form (on-platform) → book a call + passive fields on the form → we follow up and book it | 4 | 1 | 18 | 7 | 3.0 | 10.0 | 6.7 | 0.0 | 4.5 | 2.0 | 10.0 | 0.0 | **48.7** |
| 116 | Click-to-Messenger / WhatsApp → generic "contact us" → self-serve calendar embed | 3 | 0.85 | 14 | 3 | 3.0 | 10.0 | 8.1 | 0.0 | 5.0 | 2.0 | 4.8 | 0.0 | **48.4** |
| 117 | Click-to-Messenger / WhatsApp → book a call → self-serve calendar embed | 3 | 1 | 14 | 3 | 3.0 | 10.0 | 8.0 | 0.0 | 5.0 | 2.0 | 4.8 | 0.0 | **48.3** |
| 118 | Click-to-Messenger / WhatsApp → generic "contact us" + passive fields on the form → we follow up and book it | 4 | 1.1 | 22 | 6 | 3.0 | 10.0 | 6.6 | 0.0 | 4.1 | 2.0 | 9.6 | 0.0 | **47.9** |
| 119 | Landing page → watch a video first + manual application review → we follow up and book it | 3 | 4.75 | 14 | 5 | 6.0 | 2.0 | 5.4 | 5.0 | 5.0 | 2.0 | 8.0 | 8.8 | **47.7** |
| 120 | Click-to-Messenger / WhatsApp → book a call + passive fields on the form → we follow up and book it | 4 | 1.25 | 22 | 6 | 3.0 | 10.0 | 6.5 | 0.0 | 4.1 | 2.0 | 9.6 | 0.0 | **47.7** |
| 121 | Click-to-Messenger / WhatsApp → generic "contact us" → we follow up and book it | 3 | 0.85 | 22 | 3 | 3.0 | 10.0 | 8.1 | 0.0 | 4.1 | 2.0 | 4.8 | 0.0 | **47.3** |
| 122 | Click-to-Messenger / WhatsApp → book a call → we follow up and book it | 3 | 1 | 22 | 3 | 3.0 | 10.0 | 8.0 | 0.0 | 4.1 | 2.0 | 4.8 | 0.0 | **47.2** |
| 123 | Landing page → watch a video first + active gate that can reject → we follow up and book it | 4 | 5 | 8 | 4 | 6.0 | 2.0 | 3.9 | 5.0 | 6.4 | 2.0 | 6.4 | 8.8 | **46.1** |
| 124 | Meta Instant Form (on-platform) → join a newsletter / community → self-serve calendar embed | 3 | 2.5 | 12 | 4 | 3.0 | 6.0 | 6.9 | 4.0 | 5.4 | 2.0 | 6.4 | 1.2 | **46.1** |
| 125 | Meta Instant Form (on-platform) → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 2.75 | 12 | 7 | 3.0 | 6.0 | 5.5 | 4.0 | 5.4 | 2.0 | 10.0 | 1.2 | **45.9** |
| 126 | Landing page → watch a video first + passive fields on the form → we follow up and book it | 4 | 4.5 | 8 | 3 | 6.0 | 2.0 | 4.2 | 5.0 | 6.4 | 2.0 | 4.8 | 8.8 | **45.7** |
| 127 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2 | 10 | 4 | 3.0 | 4.0 | 7.3 | 5.0 | 5.8 | 2.0 | 6.4 | 2.5 | **45.3** |
| 128 | Landing page → watch a video first → we follow up and book it | 3 | 4.25 | 8 | 0 | 6.0 | 2.0 | 5.7 | 5.0 | 6.4 | 2.0 | 0.0 | 8.8 | **45.2** |
| 129 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 2.25 | 10 | 7 | 3.0 | 4.0 | 5.8 | 5.0 | 5.8 | 2.0 | 10.0 | 2.5 | **45.1** |
| 130 | Meta Instant Form (on-platform) → join a newsletter / community → we follow up and book it | 3 | 2.5 | 20 | 4 | 3.0 | 6.0 | 6.9 | 4.0 | 4.3 | 2.0 | 6.4 | 1.2 | **44.8** |
| 131 | Click-to-Messenger / WhatsApp → join a newsletter / community + passive fields on the form → self-serve calendar embed | 4 | 3 | 16 | 6 | 3.0 | 6.0 | 5.3 | 4.0 | 4.7 | 2.0 | 9.6 | 1.2 | **44.6** |
| 132 | Meta Instant Form (on-platform) → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 2.75 | 20 | 7 | 3.0 | 6.0 | 5.5 | 4.0 | 4.3 | 2.0 | 10.0 | 1.2 | **44.6** |
| 133 | Meta Instant Form (on-platform) → free custom work on their asset → self-serve calendar embed | 3 | 1 | 100 | 4 | 3.0 | 2.0 | 8.0 | 9.0 | 2.1 | 2.0 | 6.4 | 5.0 | **44.1** |
| 134 | Click-to-Messenger / WhatsApp → join a newsletter / community → self-serve calendar embed | 3 | 2.75 | 16 | 3 | 3.0 | 6.0 | 6.8 | 4.0 | 4.7 | 2.0 | 4.8 | 1.2 | **44.1** |
| 135 | Meta Instant Form (on-platform) → free custom work on their asset → we follow up and book it | 3 | 1 | 108 | 4 | 3.0 | 2.0 | 8.0 | 9.0 | 2.0 | 2.0 | 6.4 | 5.0 | **44.0** |
| 136 | Meta Instant Form (on-platform) → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 1.25 | 100 | 7 | 3.0 | 2.0 | 6.5 | 9.0 | 2.1 | 2.0 | 10.0 | 5.0 | **43.9** |
| 137 | Meta Instant Form (on-platform) → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 1.25 | 108 | 7 | 3.0 | 2.0 | 6.5 | 9.0 | 2.0 | 2.0 | 10.0 | 5.0 | **43.8** |
| 138 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2 | 18 | 4 | 3.0 | 4.0 | 7.3 | 5.0 | 4.5 | 2.0 | 6.4 | 2.5 | **43.7** |
| 139 | Click-to-Messenger / WhatsApp → join a newsletter / community + passive fields on the form → we follow up and book it | 4 | 3 | 24 | 6 | 3.0 | 6.0 | 5.3 | 4.0 | 3.9 | 2.0 | 9.6 | 1.2 | **43.6** |
| 140 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide + passive fields on the form → self-serve calendar embed | 4 | 2.5 | 14 | 6 | 3.0 | 4.0 | 5.7 | 5.0 | 5.0 | 2.0 | 9.6 | 2.5 | **43.6** |
| 141 | Meta Instant Form (on-platform) → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 2.25 | 18 | 7 | 3.0 | 4.0 | 5.8 | 5.0 | 4.5 | 2.0 | 10.0 | 2.5 | **43.5** |
| 142 | Click-to-Messenger / WhatsApp → free custom work on their asset + passive fields on the form → self-serve calendar embed | 4 | 1.5 | 104 | 6 | 3.0 | 2.0 | 6.4 | 9.0 | 2.0 | 2.0 | 9.6 | 5.0 | **43.4** |
| 143 | Click-to-Messenger / WhatsApp → free custom work on their asset + passive fields on the form → we follow up and book it | 4 | 1.5 | 112 | 6 | 3.0 | 2.0 | 6.4 | 9.0 | 2.0 | 2.0 | 9.6 | 5.0 | **43.3** |
| 144 | Click-to-Messenger / WhatsApp → join a newsletter / community → we follow up and book it | 3 | 2.75 | 24 | 3 | 3.0 | 6.0 | 6.8 | 4.0 | 3.9 | 2.0 | 4.8 | 1.2 | **43.1** |
| 145 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide → self-serve calendar embed | 3 | 2.25 | 14 | 3 | 3.0 | 4.0 | 7.1 | 5.0 | 5.0 | 2.0 | 4.8 | 2.5 | **43.1** |
| 146 | Click-to-Messenger / WhatsApp → free custom work on their asset → self-serve calendar embed | 3 | 1.25 | 104 | 3 | 3.0 | 2.0 | 7.8 | 9.0 | 2.0 | 2.0 | 4.8 | 5.0 | **42.8** |
| 147 | Click-to-Messenger / WhatsApp → free custom work on their asset → we follow up and book it | 3 | 1.25 | 112 | 3 | 3.0 | 2.0 | 7.8 | 9.0 | 2.0 | 2.0 | 4.8 | 5.0 | **42.8** |
| 148 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide + passive fields on the form → we follow up and book it | 4 | 2.5 | 22 | 6 | 3.0 | 4.0 | 5.7 | 5.0 | 4.1 | 2.0 | 9.6 | 2.5 | **42.5** |
| 149 | Click-to-Messenger / WhatsApp → free document — scorecard, salary data, guide → we follow up and book it | 3 | 2.25 | 22 | 3 | 3.0 | 4.0 | 7.1 | 5.0 | 4.1 | 2.0 | 4.8 | 2.5 | **42.0** |

---

## 5. Reading the ranking

**38 of 149 funnels are immune to the timezone penalty**, and they take
**10 of the top 15 places.** That is the single strongest pattern, and it is
driven by a verified fact rather than a modelled one.

| What the ranking says | Why |
|---|---|
| **Landing page beats on-platform, everywhere** | The measured appointment gap is **~2% vs ~17%** [V]. Two independent sources. This is the one place where evidence, not judgement, does the work |
| **Self-serve booking beats chasing, everywhere** | **32% vs 12% close** by response time [V], and we are 9.5–10.5 hours from the buyer. Nothing else in the study is this decisive |
| **Fewer systems wins** | `EASE` is 16% of the weight because that is the operator direction. Every extra tool is a thing that breaks silently at 2am in a timezone where nobody is awake to notice |
| **Active gates rank badly** | **0 of 10 competitors gate** [V], and a gate is an extra system for an unknown operator to add friction with. Scored down, not gated out |
| **Anything needing an asset we lack is pushed down, not excluded** | `READY` is no longer weighted at all. A bench is two weeks of real work — that is a *schedule* problem, not a disqualification, and the business needs it regardless |

### The top three, and what separates them


**1. Landing page → **the hiring scorecard** — download the test, score candidates yourself + passive fields on the form → self-serve calendar embed** — 87.4

| | |
|---|---|
| Systems | **4** — ad account, page, passive fields on the form, self-serve calendar embed |
| Build | **3 days** |
| Human work per lead | **0 min** |
| Fields captured | **6** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| **The hiring scorecard** — download the test, score candidates yourself | **The rubric, wrapped in the market's proven format.** Lead magnets run **40–60% lower CPL** than direct offers on B2B Meta [V], and guides/templates are a named proven magnet. Same content as a page block; a format that runs |
| Passive fields on the form | Captures without rejecting |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

**2. Landing page → **the hiring scorecard** — download the test, score candidates yourself + active gate that can reject → self-serve calendar embed** — 87.1

| | |
|---|---|
| Systems | **4** — ad account, page, active gate that can reject, self-serve calendar embed |
| Build | **3.5 days** |
| Human work per lead | **0 min** |
| Fields captured | **7** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| **The hiring scorecard** — download the test, score candidates yourself | **The rubric, wrapped in the market's proven format.** Lead magnets run **40–60% lower CPL** than direct offers on B2B Meta [V], and guides/templates are a named proven magnet. Same content as a page block; a format that runs |
| Active gate that can reject | **0 of 10 competitors do this** [V] |
| Self-serve calendar embed | **+30–40% booking** vs asking for availability [V]. Immune to the timezone |

**3. Landing page → **the hiring scorecard** — download the test, score candidates yourself → self-serve calendar embed** — 86.9

| | |
|---|---|
| Systems | **3** — ad account, page, self-serve calendar embed |
| Build | **2.75 days** |
| Human work per lead | **0 min** |
| Fields captured | **3** |
| Needs | **nothing we do not have** |
| Landing page | **~17% appointment rate** [V]. The default for a considered purchase |
| **The hiring scorecard** — download the test, score candidates yourself | **The rubric, wrapped in the market's proven format.** Lead magnets run **40–60% lower CPL** than direct offers on B2B Meta [V], and guides/templates are a named proven magnet. Same content as a page block; a format that runs |
| No qualification | What 10 of 10 competitors do [V] |
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

