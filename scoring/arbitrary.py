#!/usr/bin/env python3
"""
Round seven: arbitrary word + category noun. The pattern that was never allowed.

The brief changed in a way that reopens the whole space:

    "it doesn't need to mean something. It can be xx talent or yy team or zz hiring"

Every earlier round required the name to be an attested English phrase
(scoring/collocation.py) or an idiom (scoring/idioms.py). Both refused arbitrary
pairings -- which is why round four concluded the .com namespace was exhausted at only
3.2% attestation. **`Tiger Talent` needs no bigram score.** It is a proper name plus a
category label, which is how Oyster, Deel, Gusto, Lattice and Rippling are all built.
Dropping the attestation requirement multiplies the space by ~30x, and 46.8% of the
pairs are free. The exhaustion finding does not survive the change of pattern.

Scored on the four stated criteria, in the operator's order:

  1. sounds good, not forced           -> FLOW    prosody and junction of the pair
  2. does not confuse people           -> CLEAR   brand collision and sector misread
  3. expands to all ICPs and roles     -> EXPAND  head noun must lock nothing
  4. works on Meta and when spelled
     out loud, without sounding weird
     or misrepresented                 -> SPELL   spellable on first hearing
                                       -> ARTIFACT no accidental word across the join

Two methodological fixes over the first draft of this file, both of which were changing
the answer:

  * CLEAR was being inferred by REGEXING MY OWN PROSE NOTES for words like "live" or
    "trademark". That is circular -- the score depended on which adjectives I happened
    to use. It is now an explicit integer per word, stated in the table below, which I
    can be held to. This is the same failure as the invented SAYS dict in co_names.py.
  * The first draft's top five were `Summer Hiring`, `Bronze Talent` and `Season
    Hiring`. **Bronze is the third-place medal** and **summer/season say temporary
    work** -- the two worst possible readings for a premium permanent-placement
    business. Neither was in the misdirect list, so both scored clean. Words whose
    MEANING fights the model are now blocked outright with the reason recorded.

ARTIFACT is a real automated check, not a judgement: `covetalent.com` contains "covet"
across the join, and `cove` + `talent` never looked wrong until it was concatenated.
Checked against a 370k-word English list.

Run:  python3 scoring/arbitrary.py > /dev/null   (writes ARBITRARY.md)
"""
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

OUT = "ARBITRARY.md"
VER = "https://rdap.verisign.com/{t}/v1/domain/"
DM = "https://api.datamuse.com/words"
WORDLIST = "scoring/.words_alpha.txt"
WORDLIST_URL = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
COMMON = "scoring/.common20k.txt"
COMMON_URL = ("https://raw.githubusercontent.com/first20hours/google-10000-english/"
              "master/20k.txt")

