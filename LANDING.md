# `/agencies` — A to Z, From the Ad Onward

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
