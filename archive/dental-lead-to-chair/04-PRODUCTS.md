# Product Specifications

Three modules. Every deliverable below is a real artifact you build and hand over.

**Architectural rule that governs everything:** the system is installed **inside the client's
stack** — their CRM, their phone number, their calendar, their sending identity. We configure
and manage; we don't take custody. That keeps the HIPAA burden at "BAA + access controls"
instead of "build your own compliant infrastructure," and it means every patient-facing message
goes out as the practice.

**Never integrate with the practice management system.** Work at the lead and CRM layer. You
need lead data and appointment data, not clinical records.

---

## Stack

| Layer | Tool | Notes |
|---|---|---|
| Orchestration | n8n (self-hosted) or Make | n8n preferred — cheaper at volume, self-hostable |
| CRM / pipeline | Client's existing, or GoHighLevel if none | GHL if you have to install one; it bundles SMS + email + calendar |
| SMS / voice | Client's Twilio subaccount or GHL | **Must be client-owned. BAA with Twilio required** |
| Calendar | Client's existing (Calendly, GHL, LocalMed) | |
| Lender portals | Native lender links | No integration needed — links only |
| Reporting | Looker Studio or Metabase on aggregate exports | **No PHI. Counts and rates only** |
| Video hosting | Loom or Vimeo (unlisted) | Pre-frame video |

---

# Module 1 — Speed + Show

**Target outcome: no-show rate 35% → 15%.**

## 1.1 Lead intake

Capture every inbound full-arch opportunity into one pipeline:

| Source | Method |
|---|---|
| Practice website form | Webhook → n8n |
| Landing page / ad lead forms | Native integration or webhook |
| Google LSA / Google Ads | Email parser or Zapier bridge |
| Inbound phone calls | Missed-call detection via Twilio; call tracking if available |
| Third-party lead vendors | Email parser |
| Referrals / walk-ins | Manual entry form for front desk |

**Deliverable:** one unified intake with source tagging, deduplication, and a normalized record.

## 1.2 Sub-60-second response

Fires on every new lead, 7 days a week:

**T+0 (immediate) — SMS from the practice number:**

> Hi [First], this is [Practice] — thanks for reaching out about full-arch implants. I have two
> consult times this week: [Slot A] or [Slot B]. Which works better?

**T+0 — call task created**, assigned to whoever is on duty, with a 5-minute SLA.

**T+5 min — if no reply:** outbound call attempt logged.

**T+30 min — if no reply, second SMS:**

> [First] — happy to answer questions before you commit to anything. Is [Slot A] or [Slot B]
> easier, or would you rather I call?

**Then:** T+4h, T+24h, T+48h, T+96h, then weekly for 3 weeks before moving to Module 3.

### Quiet hours

No outbound SMS before 8:00am or after 8:00pm in the **patient's** timezone. A lead that arrives
at 11pm gets its first message at 8:01am. Non-negotiable — this is a compliance control, not a
UX preference.

## 1.3 Qualification logic

Four questions, embedded in SMS conversation or asked on the call. Scored, not gatekept — the
purpose is routing and prep, not rejection.

| Question | Signal |
|---|---|
| "Is this for you or someone else?" | Decision maker identification |
| "Upper, lower, or both?" | Case value (single vs. dual arch) |
| "Are you looking to get this done in the next few months, or still researching?" | Timeline |
| "Have you had a CT scan or consult anywhere else?" | Shopping stage, prior objections |

**Routing:**
- Both arches + near-term = priority slot, senior consult person, flag for owner
- Researching = book anyway, but tag for the long-cycle sequence from day one
- Third-party decision maker = the confirmation sequence targets **both** contacts

## 1.4 Confirmation cadence

Four touches, plus the pre-frame video. This is where the no-show rate actually moves.

| Timing | Channel | Content |
|---|---|---|
| **At booking** | SMS + email | Confirmation, address, parking, what to bring, **pre-frame video link**, **financing pre-qual link** |
| **T−48h** | Email | Pre-frame video again + intake form + "bring whoever helps you decide" |
| **T−24h** | SMS | "Still good for [time] tomorrow? Reply Y to confirm or R to reschedule" |
| **T−2h** | SMS | "See you at [time]. We're at [address]. Text this number if you're running late" |

**The T−24h reply mechanic matters.** A patient who types "Y" has made a micro-commitment. A
patient who types "R" reschedules instead of ghosting — which converts a no-show into a future
consult.

## 1.5 The pre-frame video

