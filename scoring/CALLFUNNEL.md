# Twelve Booked-Call Funnels, Ranked

> Operator direction: **no $500 teardown.** Same page for every ICP x role, and the
> conversion is a booked call. Day 1 tests **2-3 roles x 2-3 ICPs**.

Gross profit is the real one from [`offer_model.py`](offer_model.py): **$4,148 at 30 days**, 
**$11,074 lifetime**. Audience CPMs and CTRs are [`funnel.py`](funnel.py)'s. Budget **$5,000/month**,
founder time at **$60/hour** — which is exactly [`funnel.py`](funnel.py)'s $60 per held call.

---

## 1. First: what removing the teardown actually costs

Worth settling before ranking anything, because the answer is not what the repo assumed.

**[`funnel.py`](funnel.py) put the $500 *after* the held call** — step 7 of 9. So in the
model that already exists, **the deposit rate *was* a close rate.** Removing the teardown
therefore does not delete a funnel step. It changes what happens on the one that remains.

| | With the $500 | Free — bare calendar | Free — **gated** | Why |
|---|---|---|---|---|
| Held call → committed | 21% | 14% | **21%** | A free yes is easier to give and worth less |
| Committed → placed | 85% | 68% | **78%** | A yes with no money behind it ghosts more |
| **Held call → placed** | **17.6%** | **9.4%** | **16.1%** | |

> **A bare free calendar loses 47% of the held-call-to-placement rate. A gated one loses 8%.**

That is the finding, and it is not the one I expected. **The money was doing real work, and
most of that work can be done by friction instead** — but only if something is actually put
in the way. Take the $500 out and put nothing in its place and you lose roughly half the
value of every held call, which shows up as CAC doubling in §2 rather than as a missing step.

The cash it collected was **credited in full against the fee**, so it was working capital,
not profit. The only true revenue loss is the ~15% who paid and never placed —
**about $75 per deposit taken**, against $4,148 of gross profit per client. Under 2%.

**So the operator direction does not break the economics.** What it breaks is the *filter*,
and the ranking below is really a search for the cheapest thing that filters as well as
money did. That is the whole question, and §4 answers it.

One correction to the record while we are here: the landing page had **"Get the $500 teardown"**
as its CTA — i.e. *before* the call — while [`funnel.py`](funnel.py) scored it *after*. **Those are
different businesses**, and only the pre-call version satisfied the standing constraint that
no sales call may determine CAC. The repo has been quietly modelling two funnels at once.

---

## 2. All twelve, on the numbers

Blended across the three audience layers by spend (25% / 45% / 30%), as [`ltgp.py`](ltgp.py) does.

| # | Funnel | Pixel event | Events/mo | CPL | Held calls | Placements | **CAC** | **30-day** | Hrs/mo | Hrs/placement |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Calendar embedded on the landing page | Booked call | 60 | $83 | 39 | 4.0 | **$1,904** | **2.18:1** | 44 | 11 |
| 2 | Form fill, then calendar on the thank-you page | Form fill | 150 | $33 | 46 | 4.2 | **$2,149** | **1.93:1** | 66 ⚠️ | 16 |
| 3 | Application-gated calendar | Application submitted | 66 | $76 | 33 | 5.9 | **$1,222** | **3.40:1** | 37 | 6 |
| 4 | Volume calculator, result gated by email | Calculator completed | 181 | $28 | 43 | 7.0 | **$1,249** | **3.32:1** | 61 ⚠️ | 9 |
| 5 | Free graded work sample, delivered async, then a call | Sample requested | 135 | $37 | 56 | 14.6 | **$900** | **4.61:1** | 136 ⚠️ | 9 |
| 6 | Bench preview — three graded candidates behind an email gate | Bench unlocked | 211 | $24 | 43 | 6.2 | **$1,425** | **2.91:1** | 64 ⚠️ | 10 |
| 7 | Video sales letter above the calendar | Booked call | 79 | $63 | 54 | 6.6 | **$1,298** | **3.20:1** | 61 ⚠️ | 9 |
| 8 | Meta Instant Form — no landing page at all | Lead (on-platform) | 425 | $12 | 51 | 2.1 | **$6,216** | **0.67:1** ⚠️ | 136 ⚠️ | 64 |
| 9 | Small refundable deposit to hold the slot | Deposit paid | 24 | $208 | 22 | 6.9 | **$921** | **4.50:1** | 23 | 3 |
| 10 | Click-to-Messenger / WhatsApp conversation | Conversation started | 159 | $31 | 31 | 2.4 | **$3,858** | **1.08:1** ⚠️ | 70 ⚠️ | 29 |
| 11 | Lead magnet — the role scorecard — then nurture to a call | Guide downloaded | 256 | $20 | 28 | 3.2 | **$2,428** | **1.71:1** | 45 | 14 |
| 12 | Two calls — 15-minute fit, then a 45-minute working session | Booked call | 105 | $47 | 74 | 8.3 | **$1,072** | **3.87:1** | 65 ⚠️ | 8 |

