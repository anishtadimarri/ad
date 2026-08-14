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
