# What Actually Ports Across ICP × Role

> The middle slot of `LP → ??? → self-serve calendar`, decided on the dimension the
> enumeration was missing: **does it work unchanged across every cell we need to test?**

---

## 1. The volume calculator was wrong, and for a worse reason than "it's video-only"

It asks: *"what does your studio invoice **per ad**?"*

**No vendor in the study bills per unit.** From [`COMPETITORS.md`](COMPETITORS.md), fetched:

| Vendor | Billing |
|---|---|
| **Vidpros** — video | **$1,000/mo** part-time · **$4,000/mo** full-time |
| **Vidchops** — video | **Monthly subscription**, credits per month |
| Hireframe | **$2,500/mo** |
| GrowthAssistant | **$3,500/mo** |
| Athena · Oceans | Monthly |
| Design subscriptions, agency retainers, BPOs | Monthly |

> **Both video vendors bill monthly.** So the per-unit number the calculator asks for does
> not exist in the buyer's head even in the vertical it was designed for. They would have to
> divide a retainer by an output count to answer, and most cannot.

**And the structural error underneath it:** [`ALLFUNNELS.md`](ALLFUNNELS.md) ranked **137** funnels
with **no portability dimension at all.** I optimised for build simplicity and discovery
signal, and never scored the thing that was actually required.

`PORTABLE` is now a component property, taken as the **weakest link** across a funnel's
parts — because one non-porting component breaks the whole funnel — and weighted at **22**,
the heaviest. What that one change does:

| Offer | Ports | Best rank **before** | Best rank **now** |
|---|---|---|---|
| Volume calculator — units × vendor unit cost | **3** | **1st** | **32th** |
| Get a price / instant quote | **8** | 3rd | **8th** |
| See the graded bench | **5** | 5th | **25th** |
| Book a call | **10** | 8th | **9th** |
| Free document — scorecard, salary data, guide | **4** | 15th | **44th** |
| Watch a video first | **2** | 24th | **77th** |
| Paid micro-trial, $100–250 | **2** | 28th | **79th** |
| Free custom work on their asset | **2** | 60th | **120th** |

**The four options that need an asset rebuilt per role — video, free document, paid trial,
free custom work — were already losing. Portability just makes the reason explicit.**

---

## 2. What ports, ranked

| Offer | Ports | Best rank | Build days | Fields | `PERSUADE` | Score |
|---|---|---|---|---|---|---|
| **Monthly-spend comparison — what you pay now vs full-time** ✅ | **10** | 1 | 2.75 | 6 | 8.8 | 87.1 |
| **See the test — the graded rubric for that role, and a scored sample** ✅ | **9** | 3 | 3.5 | 6 | 10.0 | 84.2 |
| **"Three graded candidates in 7 days" — the shortlist promise** ✅ | **10** | 4 | 2.75 | 6 | 7.5 | 84.2 |
| **Get a price / instant quote** | **8** | 8 | 3 | 6 | 8.8 | 81.1 |
| **Book a call** | **10** | 9 | 2.25 | 5 | 5.0 | 80.9 |
| **Generic "contact us"** | **10** | 13 | 1.6 | 4 | 5.0 | 79.6 |
| **See the graded bench** | **5** | 25 | 3.5 | 5 | 10.0 | 73.1 |
| **Volume calculator — units × vendor unit cost** | **3** | 32 | 3.5 | 6 | 8.8 | 70.6 |
| **Join a newsletter / community** | **6** | 41 | 3.5 | 4 | 6.2 | 68.7 |
| **Free document — scorecard, salary data, guide** | **4** | 44 | 3.5 | 5 | 7.5 | 67.2 |
| **Watch a video first** | **2** | 77 | 5 | 4 | 8.8 | 60.2 |
| **Paid micro-trial, $100–250** | **2** | 79 | 3 | 5 | 10.0 | 59.4 |
| **Free custom work on their asset** | **2** | 120 | 2 | 4 | 10.0 | 45.4 |

