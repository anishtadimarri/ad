# Building `allhandstalent.com`

> **Framer Pro, $30/month. One tool, one domain, path-based pages. Cal.com for booking, a Stripe
> Payment Link for the paid teardown. Do not buy an A/B testing product — §1 shows you cannot
> reach significance at launch volume, and the money is better spent on being able to change the
> page in two minutes.**

---

## 1. First: "test landing pages" cannot mean split-testing yet

Every platform upsells A/B testing — **Webflow Optimize is $299/month**, Framer's *Convert* add-on
bills per event. So it is worth computing whether a split test can conclude anything at your volume,
using this repo's own funnel rather than a guess.

The landing page converts at **2.0%** ([`funnel.py`](scoring/funnel.py), calendar-booking flow).
Standard two-proportion test, **80% power, 95% confidence**:

| To detect a lift of | LP views **per arm** | Total LP views | Ad spend to get there |
|---|---|---|---|
| **10%** | 80,679 | 161,357 | **$332,206** |
| **20%** | 21,106 | 42,211 | **$86,906** |
| **30%** | 9,795 | 19,589 | **$40,330** |
| **50%** | 3,822 | 7,645 | **$15,739** |

At $5,000 of spend on broad you get **2,429 landing-page views** and **49 leads**.

> **One test at a 20% lift needs $86,906 of spend** — roughly **17× a $5,000 month**, to answer
> *one* question about *one* headline. A 10% lift needs $332,206. **Split-testing is a month-twelve
> tool.** Anyone selling it to you now is selling statistical theatre.

What this changes: **the requirement is not a testing engine, it is an editor.** Change the page,
ship it, read the direction, change it again — and judge with your eyes and your call notes, not
with a p-value. That is a $30/month problem, not a $299/month one.

**Where split-testing *does* work from day one is the ad, not the page.** Meta tests creative natively
at the ad level, where the unit is an impression rather than a lead, so volume arrives ~50× faster.
Put the testing effort there — which is also the thing the operator is already world-class at.

---

## 2. Where to build it

| Dimension | Wt | What it measures |
|---|---|---|
| **EDIT** | 26 | Can the operator change a headline and republish **alone, in minutes**, with no developer and no deploy step |
| **NOCODE** | 18 | Does *maintenance* need a developer — updates, security, plugins, broken builds |
| **SPEED** | 16 | Page load. Not vanity: [`funnel.py`](scoring/funnel.py) carries an **85% landing-page-view rate**, and that number is a page-speed number. Every point lost there is lost at the top of the funnel |
| **STACK** | 16 | Meta pixel and **Conversions API**, forms, booking, and a **payment step for the paid teardown** ([`OFFER.md`](OFFER.md) §9.1) |
| **CREDIBLE** | 12 | Does the output look like a company a buyer pays $6k–$20k? No track record means the site carries more trust load than usual |
| **COST** | 7 | Monthly, all-in |
| **PORTABLE** | 5 | Can you leave, and do you own the content |

| Platform | EDIT | NOCODE | SPEED | STACK | CREDIBLE | COST | PORTABLE | Score | Price |
|---|---|---|---|---|---|---|---|---|---|
| **Framer** ✅ | 5 | 5 | 5 | 4 | 5 | 4 | 3 | **93.4** | **Pro $30/mo** (CMS + forms). A/B add-on *Convert* is available on Pro, billed **$50 per 500K events**. Editor seats $20/mo |
| **Webflow** | 4 | 5 | 5 | 4 | 5 | 3 | 4 | **87.8** | **Basic $15/mo, Premium $25/mo** (annual). **Optimize — the A/B product — is $299/mo** |
| **Carrd** | 5 | 5 | 5 | 2 | 2 | 5 | 2 | **80.2** | **$19/year** |
| **Squarespace / Wix** | 5 | 5 | 3 | 3 | 3 | 4 | 2 | **78.0** | ~$16–29/mo |
| **GoHighLevel** | 4 | 5 | 3 | 5 | 2 | 2 | 1 | **73.0** | **~$97/mo** |
| **WordPress + Elementor** | 4 | 2 | 2 | 5 | 3 | 4 | 5 | **68.2** | ~$10–30/mo hosting + plugin licences |
| **Next.js or Astro on Vercel** | 1 | 1 | 5 | 5 | 5 | 5 | 5 | **64.8** | $0–20/mo |

**Framer — 93.4** · **Easiest of the serious options for a non-developer** — consistently rated easier to learn than Webflow, especially coming from Figma. Static output, so pages are fast. `STACK`=4 only because CAPI needs a third-party relay rather than being native

**Webflow — 87.8** · More powerful and more portable, and **not fast to learn**. The $299 Optimize tier is irrelevant at launch volume (§1), so ignore it — but so is most of what makes Webflow worth the learning curve, at this stage

**Carrd — 80.2** · Genuinely the fastest way to ship one page. **Single-page-oriented and visibly template-y** — wrong for a multi-page site carrying a five-figure offer

**Squarespace / Wix — 78.0** · Easy, but slower pages and weaker control over the one thing that matters most here — many near-identical landing-page variants

**GoHighLevel — 73.0** · Native to the media-buying world and **collapses pages + CRM + booking + payments into one bill**. But funnel-builder output looks like funnel-builder output, which fights a premium claim, and it is the most locked-in option here

