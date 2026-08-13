#!/usr/bin/env python3
"""
The workflows to set up, not the activities to do.

The correction that produced this file: SURFACES.md listed 62 *activities*. An activity
is a thing you do. A **workflow** is trigger -> steps -> output, set up once, and the
point of it is that it runs afterwards **without you deciding anything**. With no
employees, workflows are the only leverage that exists -- every one you do not build is
a decision you make again every week, forever.

Cold email was the example given, and it is the right one: it is not an activity, it is
**23 steps across four stages**, two of which have multi-week lead times that will
silently delay launch if they are not started first.

This file does three things:
  1. inventories the workflows and ranks them on when they must exist
  2. decomposes cold email fully, because it was asked for and because it is the
     longest-lead-time system in the business
  3. models cold-email economics against the SAME funnel constants as Meta, so the two
     channels are comparable rather than vibes. Deliberately solved as a BREAKEVEN --
     "what reply rate do you need" -- rather than by inventing a reply rate.

Run:  python3 scoring/workflows.py > /dev/null   (writes WORKFLOWS.md)
"""
import contextlib
import io
import sys

sys.path.insert(0, "scoring")
with contextlib.redirect_stdout(io.StringIO()):
    import funnel as fn

OUT = "WORKFLOWS.md"

FEE = fn.FEE                 # 6600
GP_RATE = fn.GP_RATE         # 0.62
FILL = fn.FILL               # 0.85
SALES_COST = fn.SALES_COST   # 60 per held call
META_CAC = 732.0             # blended, LTGP.md
GP30 = 4435.0

# cold-email funnel. Every rate here is [?] -- that is the point of solving breakevens.
POSITIVE_SHARE = 0.30    # of all replies, share that are positive [?]
MEETING_HELD = 0.60      # of positive replies, share that become a held call [?]
DEPOSIT = 0.24           # held call -> paid teardown. SAME as the Meta funnel
REPLY_RATES = [0.005, 0.01, 0.02, 0.03, 0.05]
TOOL_COST_MO = 150.0     # sending tool + verification + domains + mailboxes [?]
EMAILS_PER_MO = 3000.0   # 3 domains x 3 mailboxes x ~35/day [?]
# The first version of this model charged founder time ONLY for held calls, which made
# cold email look almost free. It is not: the real cost is attention, and it is spent
# on every reply and every hour of list-building. Both are now counted.
MIN_PER_REPLY = 5.0      # triage + respond, every reply not just positive ones [?]
HOURS_PER_1K_LIST = 1.0  # residual manual work after the pipeline does the bulk [?]

