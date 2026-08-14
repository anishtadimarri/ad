# Somewhere's Site, and the Meta Build Spec

Two questions answered together, because the second constrains the first: **what does a working
site in this exact category look like**, and **what does Meta specifically require of it**.

Somewhere is the right reference. [`COMPETITOR-DATA.md`](COMPETITOR-DATA.md) already established
they are the closest large operator to this model — and unlike a template demo, **their site is
load-bearing for a real business.**

---

## 1. What is actually deployed

Crawled. A control path returned 404, so the inventory is reliable.

| Live | Notes |
|---|---|
| `/` · `/about` · `/blog` · `/contact` | Standard |
| **`/pricing`** | **A real page. The category leader publishes pricing** |
| **`/roles`** | A role directory — the demand-facing analogue of the graded bench |
| **`/reviews` → `/reviews/clients`** | **Client reviews get their own section**, not a homepage strip |
| `/candidates` · `/jobs` · `/talent` | **The supply side, on the same domain** |
| `/legal/privacy-policy` | Legal in a `/legal/` namespace |
| ❌ `/case-studies` `/faq` `/guarantee` `/terms` `/employers` | Do not exist as pages |

---

## 2. The homepage, in order

| # | Section | What to take from it |
|---|---|---|
| 1 | **Hero**: *"We recruit, vet, and place top 1% remote talent for 80% less than US equivalents."* | **A claim with a number in it.** Not an adjective |
| 2 | Stats immediately under the hero — 5,000+ companies, 11,000+ hires, $400M saved | Scale as the first proof |
| 3 | Client logos | |
| 4 | *"Why Choose Somewhere? Ask AI"* — links to ChatGPT, Claude, Gemini, Grok | Novel. Not for you yet |
| 5 | **Eight named candidates with their previous employers** | **The single most copyable idea on the page** — §3 |
| 6 | Popular categories, with candidate counts per category | Depth as proof |
| 7 | Services: Direct Hire, Talent On-Demand, Executive Search, **EOR**, Equipment | **EOR is sold as a named service**, which [`SCALE.md`](SCALE.md) §7 argued for |
| 8 | **5-step process**: Book Call → Meet Talent → Interview → Ongoing Support → Hire Globally | **Step one is a free call. No paid gate** — §4 |
| 9 | **Interactive savings calculator**, US vs offshore by role and level | **The second most copyable idea** — §3 |
| 10 | Popular roles with salary breakdowns | Feeds SEO and answers the money question |
| 11 | Who we serve — three buyer segments | |
| 12 | Testimonials | |
| 13 | **SOC2 · ISO27001 · GDPR badges** | Institutional trust signals |
| 14 | FAQ — four questions | |

**Primary CTA is *"Start Hiring"*, repeated throughout**, into a contact flow and a HubSpot booking
link. Secondary *"Find a Job"* for candidates sits in the top nav.

---

## 3. The four things worth stealing

| | |
|---|---|
| **Show the people early** | Eight named candidates with prior employers, high on the page. **This is the graded directory used as demand-side proof** — [`HUNGRY.md`](HUNGRY.md) §9's mechanism, deployed as a homepage section. Your version is stronger, because a recut ad with a **3-second and 15-second retention delta** is *falsifiable* and a headshot is not |
| **Build the calculator** | Theirs compares US vs offshore salary. **Yours should not** — that is the salary-arbitrage frame [`MODEL-V2.md`](MODEL-V2.md) §8 deliberately rejected. **Build a creative-volume calculator instead**: *how many cuts do you ship a month, what does your studio invoice, what would in-house cost.* It computes the **$5,000–16,500/mo vendor-invoice comparator** live, and it walks the buyer into the volume conclusion that [`TEARDOWN.md`](TEARDOWN.md) §4 says is the only conclusion that sells |
| **Put a number in the hero** | *"80% less than US equivalents"* is a claim you can argue with. **Yours is 4–13× against the studio invoice** — a bigger number against a better comparator |
| **Sell EOR as a named service** | Not an upsell buried in a pricing table. [`MODEL-V2.md`](MODEL-V2.md) gap 4 flagged that EOR is **37–65% of lifetime gross profit** and was being demoted to optional |

### And two things not to copy

