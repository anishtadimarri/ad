#!/usr/bin/env python3
"""
Choosing a Framer template for allhandstalent.com -- criteria first, shortlist second.

Two honest constraints shape this file:

  1. **The two criteria that matter most cannot be verified from a listing.** Whether the
     promise and CTA fit above the fold on a 390x844 phone, and how heavy the page is on
     a 4G connection, are properties of the live preview -- not of a marketplace
     description. So the shortlist below is *a list to test*, not a verdict, and the
     20-minute test in section 4 is the part that actually decides it.

  2. **Template names and prices churn.** Anything sourced from an aggregator is marked.

The more useful finding is structural and sits in section 1: **the template only has to
be right for the brand pages.** The pages that carry the ad traffic -- /agencies and
/ecommerce -- are six blocks each and are better built from blank. Buying a template to
solve the landing page is solving the wrong page.

Weights are set by this specific funnel, not by generic web-design advice:
Meta traffic is overwhelmingly mobile, arrives cold mid-scroll, and funnel.py carries an
**85% landing-page-view rate** -- which is a page-weight number.

Run:  python3 scoring/template.py > /dev/null   (writes TEMPLATE.md)
"""

OUT = "TEMPLATE.md"

DIM = [
 ("MOBILEHERO", 20, "**Promise + CTA above the fold on a 390×844 phone, no scroll.** Meta "
                    "traffic is overwhelmingly mobile and arrives mid-scroll. Most templates "
                    "are desktop-first with a tall hero that pushes the CTA under the fold on "
                    "a phone — **the most common failure, and invisible on a laptop**",
                    "`[?]` needs the phone test"),
 ("SPEED",      15, "Weight and animation on 4G. [`funnel.py`](scoring/funnel.py) carries an "
                    "**85% LP-view rate** — a speed number, lost at the very top of the funnel",
                    "`[?]` needs the phone test"),
 ("COMPLETE50", 15, "**New.** *\"Everything for the first 50 converts.\"* Does it ship every "
                    "surface you need before a rebuild — **CMS for accumulating `/proof` "
                    "entries and case studies**, pricing, testimonials, forms, booking embed, "
                    "thank-you page, legal pages? **A template you outgrow at client ten costs "
                    "you a rebuild in the busiest month you will have**", "assessable"),
 ("STABLE",     13, "**New.** *\"Stability and clean.\"* Maintained, lifetime updates, and "
                    "**structurally clean — components and global styles rather than "
                    "hand-placed pages.** Clean structure is also what makes `/agencies` and "
                    "`/ecommerce` a duplicate-and-edit rather than two of everything forever",
                    "partly — longevity is the best available proxy"),
 ("SECTIONS",   12, "Ships the sections this offer needs, in order: hero → proof → how it "
                    "works → pricing → guarantee → CTA. **Most agency templates are "
                    "portfolio-shaped**, which is a different page", "assessable"),
 ("CTAREPEAT",   8, "CTA in hero, mid-page, and sticky or footer. **Mobile users do not scroll "
                    "back up**", "assessable"),
 ("PROOFSLOT",   7, "A block that holds **two videos side by side with retention numbers under "
                    "them** — the recut-vs-original comparison", "assessable"),
 ("CREDIBLE",    6, "Reads as a firm a $6k–$20k buyer trusts. Not startup-gradient, not "
                    "creative-portfolio", "assessable"),
 ("NETCOST",     4, "**Changed.** Cost **net of the bundled 3 months of Framer Pro** that paid "
                    "templates commonly include — see §2. A free template has no bundle, so it "
                    "is not the cheapest option", "verifiable on the listing"),
]