**WordPress + Elementor — 68.2** · Infinitely extensible and **the maintenance is the product**: updates, plugin conflicts, security, and page speed you have to fight for. Exactly the burden the brief rules out

**Next.js or Astro on Vercel — 64.8** · Fastest and most controllable, and **every headline change is a code edit and a deploy**. Correct answer for a team with an engineer. Wrong answer for a solo operator whose scarcest input is attention

> **Framer wins by 5.6 points over Webflow**, almost entirely on `EDIT`. Given §1, that is
> the right thing to optimise: the loop is *change it and look*, run dozens of times, alone.

---

## 3. The structure

One domain. Paths, not subdomains. Homepage entirely demand.

| Path | For | What it is | Build |
|---|---|---|---|
| **`/`** | buyer | **The homepage. Demand only.** Hero → the graded proof → how it works → guarantee → one CTA. No careers link above the fold | week 1 |
| **`/agencies`** | buyer | **Ad destination, ICP 1.** Marketing agencies. Ads point *here*, never at `/` — [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §7 makes this the control that keeps Meta's page review away from any job content | week 1 |
| **`/ecommerce`** | buyer | **Ad destination, ICP 2.** E-comm brands. Same page, different proof and different language. [`MODEL-V2.md`](MODEL-V2.md) gap 8: **two ICPs, one role, two ads** — five starves Meta of signal | week 1 |
| **`/proof`** | buyer | **The graded work sample, and the most important page on the site.** Recut ads with **3-second and 15-second retention measured against the original** ([`MODEL-V2.md`](MODEL-V2.md) gap 6). This is what makes *premium* falsifiable instead of an adjective | week 2 |
| **`/pricing`** | buyer | **One-time, 30–35% of first-year compensation**, plus EOR presented as the **default** employment path. Gaps 1 and 4 — the pricing conflation breaks the model 8× if left ambiguous | week 2 |
| **`/guarantee`** | buyer | **12-month unlimited replacement, no cash refunds.** Modelled as *cheaper* than the 6-month industry standard while sounding stronger — the cheapest differentiation available | week 2 |
| **`/teardown`** | buyer | **The money gate.** Paid ad-account and creative teardown → Stripe → booking. This is the paid step that funds the search and filters tyre-kickers | week 1 |
| **`/thanks`** | buyer | Confirmation + what happens next + calendar | week 1 |
| **`/talent`** | supply | **Footer link only. `noindex, nofollow`. No Meta pixel.** And **do not publish it in launch month at all** — supply needs zero ad spend, referral and LinkedIn fill the first ten to twenty seats | month 3–6 |

**Ads never point at `/`.** They point at `/agencies` or `/ecommerce`. Two reasons: the message
matches the audience, and page review sees a dedicated buyer page with no route to job content.

---

## 4. The rest of the stack

| Job | Tool | Cost | Why |
|---|---|---|---|
| Site + landing pages | **Framer Pro** | $30/mo | One tool for the brand site *and* every LP variant. Duplicate a page, change the headline, publish — that is the whole loop §1 says you actually need |
| Booking | **Cal.com** | free–$15/mo | Embeds in Framer. Free tier is enough for one calendar |
| Payment for the teardown | **Stripe Payment Link** | 2.9% + 30¢ | **No code at all** — a hosted checkout URL you paste into a button. Do not build a checkout |
| Forms → inbox | Framer Forms → email + Google Sheet | included | A spreadsheet is a sufficient CRM until roughly placement ten |
| Pixel + CAPI | Meta Pixel via Framer's custom-code field; **CAPI via Stape or Zapier** | $0–20/mo | Browser pixel alone under-reports. **Verify CAPI works before spending**, since every CAC number in [`LTGP.md`](LTGP.md) assumes conversions are actually attributed |
| Analytics | Framer Analytics or Plausible | $0–9/mo | You need page-level conversion rate, not a dashboard |
| Email | **Google Workspace on the domain** | $6/user/mo | `you@allhandstalent.com` before the first ad runs |

**All-in: roughly $45–70/month.** The $299 tier you were being sold does not appear, because §1
says it would buy nothing until month twelve.

---

## 5. Build order

| | Week | Ship |
|---|---|---|
| 1 | Week 1 | `/agencies`, `/ecommerce`, `/teardown`, `/thanks`, and a one-screen `/`. **Ad destinations before brand pages** — nothing else can earn a dollar |
| 2 | Week 1 | Stripe Payment Link, Cal.com, pixel **and CAPI verified with test events before any spend** |
| 3 | Week 2 | `/proof` — the recut ads with retention numbers. **The single highest-leverage page**, and the only one that turns *premium* from an adjective into a claim a buyer can check |
| 4 | Week 2 | `/pricing` and `/guarantee`. State the fee as **one-time, 30–35% of first-year comp**; present EOR as the default |
| 5 | Week 3 | Fill `/` properly. LinkedIn company page live |
| 6 | Month 3–6 | `/talent`, footer-linked, `noindex`, with the pass rate on it |

*Prices checked at time of writing and they move — Framer Pro $30/mo with Convert billed per event,
Webflow Basic $15 / Premium $25 annual with Optimize at $299/mo. Re-check before you subscribe.*