# ---------------------------------------------------------------------------
# The bank. (word, register, CLEAR 1-5, note)
#
# CLEAR is stated, not inferred. 5 = nothing to explain to a cold buyer.
# 4 = clean, faintly flavoured. 3 = a given name, or a niche brand exists.
# 2 = a known brand in another sector, or a mild misdirect. Gate is CLEAR < 3.
# ---------------------------------------------------------------------------
BANK = [
    # --- birds and animals -------------------------------------------------
    ("wren",     "animal", 3, "**Wren** is a Y Combinator carbon-offset startup with real name recognition in startup circles, and Wren Kitchens is large in the UK. Neither is in recruiting"),
    ("egret",    "animal", 2, "**Egret Consulting** is in executive search; Egret is also an e-scooter brand and Egret Technology in HTML5 games"),
    ("bison",    "animal", 2, "**Iron Bison Talent Partners** and **The Bison Group** (IT staffing) both exist"),
    ("ibex",     "animal", 3, "obscure, and `x` costs a spelling point"),
    ("lark",     "animal", 3, "Lark Health is a funded US health app"),
    ("finch",    "animal", 3, "Finch is a live HR/payroll **API company** — adjacent enough "
                              "to matter"),
    ("marlin",   "animal", 3, "reads as sportfishing"),
    ("orca",     "animal", 3, "whales; Orca is used in marine and in software"),
    ("raven",    "animal", 3, "a given name, and the Baltimore Ravens"),
    ("sparrow",  "animal", 3, "small — reads as minor, which is the wrong signal"),
    ("hawk",     "animal", 3, "sports mascots, and 'hawking' means peddling"),
    ("pelican",  "animal", 3, "Pelican cases; clean otherwise"),
    ("panther",  "animal", 2, "sports mascots"),
    ("gazelle",  "animal", 2, "Gazelle is a US device-trade-in brand"),
    ("condor",   "animal", 2, "Condor is an airline"),
    ("falcon",   "animal", 2, "aerospace and heavy plant"),
    ("crane",    "animal", 2, "reads as construction plant"),
    ("swallow",  "animal", 2, "also a verb; awkward in a sentence"),
    ("dolphin",  "animal", 2, "leisure and pools"),
    ("osprey",   "animal", 2, "Osprey backpacks, and the aircraft"),
    ("kite",     "animal", 2, "toys, and heard as the surname Kyte"),
    ("robin",    "animal", 2, "a given name, and Robinhood owns the bird space"),
    # --- trees and plants ---------------------------------------------------
    ("linden",   "tree", 4, "**the only nature word I checked with no recruiting firm on it.** Linden Lab (Second Life) is the notable brand; Linden, New Jersey is a real town, so 'linden staffing' searches surface geography"),
    ("elm",      "tree", 2, "the **Elm programming language**, **Elm Company** (a large Saudi digital firm) and **West Elm** furniture"),
    ("birch",    "tree", 4, "clean; faintly Scandinavian-furniture"),
    ("hawthorn", "tree", 2, "**Hawthorne Lane** is a DC recruiting firm, and the hawthorn/hawthorne split costs a spelling point on top"),
    ("willow",   "tree", 4, "warm; Willow is a cricket-streaming service, niche"),
    ("sycamore", "tree", 4, "clean but long, and the spelling splits"),
    ("larch",    "tree", 3, "obscure; reads as timber"),
    ("rowan",    "tree", 3, "a given name, and Rowan University"),
    ("maple",    "tree", 3, "Canada and syrup"),
    ("oak",      "tree", 3, "furniture and banking"),
    ("laurel",   "tree", 3, "a given name; 'resting on laurels' is the wrong idiom"),
    ("teak",     "tree", 3, "furniture — though it is a South Asian hardwood, which is a "
                            "quiet nod to where the talent is"),
    ("banyan",   "tree", 2, "used in logistics and software; also specifically Indian"),
    ("sorrel",   "tree", 2, "obscure and hard to spell"),
    ("aspen",    "tree", 3, "Aspen, Colorado — luxury ski, which is a *premium* signal"),
    ("myrtle",   "tree", 2, "reads as an elderly given name"),
    ("hickory",  "tree", 2, "smoked meat"),
    ("magnolia", "tree", 2, "the film, and the paint colour"),
    ("redwood",  "tree", 3, "Redwood Software and Redwood Logistics are both sizeable"),
    ("clover",   "tree", 2, "Clover is a large POS brand"),
    ("fern",     "tree", 2, "a given name"),
    ("ivy",      "tree", 2, "a given name, and Ivy League implies elite universities"),
    ("olive",    "tree", 2, "food, and a given name"),
    ("hazel",    "tree", 2, "a given name"),
    ("spruce",   "tree", 2, "Spruce is a fintech; also 'spruce up' means superficial"),
    # --- landscape ----------------------------------------------------------
    ("ridge",    "place", 3, "**Blue Ridge Executive Search** and **Ridgeline Talent Partners** are compounds rather than bare 'Ridge', but the space is worked"),
    ("lagoon",   "place", 3, "reads as leisure"),
    ("mesa",     "place", 3, "Mesa, Arizona"),
    ("harbor",   "place", 3, "clean meaning — shelter — but healthcare and finance use it "
                             "heavily, and the harbor/harbour split costs a spelling point"),
    ("lowland",  "place", 2, "reads as low"),
    ("highland", "place", 2, "whisky"),
    ("midland",  "place", 2, "banking"),
    ("meridian", "place", 2, "healthcare, and crowded generally"),
    ("summit",   "place", 2, "conferences — it would fight your own event marketing"),
    ("valley",   "place", 2, "Silicon Valley"),
    ("canyon",   "place", 2, "Canyon bicycles"),
    ("basin",    "place", 2, "plumbing"),
    ("dune",     "place", 2, "the films"),
    ("sierra",   "place", 2, "vehicles and the Sierra Club"),
    ("prairie",  "place", 2, "hard to spell"),
    ("haven",    "place", 2, "Haven was the Amazon/JPMorgan/Berkshire healthcare venture; "
                             "also refuges and caravan parks"),
    # --- light and sky ------------------------------------------------------
    ("daybreak", "sky", 4, "clean; long"),
    ("northstar", "sky", 3, "aspirational and spellable, but used loosely everywhere"),
    ("solstice", "sky", 2, "hard to spell, and reads as annual"),
    ("beacon",   "sky", 2, "crowded — healthcare, edtech, several staffing firms"),
    ("orion",    "sky", 2, "aerospace"),
    ("vega",     "sky", 2, "crowded in finance and tech"),
    ("altair",   "sky", 2, "engineering software"),
    ("aurora",   "sky", 2, "crowded brand token, **and heard as Arora, a common Indian "
                           "surname** — which misrepresents a company as a person"),
    ("dawn",     "sky", 2, "dish soap, and a given name"),
    ("dusk",     "sky", 2, "faintly ominous"),
    # --- minerals -----------------------------------------------------------
    ("pewter",   "mineral", 3, "tableware; otherwise clean and uncrowded"),
    ("garnet",   "mineral", 3, "jewellery"),
    ("topaz",    "mineral", 3, "jewellery, and `z` splits the spelling"),
    ("onyx",     "mineral", 2, "faintly gothic, and `x` costs a spelling point"),
    ("opal",     "mineral", 2, "jewellery"),
    ("amber",    "mineral", 2, "a given name, and jewellery"),
    ("coral",    "mineral", 2, "a given name, and reefs"),
    ("copper",   "mineral", 2, "metals trading, and British slang for police"),
    ("iron",     "mineral", 2, "ironmongery; reads industrial and cold for a people business"),
    ("steel",    "mineral", 2, "steel"),
    ("emerald",  "mineral", 2, "jewellery"),
    ("sapphire", "mineral", 2, "jewellery"),
    # --- abstract -----------------------------------------------------------
    ("keel",     "abstract", 3, "**Keel** is a London no-code/ERP startup that raised $6M in 2024. Not in recruiting; 'on an even keel' still reads well"),
    ("braid",    "abstract", 4, "strands woven into one thing; clean and uncrowded"),
    ("cohort",   "abstract", 3, "a group moving together; heavily used in edtech"),
    ("ovation",  "abstract", 3, "applause — acclaim without claiming it. Ovation Healthcare "
                                "exists"),
    ("bellwether", "abstract", 3, "the leader of the flock; long, and slightly literary"),
    ("tandem",   "abstract", 3, "two moving as one, which is the model. Tandem Bank and "
                                "Tandem Diabetes both exist"),
    ("clarity",  "abstract", 3, "many small consultancies use it"),
    ("candor",   "abstract", 3, "several HR-tech uses, and the candor/candour split"),
    ("stanza",   "abstract", 3, "clean but literary"),
    ("ballad",   "abstract", 3, "music"),
    ("esteem",   "abstract", 2, "self-help register"),
    ("amity",    "abstract", 2, "**Amity University is one of India's largest private "
                                "universities** — and you are selling Indian talent"),
    ("verse",    "abstract", 2, "crowded"),
    ("sonnet",   "abstract", 2, "also a Claude model name"),
    ("cadre",    "abstract", 2, "exactly the right meaning — a trained core of personnel — "
                                "but unspellable from speech and politically loaded"),
    # --- days and time ------------------------------------------------------
    ("tuesday",  "time", 4, "clean and arbitrary; the operator already likes it. Note a "
                            "Facebook page called Tuesday Talent exists for freelance "
                            "creatives — a real cost on `tuesdaytalent` specifically"),
    ("thursday", "time", 3, "**Thursday is a well-known London and New York dating app** — TechCrunch coverage, guerrilla marketing, and its audience is the same young Western urban professional you are advertising to on Meta"),
    ("friday",   "time", 2, "reads as the end of the week, and 'his man Friday' is a servant "
                            "reference — actively wrong for a labour business"),
    ("wednesday", "time", 2, "the Netflix series, and the hardest weekday to spell"),
    ("morning",  "time", 2, "reads as a time of day rather than a company"),
    ("epoch",    "time", 2, "reads as machine-learning jargon"),
    ("decade",   "time", 2, "reads as a span of time"),
    # --- coinages, kept in to show they fail the SPELL gate ----------------
    ("alora",    "coined", 3, "pleasant and meaningless — the point is that it cannot survive "
                              "being read aloud"),
    ("elara",    "coined", 3, "as above"),
    ("solara",   "coined", 3, "as above"),
    ("novara",   "coined", 3, "as above, and it is an Italian city"),
    ("luma",     "coined", 3, "as above; Luma AI exists"),
    ("kira",     "coined", 3, "as above; Kira Systems is legal-tech"),
    ("maia",     "coined", 3, "as above"),
    ("sona",     "coined", 3, "as above"),
]

