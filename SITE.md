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
| **Static site + Claude Code + Cloudflare Pages** | 4 | 4 | 5 | 5 | 4 | 5 | 5 | **88.8** | **$0 hosting** — Cloudflare Pages' free tier **explicitly permits commercial use**, unlimited bandwidth, unlimited static requests, 500 builds/month |
| **Webflow** | 4 | 5 | 5 | 4 | 5 | 3 | 4 | **87.8** | **Basic $15/mo, Premium $25/mo** (annual). **Optimize — the A/B product — is $299/mo** |
| **Carrd** | 5 | 5 | 5 | 2 | 2 | 5 | 2 | **80.2** | **$19/year** |
| **Squarespace / Wix** | 5 | 5 | 3 | 3 | 3 | 4 | 2 | **78.0** | ~$16–29/mo |
| **GoHighLevel** | 4 | 5 | 3 | 5 | 2 | 2 | 1 | **73.0** | **~$97/mo** |
| **WordPress + Elementor** | 4 | 2 | 2 | 5 | 3 | 4 | 5 | **68.2** | ~$10–30/mo hosting + plugin licences |
| **Next.js or Astro on Vercel** | 1 | 1 | 5 | 5 | 5 | 5 | 5 | **64.8** | **$20/mo — Vercel's Hobby plan prohibits commercial use**, so Pro is required |

**Framer — 93.4** · **Easiest of the serious options for a non-developer** — consistently rated easier to learn than Webflow, especially coming from Figma. Static output, so pages are fast. `STACK`=4 only because CAPI needs a third-party relay rather than being native

**Static site + Claude Code + Cloudflare Pages — 88.8** · **Added after the first version of this file scored the code option `EDIT`=1 — which assumed the operator hand-editing code.** With an agent doing the editing that is wrong. Put **all copy in one content file** and a headline change is one line in GitHub's web UI, no code and no agent, auto-deploying in about a minute. A new LP variant is a copied block, and variants are **free and unlimited** rather than metered. `NOCODE`=4 and `CREDIBLE`=4 are the honest deductions — see §6

**Webflow — 87.8** · More powerful and more portable, and **not fast to learn**. The $299 Optimize tier is irrelevant at launch volume (§1), so ignore it — but so is most of what makes Webflow worth the learning curve, at this stage

**Carrd — 80.2** · Genuinely the fastest way to ship one page. **Single-page-oriented and visibly template-y** — wrong for a multi-page site carrying a five-figure offer

**Squarespace / Wix — 78.0** · Easy, but slower pages and weaker control over the one thing that matters most here — many near-identical landing-page variants

**GoHighLevel — 73.0** · Native to the media-buying world and **collapses pages + CRM + booking + payments into one bill**. But funnel-builder output looks like funnel-builder output, which fights a premium claim, and it is the most locked-in option here

**WordPress + Elementor — 68.2** · Infinitely extensible and **the maintenance is the product**: updates, plugin conflicts, security, and page speed you have to fight for. Exactly the burden the brief rules out

**Next.js or Astro on Vercel — 64.8** · The hand-coded version of the row above, without an agent: **every headline change is a code edit and a deploy you perform yourself.** Right for a team with an engineer, wrong for a solo operator whose scarcest input is attention. Note the licence point — Hobby is not an option for a business

> **Framer wins by 4.6 points over Static site + Claude Code + Cloudflare Pages**, almost entirely on `EDIT`. Given §1, that is
> the right thing to optimise: the loop is *change it and look*, run dozens of times, alone.

---

## 7. Re-weighted: easy, unbreakable, and 80–90% is enough

The brief tightened, and **it reverses §6's recommendation.** Three changes:

| What you said | What it changes |
|---|---|
| *"super easy to build, maintain and update"* | `EDIT` and `NOCODE` stay at the top |
| *"at least 80–90% good"* | `CREDIBLE` becomes a **gate at 3**, not a maximiser. But note what this does *not* do — see the verdict |
| *"no issues that might easily break"* | **A new dimension, `FRAGILE`, at weight 22.** Nothing in §2 measured this, and it is the axis the code path loses on |

