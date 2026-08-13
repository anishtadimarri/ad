#!/usr/bin/env python3
"""
THE MASTERLIST. One page. Everything else defers to this.

Fair criticism: four overlapping documents now exist -- CLAUDE-CODE.md (33 uses),
SURFACES.md (62 activities), WORKFLOWS.md (25 systems), ACTIVITIES.md (106 activities).
Each was a better pass than the last, and together they are unusable, because a person
running a company alone needs **one list**, not four views of one.

So this file **imports** from the others rather than restating them. activities.A and
workflows.WF are the single sources of truth; if either changes, this regenerates and
stays consistent. That is the whole reason it is a script and not a document.

Structure, in the order a solo operator actually needs it:
  1. the critical path  -- what blocks what, in dependency order
  2. the calendar       -- what to do in which week
  3. the full list      -- 106 activities by function, ranked, with surface
  4. the workflows      -- the 25 systems and when each must exist
  5. the do-not list    -- where an agent is the wrong tool
  6. the doc index      -- what supersedes what

Run:  python3 scoring/masterlist.py > /dev/null   (writes MASTERLIST.md)
"""
import contextlib
import io
import sys

sys.path.insert(0, "scoring")
with contextlib.redirect_stdout(io.StringIO()):
    import activities as ACT
    import workflows as WFM

OUT = "MASTERLIST.md"

# Explicit dependency sequence for the blockers. Score order is wrong here by
# construction -- a blocker's rank is set by what it unblocks, not by its value.
DEP = [
    "Decide the entity structure", "Register the entity", "Business bank account",
    "Choose the payment rail", "Payout rail", "W-8BEN-E", "GST registration",
    "Decide: are you the EOR", "Contractor vs employee", "Talent contract",
    "Rate card and the fee definition", "Guarantee terms", "MSA and per-placement SOW",
    "LinkedIn company page", "Pixel, CAPI and event", "UTM and naming",
    "Self-reported attribution", "Meta Business Manager structure",
    "Client ad-account access", "Cold-email infrastructure", "Email verification",
    "Cash-flow forecast",
]

# The calendar. (when, why this week, [items])
CAL = [
 ("**Week 0 — start the long clocks**",
  "Two things here have lead times measured in weeks. **Everything else can be compressed; "
  "these cannot.** Left until they feel urgent, each costs a month",
  ["**Entity decision → registration → bank → payment rails.** The India→US chain, and "
   "nothing gets paid until it is done",
   "**Cold-email infrastructure**: domains, SPF/DKIM/DMARC, mailboxes, **warm-up begins**",
   "Decide **EOR yourself or partner** — it changes what you are building",
   "Runway and personal burn: how many months of zero revenue you can absorb"]),
 ("**Week 1 — the things you cannot sell without**",
  "Supply must lead demand, and the offer must be unambiguous before anyone reads it",
  ["Sourcing → screen → take-home → **grade** → bench",
   "**Rate card and fee definition** — one-time, 30–35% of first-year comp. `MODEL-V2.md` "
   "gap 1 breaks the model 8× if this stays ambiguous",
   "Guarantee terms — 12-month replacement, no cash refunds",
   "Talent contract with **IP assignment** and non-solicit; MSA and SOW drafts",
   "**Count job postings across all three phrasings** — free, one afternoon, decides the ad"]),
 ("**Week 2 — the assets that do the selling**",
  "Each of these is reused on every deal for the life of the business",
  ["**Teardown generator** — the money gate as a product, not a bespoke job",
   "**Grading rubric as a scoring tool** — 3s and 15s retention vs the original",
   "Intent-seed audience built from scraped job postings",
   "`/proof` write-ups · landing-page copy for `/agencies`, `/ecommerce`, `/teardown`",
   "LinkedIn company page — the first thing a Western buyer checks",
   "**Meta Business Manager structure and a spare ad account**, before you need it"]),
 ("**Week 3 — first spend**",
  "Nothing here is reversible once money is moving, so the measurement scaffolding goes "
  "first",
  ["**UTM discipline and the self-reported attribution field** — impossible to retrofit",
   "**Pixel and CAPI verified with test events** — every CAC number assumes attribution works",
   "Inbound: form → Stripe payment link → calendar → confirmation",
   "Meta ads live. Special Ad Category pre-check first",
   "Pre-call research brief, running before the first call"]),
 ("**Week 4 — close and count**",
  "Cold email sends now because warm-up started in week 0",
  ["Cold email stages B–D go live",
   "Proposal → contract → invoice → kickoff, templated",
   "**Cash-flow forecast** — you pay talent monthly and get paid lumpily",
   "Weekly metrics review, one command"]),
 ("**Before placement one**",
  "Both are promises already made in the offer. Making them true after the fact is expensive",
  ["Onboarding day 0–30 · 30/60/90 cadence",
   "Replacement handling · escalation path for mid-month underperformance",
   "**Client ad-account access protocol** — partner access, 2FA, documented revocation",
   "Time-zone overlap and comms norms agreed in writing at kickoff"]),
 ("**Month 2 — the recurring machine**", "Everything that has to happen every month",
  ["Monthly EOR run · invoicing · collections",
   "**Monthly model re-run** — replace assumptions with actuals and re-derive everything",
   "Bench nurture · competitor and salary monitors",
   "**Win/loss analysis** on every dead deal"]),
 ("**Month 3–6 — compounding**", "Only possible once placements exist",
  ["Case studies with real numbers · referral loop after each 90-day check-in",
   "Seat expansion · cohort and payback analysis",
   "`/talent` page, footer-only and `noindex`, with the pass rate on it",
   "First VA or recruiter — **the SOPs are what make this hire cheap**"]),
]