4 minutes, the owner-dentist on camera, shot on a phone. This single asset does four jobs:
kills price shock, drives financing pre-qualification, gets the decision maker in the room, and
makes the patient feel committed.

### Script

> **[0:00]** "Hi, I'm Dr. [Name]. You're scheduled to come see us on [day]. I wanted to tell
> you exactly what's going to happen so there are no surprises."
>
> **[0:20]** "First we'll take a 3D scan of your jaw. It takes about ten minutes, there's no
> discomfort, and nothing goes in your mouth."
>
> **[0:45]** "Then you and I will sit down and look at that scan together. I'll tell you
> honestly whether you're a good candidate for full-arch treatment. Some people aren't, and
> if that's you, I'll tell you and I'll tell you what your other options are."
>
> **[1:30]** "Now let's talk about cost, because I'd rather you hear it from me now than be
> surprised in the chair. Full-arch treatment at our practice runs between $[X] and $[Y] per
> arch, depending on your bone and what materials we use."
>
> **[2:15]** "Almost nobody pays that out of pocket. Most of our patients finance it, and monthly
> payments usually land between $[A] and $[B]. There's a link below this video — it takes two
> minutes, it does **not** affect your credit score, and it tells you what you're approved for
> before you even come in. Please do it. It means we can have a real conversation about your
> options instead of guessing."
>
> **[3:15]** "Last thing. If there's someone who helps you make decisions like this — a spouse,
> an adult child — please bring them. This is a big decision and it goes better when everyone
> hears the same information at the same time."
>
> **[3:45]** "See you [day]. If anything comes up, text the number that sent you this."

### Production notes

- Phone camera, natural light, quiet room. Polish is not the point — the dentist's face is
- One take is fine. Warmth beats production value
- Shoot **two versions** if they treat both single and dual arch, so pricing is accurate
- Reshoot annually or whenever pricing changes

## 1.6 No-show recovery

Fires the moment the appointment slot passes without arrival:

| Timing | Channel | Content |
|---|---|---|
| **T+15 min** | SMS | "[First], we had you down for [time] — everything okay? Happy to move it" |
| **T+2h** | Call task | Human call, no voicemail-only |
| **T+24h** | SMS | "Still want to get that scan done? I can do [Slot A] or [Slot B]" |
| **T+72h** | Email | Pre-frame video again + "no pressure, just want to make sure you got answers" |
| **T+7d** | Call task | Final human attempt, then move to Module 3 |

**Deliverables for Module 1:** intake workflow, 6-message response sequence, 4-question
qualification script, 4-touch confirmation cadence, pre-frame video (shot and hosted), intake
form, reschedule flow, 5-touch no-show recovery, quiet-hours logic.

---

# Module 2 — Pre-Approved Arrival

**Target outcomes: 60% of patients arrive knowing their approved amount. 30–40% of declines
recovered.**

This is the highest-dollar module. Single-lender practices approve roughly 50% of full-arch
applicants; a properly routed waterfall reaches 70–80%.

## 2.1 The lender stack

Five lenders, applied for in the client's name during install. Positioned by typical credit
band and capacity.

| Tier | Lender | Typical band | Capacity | Role |
|---|---|---|---|---|
| 1 | **Proceed Finance** | 650+ | Up to $75k+ | Primary for full-arch — built for high-ticket dental |
| 1 | **Alphaeon Credit** | 640+ | $25k+ | Parallel primary, elective/aesthetic focus |
| 2 | **Cherry** | 580+ | $10–35k | Soft-pull prequal, fast, good UX |
| 2 | **Wisetack / LendingPoint** | 600+ | $10–35k | Secondary catch |
| 3 | **Sunbit** | 550+ | Up to ~$20k | Subprime catch, high approval |
| 3 | **HFD / in-house** | Varies | Varies | Down-payment + in-house split |

Verify current terms and merchant fees at install — these change. Track merchant discount rates
per lender; the practice needs to know its net.

## 2.2 The waterfall routing map

```
PATIENT SUBMITS PRE-QUAL (soft pull, pre-visit)
        │
        ├─ APPROVED for full plan ──────────────► Arrives pre-approved. Flag: PRE-APPROVED $X
        │
        ├─ APPROVED for partial ───────────────► Route to SPLIT PATH (§2.4)
        │
        └─ DECLINED
               │
               ├─ Auto-route to Tier 2 (Cherry / Wisetack)  ── approved? ──► PRE-APPROVED $X
               │                                                  │
               │                                                  └─ declined
               │                                                        │
               ├─ Auto-route to Tier 3 (Sunbit)  ── approved? ──► PRE-APPROVED $X
               │                                        │
               │                                        └─ declined
               │                                              │
               └─ CO-APPLICANT PATH ──► spouse/adult child applies ──► approved? ──► PRE-APPROVED
                                                                             │
                                                                             └─ declined
                                                                                   │
                                                                    PHASED TREATMENT PATH (§2.5)
```

