# Business Repository

## Start here

### → [`MAP.md`](MAP.md) — the decision: 2 verticals × 5 roles

---

## Nine documents

| | |
|---|---|
| **[`MAP.md`](MAP.md)** | **THE DECISION.** E-comm + marketing agencies × 5 roles. Two ads, one legible promise, five sellable seats. Supersedes the vertical/role picks elsewhere |
| **[`OFFER.md`](OFFER.md)** | **The buildable thing.** One skill, both ICPs, priced, with the retention architecture and the economics stress-tested against 6-month attrition |
| **[`MASTER.md`](MASTER.md)** | The analysis behind it — market data, 179-role screen, competitor teardown, decision history, what's unvalidated |
| **[`BEACHHEAD.md`](BEACHHEAD.md)** | **Three verticals, one bench** — e-comm + marketing agencies + SaaS, ranked on measured **switch cost**. 6 of 10 roles are drop-in. Launch role is AR & Collections, not Ledger & Close |
| **[`TARGETING.md`](TARGETING.md)** | **How to reach them mid-search** — job postings as a dated intent signal, scraped into a Meta custom audience. Reverses the Meta-targetability gate |
| **[`PATTERN.md`](PATTERN.md)** | **The supply-side screen** — which occupations the US stopped producing, where the work is digital and somebody already proved it transfers. Insurance is a worse shortage than accounting |
| **[`COMPETITOR-DATA.md`](COMPETITOR-DATA.md)** | **What Somewhere and Oceans actually sell** — 60+ published roles with rates, bookkeeper priced by country, and the finding that **neither of them sources India** |
| **[`NAME.md`](NAME.md)** | **The name.** Pick: **All Aboard Talent** (`allaboardtalent.com`) — All Hands with the defects removed: same `All ___` warmth, but it means *joining a team* rather than an emergency, and "aboard" is literally the hiring word. ~1,680 domains checked against Verisign RDAP; `.talent` confirmed non-existent against IANA |
| **[`SCALE.md`](SCALE.md)** | **The path to \$20M on two products** — placement + EOR, 88 people, 32–36% EBITDA. Why the managed-service \$100M path was rejected on operational intensity |

---

## What this is

A working file for an **offshore talent placement business**: recruiting full-time remote
professionals from India/South Africa/Philippines into US small and mid-market companies, on a
one-time placement fee of ~35% of first-year salary.

**Wedge:** e-commerce accounting/bookkeeping placed into US Shopify and Amazon brands, then the
same portable roles into marketing agencies and SaaS ([`BEACHHEAD.md`](BEACHHEAD.md)) —
~66,000 businesses, every one of which already employs remote staff.
**Long-term:** $20M on two products — placement fee + EOR, ~88 people, 32–36% EBITDA
([`SCALE.md`](SCALE.md)). **Status:** pre-launch, nothing validated, no customer met.

---

## Document map

| Section | What's in it |
|---|---|
| **§0** | Evidence tagging — `[V]` verified, `[E]` estimate, `[C]` company claim, `[?]` assumption |
| **§1** | The business in one page |
| **§2** | **Decision history — 60+ ideas killed, and by what evidence.** Includes errors made and corrected |
| **§3** | The filter framework — hard constraints, market filters, the seven role filters |
| **§4** | Market structure — size, salaries both sides, attrition by function and country, wage inflation |
| **§5** | Competitor teardown — Somewhere, Oceans, TOA, Entigrity, Wing, MyOutDesk, ReSource Pro |
| **§6** | Five business model variants compared; why recruit-and-handoff wins |
| **§7** | **Role selection — 179 roles scored on a 14-dimension weighted model, with knockout gates.** Methodology, results, what it overturned, and the model's own limits |
| **§8** | Geography selection |
| **§9** | The recommended model spec — offer, deposit, protection layer, retention architecture. **§9.6 retracts the "academy is the moat" claim** and replaces it with assessment + outcome data |
| **§10** | Unit economics — per-placement P&L, CAC scenarios, 30-day and lifetime LTGP:CAC |
| **§11** | Acquisition — the honest position on Meta, channel portfolio |
| **§12** | Operating model — team skills by %, fill rate, headcount, known headaches |
| **§13** | Path to $5M + P&L |
| **§14** | Valuation and exit |
| **§15** | Risk register |
| **§16** | Legal and compliance |
| **§17** | **What is actually unvalidated** — ranked, with cost to test |
| **§18** | Open decisions |
| **App. A** | Full reference data corpus |
| **App. B** | Frameworks used |
| **App. C** | Archived work |

---

## The numbers to remember

At $20,000 placed salary, 30% fee, 9-month worker stay, recruitment costed at one month of salary:

