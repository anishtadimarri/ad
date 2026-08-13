# The Teardown Generator

> *"What's the teardown generator?"*

It appears as the **#3 activity** in [`MASTERLIST.md`](MASTERLIST.md) and is referenced in four
documents, and it has never been specified. This is the spec.

---

## 1. What the teardown is

**The $500 paid step**, and the most important sentence in the model that isn't about money:

> [`MODEL-V2.md`](MODEL-V2.md) gap 2: *"Re-insert it as a **paid ad-account and creative teardown** —
> he can perform it himself, and it ***is*** the work sample."*

It does four jobs at once, which is why it scores where it does:

| Job | Why it matters |
|---|---|
| **The money gate** | Filters tyre-kickers and funds the search. [`LTGP.md`](LTGP.md) identified deposit take-up as **the single most fragile input in the whole model** |
| **The work sample** | You claim to grade creative. **A teardown of their account is you doing exactly that, on their data, before they've paid you a fee.** Nothing else you can say is as persuasive |
| **The qualifier** | You see their spend, their creative volume and their cadence. **You know whether they can afford a full-time editor before the call** |
| **The setup for the sale** | §4 — done right, the teardown's conclusion *is* the pitch |

Priced at **$500, credited in full against the placement fee** ([`OFFER.md`](OFFER.md) §230). So the
buyer isn't spending $500 — they're pre-paying $500 of $6,600 and getting a deliverable if they walk
away. **That's a materially smaller decision than "wire a stranger a refundable deposit,"** which is
the whole reason §9.1 made the change.

---

## 2. What the *generator* is

The teardown is your judgement. **The generator is the production system around it**, so the
judgement is the only part that costs you time.

Without it, each teardown is a bespoke 3–5 hour job — fine for client one, fatal by client ten,
because the model needs this to run alongside everything else you're doing alone.

```
  INPUT   their Meta ad export  ·  or public Ad Library data pre-sale
          their landing page    ·  their current creative

  AUTO    ── pull every ad, live and dead, with run dates
          ── hook rate, hold rate, CTR, CPM, CPA, frequency, per ad
          ── rank creative by 3-second and 15-second retention
          ── flag fatigue: frequency climbing + CPM drifting + CTR decaying
          ── count distinct angles, and how long each has been running
          ── creative refresh rate: new cuts shipped per month
          ── landing-page speed and mobile check

  YOU     ── the three things to fix, in order, and why
          ── which of them is a creative-volume problem      ← the sale
          ── one honest thing they're doing well

  OUTPUT  same document, same sections, every time
```

**Roughly 30–45 minutes of your attention instead of 3–5 hours**, and the analysis is identical
every time — which is the same consistency argument that makes the grading rubric work.

---

## 3. Why it scores third

Behind only the intent-seed audience and the prospect-list pipeline, and ahead of keeping the model
live:

- **It's revenue at the top of the funnel** — the only paid step before placement
- **It's reusable forever** — built once, run on every prospect
- **It's the proof that makes *premium* credible** to a buyer with no reason to trust you
- **It's the one deliverable you're already world-class at.** [`LAUNCH.md`](LAUNCH.md)'s
  `FOUNDERGRADE` — *can the operator personally judge this with no team* — is the reason video was
  chosen as the wedge. The teardown is that same skill, pointed at the buyer instead of the candidate

---

## 4. The design rule that decides whether it sells

This is the part worth getting right, and it's not obvious.

> **The teardown must conclude in a *volume* problem — because a volume problem is solved by a
> person, and nothing else is.**

| If the teardown concludes… | What the buyer does |
|---|---|
| *"Your CPM is high"* | Adjusts targeting. **Buys nothing** |
| *"Your landing page is slow"* | Fixes the page. **Buys nothing** |
| *"Your hooks are weak"* | Tries harder. Maybe hires a freelancer for one batch |
| **"Your best ad is 6 weeks old and fatiguing, you're shipping 3 cuts a month, and this account needs 12–16 to stay fed — that's a full-time editor, not a freelancer"** | **Buys a placement** |

The last one works because it reframes the purchase. Not *"is this editor good?"* — an unanswerable
question about a stranger in another country — but *"can I sustain 16 cuts a month without one?"*,
which they can answer themselves, and the answer is no.

It also sets up the **vendor-invoice comparator** that [`MODEL-V2.md`](MODEL-V2.md) §8 identified as
the largest true claim in the study: at that cadence a studio bills **$5,000–16,500/month**. A
placed editor at a one-time 30% fee is 4–13× cheaper for the same output. **That comparison only
lands if the teardown has already established the cadence they need.**

---

## 5. Build notes

| | |
|---|---|
| **When** | Week 2 — [`MASTERLIST.md`](MASTERLIST.md) §2. Before first spend, because it's what the spend converts *into* |
| **Surface** | `Code` for the generator, `Chat` for the judgement calls inside it |
| **Pre-sale version** | Uses **Meta Ad Library data only** — public, no account access needed. Lets you run one unprompted for a cold prospect, which is the strongest possible outbound opener |
| **Post-payment version** | Uses their actual export. Deeper, and the access request is itself a commitment step |
| **Access** | Partner access via Business Manager, never shared logins — [`ACTIVITIES.md`](ACTIVITIES.md) flags client ad-account access as a Tier 0 blocker |
| **Reuse** | Every teardown you run is also **a data point for your own creative benchmarks** — after twenty, you know what normal looks like in this category better than your prospects do |

---

## 6. What is still undecided

- **Price.** $500 is carried from [`OFFER.md`](OFFER.md) §9.1 and credited against the fee. Whether
  $500 is right for the video ICP rather than the finance ICP has **not been tested** — take-up is
  modelled at **24%** and that number is marked `[?]` in [`funnel.py`](scoring/funnel.py)
- **Whether it's delivered live or as a document.** Live on a call converts better; a document
  scales. Probably both: document, then walk through it
- **Turnaround promise.** 48 hours is a stronger offer than "within a week" and the generator is
  what makes it safe to promise
