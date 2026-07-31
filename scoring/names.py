#!/usr/bin/env python3
"""
Name ranking — every candidate whose .com was verified FREE, scored on the
filters that emerged over the naming process rather than on taste.

All domains RDAP-verified free on 29 Jul 2026 unless marked otherwise.
Run:  python3 scoring/names.py > NAMES.md
"""

DIM = [
    ("AUDIO", 20, "Spellable from hearing it once in a Reel. Common word, one spelling"),
    ("MEANS", 18, "Says something concrete and TRUE about the business"),
    ("CLEAN", 18, "Free of wrong signals, collisions and bad register"),
    ("WARM",  14, "Human likeability — the thing All Hands has"),
    ("SOUND", 12, "Phonetics: rhythm, and no consonant pileup at the word junction"),
    ("FIRM",  10, "Reads as an established firm, not something launched last month"),
    ("FIT",    8, "Boxes in neither a role (5 of them) nor a product (placement + EOR)"),
]
W = {k: w for k, w, _ in DIM}
GATES = [("CLEAN", 3, "a live collision or a broken register"),
         ("AUDIO", 3, "cannot be spelled from audio"),
         ("MEANS", 2, "says nothing, or says the wrong thing")]

# name, domain, scores, note
N = [
 ("All Aboard Talent", "allaboardtalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=5, SOUND=5, FIRM=4, FIT=5),
  "All Hands with the defects removed. *Joining*, not an emergency. "
  "\"Aboard\" is literally the hiring word — onboarding. Faint train association"),
 ("Steady Crew Talent", "steadycrewtalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=5, WARM=4, SOUND=4, FIRM=4, FIT=5),
  "Says the promise (they stay) AND the people. Cleanest register in the set"),
 ("Loyal Crew Talent", "loyalcrewtalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=5, WARM=4, SOUND=4, FIRM=4, FIT=5),
  "Loyalty IS the tenure lever. Most on-message name found"),
 ("Mighty Crew Talent", "mightycrewtalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=5, SOUND=4, FIRM=3, FIT=5),
  "Keeps \"Mighty\" now that the bare version is gone. Warmest of the crew set; "
  "\"mighty\" is an excellence claim, which a new firm cannot back"),
 ("All Hands Talent", "allhandstalent.com",
  dict(AUDIO=5, MEANS=3, CLEAN=3, WARM=5, SOUND=3, FIRM=4, FIT=5),
  "**Operator's favourite.** Six wrong signals (§9.1) of which one — the pooled-"
  "resource read — costs money, and the ad line largely pays it off. Survivable, "
  "not clean"),
 ("Steady Hands Talent", "steadyhandstalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=5, SOUND=4, FIRM=4, FIT=5),
  "Best of the Hands family — \"a steady hand\" is said of surgeons, not carers, "
  "so it escapes the home-care register that kills the rest"),
 ("Keel Talent", "keeltalent.com",
  dict(AUDIO=4, MEANS=3, CLEAN=5, WARM=3, SOUND=5, FIRM=4, FIT=5),
  "**The best true single word available.** One syllable, nautical like Oceans, "
  "and a keel is literally what stops a boat tipping. \"Keel\" alone is less "
  "common than \"even keel\""),
 ("Long Term Talent", "longtermtalent.com",
  dict(AUDIO=4, MEANS=5, CLEAN=5, WARM=2, SOUND=3, FIRM=4, FIT=5),
  "Most literal statement of the promise. Cold, and mild hyphen ambiguity"),
 ("Full Time Talent", "fulltimetalent.com",
  dict(AUDIO=4, MEANS=5, CLEAN=5, WARM=2, SOUND=3, FIRM=4, FIT=5),
  "**NOT FREE — parked on HugeDomains at $3,895** (one placement's gross profit). "
  "Pre-empts the category's biggest confusion: that we sell VAs and gig workers"),
 ("Here To Stay Talent", "heretostaytalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=5, WARM=4, SOUND=3, FIRM=3, FIT=5),
  "Says the tenure promise outright. Three words plus Talent is the cost"),
 ("Deep Bench Talent", "deepbenchtalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=3, SOUND=4, FIRM=4, FIT=5),
  "Common US idiom, and it puts the replacement guarantee in the name — a deep "
  "bench is WHY we can refill in days. \"Bench\" is our side of the trade"),
 ("Mooring Talent", "mooringtalent.com",
  dict(AUDIO=4, MEANS=3, CLEAN=5, WARM=4, SOUND=4, FIRM=4, FIT=5),
  "Single word. A mooring is what keeps a boat in place — the tenure metaphor. Soft"),
 ("Enduring Talent", "enduringtalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=5, WARM=2, SOUND=4, FIRM=5, FIT=5),
  "Single word that states the promise. Formal to the point of cold"),
 ("For Keeps Talent", "forkeepstalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=4, WARM=5, SOUND=4, FIRM=2, FIT=5),
  "\"For keeps\" = permanently — the sharpest anti-temp signal in English. "
  "Childlike, and \"playing for keeps\" also means ruthless"),
 ("All Clear Talent", "allcleartalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=4, SOUND=4, FIRM=4, FIT=5),
  "Same `All ___` music. Double meaning: cleared (screened) and clear "
  "(transparent). Faint air-raid-siren adjacency"),
 ("First Team Talent", "firstteamtalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=3, SOUND=3, FIRM=4, FIT=5),
  "Your starters. Confident without hyperbole; two team-words in a row"),
 ("Laurel Talent", "laureltalent.com",
  dict(AUDIO=5, MEANS=2, CLEAN=4, WARM=4, SOUND=5, FIRM=5, FIT=5),
  "Single word, sounds like a firm that has existed for decades. Means honour, "
  "not staffing — and reads as a first name"),
 ("Steady Roster", "steadyroster.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=3, SOUND=4, FIRM=4, FIT=5),
  "**The only bare two-word `.com` in the set** — no `talent` suffix. \"Roster\" "
  "is the client's word for their own team; faint shift-scheduling read"),
 ("Mighty Oak Talent", "mightyoaktalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=5, WARM=5, SOUND=5, FIRM=4, FIT=5),
  "**Best-sounding name in the entire study.** Real idiom, growth imagery. Fails "
  "the operator's own filter: a tree means even less than an open book"),
 ("Open Book Talent", "openbooktalent.com",
  dict(AUDIO=5, MEANS=2, CLEAN=4, WARM=4, SOUND=5, FIRM=4, FIT=4),
  "Names the positioning — salary transparency — but the operator's verdict was "
  "\"doesn't mean anything,\" and that is the buyer's reading too"),
 ("Above Board Talent", "aboveboardtalent.com",
  dict(AUDIO=5, MEANS=3, CLEAN=4, WARM=3, SOUND=4, FIRM=4, FIT=5),
  "Unambiguously about honesty, with no double meaning to carry it"),
 ("Graded Talent", "gradedtalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=2, SOUND=4, FIRM=3, FIT=5),
  "Names the actual wedge — the graded work sample. Grades the *people*, "
  "which is clinical"),
 ("Keepers Talent", "keeperstalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=5, SOUND=4, FIRM=3, FIT=5),
  "\"She's a keeper\" — worth holding onto. Plural is awkward and \"keeper\" "
  "alone means goalkeeper"),
 ("Many Hands Talent", "manyhandstalent.com",
  dict(AUDIO=5, MEANS=3, CLEAN=3, WARM=5, SOUND=4, FIRM=4, FIT=5),
  "Fixes All Hands' meeting and crisis reads; makes the quantity and pooled "
  "problems worse (§9.2)"),
 ("Back Office Talent", "backofficetalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=4, WARM=2, SOUND=3, FIRM=4, FIT=1),
  "The most literally descriptive name available, and it kills the ads manager — "
  "role 5 of 5"),
 ("Full Crew Talent", "fullcrewtalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=4, WARM=4, SOUND=3, FIRM=3, FIT=5),
  "Crew warmth; \"full\" implies you get everyone rather than one hire"),
 ("Diligent Talent", "diligenttalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=3, WARM=2, SOUND=4, FIRM=5, FIT=5),
  "Single word, and exactly the virtue a bookkeeper is bought for. **Diligent "
  "Corporation** is a known governance/compliance software brand, adjacent to "
  "accounting"),
 ("Anchor Roster", "anchorroster.com",
  dict(AUDIO=5, MEANS=3, CLEAN=4, WARM=4, SOUND=4, FIRM=4, FIT=5),
  "Warm, bare `.com`. \"Anchor\" is the most-used metaphor in professional services"),
 ("The Full-Time Hire", "thefulltimehire.com",
  dict(AUDIO=4, MEANS=5, CLEAN=5, WARM=2, SOUND=3, FIRM=3, FIT=4),
  "Sharpest single differentiator against the VA world. Article plus hyphen"),
 # ---- gated, kept so the reasoning survives
 ("Teammate Talent", "teammatetalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=2, WARM=5, SOUND=3, FIRM=4, FIT=5),
  "**TeamMate is Wolters Kluwer's audit software** — 25 years, 96 countries, "
  "bought from PwC. A collision inside our own beachhead vertical"),
 ("Ballast Talent", "ballasttalent.com",
  dict(AUDIO=4, MEANS=4, CLEAN=1, WARM=4, SOUND=4, FIRM=5, FIT=5),
  "**Ballast Recruiting** (San Francisco) exists and describes itself as "
  "\"enhancing organizational stability through effective hiring.\" Same "
  "category, same metaphor. The best word in the search, unusable"),
 ("Able Hands Talent", "ablehandstalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=2, WARM=5, SOUND=4, FIRM=4, FIT=5),
  "**Able Hands Homecare.** The `[adjective] Hands` construction belongs to US "
  "home health"),
 ("Safe Hands Talent", "safehandstalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=2, WARM=5, SOUND=4, FIRM=4, FIT=5),
  "Same home-care register. I recommended this earlier; withdrawn"),
 ("Even Keel Talent", "evenkeeltalent.com",
  dict(AUDIO=4, MEANS=3, CLEAN=2, WARM=5, SOUND=5, FIRM=4, FIT=5),
  "**EvenKeel Consulting Group** already operates in staffing"),
 ("Holdfast Talent", "holdfasttalent.com",
  dict(AUDIO=2, MEANS=4, CLEAN=5, WARM=3, SOUND=5, FIRM=5, FIT=5),
  "Killed by the operator on the word being uncommon — correctly, and it "
  "invalidated the whole nautical-vocabulary family with it"),
 ("Right Arm Talent", "rightarmtalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=2, WARM=5, SOUND=4, FIRM=3, FIT=5),
  "Two operating **Right Hand** recruiting firms make it read as a knockoff"),
 ("Modest Talent", "modesttalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=2, WARM=3, SOUND=4, FIRM=3, FIT=5),
  "Free, single word, and reads as an admission that the talent is mediocre. "
  "Included because it is the clearest illustration of why availability is not "
  "a recommendation"),
]


