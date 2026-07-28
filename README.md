# Business Repository

## → [`MASTER.md`](MASTER.md)

Everything lives in one document. Start there.

---

## What this is

A working file for an **offshore talent placement business**: recruiting full-time remote
professionals from India/South Africa/Philippines into US small and mid-market companies, on a
one-time placement fee of ~35% of first-year salary.

**Target:** $5M revenue in 3–5 years (~60 placements/month).
**Status:** pre-launch, nothing validated, no customer met.

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
| **§9** | The recommended model spec — offer, deposit, protection layer, retention architecture |
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

## The four numbers to remember

| | |
|---|---|
| Gross profit per placement | **$5,759** (82% margin) |
| 30-day LTGP:CAC, Meta base case | **2.6:1** — clears the 1.5:1 constraint |
| CAC at which the model breaks | **$3,839** |
| The number that decides everything | **Fill rate** — below 40% the model stops working |

---

## The two tests that come before anything else

Together: **under $2,000 and about ten days.** They resolve both sides of the marketplace, and
nothing downstream is modellable until they're done.

1. **Demand** — run the "$20,000/yr remote accountant, placed in two weeks" hook on Meta. ~$1,500.
   Measures cost per lead against the $100 assumption.
2. **Supply** — post one role to Indian candidate channels. ~$300. Counts qualified applicants
   in 72 hours.

---

## Scoring model

| File | What it is |
|---|---|
| [`scoring/model.py`](scoring/model.py) | 179 roles × 14 weighted dimensions + knockout gates. Editable weights; re-run to regenerate |
| [`scoring/RANKING.md`](scoring/RANKING.md) | Generated output — full ranking, top 25, all 49 knockouts, cluster averages |

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
