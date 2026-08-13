#!/usr/bin/env python3
"""
Where to build allhandstalent.com, and what the structure is.

The stated brief: ease of build, ease of maintenance, easy edits so landing pages can
be tested. That last word is the one worth checking before spending anything, because
**"test landing pages" has two very different meanings** and only one of them is
affordable at launch volume:

  ITERATE   change the headline, ship it, watch the number move. Needs a fast editor.
  SPLIT-TEST  run A and B concurrently and declare a winner at significance. Needs
              traffic, and section 1 computes how much off this repo's own funnel.

Every landing-page platform sells the second. The first is what actually matters for
the first six months, and it is much cheaper.

Sample size is the standard two-proportion test at 80% power, alpha 0.05 two-sided:

    n per arm = (z_a/2 + z_b)^2 * [p1(1-p1) + p2(1-p2)] / (p2 - p1)^2

with p1 taken from funnel.py's real LP conversion rate rather than a guess.

Prices below were checked and are dated; they move.

Run:  python3 scoring/site.py > /dev/null   (writes SITE.md)
"""
import contextlib
import io
import sys

sys.path.insert(0, "scoring")
with contextlib.redirect_stdout(io.StringIO()):
    import funnel as fn
    import ltgp

OUT = "SITE.md"
Z_A, Z_B = 1.959964, 0.841621          # 95% two-sided, 80% power
LIFTS = [0.10, 0.20, 0.30, 0.50]
SPEND = 5000.0
BROAD = "Broad / Advantage+"


def sample_per_arm(p1, lift):
    p2 = p1 * (1 + lift)
    return ((Z_A + Z_B) ** 2 * (p1 * (1 - p1) + p2 * (1 - p2)) / (p2 - p1) ** 2)


# ---------------------------------------------------------------------------
# Platforms. (name, scores, price note, comment)
# EDIT is weighted highest because it is the operator's stated first requirement
# and because section 1 shows iteration -- not split-testing -- is the real loop.
# ---------------------------------------------------------------------------
DIM = [
    ("EDIT",     26, "Can the operator change a headline and republish **alone, in "
                     "minutes**, with no developer and no deploy step"),
    ("NOCODE",   18, "Does *maintenance* need a developer — updates, security, plugins, "
                     "broken builds"),
    ("SPEED",    16, "Page load. Not vanity: [`funnel.py`](scoring/funnel.py) carries an "
                     "**85% landing-page-view rate**, and that number is a page-speed "
                     "number. Every point lost there is lost at the top of the funnel"),
    ("STACK",    16, "Meta pixel and **Conversions API**, forms, booking, and a **payment "
                     "step for the paid teardown** ([`OFFER.md`](OFFER.md) §9.1)"),
    ("CREDIBLE", 12, "Does the output look like a company a buyer pays $6k–$20k? No track "
                     "record means the site carries more trust load than usual"),
    ("COST",      7, "Monthly, all-in"),
    ("PORTABLE",  5, "Can you leave, and do you own the content"),
]
PLATFORM = [
    ("Framer",
     dict(EDIT=5, NOCODE=5, SPEED=5, STACK=4, CREDIBLE=5, COST=4, PORTABLE=3),
     "**Pro $30/mo** (CMS + forms). A/B add-on *Convert* is available on Pro, billed "
     "**$50 per 500K events**. Editor seats $20/mo",
     "**Easiest of the serious options for a non-developer** — consistently rated easier "
     "to learn than Webflow, especially coming from Figma. Static output, so pages are "
     "fast. `STACK`=4 only because CAPI needs a third-party relay rather than being native"),
    ("Webflow",
     dict(EDIT=4, NOCODE=5, SPEED=5, STACK=4, CREDIBLE=5, COST=3, PORTABLE=4),
     "**Basic $15/mo, Premium $25/mo** (annual). **Optimize — the A/B product — is "
     "$299/mo**",
     "More powerful and more portable, and **not fast to learn**. The $299 Optimize tier "
     "is irrelevant at launch volume (§1), so ignore it — but so is most of what makes "
     "Webflow worth the learning curve, at this stage"),
    ("Carrd",
     dict(EDIT=5, NOCODE=5, SPEED=5, STACK=2, CREDIBLE=2, COST=5, PORTABLE=2),
     "**$19/year**",
     "Genuinely the fastest way to ship one page. **Single-page-oriented and visibly "
     "template-y** — wrong for a multi-page site carrying a five-figure offer"),
    ("WordPress + Elementor",
     dict(EDIT=4, NOCODE=2, SPEED=2, STACK=5, CREDIBLE=3, COST=4, PORTABLE=5),
     "~$10–30/mo hosting + plugin licences",
     "Infinitely extensible and **the maintenance is the product**: updates, plugin "
     "conflicts, security, and page speed you have to fight for. Exactly the burden the "
     "brief rules out"),
    ("GoHighLevel",
     dict(EDIT=4, NOCODE=5, SPEED=3, STACK=5, CREDIBLE=2, COST=2, PORTABLE=1),
     "**~$97/mo**",
     "Native to the media-buying world and **collapses pages + CRM + booking + payments "
     "into one bill**. But funnel-builder output looks like funnel-builder output, which "
     "fights a premium claim, and it is the most locked-in option here"),
    ("Next.js or Astro on Vercel",
     dict(EDIT=1, NOCODE=1, SPEED=5, STACK=5, CREDIBLE=5, COST=5, PORTABLE=5),
     "$0–20/mo",
     "Fastest and most controllable, and **every headline change is a code edit and a "
     "deploy**. Correct answer for a team with an engineer. Wrong answer for a solo "
     "operator whose scarcest input is attention"),
    ("Squarespace / Wix",
     dict(EDIT=5, NOCODE=5, SPEED=3, STACK=3, CREDIBLE=3, COST=4, PORTABLE=2),
     "~$16–29/mo",
     "Easy, but slower pages and weaker control over the one thing that matters most "
     "here — many near-identical landing-page variants"),
]