# (workflow, stage, when it must exist, lead time, surface, steps, why)
WF = [
 ("Cold email pipeline", "Acquisition", "Week 1 setup, Week 4 send", "**3–4 weeks**", "Code",
  22, "**Longest lead time in the business.** Domain warm-up alone is 2–4 weeks, so if this "
  "starts in week 4 it sends in week 8. Start it first even though it launches last"),
 ("Meta ads loop", "Acquisition", "Week 3", "1 week", "Code",
  9, "Creative → launch → read → reallocate, weekly. The primary channel"),
 ("Intent-seed audience refresh", "Acquisition", "Week 2, monthly after", "3 days", "Code",
  7, "**25% of spend at the best CAC in the model.** Job postings go stale, so this is a "
  "recurring rebuild, not a one-off build"),
 ("Inbound lead → teardown → call", "Acquisition", "Week 3", "3 days", "Code",
  8, "The handoff every paid click depends on. Form → payment → calendar → confirmation"),
 ("Teardown production", "Sales", "Week 2", "1 week", "Code",
  7, "The paid deliverable. **A generator, not a bespoke job** — that is what makes it "
  "survive client ten"),
 ("Pre-call → call → follow-up", "Sales", "Week 3", "2 days", "Code",
  6, "Research brief in, notes out, follow-up same day"),
 ("Proposal → contract → invoice → kickoff", "Sales", "Week 4", "3 days", "Cowork",
  7, "The close. Templated once so no deal stalls on paperwork"),
 ("Sourcing → screen → take-home → grade → bench", "Supply", "Week 2", "1 week", "Code",
  10, "**You cannot sell a placement you cannot fill.** This has to run ahead of demand"),
 ("Client brief → shortlist of three", "Supply", "Week 4", "2 days", "Cowork",
  6, "The match. Where the graded bench turns into revenue"),
 ("Bench nurture", "Supply", "Month 2", "2 days", "Cowork",
  5, "Graded people go cold. A monthly touch keeps the bench real rather than historical"),
 ("Placement onboarding, day 0–30", "Delivery", "Before placement 1", "3 days", "Cowork",
  9, "Protects **seat continuity — the largest single lever in the business**"),
 ("30 / 60 / 90 check-in cadence", "Delivery", "Month 2", "2 days", "Cowork",
  6, "The mechanism that turns 9 EOR months into 30, worth **+$9,022 per client**"),
 ("Replacement request handling", "Delivery", "Before placement 1", "1 day", "Cowork",
  6, "The 12-month guarantee is the cheapest differentiation you have — and only if it is "
  "fast"),
 ("Seat expansion play", "Delivery", "Month 3", "2 days", "Chat",
  5, "Seats-per-client is where the economics actually live"),
 ("Monthly EOR run", "Finance", "Month 2", "3 days", "Cowork",
  8, "Salaries out, invoices out, reconcile. **$477/employee/month recurring**"),
 ("Cash-flow forecast", "Finance", "Week 4", "2 days", "Code",
  6, "**You pay talent monthly and get paid lumpily.** The failure mode that kills "
  "placement businesses, and nothing in the repo models it yet"),
 ("Collections chase", "Finance", "Month 2", "1 day", "Cowork",
  5, "Polite, automatic, escalating. Founders are bad at this and it costs them"),
 ("Weekly metrics review", "Measurement", "Week 4", "1 day", "Code",
  5, "One command, six numbers, fifteen minutes"),
 ("Monthly model re-run + decision memo", "Measurement", "Month 2", "2 days", "Code",
  6, "**Replace assumptions with actuals and re-derive everything.** The compounding use"),
 ("Competitor and market monitor", "Measurement", "Month 2", "1 day", "Code",
  4, "Scheduled diffs on pricing pages and salary benchmarks. Runs without you"),
 ("Proof-page production", "Content", "Week 2", "ongoing", "Chat",
  6, "Each recut → retention delta → published. **The page that makes premium falsifiable**"),
 ("Case-study production", "Content", "Month 3", "2 days", "Cowork",
  6, "Only with real numbers"),
 ("SOP capture", "Ops", "Continuous", "0", "Cowork",
  4, "**The substitute for employees.** Anything done twice gets written down once"),
 ("Referral request loop", "Acquisition", "Month 3", "1 day", "Cowork",
  5, "After a successful 90-day check-in, ask. Systematically, not when you remember"),
 ("Trademark and brand monitor", "Legal", "Week 2", "1 day", "Code",
  3, "Class 35 is still outstanding, and two live users of *All Hands* exist in talent "
  "services"),
]

