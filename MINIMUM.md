# The Bare Minimum

> Everything else in this repo describes what the site becomes. This is what has to exist **before
> the first dollar of spend**, and nothing more.

The governing rule, because it cuts the list roughly in half:

> **A page exists to own a URL, not to hold content.** Content goes in sections. You need a separate
> page only when something needs its own address — an ad destination, a legal document, a conversion
> trigger, or a link you send externally. **Everything else is a block on the landing page.**

---

## 1. Four pages. That is the minimum

| # | Page | Why it cannot be a section |
|---|---|---|
| **1** | **`/agencies`** — the single ad destination | **Ads must never point at `/`** ([`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §7). It needs its own URL so page review sees a buyer page, and so the ad's promise matches the page's headline |
| **2** | **`/thanks`** | **The conversion event fires here.** It also holds the booking embed. Without a distinct URL you cannot measure anything |
| **3** | **`/privacy`** | **Meta's ad review looks for it.** Ten minutes, and its absence can hold up approval |
| **4** | **`/`** — a thin homepage | A buyer who is about to send $500 will type the domain. **It cannot 404**, and it cannot be a landing page for the wrong ICP |

**Stripe hosts the checkout**, so there is no `/teardown` page at launch — a Payment Link is a hosted
URL you point a button at, with the success URL set to `/thanks`. That is one fewer page to build
and one fewer thing to break.

### Launch with one ICP, not two

[`MAP.md`](MAP.md) names two verticals and [`MODEL-V2.md`](MODEL-V2.md) gap 8 says **concentration is
what Meta needs to learn.** Two ICPs means two pages, two ad sets and half the signal each.
**Start with agencies** — they buy creative volume by definition, so the volume argument lands
without explaining itself. Add `/ecommerce` once the first page has data.

---

## 2. The landing page, in seven blocks

Everything that looks like it wants its own page starts life here.

| # | Block | Note |
|---|---|---|
| **1** | **Hero: the promise, a number, one CTA** | Must fit above the fold on a **390×844** phone. The number is **4–13× against the studio invoice** — not a salary comparison ([`REFERENCE.md`](REFERENCE.md) §3) |
| **2** | **The volume calculator** | Cuts shipped per month → studio invoice → in-house cost. **It does the teardown's job for free**, and it walks them into the volume conclusion that [`TEARDOWN.md`](TEARDOWN.md) §4 says is the only one that sells |
| **3** | **Proof** — one recut, with 3-second and 15-second retention against the original | **If you have no recut, you have no business yet.** Do one before you spend anything |
| **4** | **How it works** — three steps, ending at the paid teardown | The teardown *is* the CTA. Not "book a call" |
| **5** | **Price and guarantee** | One-time, **30–35% of first-year comp**; **12-month unlimited replacement**. Both as blocks, not pages |
| **6** | **The objection block** | Two objections only: *"why India"* ([`COUNTRIES.md`](COUNTRIES.md) §9 prices it) and *"why not a freelancer"* — answered by the volume number from block 2 |
| **7** | **Repeat the CTA** | Mobile users do not scroll back up |

**Nothing else.** No team, no about, no blog, no logos you do not have, no testimonials you have not
earned.

---

## 3. What goes on the thin homepage

Four blocks, twenty minutes:

1. What you do, in one sentence
2. The same proof block from the landing page
3. Who it is for → link to `/agencies`
4. Footer with `/privacy` and a real contact address

---

## 4. The non-page requirements

These are not pages, and **launch is blocked without them**:

| | |
|---|---|
| **Facebook Page with the username claimed** | You cannot run an ad without one |
| **Business Manager + a second ad account ready** | Build it before you need it — you cannot build it after |
| **Domain verified** | In Business Manager |
| **Pixel + CAPI, verified with test events** | **Every CAC number assumes attribution works** |
| **UTMs and a self-reported attribution field** | Set before the first click. **Cannot be retrofitted** |
| **Stripe Payment Link** | With the success URL pointing at `/thanks` |
| **Cal.com embed on `/thanks`** | Free tier |
| **`you@allhandstalent.com`** | A gmail reply-to on a $6,600 offer is a leak you never see |

---

## 5. What you are deliberately not building yet

| Later | When |
|---|---|
| `/ecommerce` | After the first page has data |
| `/pricing`, `/guarantee`, `/faq` as **pages** | They are blocks until someone asks for a link |
| `/proof` as a **page** with many entries | Block first. Page at ~3 recuts. **CMS at ~10** |
| `/about`, `/contact` | Contact is an email address in the footer until it isn't |
| `/talent` | **Month 3–6**, footer-only and `noindex` — and not before, because supply comes from referral at launch |
| `/terms`, blog, case studies, calculator variants | Once there is something to write about |

---

## 6. The honest test

If you cannot fill block 3 — **one recut ad, with the retention delta measured against the
original** — then no amount of the rest of this matters. **That block is the business.** The other
six exist to get someone to look at it.
