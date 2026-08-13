#!/usr/bin/env python3
"""
Round two: stop generating literary names.

Evidence from the operator's own reactions, which is better evidence than my prosody model:

  liked      All Hands · Teammate · Tuesday · Monday Teams · Kloud Teams
  rejected   Hold Fast ("such a not common word") · Open Book ("doesn't mean anything")
             Graded Crew ("very forced") · Verity People ("so forced")

The liked list is **plain spoken English** — things a person says out loud at work.
The rejected list is either a word nobody says (verity, fast=hold fast) or an
adjective+noun spec (graded crew). My last two rounds optimised prosody and kept
producing literary abstractions: verity, mettle, surety, kindred, lumina. Those flow
beautifully and **nobody says them**, which is exactly what "forced" means.

So this screen changes the generator, not the scorer. Three registers, all plain:

  A  WORKPLACE SPEECH   things said in an office: all hands, stand up, first day,
                        good hands, right hand, head count, back fill, hand picked
  B  SELECTION SPEECH   how people already talk about picking talent, borrowed from
                        sport: line up, first team, depth chart, draft day, scouted,
                        starters, top pick. Semantically exact for graded talent, and
                        it is the register the graded directory already lives in.
  C  BARE PLAIN WORDS   one everyday word, checked against nine semantic TLDs so the
                        word can stand alone instead of being welded to "Talent":
                        `lineup.team` is speech; `LineupTalent.com` is a spec.

Availability: RDAP everywhere except `.co`, which uses the DNS proxy calibrated at
0/82 false-availables in scoring/dns_probe.py.

Run:  python3 scoring/plainspeech.py > /dev/null   (writes CO.md section 6+)
"""
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

ID = "https://rdap.identitydigital.services/rdap/domain/"
RDAP = {
    "com": "https://rdap.verisign.com/com/v1/domain/",
    "net": "https://rdap.verisign.com/net/v1/domain/",
    "team": ID, "group": ID, "works": ID, "studio": ID, "house": ID,
    "company": ID, "partners": ID, "careers": ID, "agency": ID, "ai": ID,
}

# --- A: workplace speech ----------------------------------------------------
PHRASE_A = [
    ("allhands", "All Hands", "the whole-company meeting; also 'all hands on deck'"),
    ("goodhands", "Good Hands", "\"you're in good hands\" — the promise, said plainly"),
    ("righthand", "Right Hand", "\"my right hand\" — the indispensable teammate"),
    ("extrahands", "Extra Hands", "what the buyer literally asks for"),
    ("morehands", "More Hands", "the buyer's own words"),
    ("steadyhands", "Steady Hands", "reliability, spoken not claimed"),
    ("surehands", "Sure Hands", "sport commentary for someone who never drops it"),
    ("handpicked", "Handpicked", "one everyday word that *is* the graded-selection promise"),
    ("firstday", "First Day", "the moment the buyer is buying"),
    ("dayone", "Day One", "\"from day one\" — said constantly"),
    ("weekone", "Week One", "the ramp"),
    ("standup", "Standup", "the daily meeting"),
    ("huddle", "Huddle", "the meeting, and the team"),
    ("headcount", "Headcount", "the buyer's budget line, in their words"),
    ("backfill", "Backfill", "what a departure creates"),
    ("onboard", "Onboard", "the verb every buyer uses"),
    ("shortlist", "Shortlist", "exactly what is delivered"),
    ("newhire", "New Hire", "plainest possible"),
    ("firsthire", "First Hire", "the buyer's first offshore hire"),
    ("nexthire", "Next Hire", "and the second"),
    ("goodpeople", "Good People", "\"we just need good people\""),
    ("ourpeople", "Our People", "how a client refers to a placed teammate"),
    ("yourpeople", "Your People", "the ownership transfer, stated"),
    ("morepeople", "More People", "the ask"),
    ("teammate", "Teammate", "already on the operator's shortlist"),
    ("crewmate", "Crewmate", "same shape, less contested"),
    ("workmate", "Workmate", "British-English everyday"),
    ("sidekick", "Sidekick", "warm, said out loud, slightly junior — a real risk"),
    ("onloan", "On Loan", "\"seconded\" in plain speech; describes the EOR model exactly"),
    ("vouched", "Vouched", "past participle — the graded claim as speech"),
    ("wevouch", "We Vouch", "a sentence, not a spec"),
    ("legup", "Leg Up", "\"gives you a leg up\""),
    ("headstart", "Head Start", "same, more common"),
    ("upperhand", "Upper Hand", "what the buyer gets"),
    ("payroll", "Payroll", "the EOR product in one everyday word"),
]

