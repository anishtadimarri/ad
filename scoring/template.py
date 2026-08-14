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
 ("COMPLETE",   34, "**Tooling and real pages that actually exist.** Now verified by crawling "
                    "each demo's sub-paths rather than reading its homepage — a control path "
                    "returned 404 on every site, so the results are reliable",
                    "**crawled**"),
 ("CONVERT",    28, "**Funnel-optimised for cold Meta traffic.** Single-goal pages, CTA in hero "
                    "and repeated, social proof early, an objection or comparison block, "
                    "booking at the end", "verified by demo"),
 ("SHAPE",      18, "Employer-facing **services** structure — not a candidate job board, not a "
                    "SaaS product page. Structural, and a job-board shape risks Meta's "
                    "Employment Special Ad Category ([`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) §1, "
                    "a 10–29% CAC tax)", "verified by demo"),
 ("STABLE",      8, "**Cut from 20 — see §3.** In Framer there is no upstream to break: no "
                    "plugins, no dependencies, no updates to apply. Once remixed, the template "
                    "is a frozen copy inside your project", "reframed"),
 ("NETCOST",     6, "Cost net of the bundled 3 months of Framer Pro (§2)", "listing"),
 ("RECOPY",      6, "Register distance. A copy-and-colour job, not a build job", "verified"),
]

