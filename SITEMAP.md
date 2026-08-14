# The Full Sitemap

Every page `allhandstalent.com` will ever need, when it appears, and why it earns a URL.
[`MINIMUM.md`](MINIMUM.md) is the first four rows of this.

**The rule, applied throughout:** a page exists to own a URL — an ad destination, a legal document,
a conversion trigger, or a link sent externally. Anything else is a block on a page that already
exists.

---

## The list

| # | Path | What | When | Index | In ad path | Why it needs a URL |
|---|---|---|---|---|---|---|
| **1** | **`/`** | Thin homepage — 4 blocks | **Launch** | index | no | Someone about to send $500 types the domain. **It cannot 404** |
| **2** | **`/agencies`** | Ad destination, ICP 1 | **Launch** | index | **yes** | Ads must never point at `/`. Message match, and page review sees a buyer page |
| **3** | **`/thanks`** | Form submitted → booking embed | **Launch** | **noindex** | yes | **The conversion event fires here.** Without a distinct URL you measure nothing |
| **4** | **`/privacy`** | Privacy policy | **Launch** | index | no | **Meta ad review looks for it** |
| **5** | **`/paid`** | Teardown purchased — Stripe success URL | **Launch** | **noindex** | yes | **A different, more valuable conversion event than a form fill.** Same reason as #3: separate URL or you cannot tell them apart |
| **6** | `/guarantee` | 12-month replacement, terms in full | Week 2 | index | no | **A bullet reads as marketing; a page reads as a commitment.** Cheapest differentiation you have |
| **7** | `/proof` | Recuts with 3s/15s retention deltas | **~3 recuts** | index | no | **The most important page on the site.** Block on the LP until there are three |
| **8** | `/terms` | Terms of service | Week 3–4 | index | no | Once money moves and contracts flow |
| **9** | `/access` | **How you handle their ad-account access** | Week 3–4 | index | no | **Differentiating, and nobody expects it.** Answers the scariest thing in the transaction, where Somewhere uses SOC2 badges you cannot claim |
| **10** | `/ecommerce` | Ad destination, ICP 2 | **After #2 has data** | index | **yes** | Second ICP. Not at launch — two pages halves Meta's signal |
| **11** | `/pricing` | Fee structure, EOR as a named service | Month 2 | index | no | The category leader publishes. Becomes a page when people ask for a link |
| **12** | `/faq` | Objection handling | Month 2 | index | no | Block on the LP first. A page once you have repeated questions from real calls |
| **13** | `/about` | You — named, with a face | Month 2 | index | no | Founder block goes on `/` at launch; a page when there is more to say than a paragraph |
| **14** | `/contact` | Form + email | Month 2 | index | no | An email in the footer until that stops being enough |
| **15** | `/refunds` | What happens to the $500 if the search stalls | Month 2 | index | no | States it before someone has to ask |
| **16** | `/agencies-b`, `-c` … | **LP variants** | Ongoing | **noindex** | **yes** | **Never a variant of `/`.** Duplicate-and-edit; noindex so they never compete in search |
| **17** | `/talent` | Supply — application | **Month 3–6** | **noindex** | **never** | **Off-site form until then** ([`MINIMUM.md`](MINIMUM.md) §8). Moves on-site only when you want the SEO |
| **18** | `/blog` + `/blog/[slug]` | CMS collection | Month 3–6 | index | no | The organic surface. Needs a CMS, not hand-built pages |
| **19** | `/proof/[slug]` | Individual recut entries | **~10 recuts** | index | no | When `/proof` outgrows one page. **This is the CMS trigger** |
| **20** | `/roster` | **The graded directory, gated** | Month 4–6 | **noindex** | no | Supply shown *to buyers*, behind the deposit — a proof asset, not a job board. Somewhere's `/roles` equivalent |
| **21** | `/referral` | Referral programme | Month 4–6 | index | no | Somewhere runs one. Only once there are clients to refer |
| **22** | `/case-studies` | Client outcomes | Month 6 | index | no | **Real ones only.** Distinct from `/proof`: proof is craft, case studies are business outcomes |
| **23** | `/designers`, `/motion` … | Ad destinations for **role two** | Month 6+ | index | **yes** | One LP per role × ICP as you expand. This is where the count grows |
| **24** | `/404` | Custom 404 | Week 2 | noindex | no | Ten minutes. Catches typos and dead links into a CTA |

