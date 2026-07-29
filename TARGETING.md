# TARGETING — Meet Them Mid-Search

Every previous targeting analysis asked *"which vertical's owners happen to browse Facebook?"*
That is the wrong question. The right one:

> **Which companies are, right now, actively trying to fill a remote role — and how do I put an ad
> in front of that specific person while they are still looking?**

A vertical is a *static* attribute. A job posting is a **dated intent signal with an expiry.**
Companies in-market for a remote bookkeeper are in-market for roughly 30–60 days. Reaching them in
that window is not interruption — it is arrival.

---

## 1. The mechanism

Meta cannot target "company that posted a remote bookkeeper job." But it does not have to. You
build the audience yourself:

```
1. SCRAPE      job boards for "remote <role>" postings by US companies
                    ↓ (company name, role, salary, date posted)
2. ENRICH      owner / hiring manager → personal email + mobile
                    ↓ (Apollo, Clay, Findymail, Prospeo)
3. UPLOAD      as a Meta Custom Audience — Meta matches to personal FB/IG accounts
                    ↓
4. RUN ADS     directly at people who are mid-search, right now
                    ↓
5. LOOKALIKE   1% lookalike off that seed → scale far beyond the scraped list
```

**Steps 1–4 solve intent. Step 5 solves scale.** The scraped list might be 2,000 companies; the
lookalike built from it can be millions of profiles who *resemble* people who hire remote
bookkeepers.

### What has to be true, and the honest uncertainty

| Requirement | Reality |
|---|---|
| Custom Audience minimum | ~100 matched users to activate; **1,000+ for a usable lookalike seed** |
| B2B email match rate | **Low — roughly 20–40%** [E]. Business emails often are not the Facebook login |
| **Mobile number match rate** | **Materially better than email** [E]. Prioritise phone enrichment |
| Practical implication | You need **~3,000–5,000 enriched contacts** to yield a ~1,000-match seed |
| Compliance | Meta requires the list be lawfully obtained with a lawful basis. Scraped public job posts plus commercial enrichment is standard practice, but the terms are yours to honour |

⚠️ **The match rate is the load-bearing assumption and it is [E], not [V].** Test it with one
2,000-contact upload before building anything on top of it. Meta shows you the matched size
immediately, so this is a same-day test.

---

## 2. Sources, ranked by intent

### Tier 1 — proven offshore buyers (highest intent that exists)

These people have already decided to hire offshore. There is no education left to do.

| Source | Why it is Tier 1 |
|---|---|
| **OnlineJobs.ph employer postings** | **2M+ worker profiles**; employers pay a flat monthly subscription to post [V]. Every poster is a US company paying money to hire Filipino staff. **The single highest-intent list in this business** |
| **Upwork job posts** filtered to the role + country preference | Public, dated, role-specific |
| **Competitors' live job boards** — Somewhere (`apply.workable.com/jobssomewhere`), Pearl Talent, Wing, MyOutDesk | Their open reqs are *their clients' unfilled roles*. Anonymised, but role, salary and often industry are visible |
| Facebook groups for offshore hiring — OnlineJobs.ph employers, "Hire Filipino VAs", e-comm hiring groups | Native Meta surface. You can engage *and* build audiences |

**The sharpest play in Tier 1:** companies that posted on OnlineJobs.ph or Upwork **and did not
fill the role.** A stale unfilled post is a frustrated buyer with proven offshore intent — the
warmest prospect available anywhere.

### Tier 2 — remote-role intent, offshore not yet decided

| Source | Note |
|---|---|
| **Accountingfly** | Accounting-specific remote job board. Exactly our role, exactly our intent |
| We Work Remotely · RemoteOK · Remotive · JustRemote · Working Nomads · FlexJobs | Remote-first boards; scrapeable |
| **Indeed** with the remote filter | Largest volume by far |
| LinkedIn Jobs (remote) · ZipRecruiter · Google Jobs | Volume, harder to scrape |

### Tier 3 — ICP fit, no hiring intent