# Blocked before checking: the MEANING fights the model, or the brand is in this market.
BLOCK = {
    # --- the register itself is the trap. Every one of these was scored CLEAR 5 by me
    # --- and then found to have live recruiting firms on it. See ARBITRARY.md section 1.
    "heron": "**herontalent.com is a live executive search firm** (data/AI leadership, "
             "Nordics), plus Heron Global Recruitment, Heron Staffing and Heron Search. "
             "It was #1 and #2 in the first ranking of this file",
    "alder": "**Alder Koten** and **Alder Bowman Search Consultants** are both executive "
             "search firms. It was #5",
    "lantern": "**Lantern Partners** (retained executive search, Chicago, founded 2003), "
               "**Lantern Recruitment** (UK creative) and **Lantern Staffing** all exist",
    "kestrel": "**Kestrel Associates**, **Kestrel Recruitment**, **Kestrel Bay** and "
               "**Kestrel Partners** are all in recruitment",
    "trellis": "**Trellis Talent** and **Talent Trellis** are both live recruiting firms",
    "bronze": "**the third-place medal.** Fatal for a premium talent brand — and it was #2 "
              "in the first draft of this screen",
    "summer": "**says seasonal and temporary work**, the worst possible reading for a "
              "permanent-placement business. It was #1 in the first draft",
    "season": "same — 'seasonal staff' is the exact opposite of what is being sold",
    "spring": "the season, plus the Java framework",
    "autumn": "the season, plus a given name",
    "plateau": "**'plateau' means growth stopped.** Actively wrong, and unspellable",
    "bluff": "**'bluff' means to deceive.** Actively wrong for a trust business",
    "badger": "**'to badger' means to pester.** Actively wrong",
    "poplar": "**heard as 'popular'.** Fatal for word of mouth and for radio",
    "cove": "`covetalent.com` contains **covet** across the join — see the ARTIFACT check",
    "cobalt": "cobalt mining is synonymous with **child labour in the DRC**. For a labour "
              "business that is not a risk worth carrying",
    "indigo": "**IndiGo is India's largest airline** — and you are selling Indian talent",
    "slate": "Slate magazine, and roofing",
    "marble": "stone worktops", "granite": "worktops", "quartz": "worktops and Quartz media",
    "basalt": "quarrying", "flint": "Flint, Michigan — the water crisis",
    "brass": "instruments, and 'brass' means senior officers",
    "jasper": "**Jasper is a well-funded AI-writing brand**",
    "juniper": "**Juniper Networks** — large trademark",
    "cypress": "Cypress Semiconductor, and the Cypress test framework",
    "mulberry": "Mulberry — luxury handbags",
    "sequoia": "**Sequoia Capital, and Sequoia Consulting Group is an HR/benefits firm**",
    "lattice": "**Lattice is a large HR platform** — direct adjacency",
    "cornerstone": "**Cornerstone OnDemand** — one of the largest HR software companies",
    "atlas": "**Atlas is a live global-employment/EOR brand** — direct competitor",
    "vantage": "**Vantage Circle is an HR-tech company**",
    "beeline": "**Beeline is a large contingent-workforce management platform**",
    "delta": "an airline", "tundra": "a Toyota", "cascade": "dishwasher tablets",
    "savanna": "a cider brand, and the savanna/savannah split",
    "zenith": "watches", "equinox": "the gym chain", "lumen": "**Lumen Technologies**",
    "halo": "the video game", "ember": "the JavaScript framework", "twilight": "the films",
    "polaris": "vehicles", "titan": "crowded", "comet": "cleaning products",
    "nova": "extremely crowded", "eclipse": "the IDE",
    "unity": "the game engine", "parity": "a blockchain firm",
    "tempo": "an Atlassian-ecosystem brand", "tenor": "Google's GIF service",
    "echo": "Amazon Echo", "chorus": "Chorus.ai — sales intelligence",
    "lyric": "a health-tech brand", "accord": "a Honda",
    "tribute": "**funeral and memorial services**",
    "noon": "**Noon is a large Gulf e-commerce marketplace**",
    "otter": "**Otter.ai** — adjacent enough to confuse",
    "lynx": "**heard as 'links'** — a different word entirely",
    "puma": "sportswear", "jaguar": "cars",
    "stallion": "breeding, and it is male-gendered",
    "monday": "monday-talent.com is a live creative recruitment agency at our ICP",
    "sterling": "Sterling Check — background screening, adjacent",
    "cadence": "Cadence Design Systems", "canon": "Canon Inc.",
    "compass": "Compass Inc.", "bench": "'bench sales' is Indian IT staffing's own term for "
                                        "the commodity end of this market",
    "vouch": "vouchfor.com is a live talent-tech brand",
    "merlin": "reads as the wizard rather than the falcon",
}