**They lead on price.** *"80% less"* is a cost claim, and [`MODEL-V2.md`](MODEL-V2.md) §8 deliberately
flipped this business from price to quality — `TRUECLAIM` was V2's biggest win. **Competing with the
category leader on their own axis, with no track record, is the losing side of that fight.** Lead on
the graded work sample.

**Their process starts with a free call.** Yours starts with the **$500 paid teardown**. That is
worse for top-of-funnel volume and better for everything after it — it funds the search, filters
tyre-kickers, and is the work sample. Keep it.

---

## 4. Somewhere runs supply and demand on one domain — does that break our rule?

`/candidates`, `/jobs` and `/talent` are live, and *"Find a Job"* is in the top nav.
[`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §7 says keep supply footer-only and `noindex`. Both cannot
be right, so which is?

> **They are both right, because the channels are different.** Somewhere's visible strategy is
> **organic**: a large blog, salary guides, a role directory, category pages with candidate counts
> — all SEO surface area, and job pages are *excellent* SEO surface. **You are buying cold Meta
> traffic**, where a job-board shape risks reclassification into the **Employment Special Ad
> Category** — priced at a **10–29% CAC tax** in [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §2.

So the rule stands, and it is now better understood: **supply pages are an SEO asset and a paid-ads
liability.** Somewhere is paying no such tax because they are not buying the traffic. Publish
`/talent` when organic starts to matter — month three to six, exactly as scheduled.

---

## 5. What Meta specifically requires

Distinct from what converts. These are the things that, if missing, cost you money or an account.

### Before the first dollar

| | Why |
|---|---|
| **Facebook Page, with the username claimed** | You cannot run ads without a Page. It is the advertiser identity on every impression |
| **Business Manager with a clean structure** | A new advertiser, new domain, new Page, in a scrutinised category, **is the profile that gets restricted.** Separate BM, and a second ad account ready — [`ACTIVITIES.md`](ACTIVITIES.md) has this as a Tier-0 blocker |
| **Domain verified in Business Manager** | Required to control link editing and event configuration on your own domain |
| **Pixel installed and CAPI live, verified with test events** | Browser-only under-reports. **Every CAC number in [`LTGP.md`](LTGP.md) assumes conversions are attributed** |
| **A privacy policy at a real URL** | Ad review looks for it. Somewhere has one; Recruitify ships one, Funnelz does not |
| **UTMs and a naming convention** | Set before the first click or the data is never clean. **Cannot be retrofitted** |
| **Self-reported attribution on the form** | *"How did you hear about us?"* Once cold email runs alongside, platform numbers double-count |

### On the landing pages

| | Why |
|---|---|
| **Ads point at `/agencies` or `/ecommerce`, never `/`** | Message match, and **page review sees a buyer page with no route to job content** |
| **Promise and CTA above the fold on a 390×844 phone** | The one test that eliminates most templates |
| **Ad promise and page headline must match** | A mismatch is both a policy risk and the largest silent conversion killer |
| **No employment framing anywhere in the ad path** | No *"apply"*, no *"join our talent network"*, no job listings. `/talent` stays footer-only and `noindex` |
| **Fast** | The funnel carries an **85% LP-view rate**, and that is a page-weight number |
| **One conversion event per page** | The teardown purchase is the event worth optimising toward once volume allows; the form fill before that |

### The one that is easy to get wrong

**Do not let the site read as an employment offer.** It is not a rule you break loudly — it is a
reviewer glancing at a page with *"Find a Job"* in the nav and ticking Employment. That single tick
**removes lookalike audiences, which is 45% of the modelled spend**, and costs 10–29% on CAC.
Somewhere can afford that nav item. On a Meta-led launch, you cannot.

---

## 6. What this changes about the build

| | |
|---|---|
| **Add a creative-volume calculator to `/agencies`** | Not on the shortlist before. It is the highest-value custom block on the site — it does the teardown's job for free, at the top of the funnel |
| **Show graded people early on `/`** | A homepage section, not a page you click into |
| **`/pricing` as a real page** | The category leader publishes. Recruitify ships one; Funnelz would need it built |
| **Client reviews as their own section** | Somewhere gives them a URL. Cheap credibility for an operator with none |
| **Legal pages at real URLs before the first ad** | Ad review, and it is ten minutes |
| **Keep the paid teardown as step one** | The deliberate difference from the leader's funnel. It is the whole `TRUECLAIM` advantage made concrete |