Storeleads and BuiltWith for Shopify + A2X · Clutch for agencies · state registries. Useful for
cold email, **not** for Meta — a named list is not an audience.

---

## 3. What to actually run on Meta

Three layers, in the order you should build them:

| Layer | Audience | Expected volume | Expected CPL |
|---|---|---|---|
| **1. Intent seed** | Custom Audience from scraped job posters | Small — hundreds to low thousands | **Lowest** — they are mid-search |
| **2. Lookalike** | 1% lookalike off layer 1 | Millions | Low-mid |
| **3. Broad + hook** | Near-broad targeting, creative does the qualifying | Unlimited | Highest, but scales |

**Layer 3 deserves explaining, because it is counter-intuitive.** Meta's B2B interest targeting is
weak — "small business owner" is enormous and imprecise. But Advantage+ with near-broad targeting
plus a **hook that only one person responds to** works better than tight targeting. The creative
does the qualifying, not the audience.

### The hook has to name the moment, not the service

| ❌ Generic | ✅ Names the moment they are in |
|---|---|
| "Hire offshore accountants" | **"Still trying to fill that bookkeeper role?"** |
| "Save 70% on payroll" | **"Your bookkeeper posting has been up 6 weeks. We can fill it in 21 days."** |
| "Top 1% remote talent" | **"You posted for a remote bookkeeper. Here are three, graded, today."** |
| "Offshore staffing solutions" | **"$20,000/yr instead of $75,000. Same QuickBooks, same Xero, same close."** |

The second and third only work at scale if you have the intent list — which is the point of §1.
**On the intent seed you can be specific enough to feel like a coincidence.**

---

## 4. Where the signal is thickest

Not all role × vertical pairs post at the same volume. Ranked by how much scrapeable intent exists:

| Role posted remotely | Signal volume | Where it concentrates |
|---|---|---|
| **Bookkeeper / accountant** | **Very high** | OnlineJobs.ph, Accountingfly, Indeed, Upwork |
| Executive assistant / VA | **Highest of all** | OnlineJobs.ph dominates — but the role fails our gradeability gate |
| **AP / AR specialist** | **High** | Indeed, OnlineJobs.ph |
| Customer support | Very high | OnlineJobs.ph — fails our async gate |
| **Paid media / PPC specialist** | High | Upwork, agency boards |
| **Medical biller / coder** | High | Indeed, healthcare boards |
| Data entry | High | OnlineJobs.ph — fails our AI gate |
| Steel detailer / CAD | **Low** | Scarce postings. Buyers use engineering networks, not job boards |

> **The three that pass our gates AND have thick signal: bookkeeper/accountant, AP/AR specialist,
> paid media operations.** Everything with more signal fails a gate; everything that passes a gate
> more cleanly has thinner signal.

**And note what this does to the AEC question:** steel detailing kept scoring well on worker
economics and kept failing on buyer readiness. Here it fails again, for a new reason — **there is
almost no scrapeable hiring intent.** That is now three independent screens pointing the same way.

---

## 5. Verticals ranked on intent flow

Same lens applied to verticals. **This is a ranking of *flow*, not stock** — a vertical with 300,000
businesses that hires rarely generates less scrapeable intent than one with 20,000 that hires
constantly.

`FLOW` 25 · `REMOTE` 20 (do postings actually say remote) · `OFFSHORE` 20 (do they post on
OnlineJobs.ph / Upwork) · `IDENT` 15 (can you tell the vertical *from the posting*) · `PUBLIC` 12 ·
`STALE` 8 (share sitting unfilled 60+ days — the frustrated-buyer signal)

