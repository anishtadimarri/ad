#!/usr/bin/env python3
"""
Should supply and demand live on the same page?

Asked plainly, and it has a quantitative answer rather than a stylistic one, because
Meta treats employment advertising as a **Special Ad Category** and the model in
scoring/ltgp.py puts 45% of paid spend on lookalike audiences -- which that category
removes outright.

Confirmed restrictions on Employment ads (job opportunities, internships, job boards):
  * lookalike audiences built on Meta's data are unavailable
  * Special Ad Audiences were removed for recruitment on 12 October
  * states can be targeted, ZIP codes cannot, and location exclusion is disallowed
  * age must be 18-65+ and all genders must be included
  * demographic, behavioural and interest options are limited
  * custom audiences from your own first-party data ARE still permitted

That last line matters: TARGETING.md's intent seed is a custom audience scraped from
job postings, so it survives. The lookalike leg does not.

Classification is a review decision, and Meta reviews the ad creative AND the landing
page. A page that prominently offers job opportunities raises the odds that a B2B ad
gets reclassified as employment. This file prices that outcome instead of asserting it.

Blended CAC is spend-weighted (total cost / total placements) and is computed by driving
the real funnel in scoring/funnel.py, not by a closed form -- see the note at the top of
main() for why the algebraic version was 1.8% out.

Run:  python3 scoring/supply_demand.py > /dev/null   (writes SUPPLY-DEMAND.md)
"""

OUT = "SUPPLY-DEMAND.md"

# Drive the REAL funnel rather than a closed form. A first draft of this file
# reconstructed blended CAC as 1/sum(w/CAC) from the three published per-audience
# CACs and landed on $745 against the repo's $732 -- 1.8% out, because funnel.run()
# is non-linear (the deposit step applies an intent multiplier under a 0.60 cap) and
# the intent seed is capped by matched audience size. So: import it.
import contextlib
import io
import sys

sys.path.insert(0, "scoring")
with contextlib.redirect_stdout(io.StringIO()):     # both modules print on import
    import funnel as fn
    import ltgp

DEPOSIT = 0.24          # teardown take-up. Reproduces LTGP.md's $732 baseline exactly
GP30 = 4435.0           # 30-day gross profit per client, MODEL-V2 V2.1
GP_LIFE = 11333.0       # lifetime GP at 9 EOR months
HARD = 1.5              # the operator's hard 30-day constraint
SPEND = 5000.0

I = "Intent seed (job posters)"
L = "1% Lookalike"
B = "Broad / Advantage+"

# --- section 7: the architecture question, scored -------------------------------
# (key, weight, what it measures)
ARCH_DIM = [
    ("SACRISK",  24, "Risk of a B2B ad being reclassified into the **Employment Special Ad "
                     "Category**, which §2 prices at a 10–29% CAC tax"),
    ("BRAND",    18, "Does brand equity concentrate on one domain? Weighted high because "
                     "[`ARBITRARY.md`](ARBITRARY.md) §13 found *all hands talent* currently "
                     "returns three other organisations on Google — split equity makes that "
                     "worse"),
    ("OPSLOAD",  16, "One operator, one month to launch. Low operational intensity has been "
                     "rejected as a constraint twice"),
    ("SUPPLY",   14, "Can it actually fill the bench at volume?"),
    ("TRUST",    12, "Does a candidate see a real company with real clients, or a shell?"),
    ("BUYERSAFE", 8, "What happens when a *buyer* finds the supply page"),
    ("PIXEL",     4, "Keeping supply events out of buyer optimisation"),
    ("EV",        4, "One brand, one asset, at exit"),
]
ARCH = [
    ("A", "Two separate domains",
     dict(SACRISK=5, BRAND=2, OPSLOAD=2, SUPPLY=5, TRUST=2, BUYERSAFE=5, PIXEL=5, EV=3),
     "Cleanest possible isolation — a reviewer crawling the ad's domain finds no job content "
     "at all. But it **splits brand equity, needs a second name** after nine rounds of naming, "
     "doubles the site/hosting/analytics surface, and a candidate landing on a standalone "
     "apply-domain sees a shell"),
    ("B", "One domain, `/talent` path, demand-first homepage",
     dict(SACRISK=4, BRAND=5, OPSLOAD=5, SUPPLY=5, TRUST=5, BUYERSAFE=4, PIXEL=5, EV=5),
     "**The proposal, and it wins.** One site to build and maintain, all equity in one place, "
     "and a candidate sees the real clients. `SACRISK` is 4 not 5 because Meta reviews landing "
     "pages — mitigated by the three controls below, not by a second domain"),
    ("C", "One domain, `talent.` subdomain",
     dict(SACRISK=4, BRAND=4, OPSLOAD=4, SUPPLY=5, TRUST=4, BUYERSAFE=4, PIXEL=5, EV=5),
     "Same policy exposure as B with **none of the upside**: extra DNS, SSL and deploy target, "
     "and analytics and SEO tooling treat subdomains as separate sites. A path costs nothing "
     "and keeps everything unified"),
    ("D", "No public supply page — referral, LinkedIn and invite only",
     dict(SACRISK=5, BRAND=5, OPSLOAD=5, SUPPLY=3, TRUST=4, BUYERSAFE=5, PIXEL=5, EV=5),
     "**No job-opportunity page exists anywhere, so the category risk goes to zero** and there "
     "is nothing to build. `SUPPLY`=3 is the whole catch: fine for the first ten to twenty "
     "placements, a real constraint after that"),
]

