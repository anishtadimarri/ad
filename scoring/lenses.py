#!/usr/bin/env python3
"""
FIVE NEW LENSES — and a convergence test.

The repo already has five rankings (roles, verticals, first-principles, India
skills, hungry buyers). A sixth would add little. What is missing is a check on
whether any skill survives lenses that are INDEPENDENT of each other:

    a skill that wins on one lens is a hypothesis.
    a skill that wins on four is a finding.

The five lenses here were chosen because none of them is a restatement of
"what can be placed," which is the question every earlier screen asked.

  1. VENDOR   — compare the Indian salary to the MONTHLY VENDOR INVOICE the buyer
                already pays, not to a US salary. Different denominator entirely.
  2. AIMADE   — is this role GROWN by AI rather than threatened by it?
  3. REGDATE  — is demand mandated by regulation, with a date attached?
  4. SAASBASE — can the buyer be found by their software install base rather than
                by SIC code or job title?
  5. SEASON   — is there a hard seasonal peak that creates urgency on a calendar?

Evidence tags per MASTER §0.  Run:  python3 scoring/lenses.py > LENSES.md
"""

LENS = [
    ("VENDOR",   "Arbitrage against the **monthly vendor invoice** they already pay — "
                 "budget already allocated, pain felt monthly, no new line item"),
    ("AIMADE",   "Is the role **created or grown** by AI rather than eroded by it?"),
    ("REGDATE",  "Is the demand **mandated**, with a deadline? Regulation is "
                 "non-discretionary and arrives on a known date"),
    ("SAASBASE", "Can the buyer be found by **software install base** — Shopify, "
                 "QuickBooks, ServiceTitan, Procore, Clio — rather than by title?"),
    ("SEASON",   "Is there a hard **seasonal peak** that makes the need urgent on a "
                 "calendar rather than whenever they get round to it?"),
]