| # | Vertical | Score | `FLOW` | `REMOTE` | `OFFSHORE` | `IDENT` | `PUBLIC` | `STALE` |
|---|---|---|---|---|---|---|---|---|
| 1 | **E-comm / DTC** | **91.8** | 4 | 5 | 5 | 5 | 5 | 3 |
| 2 | **Marketing agency** | **88.8** | 4 | 5 | 5 | 4 | 5 | 3 |
| 3 | **Freight / trucking** | **84.8** | 4 | 4 | 5 | 4 | 5 | 3 |
| 4 | **Medical practice** | **83.4** | 5 | 3 | 4 | 4 | 5 | 4 |
| 5 | **Staffing agency** | **80.8** | 4 | 4 | 4 | 4 | 5 | 3 |
| 6 | Property mgmt | 76.8 | 4 | 3 | 4 | 4 | 5 | 3 |
| 7 | Dental / DSO | 76.0 | 4 | 2 | 4 | 4 | 5 | **5** |
| 8 | Insurance agency | 73.6 | 4 | 3 | 3 | 4 | 4 | **5** |
| 9 | MSP / IT services | 73.4 | 3 | 4 | 4 | 4 | 4 | 3 |
| 10 | Home services | 67.4 | **5** | **1** | 2 | 4 | 5 | 4 |
| 11 | PI law firm | 65.4 | 3 | 3 | 3 | 4 | 4 | 3 |
| 12 | SaaS | 64.8 | 3 | **5** | **2** | 3 | 4 | 2 |

### The `IDENT` dimension is new and it matters more than it looks

A posting that says *"Bookkeeper — QuickBooks"* tells you nothing about the vertical. One that says
*"Ecommerce Bookkeeper — Shopify, Amazon, A2X"* tells you everything. **Verticals whose postings
self-identify are targetable; verticals whose postings are generic are not** — you cannot segment
what you cannot label.

E-comm is the only vertical scoring 5 on `REMOTE`, `OFFSHORE` **and** `IDENT` simultaneously.

### What each result turns on

| Vertical | |
|---|---|
| **E-comm / DTC** | Postings literally contain the stack — Shopify, Amazon, A2X. Nothing else is this legible |
| **Marketing agency** | Hire offshore production constantly on Upwork; postings say *"our clients"* |
| **Freight / trucking** | Dispatch is already massively offshored — **but that role is gated on retention.** Their back-office flow is thinner than the headline suggests |
| **Medical practice** | **Highest raw flow of any qualifying vertical** — ~90k practices, high turnover — but postings usually assume on-site |
| **Staffing agency** | Post more than anyone, because posting *is* their business. Already use Indian sourcers |
| **Insurance agency** | ⭐ **Highest stale rate.** The 400,000-retirement shortage (PATTERN §3) means postings genuinely sit unfilled. **Warmest buyers, thinnest remote language** |
| **Home services** | ⚠️ **Highest raw flow of all twelve and the lowest remote language.** They are posting for technicians, not back office. This is the fourth independent screen to reject it |
| **SaaS** | Postings always say remote — but they do not use offshore boards, and **you cannot identify a SaaS company from a job posting.** `IDENT` 3 is what kills it |

### The tension this exposes

**Volume and readiness are inversely correlated at the extremes.**

| | Highest flow | Highest readiness |
|---|---|---|
| Home services | ✅ 5 | ❌ 1 |
| Medical practice | ✅ 5 | ⚠️ 3 |
| SaaS | ⚠️ 3 | ✅ 5 |
| **E-comm / DTC** | **4** | **5** | 

**E-comm wins by not being extreme on either.** That is a less exciting answer than a hidden gem,
but it is the correct one — and it is now the fourth independent method to select it.

---

## 5B. Top 5 verticals to target on Meta

§5 ranked **intent flow**. This ranks **Meta-workability** — a different question, because a
vertical can be full of in-market buyers who simply are not on Facebook.

`FB_NATIVE` 25 (does the *owner personally* live on FB/IG, not LinkedIn) · `IDENT` 20 (identifiable
from a job posting, which feeds the custom-audience seed) · `HEADLINE` 18 (can the pain fit in one
ad headline with no explanation) · `DECIDE` 15 · `AFFORD` 12 · `INTEREST` 10 (usable Meta
interest/behaviour signals as fallback)