# Employment category removes the lookalike leg. Custom audiences survive, so the
# intent seed is untouched and the 45% has nowhere to go but broad. Broad then
# degrades too, because interest and behavioural targeting are limited -- modelled
# as a CTR haircut, the same lever funnel.py's own sensitivity tests use.
SCENARIOS = [("broad CTR holds", 1.00),
             ("broad CTR −25%", 0.75),
             ("broad CTR −40%", 0.60)]


def blend(mix):
    """Spend-weighted CAC through the real funnel: total cost / total placements."""
    cost = place = 0.0
    for aud, share in mix.items():
        r = fn.run(aud, ltgp.FLOW, spend=SPEND * share)
        cost += r["cost"]
        place += r["place"]
    return cost / place


def main():
    fn.DEPOSIT_COLD = DEPOSIT
    base = blend(ltgp.MIX)
    per = {a: fn.run(a, ltgp.FLOW, spend=SPEND)["cac"] for a in (I, L, B)}
    rows = []
    for label, mult in SCENARIOS:
        old = fn.AUD[B]
        fn.AUD[B] = (old[0], old[1] * mult, old[2])
        cac = blend({I: 0.25, B: 0.75})
        fn.AUD[B] = old
        rows.append((label, per[B] * (1 / mult if mult else 1), cac,
                     GP30 / cac, GP_LIFE / cac, (cac / base - 1) * 100))

    lo, hi = rows[0], rows[-1]
    doc = []
    A = doc.append
    A("# Supply and Demand on the Same Page?\n")
    A("> **One domain. `/talent` as a path, homepage entirely demand. Not a second domain, not a "
      "subdomain —\n> and at launch, no public supply page at all.** §7 scores the four "
      "architectures; §1–§3 are why it\n> matters, which is a "
      f"**{lo[5]:.0f}–{hi[5]:.0f}% CAC tax** priced off the funnel model itself.\n")

    A("---\n\n## 1. The expensive reason: Meta's Special Ad Category\n")
    A("Meta classifies advertising for **job opportunities, internships and job boards** as "
      "*Employment*,\na Special Ad Category. Inside it:\n")
    A("| Restriction | Consequence for [`TARGETING.md`](TARGETING.md) |")
    A("|---|---|")
    A("| **Lookalike audiences built on Meta's data are unavailable**, and Special Ad Audiences "
      "were removed for recruitment on 12 October | **This is the one that costs money. "
      "[`LTGP.md`](LTGP.md) puts 45% of spend on the lookalike leg** |")
    A("| Custom audiences from your own first-party data **are still permitted** | The intent "
      "seed — a custom audience scraped from job postings — **survives** |")
    A("| States can be targeted; **ZIP codes cannot**, and location exclusion is disallowed | "
      "No metro-level concentration |")
    A("| Age must be 18–65+, all genders included | No demographic narrowing |")
    A("| Demographic, behavioural and interest options limited | **Broad gets worse too**, "
      "which is why §2 runs three scenarios |")
    A("")
    A("**Classification is a review decision, and Meta reviews the ad creative *and the landing "
      "page*.**\nA page that prominently offers jobs raises the odds that a B2B ad aimed at "
      "employers gets reclassified\nas employment. That is the mechanism — not a rule that "
      "mixing them is forbidden, but a materially\nhigher chance of landing in a category that "
      "deletes 45% of the audience plan.\n")

    A("---\n\n## 2. What the reclassification actually costs\n")
    A("Driven through the **real funnel** in [`funnel.py`](scoring/funnel.py) at the same "
      "24% teardown\ntake-up that produces [`LTGP.md`](LTGP.md)'s $732 baseline — not a closed "
      "form. A first draft of this\nfile reconstructed the blend algebraically and came out "
      "1.8% high, because the deposit step applies\nan intent multiplier under a cap and the "
      "intent seed is limited by matched audience size. The\nlost-targeting effect is modelled "
      "as a **CTR haircut on broad**, the same lever `funnel.py`'s own\nsensitivity tests "
      "use.\n")
    A("| | Intent seed | Lookalike | Broad | Blended CAC | 30-day | Lifetime |")
    A("|---|---|---|---|---|---|---|")
    A(f"| **As modelled** | 25% @ ${per[I]:,.0f} | 45% @ ${per[L]:,.0f} | "
      f"30% @ ${per[B]:,.0f} | **${base:,.0f}** | **{GP30/base:.2f}:1** | "
      f"**{GP_LIFE/base:.2f}:1** |")
    for label, _, cac, r30, rlife, delta in rows:
        A(f"| Employment category — *{label}* | 25% @ ${per[I]:,.0f} | **unavailable** | "
          f"75% | **${cac:,.0f}** *(+{delta:.0f}%)* | **{r30:.2f}:1** | {rlife:.2f}:1 |")
    A("")
    A(f"**It does not break the hard constraint.** Even the worst case, {hi[3]:.2f}:1, clears "
      f"{HARD}:1 with room —\nso this is not existential and I am not going to dress it up as "
      f"though it were. It is a\n**${lo[2]-base:,.0f}–${hi[2]-base:,.0f} per-client tax "
      f"({lo[5]:.0f}–{hi[5]:.0f}%) for no benefit whatsoever**, taken off the top of every "
      "client you\never acquire, and it compounds against the 30-day ratio that the whole plan "
      "is built to protect.\n")

    A("---\n\n## 3. The subtler reason, which is worse than it looks\n")
    A("**Pixel contamination.** Job seekers convert far more cheaply than employers — they are "
      "more numerous,\nmore motivated, and asking less of themselves. Put both offers on one "
      "page behind one conversion\nevent and Meta's optimiser will find the cheap audience, "
      "because that is precisely what it is built\nto do.\n")
    A("> Your **cost per lead falls** while your **cost per client rises**. The dashboard "
      "improves as the\n> business gets worse, and the metric that hides it is the one you look "
      "at daily. That is a nastier\n> failure than a 27% CAC tax, because the tax is at least "
      "visible.\n")
    A("It also poisons the retargeting pool and every lookalike you later build from it, so the "
      "damage\ncompounds rather than staying put.\n")

    A("---\n\n## 4. The positioning reason\n")
    A("| Claim | What an open application page says instead |")
    A("|---|---|")
    A("| *Handpicked. Graded. We recut your ad and measure retention against the original* | "
      "*We take whoever applies* |")
    A("| A curated bench you cannot access elsewhere | A job board |")
    A("| The buyer is a **bottleneck** buyer being sold speed | A **marketplace**, which is a "
      "cost centre — the exact distinction in [`HUNGRY.md`](HUNGRY.md) |")
    A("")
    A("Every high-end search firm hides candidate intake, and not by accident: **visible supply "
      "destroys the\nscarcity claim that justifies the fee.** There is also a specific trap "
      "here — [`COMPETITOR-DATA.md`](COMPETITOR-DATA.md)\n§7 found that **three of three India "
      "analogues monetise the worker and give the employer relationship\naway.** A "
      "supply-forward site is the first step down that path, and it is the exact model this plan "
      "was\nbuilt to avoid.\n")

    A("---\n\n## 5. So build it like this\n")
    A("| Surface | Audience | Rules |")
    A("|---|---|---|")
    A("| **`allhandstalent.com`** — root, and every ad destination | **Buyer only** | One offer, "
      "one CTA: the paid ad-account and creative teardown ([`OFFER.md`](OFFER.md) §9.1). No "
      "\"careers\", no \"apply\", no \"join our talent network\" above the fold |")
    A("| **`allhandstalent.com/talent`** | Supply | **Footer link only, never in the nav.** Its "
      "own conversion event, or excluded from the conversion event entirely. `noindex` if you "
      "want it invisible to Meta's page review |")
    A("| **The graded directory** | Buyer | Gated, behind the deposit. This is supply shown *to "
      "demand*, which is the opposite thing — see §6 |")
    A("")
    A("**Same domain, not a second domain.** A candidate asked to apply needs to see a real "
      "company with\nreal clients; a standalone `apply-here.com` reads as a shell, and you are "
      "an unknown operator who\ncannot afford to look like one.\n")
    A("And note what makes this cheap: **supply needs zero ad spend at launch.** Referral, "
      "LinkedIn outbound\nand the graded directory fill the bench. A page nobody advertises to "
      "does not need to be optimised\nfor anything — so separating the two costs you nothing.\n")

    A("---\n\n## 6. When this reverses\n")
    A("Once the bench exists, **showing supply becomes your strongest demand asset** — *\"forty "
      "graded editors,\neach with 3-second and 15-second retention measured against the ad they "
      "replaced\"* is the single most\npersuasive page you will ever put in front of an agency "
      "owner.\n")
    A("But that is **supply displayed to buyers, gated behind the deposit** — not an open "
      "application form.\nOne is a proof asset. The other is a job board. Same content, opposite "
      "businesses.\n")

    # ---- section 7 -------------------------------------------------------
    W = {k: w for k, w, _ in ARCH_DIM}

    def sc(d):
        return sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100

    A("---\n\n## 7. Separate domain, or one domain with separate pages?\n")
    A("The question asked directly. Four architectures, scored on what actually differs between "
      "them.\n")
    A("| Dimension | Wt | What it measures |\n|---|---|---|")
    for k, w, why in ARCH_DIM:
        A(f"| **{k}** | {w} | {why} |")
    A("")
    A("| | Architecture | " + " | ".join(k for k, _, _ in ARCH_DIM) + " | Score |")
    A("|---|---|" + "---|" * (len(ARCH_DIM) + 1))
    ranked = sorted(ARCH, key=lambda x: -sc(x[2]))
    for tag, name, d, _ in ARCH:
        mark = " ✅" if tag == ranked[0][0] else ""
        A(f"| **{tag}** | {name}{mark} | " + " | ".join(str(d[k]) for k, _, _ in ARCH_DIM) +
          f" | **{sc(d):.1f}** |")
    A("")
    for tag, name, d, why in ranked:
        A(f"**{tag} — {name} · {sc(d):.1f}** — {why}\n")
    a, b = [x for x in ARCH if x[0] == "A"][0], [x for x in ARCH if x[0] == "B"][0]
    A(f"> **B beats A by {sc(b[2])-sc(a[2]):.1f} points**, and the margin is not about policy — it "
      f"is `BRAND`, `OPSLOAD` and\n> `TRUST`. **A is safer on the one dimension I can fix with "
      f"three lines of config, and worse on the\n> three I cannot.**\n")

    A("### One argument for a separate domain that used to be true and is not\n")
    A("Meta's **Aggregated Event Measurement** historically capped you at **eight conversion "
      "events per\nverified domain**, so sharing a domain with a supply funnel meant supply "
      "events competing for those\nslots. **Meta removed the 8-event limit and manual event "
      "prioritisation in June 2025**, and domain\nverification is no longer required for AEM — "
      "events are aggregated automatically. I checked before\nwriting it down, because it is "
      "exactly the kind of stale received wisdom that would have argued for\nsplitting the "
      "domain for no reason.\n")

    A("### The three controls that do the work `SACRISK` is worried about\n")
    A("| Control | Why |\n|---|---|")
    A("| **Ads point at `/hire` or `/teardown`, never at `/`** | Page review sees a dedicated "
      "buyer page with no navigation to job content |")
    A("| **`/talent` is `noindex, nofollow`, linked once from the footer with `rel=\"nofollow\"`** "
      "| Reachable by a candidate who is told where to look; not crawled into the same site graph "
      "as the ad destination |")
    A("| **No Meta pixel on `/talent`** — or a separate dataset | Supply visitors never enter "
      "the buyer optimisation pool, the retargeting audience, or any lookalike built from it |")
    A("")
    A("### And write the supply page as proof, not as a secret\n")
    A("The instinct is to hide it. Better: **write it so a buyer finding it strengthens the "
      "pitch.** A page\nthat states the bar — *what is tested, what the pass rate is, how many "
      "applicants were rejected last\nmonth* — is evidence for the graded claim rather than "
      "against it. A page that says *\"join our talent\nnetwork\"* is a job board. **Same "
      "surface, opposite effect**, and the difference is entirely in the copy.\n")

    A("### What to actually do, in order\n")
    A("**Build B's structure. Ship D's content.** For launch month there is no public supply page "
      "at all —\n[`§5`](#5-so-build-it-like-this) already notes supply needs **zero ad spend**, "
      "and referral plus LinkedIn\noutbound fills the first ten to twenty seats. That takes "
      "`SACRISK` to zero for free.\n")
    A("Publish `/talent` when referral stops keeping up with demand — realistically month three "
      "to six —\nand publish it with the pass rate on it.\n")
    open(OUT, "w").write("\n".join(doc))
    print(f"base CAC ${base:,.0f} -> " +
          ", ".join(f"{lb}: ${c:,.0f} ({d:+.0f}%, {r:.2f}:1)"
                    for lb, _, c, r, _, d in rows))


if __name__ == "__main__":
    main()
