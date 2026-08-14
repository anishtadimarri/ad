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
 ("COMPLETE",   30, "**Is the tooling already there?** Every section and page you need, "
                    "shipped: **CMS/blog**, pricing, case studies, testimonials, FAQ, forms, "
                    "booking, team, legal. **What is missing is what you build from blank** — "
                    "and that is real work, unlike editing copy", "verified by demo"),
 ("CONVERT",    25, "**Funnel-optimised for Meta traffic.** Single-goal pages, CTA in hero and "
                    "repeated down the page, social proof early, a comparison or objection "
                    "block, booking or form at the end. **Cold paid traffic needs persuasion "
                    "architecture, not a brochure**", "verified by demo"),
 ("STABLE",     20, "Maintained, clean component structure, longevity. **Marketplace age and "
                    "volume is the only real evidence available** for *still works, still "
                    "supported*", "partly — longevity as proxy"),
 ("SHAPE",      15, "Employer-facing **services** structure. Not a candidate job board, not a "
                    "SaaS product page. **This is structural, not cosmetic** — and a job-board "
                    "shape also risks Meta's Employment Special Ad Category "
                    "([`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §1, a 10–29% CAC tax)",
                    "verified by demo"),
 ("NETCOST",     5, "Cost net of the bundled 3 months of Framer Pro (§2)", "listing"),
 ("RECOPY",      5, "**Dropped from 15 to 5.** *\"We can edit whatever as long as the tooling "
                    "is there.\"* Register distance is a copy-and-colour job, not a build job "
                    "— **and weighting it at 15 is what put Recruitify top last time**",
                    "verified by demo"),
]