**Critical design rule:** a decline must never terminate a conversation. Every decline branch
has a next action, automatically triggered, with a human task attached.

## 2.3 Pre-qual placement

The pre-qual link appears in **five** places. Redundancy is the point.

1. Booking confirmation SMS
2. Booking confirmation email
3. Below the pre-frame video (with the dentist verbally asking for it)
4. T−48h email
5. Intake form completion page

**Track completion rate.** If under 40%, the pre-frame video ask is too weak — reshoot it.

## 2.4 Split-funding paths

| Situation | Path |
|---|---|
| Approved for $22k, plan is $38k | Lender 1 at $22k + down payment + in-house on remainder |
| Two arches needed | Finance upper now, lower in 6 months (two applications, two approvals) |
| Declined solo | Co-applicant: spouse or adult child as primary |
| Thin file, good income | Manual underwriting request with income documentation |

## 2.5 Phased treatment path

When every financing route fails, the answer is not "no." It's a smaller yes:

Extractions and immediate denture now → implants in 6–12 months. Keeps the patient in the
practice, generates immediate revenue, and preserves the full-arch case for later. Build a
dedicated 6-month sequence for this cohort.

## 2.6 Presentation scripts

Four scripts. The through-line: **monthly payment before total price, always.**

**Script A — the money conversation opener**
> "Before we look at the scan, let me tell you how people pay for this, because it's usually the
> first thing on people's minds. Treatment like yours runs $[X]. Most of our patients don't pay
> that up front — they're at about $[Y] a month. You already got pre-approved for $[Z] before
> you came in, so we know what we're working with. Sound okay to keep going?"

**Script B — "I need to think about it"**
> "Completely fair — this is a big decision. Can I ask what specifically you want to think
> about? Is it the money, the surgery itself, or the timing?"
>
> *[Then handle the actual objection instead of the stated one.]*
>
> "Here's what I'd suggest either way: let's hold a surgical date. It's refundable, it costs you
> nothing to hold, and my next opening after this one is [X weeks] out. If you decide against it,
> you cancel and you've lost nothing."

**Script C — the decline**
> "So that lender came back as a no — which honestly happens a lot and usually says more about
> their algorithm than about you. We work with five. Let me run the next one, it takes about two
> minutes. And if none of them work, there's a way to phase this so you're not waiting years."

**Script D — the absent decision maker**
> "It sounds like [spouse/son/daughter] is part of this decision. Rather than you going home and
> trying to explain a 3D scan secondhand — can we get them on a video call for ten minutes right
> now? Or I'll hold this slot and you both come back Thursday."

## 2.7 Approval tracking

Weekly report, aggregate only, no PHI:

| Metric | Why |
|---|---|
| Pre-qual completion rate | Is the pre-frame ask working? |
| Approval rate by lender | Which lender to lead with |
| Approval rate by tier | Waterfall effectiveness |
| Declines recovered by tier 2/3 | The core value proof |
| Co-applicant conversion rate | Is the script being used? |
| Average approved amount vs. average case value | Pricing/capacity gap |

**Deliverables for Module 2:** 5 lender applications submitted and approved, waterfall routing
automation, pre-qual links placed in 5 locations, decline recovery branches with human tasks,
split-funding decision tree, phased-treatment sequence, 4 presentation scripts, approval
tracking dashboard.

---

# Module 3 — Long-Cycle Recovery

**Target outcome: 1–2 recovered cases per month.**

A full-arch decision takes 3–7 months. Most practices follow up twice and stop. Eleven patients
per month enter this pile at a typical practice — that's $385,000 of pipeline nobody is working.

**Consent posture:** everyone in this sequence **physically attended a consultation.** That's an
established treatment relationship — a materially stronger position than reactivating cold web
leads. Still: honor opt-outs instantly, respect quiet hours, and the client warrants consent.

## 3.1 The 6-month sequence

