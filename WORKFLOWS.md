# Workflows, Not Activities

> *"We need to set up workflows for so many things — for example cold email."*

Correct, and [`SURFACES.md`](SURFACES.md) has the wrong shape for it. It lists 62 **activities** —
things you do. A **workflow** is *trigger → steps → output*, built once, and the whole point is that
afterwards **it runs without you deciding anything**.

> With no employees, workflows are the only leverage that exists. **Every workflow you do not build
> is a decision you make again every week, forever.**

**25 workflows below.** Cold email is decomposed in full in §2, because it was the example and
because it is the **longest-lead-time system in the business** — domain warm-up alone is 2–4 weeks,
so a pipeline started in week four does not send until week eight.

---

## 1. The inventory

Ordered by **when it must exist**, not by how interesting it is.

| Workflow | Stage | Must exist | Lead time | Steps | Surface | Why |
|---|---|---|---|---|---|---|
| **Cold email pipeline** | Acquisition | Week 1 setup, Week 4 send | **3–4 weeks** | 22 | Code | **Longest lead time in the business.** Domain warm-up alone is 2–4 weeks, so if this starts in week 4 it sends in week 8. Start it first even though it launches last |
| **SOP capture** | Ops | Continuous | 0 | 4 | Cowork | **The substitute for employees.** Anything done twice gets written down once |
| **Intent-seed audience refresh** | Acquisition | Week 2, monthly after | 3 days | 7 | Code | **25% of spend at the best CAC in the model.** Job postings go stale, so this is a recurring rebuild, not a one-off build |
| **Teardown production** | Sales | Week 2 | 1 week | 7 | Code | The paid deliverable. **A generator, not a bespoke job** — that is what makes it survive client ten |
| **Sourcing → screen → take-home → grade → bench** | Supply | Week 2 | 1 week | 10 | Code | **You cannot sell a placement you cannot fill.** This has to run ahead of demand |
| **Proof-page production** | Content | Week 2 | ongoing | 6 | Chat | Each recut → retention delta → published. **The page that makes premium falsifiable** |
| **Trademark and brand monitor** | Legal | Week 2 | 1 day | 3 | Code | Class 35 is still outstanding, and two live users of *All Hands* exist in talent services |
| **Placement onboarding, day 0–30** | Delivery | Before placement 1 | 3 days | 9 | Cowork | Protects **seat continuity — the largest single lever in the business** |
| **Replacement request handling** | Delivery | Before placement 1 | 1 day | 6 | Cowork | The 12-month guarantee is the cheapest differentiation you have — and only if it is fast |
| **Meta ads loop** | Acquisition | Week 3 | 1 week | 9 | Code | Creative → launch → read → reallocate, weekly. The primary channel |
| **Inbound lead → teardown → call** | Acquisition | Week 3 | 3 days | 8 | Code | The handoff every paid click depends on. Form → payment → calendar → confirmation |
| **Pre-call → call → follow-up** | Sales | Week 3 | 2 days | 6 | Code | Research brief in, notes out, follow-up same day |
| **Proposal → contract → invoice → kickoff** | Sales | Week 4 | 3 days | 7 | Cowork | The close. Templated once so no deal stalls on paperwork |
| **Client brief → shortlist of three** | Supply | Week 4 | 2 days | 6 | Cowork | The match. Where the graded bench turns into revenue |
| **Cash-flow forecast** | Finance | Week 4 | 2 days | 6 | Code | **You pay talent monthly and get paid lumpily.** The failure mode that kills placement businesses, and nothing in the repo models it yet |
| **Weekly metrics review** | Measurement | Week 4 | 1 day | 5 | Code | One command, six numbers, fifteen minutes |
| **Bench nurture** | Supply | Month 2 | 2 days | 5 | Cowork | Graded people go cold. A monthly touch keeps the bench real rather than historical |
| **30 / 60 / 90 check-in cadence** | Delivery | Month 2 | 2 days | 6 | Cowork | The mechanism that turns 9 EOR months into 30, worth **+$9,022 per client** |
| **Monthly EOR run** | Finance | Month 2 | 3 days | 8 | Cowork | Salaries out, invoices out, reconcile. **$477/employee/month recurring** |
| **Collections chase** | Finance | Month 2 | 1 day | 5 | Cowork | Polite, automatic, escalating. Founders are bad at this and it costs them |
| **Monthly model re-run + decision memo** | Measurement | Month 2 | 2 days | 6 | Code | **Replace assumptions with actuals and re-derive everything.** The compounding use |
| **Competitor and market monitor** | Measurement | Month 2 | 1 day | 4 | Code | Scheduled diffs on pricing pages and salary benchmarks. Runs without you |
| **Seat expansion play** | Delivery | Month 3 | 2 days | 5 | Chat | Seats-per-client is where the economics actually live |
| **Case-study production** | Content | Month 3 | 2 days | 6 | Cowork | Only with real numbers |
| **Referral request loop** | Acquisition | Month 3 | 1 day | 5 | Cowork | After a successful 90-day check-in, ask. Systematically, not when you remember |