**Three role-agnostic offers take the top four places**, and two of them did not exist in
the previous enumeration because I had not thought to look for them.

---

## 3. The three that survive

| | **A. Monthly-spend comparison** | **B. See the test** | **C. Shortlist promise** |
|---|---|---|---|
| The question it asks | *"What do you spend on this function per month?"* | *"Here is the test every one of these takes before you meet them"* | *"Three graded candidates in 7 days"* |
| Why it ports | **Every function has a monthly spend**, and it is the unit every vendor actually bills in | **Every role has a test.** The rubric changes; the mechanism does not | **Nothing in it is role-specific at all** |
| What it needs on day 1 | A salary band per role — a lookup, published for 60+ titles | **A written rubric per role** — which you must write anyway to grade anyone | Nothing |
| Build days | **2.75** | 3.0 | **2.25** — the cheapest |
| Fields captured | **6** | 5 | 5 |
| What it proves | Their spend is bigger than they thought | **We know how to judge this work** | Nothing yet — it is a promise |
| Precedent | Somewhere and Athyna both ship salary tools | **Nobody. Zero of ten** | Genius' *"See Pre-vetted Candidates"* |

### A. Monthly-spend comparison

| ✅ | |
|---|---|
| **Ports perfectly — 10** | Video, media buying, ops, design, books, support. Every one has a monthly spend, and the buyer knows it without doing arithmetic |
| **One input** | *"What do you spend on this per month?"* — against three for the volume calculator, two of which they could not answer |
| **The volume argument survives, in new units** | [`TEARDOWN.md`](../TEARDOWN.md) §4 said the only conclusion that sells is a *volume* problem, because volume is solved by a person. **"You are spending $4,000/month on this through a vendor" is the same argument in dollars instead of cuts** — and dollars port |
| **Precedented** | Somewhere's role→region tool and Athyna's LATAM salary tool are both this shape, across 60+ titles each — which is the portability proof |

| ❌ | |
|---|---|
| **It is the salary-arbitrage frame, and that was rejected on purpose** | [`MODEL-V2.md`](../MODEL-V2.md) §8 moved this business from price to quality, and [`REFERENCE.md`](../REFERENCE.md) §3 said explicitly *do not* build Somewhere's salary calculator. **This walks that back** |
| **It is a head-on collision with the category leader's axis** | *"80% less"* appears verbatim in **2 of 8** competitor headlines. Entering on their axis with no track record is the losing side of that fight |
| **It proves nothing about us** | Anyone can publish a cost comparison. It does not answer *can this person judge talent* |

### B. See the test

| ✅ | |
|---|---|
| **It is the only differentiated thing on the list** | **Zero of ten competitors shows a test or a score.** They show photos, titles and prices. This is [`MODEL-V2.md`](../MODEL-V2.md) §8's `TRUECLAIM` position made concrete |
| **Needs a rubric, not a bench** | The graded-bench option ranked 5th and now ranks 25th partly because it needs two hired, tested people per role before launch. **A rubric is a document you write in an afternoon** — and you must write it anyway |
| **It enforces the role filter automatically** | A role you cannot write a credible rubric for is a role you cannot grade. [`LAUNCH.md`](../LAUNCH.md)'s `FOUNDERGRADE`, applied by construction rather than by discipline |
| **It survives the bench paradox** | A placed candidate leaves the bench; **the test does not go anywhere.** The proof is in the method, not in the person |
| **Ports at 9** | The rubric differs per role; the page structure, the scoring format and the persuasion mechanism are identical |

| ❌ | |
|---|---|
| **Zero precedent, and that cuts both ways** | Ten operating companies all found other ways to prove quality. Either they are missing something or it does not work — and I cannot tell you which from here |
| **It is about us, not about them** | A rubric interests someone already considering. It may not stop a scroller the way *"you are spending $4,000/month on this"* does |
| **A rubric can be copied** | It is the one asset a competitor can lift in an afternoon. The defence is that they cannot copy *doing the grading*, but the page itself is not defensible |