# (name, price, register, COMPLETE50, STABLE, SECTIONS, CTAREPEAT, PROOFSLOT,
#  CREDIBLE, NETCOST, note)   -- MOBILEHERO and SPEED deliberately unscored, see section 3
T = [
 ("Conversion", "~$79 `[?]`", "conversion / lead-gen",
  4, 5, 5, 5, 3, 4, 5,
  "**Built for lead generation rather than showcase** — the rarest property here. "
  "**`STABLE`=5 on the strongest evidence available**: one of the longest-running templates "
  "on the marketplace with 100k+ views, which is the only real proxy for *it still works and "
  "is still maintained*"),
 ("Funnelz", "paid `[?]`", "lead-gen agency",
  5, 3, 5, 4, 5, 3, 5,
  "**Verified live.** By Ramish Aziz. Ships hero+CTA, social proof, **case studies**, "
  "services, **3-tier pricing**, team bios, **blog/resources**, booking in the nav — "
  "**`COMPLETE50`=5, the most complete section set on this list.** Two mismatches, both "
  "edits not rebuilds: **3-tier pricing when you have one price**, and **team bios when you "
  "are one person** (repurpose as the founder story — useful when you have no track record). "
  "**`CREDIBLE`=3 is the real risk**: *\"Fuelling growth with every click\"* is "
  "funnel-agency register, and **your buyer *is* an agency owner who will recognise it "
  "instantly**"),
 ("Cubicles", "~$59 `[?]`", "corporate / consultancy",
  4, 4, 4, 3, 3, 5, 5,
  "**Corporate B2B — the right register**, and the opposite risk to Funnelz. Structured for "
  "services rather than showcase. Weaker repeated CTA, which is a fixable edit"),
 ("Nakula / Fabrica / Lyniq", "$69–129 `[?]`", "premium agency",
  4, 4, 4, 3, 4, 5, 4,
  "The 'looks expensive' tier for high-ticket B2B. `CREDIBLE`=5 is real. **But premium "
  "agency templates are usually the heaviest** — big imagery, heavy motion — so `SPEED` is "
  "the risk and it is exactly what I cannot check"),
 ("Nebula", "$49 `[?]`", "lead-gen, dark + gradient",
  3, 3, 4, 4, 3, 3, 5,
  "Lead-gen shaped and cheap. **`CREDIBLE`=3**: dark gradient reads SaaS-startup, and your "
  "buyer is deciding whether an unknown Indian firm is real"),
 ("Greenleaf", "**free**", "consulting",
  3, 4, 4, 3, 2, 4, 3,
  "Clean consulting register, services section, clear contact-to-consultation flow. "
  "**`NETCOST`=3, not 5 — free templates carry no Pro bundle**, so you pay $30/mo from day "
  "one and it is not actually the cheapest path (§2). Built for ESG consultants, so expect "
  "green styling — a skin change, not structural"),
 ("Kajo", "**free**", "general",
  2, 3, 3, 3, 2, 3, 3, "Fewer sections, less structure, no bundle"),
 ("Halo", "$69 `[?]`", "general / startup",
  3, 3, 3, 3, 3, 3, 4, "No strong reason over the lead-gen options above"),
]

# The 20-minute test, run on the operator's own phone.
TEST = [
 ("Open the live preview **on your phone, on mobile data — not wifi**", "SPEED",
  "The whole point. A laptop on fibre tells you nothing about the buyer's experience"),
 ("**Do not scroll. Screenshot.** Is the promise *and* a tappable CTA both visible?", "MOBILEHERO",
  "**This one test eliminates most templates.** If the CTA is below the fold on a phone, "
  "everything else about the template is irrelevant"),
 ("Count the seconds until the hero text is readable", "SPEED",
  "Anything past ~3 seconds on 4G is costing you LP views before anyone reads a word"),
 ("Scroll once, fast, the way a person actually does", "SECTIONS",
  "Does the order make sense without reading? Promise → proof → mechanism → price → ask"),
 ("Count CTAs on the way down", "CTAREPEAT",
  "Fewer than three on a long page means people who are convinced at 60% have nothing to tap"),
 ("Look for a block that could hold **two videos side by side with numbers under them**",
  "PROOFSLOT", "That is the recut-vs-original comparison. If nothing fits, you are building it"),
 ("Ask: would I give this company $6,600?", "CREDIBLE",
  "Answer as your buyer — a US agency owner who has never heard of you"),
 ("Check the template's own page count and whether sections are components", "VARIANT",
  "Components mean `/agencies` and `/ecommerce` are a duplicate-and-edit. Hand-built pages "
  "mean two of everything, forever"),
]