| # | Vertical | Meta score | `FB_NATIVE` | `IDENT` | `HEADLINE` | `DECIDE` | `AFFORD` | `INTEREST` |
|---|---|---|---|---|---|---|---|---|
| **1** | **E-comm / DTC** | **100.0** | 5 | 5 | 5 | 5 | 5 | 5 |
| **2** | **Marketing agency** | **88.0** | 5 | 4 | 4 | 5 | 4 | 4 |
| **3** | **PI law firm** | **83.4** | 4 | 4 | 4 | 5 | **5** | 3 |
| **4** | **Insurance agency** | **81.6** | 4 | 4 | **5** | 4 | 4 | 3 |
| **5** | **Medical practice** | **81.2** | 4 | 4 | **5** | 4 | 3 | 4 |
| 6 | Freight / trucking | 78.2 | 4 | 4 | 4 | 5 | **2** | 4 |
| 7 | Property mgmt | 70.6 | 3 | 4 | 4 | 4 | 3 | 3 |
| 8 | Staffing agency | 69.0 | **2** | 4 | 4 | 5 | 4 | 2 |
| 9 | MSP / IT services | 65.4 | **2** | 4 | 3 | 5 | 4 | 2 |
| 10 | SaaS | 54.2 | **2** | 3 | **2** | 3 | 5 | 2 |
| — | *Home services* | *89.2* | 5 | 4 | 5 | 5 | 3 | 4 | ⛔ not remote-ready |
| — | *Dental / DSO* | *84.2* | 4 | 4 | 5 | 5 | 3 | 4 | ⛔ not remote-ready |

**Home services would rank #2 on Meta-workability alone** — the best Facebook buyer in the entire
set. It stays excluded only on the remote-readiness gate, and that is the single most frustrating
result in this whole analysis: the easiest buyer to *reach* is the hardest to *convert*.

### The demographic inversion

> **Facebook's strongest US demographic is 45–65. The insurance workforce averages mid-50s, with
> one in four underwriters over 50** (PATTERN §3). **The aging that creates the shortage also makes
> those owners more Facebook-reachable, not less.**

I had scored insurance `META` = 3 across three earlier documents. On demographics it is a **4**, and
that moves it from 8th to 4th here.

The inverse holds too: **SaaS founders are the youngest buyer in the set and the least
Facebook-reachable.** Young B2B buyer → LinkedIn. Old B2B buyer → Facebook. That is the opposite of
the intuition that "modern" verticals are easier to reach on modern channels.

### The real Meta test is the headline

Meta gives you one line and one image. **If the value proposition needs a second sentence, the
vertical fails regardless of its score.**

| Vertical | The one line |
|---|---|
| **E-comm / DTC** | *"Your bookkeeper costs $75k. Ours is $20k and already knows Shopify + A2X."* |
| **Marketing agency** | *"Your margin is people. Move the back office, keep the creatives."* |
| **PI law firm** | *"Your paralegal is chasing medical records instead of settling cases."* |
| **Insurance agency** | *"Your CSR retired. Nobody applied. We have three, starting in 21 days."* |
| **Medical practice** | *"Your front desk loses 3 hours a day to insurance verification."* |
| SaaS | ⚠️ Needs a second sentence. That is why it scores 2 |

**Insurance has the strongest single line in the set**, because the shortage is so acute that the ad
can simply describe their situation back to them.

### 5C. Facebook and Instagram are not the same audience

§5B collapsed both into one `FB_NATIVE` score. That was wrong, because the platforms have nearly
opposite age profiles: **Facebook is strongest 45–65 in the US; Instagram is strongest 18–44, peaking
25–34.** Requiring *both* is a real constraint, and it narrows the field hard.

You are only reachable on both platforms **as much as your weaker one**, so the score below uses the
minimum, not the average.