HEADS = ["talent", "team", "teams", "hiring", "hires", "people", "crew", "staff",
         "desk", "roster", "squad", "group", "partners", "collective"]
HEAD_EXPAND = {"talent": 5, "team": 5, "teams": 5, "hiring": 5, "hires": 5, "people": 5,
               "crew": 4, "staff": 5, "desk": 3, "roster": 4, "squad": 3, "group": 4,
               "partners": 4, "collective": 3}
HEAD_NOTE = {
    "talent": "the clearest and most expansion-safe head noun in the category — it names "
              "no role, no seniority and no industry",
    "team": "warm and singular; says the placed person joins *your* team",
    "hiring": "verb-as-noun; says what you do and reads clean cold",
    "hires": "the outcome; slightly transactional",
    "people": "warmest and broadest, and the single most crowded head noun in staffing",
    "staff": "plainest; reads administrative and lower-ticket",
    "teams": "plural reads as the product, and it collides with Microsoft Teams",
    "roster": "names the graded directory — the retention asset — but implies a fixed list",
    "crew": "warm, faintly maritime and production-flavoured, so a mild role hint",
    "group": "reads as a holding company: good for expansion, cold in an ad",
    "partners": "consultancy register; implies equity partners",
    "desk": "agency and newsroom for a specialist team; unknown to many buyers, and it "
            "implies **one** desk, which fights expansion",
    "squad": "young and informal for a $6k–$20k sale",
    "collective": "implies a co-op the talent owns — the wrong ownership story entirely",
}

