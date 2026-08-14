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