# (name, price, register, COMPLETE, CONVERT, STABLE, SHAPE, NETCOST, RECOPY, missing, note)
T = [
 ("Funnelz", "paid `[?]`", "lead-gen agency",
  5, 5, 3, 4, 4, 2, "team-bio page only",
  "**[Demo verified.](https://funnelz.framer.website/)** By Ramish Aziz. **The only template "
  "found with the full tooling set**: hero+CTA, social proof, **case studies**, services, "
  "**3-tier pricing**, team, **blog/CMS**, **booking in the nav**. Built as a lead-gen site, "
  "so the persuasion order is already right. `RECOPY`=2 — funnel-agency voice — **which no "
  "longer costs it anything**"),
 ("Conversion", "~$79 `[?]`", "paid-ads agency",
  2, 5, 5, 4, 4, 3, "**blog/CMS, pricing page**",
  "**[Demo verified.](https://conversion.framer.media/)** *\"Ready to scale your brand with "
  "paid ads?\"* **The best conversion architecture of anything found** — a Results metrics "
  "block, a **comparison table**, a 3-step process, testimonials high on the page. And "
  "`STABLE`=5 on the only hard evidence available: **one of the longest-running, most-viewed "
  "templates on the marketplace.** Its problem is `COMPLETE`=2 — **no CMS and no pricing "
  "page**"),
 ("Recruitify", "paid `[?]`", "recruitment agency",
  4, 4, 3, 5, 4, 5, "blog/CMS, team",
  "**[Demo verified.](https://recruitify.framer.website/)** *\"Connecting Top Talent with "
  "Leading Companies.\"* Process is already Consultation → Screening → Placement; ships "
  "services, stats, testimonials, case studies, FAQ, pricing, 8–10 pages. **Last round's pick "
  "— and it won mostly on `RECOPY`, which you have just told me not to weight.** Still strong, "
  "but the missing CMS matters more now"),
 ("Cubicles", "~$59 `[?]`", "corporate consulting",
  3, 2, 4, 4, 4, 3, "pricing, testimonials, booking",
  "**[Demo verified.](https://cubicles.framer.website/)** Has **case studies and a real "
  "blog/CMS**, plus industries and about. But `CONVERT`=2: weak repeated CTA, no pricing, no "
  "objection block. **A brochure, not a funnel**"),
 ("Recruitment Hub", "**free**", "recruitment consulting",
  3, 4, 3, 5, 3, 5, "**CMS, case studies**",
  "**[Demo verified.](https://recruitment-hub.framer.website/)** *\"We help you hire the "
  "right people, faster.\"* Good persuasion structure — **why-us comparison**, 3-step "
  "process, benefits, **pricing (2 plans)**, FAQ. Free. But **no CMS and no case studies**, "
  "which is the tooling gap that bites"),
 ("HRPro", "paid `[?]`", "HR / recruiting agency",
  3, 3, 3, 4, 4, 4, "unverified",
  "**Not demo-verified — listing only.** Open the demo before considering it"),
 ("Recruitment (Shah)", "**free**", "recruitment / HR",
  3, 3, 3, 4, 3, 4, "unverified", "**Not demo-verified — listing only.** Free"),
 ("Nakula / Fabrica / Lyniq", "$69–129 `[?]`", "premium agency",
  4, 3, 4, 3, 4, 3, "unverified",
  "**Not demo-verified.** The 'looks expensive' tier — and usually the heaviest, which fights "
  "`CONVERT` on a phone"),
 ("Greenleaf", "**free**", "ESG consulting",
  2, 3, 4, 4, 2, 2, "CMS proof slot, pricing, booking",
  "**[Demo verified.](https://greenleaf.framer.website/)** Clean and free, but thin on tooling "
  "and no bundle"),
 ("Talentify", "**free**", "❌ **candidate job board**",
  2, 2, 3, 1, 3, 2, "everything employer-facing",
  "**[Demo verified — disqualified.](https://talentify.framer.website/)** *\"Your gateway to "
  "remote tech careers.\"* Featured roles, application flow. **This is the supply side, and a "
  "job-board shape is what risks Meta's Employment Special Ad Category** — a 10–29% CAC tax"),
 ("TalentBridge", "paid `[?]`", "❌ **HR SaaS product**",
  2, 3, 3, 1, 3, 1, "everything services-shaped",
  "**[Demo verified.](https://talentbridge.framer.website/)** An all-in-one HR platform with "
  "integrations and *Request Demo*. **A product site, not a services firm.** Single page, no "
  "CMS"),
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
    SUB = ["COMPLETE", "CONVERT", "STABLE", "SHAPE", "NETCOST", "RECOPY"]
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

    P("---\n\n## 3. Re-weighted: edit work is now the whole metric\n")
    P("> *\"We need a framework to edit and do least work. We don't care about other "
      "things.\"*\n")
    P("That collapses the scoring into one question — **how far is this template from the site "
      "you need?**\nEdit distance decomposes into five terms, and `SHAPE` dominates because a "
      "wrong-shaped template is not\na restyle, it is a different website.\n")
    P("**On \"consider hundreds\":** I did not enumerate hundreds, and I would not trust it if "
      "I had. **Three\ntimes in this project a listing has been wrong** — `conversion.framer."
      "website` turned out to be a\ngeneric Framer starter page, Framer serves a soft-200 for "
      "slugs that do not exist, and aggregator\narticles repeat each other. What changed the "
      "answer was **opening six demos and reading what is\nactually on them.** Verification "
      "beat enumeration, and the biggest finding came from a search I had\nnot run at all — "
      "recruitment templates.\n")

    P("---\n\n## 4. The criteria\n")
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

    P("---\n\n## 5. The top 10, ranked on edit work\n")
    P(f"Scored on the {len(SUB)} assessable criteria only — {subw} of 100 points. "
      "**`MOBILEHERO` and `SPEED` are\ndeliberately absent**, which is why the top score here "
      "is not a recommendation.\n")
    P("| # | Template | Price | Complete | Convert | Stable | Shape | **Score** | "
      "**You must build** | Note |")
    P("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        P(f"| {i} | **{r[0]}** | {r[1]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | **{sc(r):.0f}** | "
          f"{r[9]} | {r[10]} |")
    P("")
    P("*Names and prices are from marketplace aggregators and are marked `[?]` — **verify both "
      "on Framer\nbefore buying**, since listings and pricing churn.*\n")

    P("---\n\n## 6. The phone test — still run it\n")
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

    P("---\n\n## 7. What I would actually do\n")
    P("**Funnelz.** It is **the only template found with the full tooling set** — CMS, pricing, "
      "case studies,\ntestimonials, team, booking in the nav — and it was built as a lead-gen "
      "site, so the persuasion\norder is already right for cold paid traffic. Its one weakness "
      "was the funnel-agency voice, and\n**that is a copy job, which you have said is free.**\n")
    P("| | |\n|---|---|")
    P("| **Why not Recruitify** | It was last round's pick and it won largely on `RECOPY`=5. "
      "**With that weight cut from 15 to 5, its missing CMS is no longer offset.** Still second, "
      "still good, and the better choice if you would rather start from recruitment language "
      "than rewrite funnel language |")
    P("| **Why not Conversion** | **The best conversion architecture of anything found** and the "
      "only one with real stability evidence — but `COMPLETE`=2. **No CMS and no pricing page** "
      "is the largest build cost on the list, and it is exactly the tooling you said must "
      "already be there |")
    P("| **Steal from Conversion anyway** | Its **comparison table** and **Results metrics "
      "block** are the two strongest conversion devices found. Rebuild both inside whatever you "
      "pick — the comparison block is where the **$5,000–16,500/mo vendor-invoice** argument "
      "lives |")
    P("")
    P("### What changed, and why\n")
    P("| Round | Weighting | Winner |\n|---|---|---|")
    P("| Round 1 | Mobile + speed + sections | Conversion |")
    P("| Round 2 | **Edit distance, `RECOPY` at 15** | **Recruitify** |")
    P("| **Round 3** | **`COMPLETE` 30 · `CONVERT` 25 · `STABLE` 20, `RECOPY` cut to 5** | "
      "**Funnelz** |")
    P("")
    P("**Recruitify topped round two because I weighted register distance at 15**, reading "
      "*\"least work\"* as\n*least editing*. You have corrected that: editing is free, tooling "
      "is not. **That single weight change\nis the whole difference** — it is worth knowing "
      "which criterion is carrying a recommendation.\n")
    P("### Still disqualified regardless of weighting\n")
    P("**Talentify** and **TalentBridge** — the two templates with *talent* in the name. One is "
      "a\n**candidate-facing job board** (the supply side, and the shape that risks Meta's "
      "Employment Special Ad\nCategory at a **10–29% CAC tax**), the other is an **HR SaaS "
      "product page**. Neither is a copy problem.\n")
    P("**Then run the phone test** (§6) on Funnelz and Recruitify before paying, and **confirm "
      "the 3-months-Pro\ncode is on the listing** — it is creator-dependent and it is what "
      "makes paid cheaper than free.\n")

    open(OUT, "w").write("\n".join(L))
    print(f"{len(T)} templates scored on {len(SUB)} of {len(DIM)} criteria "
          f"({subw}/100 pts assessable)")
    for r in rows:
        print(f"  {sc(r):5.1f}  {r[0]:28s} {r[1]}")


if __name__ == "__main__":
    main()
