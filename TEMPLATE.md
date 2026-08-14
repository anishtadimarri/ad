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

## 3. Two corrections: I crawled the pages, and `STABLE` was the wrong worry

**I cannot log into Framer** — no account, and I will not pretend to have looked inside the editor.
The one thing that genuinely requires it is whether a blog is a **CMS collection or hand-built pages**,
because **Framer statically generates CMS pages**, so the served HTML looks identical either way.

What I could do, and had not: **crawl each demo's sub-paths.** Every judgement before this was made
from homepages. A control path returned **404 on all five sites**, so the results are trustworthy:

| Template | Real pages found | Effect |
|---|---|---|
| **Recruitify** | **7** — `/about` `/services` `/pricing` `/faq` `/projects` `/contact` `/privacy` `/terms` | **The most of anything tested**, including legal pages that Meta's ad review looks for |
| Conversion | 4 — `/about` `/services` `/blog` `/contact` | `COMPLETE` 2→3. **But the `/blog` has broken placeholder links including a literal `404` in the nav** |
| Cubicles | 4 | As expected |
| **Funnelz** | **2** — home + `/blog` | `COMPLETE` 5→4. Pricing and team are homepage *sections*, not pages |
| **Recruitment Hub** | **1** — `/contact` only | `COMPLETE` 3→2. **Effectively a one-pager**; everything else was an anchor link |

### And `STABLE` was importing a WordPress worry into a platform where it does not apply

> *"Is stability going to be an issue for Funnelz?"* — **No, and I had the criterion weighted wrong at 20.**

**In Framer there is no upstream to break.** No plugins, no dependencies, no version updates, no
security patches. When you remix a template it becomes **a frozen copy inside your own project**. A
creator who abandons a template cannot affect a site that is already live — unlike WordPress, where
an unmaintained plugin is a live liability.

So the real question is narrower: **will the creator answer a setup question in week one?** That is
worth something, and it is worth **8, not 20**. Cutting it also removes the main thing propping up
Conversion, whose demo **ships with broken links** — which is a better stability signal than age, and
it points the other way.

---

## 4. The criteria

> *"We need a framework to edit and do least work. We don't care about other things."*

That collapses the scoring into one question — **how far is this template from the site you need?**
Edit distance decomposes into five terms, and `SHAPE` dominates because a wrong-shaped template is not
a restyle, it is a different website.

**On "consider hundreds":** I did not enumerate hundreds, and I would not trust it if I had. **Three
times in this project a listing has been wrong** — `conversion.framer.website` turned out to be a
generic Framer starter page, Framer serves a soft-200 for slugs that do not exist, and aggregator
articles repeat each other. What changed the answer was **opening six demos and reading what is
actually on them.** Verification beat enumeration, and the biggest finding came from a search I had
not run at all — recruitment templates.

---

## 4. The criteria

Not generic web-design advice. These weights come from **your** traffic: overwhelmingly mobile,
cold, mid-scroll, and metered by an 85% LP-view rate.

| Criterion | Wt | What it means | Can I check it? |
|---|---|---|---|
| **COMPLETE** | 34 | **Tooling and real pages that actually exist.** Now verified by crawling each demo's sub-paths rather than reading its homepage — a control path returned 404 on every site, so the results are reliable | **crawled** |
| **CONVERT** | 28 | **Funnel-optimised for cold Meta traffic.** Single-goal pages, CTA in hero and repeated, social proof early, an objection or comparison block, booking at the end | verified by demo |
| **SHAPE** | 18 | Employer-facing **services** structure — not a candidate job board, not a SaaS product page. Structural, and a job-board shape risks Meta's Employment Special Ad Category ([`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §1, a 10–29% CAC tax) | verified by demo |
| **STABLE** | 8 | **Cut from 20 — see §3.** In Framer there is no upstream to break: no plugins, no dependencies, no updates to apply. Once remixed, the template is a frozen copy inside your project | reframed |
| **NETCOST** | 6 | Cost net of the bundled 3 months of Framer Pro (§2) | listing |
| **RECOPY** | 6 | Register distance. A copy-and-colour job, not a build job | verified |

> **The top two weights — 40 points of 100 — are the two I cannot verify.** `MOBILEHERO` and `SPEED`
> are properties of the live preview on a phone on mobile data. Everything below is therefore a
> **shortlist to test**, not a ranking to trust.

---

## 5. The ranking, after crawling

Scored on the 6 assessable criteria only — 100 of 100 points. **`MOBILEHERO` and `SPEED` are
deliberately absent**, which is why the top score here is not a recommendation.

