# `/agencies` — A to Z, From the Ad Onward

> ⚠️ **Superseded on the funnel, August 2026.** The **$500 teardown has been removed** by operator
> direction — every ICP × role now gets the same page and the conversion is a **booked call**.
> The CTA is no longer *"Get the $500 teardown"* — it is the **volume calculator**, and
> `/hire/[slug]` × 20 is replaced by **one page with a role picker**.
> See [`scoring/CALLFUNNEL.md`](scoring/CALLFUNNEL.md), which ranks twelve booked-call funnels
> and specifies the ad, landing page and homepage that replace this. **The reasoning below is kept
> because the trade it identifies is still real** — it was just priced differently.

The one page you build from blank, traced from the impression to the money. Every element is here
because of what the visitor is doing at that exact moment, not because landing pages usually have it.

**The governing idea:**

> **The ad puts the visitor into a specific mental state. The page's only job is to *continue* that
> state, not restart it.** Almost every landing page fails by restarting — the ad makes a sharp,
> specific claim, and the page opens with a generic value proposition. **The visitor has to re-decide
> whether they care, and most of them decide no.**

---

## The sample ad — so the page has something to continue

**Audience:** intent seed — agencies that posted a video-editor role in the last 30 days
([`TARGETING.md`](TARGETING.md)). **Placement:** Feed and Reels, mobile.

**Creative:** a 9:16 split-screen. Their category's ad on the left, your recut on the right, playing
in sync. A retention curve overlaid, with two numbers burned in: **`3s: 41% → 68%`**.

**Primary text:**
> You're shipping three cuts a month. Your best-performing ad is six weeks old and its CPM is
> climbing. That isn't a creative problem. It's a headcount problem.

**Headline:** *A full-time performance editor, graded before you meet them.*
**Description:** *$500 ad-account teardown. Credited against the fee.*
**CTA button:** `Learn More`

---

## A. Know what they believe at the moment of the tap

They are on a phone, mid-scroll, probably between other tasks. They have just accepted **one
proposition**: *my creative volume is too low and that might be a hiring problem.* They have not
accepted that you can solve it, that India is fine, or that $500 is reasonable.

**Everything below is in service of that specific starting point.** Write for it, not for a stranger.

## B. Match the message in the first 40 characters

The page headline must **echo the ad's claim in the ad's own words.** If the ad said *volume* and the
page says *"premium talent solutions"*, you have restarted them.

> **Page H1:** *Three cuts a month isn't a creative problem.*
> **Sub:** *It's one editor short. We grade them before you meet them.*

## C. Pass the three-second test on a 390×844 phone

Headline, one line of sub, one tappable button — **all above the fold, no scrolling.** Screenshot it
on your own phone without scrolling. If the button is not in the shot, the page fails and nothing
else on it matters.

## D. Carry the visual across the click

**The same split-screen frame from the ad appears immediately below the fold** — ideally the identical
still. Visual continuity is the cheapest trust mechanism there is: it tells them they arrived in the
right place before they read a word.

## E. Give them one number, and repeat the ad's number

`3s: 41% → 68%` was in the creative. **Use the same figures on the page.** A different number reads
as a different claim.

## F. Remove the navigation

A landing page has **no header nav.** Every nav link is an exit. Logo, unlinked or linking to nothing.
Footer gets `/privacy` and a real address — nothing else.

**This is the single most common conversion mistake made by people who build LPs inside a website
template**, because the template's nav comes along for free.

## G. Prove it with the recut, playable, muted, captioned

- Autoplay muted, loop, **captions burned in** — Reels-trained viewers watch without sound
- Side by side, original left, recut right
- **Retention numbers under each, not over the video**
- One sentence: *"Same offer, same audience, same spend. Only the cut changed."*

**This block is the business.** If you have nothing to put here, do not run the ad yet.

## H. Let them diagnose themselves — the volume calculator

Three inputs, no email gate:

| Input | Example |
|---|---|
| Cuts shipped per month | 3 |
| What your studio or freelancer invoices | $4,000 |
| Cuts you'd ship if capacity were free | 16 |

Output, computed live:

> **At 16 cuts a month your current vendor bills ≈ $21,300/mo. A full-time editor costs a one-time
> fee and $1,650/mo.**