---

## Counts, so the scale is clear

| Milestone | Live pages | Note |
|---|---|---|
| **Launch** | **5** | Rows 1–5 |
| End of month 1 | ~9 | + guarantee, proof, terms, access |
| End of month 3 | ~15 | + second ICP, pricing, FAQ, about, contact, refunds, variants |
| Month 6 | ~20–24 | + talent, blog, roster, referral, case studies, role-two LPs |

**Fewer than 25 pages, ever**, until you add roles or countries. That is why the template's page
count mattered less than it seemed and its **CMS** mattered more — rows 18, 19 and 22 are collections,
and the other twenty are hand-built once.

---

## Two things this list makes visible

**The ad path is four URLs, not twenty.** `/agencies`, `/ecommerce`, their variants, `/thanks` and
`/paid`. **Everything Meta reviews, and every page whose speed affects the 85% LP-view rate, is in
that short list.** The other twenty pages can be as slow and as long as you like.

**`/paid` was missing from every earlier version of this.** A form fill and a $500 purchase are
different events with different values, and if they share a URL you cannot optimise toward the one
that matters. It costs nothing to split them at launch and cannot be retrofitted cleanly.

---

## The 14 you actually need, and what produces each

Scope confirmed: rows 1–10, plus `/about`, `/contact`, `/talent`, `/404`.

**The finding, before the table: only one of the fourteen is built from blank.**

| # | Page | Source | Effort |
|---|---|---|---|
| 1 | **`/`** | **Recruitify homepage** — edit copy | template |
| 2 | **`/agencies`** | **Built from blank**, reusing the template's components | **the only real build** |
| 3 | `/ecommerce` | **Duplicate `/agencies`**, swap the ICP language | ~20 min |
| 4 | `/thanks` | Build — headline, next steps, Cal.com embed | ~15 min |
| 5 | `/paid` | **Duplicate `/thanks`**, different copy + conversion event | ~5 min |
| 6 | `/privacy` | **Recruitify `/privacy`** — replace the text | ~10 min |
| 7 | `/terms` | **Recruitify `/terms`** — replace the text | ~10 min |
| 8 | `/guarantee` | **Duplicate `/privacy`'s layout** | ~20 min |
| 9 | `/access` | **Duplicate `/privacy`'s layout** | ~20 min |
| 10 | `/talent` | **Duplicate `/privacy`'s layout** + form embed | ~20 min |
| 11 | `/proof` | **Recruitify `/projects`** — adapt to recut + retention | template |
| 12 | `/about` | **Recruitify `/about`** — edit | template |
| 13 | `/contact` | **Recruitify `/contact`** — edit | template |
| 14 | `/404` | **Framer's built-in** | ~5 min |

| Source | Pages |
|---|---|
| **Comes with Recruitify** | **5** — `/`, `/proof`, `/about`, `/contact`, `/privacy` + `/terms` |
| **Duplicate an existing text page and change words** | **4** — `/guarantee`, `/access`, `/talent`, `/paid` |
| **Duplicate the LP** | **1** — `/ecommerce` |
| **Framer built-in** | **1** — `/404` |
| **Genuinely built** | **2** — `/agencies` and `/thanks`, and `/thanks` is fifteen minutes |

> **So the template covers five, duplication covers six, Framer covers one, and you build `/agencies`.**
> Roughly a day of work after the template is remixed — and **`/agencies` is where the whole day
> should go**, because it takes 100% of the paid traffic.

---

## Should you buy a second template just for `/agencies`?