# structure: (path, who, what, when)
PAGES = [
    ("/", "buyer", "**The homepage. Demand only.** Hero → the graded proof → how it "
     "works → guarantee → one CTA. No careers link above the fold", "week 1"),
    ("/agencies", "buyer", "**Ad destination, ICP 1.** Marketing agencies. Ads point "
     "*here*, never at `/` — [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §7 makes this the "
     "control that keeps Meta's page review away from any job content", "week 1"),
    ("/ecommerce", "buyer", "**Ad destination, ICP 2.** E-comm brands. Same page, "
     "different proof and different language. [`MODEL-V2.md`](MODEL-V2.md) gap 8: **two "
     "ICPs, one role, two ads** — five starves Meta of signal", "week 1"),
    ("/proof", "buyer", "**The graded work sample, and the most important page on the "
     "site.** Recut ads with **3-second and 15-second retention measured against the "
     "original** ([`MODEL-V2.md`](MODEL-V2.md) gap 6). This is what makes *premium* "
     "falsifiable instead of an adjective", "week 2"),
    ("/pricing", "buyer", "**One-time, 30–35% of first-year compensation**, plus EOR "
     "presented as the **default** employment path. Gaps 1 and 4 — the pricing "
     "conflation breaks the model 8× if left ambiguous", "week 2"),
    ("/guarantee", "buyer", "**12-month unlimited replacement, no cash refunds.** "
     "Modelled as *cheaper* than the 6-month industry standard while sounding stronger — "
     "the cheapest differentiation available", "week 2"),
    ("/teardown", "buyer", "**The money gate.** Paid ad-account and creative teardown → "
     "Stripe → booking. This is the paid step that funds the search and filters "
     "tyre-kickers", "week 1"),
    ("/thanks", "buyer", "Confirmation + what happens next + calendar", "week 1"),
    ("/talent", "supply", "**Footer link only. `noindex, nofollow`. No Meta pixel.** And "
     "**do not publish it in launch month at all** — supply needs zero ad spend, referral "
     "and LinkedIn fill the first ten to twenty seats", "month 3–6"),
]

