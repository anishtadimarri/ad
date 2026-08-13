# Choosing the Framer Template

> Criteria first, shortlist second — because **the two criteria that matter most cannot be judged
> from a marketplace listing**, and pretending otherwise would produce a confident wrong answer.

---

## 1. First: you are buying a template for the wrong page

The instinct is to find a template that solves the landing page. It does not, and it should not.

| Page | What it is | Template? |
|---|---|---|
| **`/agencies`, `/ecommerce`** | **The ad destinations. Where 100% of paid traffic lands.** Six blocks: promise, proof, mechanism, price, guarantee, one ask | **No. Build from blank.** A landing page is six blocks and no template does six blocks better than you do with the copy in front of you |
| `/`, `/proof`, `/pricing`, `/guarantee` | The brand and credibility pages. Read after the ad, or by a referral, or by someone checking you are real | **Yes.** This is what the template is for — structure and polish you would otherwise spend days on |

> **So the template's job is credibility, not conversion.** That changes what you are shopping for,
> and it means a **free** template may be entirely sufficient — see §5.

---

## 2. The criteria, weighted for this funnel

Not generic web-design advice. These weights come from **your** traffic: overwhelmingly mobile,
cold, mid-scroll, and metered by an 85% LP-view rate.

| Criterion | Wt | What it means | Can I check it? |
|---|---|---|---|
| **MOBILEHERO** | 22 | **Promise + CTA above the fold on a 390×844 phone, with no scroll.** Meta traffic is overwhelmingly mobile and arrives mid-scroll. Most templates are designed desktop-first with a tall hero image that pushes the CTA below the fold on a phone — **this is the single most common failure and it is invisible on a laptop** | `[?]` from listings |
| **SPEED** | 18 | Page weight and animation load on 4G. [`funnel.py`](scoring/funnel.py) carries an **85% LP-view rate** — that is a speed number, and every point lost is lost at the very top of the funnel. **Framer templates love scroll animation and video backgrounds** | `[?]` from listings |
| **SECTIONS** | 16 | Does it ship the sections this offer needs, in this order — hero → proof → how it works → pricing → guarantee → CTA? **Most agency templates are portfolio-shaped** (case-study grid, big imagery), which is a different page | assessable |
| **CTAREPEAT** | 12 | CTA in the hero, mid-page, and sticky or footer. **Mobile users do not scroll back up** | assessable |
| **PROOFSLOT** | 10 | Somewhere to put a **before/after video comparison with retention numbers** — the `/proof` page is the most important on the site | assessable |
| **CREDIBLE** | 10 | Reads as a firm a $6k–$20k buyer trusts. **Not startup-gradient, not creative-portfolio.** You have no track record, so the site carries more trust load than usual | assessable |
| **VARIANT** | 7 | How easily it duplicates into `/agencies` and `/ecommerce` — component-driven with global styles, or hand-built pages | assessable |
| **COST** | 5 | One-time. Real, but small against the decision | verifiable |

> **The top two weights — 40 points of 100 — are the two I cannot verify.** `MOBILEHERO` and `SPEED`
> are properties of the live preview on a phone on mobile data. Everything below is therefore a
> **shortlist to test**, not a ranking to trust.

---

## 3. The shortlist, scored on what *is* assessable

Scored on the 6 assessable criteria only — 60 of 100 points. **`MOBILEHERO` and `SPEED` are
deliberately absent**, which is why the top score here is not a recommendation.

