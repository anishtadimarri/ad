# Supply and Demand on the Same Page?

> **One domain. `/talent` as a path, homepage entirely demand. Not a second domain, not a subdomain —
> and at launch, no public supply page at all.** §7 scores the four architectures; §1–§3 are why it
> matters, which is a **10–29% CAC tax** priced off the funnel model itself.

---

## 1. The expensive reason: Meta's Special Ad Category

Meta classifies advertising for **job opportunities, internships and job boards** as *Employment*,
a Special Ad Category. Inside it:

| Restriction | Consequence for [`TARGETING.md`](TARGETING.md) |
|---|---|
| **Lookalike audiences built on Meta's data are unavailable**, and Special Ad Audiences were removed for recruitment on 12 October | **This is the one that costs money. [`LTGP.md`](LTGP.md) puts 45% of spend on the lookalike leg** |
| Custom audiences from your own first-party data **are still permitted** | The intent seed — a custom audience scraped from job postings — **survives** |
| States can be targeted; **ZIP codes cannot**, and location exclusion is disallowed | No metro-level concentration |
| Age must be 18–65+, all genders included | No demographic narrowing |
| Demographic, behavioural and interest options limited | **Broad gets worse too**, which is why §2 runs three scenarios |

**Classification is a review decision, and Meta reviews the ad creative *and the landing page*.**
A page that prominently offers jobs raises the odds that a B2B ad aimed at employers gets reclassified
as employment. That is the mechanism — not a rule that mixing them is forbidden, but a materially
higher chance of landing in a category that deletes 45% of the audience plan.

---

## 2. What the reclassification actually costs

Driven through the **real funnel** in [`funnel.py`](scoring/funnel.py) at the same 24% teardown
take-up that produces [`LTGP.md`](LTGP.md)'s $732 baseline — not a closed form. A first draft of this
file reconstructed the blend algebraically and came out 1.8% high, because the deposit step applies
an intent multiplier under a cap and the intent seed is limited by matched audience size. The
lost-targeting effect is modelled as a **CTR haircut on broad**, the same lever `funnel.py`'s own
sensitivity tests use.

| | Intent seed | Lookalike | Broad | Blended CAC | 30-day | Lifetime |
|---|---|---|---|---|---|---|
| **As modelled** | 25% @ $489 | 45% @ $817 | 30% @ $1,070 | **$732** | **6.06:1** | **15.49:1** |
| Employment category — *broad CTR holds* | 25% @ $489 | **unavailable** | 75% | **$803** *(+10%)* | **5.52:1** | 14.11:1 |
| Employment category — *broad CTR −25%* | 25% @ $489 | **unavailable** | 75% | **$883** *(+21%)* | **5.02:1** | 12.83:1 |
| Employment category — *broad CTR −40%* | 25% @ $489 | **unavailable** | 75% | **$944** *(+29%)* | **4.70:1** | 12.00:1 |

**It does not break the hard constraint.** Even the worst case, 4.70:1, clears 1.5:1 with room —
so this is not existential and I am not going to dress it up as though it were. It is a
**$72–$212 per-client tax (10–29%) for no benefit whatsoever**, taken off the top of every client you
ever acquire, and it compounds against the 30-day ratio that the whole plan is built to protect.

---

## 3. The subtler reason, which is worse than it looks

**Pixel contamination.** Job seekers convert far more cheaply than employers — they are more numerous,
more motivated, and asking less of themselves. Put both offers on one page behind one conversion
event and Meta's optimiser will find the cheap audience, because that is precisely what it is built
to do.

> Your **cost per lead falls** while your **cost per client rises**. The dashboard improves as the
> business gets worse, and the metric that hides it is the one you look at daily. That is a nastier
> failure than a 27% CAC tax, because the tax is at least visible.

It also poisons the retargeting pool and every lookalike you later build from it, so the damage
compounds rather than staying put.

---

## 4. The positioning reason

| Claim | What an open application page says instead |
|---|---|
| *Handpicked. Graded. We recut your ad and measure retention against the original* | *We take whoever applies* |
| A curated bench you cannot access elsewhere | A job board |
| The buyer is a **bottleneck** buyer being sold speed | A **marketplace**, which is a cost centre — the exact distinction in [`HUNGRY.md`](HUNGRY.md) |

Every high-end search firm hides candidate intake, and not by accident: **visible supply destroys the
scarcity claim that justifies the fee.** There is also a specific trap here — [`COMPETITOR-DATA.md`](COMPETITOR-DATA.md)
§7 found that **three of three India analogues monetise the worker and give the employer relationship
away.** A supply-forward site is the first step down that path, and it is the exact model this plan was
built to avoid.

---

## 5. So build it like this

| Surface | Audience | Rules |
|---|---|---|
| **`allhandstalent.com`** — root, and every ad destination | **Buyer only** | One offer, one CTA: the paid ad-account and creative teardown ([`OFFER.md`](OFFER.md) §9.1). No "careers", no "apply", no "join our talent network" above the fold |
| **`allhandstalent.com/talent`** | Supply | **Footer link only, never in the nav.** Its own conversion event, or excluded from the conversion event entirely. `noindex` if you want it invisible to Meta's page review |
| **The graded directory** | Buyer | Gated, behind the deposit. This is supply shown *to demand*, which is the opposite thing — see §6 |

**Same domain, not a second domain.** A candidate asked to apply needs to see a real company with
real clients; a standalone `apply-here.com` reads as a shell, and you are an unknown operator who
cannot afford to look like one.