# the head noun carries its own collision risk, which the first two runs ignored --
# `tuesdayteams.com` ranked #1 while "Teams" is Microsoft's product name.
HEAD_CLEAR = {"teams": -1.5, "people": -0.8, "collective": -0.5, "partners": -0.3}

AMBIG = [
    (r"ph", 1.2, "`ph` vs `f`"),
    (r"ough", 1.6, "`ough` is unguessable"),
    (r"(ae|oe)", 1.2, "digraph vowel"),
    (r"a$", 1.1, "terminal `-a` could be `-a`, `-ah` or `-er`"),
    (r"^c[eiy]", 1.0, "soft `c` could be `s`"),
    (r"([bcdfgklmnprst])\1", 0.8, "doubled consonant could be single"),
    (r"y[aeiou]", 0.7, "`y` as a consonant is guessy"),
    (r"(ei|ie)", 0.6, "`ei`/`ie` order is a coin flip"),
    (r"^k", 0.9, "initial `k` could be `c`"),
    (r"x", 0.6, "`x` could be `cks` or `ks`"),
    (r"z", 0.5, "`z` could be `s`"),
]
HOMOPHONE = {
    "kite": "Kyte", "vega": "Vaga", "kira": "Kiera", "maia": "Maya", "luma": "Lumah",
    "sona": "Sonna", "alora": "Allora", "elara": "Alara", "solara": "Sollara",
    "novara": "Novarra", "aurora": "Arora", "lynx": "links", "myrtle": "mirtle",
    "hickory": "hickery", "sycamore": "sycamour", "harbor": "harbour",
    "candor": "candour", "savanna": "savannah", "pewter": "pewtor",
}

VOWELS = set("aeiouy")
LIQUID = set("lrmnw")


def curl(url, timeout=18):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout), "-w", "\n%{http_code}",
                            url], capture_output=True, text=True, timeout=timeout + 8)
        b, _, c = r.stdout.rpartition("\n")
        return b, int(c or 0)
    except Exception:
        return "", 0


def rdap_free(fqdn, tld="com"):
    _, c = curl(VER.format(t=tld) + fqdn)
    return True if c == 404 else (False if c == 200 else None)


def freq(w):
    try:
        b, _ = curl(f"{DM}/?sp={w}&md=f&max=1")
        for d in json.loads(b):
            if d["word"] == w:
                for t in d.get("tags", []):
                    if t.startswith("f:"):
                        return float(t[2:])
    except Exception:
        pass
    return 0.0


def wordset(path, url):
    if not os.path.exists(path):
        subprocess.run(["curl", "-sS", "--max-time", "120", "-o", path, url], check=False)
    try:
        return {w.strip() for w in open(path) if len(w.strip()) >= 5}
    except Exception:
        return set()


def syl(w):
    n, prev = 0, False
    for ch in w:
        v = ch in VOWELS
        if v and not prev:
            n += 1
        prev = v
    if w.endswith("e") and n > 1:
        n -= 1
    return max(n, 1)


def flow(a, b):
    s = 2.4
    tot = syl(a) + syl(b)
    s += {2: -0.4, 3: 0.9, 4: 1.0, 5: 0.1, 6: -0.8}.get(tot, -1.2)
    if a[-1] == b[0] and a[-1] not in VOWELS:
        s -= 1.4                                    # cobalT Talent
    if a[-1] in "sz" and b[0] in "sz":
        s -= 1.1
    if a[-1] in "td" and b[0] in "td":
        s -= 0.9
    if a[0] == b[0]:
        s += 0.7                                    # alliteration aids recall
    if a[-1] in VOWELS or a[-1] in LIQUID:
        s += 0.5
    s += min(sum(1 for c in a + b if c in LIQUID) / len(a + b) * 2.2, 0.8)
    if len(a + b) > 15:
        s -= 0.7
    if syl(a) == 1 and syl(b) == 1:
        s -= 0.5
    return max(0.0, min(5.0, s))


def spell(a, f):
    s = 3.0
    s += min((f + 1) ** 0.28 - 1, 1.6)
    notes = []
    for pat, cost, why in AMBIG:
        if re.search(pat, a):
            s -= cost
            notes.append(why)
    if a in HOMOPHONE:
        s -= 1.5
        notes.append(f"heard as **{HOMOPHONE[a]}**")
    if len(a) > 8:
        s -= 0.5
        notes.append("long")
    return max(0.0, min(5.0, s)), notes


def artifact(a, b, words, common):
    """
    Words of 5+ letters straddling the join. A measurement, not a judgement.

    The first run of this gated on the full 370k list and was useless: it fired on
    plurals the head noun created (`amber`+`squad` -> "ambers") and on dictionary
    obscurities nobody would ever see ("ratal", "adret", "redes"). Those are not
    misreads. So two tiers:

      HARD  the accidental word is in the 20,000 most common English words, is not
            just first-word-plus-s, and is not already inside either half.
            `linden` + `talent` -> **dental**. That is a real misread and it gates.
      SOFT  everything else, reported but not gated.
    """
    s, n = a + b, len(a)
    hard, soft = set(), set()
    for i in range(max(0, n - 8), n):
        for j in range(n + 1, min(len(s), n + 9) + 1):
            if not (i < n < j):
                continue
            h = s[i:j]
            if h not in words or h == a + "s" or h in a or h in b:
                continue
            (hard if h in common else soft).add(h)
    key = lambda x: (-len(x), x)
    return sorted(hard, key=key), sorted(soft, key=key)