| Dimension | Wt | What it measures |
|---|---|---|
| **EDIT** | 24 | *"super easy to update"* — change a headline alone, in minutes |
| **FRAGILE** | 22 | **New, and close to a veto.** *"No issues that might easily break."* Can this fail in your hands, at 11pm, before a campaign, in a way you cannot fix alone? |
| **NOCODE** | 14 | *"easy to maintain"* — no updates, plugins, dependencies or builds to keep alive |
| **SPEED** | 12 | Page load. The funnel carries an 85% LP-view rate |
| **STACK** | 12 | Pixel + CAPI, forms, booking, a payment step for the teardown |
| **CREDIBLE** | 10 | **Gated at 3.** *"80–90% good"* is a floor to clear, not a target to maximise — but a page carrying a five-figure offer cannot look cheap |
| **COST** | 4 | Monthly |
| **HANDOFF** | 2 | Can you hand it to a freelancer or VA later without hiring an engineer |

| Platform | EDIT | FRAGILE | NOCODE | SPEED | STACK | CREDIBLE | COST | HANDOFF | Score | Cost |
|---|---|---|---|---|---|---|---|---|---|---|
| **Framer** ✅ | 5 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | **96.4** | $30/mo |
| **Webflow** | 4 | 5 | 5 | 5 | 4 | 5 | 3 | 5 | **91.2** | $15–25/mo |
| **Leadpages** | 5 | 5 | 5 | 4 | 5 | 3 | 1 | 3 | **89.6** | **$99/mo** |
| **Carrd** ❌ gated | 5 | 5 | 5 | 5 | 2 | 2 | 5 | 3 | ~~86.0~~ | $19/yr |
| **Squarespace / Wix** | 5 | 5 | 5 | 3 | 3 | 3 | 4 | 4 | **85.2** | $16–29/mo |
| **Systeme.io** ❌ gated | 4 | 5 | 5 | 3 | 5 | 2 | 5 | 2 | ~~83.2~~ | free–$27/mo |
| **Static site + Claude Code + Cloudflare** | 4 | 3 | 4 | 5 | 5 | 4 | 5 | 2 | **80.4** | $0/mo |
| **Notion + Super.so** | 5 | 4 | 5 | 3 | 2 | 3 | 4 | 2 | **77.6** | ~$16/mo |
| **GoHighLevel** ❌ gated | 4 | 4 | 5 | 3 | 5 | 2 | 2 | 4 | ~~77.2~~ | ~$97/mo |
| **WordPress + Elementor** | 4 | 1 | 2 | 2 | 5 | 3 | 4 | 5 | **57.2** | $10–30/mo |

**Framer · 96.4** — **Cannot break in the way you are worried about.** No build step, no dependencies, no updates, no plugins. Templates get you to 90% on day one, which is exactly the bar you set. Editing works from a phone

**Webflow · 91.2** — Same unbreakability, biggest freelancer pool, **slower to learn**. Ignore Optimize at $299 — §1

**Leadpages · 89.6** — Purpose-built for landing pages with A/B testing included — **and §1 proved you cannot use A/B testing for a year.** You would be paying $99/mo for the one feature that does not work at your volume

**Carrd · 86.0** — **gated on `CREDIBLE`** — Unbreakable, near-free, and **visibly template-y** — gated on `CREDIBLE`, because a $6k–$20k offer cannot arrive on a page that looks like a link-in-bio

**Squarespace / Wix · 85.2** — Unbreakable and genuinely easy. Slower pages, and weaker at holding many near-identical LP variants — the thing you said you want most

**Systeme.io · 83.2** — **gated on `CREDIBLE`** — Cheap and all-in-one; **templates are generic and there is no A/B testing at all.** Gated on `CREDIBLE`

**Static site + Claude Code + Cloudflare · 80.4** — **`FRAGILE`=3 is the whole story now.** The live site does not go down from a bad build — Cloudflare keeps the last good deploy — and rollback is one click. But a dependency can drift, a build can fail, and **structural changes need me.** Cheapest and most portable, and it is the one option that can leave you stuck

**Notion + Super.so · 77.6** — Editing in Notion is the easiest updating experience of anything here. **Forms, payments and pixel control are all weak**, and it looks like a Notion page

**GoHighLevel · 77.2** — **gated on `CREDIBLE`** — Funnel-builder output reads as funnel-builder output. Gated on `CREDIBLE`, and the most locked-in option here

