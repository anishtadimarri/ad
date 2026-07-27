# Lead-to-Chair Revenue System

A productized service for US full-arch dental implant practices. We own the funnel from
lead arrival to a qualified, financing pre-approved patient sitting in the consult chair —
and the follow-up on everyone who doesn't close.

**We do not touch their marketing. We do not coach their team.**

---

## The model at a glance

```
META AD  ──►  LEAK CALCULATOR (free)  ──►  $297 LEAK AUDIT (SLO)  ──►  REVIEW CALL
                                                                            │
                                                                            ▼
                                                    MAIN OFFER: $9,500 + $2,500/mo + $300/consult
                                                                            │
                                          ┌─────────────────────────────────┼──────────────────┐
                                          ▼                                 ▼                  ▼
                                   ANNUAL PREPAY                    CONSULT VOLUME       DOWNSELLS
                                   12-for-10                        $6,000/mo            $2,500–3,500
```

## Why this offer exists

A full-arch practice running 25 consults/month leaks money in four places. Three of them
are automation problems, not people problems:

| Leak | Mechanism | Monthly value at $35k/case |
|---|---|---|
| 35% no-show rate | Sequences + pre-frame video | **5 more consults sat → $49,000** |
| Single-lender financing declines | Multi-lender waterfall routing | **2 cases → $70,000** |
| Abandoned "think about it" pile | 6-month automated nurture | **1.3 cases → $45,500** |
| ~~Same-day acceptance rate~~ | ~~Coaching~~ | *Deliberately excluded* |

**~$164,000/month of recovered revenue. ~$98,000 of gross profit. Our fee is 4% of that.**

The fourth lever — coaching the treatment coordinator to close better — is deliberately out
of scope. It requires sales-coaching skill and clinical context, it can't be measured cleanly,
and it turns out to be the least valuable of the four.

## Headline economics

| | |
|---|---|
| 30-day collected per client | **$12,750** |
| Gross margin | 80% |
| 30-day gross profit | **$10,200** |
| CAC (after SLO offset) | ~$1,428 |
| **30-day LTGP:CAC** | **7.1:1** |
| Clients needed for $20k/mo | **1.6** |

Full model in [`08-FINANCIALS.md`](08-FINANCIALS.md).

---

## Documents

| File | What's in it |
|---|---|
| [`01-ICP-AND-OFFER.md`](01-ICP-AND-OFFER.md) | Who we sell to, disqualifiers, main offer, pricing, guarantee, contract terms |
| [`02-META-ADS.md`](02-META-ADS.md) | Targeting, 6 ad variants with full copy, creative briefs, budget, test plan |
| [`03-SLO.md`](03-SLO.md) | The $297 Leak Audit — ghost call script, 12-point scorecard, delivery SOP |
| [`04-PRODUCTS.md`](04-PRODUCTS.md) | All three modules specced to deliverable detail, with sequence copy |
| [`05-UPSELL-DOWNSELL.md`](05-UPSELL-DOWNSELL.md) | The full ladder, triggers, and pricing |
| [`06-LANDING-PAGES.md`](06-LANDING-PAGES.md) | Copy decks for calculator page, SLO page, main sales page |
| [`07-SALES-CALL.md`](07-SALES-CALL.md) | 30-minute review call script + objection library |
| [`08-FINANCIALS.md`](08-FINANCIALS.md) | Unit economics, 12-month model, sensitivities |
| [`landing-pages/slo.html`](landing-pages/slo.html) | Deployable SLO landing page |

---

## Before you sell anything — three things to verify

These are the assumptions the whole model rests on. All three are cheap to check and none
have been validated yet.

1. **PMS/CRM integration reality.** Call 3 full-arch practices. Ask: what CRM, what phone
   system, who has API access. If everything lives inside Dentrix with no external access,
   delivery gets expensive. Mitigation is to work at the lead/CRM layer only — never touch
   the practice management system.
2. **Cost per booked call.** $400 of Meta spend answers this. The model assumes ~$188 per
   booked call. Above $600 and the economics change materially.
3. **Call recording consent.** 12 states require all-party consent (CA, FL, PA, IL, MD, MA,
   MI, MT, NV, NH, OR, WA). Ghost calls in those states deliver a verbatim transcript, not
   audio. Attorney review before call one.

## Compliance posture

- **HIPAA:** we operate at the lead/CRM layer, not the clinical record. Data lives in the
  client's systems. We need a BAA and access controls — not our own HIPAA infrastructure.
- **Offshore access:** the delivery team is India-based. Any seat with access to patient
  contact data must be named in the BAA and disclosed to the client. Aggregate reporting
  and build work require no PHI access at all.
- **Follow-up targets patients who physically attended a consultation** — an established
  treatment relationship. This is a materially safer TCPA position than reactivating cold
  web leads.
