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

## 2. The 3-months-free bundle reverses "start with a free one"

**Paid Framer templates commonly ship a code for 3 months of Framer Pro.** That is not a marketing
footnote — it is worth more than most of the templates cost, and it inverts the cost comparison
I gave last time.

| Path | Template | Framer Pro, months 1–3 | **Total, first 3 months** |
|---|---|---|---|
| **Free template** (Greenleaf, Kajo) | $0 | **$90** — you pay from day one | **$90** |
| **Paid template with the bundle** (~$79) | $79 | **$0** | **$79 + the template** |

> **The paid template is cheaper *and* you get the template.** A free template is only the cheapest
> option if you ignore the subscription it does not cover — which is exactly what I did last turn.

Three caveats, and the first one matters:

| | |
|---|---|
| **The bundle is creator-dependent, not universal** | It is common, not guaranteed. **Check the specific listing for the 3-months-Pro code before buying** — the whole argument above collapses without it |
| It is 3 months of the **annual** Pro plan | Which means it likely presumes annual billing afterwards. Read what you are committing to at month four |
| Prices here are `[?]` from aggregators | Verify on Framer. Listings churn |

---

## 3. The criteria, weighted for this funnel

Not generic web-design advice. These weights come from **your** traffic: overwhelmingly mobile,
cold, mid-scroll, and metered by an 85% LP-view rate.

| Criterion | Wt | What it means | Can I check it? |
|---|---|---|---|
| **MOBILEHERO** | 20 | **Promise + CTA above the fold on a 390×844 phone, no scroll.** Meta traffic is overwhelmingly mobile and arrives mid-scroll. Most templates are desktop-first with a tall hero that pushes the CTA under the fold on a phone — **the most common failure, and invisible on a laptop** | `[?]` needs the phone test |
| **SPEED** | 15 | Weight and animation on 4G. [`funnel.py`](scoring/funnel.py) carries an **85% LP-view rate** — a speed number, lost at the very top of the funnel | `[?]` needs the phone test |
| **COMPLETE50** | 15 | **New.** *"Everything for the first 50 converts."* Does it ship every surface you need before a rebuild — **CMS for accumulating `/proof` entries and case studies**, pricing, testimonials, forms, booking embed, thank-you page, legal pages? **A template you outgrow at client ten costs you a rebuild in the busiest month you will have** | assessable |
| **STABLE** | 13 | **New.** *"Stability and clean."* Maintained, lifetime updates, and **structurally clean — components and global styles rather than hand-placed pages.** Clean structure is also what makes `/agencies` and `/ecommerce` a duplicate-and-edit rather than two of everything forever | partly — longevity is the best available proxy |
| **SECTIONS** | 12 | Ships the sections this offer needs, in order: hero → proof → how it works → pricing → guarantee → CTA. **Most agency templates are portfolio-shaped**, which is a different page | assessable |
| **CTAREPEAT** | 8 | CTA in hero, mid-page, and sticky or footer. **Mobile users do not scroll back up** | assessable |
| **PROOFSLOT** | 7 | A block that holds **two videos side by side with retention numbers under them** — the recut-vs-original comparison | assessable |
| **CREDIBLE** | 6 | Reads as a firm a $6k–$20k buyer trusts. Not startup-gradient, not creative-portfolio | assessable |
| **NETCOST** | 4 | **Changed.** Cost **net of the bundled 3 months of Framer Pro** that paid templates commonly include — see §2. A free template has no bundle, so it is not the cheapest option | verifiable on the listing |

> **The top two weights — 40 points of 100 — are the two I cannot verify.** `MOBILEHERO` and `SPEED`
> are properties of the live preview on a phone on mobile data. Everything below is therefore a
> **shortlist to test**, not a ranking to trust.

---

## 4. The shortlist, scored on what *is* assessable

Scored on the 7 assessable criteria only — 65 of 100 points. **`MOBILEHERO` and `SPEED` are
deliberately absent**, which is why the top score here is not a recommendation.