| Vertical | Owner age | FB | IG | Visual-native creative | **Both** | Score |
|---|---|---|---|---|---|---|
| **Marketing agency** | 28–45 | 5 | **5** | 5 | **5** | **100.0** |
| **E-comm / DTC** | 25–45 | 5 | **5** | 5 | **5** | **100.0** |
| *Dental / DSO* | 35–55 | 4 | 3 | 4 | 3 | *69.0* ⛔ |
| Medical practice | 35–55 | 4 | 3 | 3 | 3 | 66.0 |
| *Home services* | 35–60 | **5** | 2 | 3 | 2 | *61.0* ⛔ |
| PI law firm | 35–60 | 4 | 2 | 2 | 2 | 52.0 |
| Freight / trucking | 35–55 | 4 | 2 | 2 | 2 | 52.0 |
| SaaS | 28–45 | 2 | 3 | 3 | 2 | 49.0 |
| Property mgmt | 40–60 | 3 | 2 | 2 | 2 | 46.0 |
| Staffing agency | 35–55 | 2 | 2 | 2 | 2 | 40.0 |
| **Insurance agency** | **50–60** | **4** | **1** | 1 | **1** | **38.0** |
| MSP / IT services | 35–55 | 2 | 1 | 1 | 1 | 26.0 |

**Only two verticals clear a both-platforms requirement: marketing agencies and e-commerce.**
Everything else is Facebook-only, Instagram-lean, or neither.

### This reverses what I said one section ago about insurance

In §5B I promoted insurance from 8th to 4th on the Facebook demographic — mid-50s owners are
Facebook-native. **That was right about Facebook and wrong about Meta.**

> A 55-year-old insurance agency owner is **FB 4 / IG 1.** The same demographic that makes them
> Facebook-reachable makes them Instagram-unreachable. Under a both-platforms requirement insurance
> drops to **11th of 12.**

The pattern generalises: **the both-platforms requirement selects for buyers aged roughly 25–45.**
That is e-commerce founders and agency owners, and essentially nothing else in this set.

### Why "both" is the right default anyway — it is a CPM argument, not a reach argument

| | |
|---|---|
| **Inventory** | Restricting to FB-only shrinks the auction pool → **higher CPM** |
| **Reels** | Currently the cheapest impression on the platform, and it is Instagram-native |
| **Advantage+** | Performs better with placements unrestricted |
| **Creative velocity** | More placements = more variants tested per dollar |
| **The cost** | If the buyer genuinely is not on Instagram, unrestricted placements waste spend |

So the requirement is a **good default rather than a hard law.** For e-comm and agencies, run
unrestricted and take the cheap Reels inventory. For insurance or freight, if you ever test them,
**restrict to Facebook placements and accept the higher CPM** — do not let Advantage+ spray
Instagram at a 55-year-old agency principal.

### What Instagram-native creative has to look like

Instagram punishes static banners. A "save 70% on payroll" image will not work in Reels. What does:

| Format | The creative |
|---|---|
| **Founder to camera, 15s** | *"Here's what a $20,000-a-year accountant's work actually looks like."* Then show it |
| **Screen recording** | The graded work-sample test being scored — reconciliation right vs wrong, on screen |
| **Before / after** | Close timeline: 3 weeks → 4 days. One number, animated |
| **Carousel** | Three real candidate profiles with test scores, swipeable |

**The graded work sample is unusually good Instagram creative**, which is a genuine and lucky
alignment — the thing that differentiates the offer is also the thing that films well.

### How this squares with §5

| | Intent flow (§5) | Meta workability (§5B) |
|---|---|---|
| **E-comm / DTC** | **1st** | **1st** |
| **Marketing agency** | **2nd** | **2nd** |
| Freight / trucking | 3rd | 6th — `AFFORD` = 2 kills it |
| Medical practice | 4th | 5th |
| Staffing agency | 5th | **8th** — not on Facebook |
| Insurance agency | 8th | **4th** — the demographic correction |
| PI law firm | 11th | **3rd** — rich, owner-led, Facebook-active |

**E-comm and marketing agencies are 1st and 2nd on both.** Everything else moves, which means those
two are the only verticals selected by *both* the intent lens and the channel lens.

**Launch on those two. Test insurance and PI law third** — both are far better Meta prospects than
their intent-flow rank suggested, and PI law firms have the deepest pockets of any buyer in the set.

---