**10 of 12 clear the 1.5:1 constraint** on the base case. CAC spans $900 to $6,216 — a 6.9x range, which is far wider than the 6% that separated form-fill from calendar in [`FUNNEL.md`](FUNNEL.md). **This choice does matter.**

The column to read second is **Hrs/mo**, and it disqualifies more options than CAC does. A solo
operator who is also sourcing, grading, delivering and building has roughly **60 hours a month**
for selling. **8 of the 12 exceed that**, and **Free graded work sample, delivered async, then a call** needs **136** — which is most of a full-time job on its own, at only $5,000 of spend.

---

## 3. The ranking

CAC cannot decide this alone — it says nothing about whether you can *run* the funnel, or
whether it tells you anything in month one. Eight dimensions, three of them **derived from
the model above** rather than scored by hand:

| Dimension | Weight | Source | What it measures |
|---|---|---|---|
| `LEARN` | 22 | **derived** | How fast $5,000/month produces a readable signal across the cells |
| `CAC30` | 20 | **derived** | The 30-day LTGP:CAC ratio against the 1.5:1 constraint |
| `GENERIC` | 16 | scored | Works unchanged across every ICP x role cell |
| `FOUNDER` | 14 | **derived** | Founder hours/month against the ~60 a solo operator has for selling |
| `TRUST` | 10 | scored | Works for an unknown operator with no track record |
| `CALLDEP` | 8 | scored | How little of CAC is decided on the call |
| `BUILD` | 6 | scored | What must exist before the first dollar of spend |
| `POLICY` | 4 | scored | Employment Special Ad Category exposure |

| Rank | Funnel | `LEARN` | `CAC30` | `GENERIC` | `FOUNDER` | `TRUST` | `CALLDEP` | `BUILD` | `POLICY` | **Score** |
|---|---|---|---|---|---|---|---|---|---|---|
| **1** | Volume calculator, result gated by email ✅ | 9.1 | 5.6 | 8.0 | 9.8 | 7.0 | 4.0 | 4.0 | 9.0 | **74.1** |
| **2** | Two calls — 15-minute fit, then a 45-minute working session | 7.0 | 6.7 | 10.0 | 9.3 | 5.0 | 2.0 | 9.0 | 9.0 | **73.5** |
| **3** | Small refundable deposit to hold the slot | 3.3 | 8.0 | 10.0 | 10.0 | 2.0 | 9.0 | 7.0 | 9.0 | **70.4** |
| **4** | Application-gated calendar | 5.5 | 5.8 | 9.0 | 10.0 | 6.0 | 3.0 | 8.0 | 7.0 | **68.1** |
| **5** | Form fill, then calendar on the thank-you page | 8.3 | 2.9 | 10.0 | 9.3 | 4.0 | 2.0 | 9.0 | 9.0 | **67.7** |
| **6** | Bench preview — three graded candidates behind an email gate | 9.9 | 4.8 | 5.0 | 9.5 | 8.0 | 4.0 | 2.0 | 3.0 | **66.3** |
| **7** | Lead magnet — the role scorecard — then nurture to a call | 10.0 | 2.4 | 6.0 | 10.0 | 6.0 | 4.0 | 5.0 | 9.0 | **66.2** |
| **8** | Free graded work sample, delivered async, then a call | 7.9 | 8.2 | 3.0 | 5.2 | 10.0 | 5.0 | 3.0 | 8.0 | **64.9** |
| **9** | Calendar embedded on the landing page | 5.3 | 3.4 | 10.0 | 10.0 | 4.0 | 1.0 | 10.0 | 9.0 | **62.7** |
| **10** | Click-to-Messenger / WhatsApp conversation | 8.6 | 0.0 | 9.0 | 8.8 | 5.0 | 3.0 | 8.0 | 7.0 | **60.6** |
| **11** | Video sales letter above the calendar | 6.1 | 5.4 | 4.0 | 9.9 | 6.0 | 3.0 | 5.0 | 9.0 | **59.4** |
| **12** | Meta Instant Form — no landing page at all | 10.0 | 0.0 | 10.0 | 5.2 | 1.0 | 2.0 | 10.0 | 6.0 | **56.3** |