# ---- cold email, fully decomposed --------------------------------------------
COLD = [
 ("A. Infrastructure", "**3–4 weeks lead time. Start week 1.**", [
  ("Buy 2–3 **separate sending domains**", "Code",
   "**Never send from `allhandstalent.com`.** One spam complaint spike and the domain your "
   "ads land on is damaged. Use lookalikes you already own or cheap variants — "
   "`allhandtalent.com` is free and was already flagged as the one typo worth buying"),
  ("Point each domain's DNS at a mail provider", "Code", "Google Workspace or similar"),
  ("**SPF, DKIM and DMARC on every sending domain**", "Code",
   "Start DMARC at `p=none`, watch reports, then move to `quarantine`. Missing any of the "
   "three is the single most common reason cold email lands in spam"),
  ("2–3 mailboxes per domain", "Code", "Spreads volume, contains damage"),
  ("Custom tracking domain — **or turn open-tracking off**", "Code",
   "Open-tracking pixels on a shared tracking domain are a known deliverability drag. "
   "**Reply rate is the metric that matters anyway**, and it needs no pixel"),
  ("**Warm-up, 2–4 weeks, ramping to volume**", "Code",
   "The step that cannot be compressed. This is why the workflow starts first and sends last"),
  ("Daily cap per mailbox, 20–40", "Code", "Volume comes from mailbox count, not per-box cap"),
  ("Unsubscribe mechanism and suppression list", "Code",
   "Legally required in several jurisdictions and operationally essential. Existing clients, "
   "opt-outs, competitors, anyone already in the Meta funnel"),
 ]),
 ("B. List build", "Recurring — weekly", [
  ("Define the ICP filter", "Chat",
   "`MAP.md` says marketing agencies and e-comm brands. Add size, spend signal, geography"),
  ("**Source companies from job postings**", "Code",
   "The same pipeline as the intent seed. A company hiring an editor is a company with the "
   "problem, dated"),
  ("Source from the **Meta Ad Library**", "Code",
   "**Who is running many ads is who has creative volume** — the sharpest available signal "
   "for this specific offer, and it is public"),
  ("Source from agency directories and e-comm tech stacks", "Code",
   "Broader, colder, cheaper"),
  ("Find the decision maker, then the address", "Code",
   "Founder or head of creative at agencies; founder or growth lead at brands"),
  ("**Verify every address before sending**", "Code",
   "Bounce rate above ~2–3% damages the domain. Verification is the cheapest insurance in "
   "the whole workflow"),
  ("Deduplicate against Meta audiences and the suppression list", "Code",
   "Do not cold-email someone currently seeing your ads — it looks careless and it "
   "contaminates attribution"),
 ]),
 ("C. Message", "Per campaign", [
  ("Pick the angle", "Chat",
   "Anchor on the **vendor invoice, $5,000–16,500/month for a studio** — the largest true "
   "claim in the study. Not on salary arbitrage"),
  ("**One personalisation line drawn from their own data**", "Code",
   "Their live ad, or the role they just posted. **This is what makes cold email work**, and "
   "it is the part that does not scale by hand"),
  ("Write a 3–4 touch sequence", "Chat",
   "Short. One ask. The teardown is the ask, not a call — a paid teardown is a lower-"
   "friction yes than an hour of their time, and it is the money gate"),
  ("Copy review against the brand voice", "Chat", "So email, ads and site sound like one firm"),
 ]),
 ("D. Run and measure", "Daily / weekly", [
  ("Launch and watch bounce, spam and reply rates daily", "Code",
   "Pause immediately on a bounce spike — that is a list problem, not a copy problem"),
  ("**Reply triage**: interested / objection / not now / never", "Cowork",
   "Four buckets, four responses. Never lets an interested reply sit overnight"),
  ("Route interested → teardown → calendar", "Code",
   "**Same gate as paid traffic.** One pipeline after the first touch, not two"),
  ("Weekly: reply rate, positive rate, meetings, **cost per placement**", "Code",
   "And compare it to Meta's $732. §3 computes what you need to hit"),
 ]),
]


