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
    A(f"> **No — same domain, separate paths.** The reason is not stylistic. It is a "
      f"**{lo[5]:.0f}–{hi[5]:.0f}% CAC tax**\n> arriving through Meta's ad policy, priced in "
      f"§2 off the funnel model itself.\n")

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
    open(OUT, "w").write("\n".join(doc))
    print(f"base CAC ${base:,.0f} -> " +
          ", ".join(f"{lb}: ${c:,.0f} ({d:+.0f}%, {r:.2f}:1)"
                    for lb, _, c, r, _, d in rows))


if __name__ == "__main__":
    main()