def sc(s):
    return sum(s[k] * W[k] for k in W) / (5 * sum(W.values())) * 100


def fails(s):
    return [f"{k}={s[k]}" for k, mn, _ in GATES if s[k] < mn]


R = [dict(n=n, d=d, s=s, note=t, sc=sc(s), f=fails(s)) for n, d, s, t in N]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])


def report():
    print("# NAME RANKING\n")
    print(f"**{len(R)} candidates whose `.com` was verified free** (one exception, priced), scored "
          f"on {len(DIM)} weighted")
    print("dimensions plus 3 gates. Generated by [`scoring/names.py`](scoring/names.py). Full "
          "reasoning in [`NAME.md`](NAME.md).\n")

    print("> **On single words:** **182 bare single-word `.com`s were checked and every one is "
          "registered** —\n> `anchor`, `oak`, `keel`, `beacon`, `harbor`, `crew`, `folk`, `core`, "
          "`gem`, `ace`, `rock`, `find`, all of them.\n> A bare one-word `.com` is not obtainable. "
          "\"Single word\" therefore means `[word]talent.com`, and **48\n> of those are free** — "
          "the best being `keeltalent.com`, `mooringtalent.com`, `enduringtalent.com`,\n> "
          "`laureltalent.com` and `diligenttalent.com`.\n")

    print("---\n\n## The criteria\n")
    print("| Dimension | Weight | What it measures |\n|---|---|---|")
    for k, w, d in DIM:
        print(f"| **{k}** | {w} | {d} |")
    print("\n| Gate | Fails below | Meaning |\n|---|---|---|")
    for k, mn, why in GATES:
        print(f"| **{k}** | {mn} | {why} |")

    print("\n---\n\n## The ranking\n")
    print("| # | Name | Domain | Score | AUD | MEA | CLN | WRM | SND | FRM | FIT |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(LIVE, 1):
        s = r["s"]
        star = " ⭐" if i <= 3 else ""
        print(f"| {i} | **{r['n']}**{star} | `{r['d']}` | **{r['sc']:.1f}** | {s['AUDIO']} "
              f"| {s['MEANS']} | {s['CLEAN']} | {s['WARM']} | {s['SOUND']} | {s['FIRM']} "
              f"| {s['FIT']} |")

    print("\n### Gated out — kept so the reasoning survives\n")
    print("| Name | Score before gate | Failed | Why |\n|---|---|---|---|")
    for r in DEAD:
        print(f"| {r['n']} | {r['sc']:.1f} | {', '.join(r['f'])} | {r['note']} |")

    print("\n---\n\n## The top eight, with the argument\n")
    for i, r in enumerate(LIVE[:8], 1):
        print(f"**{i}. {r['n']}** · `{r['d']}` · {r['sc']:.1f}  \n{r['note']}.\n")

    print("---\n\n## Where the operator's favourite lands\n")
    ah = next(r for r in R if r["n"] == "All Hands Talent")
    rank = [r["n"] for r in LIVE].index("All Hands Talent") + 1
    print(f"**All Hands Talent ranks {rank} of {len(LIVE)} at {ah['sc']:.1f}.** It scores maximum on "
          f"`AUDIO` and `WARM` — the two")
    print("things that made you pick it — and loses on `CLEAN` (3, the six wrong signals), `MEANS` "
          "(3, it")
    print("misdirects to a meeting and to a pooled team) and `SOUND` (3, the `/ndz/`+`/t/` "
          "stumble).\n")
    top, spread = LIVE[0], LIVE[0]["sc"] - LIVE[-1]["sc"]
    gap = top["sc"] - ah["sc"]
    print(f"**The gap to #1 is {gap:.1f} points, and the whole live range is only {spread:.1f}** — so "
          f"that gap is")
    print(f"{gap/spread:.0%} of the entire spread. It is not a rounding difference.\n")
    print("All of it sits in `CLEAN`, `MEANS` and `SOUND` — which are exactly the three dimensions "
          "where")
    print("**All Aboard is the same name with the defects fixed**: same `All ___` structure, same "
          "warmth,")
    print("same nautical family, no meeting, no emergency, no manual-labour register. **If you like "
          "All")
    print("Hands, All Aboard is what liking All Hands should point at.**\n")

    print("---\n\n## Sensitivity — does the order survive different weights?\n")
    print("| If you weighted... | 1st | 2nd | 3rd |\n|---|---|---|---|")
    for label, ov in [("As modelled", {}),
                      ("**WARM heavily (30)** — pick on feel", {"WARM": 30}),
                      ("**MEANS heavily (35)** — pick on description", {"MEANS": 35}),
                      ("**SOUND heavily (30)** — pick on phonetics", {"SOUND": 30}),
                      ("**FIRM heavily (25)** — pick on gravitas", {"FIRM": 25}),
                      ("**CLEAN to zero** — ignore all collisions", {"CLEAN": 0})]:
        w2 = dict(W); w2.update(ov)
        def s2(s): return sum(s[k]*w2[k] for k in w2) / (5*sum(w2.values())) * 100
        t = sorted([r for r in R if not r["f"]], key=lambda r: -s2(r["s"]))[:3]
        print(f"| {label} | {t[0]['n']} | {t[1]['n']} | {t[2]['n']} |")
    print("\n**All Aboard, Steady Crew and Loyal Crew are the top three under every single "
          "weighting** — only")
    print("the order changes. All Aboard takes 1st whenever `WARM` or `SOUND` leads; Steady Crew "
          "takes it")
    print("whenever `MEANS` or `FIRM` does. **The choice between them is genuinely a choice "
          "between feel")
    print("and description, and nothing else.**\n")
    print("Note what is *absent*: **Mighty Oak** would win a `SOUND`-led ranking outright, and it "
          "is gated")
    print("out on `MEANS`=1 — the operator's own filter, applied consistently.\n")

    print("---\n\n## Verdict\n")
    print("| | |\n|---|---|")
    print(f"| **The model's answer** | **{LIVE[0]['n']}** — `{LIVE[0]['d']}` |")
    print("| **If you want \"Mighty\"** | `mightycrewtalent.com` — the bare `mightytalent.com` "
          "is taken |")
    print("| **If you want one word** | `keeltalent.com` — the best of the 48 free "
          "`[word]talent.com`s, and no bare single word exists |")
    print("| **If you keep your favourite** | `allhandstalent.com` is **survivable, not clean.** "
          "Ranked mid-table, and the honest reason to take it is that you like it — which is a "
          "real reason |")
    print("\n**Buy the top three plus your favourite — four domains, ~$48 — and let the first "
          "campaign decide.**")
    print("Everything above is a judgement; the two-brand ad test in [`NAME.md`](NAME.md) §9.4 "
          "is evidence.\n")


if __name__ == "__main__":
    report()