### C. Shortlist promise

| ✅ | |
|---|---|
| **Cheapest to build — 2.25 days** | It is a sentence and a form |
| **Ports at 10** | Nothing in it is role-specific |
| **Precedented** | Genius leads with *"See Pre-vetted Candidates"* and it is their CTA |

| ❌ | |
|---|---|
| **It is a promise, not a proof** | From a named operator with a track record it is credible. **From an unknown, an unbacked promise is the weakest thing on this page** |
| **It carries a delivery cost the model does not see** | The page needs no human, so it scores `perlead = 0`. **But if sixty people request a shortlist you owe sixty shortlists.** The obligation is real and arrives later — which in practice forces it back to *"book a call and then I'll shortlist"*, which is what Genius does |
| **7 days is a promise you have not tested** | Somewhere quotes 3 days to candidates and 7–21 to filled. You have never run it once |

---

## 4. The answer: A then B, on one page

**A gives the reason to care. B gives the reason to trust.** They compose, they both port,
and the composition fixes A's worst problem.

```
  1.  Which seat is open?                     [ 6 buttons ]

  2.  What do you spend on it per month?      [ $4,000    ]
      Includes agency, freelancer, subscription, or your own time
           |
           v
      You spend            $48,000/yr
      Full-time, all-in    $19,800/yr
      Our fee, one-time     $5,940
      ----------------------------------
      Year one difference  $22,260

  3.  "But can you judge a good one?"          <- THE OBJECTION

      Here is the test every performance editor takes before you
      meet them, and a real scored submission:
        - recut one of the client's live ads, 48h
        - scored on 3-sec retention, 15-sec retention, brief adherence
        - sample: 41% -> 68% on 3-sec.  Score 8.1/10

  4.  [ See available times ]                  <- self-serve calendar
```

### Why the order matters

| | |
|---|---|
| **Cost first, then quality, never the reverse** | The cost line is what stops the scroll — it is about them. The test is what closes the objection the cost line creates, which is *"cheap offshore labour, and how would you know if they were any good?"* |
| **This is how the price frame gets neutralised** | Stating a cost gap and then immediately proving the grading is **not** competing on price — it is using price to earn attention and quality to earn the call. [`MODEL-V2.md`](../MODEL-V2.md) §8's objection was to *leading and ending* on price. **Ending on the test is the whole difference** |
| **Both blocks port** | Six seats change six labels, one salary band and one rubric. **No block is rebuilt, ever** — which is the requirement |
| **And it stays testable across, not down** | One page serves every ICP × role. The ICP lives in the ad, the role lives in button 1, and the conversion event is identical in all of them — so the cells are comparable |

### What each cell costs to add

| To add a role | Work |
|---|---|
| One button | Five minutes |
| One salary band | A lookup — Somewhere publishes bands for 60+ titles |
| **One rubric** | **An afternoon, and it is the only real cost.** A role you cannot write one for is a role you should not launch — which is the filter doing its job |
| One scored sample | One graded candidate for that role. **This is the gating item**, and it is one person, not the two-per-role a bench needs |

**One graded person per role instead of two, and a rubric instead of a bench.** That is
roughly half the day-1 asset cost of the bench option, for most of the trust.

---

## 5. What I got wrong, in order

| Pass | Claim | Why it was wrong |
|---|---|---|
| 1–3 | Ranked funnels on modelled CAC | Ninety invented conversion parameters compounded into three-significant-figure answers |
| 4 | Enumerated 137 funnels with no portability dimension | Optimised for build simplicity and discovery signal. **Never scored the requirement** |
| 5 | Recommended a volume calculator | It asks for a per-unit vendor price that **no vendor in my own competitor file charges** |

**What survives all five passes:** the landing page over on-platform (~17% vs ~2% appointment
rate), the self-serve calendar over any chase (32% vs 12% close, against a 10-hour gap), one
page and one ad set, and *a role with no measurable delta is not a role to launch.* Those
four have never moved, because each rests on a verified fact rather than on a model.