SUPERSEDED = [
 ("[`ACTIVITIES.md`](ACTIVITIES.md)", "106 activities, 22 blockers, 18 functions",
  "**Still the reference table.** This file is its front page"),
 ("[`WORKFLOWS.md`](WORKFLOWS.md)", "25 systems, cold email in 23 steps, cold-email CAC model",
  "**Still authoritative on cold email** and on the channel comparison"),
 ("[`SURFACES.md`](SURFACES.md)", "62 activities across three surfaces",
  "**Superseded** — ACTIVITIES.md contains it and adds the blockers it missed"),
 ("[`CLAUDE-CODE.md`](CLAUDE-CODE.md)", "33 uses of Claude Code",
  "**Superseded** — first pass, kept for the reasoning in its §1"),
]


def main():
    W = dict(ACT.DIM)

    def sc(i, v, t, f, n, r):
        d = {"IMPORTANCE": i, "VALUE": v, "TIMESAVED": t, "FIT": f, "NOW": n, "REUSE": r}
        return sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100

    rows = [(sc(i, v, t, f, n, r), fn_, act, sur, blk, why)
            for fn_, act, sur, blk, i, v, t, f, n, r, why in ACT.A]
    rows.sort(key=lambda x: -x[0])
    blockers = [x for x in rows if x[4]]

    def dep_rank(x):
        for i, frag in enumerate(DEP):
            if frag.lower() in x[2].lower():
                return i
        return 99

    L = []
    P = L.append
    P("# MASTERLIST — All Hands Talent\n")
    P("**One page. Everything else defers to this.**\n")
    P(f"{len(ACT.A)} activities · {len(blockers)} blockers · {len(WFM.WF)} workflows · "
      f"{len(set(x[0] for x in ACT.A))} functions.\nGenerated from "
      "[`activities.py`](scoring/activities.py) and [`workflows.py`](scoring/workflows.py), "
      "so it **cannot drift**\nout of sync with them.\n")
    P("> **Read §1 and §2. That is the operating document.** §3 onward is reference for when "
      "you need it.\n")

    # ---- 1. critical path ----
    P("---\n\n## 1. The critical path\n")
    P("**Ranked by what unblocks what, not by value.** A blocker has modest value added and "
      "infinite\nimportance — nothing downstream happens until it exists, which is exactly why "
      "leverage-ranked lists\nbury them.\n")
    P("| # | Blocker | Function | Surface |\n|---|---|---|---|")
    for k, (s, fn_, act, sur, blk, why) in enumerate(sorted(blockers, key=dep_rank), 1):
        P(f"| {k} | **{act.replace('**', '')}** | {fn_} | `{sur}` |")
    P("")
    P("**Rows 1–7 are one chain and they gate your first paid invoice:** entity structure → "
      "identifiers →\nbank → client payment rail → talent payout rail → **W-8BEN-E** → "
      "GST/LUT. In India-to-US services\nthis commonly takes weeks. **Start it in week zero.**\n")

    # ---- 2. calendar ----
    P("---\n\n## 2. The calendar\n")
    for when, why, items in CAL:
        P(f"### {when}\n")
        P(f"*{why}*\n")
        for it in items:
            P(f"- {it}")
        P("")

    # ---- 3. full list ----
    P("---\n\n## 3. The full list, by function\n")
    P("`IMPORTANCE` 24 · `VALUE` 22 · `TIMESAVED` 20 · `FIT` 16 · `NOW` 12 · `REUSE` 6. "
      "**🔒 = blocker.**  \n`FIT` scores how well an agent does it **versus you doing it** — "
      "which is why screening reels scores\n3 and building the scraper scores 5.\n")
    order = []
    for fn_, *_ in ACT.A:
        if fn_ not in order:
            order.append(fn_)
    for fn_ in order:
        items = sorted([x for x in rows if x[1] == fn_], key=lambda x: -x[0])
        nb = sum(1 for x in items if x[4])
        P(f"### {fn_} — {len(items)} activities" + (f", {nb} blockers" if nb else "") + "\n")
        P("| Activity | Surface | 🔒 | Score | Note |\n|---|---|---|---|---|")
        for s, _f, act, sur, blk, why in items:
            P(f"| {act} | `{sur}` | {'🔒' if blk else ''} | **{s:.0f}** | {why} |")
        P("")

    # ---- 4. workflows ----
    P("---\n\n## 4. The 25 workflows\n")
    P("An activity is a thing you do. **A workflow is trigger → steps → output, built once, "
      "that then runs\nwithout you deciding anything.** With no employees that is the only "
      "leverage there is.\n")
    P("| Workflow | Must exist | Lead time | Steps | Surface |\n|---|---|---|---|---|")
    seq = {"Week 1 setup, Week 4 send": 0, "Continuous": 0, "Week 2": 1,
           "Week 2, monthly after": 1, "Before placement 1": 2, "Week 3": 3, "Week 4": 4,
           "Month 2": 5, "Month 3": 6}
    for w, st, when, lead, sur, steps, why in sorted(WFM.WF,
                                                     key=lambda x: seq.get(x[2], 9)):
        P(f"| **{w}** | {when} | {lead} | {steps} | {sur} |")
    P("")
    P(f"**{sum(x[5] for x in WFM.WF)} discrete steps.** Cold email alone is 23, decomposed in "
      "[`WORKFLOWS.md`](WORKFLOWS.md) §2.\n")

    # ---- 5. do not ----
    P("---\n\n## 5. Where an agent is the wrong tool\n")
    P("| Do not | Why | Instead |\n|---|---|---|")
    for t, why, instead in WFM.__dict__.get("DONT", []) or []:
        P(f"| {t} | {why} | {instead} |")
    for t, why, instead in [
        ("**Grading the creative**", "`FOUNDERGRADE` is *why video was chosen* — you can "
         "judge it with no team", "Build the scoring sheet. **You score**"),
        ("**The sales call**", "Trust is bought in conversation, and you have no track record",
         "Brief before, follow-up after"),
        ("**Legal, tax and entity authority**", "The India→US structure, EOR compliance, the "
         "Class 35 opinion. **A confident wrong answer here is expensive and slow to unwind**",
         "Draft so the CA or attorney reviews rather than writes"),
        ("**LinkedIn automation or scraping**", "The terms forbid it and the account is your "
         "face in a trust business", "Draft messages; send them yourself"),
        ("**Cold email from `allhandstalent.com`**", "One deliverability incident damages the "
         "domain your ads land on", "A separate sending domain, warmed properly"),
        ("**Inventing a number**", "The two worst errors in this repo came from exactly that",
         "Mark it `[?]` and go measure it"),
        ("**Deciding**", "**This repo has reversed itself five times** — the domain, the "
         "platform, code-vs-Framer, the unbreakability re-weight, and whether *All Hands* was "
         "clean", "Use it to make the choice legible. You still make it"),
    ]:
        P(f"| {t} | {why} | {instead} |")
    P("")

    # ---- 6. index ----
    P("---\n\n## 6. What supersedes what\n")
    P("| Document | What it is | Status |\n|---|---|---|")
    for d, w, st in SUPERSEDED:
        P(f"| {d} | {w} | {st} |")
    P("")
    P("**The business model itself is elsewhere and unaffected:** "
      "[`MODEL-V2.md`](MODEL-V2.md) is the current model, [`OFFER.md`](OFFER.md) the buildable "
      "thing,\n[`LTGP.md`](LTGP.md) and [`funnel.py`](scoring/funnel.py) the economics, "
      "[`MAP.md`](MAP.md) the ICP and role decision, [`SITE.md`](SITE.md) the\nwebsite build, "
      "[`ARBITRARY.md`](ARBITRARY.md) the name.\n")

    tot = {}
    for s, fn_, act, sur, blk, why in rows:
        tot[sur] = tot.get(sur, 0) + 1
    P(f"**Surface split:** Code {tot['Code']} · Cowork {tot['Cowork']} · Chat {tot['Chat']}. "
      "**Code is where the leverage\nis; Cowork is where the blockers are.**\n")
    open(OUT, "w").write("\n".join(L))
    print(f"MASTERLIST: {len(ACT.A)} activities, {len(blockers)} blockers, "
          f"{len(WFM.WF)} workflows, {len(CAL)} calendar phases")


if __name__ == "__main__":
    main()