### Where the ranking disagrees with CAC

| By score | By CAC |
|---|---|
| 1. Volume calculator, result gated by email | 1. Free graded work sample, delivered async, then a call ($900) |
| 2. Two calls — 15-minute fit, then a 45-minute working session | 2. Small refundable deposit to hold the slot ($921) |
| 3. Small refundable deposit to hold the slot | 3. Two calls — 15-minute fit, then a 45-minute working session ($1,072) |
| 4. Application-gated calendar | 4. Application-gated calendar ($1,222) |
| 5. Form fill, then calendar on the thank-you page | 5. Volume calculator, result gated by email ($1,249) |

**Free graded work sample, delivered async, then a call wins on CAC and loses overall.** It produces 135 pixel events a month — 
**31.3 a week**, against the 50 Meta needs to leave the
learning phase. A funnel that cannot teach the algorithm anything cannot be scaled, and
cannot be read across nine test cells. **That is the trap the CAC column hides.**

---

## 4. The real question: what filters as well as $500 did

[`TEARDOWN.md`](TEARDOWN.md) §1 lists four jobs the $500 was doing. Money did all four at
once, which is why removing it needs four replacements, not one:

| The job $500 did | The free replacement | Where it lives |
|---|---|---|
| **Money gate** — filters tyre-kickers | **Qualifying questions with real disqualification.** Ad spend, revenue and volume, asked before the calendar appears — and a genuine *no* screen, not a form that always says yes | Landing page, between the CTA and the calendar |
| **Work sample** — proof you can judge the work | **One public teardown of a brand they know**, not of their account. Same skill, produced once, shown to everybody, costs nothing per lead | Landing page proof block |
| **Qualifier** — you know their cadence before the call | **The volume calculator.** They enter their own numbers and it returns their own gap. You read the submitted values before the call | Landing page, above the CTA |
| **Sets up the sale** — concludes in a volume problem | **The calculator concludes it for them**, which is stronger than you concluding it. [`TEARDOWN.md`](TEARDOWN.md) §4's rule survives intact, unpaid | Same block |

> **Three of the four replacements are the same object: the calculator with a qualifying
> gate in front of the calendar.** That is why funnels 3 and 4 rank where they do, and why
> the recommendation in §7 is a hybrid of them rather than either one.

---

## 5. Rank stability — because every number past the landing page is `[?]`

There is **no published benchmark** for show rate or close rate on cold paid traffic to a
free B2B call. I looked; the cold-calling literature covers dial-to-meeting, not
booking-to-show. So rather than defend point estimates, every funnel's three softest inputs
are swept at **0.7x / 1.0x / 1.3x** — 27 combinations each — and what matters is how often
each one still clears and still wins.

| Funnel | Clears 1.5:1 | Wins on CAC *and* stays runnable | Verdict |
|---|---|---|---|
| Volume calculator, result gated by email | 96% of 27 | 8/27 | **best on the grid** |
| Lead magnet — the role scorecard — then nurture to a call | 56% of 27 | 6/27 | fragile |
| Two calls — 15-minute fit, then a 45-minute working session | 100% of 27 | 3/27 | **robust** |
| Video sales letter above the calendar | 96% of 27 | 3/27 | conditional |
| Free graded work sample, delivered async, then a call | 100% of 27 | 0/27 | **robust** |
| Small refundable deposit to hold the slot | 100% of 27 | 0/27 | **robust** |
| Application-gated calendar | 96% of 27 | 0/27 | conditional |
| Bench preview — three graded candidates behind an email gate | 96% of 27 | 0/27 | conditional |
| Calendar embedded on the landing page | 78% of 27 | 0/27 | conditional |
| Form fill, then calendar on the thank-you page | 70% of 27 | 0/27 | conditional |
| Click-to-Messenger / WhatsApp conversation | 11% of 27 | 0/27 | fragile |
| Meta Instant Form — no landing page at all | 0% of 27 | 0/27 | fragile |