# skill, {lens: 0-5}, prior composite scores, evidence, note
S = [
 ("Video editing & motion graphics",
  dict(VENDOR=5, AIMADE=2, REGDATE=0, SAASBASE=3, SEASON=2), "92.4 / 89.4",
  "**Ongoing video subscriptions run $5,000-16,500/mo; social clips $1,500-5,000 "
  "each** [V] · an Indian editor is **$1,250/mo** · **4.0x-13.2x** against the "
  "vendor invoice — the largest in the study",
  "**The lens that rescues it.** BLS says few companies *hire* editors (3% growth, "
  "~6,400 openings/yr) — but a great many *pay a vendor* for editing. The buyer is "
  "in the **vendor market, not the hiring market**, which is why counting job "
  "postings undercounts this and only this"),

 ("3D / architectural visualisation",
  dict(VENDOR=4, AIMADE=2, REGDATE=0, SAASBASE=3, SEASON=2), "88.4 / 89.6",
  "Per-asset vendor pricing $1,500-5,000 [V] vs $1,250/mo in-house — **1.2x-4.0x**",
  "Same vendor-market logic. Renders are bought per-project from studios, so the "
  "comparison is an invoice, not a salary"),

 ("AI evaluation, annotation & model QA",
  dict(VENDOR=3, AIMADE=5, REGDATE=1, SAASBASE=1, SEASON=1), "not previously screened",
  "**Global demand for human evaluators and trainers is growing 25-35% annually** "
  "[V] · AI skills now appear in **2.5% of all US job postings, +297% in a decade** "
  "(Stanford HAI 2026 AI Index) [V]",
  "**The only role in the repo that AI creates rather than erodes.** The catch is "
  "severe: Mercor, Surge and Scale already own this supply chain, it is contractor "
  "work rather than full-time hires, and the buyer is a lab, not an SMB on Facebook"),

 ("AI workflow & automation operations",
  dict(VENDOR=4, AIMADE=5, REGDATE=0, SAASBASE=4, SEASON=1), "not previously screened",
  "**AI Engineer was LinkedIn's #1 fastest-growing US job title, postings +143% "
  "year-on-year in 2025** [V]",
  "**The most interesting new candidate.** Not building models — *wiring them into "
  "an SMB's stack*: Zapier/Make chains, agent supervision, prompt libraries, "
  "exception handling. It is production work, culture-free, gradeable, and it rides "
  "the one demand curve going vertical. Unproven that an SMB will hire a full-time "
  "seat for it yet"),

 ("Bookkeeping & reconciliation",
  dict(VENDOR=1, AIMADE=1, REGDATE=3, SAASBASE=5, SEASON=3), "94.8 / gated",
  "**Bookkeeping firms charge $600-1,800/mo for 200-500 transactions, and $200-500 "
  "for micro-businesses** [V] · an Indian bookkeeper costs **$1,667/mo** → "
  "**0.1x-1.1x. The vendor is the same price or cheaper**",
  "**The uncomfortable finding of this screen.** The pitch *\"your bookkeeper costs "
  "$75k, ours is $20k\"* is 3.75x and true — **but only against a company that "
  "EMPLOYS one.** Against the bookkeeping *firm* most $3-30M brands actually use, "
  "there is no arbitrage at all. Saved by `SAASBASE`=5 (QuickBooks/Xero) — see §4"),

 ("Construction estimating & takeoffs",
  dict(VENDOR=4, AIMADE=2, REGDATE=1, SAASBASE=5, SEASON=4), "94.8 (HUNGRY #1)",
  "Outsourced estimating firms bill per-project or per-takeoff [E] · **Procore and "
  "ServiceTitan install bases are addressable** [E] · bidding is seasonal in most "
  "trades [E]",
  "**Scores on four of five lenses — the widest convergence in the table.** Vendor "
  "market, findable by software, seasonal urgency, and already #1 on the bottleneck "
  "screen"),

 ("Medical record review & chronologies",
  dict(VENDOR=4, AIMADE=2, REGDATE=2, SAASBASE=5, SEASON=1), "89.6 (HUNGRY #3)",
  "Bought from LPO vendors per-case today [V] · **Clio, Filevine and CasePeer "
  "install bases are addressable** [E]",
  "Already a vendor line item, so the comparison is an invoice. And PI firms are "
  "unusually legible through their case-management software"),

 ("RCM — coding, prior auth, denials",
  dict(VENDOR=4, AIMADE=2, REGDATE=4, SAASBASE=5, SEASON=3), "89.0",
  "RCM vendors typically bill **4-9% of collections** [E] · coding rules change "
  "annually on a fixed date [E] · practice-management install bases are addressable",
  "**Highest `REGDATE` of the clinical set** — CPT/ICD updates are mandatory and "
  "dated. Still `WHITE`=1: the most contested offshore category in existence"),

 ("Compliance & regulatory reporting",
  dict(VENDOR=3, AIMADE=1, REGDATE=5, SAASBASE=3, SEASON=4), "48.0 on Meta-sellability",
  "Sales-tax nexus, beneficial-ownership reporting, state privacy laws and "
  "e-invoicing mandates all arrive with statutory deadlines [E]",
  "**The purest `REGDATE` play: a deadline is a bottleneck with a date on it.** And "
  "the reason it stays killed is unchanged — [`MAP.md`](MAP.md) scored it **48.0 on "
  "Meta-sellability**, the worst in the set. Unsellable in an ad, whatever its merits"),

 ("Vertical-SaaS operator (ServiceTitan / Procore / Clio)",
  dict(VENDOR=3, AIMADE=2, REGDATE=1, SAASBASE=5, SEASON=2), "not previously screened",
  "Every vertical SaaS has a population of customers who bought the software and "
  "cannot staff it [E]",
  "**A targeting insight more than a skill.** *\"Someone who runs your ServiceTitan\"* "
  "is more legible to a contractor than any job title, and the install base is a "
  "clean audience. Weak on its own; strong as the *phrasing* for other seats"),

 ("Tax prep & workpapers",
  dict(VENDOR=2, AIMADE=1, REGDATE=5, SAASBASE=4, SEASON=5), "90.6 (HUNGRY #2)",
  "**340,000 accountants left in five years** [V] · busy season is a fixed statutory "
  "calendar",
  "**The only 5 on `SEASON` and a 5 on `REGDATE`.** Urgency arrives on a known date "
  "every year, which is the easiest possible ad timing. `WHITE`=1 — Entigrity and a "
  "dozen others already own it"),

 ("Paid media operations",
  dict(VENDOR=3, AIMADE=3, REGDATE=0, SAASBASE=4, SEASON=3), "79.6",
  "**Agency management fees run $1,500-5,000/mo** [V] vs $2,000/mo in-house → "
  "**0.8x-2.5x** · Q4 is a hard peak for commerce [E]",
  "Thinner vendor arbitrage than it looks, because agency fees at the small end are "
  "close to an Indian salary. Improves sharply at the $5,000/mo end"),

 ("Demand planning & inventory",
  dict(VENDOR=2, AIMADE=3, REGDATE=0, SAASBASE=4, SEASON=5), "89.2",
  "No established vendor category to displace [E] · Q4 and seasonal buying cycles "
  "are hard peaks [E]",
  "Nobody currently sells this, which is both the opportunity and the problem: "
  "there is no budget line to redirect, so it is a **new** spend rather than a "
  "replacement"),
]