## 5D. Which ROLES can be sold in a Meta ad

A separate question from "which role is a good business." On Meta you have one line and one second.

`LEGIBLE` 22 (does the owner know what this role *is*, instantly) · `OWNER_PAIN` 20 (does the
**owner** personally feel its absence, not a manager) · `ONE_LINE` 18 · `BIG_NUMBER` 15 (is the
saving a large round number) · `SHOWABLE` 15 (can you demonstrate it in a 15-second Reel) ·
`LOW_RISK` 10 (can the owner imagine handing it over without fear)

| # | Ad-facing name | Internal role | Score | `LEG` | `PAIN` | `LINE` | `NUM` | `SHOW` | `RISK` |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **"Bookkeeper"** | Bookkeeping / reconciliation | **96.0** | 5 | 5 | 5 | 5 | 5 | 3 |
| **2** | **"Accountant"** | Ledger & Close | **93.0** | 5 | 5 | 5 | 5 | 4 | 3 |
| **3** | **"Ads manager"** | Paid Media Operations | **91.0** | 5 | 5 | 5 | 4 | 5 | **2** |
| 4 | *"Executive assistant"* | EA | *86.0* | 5 | 5 | 5 | 4 | **2** | 4 | ⛔ gradeability |
| **5** | **"Someone to chase your invoices"** | AR & Collections | **84.6** | 4 | 5 | 5 | 3 | 4 | 4 |
| 6 | "Email marketer (Klaviyo)" | Email / Lifecycle Ops | 80.0 | 4 | 4 | 4 | 3 | 5 | 4 |
| 7 | "Inventory & margin analyst" | Inventory & COGS | 79.6 | 3 | 5 | 4 | 4 | 4 | 4 |
| 8 | *"Customer support rep"* | Customer support | *79.4* | 5 | 4 | 4 | 4 | 3 | 3 | ⛔ async |
| 9 | "Dashboards analyst" | Reporting & Analytics | 74.0 | 3 | 4 | 3 | 3 | 5 | **5** |
| 10 | "Someone to pay your bills" | AP & Invoice Processing | 73.0 | 4 | **3** | 4 | 3 | 4 | 4 |
| 11 | "Payroll person" | Payroll processing | 70.4 | 5 | 3 | 4 | 3 | 3 | **2** |
| 12 | "Compliance / paperwork person" | Compliance & Doc Ops | **48.0** | **2** | 3 | **2** | **2** | **2** | 4 |

### This contradicts my own skill model, and the contradiction is instructive

| Internal role | Rank on skill model | Rank on Meta-sellability |
|---|---|---|
| Bookkeeping / reconciliation | 3rd | **1st** |
| Ledger & Close | 9th | **2nd** |
| AR & Collections | 2nd | 5th |
| Reporting & Analytics | 4th | 9th |
| **AP & Invoice Processing** | **1st** | **10th** |
| **Compliance & Document Ops** | 7th | **12th** |

> **The roles that score best analytically have the worst ad legibility.** "AP & Invoice Processing"
> was my #1 skill. No business owner has ever thought that phrase. "Compliance & Document Ops" is
> nearly unsellable on Meta — `LEGIBLE` 2, `ONE_LINE` 2, `SHOWABLE` 2.
>
> Meanwhile **"bookkeeper" is the most legible finance role in existence** and it only came 3rd
> analytically.

### The resolution: the ad-facing name and the internal spec do not have to match

**Sell "bookkeeper" or "accountant." Scope the actual seat on the intake call.**

That is not a trick — it is how the buyer already thinks. An e-commerce founder does not think *"I
need an AR & Collections specialist."* They think *"I need someone to do my books."* You meet them
at their language, then discover on the call whether what they actually need is reconciliation, AR,
or a full close.

| Ad says | Intake discovers | You place |
|---|---|---|
| "Bookkeeper, $20k not $75k" | *"Actually my books are fine, it's the unpaid invoices"* | AR & Collections |
| "Bookkeeper, $20k not $75k" | *"I need month-end closed properly"* | Ledger & Close |
| "Bookkeeper, $20k not $75k" | *"I can't see per-SKU margin"* | Inventory & COGS |

