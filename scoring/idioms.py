#!/usr/bin/env python3
"""
Round six: idioms. The register the liked names were actually in.

Re-reading the operator's reactions once more:

  All Hands   -- an IDIOM. "all hands on deck." Not a description of anything.
  Teammate    -- one plain word.
  Tuesday     -- one plain word, arbitrary.

  Graded Crew, Verity People -- adjective + noun DESCRIPTIONS.

The liked names describe nothing. They are idioms or arbitrary plain words, and the
buyer supplies the meaning. The rejected names try to specify the product in the name,
which is what "forced" means: a name doing a landing page's job.

Rounds one to five searched literary words (verity), collocations (steady hires) and
day-words (tuesday talent). None searched **idioms**, which is where All Hands lives.

So: two-word English idioms and single idiomatic nouns for an indispensable person,
biased toward trust, quality and selection -- because those are the three things a
buyer with no reason to trust an unknown Indian operator is actually weighing.

Prior rounds also produced kills that must be respected here, all from real data:
  vouch*        vouchfor.com -> "The AI content platform for talent teams | Vouch"
  *bench*       "bench sales recruiter" is Indian IT staffing's own term for the
                commodity end of this market -- plus Bench Accounting and two Bench
                clothing brands
  surehands     surehands.com -> home mobility lifts, the Safe Hands trap again
  monday*       monday-talent.com is a live creative recruitment agency, near-identical
                ICP, and monday.com holds the mark in software

Run:  python3 scoring/idioms.py
"""
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

ID = "https://rdap.identitydigital.services/rdap/domain/"
RD = {"com": "https://rdap.verisign.com/com/v1/domain/",
      "net": "https://rdap.verisign.com/net/v1/domain/",
      "team": ID, "group": ID, "works": ID, "studio": ID, "house": ID,
      "company": ID, "partners": ID, "careers": ID, "agency": ID}

# (slug, display, what a buyer hears)
IDIOMS = [
    # --- selection / who scouts and signs talent -----------------------------
    ("frontoffice", "Front Office", "in sport, the people who scout, sign and manage the "
                                    "roster. Everyday US speech, exactly this job"),
    ("hometeam", "Home Team", "they become part of *your* side, not a vendor's"),
    ("homefield", "Home Field", "advantage, on your ground"),
    ("firstchair", "First Chair", "orchestra: the best player in the section"),
    ("secondchair", "Second Chair", "the deputy — reads junior"),
    ("insidetrack", "Inside Track", "the advantage of knowing where to look"),
    ("frontrow", "Front Row", "the best seats"),
    ("frontrunner", "Front Runner", "who is winning"),
    ("standout", "Standout", "\"she was a standout\" — one plain word for graded-best"),
    ("standouts", "Standouts", "plural"),
    ("toppick", "Top Pick", "draft speech"),
    ("firstpick", "First Pick", "same"),
    ("wildcard", "Wild Card", "the unseeded entrant who wins — the whole India thesis"),
    ("shoein", "Shoe In", "a certainty"),
    ("darkhorse", "Dark Horse", "the unbacked contender who wins. India, named"),
    # --- the indispensable person, single idiomatic nouns --------------------
    ("mainstay", "Mainstay", "\"he was our mainstay\" — the person you rely on most"),
    ("linchpin", "Linchpin", "the part everything turns on"),
    ("backbone", "Backbone", "who holds it up"),
    ("cornerstone", "Cornerstone", "what is built on"),
    ("touchstone", "Touchstone", "the standard other things are measured against"),
    ("keystone", "Keystone", "the stone that holds the arch"),
    ("bedrock", "Bedrock", "underneath everything"),
    ("workhorse", "Workhorse", "reliable — but hints at drudgery"),
    ("righthand", "Right Hand", "\"my right hand\""),
    ("standby", "Standby", "ready when needed — hints at second-choice"),
    ("ringer", "Ringer", "the secretly excellent player brought in. Also connotes a cheat"),
    # --- quality, said plainly ----------------------------------------------
    ("topdrawer", "Top Drawer", "British everyday for first-rate"),
    ("topshelf", "Top Shelf", "US equivalent"),
    ("firstrate", "First Rate", "plain, old and unambiguous"),
    ("goldstandard", "Gold Standard", "the grade, named"),
    ("thegoldstandard", "The Gold Standard", "article form"),
    ("realdeal", "Real Deal", "\"she's the real deal\" — authenticity against a market "
                              "full of resellers"),
    ("therealdeal", "The Real Deal", "article form"),
    ("goodcompany", "Good Company", "both senses at once: pleasant to be with, and a good "
                                    "business. The best pun available in plain English"),
    ("goodhands", "Good Hands", "\"you're in good hands\""),
    ("safepair", "Safe Pair", "\"a safe pair of hands\", shortened"),
    ("cleanhands", "Clean Hands", "legal idiom for blamelessness — reads oddly for labour"),
    ("steadyhand", "Steady Hand", "singular is calmer than the plural"),
    ("freehand", "Free Hand", "latitude to act — wrong meaning here"),
    ("secondnature", "Second Nature", "what expertise feels like"),
    ("naturalfit", "Natural Fit", "matching, in the buyer's words"),
    ("rightfit", "Right Fit", "the most-used phrase in hiring"),
    ("perfectfit", "Perfect Fit", "same, overclaimed"),
    # --- the work itself ----------------------------------------------------
    ("heavylifting", "Heavy Lifting", "what gets handed over"),
    ("theheavylifting", "The Heavy Lifting", "article form"),
    ("legwork", "Legwork", "what a placement saves you"),
    ("thelegwork", "The Legwork", "article form"),
    ("groundwork", "Groundwork", "what gets done before the win"),
    ("spadework", "Spadework", "unglamorous preparation — too self-deprecating"),
    ("handiwork", "Handiwork", "the output, and it contains 'hand'"),
    ("breadandbutter", "Bread And Butter", "the core work — long"),
    # --- start / momentum ---------------------------------------------------
    ("headstart", "Head Start", "what the buyer is paying for"),
    ("legup", "Leg Up", "same, shorter"),
    ("upperhand", "Upper Hand", "advantage"),
    ("secondwind", "Second Wind", "renewed energy — for a stalled team"),
    ("cleanslate", "Clean Slate", "a fresh start"),
    ("groundfloor", "Ground Floor", "early access"),
    ("fullhouse", "Full House", "every seat filled — the seats-per-client metric, idiomatically"),
    ("fullcircle", "Full Circle", "generic"),
    ("evenkeel", "Even Keel", "stability"),
    ("fairshake", "Fair Shake", "a fair chance — points at the talent, not the buyer"),
    ("openarms", "Open Arms", "welcome"),
    ("warmwelcome", "Warm Welcome", "onboarding"),
    ("longgame", "Long Game", "the 24-month thesis"),
    ("thelonggame", "The Long Game", "article form"),
]