def main():
    W = {k: w for k, w, _, _ in DIM}
    SUB = ["COMPLETE50", "STABLE", "SECTIONS", "CTAREPEAT", "PROOFSLOT",
           "CREDIBLE", "NETCOST"]
    subw = sum(W[k] for k in SUB)

    def sc(row):
        vals = dict(zip(SUB, row[3:10]))
        return sum(vals[k] * W[k] for k in SUB) / (5 * subw) * 100

    rows = sorted(T, key=lambda r: -sc(r))

    L = []
    P = L.append
    P("# Choosing the Framer Template\n")
    P("> Criteria first, shortlist second — because **the two criteria that matter most cannot "
      "be judged\n> from a marketplace listing**, and pretending otherwise would produce a "
      "confident wrong answer.\n")

    P("---\n\n## 1. First: you are buying a template for the wrong page\n")
    P("The instinct is to find a template that solves the landing page. It does not, and it "
      "should not.\n")
    P("| Page | What it is | Template? |\n|---|---|---|")
    P("| **`/agencies`, `/ecommerce`** | **The ad destinations. Where 100% of paid traffic "
      "lands.** Six blocks: promise, proof, mechanism, price, guarantee, one ask | **No. Build "
      "from blank.** A landing page is six blocks and no template does six blocks better than "
      "you do with the copy in front of you |")
    P("| `/`, `/proof`, `/pricing`, `/guarantee` | The brand and credibility pages. Read after "
      "the ad, or by a referral, or by someone checking you are real | **Yes.** This is what "
      "the template is for — structure and polish you would otherwise spend days on |")
    P("")
    P("> **So the template's job is credibility, not conversion.** That changes what you are "
      "shopping for,\n> and it means a **free** template may be entirely sufficient — see §5.\n")

    P("---\n\n## 2. The 3-months-free bundle reverses \"start with a free one\"\n")
    P("**Paid Framer templates commonly ship a code for 3 months of Framer Pro.** That is not a "
      "marketing\nfootnote — it is worth more than most of the templates cost, and it inverts "
      "the cost comparison\nI gave last time.\n")
    P("| Path | Template | Framer Pro, months 1–3 | **Total, first 3 months** |")
    P("|---|---|---|---|")
    P("| **Free template** (Greenleaf, Kajo) | $0 | **$90** — you pay from day one | **$90** |")
    P("| **Paid template with the bundle** (~$79) | $79 | **$0** | **$79 + the template** |")
    P("")
    P("> **The paid template is cheaper *and* you get the template.** A free template is only "
      "the cheapest\n> option if you ignore the subscription it does not cover — which is "
      "exactly what I did last turn.\n")
    P("Three caveats, and the first one matters:\n")
    P("| | |\n|---|---|")
    P("| **The bundle is creator-dependent, not universal** | It is common, not guaranteed. "
      "**Check the specific listing for the 3-months-Pro code before buying** — the whole "
      "argument above collapses without it |")
    P("| It is 3 months of the **annual** Pro plan | Which means it likely presumes annual "
      "billing afterwards. Read what you are committing to at month four |")
    P("| Prices here are `[?]` from aggregators | Verify on Framer. Listings churn |")
    P("")

    P("---\n\n## 3. The criteria, weighted for this funnel\n")
    P("Not generic web-design advice. These weights come from **your** traffic: overwhelmingly "
      "mobile,\ncold, mid-scroll, and metered by an 85% LP-view rate.\n")
    P("| Criterion | Wt | What it means | Can I check it? |")
    P("|---|---|---|---|")
    for k, w, why, chk in DIM:
        P(f"| **{k}** | {w} | {why} | {chk} |")
    P("")
    P("> **The top two weights — 40 points of 100 — are the two I cannot verify.** `MOBILEHERO` "
      "and `SPEED`\n> are properties of the live preview on a phone on mobile data. Everything "
      "below is therefore a\n> **shortlist to test**, not a ranking to trust.\n")

    P("---\n\n## 4. The shortlist, scored on what *is* assessable\n")
    P(f"Scored on the {len(SUB)} assessable criteria only — {subw} of 100 points. "
      "**`MOBILEHERO` and `SPEED` are\ndeliberately absent**, which is why the top score here "
      "is not a recommendation.\n")
    P("| # | Template | Price | Register | C50 | Stab | Sect | CTA | Proof | Cred | Net$ | "
      "Score | Note |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        P(f"| {i} | **{r[0]}** | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | "
          f"{r[8]} | {r[9]} | **{sc(r):.0f}** | {r[10]} |")
    P("")
    P("*Names and prices are from marketplace aggregators and are marked `[?]` — **verify both "
      "on Framer\nbefore buying**, since listings and pricing churn.*\n")

    P("---\n\n## 5. The 20-minute test that actually decides it\n")
    P("Run this on **three** candidates. It is worth more than any ranking I can give you, "
      "because it\nmeasures the two things that carry 40% of the weight.\n")
    P("| # | Do this | Tests | Why |\n|---|---|---|---|")
    for i, (step, dim, why) in enumerate(TEST, 1):
        P(f"| {i} | {step} | `{dim}` | {why} |")
    P("")
    P("**Step 2 is the whole test.** Screenshot the top of the page on your phone without "
      "scrolling. If the\npromise and a tappable CTA are not both in that screenshot, the "
      "template fails — and **it will look\nperfect on your laptop**, which is how this mistake "
      "gets made.\n")

    P("---\n\n## 6. What I would actually do\n")
    P("**This reverses last turn's answer, and the bundle is why.**\n")
    P("| | |\n|---|---|")
    P("| **Buy a paid template with the 3-month Pro code** | It is cheaper than free over the "
      "first quarter (§2), and the two strongest candidates are both paid |")
    P("| **First choice: Conversion** | The only one built for **lead generation rather than "
      "showcase**, and `STABLE`=5 on the best evidence available — 100k+ marketplace views over "
      "years is the only real proxy for *still maintained, still works*. **Stability was one of "
      "your criteria and this is the one template with actual evidence for it** |")
    P("| **Close second: Funnelz** | **The most complete section set on the list** — case "
      "studies, blog, pricing, testimonials, booking. `COMPLETE50`=5, so nothing needs "
      "rebuilding as proof accumulates. **The risk is register**: your buyer is an agency owner "
      "who will recognise funnel-agency styling on sight |")
    P("| **Cubicles if Funnelz feels too *agency*** | Corporate-B2B register, the opposite risk "
      "profile, and cheaper |")
    P("| **Still avoid the premium tier** | Nakula, Fabrica, Lyniq look expensive and are "
      "usually the heaviest. **You are optimising for a phone on 4G** |")
    P("| **Greenleaf drops to a fallback** | Still fine, still clean — but `NETCOST`=3 because "
      "there is no bundle, and `PROOFSLOT`=2 because a consulting template has nowhere natural "
      "for a two-video comparison |")
    P("")
    P("### On \"everything for the first 50 converts\"\n")
    P("That criterion is doing real work, and it is why **Funnelz jumped past Cubicles.** The "
      "surfaces you\nwill need before client fifty, in the order they become urgent:\n")
    P("| By client | You need | Which means the template must ship |\n|---|---|---|")
    for a, b, c in [
        ("1", "Two ad destinations, a paid teardown page, booking, thank-you",
         "Forms, an embed slot, a payment button — **or you build these anyway**"),
        ("3–5", "**Your first `/proof` entries**", "**A CMS**, not hand-built pages. This is "
         "the one that bites — three case studies as static pages is fine, thirty is not"),
        ("10", "Testimonials, a real pricing page, a guarantee page",
         "Testimonial and pricing components already styled"),
        ("25", "A second ICP variant, an FAQ answering repeated objections",
         "Clean components so a duplicate-and-edit is minutes"),
        ("50", "Case studies with numbers, a talent page, legal pages",
         "**Blog/CMS depth and enough section variety that you are editing, not rebuilding**"),
    ]:
        P(f"| **{a}** | {b} | {c} |")
    P("")
    P("> **The rebuild you are avoiding would land in month three or four — your busiest "
      "month.** That is the\n> real cost of a thin template, and it is much larger than the "
      "$79.\n")
    P("**And strip whatever you buy.** Templates ship with animation and section counts designed "
      "to demo well\nin a marketplace. Delete aggressively — every animation removed buys back "
      "LP-view rate, and the 85%\nin the funnel is an assumption you can move in the right "
      "direction for free.\n")

    open(OUT, "w").write("\n".join(L))
    print(f"{len(T)} templates scored on {len(SUB)} of {len(DIM)} criteria "
          f"({subw}/100 pts assessable)")
    for r in rows:
        print(f"  {sc(r):5.1f}  {r[0]:28s} {r[1]}")


if __name__ == "__main__":
    main()
