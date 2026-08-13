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
 ("MOBILEHERO", 22, "**Promise + CTA above the fold on a 390×844 phone, with no scroll.** "
                    "Meta traffic is overwhelmingly mobile and arrives mid-scroll. Most "
                    "templates are designed desktop-first with a tall hero image that pushes "
                    "the CTA below the fold on a phone — **this is the single most common "
                    "failure and it is invisible on a laptop**", "`[?]` from listings"),
 ("SPEED",      18, "Page weight and animation load on 4G. [`funnel.py`](scoring/funnel.py) "
                    "carries an **85% LP-view rate** — that is a speed number, and every "
                    "point lost is lost at the very top of the funnel. **Framer templates "
                    "love scroll animation and video backgrounds**", "`[?]` from listings"),
 ("SECTIONS",   16, "Does it ship the sections this offer needs, in this order — hero → "
                    "proof → how it works → pricing → guarantee → CTA? **Most agency "
                    "templates are portfolio-shaped** (case-study grid, big imagery), which "
                    "is a different page", "assessable"),
 ("CTAREPEAT",  12, "CTA in the hero, mid-page, and sticky or footer. **Mobile users do not "
                    "scroll back up**", "assessable"),
 ("PROOFSLOT",  10, "Somewhere to put a **before/after video comparison with retention "
                    "numbers** — the `/proof` page is the most important on the site",
                    "assessable"),
 ("CREDIBLE",   10, "Reads as a firm a $6k–$20k buyer trusts. **Not startup-gradient, not "
                    "creative-portfolio.** You have no track record, so the site carries "
                    "more trust load than usual", "assessable"),
 ("VARIANT",     7, "How easily it duplicates into `/agencies` and `/ecommerce` — component-"
                    "driven with global styles, or hand-built pages", "assessable"),
 ("COST",        5, "One-time. Real, but small against the decision", "verifiable"),
]

# (name, price, register, SECTIONS, CTAREPEAT, PROOFSLOT, CREDIBLE, VARIANT, COST, note)
# MOBILEHERO and SPEED are deliberately NOT scored -- see section 3.
T = [
 ("Conversion", "~$79 `[?]`", "conversion / lead-gen",
  5, 5, 3, 4, 4, 3,
  "**Built for lead generation rather than showcase**, which is the rarest and most "
  "valuable property in this list. One of the longest-running templates on the Framer "
  "marketplace. `PROOFSLOT`=3 because a conversion template optimises for form-fills, not "
  "for a video comparison — you would add that block"),
 ("Nebula", "$49 `[?]`", "lead-gen, dark + gradient",
  4, 4, 3, 3, 4, 4,
  "Explicitly lead-gen focused and cheap. **`CREDIBLE`=3 is the concern** — dark gradient "
  "reads SaaS-startup, and your buyer is a 40-year-old agency owner deciding whether an "
  "unknown Indian firm is real"),
 ("Cubicles", "~$59 `[?]`", "corporate / consultancy",
  4, 3, 3, 5, 3, 4,
  "**Corporate B2B register — the right register.** Structured for services rather than "
  "showcase. Weaker on repeated CTA, which is a fixable edit"),
 ("Nakula / Fabrica / Lyniq", "$69–129 `[?]`", "premium agency",
  4, 3, 4, 5, 3, 2,
  "The 'looks expensive' tier, aimed at high-ticket B2B. **`CREDIBLE`=5 is real and "
  "matters here.** But premium agency templates are usually the heaviest — big imagery, "
  "lots of motion — so `SPEED` is the risk and it is unverified"),
 ("Greenleaf", "**free** `[?]`", "consulting",
  4, 3, 2, 4, 3, 5,
  "Free, clean, consulting-shaped, with a services section and a clear contact-to-"
  "consultation flow. **The cheapest way to test whether a template is even the "
  "constraint** — and if the answer is no, you have spent nothing"),
 ("Kajo", "**free** `[?]`", "general",
  3, 3, 2, 3, 3, 5, "Free. Fewer sections, less structure"),
 ("Halo", "$69 `[?]`", "general/startup",
  3, 3, 3, 3, 3, 3, "No strong reason to choose it over the lead-gen options above"),
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
    SUB = ["SECTIONS", "CTAREPEAT", "PROOFSLOT", "CREDIBLE", "VARIANT", "COST"]
    subw = sum(W[k] for k in SUB)

    def sc(row):
        vals = dict(zip(SUB, row[3:9]))
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

    P("---\n\n## 2. The criteria, weighted for this funnel\n")
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

    P("---\n\n## 3. The shortlist, scored on what *is* assessable\n")
    P(f"Scored on the {len(SUB)} assessable criteria only — {subw} of 100 points. "
      "**`MOBILEHERO` and `SPEED` are\ndeliberately absent**, which is why the top score here "
      "is not a recommendation.\n")
    P("| # | Template | Price | Register | Sect | CTA | Proof | Cred | Var | Cost | Score | "
      "Note |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        name, price, reg = r[0], r[1], r[2]
        P(f"| {i} | **{name}** | {price} | {reg} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | "
          f"{r[8]} | **{sc(r):.0f}** | {r[9]} |")
    P("")
    P("*Names and prices are from marketplace aggregators and are marked `[?]` — **verify both "
      "on Framer\nbefore buying**, since listings and pricing churn.*\n")

    P("---\n\n## 4. The 20-minute test that actually decides it\n")
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

    P("---\n\n## 5. What I would actually do\n")
    P("| | |\n|---|---|")
    P("| **Start with a free one** | **Greenleaf** (consulting register, services section, "
      "clear contact-to-consultation flow) costs nothing and answers the real question: *is the "
      "template the constraint, or is the copy?* It is almost always the copy |")
    P("| **If you pay, pay for the lead-gen register** | **Conversion** is the only one on the "
      "list built for lead generation rather than showcase, and that is the rarest property "
      "here. **Cubicles** if you want the corporate-B2B look instead |")
    P("| **Avoid the premium agency tier for now** | Nakula, Fabrica, Lyniq look expensive and "
      "are usually the heaviest — big imagery, heavy motion. **You are optimising for a phone "
      "on 4G, not for a design award** |")
    P("| **Avoid dark-gradient startup templates** | Nebula is cheap and lead-gen shaped, but "
      "your buyer is an agency owner deciding whether an unknown Indian firm is real. **Dark "
      "gradient reads *startup*; you want *firm*** |")
    P("| **Budget the saving, not the spend** | The gap between free and $79 is one hour of "
      "your time. **The gap between a template that fails the phone test and one that passes is "
      "every impression you ever buy** |")
    P("")
    P("**And strip whatever you buy.** Templates ship with animation, parallax and section "
      "counts designed to\ndemo well in a marketplace. Delete aggressively: every animation you "
      "remove buys back LP-view rate,\nand the 85% in the funnel is an assumption you can move "
      "in the right direction for free.\n")
    open(OUT, "w").write("\n".join(L))
    print(f"{len(T)} templates scored on {len(SUB)} of {len(DIM)} criteria "
          f"({subw}/100 pts assessable)")
    for r in rows:
        print(f"  {sc(r):5.1f}  {r[0]:28s} {r[1]}")


if __name__ == "__main__":
    main()