# (name, price, register, COMPLETE, CONVERT, SHAPE, STABLE, NETCOST, RECOPY, pages, note)
# COMPLETE is now scored from a CRAWL of each demo's sub-paths, not its homepage.
T = [
 ("Funnelz", "paid `[?]`", "lead-gen agency",
  4, 5, 4, 3, 4, 2, "home + **`/blog`**",
  "**Crawled.** One long homepage plus a blog. Homepage carries hero+CTA, social proof, "
  "**case studies**, services, **3-tier pricing**, team, **booking in the nav** — so pricing "
  "and team are *sections*, not pages, which is fine. **Its blog posts carry dates, "
  "categories, authors and individual URLs — the shape of a CMS collection**, which is the "
  "tooling that matters most. `COMPLETE` 5→4: fewer standalone pages than the homepage "
  "implied"),
 ("Recruitify", "paid `[?]`", "recruitment agency",
  4, 4, 5, 3, 4, 5,
  "home + **`/about` `/services`… `/pricing` `/faq` `/projects` `/contact` `/privacy` "
  "`/terms`**",
  "**Crawled — and it has the most real pages of anything tested: seven.** Including a "
  "genuine **`/pricing`**, **`/faq`**, **`/projects`** (case studies) and **`/privacy` + "
  "`/terms`**, which Meta's ad review looks for. Process is already Consultation → Screening "
  "→ Placement. **The single gap is no `/blog`, so no CMS** — proof entries would be "
  "hand-built"),
 ("Conversion", "~$79 `[?]`", "paid-ads agency",
  3, 5, 4, 3, 4, 3, "home + `/about` `/services` `/blog` `/contact`",
  "**Crawled, and it cost it.** `COMPLETE` 2→3 because four real pages do exist — but the "
  "`/blog` is **4 items with no dates, no categories and broken placeholder links including "
  "a literal `404` in the nav.** **`STABLE` 5→3**: a demo shipping broken links is a quality "
  "signal that contradicts the longevity story. Still the **best conversion architecture "
  "found** — Results metrics block, comparison table"),
 ("Cubicles", "~$59 `[?]`", "corporate consulting",
  3, 2, 4, 4, 4, 3, "home + `/about` `/services` `/blog` `/contact`",
  "**Crawled.** Four real pages including a blog, plus case studies and industries on the "
  "homepage. But `CONVERT`=2 — weak repeated CTA, no pricing, no objection block. **A "
  "brochure, not a funnel**"),
 ("Recruitment Hub", "**free**", "recruitment consulting",
  2, 4, 5, 3, 3, 5, "home + `/contact` **only**",
  "**Crawled — and it is thinner than the homepage suggested.** `COMPLETE` 3→2: **one "
  "sub-page.** Everything else is a homepage anchor. Good persuasion order (why-us "
  "comparison, 3-step process, pricing, FAQ) and free, but **no CMS, no case studies and no "
  "real page structure**"),
 ("Nakula / Fabrica / Lyniq", "$69–129 `[?]`", "premium agency",
  4, 3, 3, 4, 4, 3, "not crawled",
  "**Not verified.** The 'looks expensive' tier, usually the heaviest — which fights "
  "`CONVERT` on a phone"),
 ("HRPro", "paid `[?]`", "HR / recruiting agency",
  3, 3, 4, 3, 4, 4, "not crawled", "**Not verified.** Open the demo before considering it"),
 ("Recruitment (Shah)", "**free**", "recruitment / HR",
  3, 3, 4, 3, 3, 4, "not crawled", "**Not verified.** Free"),
 ("Greenleaf", "**free**", "ESG consulting",
  2, 3, 4, 4, 2, 2, "not crawled",
  "Clean and free, but thin on tooling, no bundle, and built for sustainability consultants"),
 ("Talentify", "**free**", "❌ **candidate job board**",
  2, 2, 1, 3, 3, 2, "not crawled",
  "**Disqualified.** *\"Your gateway to remote tech careers.\"* The supply side — and a "
  "job-board shape is what risks Meta's Employment Special Ad Category"),
 ("TalentBridge", "paid `[?]`", "❌ **HR SaaS product**",
  2, 3, 1, 3, 3, 1, "single page",
  "**Disqualified.** An all-in-one HR platform with integrations and *Request Demo*. A "
  "product site, not a services firm"),
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
    SUB = ["COMPLETE", "CONVERT", "SHAPE", "STABLE", "NETCOST", "RECOPY"]
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

    P("---\n\n## 3. Two corrections: I crawled the pages, and `STABLE` was the wrong worry\n")
    P("**I cannot log into Framer** — no account, and I will not pretend to have looked inside "
      "the editor.\nThe one thing that genuinely requires it is whether a blog is a **CMS "
      "collection or hand-built pages**,\nbecause **Framer statically generates CMS pages**, so "
      "the served HTML looks identical either way.\n")
    P("What I could do, and had not: **crawl each demo's sub-paths.** Every judgement before "
      "this was made\nfrom homepages. A control path returned **404 on all five sites**, so "
      "the results are trustworthy:\n")
    P("| Template | Real pages found | Effect |\n|---|---|---|")
    P("| **Recruitify** | **7** — `/about` `/services` `/pricing` `/faq` `/projects` "
      "`/contact` `/privacy` `/terms` | **The most of anything tested**, including legal pages "
      "that Meta's ad review looks for |")
    P("| Conversion | 4 — `/about` `/services` `/blog` `/contact` | `COMPLETE` 2→3. **But the "
      "`/blog` has broken placeholder links including a literal `404` in the nav** |")
    P("| Cubicles | 4 | As expected |")
    P("| **Funnelz** | **2** — home + `/blog` | `COMPLETE` 5→4. Pricing and team are homepage "
      "*sections*, not pages |")
    P("| **Recruitment Hub** | **1** — `/contact` only | `COMPLETE` 3→2. **Effectively a "
      "one-pager**; everything else was an anchor link |")
    P("")
    P("### And `STABLE` was importing a WordPress worry into a platform where it does not apply\n")
    P("> *\"Is stability going to be an issue for Funnelz?\"* — **No, and I had the criterion "
      "weighted wrong at 20.**\n")
    P("**In Framer there is no upstream to break.** No plugins, no dependencies, no version "
      "updates, no\nsecurity patches. When you remix a template it becomes **a frozen copy "
      "inside your own project**. A\ncreator who abandons a template cannot affect a site that "
      "is already live — unlike WordPress, where\nan unmaintained plugin is a live liability.\n")
    P("So the real question is narrower: **will the creator answer a setup question in week "
      "one?** That is\nworth something, and it is worth **8, not 20**. Cutting it also removes "
      "the main thing propping up\nConversion, whose demo **ships with broken links** — which "
      "is a better stability signal than age, and\nit points the other way.\n")

    P("---\n\n## 4. The criteria\n")
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

    P("---\n\n## 5. The ranking, after crawling\n")
    P(f"Scored on the {len(SUB)} assessable criteria only — {subw} of 100 points. "
      "**`MOBILEHERO` and `SPEED` are\ndeliberately absent**, which is why the top score here "
      "is not a recommendation.\n")
    P("| # | Template | Price | Cmpl | Conv | Shape | Stab | **Score** | **Real pages "
      "(crawled)** | Note |")
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
    P("**Recruitify — and the crawl is what moved it back to the top.** Seven real pages "
      "including `/pricing`,\n`/faq`, `/projects` and **`/privacy` + `/terms`**, against "
      "Funnelz's two. It is the only candidate that\nis already a *site* rather than a long "
      "page, and page structure is exactly the tooling you said has to\nbe there.\n")
    P("**Its one gap is the CMS.** Funnelz's blog carries dates, categories, authors and "
      "individual URLs —\nCMS-shaped — and Recruitify has no `/blog` at all. So the decision "
      "reduces to one question:\n")
    P("> **Do you need `/proof` to be CMS-backed on day one?** Under ten entries, hand-built "
      "pages in Framer\n> are fine and Recruitify wins comfortably. Past thirty, you want the "
      "collection — and adding a CMS\n> collection to a Framer site later is a normal "
      "afternoon, not a rebuild.\n")
    P("**That tips it to Recruitify**, because the thing you cannot add later is a coherent "
      "page structure,\nand the thing you can is a blog.\n")
    P("| | |\n|---|---|")
    P("| **Funnelz stays a close second** | Best tooling *on one page*, CMS-shaped blog, "
      "booking in the nav. **Pick it if you would rather add pages than add a CMS** |")
    P("| **Conversion drops** | Best conversion architecture found, but four pages, a fake "
      "blog, and **broken links shipped in the demo**. Still worth **stealing its comparison "
      "table and Results metrics block** — the comparison block is where the "
      "**$5,000–16,500/mo vendor-invoice** argument lives |")
    P("| **Recruitment Hub is out** | The crawl exposed it as a one-pager. Free, but you would "
      "build the entire site around it |")
    P("")
    P("### Four rounds, four weightings\n")
    P("| Round | What I weighted | Winner |\n|---|---|---|")
    P("| 1 | Mobile + speed + sections | Conversion |")
    P("| 2 | Edit distance, `RECOPY` at 15 | Recruitify |")
    P("| 3 | `COMPLETE` + `CONVERT` + `STABLE` at 20 | Funnelz |")
    P("| **4** | **Crawled pages; `STABLE` cut to 8** | **Recruitify** |")
    P("")
    P("**The ranking moved three times and each move came from one thing: better evidence or a "
      "corrected\nweight.** Round four is the first built on what is actually deployed at each "
      "URL rather than on a\nhomepage or a listing. **Run the phone test on Recruitify and "
      "Funnelz and buy the one that passes** —\nthat is the last check, and it is the one only "
      "you can run.\n")

    open(OUT, "w").write("\n".join(L))
    print(f"{len(T)} templates scored on {len(SUB)} of {len(DIM)} criteria "
          f"({subw}/100 pts assessable)")
    for r in rows:
        print(f"  {sc(r):5.1f}  {r[0]:28s} {r[1]}")


if __name__ == "__main__":
    main()