And note what makes this cheap: **supply needs zero ad spend at launch.** Referral, LinkedIn outbound
and the graded directory fill the bench. A page nobody advertises to does not need to be optimised
for anything — so separating the two costs you nothing.

---

## 6. When this reverses

Once the bench exists, **showing supply becomes your strongest demand asset** — *"forty graded editors,
each with 3-second and 15-second retention measured against the ad they replaced"* is the single most
persuasive page you will ever put in front of an agency owner.

But that is **supply displayed to buyers, gated behind the deposit** — not an open application form.
One is a proof asset. The other is a job board. Same content, opposite businesses.

---

## 7. Separate domain, or one domain with separate pages?

The question asked directly. Four architectures, scored on what actually differs between them.

| Dimension | Wt | What it measures |
|---|---|---|
| **SACRISK** | 24 | Risk of a B2B ad being reclassified into the **Employment Special Ad Category**, which §2 prices at a 10–29% CAC tax |
| **BRAND** | 18 | Does brand equity concentrate on one domain? Weighted high because [`ARBITRARY.md`](ARBITRARY.md) §13 found *all hands talent* currently returns three other organisations on Google — split equity makes that worse |
| **OPSLOAD** | 16 | One operator, one month to launch. Low operational intensity has been rejected as a constraint twice |
| **SUPPLY** | 14 | Can it actually fill the bench at volume? |
| **TRUST** | 12 | Does a candidate see a real company with real clients, or a shell? |
| **BUYERSAFE** | 8 | What happens when a *buyer* finds the supply page |
| **PIXEL** | 4 | Keeping supply events out of buyer optimisation |
| **EV** | 4 | One brand, one asset, at exit |

| | Architecture | SACRISK | BRAND | OPSLOAD | SUPPLY | TRUST | BUYERSAFE | PIXEL | EV | Score |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | Two separate domains | 5 | 2 | 2 | 5 | 2 | 5 | 5 | 3 | **70.8** |
| **B** | One domain, `/talent` path, demand-first homepage ✅ | 4 | 5 | 5 | 5 | 5 | 4 | 5 | 5 | **93.6** |
| **C** | One domain, `talent.` subdomain | 4 | 4 | 4 | 5 | 4 | 4 | 5 | 5 | **84.4** |
| **D** | No public supply page — referral, LinkedIn and invite only | 5 | 5 | 5 | 3 | 4 | 5 | 5 | 5 | **92.0** |

**B — One domain, `/talent` path, demand-first homepage · 93.6** — **The proposal, and it wins.** One site to build and maintain, all equity in one place, and a candidate sees the real clients. `SACRISK` is 4 not 5 because Meta reviews landing pages — mitigated by the three controls below, not by a second domain

**D — No public supply page — referral, LinkedIn and invite only · 92.0** — **No job-opportunity page exists anywhere, so the category risk goes to zero** and there is nothing to build. `SUPPLY`=3 is the whole catch: fine for the first ten to twenty placements, a real constraint after that

**C — One domain, `talent.` subdomain · 84.4** — Same policy exposure as B with **none of the upside**: extra DNS, SSL and deploy target, and analytics and SEO tooling treat subdomains as separate sites. A path costs nothing and keeps everything unified

**A — Two separate domains · 70.8** — Cleanest possible isolation — a reviewer crawling the ad's domain finds no job content at all. But it **splits brand equity, needs a second name** after nine rounds of naming, doubles the site/hosting/analytics surface, and a candidate landing on a standalone apply-domain sees a shell

> **B beats A by 22.8 points**, and the margin is not about policy — it is `BRAND`, `OPSLOAD` and
> `TRUST`. **A is safer on the one dimension I can fix with three lines of config, and worse on the
> three I cannot.**

### One argument for a separate domain that used to be true and is not

Meta's **Aggregated Event Measurement** historically capped you at **eight conversion events per
verified domain**, so sharing a domain with a supply funnel meant supply events competing for those
slots. **Meta removed the 8-event limit and manual event prioritisation in June 2025**, and domain
verification is no longer required for AEM — events are aggregated automatically. I checked before
writing it down, because it is exactly the kind of stale received wisdom that would have argued for
splitting the domain for no reason.

### The three controls that do the work `SACRISK` is worried about

| Control | Why |
|---|---|
| **Ads point at `/hire` or `/teardown`, never at `/`** | Page review sees a dedicated buyer page with no navigation to job content |
| **`/talent` is `noindex, nofollow`, linked once from the footer with `rel="nofollow"`** | Reachable by a candidate who is told where to look; not crawled into the same site graph as the ad destination |
| **No Meta pixel on `/talent`** — or a separate dataset | Supply visitors never enter the buyer optimisation pool, the retargeting audience, or any lookalike built from it |

### And write the supply page as proof, not as a secret

The instinct is to hide it. Better: **write it so a buyer finding it strengthens the pitch.** A page
that states the bar — *what is tested, what the pass rate is, how many applicants were rejected last
month* — is evidence for the graded claim rather than against it. A page that says *"join our talent
network"* is a job board. **Same surface, opposite effect**, and the difference is entirely in the copy.

### What to actually do, in order

**Build B's structure. Ship D's content.** For launch month there is no public supply page at all —
[`§5`](#5-so-build-it-like-this) already notes supply needs **zero ad spend**, and referral plus LinkedIn
outbound fills the first ten to twenty seats. That takes `SACRISK` to zero for free.

Publish `/talent` when referral stops keeping up with demand — realistically month three to six —
and publish it with the pass rate on it.