PARK = re.compile(r"(domain (?:name )?(?:is|may be) for sale|buy this domain|hugedomains"
                  r"|afternic|sedoparking|dan\.com|parkingcrew|bodis|make an offer"
                  r"|domain for sale|inquire about this domain|this domain is parked)", re.I)


def curl(url, timeout=18, extra=()):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout), "-w", "\n%{http_code}",
                            *extra, url], capture_output=True, text=True, timeout=timeout + 8)
        b, _, c = r.stdout.rpartition("\n")
        return b, int(c or 0)
    except Exception:
        return "", 0


def rdap_free(fqdn, tld):
    _, c = curl(RD[tld] + fqdn)
    return True if c == 404 else (False if c == 200 else None)


def doh(n, rr):
    b, c = curl(f"https://dns.google/resolve?name={n}&type={rr}")
    if c != 200:
        return None
    try:
        return json.loads(b).get("Status")
    except Exception:
        return None


def co_free(s):
    ns = doh(s + ".co", "NS")
    if ns is None:
        return None
    if ns != 3:
        return False
    return doh(s + ".co", "SOA") == 3


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
    t = re.sub(r"\s+", " ", m.group(1)).strip()[:58] if m else ""
    if c >= 400 or not (b or "").strip():
        return "dark", t
    return "live", t


def main():
    slugs = [s for s, _, _ in IDIOMS]
    print(f"{len(slugs)} idioms -> .com/.co/.net + occupant ...")
    with ThreadPoolExecutor(max_workers=12) as ex:
        com = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".com", "com"), slugs)))
        co = dict(zip(slugs, ex.map(co_free, slugs)))
        net = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".net", "net"), slugs)))
    unk = [s for s in slugs if com[s] is None or co[s] is None]
    if unk:
        with ThreadPoolExecutor(max_workers=6) as ex:
            for s, v in zip(unk, ex.map(lambda s: rdap_free(s + ".com", "com"), unk)):
                if com[s] is None:
                    com[s] = v
        for s in unk:
            if co[s] is None:
                co[s] = co_free(s)

    live = [s for s in slugs if com[s] is False]
    with ThreadPoolExecutor(max_workers=8) as ex:
        occ = dict(zip(live, ex.map(lambda s: occupant(s + ".com"), live)))

    json.dump({"com": com, "co": co, "net": net,
               "occ": {k: list(v) for k, v in occ.items()}},
              open("scoring/.idiom_cache.json", "w"), indent=1)

    print("\n=== FREE ON .COM ===")
    for s, d, w in IDIOMS:
        if com[s]:
            print(f"  {d:20s} {s+'.com':24s} co={'free' if co[s] else 'taken'} "
                  f"net={'free' if net[s] else 'taken'}")
    print("\n=== .COM TAKEN BUT DARK / FOR SALE, AND .CO FREE (leak is cheap) ===")
    for s, d, w in IDIOMS:
        if com[s] is False and co[s] and occ.get(s, ("", ""))[0] in ("dark", "for sale"):
            print(f"  {d:20s} {s+'.co':24s} .com is {occ[s][0]:9s} "
                  f"net={'free' if net[s] else 'taken'}")
    print("\n=== .com LIVE occupants (for the record) ===")
    for s, d, w in IDIOMS:
        if occ.get(s, ("", ""))[0] == "live":
            print(f"  {d:20s} {occ[s][1]}")
    print(f"\nunresolved: {sum(1 for v in list(com.values())+list(co.values()) if v is None)}")


if __name__ == "__main__":
    main()