| Week | Channel | Content |
|---|---|---|
| **1** | Email | Recap: their scan findings, their specific plan, their approved amount, monthly figure |
| **2** | SMS | Patient story — someone with a similar situation, 60-second video |
| **3** | Email | **"What happens if you wait"** — progressive bone resorption, with their own scan referenced |
| **4** | **Call task** | Human: "just checking in, any questions come up?" |
| **6** | Email | Financing explainer — reframe total as monthly, compare to a car payment |
| **8** | SMS | Patient story #2 — different objection profile |
| **10** | **Call task** | Human: "is there anything I can send you or your [spouse]?" |
| **13** | Email | Timing hook — new insurance year, HSA/FSA funds, new-year framing |
| **16** | **Call task** | Human: offer to re-run financing (approvals expire; credit may have improved) |
| **20** | Email | Bone-loss follow-up: offer a **free updated scan** to compare against the original |
| **24** | Email + Call task | Final: re-consult offer with updated scan, then move to quarterly |

After week 24: quarterly touch indefinitely. These patients don't stop having the problem.

## 3.2 Why the bone-loss angle is the strongest content

It is clinically true, verifiable on their own imaging, and creates real urgency without
manufactured scarcity. Alveolar bone resorbs progressively after tooth loss. Waiting genuinely
narrows options and can turn a straightforward case into one requiring grafting.

**Write it accurately and have the dentist approve the language.** This is the one place where
overstating would be both unethical and a liability. Accurate is also more persuasive.

## 3.3 Sample copy

**Week 3 email — the highest-performing message in the sequence**

> Subject: About your scan, Dr. [Name] wanted you to know this
>
> [First],
>
> When you came in on [date], we took a 3D scan of your jaw. Dr. [Name] asked me to pass along
> one thing about it.
>
> When teeth are missing, the bone that used to hold them starts to shrink. It's gradual and you
> won't feel it happening. But it means the options available to you now aren't necessarily the
> options available in a year.
>
> This isn't a sales pitch — plenty of people wait, and that's their call. But Dr. [Name] would
> rather you make that decision knowing what's actually happening rather than assuming nothing
> changes while you think it over.
>
> If you want to talk it through, reply to this email or call [number]. No appointment needed.
>
> [Coordinator name]
> [Practice]

**Week 16 SMS — re-run financing**

> [First] — [Coordinator] at [Practice]. Financing approvals expire after a few months, and
> yours has. If your situation has changed at all it's worth re-running — takes 2 minutes, no
> credit impact. Want me to send the link?

## 3.4 Recent-consult recovery (install week)

At install, pull every consult from the **last 90–180 days** that didn't proceed and enter them
into the sequence at the appropriate week based on elapsed time.

This is your fastest proof asset. A patient who consulted 60 days ago and never got a follow-up
is often still shopping, and consent is fresh. **Expect 1–3 recovered cases in the first 45 days
from this alone** — which is usually what makes the guarantee safe.

**Scope limit:** 180 days maximum. Do not go further back. Older records are a different
consent and reassigned-number risk profile and are not worth it.

## 3.5 Call task discipline

Module 3 has four human call tasks. They are assigned into the client's system with a 48-hour
SLA and they are the module's failure point — sequences run themselves, humans don't.

**Report task completion rate weekly.** If it drops below 70%, escalate to the owner
immediately. A client whose staff ignores call tasks will blame you for the results, and the
completion-rate report is your only defense.

**Deliverables for Module 3:** 11-touch 6-month sequence built and live, all email and SMS copy
written and dentist-approved, 2 patient story videos produced, bone-loss content clinically
reviewed, 4 call-task automations with SLA tracking, recent-consult backfill executed,
task-completion reporting.

---

## Install timeline — 21 days

| Days | Work | Client dependency |
|---|---|---|
| **1–3** | Kickoff. Audit current flow. Baseline consults-sat agreed **in writing**. BAA signed. System access granted | Owner, 90 min |
| **4–7** | Lender applications submitted (all 5). Intake workflow built. Pipeline configured | Owner signature on applications |
| **8–11** | Response + confirmation sequences built and tested. Quiet-hours logic verified | None |
| **12–14** | **Pre-frame video shot.** Intake form live. Pre-qual links placed | Owner, 60 min on camera |
| **15–17** | Module 3 sequence built. Recent-consult list pulled and backfilled | Front desk export |
| **18–20** | Presentation scripts handed over. Consult person walkthrough (60 min, not coaching — system training) | Consult person, 60 min |
| **21** | **Go live.** Reporting dashboard delivered. Guarantee clock starts | — |

**The two client dependencies that delay every install:** lender application signatures and the
pre-frame video shoot. Chase both from day one. Make the video a contractual condition of the
guarantee.
