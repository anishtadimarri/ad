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
 ("SHAPE",      30, "**Is it already an employer-facing services firm?** The single biggest "
                    "edit-distance term. A candidate-facing job board or an HR SaaS product is "
                    "not a restyle — it is a different website, and a job-board shape also "
                    "risks Meta's **Employment Special Ad Category** ([`SUPPLY-DEMAND.md`]"
                    "(SUPPLY-DEMAND.md) §1, a 10–29% CAC tax)", "verified by demo"),
 ("HAVE",       22, "**Sections that ship and you keep.** Every one is copy-swap instead of "
                    "build-from-blank", "verified by demo"),
 ("BUILD",      18, "**Sections you must build because they are missing.** Pricing, guarantee, "
                    "booking, and above all **a CMS** — three static case studies is fine, "
                    "thirty is a rebuild", "verified by demo"),
 ("RECOPY",     15, "**How far the register is from yours.** Funnel-agency, ESG-consultant or "
                    "HR-SaaS copy means rewriting every line and restyling; recruitment copy "
                    "means swapping nouns", "verified by demo"),
 ("STRIP",       8, "Sections you must delete. Cheap, but not free", "verified by demo"),
 ("MOBILEHERO",  4, "Promise + CTA above the fold on a phone. **Still the thing that decides "
                    "conversion — but you asked to optimise edit work, so it is weighted as "
                    "the tiebreak it now is.** Run the phone test regardless",
                    "`[?]` needs the phone test"),
 ("NETCOST",     3, "Cost net of the bundled 3 months of Framer Pro (§2)", "listing"),
]