I checked, because it is the page that matters and I had never searched single-page landing-page
templates. Candidates: **[Pace](https://pace.framer.media/)** (verified live), Assemble, Shiftium,
LanX.

**Pace is the best of them and it still does not earn the money.** Its section order is close —
hero → *Headaches* (problem) → solution → features → pricing → testimonials → FAQ → repeated CTA.
But:

| | |
|---|---|
| **No metrics or results block** | So the **recut with 3-second and 15-second retention** — block 3, *the business* — is built regardless |
| **No calculator** | So the **volume calculator** — block 2, and the highest-value custom block on the site — is built regardless |
| **No comparison table** | So the objection block is built regardless |
| **SaaS register**, priced at $19/$49 monthly tiers | Full rewrite, and it would sit beside a recruitment-register site |
| **A second design system to reconcile** | Two templates in one project means two type scales and two colour systems |

> **The three blocks a landing-page template cannot give you are the three that make this page
> different from every other page on the internet.** What is left — hero, testimonials, FAQ, repeated
> CTA — you already have in Recruitify's components.

**Build `/agencies` from blank in Recruitify's design system.** One template, one purchase, one type
scale.

---

## What this settles

The template question absorbed several rounds and the answer is smaller than it looked:

**One template. One page built from scratch. Everything else is duplicate-and-edit.**

That is also why `STABLE` deserved cutting to 8 and why the CMS mattered more than the page count —
you are not depending on the template for structure, you are depending on it for **a design system
and five pages of head start.**

---

## Seven templates against the 14-page requirement

All page counts below are **crawled**, with a control path returning 404 on every site. The metric
is not "how many pages does it ship" — it is **how many of your fourteen you end up building from
blank**, because eight of the fourteen are duplicate-and-edit *from a page you already have*.

**Which makes one thing decisive that nobody would guess: whether it ships a legal page.** `/privacy`
is the donor layout for `/terms`, `/guarantee`, `/access` and `/talent`. A template without one costs
you five pages, not one.

| | Template | Covers of 14 | **Real builds** | Verified |
|---|---|---|---|---|
| **1** | **Recruitify** | **6** — `/`, `/about`, `/contact`, `/privacy`, `/terms`, `/projects`→`/proof` | **2** | 8 URLs live |
| **2** | Conversion | 4 — `/`, `/about`, `/contact`, `/blog`→`/proof` | **4** | 4 URLs live |
| **3** | Cubicles | 4 — same as above | **4** | 4 URLs live |
| **4** | Funnelz | 2 — `/`, `/blog`→`/proof` | **5** | 2 URLs live |
| **5** | Recruitment Hub | 2 — `/`, `/contact` | **5** | 1 sub-page |
| **6** | Recruitment (Shah) | 1 — `/` | **6** | **single page** |
| **7** | Pace | 1 — `/` | **6** | **single page** |
| — | HRPro | — | — | **`hrpro.framer.website` does not resolve. Unverifiable** |

---

### 1. Recruitify — 2 real builds

**Pros** · Ships **both legal pages**, so `/guarantee`, `/access` and `/talent` are duplicates rather
than builds · Only template with a real `/projects` to become `/proof` · Its process section is
*already* Consultation → Screening → Placement · Employer-facing recruitment register, so almost no
restyling · Bonus `/faq` and `/pricing` you do not even need yet.
**Cons** · **No `/blog`, so no CMS** — the trigger at ~10 recuts is an afternoon you will owe later ·
Creator (Framify) has no establishable track record · Price and bundle both unconfirmed.

### 2. Conversion — 4 real builds

**Pros** · **The best conversion architecture found** — Results metrics block, comparison table,
3-step process · Longest-running template on the marketplace, the only real longevity signal.
**Cons** · **No legal pages**, so five text pages start from blank · Its `/blog` ships **broken
placeholder links including a literal `404`** · **Reads as an ads agency, not a talent firm** — a
register problem your buyer will notice because they *are* an ads agency.

### 3. Cubicles — 4 real builds

**Pros** · Corporate-consultancy register, the most institutionally credible of the set · Real
blog/CMS · Cheapest paid option.
**Cons** · `CONVERT`=2 — **a brochure, not a funnel.** Weak repeated CTA, no pricing, no objection
block · No legal pages · Generic consulting copy.

### 4. Funnelz — 5 real builds

**Pros** · **The only CMS-shaped blog** — dated, categorised, authored, individual URLs · Booking
already in the nav · Most complete *homepage* section set: case studies, pricing tiers, testimonials,
team · Creator **Ramish Aziz has 18 published templates**, the strongest support signal available.
**Cons** · **Two URLs total.** Its pricing, team and case studies are homepage sections, so they
donate nothing to your page count · **No legal page**, so five text pages start from blank ·
Funnel-agency voice — cosmetic, but it is a full rewrite.

### 5. Recruitment Hub — 5 real builds

**Pros** · **Free** · Good persuasion order — why-us comparison, 3-step process, pricing, FAQ · Right
employer-facing register.
**Cons** · **One sub-page.** Everything else was a homepage anchor · No CMS, no case studies, no legal
pages · Free means **no 3-month Pro bundle**, so it is not the cheapest path.

### 6. Recruitment (Shah) — 6 real builds

**Pros** · Free · Recruitment register.
**Cons** · **Crawled: a single page.** Donates a homepage and nothing else.

### 7. Pace — 6 real builds

**Pros** · Purpose-built landing page, conversion-ordered, repeated CTA, problem-framing section.
**Cons** · **Single page, crawl-confirmed** · **No metrics block, no calculator, no comparison
table** — the three blocks that make `/agencies` different are absent · SaaS register at $19/$49
tiers · A second design system to reconcile.

---

## The verdict, and what actually separated them

**Recruitify, on two real builds against four to six for everything else.** The gap is not taste and
it is not design quality — it is that **it ships `/privacy` and `/terms`, and those two pages are the
donor layout for four more.**

> **Nobody would have picked a template on whether it has a privacy page.** It fell out of listing
> the fourteen pages and asking what produces each — which is the only reason it is visible at all.

Its one real cost is the missing CMS, and that is a known, dated, affordable debt: **an afternoon at
around ten recuts**, not a rebuild. Funnelz wins that dimension and loses four others.

**Still run the phone test before paying** — it is the one check I cannot run, and `MOBILEHERO` is
the only criterion that can override everything above.

---

## Requirements, in priority order

Everything this repo has accumulated about the site, ranked by **what it costs you if it is wrong**
rather than by how much it was discussed.

### Tier A — binary. Get one wrong and the others stop mattering

| | Requirement | Cost of getting it wrong |
|---|---|---|
| **1** | **Employer-facing shape.** Not a candidate job board | **A 10–29% CAC tax, permanently** — Meta's Employment Special Ad Category deletes lookalikes, which is 45% of modelled spend |
| **2** | **Promise + CTA above the fold on a 390×844 phone** | **Everything else on the page is irrelevant** if nobody sees the ask. And it looks perfect on your laptop |
| **3** | **Page speed on 4G** | The funnel carries an **85% LP-view rate**. Lost at the very top, before a word is read |

**Only #1 is checkable from here.** #2 and #3 require your phone on mobile data — which is why the
20-minute test outranks every score in this repo.

### Tier B — expensive to add, cheap to inherit

| | Requirement | Why it sits here |
|---|---|---|
| **4** | **A legal page that can act as a donor layout** | Gates ad approval *and* **donates four more pages** — `/terms`, `/guarantee`, `/access`, `/talent` |
| **5** | **A proof structure that can hold numbers** | Block 3 *is* the business. Index + detail pages, with room for a retention delta |
| **6** | **Repeated CTA and an objection block** | Cold traffic needs persuasion architecture. Mobile users do not scroll back up |
| **7** | **Clean components and one type scale** | Determines the edit cost of everything else, forever |

### Tier C — deferred, dated, or noise

| | Requirement | Why it is not urgent |
|---|---|---|
| **8** | **CMS** | A **dated debt** — an afternoon, at around ten recuts. Not a rebuild |
| **9** | `/pricing`, `/faq` as pages | **Not in the fourteen.** Blocks until someone asks for a link |
| **10** | Register, cost, bundle, creator support | **Below the noise floor.** Copy is free, $79 is one hour of your time, and Framer has no upstream to break |

---

## The seven, re-read against that order

`/projects` opened and read, because the recommendation depended on two things I had only assumed.

| | Tier A shape | Tier B legal donor | Tier B proof structure | Tier B conversion |
|---|---|---|---|---|
| **Recruitify** | **5** — employer recruitment | **5 — the only one** (`/privacy` + `/terms`) | **4** — `/projects` with **individual detail pages** | 4 |
| Recruitment Hub | **5** | 0 | 0 | 4 |
| Funnelz | 4 | 0 | 4 — case studies + CMS blog | **5** |
| Cubicles | 4 | 0 | 3 | 2 |
| Recruitment (Shah) | 4 | 0 | 0 | 3 |
| Conversion | 3 — **reads as an ads agency** | 0 | 3 — **metrics block, no detail pages** | **5** |
| Pace | 2 — SaaS product | 0 | 0 | 4 |

### What reading `/projects` actually changed

**Confirmed:** four items, each linking to **its own detail page** at `/projects/[slug]`. That is
index-plus-detail — exactly the shape `/proof` needs, and the reason it can absorb recut write-ups.

**Corrected:** the items carry **narrative testimonials, not numbers.** *"Perfect match", "game-
changer"* — qualitative. So **the metrics treatment gets built either way**, and my earlier
"adapt `/projects` → `/proof`" was half right: you inherit the structure, not the numbers.

> **And that splits the two best templates neatly: Recruitify gives you the `/proof` skeleton;
> Conversion gives you the metrics *design*.** Neither gives both. Build the numbers treatment inside
> Recruitify's grid, modelled on Conversion's Results block.

---

## Closing the template question

**Recruitify.** It is first on Tier A's only checkable item, **alone on the single most valuable Tier
B item**, and its one loss is Tier C.

| | |
|---|---|
| **Wins Tier A** | Employer-facing recruitment shape, which is the one binary requirement I can verify |
| **Wins Tier B outright** | **The only template of seven that ships a legal page** — and that page is the donor for four more. Plus an index-and-detail proof structure |
| **Loses Tier C** | No CMS. **A known, dated, one-afternoon debt at ~10 recuts** |

**Further template research has hit diminishing returns.** Seven demos crawled, six read, and the two
requirements that outrank everything left — mobile hero and 4G speed — **cannot be checked from here
at all.** The remaining differences between Recruitify, Funnelz and Conversion sit in Tier C.

**Buy Recruitify, run the phone test on it first, and if the hero fails, fall back to Recruitment Hub
— free, same shape, and you build four more pages.**

---

## Recruitify vs Funnelz, head to head

Both crawled, both read across multiple pages. They are close, and **they excel at different things
— which turns out to be the whole answer.**

### Where Recruitify excels

| | | Evidence |
|---|---|---|
| **1** | **Page structure — 8 URLs against 2** | Crawled: `/`, `/about`, `/services`, `/pricing`, `/faq`, `/projects`, `/contact`, `/privacy`, `/terms` |
| **2** | **The donor layout** | **Verified by opening it.** `/privacy` is a **styled 6-section policy page with headings and shared nav and footer** — not a wall of text. It is genuinely reusable for `/terms`, `/guarantee`, `/access` and `/talent`. **This one page is worth four** |
| **3** | **Shape and register** | Employer-facing recruitment. Its process section is **already Consultation → Screening → Placement** |
| **4** | **Proof structure** | `/projects` is an index with **individual detail pages** at `/projects/[slug]` — the shape `/proof` needs |
| **5** | **Legal pages ship** | Which Meta's ad review looks for, and which nothing else on the shortlist has |
| **6** | **Two bonus pages** | `/pricing` and `/faq` — not in your fourteen, but they are rows 11 and 12 and arrive free |

### Where Funnelz excels

| | | Evidence |
|---|---|---|
| **1** | **The only CMS** | Blog posts carry **dates, categories, authors and individual URLs**. Recruitify has no `/blog` at all |
| **2** | **Booking already in the nav** | Recruitify routes to `/contact` instead |
| **3** | **Creator track record** | **Ramish Aziz has 18 published templates.** The strongest support signal obtainable — Framify's volume could not be established |
| **4** | **Homepage density** | Its homepage is a **long lead-gen page**: hero+CTA, social proof, case studies, services, 3-tier pricing, team. Built to sell, not to inform |

---

### The frame that decides it

> **They donate to different things.** Recruitify donates **the site** — seven pages, a legal donor,
> a proof skeleton. Funnelz donates **a landing page and a CMS.**

That looks like it should favour Funnelz, because `/agencies` is the one page taking 100% of paid
traffic and the only one I said you would build from blank. **It does not, and here is why:**

**Funnelz's homepage donates four of your seven landing-page blocks — hero, social proof, services,
pricing. So does Recruitify's** (hero, stats, process, testimonials, case studies, FAQ). **Neither
donates the three that matter**: the metrics/results treatment, the volume calculator, the comparison
block. Those are exactly what makes `/agencies` different from every other page on the internet, and
**they get built either way.**

So the landing-page advantage Funnelz appears to have is **mostly illusory** — while Recruitify's
thirteen-page advantage is real and verified.

| | Recruitify | Funnelz |
|---|---|---|
| Pages you build from blank | **2** | **5** |
| Blocks of `/agencies` donated | ~4 of 7 | ~4 of 7 |
| The 3 blocks that matter | build | build |
| Legal donor layout | **yes, verified** | no |
| CMS | no — **an afternoon at ~10 recuts** | **yes** |

---

### Take Recruitify, and steal from the others

**Recruitify** for the site. Then, deliberately:

| Steal | From | For |
|---|---|---|
| **The Results metrics block** | Conversion | Block 3 — the recut with retention deltas. Recruitify's `/projects` has the *structure* but its items are narrative, not numeric |
| **The comparison table** | Conversion | Block 6 — where the **$5,000–16,500/mo vendor-invoice** argument lives |
| **A CMS collection** | Framer itself | `/proof/[slug]` at ~10 recuts. One afternoon, not a rebuild |

**Choose Funnelz instead only if** you would rather inherit a CMS today and build five pages, than
inherit seven pages and add a CMS in month three. **That is the entire trade**, and it is smaller
than the number of rounds spent reaching it.

**Whichever you pick, the phone test decides it** — `MOBILEHERO` and 4G speed outrank everything
above and are the two things I cannot check from here.

---

## Who is actually better at the landing page?

I said *"both donate about four of seven blocks, so it is a wash."* **That was lazy.** Compared
block by block against the seven in [`MINIMUM.md`](MINIMUM.md) §2, using what was verified on each
homepage:

| # | Block needed | **Recruitify** | **Funnelz** |
|---|---|---|---|
| 1 | Hero + a number + one CTA | hero + CTA, **no number** | hero + CTA, **no number** |
| 2 | **Volume calculator** | ✗ | ✗ |
| 3 | **Proof with metrics** | **stats block — active applicants, global reach, satisfaction.** A numbers treatment | case studies, **narrative** |
| 4 | **How it works, 3 steps** | **explicit 3-step: Consultation → Screening → Placement** | mission + services, **no process block** |
| 5 | Price + guarantee | pricing is a *page*, not a block | **3-tier pricing on the homepage** |
| 6 | **Objection block** | **FAQ on the homepage** | ✗ |
| 7 | Repeat CTA | ✓ | ✓ |
| | **Blocks donated** | **5 of 7** | **3 of 7** |

> **Recruitify's homepage is the better landing-page donor, not Funnelz's.** It brings the metrics
> block, the three-step process and the FAQ. Funnelz brings pricing tiers.

**The distinction worth holding:** Funnelz is better at *looking like a landing page* — it is
lead-gen shaped and its ordering is built to sell. **Recruitify has more of the specific blocks this
particular landing page needs.** You are not copying a generic LP; you are building a defined
seven-block page, and matching blocks beat general vibe.

---

## Can you buy Funnelz and harvest parts for `/about`, `/contact`?

**No — and the premise is inverted.**

> **Funnelz does not have `/about` or `/contact`.** Crawled: it has **two URLs**, home and `/blog`.
> Recruitify already ships both pages. **There is nothing to harvest, and nothing that needs
> harvesting.**

On mixing templates generally:

| | |
|---|---|
| **Technically possible** | You can copy layers between Framer projects if you own both |
| **But two design systems** | Different type scale, colour tokens, spacing, button styles. A pasted section arrives with its own styling and **restyling it to match is usually as much work as building the block** |
| **~$150 instead of ~$79** | For parts you would restyle anyway |

### And the CMS point deserves correcting

I have been treating *"has a CMS"* as a **template** feature. It is not — **it is a Framer platform
feature.** [`SITE.md`](SITE.md) §2 recorded it: **Framer Pro at $30/mo includes CMS and forms.**

> **You can create a CMS collection in any Framer project, on the plan you are buying anyway.**
> Funnelz does not give you a capability you would otherwise lack. It gives you **one pre-built
> collection — an afternoon saved, once.**

Which shrinks Funnelz's last real edge considerably. Its remaining genuine advantages are the
creator's 18-template track record and booking already sitting in the nav — and the second is a
Cal.com embed you were adding regardless.

---

## So, settled

| | Recruitify | Funnelz |
|---|---|---|
| **LP blocks donated** | **5 of 7** | 3 of 7 |
| Pages built from blank | **2** | 5 |
| Legal donor layout | **yes, verified** | no |
| `/about`, `/contact` | **ship** | **do not exist** |
| CMS | **build it — a Framer feature, one afternoon** | pre-built |
| Creator track record | not established | **18 templates** |

**Recruitify wins the landing page too**, which was the last argument for Funnelz. The three blocks
that actually differentiate `/agencies` — calculator, retention metrics, comparison table — are
absent from both and get built either way.

---

## Widening the search: 40 demos crawled, and Recruitify is beaten

Not "hundreds" — but **40 live demos crawled with a clean 404 control on every one**, which is worth
more than hundreds of listings, because listings have now been wrong four times (`conversion.framer.
website` was a Framer starter page; Averra's advertised *"ten pages, four CMS collections"* crawled
as **three pages**).

### The finding that made triage possible

> **Only 6 of 40 demos ship a legal page.** Template authors do not write privacy policies. That is
> *why* Recruitify looked unbeatable — and it is also the filter that cut 40 candidates to 6 in one
> pass.

The six: `influence`, `lanx`, `lyniq`, `method`, `recruitify`, `talentify` (disqualified — job board).

### Head to head, crawled

| | Pages | Legal | Blog/CMS | `/projects` | Extras |
|---|---|---|---|---|---|
| **Recruitify** | **8** | ✓ `/privacy` + `/terms` | **✗** | ✓ | `/faq`, `/pricing` |
| **Lyniq** | **7** | ✓ `/privacy` + `/terms` | **✓** | ✓ | — |
| Influence | 6 | ✓ `/terms` | ✓ | — | `/careers` |
| Vinency | 6 | ✗ | ✓ | — | `/faq`, `/pricing` |
| Method | 5 | ✓ `/terms` | ✓ | `/work` | — |
| Lanx | 3 | ✓ | ✗ | — | — |

**Lyniq is Recruitify minus `/faq` and `/pricing`, plus `/blog`.** Neither of those two is in your
fourteen. **The blog is the gap I have flagged in every round.**

### And its homepage is the best landing-page donor found

Read in full. **6 of your 7 blocks**, against Recruitify's 5:

| Block | Lyniq | Recruitify |
|---|---|---|
| Hero + CTA | ✓ | ✓ |
| **Volume calculator** | ✗ | ✗ |
| **Metrics block** | ✓ stats — launched, reached, satisfaction, years | ✓ stats |
| **Step process** | ✓ four-step | ✓ three-step |
| **Price block on the page** | **✓ three tiers, on the homepage** | ✗ — pricing is a *page* |
| **FAQ / objections** | ✓ five questions | ✓ |
| Repeat CTA | ✓ | ✓ |
| | **6 of 7** | **5 of 7** |

Plus **testimonials carrying metrics**, and — checked because I had dismissed the premium tier as
heavy — **"moderate visual density, text-heavy rather than dominated by imagery or video."** That
dismissal was wrong too.

### Where Recruitify still wins

**Register.** Lyniq is a **design studio** — *"we create digital designs that help brands move faster
and convert better"*, with $999/$2,499/$4,999-a-month plans and a Discovery → Design → Development →
Launch process. Recruitify is a recruitment agency whose process is **already Consultation →
Screening → Placement**.

**But register is weighted 6 — Tier C — on your own instruction that copy is free and tooling is
what matters.** Applying my own weighting honestly, it does not carry the decision.

---

## Revised answer: Lyniq

| | |
|---|---|
| **Tier A — shape** | Both pass. Employer-facing B2B services. Recruitify is marginally closer; neither is a job board or a product page |
| **Tier B — legal donor** | **Tie.** Both ship `/privacy` and `/terms` |
| **Tier B — proof structure** | **Tie.** Both ship `/projects` |
| **Tier B — conversion architecture** | **Lyniq, 6 of 7 blocks against 5** — and the difference is **price on the page**, which a landing page needs and a pricing page does not provide |
| **Tier C — CMS** | **Lyniq.** Removes the one debt I have flagged every round |
| **Tier C — register** | **Recruitify** — a full copy rewrite either way, weighted 6 |

**Lyniq wins on Tier B and Tier C, ties on Tier A, and loses only the criterion you told me not to
weight.**

**Take Lyniq. Recruitify is the fallback** — and if the phone test kills Lyniq's hero, Recruitify is
still a good answer with one afternoon of CMS work owed.

*And the honest note: **I had Lyniq in the "premium agency, probably heaviest" bucket for four rounds
and never opened it.** It was dismissed on a guess about page weight that turned out to be wrong.
Widening the net was the right instruction.*