| | |
|---|---|
| 30-day gross profit per acquired client | **$4,148** (55% margin) |
| EOR gross profit | **$477 per employee per month**, assumed over **9 months** |
| Lifetime gross profit | **$11,074** — of which **37% is the recurring EOR layer** |
| **Blended CAC** — funnel-derived, spend-weighted | **$976** |
| **30-day LTGP:CAC** | **4.25:1** |
| **Lifetime LTGP:CAC** | **11.35:1** |
| The one fragile input | **Deposit rate.** 18% → 8% takes 30-day to **1.89:1** |
| The biggest lever left | **EOR months.** 9 → 30 adds **$9,022** per client — 18x what halving CAC adds |
| The number that decides the launch | **Fill rate** — below 40% it stops working |
| The number that decides the ceiling | **EOR attach** — it is 56% of revenue at \$20M, so make it the default, not the upsell |

Gross profit from [`scoring/offer_model.py`](scoring/offer_model.py); CAC from
[`scoring/funnel.py`](scoring/funnel.py); joined in [`scoring/LTGP.md`](scoring/LTGP.md).
**The offer model's own CAC is superseded** — it used a flat $75 CPL and an assumed funnel, and
came out roughly 2x too kind.

---

## The two tests that come before anything else

Together: **under $2,000 and about ten days.** They resolve both sides of the marketplace, and
nothing downstream is modellable until they're done.

0. **Match rate** — enrich 2,000 companies that posted a remote bookkeeper role, upload as a Meta
   Custom Audience, read the matched size. **Same-day answer, and everything in
   [`TARGETING.md`](TARGETING.md) depends on it.**
1. **Demand** — run the "still trying to fill that bookkeeper role?" hook at the intent seed.
   ~$1,500. Measures CPL against the $75 assumption.
2. **Supply** — post one role to Indian candidate channels. ~$300. Counts qualified applicants
   in 72 hours.

---

## Scoring model

| File | What it is |
|---|---|
| [`scoring/model.py`](scoring/model.py) | 179 roles × 14 weighted dimensions + knockout gates. Editable weights; re-run to regenerate |
| [`scoring/RANKING.md`](scoring/RANKING.md) | Generated output — full ranking, top 25, all 49 knockouts, cluster averages |
| [`scoring/offer_model.py`](scoring/offer_model.py) | Offer configurations — fee stack, funnel, recruitment cost, EOR line. Toggle `COST_MODE` between itemised and one-month-of-salary |
| [`scoring/OFFER-MODEL.md`](scoring/OFFER-MODEL.md) | Generated output — market pricing, 13 configurations, funnel optimisation, sensitivities |
| [`scoring/vertical_model.py`](scoring/vertical_model.py) | **104 role × vertical pairs across 25 verticals**, 12 dimensions. The unit that matters — "e-comm bookkeeper" beat "bookkeeper" because of the vertical |
| [`scoring/VERTICALS.md`](scoring/VERTICALS.md) | Generated output — top 20, the 10 next-best verticals, vertical averages, gated-out list, anchoring test |
| [`scoring/first_principles.py`](scoring/first_principles.py) | **The clean rebuild.** Verticals and skills scored on *separate* criteria sets, plus an interaction term, then the 3×3 grid optimised on its worst cell |
| [`scoring/funnel.py`](scoring/funnel.py) | **Step-by-step Meta funnel** — impression → CAC, by audience layer and lead-capture flow, with the break-points |
| [`scoring/FUNNEL.md`](scoring/FUNNEL.md) | Generated output — the nine steps, form-fill vs calendar booking, what \$5,000 can and cannot measure |
| [`scoring/ltgp.py`](scoring/ltgp.py) | **Joins the two models** — gross profit from the offer model, CAC from the funnel model, on a \$20k job. Discards the offer model's internal CAC |
| [`scoring/LTGP.md`](scoring/LTGP.md) | Generated output — **4.25:1 on 30 days, 11.35:1 lifetime** at a \$976 blended CAC, the EOR line per month, and the 6–30 month EOR sensitivity |
| [`scoring/FIRST-PRINCIPLES.md`](scoring/FIRST-PRINCIPLES.md) | Generated output — vertical criteria, skill criteria, interaction criteria, the map, the answer |

```
python3 scoring/model.py > scoring/RANKING.md
```

**Top 5:** Recruiter (79.0) · Bookkeeper (77.8) · Marketing ops (76.8) · Staff accountant (76.4) ·
Email/lifecycle (76.4)

**Read §7.10 before trusting the order** — the top-25 spread is 8.4 points, so the model
separates quartiles reliably and adjacent ranks unreliably.

---

## Archive

[`archive/dental-lead-to-chair/`](archive/dental-lead-to-chair/) — a fully specified productized
service for US full-arch dental implant practices. Superseded, not disproven; see MASTER.md
Appendix C.