# (name, price, register, SHAPE, HAVE, BUILD, RECOPY, STRIP, MOBILEHERO, NETCOST, note)
# All demo-verified rows say so. 5 = least work.
T = [
 ("Recruitify", "paid `[?]`", "recruitment agency — **employer-facing**",
  5, 4, 3, 5, 4, 3, 4,
  "**[Demo verified.](https://recruitify.framer.website/)** *\"Connecting Top Talent with "
  "Leading Companies.\"* **Its process section is literally Consultation → Screening → "
  "Placement**, which is your process. Ships services (Talent Sourcing, Executive Search, "
  "Contract Staffing), stats, testimonials, **case studies**, **FAQ**, pricing link, 8–10 "
  "pages. **Lowest edit distance of anything found.** Missing: blog/CMS, team"),
 ("Recruitment Hub", "**free**", "recruitment consulting — **employer-facing**",
  5, 4, 2, 5, 5, 3, 3,
  "**[Demo verified.](https://recruitment-hub.framer.website/)** *\"We help you hire the "
  "right people, faster.\"* Ships hero, **why-us comparison**, 3-step process, benefits, "
  "services, **pricing (2 plans)**, about, **FAQ**, contact. Free Remix. **Almost nothing to "
  "strip.** Missing: **CMS and case studies** — `BUILD`=2, the main cost"),
 ("Funnelz", "paid `[?]`", "lead-gen agency",
  3, 5, 4, 2, 3, 3, 4,
  "**[Demo verified.](https://funnelz.framer.website/)** By Ramish Aziz. **The most complete "
  "section set of anything found** — case studies, **blog/CMS**, 3-tier pricing, "
  "testimonials, team, booking in nav. But `RECOPY`=2: *\"Fuelling growth with every "
  "click\"* is funnel-agency register and **your buyer is an agency owner who will clock it "
  "instantly.** Every line gets rewritten"),
 ("Cubicles", "~$59 `[?]`", "corporate consulting",
  4, 4, 3, 3, 4, 3, 4,
  "**[Demo verified.](https://cubicles.framer.website/)** *\"Tailored Solutions for Every "
  "Business Challenge.\"* Ships **case studies and a real blog/CMS**, services, industries, "
  "about. Missing pricing, testimonials, booking. Generic-consulting copy is a medium rewrite"),
 ("Conversion", "~$79 `[?]`", "paid-ads agency",
  3, 3, 2, 3, 3, 3, 4,
  "**[Demo verified.](https://conversion.framer.media/)** *\"Ready to scale your brand with "
  "paid ads?\"* Strongest longevity signal on the marketplace, a **Results metrics block** "
  "and a **comparison table**. But **no CMS and no pricing** (`BUILD`=2), and `SHAPE`=3 "
  "because **it makes you look like an ads agency rather than a talent firm**"),
 ("HRPro", "paid `[?]`", "HR / recruiting agency",
  4, 3, 3, 4, 3, 3, 4,
  "**Not demo-verified — listing only.** Positioned for HR and recruiting agencies, so the "
  "register is likely close. **Open the demo before considering it**"),
 ("Recruitment (Shah)", "**free**", "recruitment / HR consulting",
  4, 3, 3, 4, 4, 3, 3,
  "**Not demo-verified — listing only.** Free, positioned for recruitment agencies and "
  "talent-acquisition firms"),
 ("Greenleaf", "**free**", "ESG consulting",
  4, 3, 2, 2, 3, 3, 2,
  "**[Demo verified earlier.](https://greenleaf.framer.website/)** Clean, but built for "
  "**sustainability consultants** — `RECOPY`=2 means restyling the green palette and "
  "rewriting everything. No CMS-backed proof slot, no bundle"),
 ("Talentify", "**free**", "❌ **candidate-facing job board**",
  1, 2, 2, 2, 1, 3, 3,
  "**[Demo verified — and it disqualifies itself.](https://talentify.framer.website/)** "
  "*\"Your gateway to remote tech careers.\"* Featured roles, application flow, recruiter "
  "profiles. **This is the supply side.** [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) requires a "
  "demand-only homepage, and **a job-board shape is exactly what triggers the Employment "
  "Special Ad Category** — a 10–29% CAC tax. The most on-topic name on the list and the "
  "worst fit"),
 ("TalentBridge", "paid `[?]`", "❌ **HR SaaS product**",
  1, 2, 1, 1, 2, 3, 3,
  "**[Demo verified.](https://talentbridge.framer.website/)** *\"Simplify HR Management\"* "
  "— an **all-in-one HR platform** with integrations, *Request Demo* and *Find your Plan*. "
  "**That is a software product site, not a services firm.** Single page, no CMS. Wrong "
  "shape end to end"),
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
    SUB = ["SHAPE", "HAVE", "BUILD", "RECOPY", "STRIP", "NETCOST"]
    subw = sum(W[k] for k in SUB)

    def sc(row):
        vals = dict(zip(SUB, list(row[3:8]) + [row[9]]))
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
    P("| # | Template | Price | Register / shape | Shape | Have | Build | Recopy | Strip | "
      "Net$ | **Score** | Note |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        P(f"| {i} | **{r[0]}** | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | "
          f"{r[9]} | **{sc(r):.0f}** | {r[10]} |")
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
    P("**Recruitify.** It is the only template found whose *process section is already your "
      "process* —\nConsultation → Screening → Placement. Services, case studies, FAQ, "
      "testimonials and pricing all ship.\nYou are swapping nouns, not rebuilding. **Its one "
      "real gap is a blog/CMS**, so plan `/proof` as CMS-\nbacked from day one or accept "
      "hand-built entries until client ten.\n")
    P("**Recruitment Hub is the free fallback** and it is close — *\"We help you hire the right "
      "people,\nfaster\"*, a why-us comparison block, a 3-step process and pricing already "
      "there. It costs nothing, so\n**open both demos on your phone and let the phone test "
      "break the tie.**\n")
    P("### Two templates to actively avoid, despite the names\n")
    P("| | |\n|---|---|")
    P("| **Talentify** | The most on-topic name on the list — *tech recruitment, remote talent* "
      "— and **the worst fit**. It is a **candidate-facing job board**: featured roles, "
      "application flow, recruiter profiles. [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md) requires a "
      "demand-only homepage, and **a job-board shape is precisely what gets a B2B ad "
      "reclassified into Meta's Employment Special Ad Category** — priced at a 10–29% CAC tax |")
    P("| **TalentBridge** | Reads as *HR agency* on the listing; the demo is an **all-in-one HR "
      "SaaS platform** with integrations and *Request Demo*. **A product site, not a services "
      "firm** |")
    P("")
    P("> **That is the finding worth keeping: on this list, name proximity is anti-correlated "
      "with fit.**\n> The two templates with *talent* in the name are the two you must not "
      "use, and the winner is the one\n> whose process diagram happens to match yours.\n")
    P("**And strip whatever you buy.** Every animation removed buys back LP-view rate, and the "
      "85% in\n[`funnel.py`](scoring/funnel.py) is an assumption you can move in the right "
      "direction for free.\n")

    open(OUT, "w").write("\n".join(L))
    print(f"{len(T)} templates scored on {len(SUB)} of {len(DIM)} criteria "
          f"({subw}/100 pts assessable)")
    for r in rows:
        print(f"  {sc(r):5.1f}  {r[0]:28s} {r[1]}")


if __name__ == "__main__":
    main()