**Why this is the highest-value block on the page:** it makes *them* say the number. A claim you
assert is resisted; a number they generated is accepted. And it does the paid teardown's core job for
free, at the top of the funnel — [`TEARDOWN.md`](TEARDOWN.md) §4.

## I. Show the mechanism in three steps, ending at the ask

1. **$500 teardown** — I audit your account and creative, and tell you the cadence you actually need
2. **Graded shortlist** — three editors, each with a recut and measured retention
3. **You hire. 12-month replacement.**

Three steps, not five. **Step one is the CTA**, which is what makes the teardown feel like the
beginning rather than a toll.

## J. Put the price on the page

**One-time, 30–35% of first-year compensation. $500 of it credited from the teardown.** Plus EOR at
$477/employee/month as the default employment path.

Hiding price costs you the buyers who cannot afford you *after* you have paid for their click, and it
makes the ones who can afford you suspicious.

## K. Reverse the risk twice

- **12 months, unlimited replacement, no cash refunds** — modelled as *cheaper* than the 6-month
  industry standard while sounding stronger
- **The teardown is credited** — so the $500 is not really at risk either

## L. Answer exactly three objections, in their words

| They think | You answer |
|---|---|
| *"Why India?"* | The graded work sample. Not a country argument — a numbers argument. [`COUNTRIES.md`](COUNTRIES.md) §9 shows the wary buyer is a **better** client, not a worse one |
| *"Why not a freelancer?"* | The calculator's own output. At 16 cuts a month a freelancer is more expensive and less available |
| *"Why not AI?"* | Honest: AI does the cut, judgement does the hook. Name it before they do — it is [`MODEL-V2.md`](MODEL-V2.md)'s weakest score and pretending otherwise reads as evasion |

## M. Say who it is *not* for

> *"If you ship fewer than eight cuts a month, you do not need this. Hire a freelancer."*

**Disqualification raises conversion** among the people who remain, and it is the fastest credibility
signal available to someone with no track record.

## N. Put your face and name on it

One photo, one line: *"I grade every editor personally before you meet them."* An anonymous page
asking for $500 from a country the buyer has opinions about is the wrong combination.

## O. Ask for the minimum

**Three fields. Email, company URL, cuts per month.** Not phone, not team size, not budget range —
you learn all of that on the call, and every field costs completions.

The one field that *earns* its place is **"how did you hear about us?"** — the moment cold email runs
alongside Meta, platform attribution double-counts and you defund the wrong channel.

## P. Audit the friction, ruthlessly

No account creation. No captcha unless spam forces it. No multi-step wizard. No cookie banner
covering the CTA on mobile. **No chat widget** — it obscures the button on a phone and it is a promise
to answer that you cannot keep alone.

## Q. Write the micro-copy under the button

> *"Takes 30 seconds. I reply within one business day with the teardown scope and a payment link."*

**Uncertainty about what happens next is a silent objection.** One sentence removes it.

## R. Get the mobile mechanics right

Sticky CTA bar after the first scroll · tap targets ≥ 44px · nothing that depends on hover · text
≥ 16px so iOS does not zoom on focus · **the CTA repeated after every second block**, because mobile
users do not scroll back up.

## S. Hold a speed budget

Static hero image, not video, above the fold. The recut loads **below** it, lazily. Strip the
template's scroll animations. Two web fonts maximum. **The funnel carries an 85% LP-view rate — that
is a page-weight number**, and every point is lost before a word is read.

## T. Instrument it before you spend

- **Pixel + CAPI, verified with test events**
- Events: `LP view` → `Lead` (form) → **`Purchase` (teardown)** — and optimise toward `Lead` until
  there is enough volume for `Purchase`
- **UTMs set from the first click.** Cannot be retrofitted
- `/thanks` and `/paid` as **separate URLs**, or you cannot tell a form fill from a $500 sale

## U. Make `/thanks` do work

Not a dead end. **What happens next in three lines, a Cal.com embed, and the teardown payment link.**
The booking is the real conversion; the form was just permission to ask.

## V. Fire the money event on `/paid`