| # | Template | Price | Register | C50 | Stab | Sect | CTA | Proof | Cred | Net$ | Score | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Conversion** | ~$79 `[?]` | conversion / lead-gen | 4 | 5 | 5 | 5 | 3 | 4 | 5 | **89** | **Built for lead generation rather than showcase** — the rarest property here. **`STABLE`=5 on the strongest evidence available**: one of the longest-running templates on the marketplace with 100k+ views, which is the only real proxy for *it still works and is still maintained* |
| 2 | **Funnelz** | paid `[?]` | lead-gen agency | 5 | 3 | 5 | 4 | 5 | 3 | 5 | **86** | **Verified live.** By Ramish Aziz. Ships hero+CTA, social proof, **case studies**, services, **3-tier pricing**, team bios, **blog/resources**, booking in the nav — **`COMPLETE50`=5, the most complete section set on this list.** Two mismatches, both edits not rebuilds: **3-tier pricing when you have one price**, and **team bios when you are one person** (repurpose as the founder story — useful when you have no track record). **`CREDIBLE`=3 is the real risk**: *"Fuelling growth with every click"* is funnel-agency register, and **your buyer *is* an agency owner who will recognise it instantly** |
| 3 | **Nakula / Fabrica / Lyniq** | $69–129 `[?]` | premium agency | 4 | 4 | 4 | 3 | 4 | 5 | 4 | **79** | The 'looks expensive' tier for high-ticket B2B. `CREDIBLE`=5 is real. **But premium agency templates are usually the heaviest** — big imagery, heavy motion — so `SPEED` is the risk and it is exactly what I cannot check |
| 4 | **Cubicles** | ~$59 `[?]` | corporate / consultancy | 4 | 4 | 4 | 3 | 3 | 5 | 5 | **78** | **Corporate B2B — the right register**, and the opposite risk to Funnelz. Structured for services rather than showcase. Weaker repeated CTA, which is a fixable edit |
| 5 | **Nebula** | $49 `[?]` | lead-gen, dark + gradient | 3 | 3 | 4 | 4 | 3 | 3 | 5 | **69** | Lead-gen shaped and cheap. **`CREDIBLE`=3**: dark gradient reads SaaS-startup, and your buyer is deciding whether an unknown Indian firm is real |
| 6 | **Greenleaf** | **free** | consulting | 3 | 4 | 4 | 3 | 2 | 4 | 3 | **67** | Clean consulting register, services section, clear contact-to-consultation flow. **`NETCOST`=3, not 5 — free templates carry no Pro bundle**, so you pay $30/mo from day one and it is not actually the cheapest path (§2). Built for ESG consultants, so expect green styling — a skin change, not structural |
| 7 | **Halo** | $69 `[?]` | general / startup | 3 | 3 | 3 | 3 | 3 | 3 | 4 | **61** | No strong reason over the lead-gen options above |
| 8 | **Kajo** | **free** | general | 2 | 3 | 3 | 3 | 2 | 3 | 3 | **53** | Fewer sections, less structure, no bundle |

*Names and prices are from marketplace aggregators and are marked `[?]` — **verify both on Framer
before buying**, since listings and pricing churn.*

---

## 5. The 20-minute test that actually decides it

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

## 6. What I would actually do

**This reverses last turn's answer, and the bundle is why.**

| | |
|---|---|
| **Buy a paid template with the 3-month Pro code** | It is cheaper than free over the first quarter (§2), and the two strongest candidates are both paid |
| **First choice: Conversion** | The only one built for **lead generation rather than showcase**, and `STABLE`=5 on the best evidence available — 100k+ marketplace views over years is the only real proxy for *still maintained, still works*. **Stability was one of your criteria and this is the one template with actual evidence for it** |
| **Close second: Funnelz** | **The most complete section set on the list** — case studies, blog, pricing, testimonials, booking. `COMPLETE50`=5, so nothing needs rebuilding as proof accumulates. **The risk is register**: your buyer is an agency owner who will recognise funnel-agency styling on sight |
| **Cubicles if Funnelz feels too *agency*** | Corporate-B2B register, the opposite risk profile, and cheaper |
| **Still avoid the premium tier** | Nakula, Fabrica, Lyniq look expensive and are usually the heaviest. **You are optimising for a phone on 4G** |
| **Greenleaf drops to a fallback** | Still fine, still clean — but `NETCOST`=3 because there is no bundle, and `PROOFSLOT`=2 because a consulting template has nowhere natural for a two-video comparison |

### On "everything for the first 50 converts"

That criterion is doing real work, and it is why **Funnelz jumped past Cubicles.** The surfaces you
will need before client fifty, in the order they become urgent:

| By client | You need | Which means the template must ship |
|---|---|---|
| **1** | Two ad destinations, a paid teardown page, booking, thank-you | Forms, an embed slot, a payment button — **or you build these anyway** |
| **3–5** | **Your first `/proof` entries** | **A CMS**, not hand-built pages. This is the one that bites — three case studies as static pages is fine, thirty is not |
| **10** | Testimonials, a real pricing page, a guarantee page | Testimonial and pricing components already styled |
| **25** | A second ICP variant, an FAQ answering repeated objections | Clean components so a duplicate-and-edit is minutes |
| **50** | Case studies with numbers, a talent page, legal pages | **Blog/CMS depth and enough section variety that you are editing, not rebuilding** |

> **The rebuild you are avoiding would land in month three or four — your busiest month.** That is the
> real cost of a thin template, and it is much larger than the $79.

**And strip whatever you buy.** Templates ship with animation and section counts designed to demo well
in a marketplace. Delete aggressively — every animation removed buys back LP-view rate, and the 85%
in the funnel is an assumption you can move in the right direction for free.