| # | Template | Price | Register | Sect | CTA | Proof | Cred | Var | Cost | Score | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Conversion** | ~$79 `[?]` | conversion / lead-gen | 5 | 5 | 3 | 4 | 4 | 3 | **84** | **Built for lead generation rather than showcase**, which is the rarest and most valuable property in this list. One of the longest-running templates on the Framer marketplace. `PROOFSLOT`=3 because a conversion template optimises for form-fills, not for a video comparison — you would add that block |
| 2 | **Cubicles** | ~$59 `[?]` | corporate / consultancy | 4 | 3 | 3 | 5 | 3 | 4 | **74** | **Corporate B2B register — the right register.** Structured for services rather than showcase. Weaker on repeated CTA, which is a fixable edit |
| 3 | **Nakula / Fabrica / Lyniq** | $69–129 `[?]` | premium agency | 4 | 3 | 4 | 5 | 3 | 2 | **74** | The 'looks expensive' tier, aimed at high-ticket B2B. **`CREDIBLE`=5 is real and matters here.** But premium agency templates are usually the heaviest — big imagery, lots of motion — so `SPEED` is the risk and it is unverified |
| 4 | **Nebula** | $49 `[?]` | lead-gen, dark + gradient | 4 | 4 | 3 | 3 | 4 | 4 | **73** | Explicitly lead-gen focused and cheap. **`CREDIBLE`=3 is the concern** — dark gradient reads SaaS-startup, and your buyer is a 40-year-old agency owner deciding whether an unknown Indian firm is real |
| 5 | **Greenleaf** | **free** `[?]` | consulting | 4 | 3 | 2 | 4 | 3 | 5 | **69** | Free, clean, consulting-shaped, with a services section and a clear contact-to-consultation flow. **The cheapest way to test whether a template is even the constraint** — and if the answer is no, you have spent nothing |
| 6 | **Kajo** | **free** `[?]` | general | 3 | 3 | 2 | 3 | 3 | 5 | **60** | Free. Fewer sections, less structure |
| 7 | **Halo** | $69 `[?]` | general/startup | 3 | 3 | 3 | 3 | 3 | 3 | **60** | No strong reason to choose it over the lead-gen options above |

*Names and prices are from marketplace aggregators and are marked `[?]` — **verify both on Framer
before buying**, since listings and pricing churn.*

---

## 4. The 20-minute test that actually decides it

Run this on **three** candidates. It is worth more than any ranking I can give you, because it
measures the two things that carry 40% of the weight.

| # | Do this | Tests | Why |
|---|---|---|---|
| 1 | Open the live preview **on your phone, on mobile data — not wifi** | `SPEED` | The whole point. A laptop on fibre tells you nothing about the buyer's experience |
| 2 | **Do not scroll. Screenshot.** Is the promise *and* a tappable CTA both visible? | `MOBILEHERO` | **This one test eliminates most templates.** If the CTA is below the fold on a phone, everything else about the template is irrelevant |
| 3 | Count the seconds until the hero text is readable | `SPEED` | Anything past ~3 seconds on 4G is costing you LP views before anyone reads a word |
| 4 | Scroll once, fast, the way a person actually does | `SECTIONS` | Does the order make sense without reading? Promise → proof → mechanism → price → ask |
| 5 | Count CTAs on the way down | `CTAREPEAT` | Fewer than three on a long page means people who are convinced at 60% have nothing to tap |
| 6 | Look for a block that could hold **two videos side by side with numbers under them** | `PROOFSLOT` | That is the recut-vs-original comparison. If nothing fits, you are building it |
| 7 | Ask: would I give this company $6,600? | `CREDIBLE` | Answer as your buyer — a US agency owner who has never heard of you |
| 8 | Check the template's own page count and whether sections are components | `VARIANT` | Components mean `/agencies` and `/ecommerce` are a duplicate-and-edit. Hand-built pages mean two of everything, forever |

**Step 2 is the whole test.** Screenshot the top of the page on your phone without scrolling. If the
promise and a tappable CTA are not both in that screenshot, the template fails — and **it will look
perfect on your laptop**, which is how this mistake gets made.

---

## 5. What I would actually do

| | |
|---|---|
| **Start with a free one** | **Greenleaf** (consulting register, services section, clear contact-to-consultation flow) costs nothing and answers the real question: *is the template the constraint, or is the copy?* It is almost always the copy |
| **If you pay, pay for the lead-gen register** | **Conversion** is the only one on the list built for lead generation rather than showcase, and that is the rarest property here. **Cubicles** if you want the corporate-B2B look instead |
| **Avoid the premium agency tier for now** | Nakula, Fabrica, Lyniq look expensive and are usually the heaviest — big imagery, heavy motion. **You are optimising for a phone on 4G, not for a design award** |
| **Avoid dark-gradient startup templates** | Nebula is cheap and lead-gen shaped, but your buyer is an agency owner deciding whether an unknown Indian firm is real. **Dark gradient reads *startup*; you want *firm*** |
| **Budget the saving, not the spend** | The gap between free and $79 is one hour of your time. **The gap between a template that fails the phone test and one that passes is every impression you ever buy** |

**And strip whatever you buy.** Templates ship with animation, parallax and section counts designed to
demo well in a marketplace. Delete aggressively: every animation you remove buys back LP-view rate,
and the 85% in the funnel is an assumption you can move in the right direction for free.
