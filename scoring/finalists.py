#!/usr/bin/env python3
"""
Round five: take the corpus-attested phrases that are TAKEN on .com and check .co.

scoring/collocation.py established the constraint precisely:

  * only 3.2% of modifier+noun pairs are attested English phrases -- the measured
    reason `Graded Crew` reads as forced
  * of 141 attested phrases about people and hiring, 131 are already taken on .com
  * the 10 that are free are free BECAUSE they are the weakest collocations in the set
    (`stout people`, `tall office`, `hires staff`)

So the .com plain-speech register is exhausted. That is a finding, not an opinion, and
it means the operator's question answers itself: **you cannot have plain language, a
strong phrase, and .com simultaneously.** The available combinations are

  plain + strong + not-.com        <- this file
  plain + weak   + .com            <- stoutpeople.com
  forced + strong + .com           <- GradedCrew.com, rejected twice

This file prices the first row. Every strong attested phrase gets checked on .co
(DNS proxy, calibrated), .net, and the nine semantic gTLDs (authoritative RDAP), plus
an HTTP fetch of the .com to see whether the type-in leak actually costs anything.

Run:  python3 scoring/finalists.py > /dev/null   (appends CO.md section 7)
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
SEM = ["team", "group", "works", "studio", "house", "company", "partners", "careers",
       "agency"]


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


def co_free(slug):
    ns = doh(slug + ".co", "NS")
    if ns is None:
        return None
    if ns != 3:
        return False
    s = doh(slug + ".co", "SOA")
    return None if s is None else s == 3


PARK = re.compile(r"(domain (?:name )?(?:is|may be) for sale|buy this domain|hugedomains"
                  r"|afternic|sedoparking|dan\.com|parkingcrew|bodis|make an offer"
                  r"|domain for sale|inquire about this domain|this domain is parked)", re.I)


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


# hand-added candidates that the collocation generator cannot produce, because they are
# not modifier+noun: sentences, articles, and compounds already in the operator's list
EXTRA = ["wevouch", "usvouch", "vouchfor", "wevouchforthem", "allhands", "teammate",
         "goodhands", "righthand", "firstteam", "deepbench", "benchdepth", "thelineup",
         "lineup", "handpicked", "scoutreport", "thecallup", "depthchart", "farmteam",
         "walkon", "dayone", "firstday", "onloan", "shortlist", "huddle", "standup",
         "tuesdayteams", "mondayteams", "tuesdaytalent", "tuesdaycrew", "thursdaycrew",
         "surehands", "steadyhands", "steadyhires", "readyhands", "extrahands",
         "properhands", "safepair", "safepairofhands", "apairofhands", "goodfolks",
         "goodcrew", "greatcrew", "goodbench", "fullbench", "thewholebench"]


def main():
    cache = json.load(open("scoring/.colloc_cache.json"))
    fr = cache["fr"]
    pairs = [(a, b, s) for a, b, s in cache["pairs"]]

    # strongest attested phrases, regardless of .com status
    def rank(p):
        a, b, s = p
        return (s ** 0.5) * ((fr.get(a, 0) + 1) ** 0.25) * ((fr.get(b, 0) + 1) ** 0.25)

    pairs.sort(key=rank, reverse=True)
    strong = [(a, b, s) for a, b, s in pairs if 5 <= len(a + b) <= 16][:70]
    slugs = [a + b for a, b, _ in strong] + EXTRA
    slugs = list(dict.fromkeys(slugs))
    bigram = {a + b: s for a, b, _ in [] } or {}
    for a, b, s in strong:
        bigram[a + b] = s
    disp = {}
    for a, b, _ in strong:
        disp[a + b] = f"{a.capitalize()} {b.capitalize()}"

    print(f"checking {len(slugs)} candidates on .co, .net and {len(SEM)} semantic TLDs ...")
    with ThreadPoolExecutor(max_workers=12) as ex:
        co = dict(zip(slugs, ex.map(co_free, slugs)))
        net = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".net", "net"), slugs)))
        com = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".com", "com"), slugs)))

    pool = [s for s in slugs if co.get(s) or net.get(s) or com.get(s)]
    combos = [(s, t) for s in pool for t in SEM]
    with ThreadPoolExecutor(max_workers=14) as ex:
        sem = dict(zip(combos, ex.map(lambda p: rdap_free(f"{p[0]}.{p[1]}", p[1]), combos)))
    with ThreadPoolExecutor(max_workers=8) as ex:
        occ = dict(zip(pool, ex.map(lambda s: occupant(s + ".com"), pool)))

    json.dump({"co": co, "net": net, "com": com, "occ": {k: list(v) for k, v in occ.items()},
               "sem": {f"{a}|{b}": v for (a, b), v in sem.items()}, "bigram": bigram},
              open("scoring/.final_cache.json", "w"), indent=1)

    print(f"\n=== AVAILABLE SOMEWHERE ({len(pool)}) ===")
    for s in sorted(pool):
        k, t = occ[s]
        st = [tl for tl in SEM if sem.get((s, tl))]
        print(f"  {s:18s} com={'FREE' if com[s] else k:9s} co={'free' if co[s] else '-':5s} "
              f"net={'free' if net[s] else '-':5s} bigram={bigram.get(s,0) or '-':>8} "
              f"sem={','.join(st[:5])}")
        if t:
            print(f"      .com title: {t}")
    return pool


if __name__ == "__main__":
    main()