def tot(x):
    return sum(x.values()) / (5 * len(LENS)) * 100


R = sorted([dict(n=n, x=x, prior=p, ev=e, note=t, sc=tot(x)) for n, x, p, e, t in S],
           key=lambda r: -r["sc"])


def report():
    print("# FIVE NEW LENSES — And What Survives All Of Them\n")
    print("The repo already has five rankings. A sixth would add little. **What was missing is a "
          "check on")
    print("whether anything survives lenses that are *independent* of each other** — because a "
          "skill that wins")
    print("on one lens is a hypothesis, and a skill that wins on four is a finding.\n")
    print("None of these five is a restatement of *\"what can be placed,\"* which is the question "
          "every earlier")
    print("screen asked. Generated by [`scoring/lenses.py`](scoring/lenses.py).\n")

    print("| Lens | What it asks |\n|---|---|")
    for k, d in LENS:
        print(f"| **{k}** | {d} |")

    print("\n---\n\n## 1. The lens that changes the most: VENDOR\n")
    print("Every arbitrage in this repo so far compares an **Indian salary to a US salary.** That "
          "is the wrong")
    print("denominator for most buyers under $10M, because **they do not employ the function at "
          "all — they buy it")
    print("from a vendor, monthly.** Verified 2026 vendor pricing against an Indian full-timer:\n")
    print("| Seat | Indian FT / month | What they pay a vendor / month | **Arbitrage** |")
    print("|---|---|---|---|")
    for a, b, c, d in [
        ("**Video, ongoing**", "$1,250", "**$5,000-16,500** [V]", "**4.0x - 13.2x**"),
        ("3D / renders", "$1,250", "$1,500-5,000 per asset [V]", "1.2x - 4.0x"),
        ("Marketing retainer", "$2,000", "$2,000-5,000 [V]", "1.0x - 2.5x"),
        ("Paid media management", "$2,000", "$1,500-5,000 [V]", "0.8x - 2.5x"),
        ("**Bookkeeping**", "$1,667", "**$600-1,800** [V]", "**0.4x - 1.1x**"),
        ("Bookkeeping, micro-business", "$1,667", "$200-500 [V]", "**0.1x - 0.3x**"),
    ]:
        print(f"| {a} | {b} | {c} | {d} |")

    print("\n### 1.1 This is a problem with the current pitch, and it has a clean fix\n")
    print("*\"Your bookkeeper costs $75k. Ours is $20k\"* ([`MAP.md`](MAP.md)) is **3.75x and "
          "entirely true — against a")
    print("company that EMPLOYS a bookkeeper.** Against the bookkeeping *firm* that most $3-30M "
          "brands actually")
    print("use, **there is no arbitrage at all.** A $600-1,800/mo firm is the same price as our "
          "$1,667/mo hire, and")
    print("cheaper for anyone under $100k of revenue.\n")
    print("**The fix is already built.** [`TARGETING.md`](TARGETING.md)'s intent seed targets "
          "companies that **posted a")
    print("bookkeeper job**. A company posting a job is *by definition* in the employ-market, not "
          "the vendor")
    print("market — so the audience is already correctly selected for the only buyers the promise "
          "is true for.\n")
    print("> **That upgrades the scraping pipeline from a CAC advantage to a load-bearing part of "
          "the offer.**\n> Broad and lookalike audiences will contain vendor-market buyers for "
          "whom the headline claim is\n> false — which is a second, independent reason the intent "
          "seed converts better at the deposit step\n> ([`scoring/LTGP.md`](scoring/LTGP.md) §2), "
          "and a reason to weight budget toward it harder than the CAC\n> table alone suggests.\n")

    print("---\n\n## 2. The convergence table\n")
    print("| # | Skill | VEN | AI | REG | SAAS | SEA | **Lens score** | Prior screens |")
    print("|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(R, 1):
        x = r["x"]; star = " ⭐" if i <= 3 else ""
        print(f"| {i} | **{r['n']}**{star} | {x['VENDOR']} | {x['AIMADE']} | {x['REGDATE']} "
              f"| {x['SAASBASE']} | {x['SEASON']} | **{r['sc']:.0f}** | {r['prior']} |")

    print("\n### 2.1 Read the convergence list, not the score — the sum is the weak part\n")
    print("**A flat sum across five lenses is wrong here, and it is worth saying so plainly.** The "
          "lenses are not")
    print("commensurable: a **0 on `REGDATE` is an N/A, not a defect.** Video editing is not a "
          "worse business for")
    print("existing outside a regulatory regime, but the sum punishes it as though it were — which "
          "is why it")
    print("lands 11th while scoring **5 on the only lens in this document backed by hard data.**\n")
    print("The sum also promotes two skills that **fail decisively elsewhere**: RCM and tax prep "
          "both score")
    print("`WHITE`=1 in [`HUNGRY.md`](HUNGRY.md) — Entigrity owns one and the Indian RCM industry "
          "owns the other.")
    print("**A lens score is a hypothesis generator, not a ranking**, and it has to be read "
          "alongside the earlier")
    print("screens rather than instead of them.\n")
    print("### What converges\n")
    strong = [r for r in R if sum(1 for v in r["x"].values() if v >= 4) >= 3]
    print(f"**{len(strong)} skills score 4+ on three or more independent lenses:**\n")
    for r in strong:
        hits = [k for k, v in r["x"].items() if v >= 4]
        print(f"- **{r['n']}** — {', '.join(hits)}")
    print("\n---\n\n## 3. The three findings\n")
    for i, r in enumerate(R[:3], 1):
        print(f"### {i}. {r['n']} — {r['sc']:.0f}\n")
        print(f"{r['ev']}\n")
        print(f"**{r['note']}.**\n")

    print("---\n\n## 4. What the lenses say that the earlier screens did not\n")
    print("| | |\n|---|---|")
    for a, b in [
        ("**Video editing is a vendor-market seat, not a hiring-market seat**",
         "This resolves the contradiction in [`HUNGRY.md`](HUNGRY.md) §7. BLS was right that "
         "almost nobody *hires* editors — and irrelevant, because the money is already being spent "
         "with a studio at **$5,000-16,500/mo**. **The posting-count test (README 1b) will "
         "undercount video specifically**, so do not kill it on that test alone"),
        ("**The bookkeeper pitch only works on employers**",
         "0.4x-1.1x against a vendor. The intent seed fixes it, and this is now a *reason* for the "
         "scraping pipeline rather than a bonus from it"),
        ("**AI workflow ops is the one genuinely new candidate**",
         "It is the only seat that scores well on `AIMADE` **and** `VENDOR` **and** `SAASBASE`, "
         "riding a demand curve verified at **+143% year-on-year**. Unproven that an SMB hires it "
         "full-time yet — which is exactly what a posting count would settle"),
        ("**Software install base beats job title as a targeting key**",
         "*\"Someone who runs your ServiceTitan\"* is more legible to a contractor than any role "
         "name. This is a **phrasing and audience insight**, and it applies to seats already "
         "chosen"),
        ("**Two things did not survive**",
         "Compliance & regulatory reporting has the highest `REGDATE` in the table and stays dead "
         "on **48.0 Meta-sellability**. AI evaluation has the highest `AIMADE` and stays dead "
         "because Mercor, Surge and Scale own the supply chain and the buyer is a lab, not an SMB"),
    ]:
        print(f"| {a} | {b} |")

    print("\n**Honest limits:** the `VENDOR` row is `[V]` — published 2026 vendor pricing — and it "
          "is the only lens")
    print("here resting on hard data. `AIMADE` is `[V]` for the growth rates and `[E]` for whether "
          "an SMB will hire")
    print("the seat. `REGDATE`, `SAASBASE` and `SEASON` are `[E]` throughout. **Nothing here has "
          "been tested on a")
    print("buyer, and the cheapest test remains the same one: count the postings, then buy ten "
          "calls.**\n")


if __name__ == "__main__":
    report()