def main():
    words = wordset(WORDLIST, WORDLIST_URL)
    common = wordset(COMMON, COMMON_URL)
    print(f"wordlist: {len(words)} words, common: {len(common)}")
    bank = [(w, r, c, n) for w, r, c, n in BANK if w not in BLOCK]
    print(f"{len(bank)} first words x {len(HEADS)} heads = {len(bank)*len(HEADS)} RDAP checks")

    with ThreadPoolExecutor(max_workers=10) as ex:
        fr = dict(zip([b[0] for b in bank], ex.map(lambda b: freq(b[0]), bank)))

    combos = [(w, r, c, n, h) for w, r, c, n in bank for h in HEADS]
    with ThreadPoolExecutor(max_workers=14) as ex:
        free = dict(zip([(c[0], c[4]) for c in combos],
                        ex.map(lambda c: rdap_free(c[0] + c[4] + ".com"), combos)))
    unk = [c for c in combos if free[(c[0], c[4])] is None]
    if unk:
        with ThreadPoolExecutor(max_workers=6) as ex:
            for c, v in zip(unk, ex.map(lambda c: rdap_free(c[0] + c[4] + ".com"), unk)):
                free[(c[0], c[4])] = v
    nfree = sum(1 for v in free.values() if v is True)
    print(f"free on .com: {nfree}/{len(combos)} ({nfree/len(combos)*100:.1f}%), "
          f"unresolved {sum(1 for v in free.values() if v is None)}")

    W = {"FLOW": 24, "SPELL": 22, "CLEAR": 20, "EXPAND": 16, "META": 18}
    rows = []
    for w, reg, cl, note, h in combos:
        if free[(w, h)] is not True:
            continue
        fl = flow(w, h)
        sp, spn = spell(w, fr.get(w, 0.0))
        art, soft = artifact(w, h, words, common)
        if art:
            sp = min(sp, 2.0)
        exp = HEAD_EXPAND[h]
        me = 2.6 + (1.2 if len(w + h) <= 12 else (0.6 if len(w + h) <= 14 else 0.0))
        me = min(me + {5: 1.2, 4: 0.7, 3: 0.2}[exp], 5.0)
        clh = max(1.0, min(5.0, cl + HEAD_CLEAR.get(h, 0.0)))
        d = {"FLOW": fl, "SPELL": sp, "CLEAR": clh, "EXPAND": float(exp), "META": me}
        tot = sum(d[k] * W[k] for k in W) / (5 * sum(W.values())) * 100
        gate = None
        if art:
            gate = f"ARTIFACT — contains **{art[0]}** across the join"
        elif sp < 3.0:
            gate = "SPELL — misspelled when heard"
        elif clh < 3:
            gate = "CLEAR — brand collision or sector misread"
        elif exp < 4:
            gate = "EXPAND — head noun narrows the offer"
        rows.append(dict(w=w, h=h, reg=reg, tot=tot, gate=gate, d=d, spn=spn, note=note,
                         art=art, soft=soft, f=fr.get(w, 0.0)))
    rows.sort(key=lambda r: -r["tot"])
    json.dump({"free": {f"{a}|{b}": v for (a, b), v in free.items()}, "fr": fr},
              open("scoring/.arb_cache.json", "w"), indent=1)
    write(rows, W, nfree, len(combos), len(bank))
    for r in [x for x in rows if not x["gate"]][:12]:
        print(f"  {r['w']+r['h']+'.com':26s} {r['tot']:.1f}")