**WordPress + Elementor · 57.2** — **The single most fragile option on the board** — plugin conflicts, forced updates, security patching, and speed you have to fight for. It is the specific thing you just ruled out

### Verdict — and it reverses §6

**Framer, 96.4.** Second is Webflow at 91.2. **The code path falls to 80.4**, and it
falls on exactly the axis you just named.

I recommended the code path last turn on **cost and unlimited variants**, having flagged fragility
as the one real risk. **You have now weighted that risk as near-decisive, so the recommendation
moves. That is the input changing, not me hedging** — and paying $30/month to delete an entire
class of failure is obviously correct for someone whose scarcest resource is attention in a
launch month.

> **The sharper point: lowering the bar to "80–90% good" does not help the code path — it helps the
> template path.** Templates are precisely how you reach 90% without effort. A lower quality bar
> would only favour building it yourself if code were the cheaper way to be *good enough*. It is not;
> it is the cheaper way to be *free*.

**What you give up by choosing Framer:** about $30–50/month, and landing-page variants become
inventory you rent rather than files you copy. At the volumes in §1 — 2,429 LP views a month — that
is not a constraint you will feel this year.

**And note the two purpose-built landing-page tools both lose**, which is the counter-intuitive
result here. Leadpages is $99/month and Systeme.io is free-ish, and both sell **A/B testing as the
headline feature that §1 proved you cannot use for roughly a year.** You would be buying the one
thing that does not work at your volume.

---

## 8. Framer vs Webflow, head to head

They score 96.4 and 91.2, which is close enough to be worth separating properly. Most comparisons
of these two are written for agencies. This one is written for **a solo media buyer with one month**.

| | Framer | Webflow | Who wins, and by how much |
|---|---|---|---|
| **Learning curve** | Canvas-based, close to Figma | **Exposes the CSS box model** — a class system you have to actually learn | **Framer, decisively.** This is the whole difference. Webflow is a professional tool that makes you competent at CSS before it makes you productive |
| **Time to a live page** | Template → live in an afternoon | Template → live in a day or two, then fighting classes | **Framer.** Measured in days of a one-month launch |
| **Price** | Pro **$30/mo**, editor seats $20 | Basic **$15/mo**, Premium $25 (annual) | **Webflow**, but less than it looks — Webflow bills **site plan *and* workspace plan**, so the gap narrows |
| **Page allowance for LP variants** | No explicit static-page cap on Pro | **300 static pages** on Basic | **Neither.** Both are far beyond a 6-page site plus variants — this is not a real constraint at your scale |
| **CMS depth** | 10,000 items, hard cap on Pro | 20,000 items on Premium | **Webflow**, and irrelevant until the graded directory exists |
| **Freelancer pool** | Smaller, growing | **Much larger and cheaper** | **Webflow.** And note the irony — *you are building a company that places Indian talent*, so hiring a Webflow freelancer is trivially easy for you specifically |
| **Export / lock-in** | No code export | Can export static HTML/CSS | **Webflow.** Framer is the more locked-in of the two |
| **Extensibility in year two** | Fine | **Better** | **Webflow** |
| **Page speed** | Static, CDN | Static, CDN | **Tie** |
| **Can it break on you** | No | No | **Tie** — which is the point of §7 |

### The trade, stated plainly

> **Framer buys you launch speed. Webflow buys you optionality later.**

And that is the whole decision, because **the optionality Webflow buys is optionality on a business
that does not exist yet.** Framer's advantage lands in week one. Webflow's lands in year two — by
which point you have revenue and can pay someone to rebuild it in anything you like. **Buy the thing
that helps now; the later problem is a better problem to have and it is solved with money you will
have by then.**

### When I would tell you to pick Webflow instead

| | |
|---|---|
| **You already know it** | Then the learning curve — the only real Framer advantage — is zero, and every Webflow advantage stands. Pick Webflow |
| **You intend to hand the site to a freelancer immediately** | Then you are not paying the learning cost either way, and the bigger pool plus code export wins |
| **You expect the graded directory to become a large CMS-driven site inside 12 months** | Webflow's CMS ceiling is double, and its collection tooling is stronger |

**None of those is true today**, on what you have told me: you want to edit it yourself, constantly,
starting now. That is the Framer case.