STACK = [
    ("Site + landing pages", "**Framer Pro**", "$30/mo",
     "One tool for the brand site *and* every LP variant. Duplicate a page, change the "
     "headline, publish — that is the whole loop §1 says you actually need"),
    ("Booking", "**Cal.com**", "free–$15/mo",
     "Embeds in Framer. Free tier is enough for one calendar"),
    ("Payment for the teardown", "**Stripe Payment Link**", "2.9% + 30¢",
     "**No code at all** — a hosted checkout URL you paste into a button. Do not build a "
     "checkout"),
    ("Forms → inbox", "Framer Forms → email + Google Sheet", "included",
     "A spreadsheet is a sufficient CRM until roughly placement ten"),
    ("Pixel + CAPI", "Meta Pixel via Framer's custom-code field; **CAPI via Stape or "
     "Zapier**", "$0–20/mo",
     "Browser pixel alone under-reports. **Verify CAPI works before spending**, since "
     "every CAC number in [`LTGP.md`](LTGP.md) assumes conversions are actually attributed"),
    ("Analytics", "Framer Analytics or Plausible", "$0–9/mo",
     "You need page-level conversion rate, not a dashboard"),
    ("Email", "**Google Workspace on the domain**", "$6/user/mo",
     "`you@allhandstalent.com` before the first ad runs"),
]