Stripe Payment Link → success URL `/paid` → `Purchase` event. **That is the event that actually maps
to revenue**, and the reason it needs its own URL.

## W. Follow up within minutes, not days

An automatic email with the teardown scope and the payment link. Speed at this moment is the
strongest signal a one-person company can send — **it is the one thing you can beat a large
competitor at, every time.**

## X. What to leave off

No stock photography of people at laptops. No invented client logos. No *"trusted by 500+
companies"*. No team page. No blog links. No awards. **No testimonials you have not earned** — the
whole positioning is that your claims can be checked, and one fabricated proof point makes the graded
sample worthless.

## Y. Know which number tells you what

| Symptom | Where the problem is |
|---|---|
| Low CTR | The **ad**, not the page |
| Good CTR, low LP view rate | **Speed** |
| Good LP views, low form fills | **Above the fold** — headline, offer, or CTA placement |
| Good form fills, low teardown purchases | **The offer or the price**, not the page |
| Good purchases, no placements | **Supply**, not marketing |

And remember [`SITE.md`](SITE.md) §1: **you cannot A/B test this.** At 2.0% conversion, detecting a
20% lift needs ~$87k of spend. **Change things, ship, read the direction, keep the win.**

## Z. The one that decides it

> **Block G.** One recut, side by side, with the retention delta measured against the original.
>
> Every other letter here is a way of getting someone to look at it, and none of them can compensate
> for its absence. **If you cannot fill G, you do not have a landing-page problem — you have a
> business that has not started yet.**

---

# The same page, 20 combinations

**Correction to everything above.** I wrote `/agencies` as a bespoke page with performance video and
agencies baked into the blocks — the split-screen recut, retention percentages, cuts-per-month. **That
does not survive twenty ICP × role combinations.** Bookkeeping for creator businesses has no recut and
no retention curve.

So the page has to be **one structure with a small set of variables**, and the whole design question
becomes: *which blocks are invariant, and what is the smallest variable set that still carries
specificity?*

---

## 1. What is invariant — and it is most of the page

| Block | Why it does not change |
|---|---|
| **The seven-block order** | Hero → self-diagnosis → proof → mechanism → price → objections → CTA. This is a persuasion sequence, not a content choice |
| **The mechanism** | Paid teardown → graded shortlist of three → you hire → 12-month replacement. **Identical for every role** |
| **The guarantee** | 12 months, unlimited replacement, no cash refunds |
| **The pricing model** | One-time, 30–35% of first-year compensation, teardown credited. The *percentage* is invariant; the dollar figure follows salary |
| **EOR as the default** | $477/employee/month, every role |
| **Your face and name** | *"I grade every one personally"* is the same claim regardless of what is being graded |
| **Who it is not for** | Only the threshold number changes |
| **The three objections** | *Why India · why not a freelancer · why not AI* — same three, every combination |
| **Form, micro-copy, mobile mechanics, speed, tracking** | Entirely structural |

> **Roughly 80% of the page is invariant.** That is the finding — the specificity that makes a cold
> page convert is concentrated in a handful of nouns and one number, not spread through the copy.

---

## 2. The variable set — eight fields

| # | Variable | `ecom × performance video` | `agency × performance video` | `creator × bookkeeping` |
|---|---|---|---|---|
| 1 | **Role noun** | performance video editor | performance video editor | bookkeeper |
| 2 | **ICP noun** | e-commerce brand | agency | creator business |
| 3 | **Volume unit** | cuts per month | cuts per month | transactions per month |
| 4 | **Pain trigger** | *"your best ad is six weeks old"* | *"you are turning down retainers"* | *"your books close three weeks late"* |
| 5 | **Vendor comparator** | studio, $4–16k/mo | studio or freelancer | bookkeeping firm, $500–2k/mo |
| 6 | **Proof artefact** | recut, 3s/15s retention | recut, 3s/15s retention | reconciled month, days-to-close |
| 7 | **The grading test** | recut an existing ad | recut an existing ad | reconcile a messy month |
| 8 | **Not-for threshold** | fewer than 8 cuts/month | fewer than 8 cuts/month | fewer than 200 txns/month |

**Eight fields. Fifteen to twenty minutes per combination**, once the structure exists.

---

## 3. Build it as a CMS collection, not twenty pages