**171 discrete steps across 25 workflows.** That number is the argument: none of this is
remembered reliably by a person running everything alone. It is written down once or it is
re-improvised weekly.

---

## 2. Cold email, fully decomposed

**23 steps in four stages.** Stage A is the one that will silently delay your launch if you leave
it until you feel ready to send.

### A. Infrastructure — ***3–4 weeks lead time. Start week 1.***

| Step | Surface | Note |
|---|---|---|
| Buy 2–3 **separate sending domains** | `Code` | **Never send from `allhandstalent.com`.** One spam complaint spike and the domain your ads land on is damaged. Use lookalikes you already own or cheap variants — `allhandtalent.com` is free and was already flagged as the one typo worth buying |
| Point each domain's DNS at a mail provider | `Code` | Google Workspace or similar |
| **SPF, DKIM and DMARC on every sending domain** | `Code` | Start DMARC at `p=none`, watch reports, then move to `quarantine`. Missing any of the three is the single most common reason cold email lands in spam |
| 2–3 mailboxes per domain | `Code` | Spreads volume, contains damage |
| Custom tracking domain — **or turn open-tracking off** | `Code` | Open-tracking pixels on a shared tracking domain are a known deliverability drag. **Reply rate is the metric that matters anyway**, and it needs no pixel |
| **Warm-up, 2–4 weeks, ramping to volume** | `Code` | The step that cannot be compressed. This is why the workflow starts first and sends last |
| Daily cap per mailbox, 20–40 | `Code` | Volume comes from mailbox count, not per-box cap |
| Unsubscribe mechanism and suppression list | `Code` | Legally required in several jurisdictions and operationally essential. Existing clients, opt-outs, competitors, anyone already in the Meta funnel |

### B. List build — *Recurring — weekly*

| Step | Surface | Note |
|---|---|---|
| Define the ICP filter | `Chat` | `MAP.md` says marketing agencies and e-comm brands. Add size, spend signal, geography |
| **Source companies from job postings** | `Code` | The same pipeline as the intent seed. A company hiring an editor is a company with the problem, dated |
| Source from the **Meta Ad Library** | `Code` | **Who is running many ads is who has creative volume** — the sharpest available signal for this specific offer, and it is public |
| Source from agency directories and e-comm tech stacks | `Code` | Broader, colder, cheaper |
| Find the decision maker, then the address | `Code` | Founder or head of creative at agencies; founder or growth lead at brands |
| **Verify every address before sending** | `Code` | Bounce rate above ~2–3% damages the domain. Verification is the cheapest insurance in the whole workflow |
| Deduplicate against Meta audiences and the suppression list | `Code` | Do not cold-email someone currently seeing your ads — it looks careless and it contaminates attribution |

### C. Message — *Per campaign*

| Step | Surface | Note |
|---|---|---|
| Pick the angle | `Chat` | Anchor on the **vendor invoice, $5,000–16,500/month for a studio** — the largest true claim in the study. Not on salary arbitrage |
| **One personalisation line drawn from their own data** | `Code` | Their live ad, or the role they just posted. **This is what makes cold email work**, and it is the part that does not scale by hand |
| Write a 3–4 touch sequence | `Chat` | Short. One ask. The teardown is the ask, not a call — a paid teardown is a lower-friction yes than an hour of their time, and it is the money gate |
| Copy review against the brand voice | `Chat` | So email, ads and site sound like one firm |

### D. Run and measure — *Daily / weekly*

| Step | Surface | Note |
|---|---|---|
| Launch and watch bounce, spam and reply rates daily | `Code` | Pause immediately on a bounce spike — that is a list problem, not a copy problem |
| **Reply triage**: interested / objection / not now / never | `Cowork` | Four buckets, four responses. Never lets an interested reply sit overnight |
| Route interested → teardown → calendar | `Code` | **Same gate as paid traffic.** One pipeline after the first touch, not two |
| Weekly: reply rate, positive rate, meetings, **cost per placement** | `Code` | And compare it to Meta's $732. §3 computes what you need to hit |