*Runnable* means three things at once: **at least 20 pixel events a week** (below that
you are reading noise), **under 60 founder hours a month**, and **clearing 1.5:1**. Several
funnels with attractive CACs win zero grid points because they fail one of the other two —
**the free work sample above all, which is the cheapest CAC in the study and unrunnable by
one person.**

---

## 6. How many ICP x role cells can $5,000 actually support?

This is the part that changes the plan, and it is arithmetic rather than opinion.

Meta needs **~50 optimisation events per ad set per 7 days** to leave the
learning phase, and inside it **CPA runs 20-50% higher** [V]. So:

| Funnel | Events/week | One ad set clears 50/wk? | Split 9 ways | Intent of the event |
|---|---|---|---|---|
| Meta Instant Form — no landing page at all | 98 | ✅ | 10.9/wk each | **weak** — a download or an unlock |
| Lead magnet — the role scorecard — then nurture to a call | 59 | ✅ | 6.6/wk each | **weak** — a download or an unlock |
| Bench preview — three graded candidates behind an email gate | 49 | ❌ | 5.4/wk each | **weak** — a download or an unlock |
| Volume calculator, result gated by email | 42 | ❌ | 4.6/wk each | strong |
| Click-to-Messenger / WhatsApp conversation | 37 | ❌ | 4.1/wk each | **weak** — a download or an unlock |
| Form fill, then calendar on the thank-you page | 35 | ❌ | 3.9/wk each | strong |
| Free graded work sample, delivered async, then a call | 31 | ❌ | 3.5/wk each | strong |
| Two calls — 15-minute fit, then a 45-minute working session | 24 | ❌ | 2.7/wk each | strong |

**Two things are true at once, and the tension between them is the finding.**

1 of the twelve does clear 50 events a week while also clearing 1.5:1 — and it optimises
toward a **download, an unlock or a chat**, not toward a buying decision. That is *why* it is
cheap. Teaching Meta to find people who download things is teaching it the wrong lesson at
high speed, and the CAC column in §2 is where that shows up — the lead magnet buys events at
$20 and placements at $2,428, against $28 and $1,249 for the calculator.

Among the funnels whose event actually means something, the best is the top-ranked one:
**42 events a week against a threshold of 50** — the closest any high-intent event gets,
and **83% of the way there.** That single fact is most of why it ranks first.

> **Split nine ways it is 4.6 events per cell per week.** Not a test — noise with a dashboard.

To get *one* ad set to 50/week on that funnel needs **$5,995/month**. Nine cells needs
**$53,957/month**, which is 11x the test budget. Neither is the plan, and the
second one is not a plan at any budget you will have this year.

### So the cells cannot be campaign structure

> **The ICP x role matrix belongs in the creative, not in the campaign structure and not in
> the landing page.** One campaign, one ad set, one landing page, nine ads.

| | |
|---|---|
| **Conversion signal pools** | All nine ads feed one optimisation event on one page, so the ad set accumulates events nine times faster than nine ad sets would |
| **The ICP x role read is still clean** | You read it at **ad level** — CTR, cost per event, and the role tapped on the page. Those need dozens of events, not fifty a week each |
| **Meta does the audience work** | Nine ads in one ad set is exactly what Advantage+ style delivery is built to resolve. You are testing *message*, and message is what ad-level reporting is for |
| **It is the cheapest possible test** | Nine creatives is nine hours of work. Nine ad sets is nine learning phases you cannot afford to fund |
| **One page keeps the page test alive** | A landing-page variant needs 42,000 views to prove a 20% lift ([`SITE.md`](SITE.md)). Nine pages means never testing the page at all |

**And the role picker already carries the role dimension.** The tap is a first-party read on
which seat the ad brought in, at zero incremental spend — which is a better instrument than nine
ad sets would have been, because it separates *what the ad promised* from *what the buyer wanted*.

---

## 7. The recommended funnel

**Volume calculator, result gated by email** at **74.1**, built as a hybrid with
**Application-gated calendar** at **68.1** — because §4 showed the qualifying gate and
the calculator are two halves of one replacement for money, not two competing options.

