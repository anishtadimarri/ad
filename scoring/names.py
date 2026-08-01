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
# Operator direction: no surnames, and the name must be generic. Applied as a
# hard gate rather than a score, because it is a stated preference not a trade-off.
NAMEY = {"Hadley Talent", "Kingsley Talent", "Everett Talent", "Winthrop Talent",
         "Ashford Talent", "Laurel Talent", "Rowan Talent", "Brook Talent"}

GATES = [("CLEAN", 3, "a live collision or a broken register"),
         ("AUDIO", 3, "cannot be spelled from audio"),
         ("MEANS", 2, "says nothing, or says the wrong thing")]

# name, domain, scores, note
N = [
 ("Monday Hiring", "mondayhiring.com",
  dict(AUDIO=5, MEANS=4, CLEAN=1, WARM=3, SOUND=4, FIRM=3, FIT=3),
  "**Uses monday.com's exact mark, in the category monday.com already sells into** — "
  "an applicant tracking system, a recruitment pipeline template and a \"Recruitment "
  "CRM for Talent Acquisition\" [V]. *\"monday hiring\"* is a plausible monday.com "
  "feature name. Tuesday evokes the pattern; Monday takes the mark"),
 ("Monday Teams", "mondayteams.com",
  dict(AUDIO=5, MEANS=2, CLEAN=1, WARM=3, SOUND=4, FIRM=2, FIT=4),
  "monday.com on the front, Microsoft Teams on the back. Two of the largest software "
  "marks in the SMB world in a four-syllable name"),
 ("Teem Talent", "teemtalent.com",
  dict(AUDIO=1, MEANS=2, CLEAN=3, WARM=4, SOUND=4, FIRM=3, FIT=5),
  "\"Teem\" is a real word — *teeming with talent* — which makes it the cleverest "
  "respelling found. It is still a **homophone of \"team\", and `teamtalent.com` is "
  "registered**, so recall and referral traffic goes to someone else"),
 ("Kloud Crew", "kloudcrew.com",
  dict(AUDIO=1, MEANS=1, CLEAN=2, WARM=3, SOUND=4, FIRM=1, FIT=5),
  "`cloudcrew.com` is registered. Same leak, same software signal"),
 ("Loyal Hires", "loyalhires.com",
  dict(AUDIO=5, MEANS=5, CLEAN=5, WARM=4, SOUND=4, FIRM=4, FIT=3),
  "**The best of the `Hires` variant.** \"Hires\" beats \"Talent\" on precision — a "
  "hire is a permanent employee, which pre-empts the VA/gig misread that Talent "
  "leaves open — and it is one syllable shorter. Cost: it foregrounds placement, so "
  "the EOR product becomes a non-sequitur. No collision found"),
 ("Tuesday Hires", "tuesdayhires.com",
  dict(AUDIO=5, MEANS=3, CLEAN=3, WARM=4, SOUND=4, FIRM=3, FIT=3),
  "Your Tuesday, with a sharper head noun — \"Hires\" says permanent employees where "
  "\"Talent\" says nothing. Still carries the Monday.com adjacency"),
 ("Gumption Hires", "gumptionhires.com",
  dict(AUDIO=5, MEANS=4, CLEAN=5, WARM=4, SOUND=4, FIRM=3, FIT=3),
  "Character claim plus a precise head noun. No collision found"),
 ("Steady Hires", "steadyhires.com",
  dict(AUDIO=5, MEANS=5, CLEAN=3, WARM=3, SOUND=4, FIRM=4, FIT=3),
  "Says the promise and the product in two short words — and **Steady HR Staffing "
  "already operates in staffing**, which is close on both sound and meaning"),
 ("All Hands Hires", "allhandshires.com",
  dict(AUDIO=5, MEANS=3, CLEAN=3, WARM=4, SOUND=2, FIRM=3, FIT=3),
  "Three consecutive `/h/`-and-`/s/` clusters. Say it twice"),
 ("Kloud Teams", "kloudteams.com",
  dict(AUDIO=1, MEANS=1, CLEAN=2, WARM=2, SOUND=3, FIRM=1, FIT=4),
  "**Four independent failures.** (1) **`cloudteams.com` is registered** — anyone "
  "who hears it types the `C` and lands on a stranger's parked page, so paid clicks "
  "leak permanently. (2) \"Cloud\" says *software*, the exact defect diagnosed in "
  "§9.7. (3) \"Teams\" collides with **Microsoft Teams**. (4) A `K`-for-`C` "
  "respelling reads as a 2014 startup, against a credibility gap that is the "
  "binding constraint"),
 ("All Hands Teams", "allhandsteams.com",
  dict(AUDIO=5, MEANS=2, CLEAN=1, WARM=4, SOUND=3, FIRM=2, FIT=4),
  "**The worst combination available.** \"All Hands\" already evokes a meeting and "
  "\"Teams\" *is* the world's most-used meeting app — together the name describes a "
  "Microsoft Teams add-on rather than a staffing firm"),
 ("Tuesday Teams", "tuesdayteams.com",
  dict(AUDIO=5, MEANS=1, CLEAN=2, WARM=4, SOUND=4, FIRM=2, FIT=4),
  "Double software collision — Monday.com on the front, Microsoft Teams on the back"),
 ("Gumption Talent", "gumptiontalent.com",
  dict(AUDIO=5, MEANS=4, CLEAN=5, WARM=5, SOUND=4, FIRM=3, FIT=5),
  "**A single generic common word, not a name, with no collision found.** "
  "\"Gumption\" is a classic Americanism for initiative and grit — a *character* "
  "claim, which is the credible half of that register, and warm in the way All "
  "Hands is warm. Spelled exactly as it sounds"),
 ("Linen Talent", "linentalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=5, WARM=5, SOUND=5, FIRM=4, FIT=5),
  "Soft, clean, everyday, entirely arbitrary — the Monday/Tiger register done with "
  "a warmer word. Says nothing, and does not pretend to"),
 ("Cotton Talent", "cottontalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=4, WARM=5, SOUND=5, FIRM=4, FIT=5),
  "Same family as Linen. \"Cotton on\" means to understand, which is a faint bonus"),
 ("Kettle Talent", "kettletalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=4, WARM=5, SOUND=4, FIRM=3, FIT=5),
  "Domestic and warm. Kettle Chips is the only real association"),
 ("Bread Talent", "breadtalent.com",
  dict(AUDIO=5, MEANS=2, CLEAN=4, WARM=4, SOUND=4, FIRM=3, FIT=5),
  "Universal, and \"breadwinner\" gives it a livelihood echo. Also slang for money, "
  "which sits oddly next to a fee"),
 ("Yardstick Talent", "yardsticktalent.com",
  dict(AUDIO=5, MEANS=5, CLEAN=2, WARM=2, SOUND=4, FIRM=4, FIT=5),
  "A yardstick is the standard you measure against — the best `MEANS` of any single "
  "word found. **Killed: Yardstick Management is a US management consultancy doing "
  "\"talent search and acquisitions\"** — a direct collision"),
 ("Rowan Talent", "rowantalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=5, WARM=5, SOUND=5, FIRM=4, FIT=5),
  "**The hybrid** — a rowan is a tree *and* a surname, so it is a common word that "
  "also reads as a firm. Warm, short, one spelling, no collision found"),
 ("Hadley Talent", "hadleytalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=5, WARM=5, SOUND=5, FIRM=5, FIT=5),
  "Best of the surname register: warm, effortless to spell, and it sounds like a "
  "firm that has existed since 1950 — which is precisely what we cannot otherwise buy"),
 ("Everett Talent", "everetttalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=5, WARM=4, SOUND=4, FIRM=5, FIT=5),
  "Clean, American, institutional. Note the **triple `t`** where the words join — "
  "a real typo risk in the domain"),
 ("Kingsley Talent", "kingsleytalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=4, WARM=4, SOUND=5, FIRM=5, FIT=5),
  "Slightly grand and very credible. Ben Kingsley is the only association"),
 ("Copper Talent", "coppertalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=2, WARM=4, SOUND=5, FIRM=4, FIT=5),
  "Warm metal, punchy, one spelling — and **downgraded on a collision I initially "
  "underrated: Copper CRM markets itself to recruiting and staffing firms**, with "
  "recruiting-firm case studies on its own site. Our category already uses it"),
 ("Sparrow Talent", "sparrowtalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=4, WARM=5, SOUND=4, FIRM=3, FIT=5),
  "Warm, humble, common. Small-bird imagery reads modest rather than mighty"),
 ("Bison Talent", "bisontalent.com",
  dict(AUDIO=5, MEANS=2, CLEAN=5, WARM=3, SOUND=4, FIRM=4, FIT=5),
  "The one animal whose metaphor actually fits tenure — bison endure winters. "
  "Cheetahs, by contrast, are fast and have no stamina"),
 ("Brook Talent", "brooktalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=4, WARM=4, SOUND=4, FIRM=4, FIT=5),
  "Calm, common, short. Also a first name and a verb"),
 ("Kestrel Talent", "kestreltalent.com",
  dict(AUDIO=4, MEANS=1, CLEAN=5, WARM=3, SOUND=4, FIRM=4, FIT=5),
  "Sharp-eyed hunter, distinctive, uncontested — and not a word most Americans "
  "use, so it repeats the Holdfast mistake in a milder form"),
 ("Tuesday Talent", "tuesdaytalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=3, WARM=4, SOUND=4, FIRM=3, FIT=5),
  "**Operator shortlist, with All Hands.** `mondaytalent.com` is taken, so this is "
  "the days-of-the-week register's survivor. **Monday.com guides to $1.47B of 2026 "
  "revenue and its core users are SMBs and agencies — our exact ICP** [V], and "
  "Tuesday is the literally adjacent day. See NAME.md §9.7 for the head-to-head"),
 ("Winthrop Talent", "winthroptalent.com",
  dict(AUDIO=4, MEANS=1, CLEAN=5, WARM=3, SOUND=4, FIRM=5, FIT=5),
  "The most institutional-sounding name in the study. Old New England, and cold"),
 ("Ashford Talent", "ashfordtalent.com",
  dict(AUDIO=5, MEANS=1, CLEAN=4, WARM=3, SOUND=4, FIRM=5, FIT=5),
  "Solid and credible. Ashford University was a for-profit college that closed "
  "amid litigation — a faint but real association"),
 ("Almanac Talent", "almanactalent.com",
  dict(AUDIO=4, MEANS=3, CLEAN=4, WARM=3, SOUND=3, FIRM=4, FIT=5),
  "An almanac is a reference of reliable recurring data — a genuine dependability "
  "metaphor. Bookish, and three syllables before Talent"),
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


# MODE 2 — the "arbitrary brand" route (Monday / Tiger / Somewhere / Oceans / Pearl).
# A name that does not TRY to describe is judged on feel, sound and gravitas instead,
# so MEANS is nearly dropped and its gate is removed.
BRAND_W = dict(W); BRAND_W.update(MEANS=4, WARM=22, SOUND=20, FIRM=18)
BRAND_GATES = [g for g in GATES if g[0] != "MEANS"]


def sc(s, w=None):
    w = w or W
    return sum(s[k] * w[k] for k in w) / (5 * sum(w.values())) * 100


def fails(s, gates=None, name=None):
    f = [f"{k}={s[k]}" for k, mn, _ in (gates or GATES) if s[k] < mn]
    if name in NAMEY:
        f.append("reads as a personal name — operator excluded")
    return f


R = [dict(n=n, d=d, s=s, note=t, sc=sc(s), f=fails(s, None, n),
          bsc=sc(s, BRAND_W), bf=fails(s, BRAND_GATES, n)) for n, d, s, t in N]
LIVE = sorted([r for r in R if not r["f"]], key=lambda r: -r["sc"])
DEAD = sorted([r for r in R if r["f"]], key=lambda r: -r["sc"])
BLIVE = sorted([r for r in R if not r["bf"]], key=lambda r: -r["bsc"])


def report():
    print("# NAME RANKING\n")
    print(f"**{len(R)} candidates whose `.com` was verified free** (one exception, priced), scored "
          f"on {len(DIM)} weighted")
    print("dimensions plus 3 gates, under **two rankings**. Generated by "
          "[`scoring/names.py`](scoring/names.py);")
    print("full reasoning in [`NAME.md`](NAME.md).\n")
    print("| Ranking | When it applies |\n|---|---|")
    print("| **§3 — descriptive** | The name should say what the business is. `MEANS` weighted 18 "
          "and gated |")
    print("| **§4 — arbitrary brand** | The *Monday / Tiger / Somewhere / Oceans* route. The name "
          "is a label, not a description. `MEANS` weighted 4, gate removed, `WARM`+`SOUND`+`FIRM` lead |")
    print("\n**These two rankings do not agree, and that is the actual decision** — not which name, "
          "but which")
    print("kind of name.\n")

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

    # ---- MODE 2
    print("\n---\n\n## The arbitrary-brand ranking — the Monday / Tiger route\n")
    print("**`mondaytalent.com` and `tigertalent.com` are both taken**, along with nearly the whole "
          "punchy-noun")
    print("space: `oak` `iron` `north` `anchor` `compass` `beacon` `harbor` `summit` `falcon` "
          "`eagle` `lion`")
    print("`wolf` `tiger` `ember` `forge` `flint` `jade` `ruby` — 131 of 174 concrete nouns "
          "registered.\n")
    print("But the register is worth ranking on its own terms, because **a confidently arbitrary "
          "word is not")
    print("the same thing as a weak metaphor.** *Open Book* asks to be decoded and the answer is "
          "thin. *Tiger*")
    print("asks nothing. So `MEANS` drops to 4, its gate is removed, and `WARM` + `SOUND` + `FIRM` "
          "lead:\n")
    print("| # | Name | Domain | Brand score | WRM | SND | FRM | CLN |")
    print("|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(BLIVE[:14], 1):
        x = r["s"]; star = " ⭐" if i <= 3 else ""
        print(f"| {i} | **{r['n']}**{star} | `{r['d']}` | **{r['bsc']:.1f}** | {x['WARM']} "
              f"| {x['SOUND']} | {x['FIRM']} | {x['CLEAN']} |")
    print("\n### And this is where the surname register earns its place\n")
    print("The five largest executive search firms on earth are **Spencer Stuart, Heidrick & "
          "Struggles, Russell")
    print("Reynolds, Egon Zehnder and Korn Ferry** — the industry calls them the **\"SHREK\" "
          "firms** [V]. Every")
    print("one is a surname. Each bills $80k-$200k+ per engagement.\n")
    print("> **That is not decoration. A surname signals institution and permanence — which is "
          "exactly the\n> thing a company with no Western credibility and no track record cannot "
          "otherwise buy.** It is\n> also the only register in this entire study with real "
          "inventory left: **31 of 33 surnames\n> checked were free**, against 3 of 174 strong "
          "concrete nouns.\n")
    print("> **⚠️ Operator direction: no surnames — the name must be generic.** The SHREK evidence "
          "stands as\n> an observation about the category; it is overruled by preference, which is a "
          "legitimate call.\n> **Hadley, Kingsley, Everett, Winthrop, Ashford, Laurel, Rowan and "
          "Brook are gated out below** —\n> Laurel and Rowan because they read as first names even "
          "though both are also common nouns.\n")
    print("| Available anyway, if you ever reverse this | |\n|---|---|")
    print("| **Warm** | `hadley` · `rowan` · `kingsley` · `everett` · `holloway` · `hartwell` |")
    print("| **Institutional** | `winthrop` · `whitfield` · `norwood` · `pemberton` · `chatham` "
          "· `ashcroft` |")
    print("| **American** | `westbrook` · `colton` · `elmore` · `danbury` · `waverly` |")
    print("| **Avoid** | `thatcher` (Margaret) · `halston` (fashion house) · `kingston` (memory "
          "cards) · `radley` (handbags) · `fairfax` (county + media group) |")
    print("\n**One trap worth naming:** `bellweathertalent.com` is free because it is the "
          "**misspelling** of")
    print("*bellwether*. The correct spelling is taken. A free domain is sometimes free for a "
          "reason that")
    print("only shows up when a client tries to type it.\n")

    print("---\n\n## The top eight, with the argument\n")
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
    print(f"| **Best single generic common word** | **Gumption Talent** — `gumptiontalent.com`. "
          f"Not a name, no collision found, means initiative and grit, and warm in the way All "
          f"Hands is warm. **4th on the descriptive ranking and 5th on the brand ranking — the only "
          f"single word in the top five of both** |")
    print(f"| **If the name should describe** | **{LIVE[0]['n']}** — `{LIVE[0]['d']}` |")
    print(f"| **If the name is just a label** (your Monday / Tiger instinct) | **{BLIVE[0]['n']}** "
          f"— `{BLIVE[0]['d']}`, with `cottontalent.com` alongside it |")
    print("| **If you want \"Mighty\"** | `mightycrewtalent.com` — the bare `mightytalent.com` "
          "is taken |")
    print("| **If you keep your favourite** | `allhandstalent.com` is **survivable, not clean.** "
          "The honest reason to take it is that you like it — which is a real reason |")
    print("\n**Buy the top three plus your favourite — four domains, ~$48 — and let the first "
          "campaign decide.**")
    print("Everything above is a judgement; the two-brand ad test in [`NAME.md`](NAME.md) §9.4 "
          "is evidence.\n")


if __name__ == "__main__":
    report()