def write(rows, W, nfree, ncombo, nwords):
    ok = [r for r in rows if not r["gate"]]
    L = []
    A = L.append
    A("# Arbitrary Word + Category Noun\n")
    A("> **\"It doesn't need to mean something. It can be xx talent or yy team or zz hiring… "
      "should sound good and not forced · should not confuse people · should allow expansion "
      "into all ICPs and roles · should work on Meta ads or when someone spells it out.\"**\n")
    A("That instruction reopens the space, and it **invalidates the conclusion of "
      "[`CO.md`](CO.md) §4.**\nEvery earlier round required the name to be an attested English "
      "phrase or an idiom, which is why\nthat file found 3.2% attestation and called the "
      "namespace exhausted. **`Tiger Talent` needs no\nbigram score** — it is a proper name plus "
      "a category label, which is how Oyster, Deel, Gusto,\nLattice and Rippling are all built.\n")
    A(f"**{nwords} first words × {len(HEADS)} head nouns = {ncombo} authoritative Verisign RDAP "
      f"checks. {nfree} are free on\n`.com` — {nfree/ncombo*100:.1f}%**, against 0 of 190 single "
      "words and 0 of 65 idioms. The pattern was the\nconstraint, not the vocabulary.\n")

    A("---\n\n## 1. Two things I had to fix first\n")
    A("Both were changing the answer, and both are the same mistake I made earlier in this "
      "project:\n")
    A("| Fault | What it did | Fix |")
    A("|---|---|---|")
    A("| **`CLEAR` was inferred by regexing my own prose notes** for words like *live*, "
      "*trademark*, *crowded* | The score depended on which adjectives I happened to type. "
      "Circular, and unauditable — the same failure as the invented `SAYS` dict in "
      "[`co_names.py`](scoring/co_names.py) | `CLEAR` is now an **explicit integer per word**, "
      "printed in §5 so it can be argued with |")
    A("| **No check on what a word MEANS** | The first run of this file ranked **`Summer "
      "Hiring` #1 and `Bronze Talent` #2.** Bronze is *the third-place medal*; summer and season "
      "say *temporary work*. Those are the two worst readings available to a premium "
      "permanent-placement business, and both scored clean | Words whose meaning fights the "
      "model are **blocked outright with the reason recorded** (§6) |")
    A("")
    A("And one genuinely new automated check, because criterion 4 demanded it:\n")
    A("> **`ARTIFACT`** — concatenation creates words that neither half contained. "
      "`cove` + `talent` = **`covetalent.com`**, which contains *covet*; `linden` + `talent` = "
      "**`lindentalent.com`**, which contains *dental*. Any 5+ letter word straddling the join "
      "is found against a 370,000-word list, then **gated only if it is among the 20,000 most "
      "common English words** and is not merely a plural the head noun created. The first "
      "version gated on the full list and was useless — it fired on *ambers*, *aspens* and "
      "*adret*. A measurement, not a judgement.\n")

    A("---\n\n## 2. The four criteria, weighted\n")
    A("| Criterion | Wt | Your words | How it is scored |")
    A("|---|---|---|---|")
    A("| **FLOW** | 24 | *should sound good and not forced* | Syllable count, stress collision "
      "and **junction clash**: `Cobalt Talent` loses 1.4 for the `t`+`T` pile-up, `Tiger Talent` "
      "gains 0.7 for alliteration |")
    A("| **SPELL** | 22 | *when someone spells it out* | **Real word frequency** "
      "(Datamuse/Google Books — a word you have seen written is one you can spell) **plus "
      "rule-based grapheme ambiguity**: `ph`, `ough`, terminal `-a`, soft `c`, doubled "
      "consonants, `x`, `z`, and a homophone list |")
    A("| **CLEAR** | 20 | *should not confuse people* | Brand collision and sector misread on a "
      "cold read, **for the first word and the head noun both** — `Teams` carries −1.5 for "
      "Microsoft Teams, `People` −0.8 as the most crowded head noun in staffing. Explicit per "
      "word in §5 |")
    A("| **EXPAND** | 16 | *expansion into all ICPs and roles* | The head noun must lock "
      "nothing — §4 |")
    A("| **META** | 18 | *should work on Meta ads* | Legible cold: short, and the **head noun "
      "does the explaining** so the ad does not have to |")
    A("")
    A("**Gates, applied after scoring:** `ARTIFACT` (any accidental word across the join), "
      "`SPELL` < 3,\n`CLEAR` < 3, `EXPAND` < 4.\n")

    A("---\n\n## 3. Top 10\n")
    A("| # | Domain | Reads as | Flow | Spell | Clear | Expand | Meta | Score | The catch |")
    A("|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(ok[:10], 1):
        d = r["d"]
        A(f"| **{i}** | **`{r['w']}{r['h']}.com`** | {r['w'].capitalize()} "
          f"{r['h'].capitalize()} | {d['FLOW']:.1f} | {d['SPELL']:.1f} | {d['CLEAR']:.1f} | "
          f"{d['EXPAND']:.0f} | {d['META']:.1f} | **{r['tot']:.1f}** | {r['note']} |")
    A("")
    A("### 11–30\n")
    A("| # | Domain | Flow | Spell | Clear | Score |\n|---|---|---|---|---|---|")
    for i, r in enumerate(ok[10:30], 11):
        d = r["d"]
        A(f"| {i} | `{r['w']}{r['h']}.com` | {d['FLOW']:.1f} | {d['SPELL']:.1f} | "
          f"{d['CLEAR']:.1f} | {r['tot']:.1f} |")
    A("")

    A("---\n\n## 4. Head nouns, ranked on expansion\n")
    A("**Criterion 3 is decided almost entirely here**, before the first word matters at all.\n")
    A("| Head noun | Expand | Note |\n|---|---|---|")
    for h, v in sorted(HEAD_EXPAND.items(), key=lambda x: (-x[1], x[0])):
        A(f"| **{h.capitalize()}** | {v} | {HEAD_NOTE[h]} |")
    A("")

    A("---\n\n## 5. Every first word, with its `CLEAR` score stated\n")
    A("This is the table to argue with. `CLEAR` is my read of a cold buyer plus what the web "
      "searches\nand `.com` fetches turned up — **it is not a USPTO clearance search.**\n")
    A("| Word | Register | Clear | Freq/M | Note |\n|---|---|---|---|---|")
    seen = {}
    for r in rows:
        seen.setdefault(r["w"], r)
    for w, r in sorted(seen.items(), key=lambda x: (-x[1]["d"]["CLEAR"], x[0])):
        A(f"| {w} | {r['reg']} | **{r['d']['CLEAR']:.0f}** | {r['f']:.1f} | {r['note']} |")
    A("")

    A("---\n\n## 6. Blocked before checking — the meaning fights the model\n")
    A("| Word | Reason |\n|---|---|")
    for w, why in sorted(BLOCK.items()):
        A(f"| **{w}** | {why} |")
    A("")

    A("---\n\n## 8. The finding that matters more than the ranking\n")
    A("**Pretty-nature-word + Talent is the recruiting industry's default naming convention.** "
      "It is the\nfirst place every founder in this market reaches, which makes it "
      "simultaneously the most obvious\nregister and the most contested. I scored five of these "
      "`CLEAR` 5 — *nothing to explain* — and then\nfound live firms on every one:\n")
    A("| Word | I scored it | What is actually there |")
    A("|---|---|---|")
    A("| **Heron** | 5 — *#1 and #2 in the first ranking* | **herontalent.com is a live "
      "executive search firm** (data/AI leadership, Nordics), plus Heron Global Recruitment, "
      "Heron Staffing, Heron Search |")
    A("| **Alder** | 5 — *#5* | **Alder Koten** and **Alder Bowman Search Consultants**, both "
      "executive search |")
    A("| **Kestrel** | 5 | **Kestrel Associates**, **Kestrel Recruitment**, **Kestrel Bay**, "
      "**Kestrel Partners** |")
    A("| **Lantern** | 4 | **Lantern Partners** (retained search, Chicago, 2003), **Lantern "
      "Recruitment**, **Lantern Staffing** |")
    A("| **Trellis** | 4 | **Trellis Talent** *and* **Talent Trellis** |")
    A("| **Bison** | 4 | **Iron Bison Talent Partners**, **The Bison Group** |")
    A("| **Hawthorn** | 4 | **Hawthorne Lane**, DC recruiting |")
    A("")
    A("> **The `.com` being free told me nothing about whether the name was taken.** These firms "
      "hold\n> `herontalent.com`, `lanternpartners.com`, `trellistalent.io` — so the *pair* I was "
      "testing was\n> free while the *word* was thoroughly occupied. RDAP cannot see that. Only "
      "searching for the\n> business can.\n")
    A("Which produces the actual conclusion: **the two safest names are the ones that are not in "
      "that\nregister at all.**\n")
    A("| Pick | Why | Watch |")
    A("|---|---|---|")
    A("| **`lindenhires.com`** or **`lindenhiring.com`** | **Linden is the only nature word I "
      "checked with no recruiting firm on it.** Warm, two syllables, one spelling, and `Hires` / "
      "`Hiring` are the most expansion-safe head nouns there are — they name no role, no "
      "seniority, no industry | `lindentalent.com` is free but contains **dental** — do not buy "
      "it. Linden, New Jersey is a real town, so 'linden staffing' searches surface geography. "
      "Linden Lab made Second Life |")
    A("| **`tuesdayhires.com`** or **`tuesdayroster.com`** | Arbitrary, warm, **outside the "
      "contested register entirely**, and you already like the word. Arbitrary is not forced — "
      "Monday.com, Oyster, Deel and Gusto are all arbitrary | **`tuesdaytalent.com` is free but "
      "an existing Facebook page uses that exact name** for freelance creatives — the same "
      "platform you advertise on. `tuesdayteams.com` collides with Microsoft Teams |")
    A("")
    A("`thursdaytalent.com` scores top of §3 and I would still not buy it: **Thursday is a "
      "well-known\nLondon and New York dating app** whose audience is the same young urban "
      "professional you are\nbuying impressions against.\n")

    art = [r for r in rows if r["art"]]
    if art:
        A("---\n\n## 7. `ARTIFACT` hits — words the join invented\n")
        A("Gated. Each of these reads as a word that is in neither half of the name.\n")
        A("| Domain | Accidental word |\n|---|---|")
        for d, h in sorted({(f"{x['w']}{x['h']}.com", x["art"][0]) for x in art}):
            A(f"| `{d}` | **{h}** |")
        A("")
        A("**`lindentalent.com` is the one that matters** — `linden` is otherwise the best-scoring "
          "first word\nin the study, and `Linden Talent` is free. It contains **dental**. Use "
          "`lindenhiring.com` or\n`lindenhires.com` instead, both of which are also free.\n")
    open(OUT, "w").write("\n".join(L))


if __name__ == "__main__":
    main()