**One ad, one legible promise, three sellable seats behind it.** This also fixes the bench-utilisation
problem from BEACHHEAD §0.2 — you are not committing the ad to the least-portable role.

### Two roles with a specific Meta problem

**"Ads manager" scores 91 but `LOW_RISK` = 2.** Owners are frightened of handing an ad account to a
stranger from an ad. It is the third most sellable role and the hardest to close. If you run it,
lead with a **read-only audit** rather than access.

**"Payroll person" has `LOW_RISK` = 2 for the same reason** — payroll errors are visible, personal
and legally messy. Legible but scary.

### What this means for creative

The `SHOWABLE` column is the Instagram/Reels column, and it re-orders things again:

| Best Reels material | Why |
|---|---|
| **Bookkeeper** (5) | Screen-record a broken reconciliation being fixed |
| **Ads manager** (5) | Screen-record a messy campaign structure being rebuilt |
| **Email marketer** (5) | Show a flow build and the revenue attribution |
| **Dashboards analyst** (5) | The output *is* a visual |
| Executive assistant (2) | Nothing to show. Talking heads only |
| Compliance ops (2) | Nothing to show |

**Bookkeeper is the only role scoring 5 on both `LEGIBLE` and `SHOWABLE`** — instantly understood
*and* filmable. That is the rare combination, and it is why it wins.

---

## 6. The measurement protocol — replace every estimate above in one afternoon

**Every score in §5 is `[E]`.** None of it needs to stay that way. Public job boards expose result
counts, so all of it is directly countable:

| What to measure | How |
|---|---|
| **Raw remote flow per role** | Indeed → `"remote bookkeeper"` · `"remote accounts receivable"` · `"remote AP specialist"` → read the result count |
| **Vertical-tagged flow** | Indeed → `"remote bookkeeper"` + `Shopify` / `agency` / `MSP` / `AppFolio` / `Applied Epic` / `Bullhorn` |
| **Proven offshore intent** | **OnlineJobs.ph employer feed** → same role keywords. Every result is a paying offshore buyer |
| **Upwork intent** | Upwork job search → role + long-term + country-preference filters |
| **Competitor client demand** | `apply.workable.com/jobssomewhere` → count open reqs by role. **These are Somewhere clients hiring right now** |
| **Stale rate** | Same Indeed query filtered to 30+ days old ÷ total = the frustrated-buyer share |
| **Accounting-specific** | Accountingfly → remote roles, tagged e-comm vs firm vs practice |

**Cost: one afternoon. Output: real `FLOW`, `REMOTE`, `OFFSHORE` and `STALE` numbers per vertical.**

This is the cheapest high-value research left in the plan, and it converts the entire §5 table from
estimate to fact. Do it before the match-rate test, because it tells you *which* 2,000 companies to
enrich.

---

## 7. What this changes

| # | Change |
|---|---|
| 1 | **The seed audience is a scraping and enrichment problem, not a media-buying problem.** The first build is a job-post scraper plus an enrichment pipeline, not an ad account |
| 2 | **OnlineJobs.ph is the highest-intent source available** and it is not a competitor — it is a directory of proven offshore buyers |
| 3 | **Competitors' job boards are prospect lists.** Somewhere's open reqs are their clients' unfilled roles |
| 4 | **Stale unfilled postings are the warmest segment in the business.** Proven intent plus proven frustration |
| 5 | **`META` as a vertical score matters less than I claimed.** With a custom-audience seed you are targeting *people*, not verticals — so MSP, SaaS and staffing agencies come back into play despite living on LinkedIn |
| 6 | **Test the match rate first.** One 2,000-contact upload, same-day answer. Everything else depends on it |

**Point 5 is the important one.** I gated three verticals out on Meta-targetability. That gate was
right when the plan was interest-based targeting and wrong now — a custom audience built from job
postings does not care whether the owner's *interests* look B2B, only whether their phone number
matches a Facebook account.