This is the part that changes an earlier decision.

| Option | At 20 combinations |
|---|---|
| **Duplicate and edit ×20** | ~7 hours, and **every structural change becomes twenty edits.** Change the guarantee wording once and you have twenty places to miss one |
| **One CMS collection, one template page** | `/hire/[slug]` · each combination is an **item with eight fields** · **change the design once and all twenty update** |

> **So the CMS is not a Tier C debt any more — it is Tier A infrastructure, needed at launch.**
> I had it as *"an afternoon at around ten recuts"*. Twenty parameterised landing pages moves it to
> the critical path, and it strengthens the case for a template that already demonstrates a
> collection-driven page.

**URL shape:** `/hire/ecom-video-editor`, `/hire/agency-video-editor`, `/hire/creator-bookkeeper`.

**All of them `noindex`.** Twenty near-identical pages is doorway-page territory for Google, and they
are ad destinations rather than organic surfaces. [`SITEMAP.md`](SITEMAP.md) already noindexes LP
variants — this is the same rule at larger scale. Organic lives on `/`, `/proof` and the blog.

---

## 4. The two blocks that need generalising

Everything else survives as written. These two were role-specific and now need a shape that holds
any role.

### The proof block

**Was:** side-by-side recut with retention percentages.
**Generalised to:** **artefact before → artefact after → one measured metric → the delta.**

| Role | Before | After | Metric |
|---|---|---|---|
| Performance video | original ad | recut | 3-second retention |
| Bookkeeping | the month as received | reconciled | days to close |
| Design | the brief | the output | — *needs a metric or this role is not ready* |

> **If a role has no measurable delta, it is not launchable.** That is a genuinely useful filter, and
> it falls out of the parameterisation — it says *stick to roles whose output can be measured*, which
> is the same `FALSIFIABLE` criterion [`DOMAINS.md`](DOMAINS.md) introduced for the name.

### The calculator

**Was:** cuts per month × studio rate vs in-house.
**Generalised to:** **volume × current vendor unit cost, against one full-time cost.**

```
  [volume]  ×  [vendor rate per unit]   =  what you spend now
                     vs
  one full-time [role]  =  one-time fee + $[salary]/mo
```

Three inputs and two labels change per combination. **The arithmetic never does.**

---

## 5. Does a parameterised page convert as well as a bespoke one?

Honestly: **slightly worse than a perfect bespoke page, and much better than twenty pages you never
finish.** And the gap is smaller than it appears, because of where specificity actually lives:

| What carries the specificity | Where it comes from |
|---|---|
| **The ad** | Fully bespoke per combination — creative, copy, audience. **This is where most message match is won** |
| **The H1** | Variables 1, 2 and 4 — *"Three cuts a month isn't a creative problem"* vs *"Books closing three weeks late isn't a diligence problem"* |
| **The calculator's output** | Their own numbers, in their own units |
| **The proof artefact** | Role-specific by construction |

**Four of the eight variables appear above the fold.** A visitor arriving from the ecom-video ad reads
their role, their ICP, their pain and their unit before scrolling — which is all message match
requires. **The invariant 80% is the part nobody reads closely anyway.**

---

## 6. What this changes upstream

| Document | Change |
|---|---|
| [`MINIMUM.md`](MINIMUM.md) §1 | `/agencies` becomes **`/hire/[slug]`, one CMS template page.** Still one build |
| [`SITEMAP.md`](SITEMAP.md) | Rows 2, 10 and 23 — `/agencies`, `/ecommerce`, `/designers` — **collapse into one collection.** The sitemap gets *smaller* as the business gets wider |
| [`SITE.md`](SITE.md) / [`TEMPLATE.md`](TEMPLATE.md) | **CMS moves from Tier C to Tier A.** A template demonstrating a collection page is now worth more than one with two extra static pages |
| [`MODEL-V2.md`](MODEL-V2.md) gap 8 | Still holds — **build twenty pages, launch two.** Meta needs concentration; the collection just means the twenty-first costs fifteen minutes rather than a day |

**And one thing gets better:** a new role or ICP is now **an eight-field CMS entry**, not a project.
That is the difference between a business that can test ten wedges and one that can test one.