def main():
    f = fn.FLOW[ltgp.FLOW]
    p1 = f["conv"]
    r = fn.run(BROAD, ltgp.FLOW, spend=SPEND)
    lpv_per_spend = r["lpv"] / SPEND

    rows = []
    for lift in LIFTS:
        n = sample_per_arm(p1, lift)
        total = 2 * n
        rows.append((lift, n, total, total / lpv_per_spend))

    L = []
    A = L.append
    A("# Building `allhandstalent.com`\n")
    A("> **Framer Pro, $30/month. One tool, one domain, path-based pages. Cal.com for "
      "booking, a Stripe\n> Payment Link for the paid teardown. Do not buy an A/B testing "
      "product — §1 shows you cannot\n> reach significance at launch volume, and the money is "
      "better spent on being able to change the\n> page in two minutes.**\n")

    A("---\n\n## 1. First: \"test landing pages\" cannot mean split-testing yet\n")
    A("Every platform upsells A/B testing — **Webflow Optimize is $299/month**, Framer's "
      "*Convert* add-on\nbills per event. So it is worth computing whether a split test can "
      "conclude anything at your volume,\nusing this repo's own funnel rather than a guess.\n")
    A(f"The landing page converts at **{p1:.1%}** ([`funnel.py`](scoring/funnel.py), calendar-"
      f"booking flow).\nStandard two-proportion test, **80% power, 95% confidence**:\n")
    A("| To detect a lift of | LP views **per arm** | Total LP views | Ad spend to get there |")
    A("|---|---|---|---|")
    for lift, n, total, spend in rows:
        A(f"| **{lift:.0%}** | {n:,.0f} | {total:,.0f} | **${spend:,.0f}** |")
    A("")
    A(f"At $5,000 of spend on broad you get **{r['lpv']:,.0f} landing-page views** and "
      f"**{r['leads']:.0f} leads**.\n")
    A(f"> **One test at a 20% lift needs ${rows[1][3]:,.0f} of spend** — roughly "
      f"**{rows[1][3]/SPEND:.0f}× a $5,000 month**, to answer\n> *one* question about *one* "
      f"headline. A 10% lift needs ${rows[0][3]:,.0f}. **Split-testing is a "
      f"month-twelve\n> tool.** Anyone selling it to you now is selling statistical theatre.\n")
    A("What this changes: **the requirement is not a testing engine, it is an editor.** "
      "Change the page,\nship it, read the direction, change it again — and judge with your "
      "eyes and your call notes, not\nwith a p-value. That is a $30/month problem, not a "
      "$299/month one.\n")
    A("**Where split-testing *does* work from day one is the ad, not the page.** Meta tests "
      "creative natively\nat the ad level, where the unit is an impression rather than a lead, "
      "so volume arrives ~50× faster.\nPut the testing effort there — which is also the thing "
      "the operator is already world-class at.\n")

    A("---\n\n## 2. Where to build it\n")
    W = {k: w for k, w, _ in DIM}

    def sc(d):
        return sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100

    A("| Dimension | Wt | What it measures |\n|---|---|---|")
    for k, w, why in DIM:
        A(f"| **{k}** | {w} | {why} |")
    A("")
    A("| Platform | " + " | ".join(k for k, _, _ in DIM) + " | Score | Price |")
    A("|---|" + "---|" * (len(DIM) + 2))
    ranked = sorted(PLATFORM, key=lambda x: -sc(x[1]))
    for name, d, price, _ in ranked:
        mark = " ✅" if name == ranked[0][0] else ""
        A(f"| **{name}**{mark} | " + " | ".join(str(d[k]) for k, _, _ in DIM) +
          f" | **{sc(d):.1f}** | {price} |")
    A("")
    for name, d, _, why in ranked:
        A(f"**{name} — {sc(d):.1f}** · {why}\n")
    a, b = ranked[0], ranked[1]
    A(f"> **{a[0]} wins by {sc(a[1])-sc(b[1]):.1f} points over {b[0]}**, almost entirely on "
      f"`EDIT`. Given §1, that is\n> the right thing to optimise: the loop is *change it and "
      f"look*, run dozens of times, alone.\n")

    A("---\n\n## 3. The structure\n")
    A("One domain. Paths, not subdomains. Homepage entirely demand.\n")
    A("| Path | For | What it is | Build |\n|---|---|---|---|")
    for path, who, what, when in PAGES:
        A(f"| **`{path}`** | {who} | {what} | {when} |")
    A("")
    A("**Ads never point at `/`.** They point at `/agencies` or `/ecommerce`. Two reasons: "
      "the message\nmatches the audience, and page review sees a dedicated buyer page with no "
      "route to job content.\n")

    A("---\n\n## 4. The rest of the stack\n")
    A("| Job | Tool | Cost | Why |\n|---|---|---|---|")
    for job, tool, cost, why in STACK:
        A(f"| {job} | {tool} | {cost} | {why} |")
    A("")
    A("**All-in: roughly $45–70/month.** The $299 tier you were being sold does not appear, "
      "because §1\nsays it would buy nothing until month twelve.\n")

    A("---\n\n## 5. Build order\n")
    A("| | Week | Ship |\n|---|---|---|")
    for i, (wk, what) in enumerate([
        ("Week 1", "`/agencies`, `/ecommerce`, `/teardown`, `/thanks`, and a one-screen `/`. "
                   "**Ad destinations before brand pages** — nothing else can earn a dollar"),
        ("Week 1", "Stripe Payment Link, Cal.com, pixel **and CAPI verified with test events "
                   "before any spend**"),
        ("Week 2", "`/proof` — the recut ads with retention numbers. **The single highest-"
                   "leverage page**, and the only one that turns *premium* from an adjective "
                   "into a claim a buyer can check"),
        ("Week 2", "`/pricing` and `/guarantee`. State the fee as **one-time, 30–35% of "
                   "first-year comp**; present EOR as the default"),
        ("Week 3", "Fill `/` properly. LinkedIn company page live"),
        ("Month 3–6", "`/talent`, footer-linked, `noindex`, with the pass rate on it"),
    ], 1):
        A(f"| {i} | {wk} | {what} |")
    A("")
    A("*Prices checked at time of writing and they move — Framer Pro $30/mo with Convert "
      "billed per event,\nWebflow Basic $15 / Premium $25 annual with Optimize at $299/mo. "
      "Re-check before you subscribe.*\n")
    open(OUT, "w").write("\n".join(L))
    print(f"LP conv {p1:.1%} · $5k broad = {r['lpv']:,.0f} LPV, {r['leads']:.0f} leads")
    for lift, n, total, spend in rows:
        print(f"  {lift:.0%} lift -> {total:,.0f} LPV, ${spend:,.0f} spend")


if __name__ == "__main__":
    main()