| # | Template | Price | Cmpl | Conv | Shape | Stab | **Score** | **Real pages (crawled)** | Note |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Recruitify** | paid `[?]` | 4 | 4 | 5 | 3 | **83** | home + **`/about` `/services`… `/pricing` `/faq` `/projects` `/contact` `/privacy` `/terms`** | **Crawled — and it has the most real pages of anything tested: seven.** Including a genuine **`/pricing`**, **`/faq`**, **`/projects`** (case studies) and **`/privacy` + `/terms`**, which Meta's ad review looks for. Process is already Consultation → Screening → Placement. **The single gap is no `/blog`, so no CMS** — proof entries would be hand-built |
| 2 | **Funnelz** | paid `[?]` | 4 | 5 | 4 | 3 | **82** | home + **`/blog`** | **Crawled.** One long homepage plus a blog. Homepage carries hero+CTA, social proof, **case studies**, services, **3-tier pricing**, team, **booking in the nav** — so pricing and team are *sections*, not pages, which is fine. **Its blog posts carry dates, categories, authors and individual URLs — the shape of a CMS collection**, which is the tooling that matters most. `COMPLETE` 5→4: fewer standalone pages than the homepage implied |
| 3 | **Conversion** | ~$79 `[?]` | 3 | 5 | 4 | 3 | **76** | home + `/about` `/services` `/blog` `/contact` | **Crawled, and it cost it.** `COMPLETE` 2→3 because four real pages do exist — but the `/blog` is **4 items with no dates, no categories and broken placeholder links including a literal `404` in the nav.** **`STABLE` 5→3**: a demo shipping broken links is a quality signal that contradicts the longevity story. Still the **best conversion architecture found** — Results metrics block, comparison table |
| 4 | **Nakula / Fabrica / Lyniq** | $69–129 `[?]` | 4 | 3 | 3 | 4 | **70** | not crawled | **Not verified.** The 'looks expensive' tier, usually the heaviest — which fights `CONVERT` on a phone |
| 5 | **Recruitment Hub** | **free** | 2 | 4 | 5 | 3 | **68** | home + `/contact` **only** | **Crawled — and it is thinner than the homepage suggested.** `COMPLETE` 3→2: **one sub-page.** Everything else is a homepage anchor. Good persuasion order (why-us comparison, 3-step process, pricing, FAQ) and free, but **no CMS, no case studies and no real page structure** |
| 6 | **HRPro** | paid `[?]` | 3 | 3 | 4 | 3 | **66** | not crawled | **Not verified.** Open the demo before considering it |
| 7 | **Recruitment (Shah)** | **free** | 3 | 3 | 4 | 3 | **65** | not crawled | **Not verified.** Free |
| 8 | **Cubicles** | ~$59 `[?]` | 3 | 2 | 4 | 4 | **61** | home + `/about` `/services` `/blog` `/contact` | **Crawled.** Four real pages including a blog, plus case studies and industries on the homepage. But `CONVERT`=2 — weak repeated CTA, no pricing, no objection block. **A brochure, not a funnel** |
| 9 | **Greenleaf** | **free** | 2 | 3 | 4 | 4 | **56** | not crawled | Clean and free, but thin on tooling, no bundle, and built for sustainability consultants |
| 10 | **TalentBridge** | paid `[?]` | 2 | 3 | 1 | 3 | **44** | single page | **Disqualified.** An all-in-one HR platform with integrations and *Request Demo*. A product site, not a services firm |
| 11 | **Talentify** | **free** | 2 | 2 | 1 | 3 | **39** | not crawled | **Disqualified.** *"Your gateway to remote tech careers."* The supply side — and a job-board shape is what risks Meta's Employment Special Ad Category |

*Names and prices are from marketplace aggregators and are marked `[?]` — **verify both on Framer
before buying**, since listings and pricing churn.*

---

## 6. The phone test — still run it

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

## 7. What I would actually do

**Recruitify — and the crawl is what moved it back to the top.** Seven real pages including `/pricing`,
`/faq`, `/projects` and **`/privacy` + `/terms`**, against Funnelz's two. It is the only candidate that
is already a *site* rather than a long page, and page structure is exactly the tooling you said has to
be there.

**Its one gap is the CMS.** Funnelz's blog carries dates, categories, authors and individual URLs —
CMS-shaped — and Recruitify has no `/blog` at all. So the decision reduces to one question:

> **Do you need `/proof` to be CMS-backed on day one?** Under ten entries, hand-built pages in Framer
> are fine and Recruitify wins comfortably. Past thirty, you want the collection — and adding a CMS
> collection to a Framer site later is a normal afternoon, not a rebuild.

**That tips it to Recruitify**, because the thing you cannot add later is a coherent page structure,
and the thing you can is a blog.

| | |
|---|---|
| **Funnelz stays a close second** | Best tooling *on one page*, CMS-shaped blog, booking in the nav. **Pick it if you would rather add pages than add a CMS** |
| **Conversion drops** | Best conversion architecture found, but four pages, a fake blog, and **broken links shipped in the demo**. Still worth **stealing its comparison table and Results metrics block** — the comparison block is where the **$5,000–16,500/mo vendor-invoice** argument lives |
| **Recruitment Hub is out** | The crawl exposed it as a one-pager. Free, but you would build the entire site around it |

### Four rounds, four weightings

| Round | What I weighted | Winner |
|---|---|---|
| 1 | Mobile + speed + sections | Conversion |
| 2 | Edit distance, `RECOPY` at 15 | Recruitify |
| 3 | `COMPLETE` + `CONVERT` + `STABLE` at 20 | Funnelz |
| **4** | **Crawled pages; `STABLE` cut to 8** | **Recruitify** |

**The ranking moved three times and each move came from one thing: better evidence or a corrected
weight.** Round four is the first built on what is actually deployed at each URL rather than on a
homepage or a listing. **Run the phone test on Recruitify and Funnelz and buy the one that passes** —
that is the last check, and it is the one only you can run.