---

## 3. Does cold email actually beat Meta? Solve, do not guess

Meta's blended CAC is **$732** with 30-day GP of **$4,435** — **6.06:1**. Cold email
is not free: it costs tool spend and, far more expensively, **your attention on every reply**.

So rather than invent a reply rate, this solves for **what you would need to hit** — using the
**same** downstream constants as the Meta funnel, so the comparison is real:

- positive share of replies **30%** `[?]` · held-meeting rate **60%** `[?]`
- teardown take-up **24%** — *the same 24% the Meta model uses* · fill rate **85%**
- tooling **$150/mo** `[?]` · **$60** of your time per held call, from `funnel.py`

| Reply rate | Emails per placement | Held calls | Cash cost | **Your hours** | vs Meta $732 |
|---|---|---|---|---|---|
| **0.5%** | 5,447 | 4.9 | **$566** | **12.6 hrs** | **beats Meta** |
| **1.0%** | 2,723 | 4.9 | **$430** | **9.9 hrs** | **beats Meta** |
| **2.0%** | 1,362 | 4.9 | **$362** | **8.5 hrs** | **beats Meta** |
| **3.0%** | 908 | 4.9 | **$340** | **8.1 hrs** | **beats Meta** |
| **5.0%** | 545 | 4.9 | **$321** | **7.7 hrs** | **beats Meta** |

> **In cash, cold email beats Meta at almost any plausible reply rate — breakeven is about 0.31%.**
> **In hours, it does not.** At a 1% reply rate one placement costs roughly **10 hours of your
> attention**: list work, 27 replies to triage, and the calls themselves. The same placement
> from Meta costs ~$732 and **about an hour**.

**So the two channels are not competing for the same budget — they are competing for different
resources.** Meta spends money you can raise. Cold email spends the one input you cannot buy more
of, and [`MODEL-V2.md`](MODEL-V2.md) gap 11 already capped your media commitments for exactly this
reason. Run cold email **because it is cheap when you have no money and time is all you have** — and
expect to cut it back the month paid starts working.

Two things that table makes obvious and that a list of activities never would:

1. **Volume is the whole game.** At a 1% reply rate you need **2,723 emails per placement.** That is
   months of sending at 3,000/month — which is why mailbox count and warm-up are the binding
   constraint, not copy.

2. **Your time is most of the cost, not the tools.** The dominant term is `$60 × held calls`, not
   the $150/month of software. Anything that raises *positive* reply rate is worth far more than
   anything that raises raw reply rate — a reply you have to argue with costs the same as one that
   books.

*Every rate marked `[?]` is an assumption. **Replace them after the first 1,000 emails and re-run
this file** — that is the same discipline `funnel.py` applies to the paid channel.*

---

## 4. Build order

Sequenced by lead time, so nothing waits on something that takes weeks.

| Week | Build | Because |
|---|---|---|
| **Week 1** | **Cold-email infrastructure — stage A, all 8 steps** | **2–4 week warm-up.** Nothing else here has a lead time you cannot compress |
| Week 1 | Sourcing → screen → grade → bench | You cannot sell a placement you cannot fill |
| Week 2 | Teardown generator · intent-seed refresh · proof-page production | The paid deliverable, the best audience, and the page that proves the claim |
| Week 3 | Meta ads loop · inbound lead → teardown → call | First spend. Verify CAPI with test events **before** the first dollar |
| Week 4 | Cold email stages B–D go live · proposal → contract → invoice | Warm-up is done. The close needs paperwork that does not stall |
| Week 4 | Cash-flow forecast · weekly metrics review | Before money moves, not after |
| **Before placement 1** | Onboarding day 0–30 · replacement handling | Both are promises you have already made in the offer |
| Month 2 | EOR run · check-in cadence · bench nurture · monthly model re-run | The recurring machine |
| Month 3 | Referral loop · case studies · seat expansion | Only possible once there are placements to refer to |
| Continuous | **SOP capture** | Anything done twice. This is what you hand a first hire instead of explaining |

> **The one thing to take from this: start cold-email infrastructure in week one, even though it
> sends in week four.** It is the only workflow here whose lead time you cannot buy your way out of,
> and it is the one most likely to be left until it feels urgent — by which point it is four weeks
> late.