# --- B: selection speech ----------------------------------------------------
PHRASE_B = [
    ("lineup", "Lineup", "the chosen eleven; one word, everyday, exactly the product"),
    ("thelineup", "The Lineup", "article form"),
    ("firstteam", "First Team", "sport for the starters — not the reserves"),
    ("firstchair", "First Chair", "orchestra for the best player in the section"),
    ("firstpick", "First Pick", "draft speech"),
    ("toppick", "Top Pick", "same"),
    ("draftday", "Draft Day", "the day talent is selected, and it is a film"),
    ("thedraft", "The Draft", "short, but 'draft' also means a rough version"),
    ("depthchart", "Depth Chart", "the roster ranked by grade — the graded directory, named"),
    ("deepbench", "Deep Bench", "\"they have a deep bench\" — the bench is the asset"),
    ("thebench", "The Bench", "the asset, plainly"),
    ("benchdepth", "Bench Depth", "same, noun-first"),
    ("farmteam", "Farm Team", "where graded talent is developed before promotion"),
    ("scouted", "Scouted", "one word, past tense, means someone went and looked"),
    ("thescout", "The Scout", "the person who grades"),
    ("scoutreport", "Scout Report", "the deliverable"),
    ("starters", "Starters", "who plays"),
    ("startinglineup", "Starting Lineup", "long but pure speech"),
    ("walkon", "Walk On", "unrecruited talent that turns out to be good — the whole thesis"),
    ("callup", "Call Up", "promotion from the farm team to the first team"),
    ("thecallup", "The Call Up", "article form"),
    ("shortlisted", "Shortlisted", "past tense"),
    ("proven", "Proven", "one everyday word; the guarantee in a syllable"),
    ("tried", "Tried", "\"tried and tested\""),
    ("tested", "Tested", "plain"),
]

# --- C: bare plain words, to be paired with a semantic TLD ------------------
BARE = ["lineup", "huddle", "roster", "bench", "crew", "scout", "starters", "handpicked",
        "vouched", "proven", "hands", "allhands", "teammate", "shortlist", "callup",
        "firstteam", "depthchart", "goodhands", "righthand", "dayone", "onloan",
        "payroll", "headcount", "backfill", "standup", "onboard", "farmteam", "walkon",
        "monday", "tuesday", "morning", "harbor", "anchor", "compass", "beacon"]
SEM_TLD = ["team", "group", "works", "studio", "house", "company", "partners",
           "careers", "agency"]


def curl(url, timeout=18, extra=()):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout),
                            "-w", "\n%{http_code}", *extra, url],
                           capture_output=True, text=True, timeout=timeout + 8)
        body, _, code = r.stdout.rpartition("\n")
        return body, int(code or 0)
    except Exception:
        return "", 0


def rdap_free(fqdn, tld):
    _, c = curl(RDAP[tld] + fqdn)
    return True if c == 404 else (False if c == 200 else None)


def doh(name, rr):
    b, c = curl(f"https://dns.google/resolve?name={name}&type={rr}")
    if c != 200:
        return None
    try:
        return json.loads(b).get("Status")
    except Exception:
        return None


def co_free(word):
    ns = doh(word + ".co", "NS")
    if ns is None:
        return None
    if ns != 3:
        return False
    s = doh(word + ".co", "SOA")
    return None if s is None else s == 3


PARK = re.compile(r"(domain (?:name )?(?:is|may be) for sale|buy this domain|hugedomains"
                  r"|afternic|sedoparking|dan\.com|parkingcrew|bodis|make an offer"
                  r"|domain for sale|inquire about this domain)", re.I)


CF = re.compile(r"(just a moment|attention required|cf-browser-verification"
                r"|checking your browser|enable javascript and cookies)", re.I)


def occupant(fqdn):
    b, c = curl(f"https://{fqdn}/", 16, ("-L", "--max-redirs", "4", "-A",
                                         "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"))
    if c == 0:
        return "dark", ""
    if PARK.search(b or ""):
        return "for sale", ""
    if CF.search(b or ""):
        # a Cloudflare interstitial means the site is LIVE but its contents are
        # unverified. Reporting this as "dark" would understate the type-in leak.
        return "protected", ""
    m = re.search(r"<title[^>]*>(.*?)</title>", b or "", re.I | re.S)
    t = re.sub(r"\s+", " ", m.group(1)).strip()[:60] if m else ""
    if c >= 400 or not (b or "").strip():
        return "dark", t
    return "live", t