def main():
    L = []
    P = L.append
    P("# Workflows, Not Activities\n")
    P("> *\"We need to set up workflows for so many things — for example cold email.\"*\n")
    P("Correct, and [`SURFACES.md`](SURFACES.md) has the wrong shape for it. It lists 62 "
      "**activities** —\nthings you do. A **workflow** is *trigger → steps → output*, built "
      "once, and the whole point is that\nafterwards **it runs without you deciding "
      "anything**.\n")
    P("> With no employees, workflows are the only leverage that exists. **Every workflow you "
      "do not build\n> is a decision you make again every week, forever.**\n")
    P(f"**{len(WF)} workflows below.** Cold email is decomposed in full in §2, because it was "
      "the example and\nbecause it is the **longest-lead-time system in the business** — "
      "domain warm-up alone is 2–4 weeks,\nso a pipeline started in week four does not send "
      "until week eight.\n")

    P("---\n\n## 1. The inventory\n")
    P("Ordered by **when it must exist**, not by how interesting it is.\n")
    P("| Workflow | Stage | Must exist | Lead time | Steps | Surface | Why |")
    P("|---|---|---|---|---|---|---|")
    order = {"Week 1 setup, Week 4 send": 0, "Week 2": 1, "Before placement 1": 2,
             "Week 3": 3, "Week 2, monthly after": 1, "Week 4": 4, "Continuous": 0,
             "Month 2": 5, "Month 3": 6}
    for w, st, when, lead, sur, steps, why in sorted(WF, key=lambda x: order.get(x[2], 9)):
        P(f"| **{w}** | {st} | {when} | {lead} | {steps} | {sur} | {why} |")
    P("")
    tot = sum(x[5] for x in WF)
    P(f"**{tot} discrete steps across {len(WF)} workflows.** That number is the argument: none "
      "of this is\nremembered reliably by a person running everything alone. It is written "
      "down once or it is\nre-improvised weekly.\n")

    P("---\n\n## 2. Cold email, fully decomposed\n")
    n = sum(len(x[2]) for x in COLD)
    P(f"**{n} steps in four stages.** Stage A is the one that will silently delay your launch "
      "if you leave\nit until you feel ready to send.\n")
    for stage, timing, steps in COLD:
        P(f"### {stage} — *{timing}*\n")
        P("| Step | Surface | Note |\n|---|---|---|")
        for s, sur, note in steps:
            P(f"| {s} | `{sur}` | {note} |")
        P("")

    P("---\n\n## 3. Does cold email actually beat Meta? Solve, do not guess\n")
    P(f"Meta's blended CAC is **${META_CAC:,.0f}** with 30-day GP of **${GP30:,.0f}** — "
      f"**{GP30/META_CAC:.2f}:1**. Cold email\nis not free: it costs tool spend and, far more "
      "expensively, **your attention on every reply**.\n")
    P("So rather than invent a reply rate, this solves for **what you would need to hit** — "
      "using the\n**same** downstream constants as the Meta funnel, so the comparison is "
      "real:\n")
    P(f"- positive share of replies **{POSITIVE_SHARE:.0%}** `[?]` · held-meeting rate "
      f"**{MEETING_HELD:.0%}** `[?]`\n- teardown take-up **{DEPOSIT:.0%}** — *the same 24% "
      f"the Meta model uses* · fill rate **{FILL:.0%}**\n- tooling **${TOOL_COST_MO:,.0f}/mo** "
      f"`[?]` · **${SALES_COST:.0f}** of your time per held call, from `funnel.py`\n")
    P("| Reply rate | Emails per placement | Held calls | Cash cost | **Your hours** | "
      "vs Meta $732 |")
    P("|---|---|---|---|---|---|")
    for r in REPLY_RATES:
        per_email = r * POSITIVE_SHARE * MEETING_HELD * DEPOSIT * FILL
        emails = 1.0 / per_email
        held = emails * r * POSITIVE_SHARE * MEETING_HELD
        months = emails / EMAILS_PER_MO
        replies = emails * r
        hours = (replies * MIN_PER_REPLY / 60.0 + emails / 1000.0 * HOURS_PER_1K_LIST
                 + held)          # one hour per held call
        cost = months * TOOL_COST_MO + held * SALES_COST
        verdict = "**beats Meta**" if cost < META_CAC else "worse"
        P(f"| **{r:.1%}** | {emails:,.0f} | {held:.1f} | **${cost:,.0f}** | "
          f"**{hours:.1f} hrs** | {verdict} |")
    P("")
    # breakeven reply rate
    lo, hi = 0.0005, 0.20
    for _ in range(200):
        mid = (lo + hi) / 2
        per_email = mid * POSITIVE_SHARE * MEETING_HELD * DEPOSIT * FILL
        emails = 1.0 / per_email
        held = emails * mid * POSITIVE_SHARE * MEETING_HELD
        cost = emails / EMAILS_PER_MO * TOOL_COST_MO + held * SALES_COST
        if cost > META_CAC:
            lo = mid
        else:
            hi = mid
    be = (lo + hi) / 2
    per_email = be * POSITIVE_SHARE * MEETING_HELD * DEPOSIT * FILL
    r1 = 0.01
    e1 = 1 / (r1 * POSITIVE_SHARE * MEETING_HELD * DEPOSIT * FILL)
    h1 = (e1 * r1 * MIN_PER_REPLY / 60.0 + e1 / 1000.0 * HOURS_PER_1K_LIST
          + e1 * r1 * POSITIVE_SHARE * MEETING_HELD)
    P(f"> **In cash, cold email beats Meta at almost any plausible reply rate — breakeven is "
      f"about {be:.2%}.**\n> **In hours, it does not.** At a 1% reply rate one placement costs "
      f"roughly **{h1:.0f} hours of your\n> attention**: list work, {e1*r1:.0f} replies to "
      f"triage, and the calls themselves. The same placement\n> from Meta costs ~$732 and "
      f"**about an hour**.\n")
    P("**So the two channels are not competing for the same budget — they are competing for "
      "different\nresources.** Meta spends money you can raise. Cold email spends the one "
      "input you cannot buy more\nof, and [`MODEL-V2.md`](MODEL-V2.md) gap 11 already capped "
      "your media commitments for exactly this\nreason. Run cold email **because it is cheap "
      "when you have no money and time is all you have** — and\nexpect to cut it back the "
      "month paid starts working.\n")
    P(f"Two things that table makes obvious and that a list of activities never would:\n")
    P(f"1. **Volume is the whole game.** At a 1% reply rate you need "
      f"**{1/(0.01*POSITIVE_SHARE*MEETING_HELD*DEPOSIT*FILL):,.0f} emails per placement.** "
      f"That is\n   months of sending at 3,000/month — which is why mailbox count and warm-up "
      f"are the binding\n   constraint, not copy.\n")
    P("2. **Your time is most of the cost, not the tools.** The dominant term is "
      "`$60 × held calls`, not\n   the $150/month of software. Anything that raises *positive* "
      "reply rate is worth far more than\n   anything that raises raw reply rate — a reply you "
      "have to argue with costs the same as one that\n   books.\n")
    P("*Every rate marked `[?]` is an assumption. **Replace them after the first 1,000 emails "
      "and re-run\nthis file** — that is the same discipline `funnel.py` applies to the paid "
      "channel.*\n")

    P("---\n\n## 4. Build order\n")
    P("Sequenced by lead time, so nothing waits on something that takes weeks.\n")
    P("| Week | Build | Because |\n|---|---|---|")
    for wk, what, why in [
        ("**Week 1**", "**Cold-email infrastructure — stage A, all 8 steps**",
         "**2–4 week warm-up.** Nothing else here has a lead time you cannot compress"),
        ("Week 1", "Sourcing → screen → grade → bench",
         "You cannot sell a placement you cannot fill"),
        ("Week 2", "Teardown generator · intent-seed refresh · proof-page production",
         "The paid deliverable, the best audience, and the page that proves the claim"),
        ("Week 3", "Meta ads loop · inbound lead → teardown → call",
         "First spend. Verify CAPI with test events **before** the first dollar"),
        ("Week 4", "Cold email stages B–D go live · proposal → contract → invoice",
         "Warm-up is done. The close needs paperwork that does not stall"),
        ("Week 4", "Cash-flow forecast · weekly metrics review",
         "Before money moves, not after"),
        ("**Before placement 1**", "Onboarding day 0–30 · replacement handling",
         "Both are promises you have already made in the offer"),
        ("Month 2", "EOR run · check-in cadence · bench nurture · monthly model re-run",
         "The recurring machine"),
        ("Month 3", "Referral loop · case studies · seat expansion",
         "Only possible once there are placements to refer to"),
        ("Continuous", "**SOP capture**",
         "Anything done twice. This is what you hand a first hire instead of explaining"),
    ]:
        P(f"| {wk} | {what} | {why} |")
    P("")
    P("> **The one thing to take from this: start cold-email infrastructure in week one, even "
      "though it\n> sends in week four.** It is the only workflow here whose lead time you "
      "cannot buy your way out of,\n> and it is the one most likely to be left until it feels "
      "urgent — by which point it is four weeks\n> late.\n")
    open(OUT, "w").write("\n".join(L))
    print(f"{len(WF)} workflows, {sum(x[5] for x in WF)} steps; cold email {n} steps")
    print(f"breakeven reply rate vs Meta ${META_CAC:.0f}: {be:.2%}")
    for r in REPLY_RATES:
        pe = r * POSITIVE_SHARE * MEETING_HELD * DEPOSIT * FILL
        e = 1 / pe
        h = e * r * POSITIVE_SHARE * MEETING_HELD
        c = e / EMAILS_PER_MO * TOOL_COST_MO + h * SALES_COST
        print(f"  reply {r:.1%}: {e:8,.0f} emails, ${c:6,.0f}/placement")


if __name__ == "__main__":
    main()
