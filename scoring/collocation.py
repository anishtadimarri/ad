#!/usr/bin/env python3
"""
Round four: measure "natural" instead of asserting it.

The operator has now rejected two rounds of names as forced. Both times I was scoring
naturalness with my own ear -- a hand-written SAYS dict in scoring/co_names.py, with
numbers I made up. That is exactly the kind of invented figure this project is not
supposed to contain, and it produced `verity` (flows, nobody says it) and
`willingtalent` (available, not a phrase).

Naturalness of a two-word name decomposes into two things, and **both are measurable**:

  COMMON        how often each word occurs in English            Datamuse md=f
                (frequency per million words, Google Books)
  COLLOCATION   how often word B actually follows word A         Datamuse rel_bga
                (bigram score from the same corpus)

"Forced" is the failure of the second. `Graded Crew` is two known words that never
co-occur; `Good Hands` is a phrase with a real bigram score. That is the whole
difference, and it is a number rather than a matter of taste.

Method:
  1. one Datamuse rel_bga call per modifier -> the full distribution of words that
     follow it in the corpus
  2. keep only pairs where the right-hand word IS in that distribution -- i.e. it is
     an attested English phrase, not a cartesian product
  3. score by bigram strength x word commonness
  4. spend RDAP/DNS checks only on the survivors

Run:  python3 scoring/collocation.py > /dev/null   (appends CO.md section 7)
"""
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

DM = "https://api.datamuse.com/words"
VER = "https://rdap.verisign.com/{t}/v1/domain/"

# what we sell, in words a buyer says
NOUNS = ["hands", "people", "folks", "crew", "team", "teams", "talent", "staff", "hires",
         "help", "mates", "bench", "roster", "lineup", "squad", "desk", "hire", "workers",
         "colleagues", "partners", "minds", "heads", "players", "hand", "seat", "seats",
         "chair", "shop", "house", "works", "office", "room", "table", "board"]

# plain modifiers: qualities, ordinals, days, quantities
MODS = """good great right sure steady extra spare ready able strong sharp solid trusted
proper plenty willing eager seasoned handy quiet calm kind warm true fair open plain
simple clear bright clean quick fast smart wise deep full whole wide long broad tall
first second next new top best early late day week month year monday tuesday wednesday
thursday friday saturday sunday north south east west home away near far high low
free fresh light heavy small big large little more most many few own real own
safe swift keen stout hardy able loyal ample""".split()

VERBS = """hire hires hired hiring vouch vouched grade graded pick picked scout scouted
place placed match matched vet vetted rate rated staff staffed back backed train trained
build built find found send sent bring brought keep kept hold held run ran""".split()


def curl(url, timeout=20):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout), url],
                           capture_output=True, text=True, timeout=timeout + 8)
        return r.stdout
    except Exception:
        return ""


def code(url, timeout=15):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout), "-o", "/dev/null",
                            "-w", "%{http_code}", url],
                           capture_output=True, text=True, timeout=timeout + 8)
        return int(r.stdout.strip() or 0)
    except Exception:
        return 0


def rdap_free(fqdn, tld="com"):
    c = code(VER.format(t=tld) + fqdn)
    return True if c == 404 else (False if c == 200 else None)


def doh(name, rr):
    try:
        return json.loads(curl(f"https://dns.google/resolve?name={name}&type={rr}")).get("Status")
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


def followers(word):
    """Corpus distribution of words that follow `word`. Real bigram data."""
    try:
        js = json.loads(curl(f"{DM}/?rel_bga={word}&max=1000"))
        return {d["word"]: d["score"] for d in js if "score" in d}
    except Exception:
        return {}


def freqs(words):
    """Frequency per million for each word (Datamuse md=f, Google Books)."""
    out = {}

    def one(w):
        try:
            js = json.loads(curl(f"{DM}/?sp={w}&md=f&max=1"))
            for d in js:
                if d["word"] == w:
                    for t in d.get("tags", []):
                        if t.startswith("f:"):
                            return float(t[2:])
        except Exception:
            pass
        return 0.0
    with ThreadPoolExecutor(max_workers=10) as ex:
        for w, v in zip(words, ex.map(one, words)):
            out[w] = v
    return out


def main():
    lefts = sorted(set(MODS + VERBS))
    print(f"pulling bigram distributions for {len(lefts)} modifiers ...")
    with ThreadPoolExecutor(max_workers=10) as ex:
        big = dict(zip(lefts, ex.map(followers, lefts)))

    vocab = sorted(set(lefts + NOUNS))
    print(f"pulling frequencies for {len(vocab)} words ...")
    fr = freqs(vocab)

    # attested pairs only
    pairs = []
    for a in lefts:
        d = big.get(a) or {}
        for b in NOUNS:
            s = d.get(b)
            if s:
                pairs.append((a, b, s))
    print(f"attested collocations found: {len(pairs)} (of {len(lefts)*len(NOUNS)} possible "
          f"-> {len(pairs)/(len(lefts)*len(NOUNS))*100:.1f}% are real phrases)")

    def rank(p):
        a, b, s = p
        # bigram strength, damped, times commonness of both words, damped
        return (s ** 0.5) * ((fr.get(a, 0) + 1) ** 0.25) * ((fr.get(b, 0) + 1) ** 0.25)

    pairs.sort(key=rank, reverse=True)
    top = [p for p in pairs if 5 <= len(p[0] + p[1]) <= 16][:260]
    slugs = [a + b for a, b, _ in top]
    print(f"checking .com for top {len(slugs)} ...")

    with ThreadPoolExecutor(max_workers=14) as ex:
        com = dict(zip(slugs, ex.map(lambda s: rdap_free(s + ".com"), slugs)))
    unk = [s for s in slugs if com[s] is None]
    if unk:
        with ThreadPoolExecutor(max_workers=6) as ex:
            for s, v in zip(unk, ex.map(lambda s: rdap_free(s + ".com"), unk)):
                com[s] = v

    free = [(a, b, s) for a, b, s in top if com.get(a + b) is True]
    print(f".com free among attested phrases: {len(free)}")

    fslug = [a + b for a, b, _ in free]
    with ThreadPoolExecutor(max_workers=10) as ex:
        co = dict(zip(fslug, ex.map(co_free, fslug)))
        net = dict(zip(fslug, ex.map(lambda s: rdap_free(s + ".net", "net"), fslug)))

    json.dump({"pairs": [[a, b, s] for a, b, s in pairs[:800]], "fr": fr,
               "com": com, "co": co, "net": net},
              open("scoring/.colloc_cache.json", "w"), indent=1)

    print("\n=== ATTESTED PHRASES, FREE ON .COM (ranked by corpus strength) ===")
    for a, b, s in free:
        print(f"  {a+'.'+b:24s} bigram={int(s):>7d}  f(a)={fr.get(a,0):7.2f} "
              f"f(b)={fr.get(b,0):6.2f}  .co={'free' if co[a+b] else 'taken'}  "
              f".net={'free' if net[a+b] else 'taken'}")
    return free, com, co, net, fr, pairs


if __name__ == "__main__":
    main()