*One caveat I would hold lightly: the handoff worry is overstated in both directions. **The edits
that matter for landing-page testing are copy edits**, and those are trivial in either tool — a
freelancer picks up Framer in a day. The freelancer-pool gap only bites on deep structural work,
which is a year-two problem.*

---

## 6. "Why not just build it with Claude Code and deploy it cheap?"

A fair challenge, and it **corrects a score in §2**. The first version of this file gave the code
option `EDIT`=1 and `NOCODE`=1 — both of which assumed *the operator* hand-editing code. With an
agent doing the editing, that assumption is wrong, and the option moves from last place to second.

| | Framer | Static + Claude Code + Cloudflare |
|---|---|---|
| **EDIT** | 5 | 4 |
| **NOCODE** | 5 | 4 |
| **SPEED** | 5 | 5 |
| **STACK** | 4 | 5 |
| **CREDIBLE** | 5 | 4 |
| **COST** | 4 | 5 |
| **PORTABLE** | 3 | 5 |
| **Score** | **93.4** | **88.8** |
| **Cost** | $30/mo + $20/seat | **$0/mo** |

### What the code path genuinely wins

| | |
|---|---|
| **Hosting is actually free** | **Cloudflare Pages' free tier explicitly allows commercial use**, with unlimited bandwidth and unlimited static requests. **Vercel's Hobby plan does not** — it restricts to non-commercial personal use, so Vercel means $20/mo Pro. If you were reaching for Vercel, reach for Cloudflare instead |
| **Landing-page variants are free and unlimited** | This is the one that matters given the brief. A variant is a copied block in a content file — no page-count tier, no per-seat fee, no per-event billing. On a hosted builder every variant is inventory you are renting |
| **Fastest possible pages** | Static HTML on an edge network. §2 weights `SPEED` at 16 because the funnel carries an 85% LP-view rate |
| **You own it** | Files in the git repo you already have. No export, no lock-in, no platform pricing change to absorb |
| **Free split-testing later** | A Cloudflare Worker can split traffic on a cookie for $0 when volume ever justifies it — versus $299/mo. §1 says that is month twelve, but it costs nothing to have the option |

### What it genuinely costs

| | |
|---|---|
| **It can break in a way Framer cannot** | A bad commit at 11pm before a campaign, and the site is down. **This is the real risk and it is the only one I would weigh heavily.** Mitigated by: every change is a git commit, so rollback is one click in GitHub; and Cloudflare keeps the last good deployment live if a build fails |
| **No visual editing** | You describe a layout change instead of dragging it. For *copy* that is fine — arguably faster. For **layout** Framer is better, and you have a media buyer's eye, which is worth something |
| **Design quality is not guaranteed by a template** | Framer hands you a credible premium look on day one. A code site looks as good as what gets built — `CREDIBLE`=4 rather than 5. Given you have **no Western track record**, the site carries more trust load than usual |
| **Structural changes need a session** | Copy edits do not. Anything else does |

### The architecture that makes `EDIT`=4 true rather than aspirational

The whole argument rests on one decision: **all copy lives in a single content file, separate from
markup.**

```
  content/site.json     <- every headline, subhead, bullet, CTA, price. YOU edit this
  content/lp/*.json     <- one file per landing-page variant. Copy a file = new variant
  src/                  <- layout and components. I edit this, rarely
```

So changing a headline is: open the file on github.com, click the pencil, type, commit. **No
terminal, no build knowledge, no agent, no local machine — it works from a phone**, and Cloudflare
rebuilds in about a minute. A new landing page for a new angle is one copied file. That is the loop
§1 says you actually need, and it is the loop the brief asked for.

### Verdict

**Framer still scores higher — 93.4 to 88.8 — and the gap is almost entirely `EDIT` and `CREDIBLE`,
which are both about *layout* rather than copy.** So the honest answer is that this is close, and
it turns on one question:

> **When something breaks the night before a campaign, can you fix it alone?** On Framer, yes — it
> cannot break that way. On code, you roll back a commit, which is one click, but you have to know
> that is the move.

**What I would actually do: build it in code, on Cloudflare Pages, with the content file.** Three
reasons. It costs **$0/month against ~$50**, which at pre-revenue is real. LP variants are unlimited
and free, which is the stated requirement. And **porting later is cheap in one direction only** — a
content file drops into Framer in an afternoon, whereas starting in Framer and moving to code means
rebuilding. Start where the exit is cheap.

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
