#!/usr/bin/env python3
"""
Round three: sweep the plain-speech register wide enough to be conclusive.

Round two tested 60 hand-picked plain-speech names and found **zero** free on .com.
Sixty is not enough to conclude the register is exhausted. So this generates the
register combinatorially from real English collocations -- not random pairs -- and
checks every one.

If a plain-speech name IS free on .com, it beats every .co and every semantic TLD and
the TLD argument becomes moot. If nothing is free, then the choice really is between
a forced .com and an unforced non-.com, which is the operator's actual question.

Generators, each a real collocation family rather than a cartesian guess:

  QUALITY + PEOPLE   good/great/right/sure/steady/extra/spare/ready/able + hands/people/crew...
  ORDINAL + SLOT     first/next/new/top/best/day + hire/day/team/pick/chair/call...
  PRONOUN + VERB     we/you + vouch/grade/pick/scout/place/hire/train/back
  VERB + PARTICLE    hire/scout/grade/pick/vouch/back/staff + up/well/right/first/on
  DAY + UNIT         monday..friday + team/crew/hire/talent/people/desk (the operator's own
                     Monday/Tuesday instinct, extended)
  SPORT SELECTION    deep/first/top/full + bench/team/roster/lineup/squad

Availability: .com/.net by Verisign RDAP (authoritative). .co by the DNS proxy
calibrated at 0/82 false-availables in scoring/dns_probe.py.

Run:  python3 scoring/plain_sweep.py
"""
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

VER = "https://rdap.verisign.com/{t}/v1/domain/"


def curl(url, timeout=15):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout), "-o", "/dev/null",
                            "-w", "%{http_code}", url],
                           capture_output=True, text=True, timeout=timeout + 8)
        return int(r.stdout.strip() or 0)
    except Exception:
        return 0


def rdap_free(fqdn, tld="com"):
    c = curl(VER.format(t=tld) + fqdn)
    return True if c == 404 else (False if c == 200 else None)


def doh(name, rr):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", "15",
                            f"https://dns.google/resolve?name={name}&type={rr}"],
                           capture_output=True, text=True, timeout=25)
        return json.loads(r.stdout).get("Status")
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


# --- collocation families ---------------------------------------------------
QUAL = ["good", "great", "right", "sure", "steady", "extra", "spare", "ready", "able",
        "strong", "sharp", "solid", "trusted", "proper", "plenty", "willing", "eager",
        "seasoned", "handy"]
PEOPLE = ["hands", "people", "folks", "crew", "team", "help", "hires", "hands", "mates",
          "talent", "staff"]

ORD = ["first", "next", "new", "top", "best", "day", "week", "early", "front"]
SLOT = ["hire", "hires", "day", "team", "pick", "chair", "call", "seat", "desk", "chairs",
        "round", "string"]

PRON = ["we", "you", "they", "us"]
VERB = ["vouch", "grade", "pick", "scout", "place", "hire", "train", "back", "staff",
        "match", "vet", "rate"]

VP = ["hire", "scout", "grade", "pick", "vouch", "back", "staff", "match", "vet", "rate",
      "place", "team", "crew", "bench"]
PART = ["up", "well", "right", "first", "on", "over", "ahead", "far", "true", "here",
        "now", "next", "more", "better", "smart", "sharp"]

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "sunday"]
UNIT = ["team", "teams", "crew", "hire", "hires", "talent", "people", "desk", "bench",
        "roster", "staff", "hands"]

DEPTH = ["deep", "first", "top", "full", "long", "wide", "whole", "big"]
SPORT = ["bench", "team", "roster", "lineup", "squad", "field", "order", "list"]


def gen():
    s = set()
    for a in QUAL:
        for b in PEOPLE:
            s.add(a + b)
    for a in ORD:
        for b in SLOT:
            s.add(a + b)
    for a in PRON:
        for b in VERB:
            s.add(a + b)
    for a in VP:
        for b in PART:
            s.add(a + b)
    for a in DAYS:
        for b in UNIT:
            s.add(a + b)
    for a in DEPTH:
        for b in SPORT:
            s.add(a + b)
    return sorted(w for w in s if 5 <= len(w) <= 16)


def main():
    cands = gen()
    print(f"generated {len(cands)} plain-speech collocations")

    with ThreadPoolExecutor(max_workers=14) as ex:
        com = dict(zip(cands, ex.map(lambda s: rdap_free(s + ".com"), cands)))

    free_com = sorted(s for s in cands if com[s] is True)
    unk = [s for s in cands if com[s] is None]
    print(f".com free : {len(free_com)}   (unresolved {len(unk)})")

    # retry unresolved once -- an unknown must not be reported as a finding
    if unk:
        with ThreadPoolExecutor(max_workers=8) as ex:
            for s, v in zip(unk, ex.map(lambda s: rdap_free(s + ".com"), unk)):
                com[s] = v
        free_com = sorted(s for s in cands if com[s] is True)
        print(f"after retry -> .com free {len(free_com)}, "
              f"still unknown {sum(1 for v in com.values() if v is None)}")

    with ThreadPoolExecutor(max_workers=10) as ex:
        net = dict(zip(free_com, ex.map(lambda s: rdap_free(s + ".net", "net"), free_com)))
        co = dict(zip(free_com, ex.map(co_free, free_com)))

    json.dump({"com": com, "net": net, "co": co},
              open("scoring/.sweep_cache.json", "w"), indent=1)

    print("\nFREE ON .COM:")
    for s in free_com:
        print(f"  {s:18s} .net={'free' if net[s] else 'taken'}  "
              f".co={'free' if co[s] else 'taken'}")
    return free_com


if __name__ == "__main__":
    main()