**The top two are 0.6 points apart, which this model cannot resolve.** Two calls — 15-minute fit, then a 45-minute working session
is the other one, and it is a genuinely good answer — a 15-minute fit call is friction that
filters, which is exactly what §4 asked for. **It is rejected on the operator's own brief,
not on the numbers:** the stated goal is that the *page* makes them knowledgeable and
interested enough to book. A two-call funnel moves qualification back into a call, which is
the one thing that cannot be mechanised, cannot be delegated, and does not scale past you.

```
  AD          qualifies on ICP + size, offers the roles as a menu
   |          one campaign · one ad set · 9 creatives
   v
  LANDING     proof · calculator · role picker · qualifying gate
   |          ONE page, ONE url, no CMS
   v
  GATE        3 questions with a real no. Spend, revenue, volume
   |
   +--> disqualified -> honest no + the scorecard. No call booked
   |
   v
  CALENDAR    shown only after the gate passes  <- the pixel event
   |
   v
  CALL        45 min. The calculator has already made the volume argument
   |
   v
  SIGNED      search begins
```

| Step | Number | Source |
|---|---|---|
| Spend | $5,000/mo | the size [`FUNNEL.md`](FUNNEL.md) argued for test one |
| Landing page views | 3,009 | [E] blended CPM/CTR, 15% pre-paint bounce |
| **Pixel event** — calculator completed | **181** | **42/week.** Still under 50, but the most of any option |
| Cost per event | $28 | **below** the verified $30-80 B2B CPL band [V] — because a calculator is a smaller ask than a form |
| Calls booked | 72 | [?] 40% of completions book |
| Calls held | 45 | [?] |
| Signed | 10.7 | [?] the softest number in the model |
| **Placements** | **8.2** | 78% fill |
| Founder hours | 63/mo | 8 hours per placement |
| **CAC** | **$1,064** | spend + founder time ÷ placements |
| **30-day** | **3.90:1** | against the 1.5:1 constraint |
| **Lifetime** | **10.41:1** |  |

### The one thing this funnel still does not satisfy

The standing constraint says **no sales call may determine CAC.** This funnel does not meet
it, and neither does any other option that ends in a booked call — funnel 9, the deposit, is
the only one that does, and it collapses volume to the point of being unmeasurable.

Worth being exact about what is given up, because it is not the ratio:

| | |
|---|---|
| **It stays measurable** | Cost per calculator completion is a paid-media number you can optimise weekly. That is the part that has to be mechanical, and it is |
| **What becomes unhirable** | The close. At 45 held calls a month you are the only closer, and the close rate is the number CAC is most sensitive to. It cannot be delegated until it is documented |
| **What becomes unforecastable** | Placements. 10.7 signings a month is far too few to measure a close rate — ±10 points either way, same as the deposit rate it replaces |
| **The mitigation that actually works** | Move persuasion earlier, permanently. Every point of close rate the calculator and the public teardown buy you is a point that does not depend on the call going well |

So the constraint is not satisfied — it is **deferred**, and the honest version of the plan
says so. The paid gate is the thing to re-test at month three, when there is a close rate to
compare it against. It is a much easier sale once one placement can be named.

---

## 8. The framework, as three assets

### The ad

Nine of them, one ad set. The invariant shape, with only the bracketed parts changing:

```
  HOOK       [ICP + size, as a question they answer yes to]
             "Running $10k+ a month in Meta ads on your own store?"
  TURN       the volume problem, in their units
             "You need 12-16 new cuts a month. You are shipping 3."
  MENU       the roles, named, as a list
             "Editors, media buyers, ops, bookkeepers - graded before you meet them."
  ASK        "See what one costs against your current invoice."  <- not "book a call"
```