def main():
    phrases = PHRASE_A + PHRASE_B
    slugs = [p[0] for p in phrases]
    print(f"{len(slugs)} phrases x .com/.co, {len(BARE)}x{len(SEM_TLD)} bare+semantic ...")

    with ThreadPoolExecutor(max_workers=12) as ex:
        com = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".com", "com"), slugs)))
        co = dict(zip(slugs, ex.map(co_free, slugs)))
        net = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".net", "net"), slugs)))

    pairs = [(w, t) for w in BARE for t in SEM_TLD]
    with ThreadPoolExecutor(max_workers=12) as ex:
        sem = dict(zip(pairs, ex.map(lambda p: rdap_free(f"{p[0]}.{p[1]}", p[1]), pairs)))

    # what sits on the .com, for anything free on .co but not .com
    leaky = [s for s in slugs if co.get(s) and not com.get(s)]
    with ThreadPoolExecutor(max_workers=8) as ex:
        occ = dict(zip(leaky, ex.map(lambda s: occupant(s + ".com"), leaky)))

    json.dump({"com": com, "co": co, "net": net,
               "sem": {f"{a}.{b}": v for (a, b), v in sem.items()},
               "occ": {k: list(v) for k, v in occ.items()}},
              open("scoring/.plain_cache.json", "w"), indent=1)

    report(phrases, com, co, net, sem, occ)


LEAK = {"dark": 5, "for sale": 4, "live": 2}


def report(phrases, com, co, net, sem, occ):
    L = []
    A = L.append
    A("\n---\n\n## 6. Round two: the register was wrong, not the prosody\n")
    A("Round one asked *does it flow*. It produced `verity`, `mettle`, `surety`, `kindred`, "
      "`lumina` —\nall of which flow, and **none of which anybody says out loud.** That is what "
      "\"forced\" means, and\nthe operator's own reactions say so more clearly than my scorer did:\n")
    A("| Liked | Rejected | What separates them |")
    A("|---|---|---|")
    A("| All Hands · Teammate · Tuesday · Monday Teams | Hold Fast — *\"such a not common word\"* |"
      " **common vs uncommon** |")
    A("| | Open Book — *\"doesn't mean anything\"* | **means something concrete vs decorative** |")
    A("| | Graded Crew · Verity People — *\"so forced\"* | **speech vs adjective+noun spec** |")
    A("")
    A("So the generator changed, not the scoring. Three registers, all of them plain spoken "
      "English:\n")
    A("| Register | Source | Why it fits |")
    A("|---|---|---|")
    A("| **Workplace speech** | what is actually said in an office | *all hands, day one, good "
      "hands, headcount, handpicked* |")
    A("| **Selection speech** | how people already talk about picking talent, from sport | "
      "*lineup, first team, depth chart, deep bench, call up* — semantically exact for graded "
      "talent, and the register the graded directory already lives in |")
    A("| **Bare word + semantic TLD** | let the word stand alone | `lineup.team` is speech; "
      "`LineupTalent.com` is a spec. **The TLD does the work the compound was doing.** |")
    A("")

    def col(v):
        return "**free**" if v is True else ("taken" if v is False else "?")

    for title, group, note in [
        ("### 6A. Workplace speech", PHRASE_A,
         "Said in an office. Nothing here needs explaining to a buyer."),
        ("### 6B. Selection speech", PHRASE_B,
         "How talent selection is already discussed. `Depth Chart` and `Deep Bench` name the "
         "graded directory — the retention mechanism from [`HUNGRY.md`](HUNGRY.md) §9 — in words "
         "the buyer already owns."),
    ]:
        A(f"\n{title}\n")
        A(f"{note}\n")
        A("| Name | `.com` | `.co` | `.net` | What sits on the `.com` | Reads as |")
        A("|---|---|---|---|---|---|")
        rows = sorted(group, key=lambda p: (not (com.get(p[0]) or co.get(p[0])), p[1]))
        for slug, disp, why in rows:
            k, t = occ.get(slug, ("", ""))
            oc = f"{k}" + (f" — {t}" if t else "") if k else ("— *free*" if com.get(slug) else "")
            A(f"| **{disp}** | {col(com.get(slug))} | {col(co.get(slug))} | "
              f"{col(net.get(slug))} | {oc} | {why} |")
        A("")

    A("\n### 6C. Bare word + semantic TLD — every combination checked\n")
    A("All authoritative RDAP. A `✓` is available; the whole point is that the left column is one "
      "plain word.\n")
    A("| Word | " + " | ".join(f"`.{t}`" for t in SEM_TLD) + " |")
    A("|---|" + "---|" * len(SEM_TLD))
    for w in BARE:
        cells = []
        for t in SEM_TLD:
            v = sem.get((w, t))
            cells.append("✓" if v is True else ("·" if v is False else "?"))
        if any(c == "✓" for c in cells):
            A(f"| **{w}** | " + " | ".join(cells) + " |")
    A("")
    A("*Rows with nothing available are omitted.*\n")

    with open("CO.md", "a") as f:
        f.write("\n".join(L))
    print("appended to CO.md")


if __name__ == "__main__":
    main()
