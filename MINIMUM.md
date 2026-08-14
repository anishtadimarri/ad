# The Bare Minimum

> ⚠️ **Superseded on the funnel, August 2026.** The **$500 teardown has been removed** by operator
> direction — every ICP × role now gets the same page and the conversion is a **booked call**.
> The Stripe Payment Link is **no longer launch infrastructure**. What is needed instead is a
> **qualifying gate in front of a calendar embed**.
> See [`scoring/CALLFUNNEL.md`](scoring/CALLFUNNEL.md), which ranks twelve booked-call funnels
> and specifies the ad, landing page and homepage that replace this. **The reasoning below is kept
> because the trade it identifies is still real** — it was just priced differently.

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

---

## 7. Can the homepage and the landing page be the same?

**Same design system — yes, and you should. Same page — no.**

Reuse the components: hero, proof block, CTA block, footer, type and colour. That is ~70% of the
landing page's parts, and rebuilding them twice is wasted work.

But they are **two different jobs**, and merging them costs you something specific:

| | **`/agencies`** | **`/`** |
|---|---|---|
| Audience | One. Cold agency owners from an ad | **Unknown** — a buyer, a candidate, a referral, a supplier, someone checking you are real |
| Job | **One action** | **Routing and legitimacy** |
| Length | Long. Seven blocks | **Short.** Four |
| Tone | Direct response | Institutional |

### The reason that actually decides it

> **Measurement.** If `/` is also the ad destination, your landing-page conversion rate is
> contaminated by direct and referral visitors, who behave nothing like cold paid traffic. **You
> would never be able to tell whether the page or the audience was moving.** And you cannot make a
> variant of `/` — but `/agencies-v2` is a duplicate and an edit.

Two smaller reasons: message match per ICP is the largest lever on a cold page, and a dedicated ad
destination is what keeps Meta's page review looking at a buyer page.

**So: one component library, two pages.** The homepage stays four blocks — what you do, the proof
block, who it is for with a link to `/agencies`, and the footer.

---

## 8. Do you need a page for talent?

**Not on the site. Not at launch.** But *not nothing* either — and the answer is better than the one
in [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §7.

Candidates **will** check you out. You will be sourcing them on LinkedIn and portfolio sites, and an
editor deciding whether to spend two hours on your take-home will look at your website first. If
there is no sign that you hire, you look less real **to the supply side** — and supply is what you
cannot sell without.

The cheap fix is not a footer link. It is:

> **Put the application form on a separate URL entirely** — Tally, Typeform, whatever — and paste it
> into your outreach messages. **It never appears on `allhandstalent.com` at all.**

| | |
|---|---|
| **Zero job content on the domain** | Which removes the Employment Special Ad Category risk completely, rather than mitigating it with `noindex` |
| **Candidates you contact still get something professional** | They reached you through outreach, so they do not need to find it |
| **No SEO surface** | Which you do not want yet anyway — [`REFERENCE.md`](REFERENCE.md) §4: supply pages are an SEO asset and a paid-ads liability |
| **One less page** | |

Move it onto `/talent` at **month 3–6**, when organic traffic starts to matter and you actively
*want* the SEO surface. Until then it is a form link in a DM.

---

## 9. What makes an unknown operator look legitimate

The question behind the question, and the answer is mostly not pages.

> **The highest-trust element on the site is not a page. It is a named human with a face, and a real
> registered address in the footer.** Anonymous sites read as risky, and you are asking a stranger to
> wire $500 to someone they have never heard of, in a country they have opinions about.

Ranked by trust bought per minute spent:

| | What | Why it works |
|---|---|---|
| **1** | **Footer: entity name, registered address, email, LinkedIn** | **Ten minutes, and the single biggest lift.** A real address is the cheapest legitimacy signal that exists. It is also why the entity chain in [`ACTIVITIES.md`](ACTIVITIES.md) Tier 0 is worth doing early |
| **2** | **You, visible on `/`** — photo, name, one paragraph | Free. **For a solo operator with no track record, being personally visible *is* the credential.** Somewhere shows eight named candidates; you show the person who grades them |
| **3** | **`/guarantee` as a real page** | Your cheapest differentiation, and **a bullet point reads as marketing while a page reads as a commitment**. Terms in full: 12 months, unlimited replacement, no cash refunds |
| **4** | **A page on how you handle their ad-account access** | **Differentiating, and nobody expects it.** You are asking for access to their Meta ad account — the scariest thing in the transaction. Partner access via Business Manager, never shared logins, 2FA, documented revocation. **Somewhere uses SOC2 and ISO badges here; you cannot, so answer the actual fear instead** |
| **5** | **`/terms` and a refund policy for the $500** | Once money moves. States what they get if the search stalls |
| **6** | Client logos, testimonials, case studies | **Real ones only.** You have none yet, and a fabricated one is fatal to a positioning built on *falsifiable* |

### What not to fake

No stock team photos, no invented client logos, no *"trusted by 500+ companies"*, no fake reviews.
**The entire positioning is that your claims can be checked** — [`MODEL-V2.md`](MODEL-V2.md) §8's
`TRUECLAIM` is the reason this model beat the previous one. One fabricated proof point and the
graded work sample stops meaning anything.

**The honest version is stronger anyway:** *"I am one person. I personally grade every editor before
you meet them. Here is the test, here is a recut I did, and here are the numbers. If the placement
does not work, I replace them for twelve months."*