| | |
|---|---|
| **The hook carries the ICP** | and nothing else does. Not the ad set, not the page |
| **The menu carries the roles** | so one ad can name three seats and let the page resolve which |
| **The ask is the calculator, not the call** | A calculator is a smaller ask than a calendar, and it is the qualifier. The call is asked for on the page, after they have convinced themselves |
| **No employment language, in any of the nine** | No *apply*, no *join*, no *hiring now*. One reviewer tick costs 10-29% on CAC ([`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md)) |

### The landing page — one URL, and what varies

| Block | Varies by cell? |
|---|---|
| Hero: ICP + size qualifier, one promise | **No.** The size band is the same across roles |
| **Role picker — 'which seat is open?'** | **No.** It IS the variation, resolved by tapping |
| Public teardown of a brand they know | **No.** Produced once, shown to everyone |
| **Volume calculator** | **Labels only.** Ads / campaigns / tickets. The arithmetic is fixed |
| Proof: one measured before-and-after | **Numbers swap on tap.** One real pair per role, or the role does not launch |
| How it works, price, guarantee | **No.** |
| Objections | **No.** Why India, why not a freelancer, why not AI |
| **Qualifying gate, then the calendar** | **No.** Three questions, same three for everyone |
| Founder block and footer | **No.** |

**Roughly 80% of the page is invariant.** The specificity lives in six labels, one number
pair, and the calculator's units — which is exactly why nine cells need one page.

### The homepage

Unchanged from [`MINIMUM.md`](MINIMUM.md) §3, with one addition and one deletion:

| | |
|---|---|
| **Keep** four blocks: what you do, the proof block, who it is for, footer with a real address | It exists so the domain does not 404 for a buyer who types it, and so you look real |
| **Add** the public teardown, linked | It is the work sample now that nothing is paid for. It is the most persuasive object you own and it should not live only on the ad path |
| **Delete** every mention of a paid teardown | It appears in [`LANDING.md`](LANDING.md), [`MINIMUM.md`](MINIMUM.md), [`TEARDOWN.md`](TEARDOWN.md) and [`SITEMAP.md`](SITEMAP.md) as the CTA |
| **Still no ads pointed at it** | Measurement, per [`MINIMUM.md`](MINIMUM.md) §7 |

---

## 9. Which 2-3 x 2-3 to pick

Since the cells are creatives rather than campaigns, the choice costs nine hours instead of
nine budgets — but it should still be the right nine. The filter that matters is not market
size:

> **Can you personally grade the work?** [`LAUNCH.md`](LAUNCH.md)'s `FOUNDERGRADE`. A role
> you cannot grade has no measurable before-and-after, and §8's proof block is empty for it.

| Role | Gradeable by you? | Measurable delta | Verdict |
|---|---|---|---|
| **Performance video editor** | **Yes** — it is the founding skill | 3-sec and 15-sec retention | **Launch cell.** The wedge |
| **Paid media buyer** | **Yes** — same skill, other side | CPA, cost per result | **Launch cell.** Same buyer, bigger seat |
| Marketing ops | Partly | Days to launch | **Third cell.** Adjacent, and you can check the output |
| Bookkeeping | **No** | Days to close | Later. You cannot grade a reconciliation |
| Design | Partly | Revision rounds | Later. Taste is not a measured delta |
| Customer support | **No** | First response time | Later |

| ICP | Why | Verdict |
|---|---|---|
| **Marketing agencies** | Buy creative volume by definition, so the volume argument needs no explaining ([`MINIMUM.md`](MINIMUM.md) §1) | **Launch cell** |
| **E-comm, $3-10M revenue, $10k+/mo ads** | The operator direction's own example, and the spend threshold is a clean qualifier | **Launch cell** |
| Creator businesses | High volume, thin budgets, and they buy on price | Third, or not at all |
| Info / education | Highest creative burn rate of any category | **Better third cell** |

**Two roles x two ICPs = four creatives, not nine.** Video and media buying, into agencies
and e-comm. Both roles are gradeable by the operator today; both ICPs already understand
creative volume. **Add the third of each only once the first four have separated** — and at
42 events a week, four cells is already more than the budget can read cleanly.

---

## 10. What this reverses

| Document | Now wrong |
|---|---|
| [`TEARDOWN.md`](../TEARDOWN.md) | The $500 price and the paid gate. **The generator survives and matters more** — it now produces the free public teardown that replaces the work sample |
| [`LANDING.md`](../LANDING.md) | *"Get the $500 teardown"* as the CTA, and `/hire/[slug]` x 20 |
| [`MINIMUM.md`](../MINIMUM.md) | §1's Stripe Payment Link as launch infrastructure; the teardown as step one of the funnel |
| [`SITEMAP.md`](../SITEMAP.md) | Every page on the paid path |
| [`funnel.py`](funnel.py) | `DEPOSIT_COLD` is now a close rate. The variable name is the last trace of the old funnel |
| [`LTGP.md`](LTGP.md) | *"the deposit rate is the one input that can break it"* — still true, but it is now the **close** rate, and it is less measurable than a payment was |

**What does not change:** the offer, the fee, the guarantee, the EOR line, the gross
profit, the audience layers, the $5,000 test size, and the volume argument. **The offer was
never the teardown.**

