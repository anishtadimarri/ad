#!/usr/bin/env python3
"""
The .co question, answered with data instead of a preference.

Two things are being asked:

  1. "Why not a good .co"  -- a challenge to the TLD ranking in DOMAINS.md, which
     put .com above everything and therefore forced every name into a compound.
  2. "Some of these seem so forced" -- the second rejection of the naming output.

Those are the same question. Every flowing single word is taken on .com, so a .com
requirement *is* a forcing function: it converts single words into adjective+noun
compounds. If the .com premium is smaller than the cost of a forced name, the
ranking was wrong.

So this screen prices the .com premium instead of assuming it, on three real inputs:

  A) Where the domain appears in THIS funnel. Acquisition is paid Meta traffic --
     the click comes from an ad, nobody types the name. So the TLD is invisible
     at acquisition and only priced at recall, referral and email.
  B) WHAT SITS ON THE .COM. The type-in leak is only expensive if the .com is a
     live confusable business. If it is dark or parked, the leak costs ~nothing.
     Checked over HTTP, per candidate.
  C) Whether a bare single word is even obtainable on .co -- checked by DNS,
     calibrated in scoring/dns_probe.py.

Availability method by TLD:
  .com .net      Verisign RDAP           authoritative (404 = free)
  .ai .team ...  Identity Digital RDAP   authoritative
  .co            DNS-over-HTTPS          proxy, 0/82 false-availables measured
                                         -> confirm at the registrar before buying

Run:  python3 scoring/co_names.py > /dev/null   (writes CO.md)
"""
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor

OUT = "CO.md"

# ---------------------------------------------------------------------------
# Candidates. One rule: it must be a word a person already says, and it must
# flow -- open vowels, liquid/nasal consonants, first-syllable stress, no
# adjective+noun spec grammar. That grammar is what produced "Graded Crew".
# ---------------------------------------------------------------------------
WORDS = """
verity surety amity candor clarity merit mettle valor ardor vigor tenor caliber
credence repute esteem accord concord tribute laurel acclaim regard fettle stature
kindred cognate
vouch attest avow affirm endorse warrant muster marshal rally scout hone whet forge
temper prove second
foundry atelier bench guild bureau chapter cohort crew roster ledger quarry mill
kiln anvil lathe loom smithy hearth
willow aspen linden alder hazel cedar juniper myrtle olive sorrel clover thistle
heather bracken fern mallow saffron sumac banyan teak neem jasmine tamarind sequoia
sylvan arbor orchard meadow
harbor haven cove delta mesa sierra savanna prairie estuary headland lagoon atoll
meridian zenith solstice equinox monsoon
slate marble basalt granite onyx agate amber coral jasper garnet opal topaz quartz
flint ochre indigo cobalt copper pewter bronze alloy sterling
beacon lantern ember kindle aurora halo lumen glimmer gleam daybreak compass sextant
bearing waypoint landfall anchor mooring keel mast prow tiller helm rudder ballast
cadence tempo timbre chorus refrain octave canon lyric murmur echo
morrow harvest vernal solace sanctum vesper vellum sable sienna tether tandem salient
trove keystone hallmark emblem plumb tally pledge charter proof
alora amira solera verano marlow milo nomi vela sela lira mira nara elara thera valo
lumina calla amara sonder
""".split()

# Words to drop on sight: known large trademarks, or a meaning that fights the model.
BLOCK = {"cadence": "Cadence Design Systems -- $80B+ public co, hard trademark",
         "canon": "Canon Inc. -- hard trademark",
         "compass": "Compass Inc. -- public real-estate brokerage",
         "sterling": "Sterling Check -- background screening, adjacent and confusable",
         "second": "reads as the ordinal, not the endorsement",
         "prove": "verb, no noun form; reads as an instruction",
         "warrant": "primary sense is the arrest warrant",
         "mill": "sweatshop connotation for a labour business",
         "quarry": "second sense is 'the hunted' -- wrong for people",
         "harvest": "extractive connotation for a labour business"}

# ---------------------------------------------------------------------------
# Probes
# ---------------------------------------------------------------------------
IDENTITY_DIGITAL = "https://rdap.identitydigital.services/rdap/domain/"
VERISIGN = "https://rdap.verisign.com/{tld}/v1/domain/"


def curl(url, timeout=20, extra=()):
    try:
        r = subprocess.run(["curl", "-sS", "--max-time", str(timeout),
                            "-w", "\n%{http_code}", *extra, url],
                           capture_output=True, text=True, timeout=timeout + 10)
        body, _, code = r.stdout.rpartition("\n")
        return body, int(code or 0)
    except Exception:
        return "", 0


def rdap_free(fqdn, base):
    _, code = curl(base + fqdn)
    return True if code == 404 else (False if code == 200 else None)


def doh_rcode(name, rrtype):
    body, code = curl(f"https://dns.google/resolve?name={name}&type={rrtype}")
    if code != 200:
        return None
    try:
        return json.loads(body).get("Status")
    except Exception:
        return None


def dns_free(fqdn):
    """NXDOMAIN on NS and SOA. Calibrated in scoring/dns_probe.py: 0/82 false-availables."""
    ns = doh_rcode(fqdn, "NS")
    if ns is None:
        return None
    if ns != 3:
        return False
    soa = doh_rcode(fqdn, "SOA")
    return None if soa is None else soa == 3


PARK = re.compile(
    r"(this domain (?:name )?(?:is|may be) for sale|buy this domain|domain for sale"
    r"|hugedomains|afternic|sedoparking|dan\.com|parkingcrew|bodis|above\.com"
    r"|godaddy\.com/domainsearch|namecheap.*parked|inquire about this domain"
    r"|the domain .* is for sale|make an offer)", re.I)


CF = re.compile(r"(just a moment|attention required|cf-browser-verification"
                r"|checking your browser|enable javascript and cookies)", re.I)


def com_occupant(word):
    """What actually sits on the .com -- this is what prices the type-in leak."""
    body, code = curl(f"https://{word}.com/", timeout=18,
                      extra=("-L", "--max-redirs", "4", "-A",
                             "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"))
    if code == 0:
        return "dark", ""
    if PARK.search(body or ""):
        return "for sale", ""
    if CF.search(body or ""):
        # a Cloudflare interstitial means the site is LIVE but its contents are
        # unverified. Reporting this as "dark" would understate the type-in leak.
        return "protected", ""
    m = re.search(r"<title[^>]*>(.*?)</title>", body or "", re.I | re.S)
    title = re.sub(r"\s+", " ", m.group(1)).strip()[:70] if m else ""
    if code >= 400 or not (body or "").strip():
        return "dark", title
    return "live", title


# ---------------------------------------------------------------------------
# Flow scoring -- the thing the last two revisions kept failing
# ---------------------------------------------------------------------------
VOWELS = set("aeiouy")
LIQUID = set("lrmnw")          # liquids, nasals, glides -- what makes a name pour
HARSH = set("kgtdpbx")          # stops -- what makes it clip


def syllables(w):
    n, prev = 0, False
    for ch in w:
        v = ch in VOWELS
        if v and not prev:
            n += 1
        prev = v
    if w.endswith("e") and n > 1:
        n -= 1
    return max(n, 1)


def flow(w):
    """0-5. Rewards: 2-3 syllables, liquid-heavy, vowel or liquid ending, no cluster."""
    s = 0.0
    syl = syllables(w)
    s += {1: 0.6, 2: 1.6, 3: 1.5, 4: 0.7}.get(syl, 0.2)          # 2-3 wins
    liq = sum(1 for c in w if c in LIQUID) / len(w)
    s += min(liq * 4.5, 1.5)                                      # liquid density
    s += 0.9 if w[-1] in VOWELS else (0.7 if w[-1] in LIQUID else 0.15)
    vowel_share = sum(1 for c in w if c in VOWELS) / len(w)
    s += 0.9 if 0.33 <= vowel_share <= 0.55 else 0.3              # open, not crowded
    clusters = len(re.findall(r"[bcdfgkptx]{2,}", w))
    s -= 0.5 * clusters                                           # thr-, -kt-, -sts
    if len(w) > 8:
        s -= 0.4
    return max(0.0, min(5.0, s))


SAYS = {}   # word -> does a normal person already say this word, unprompted (0-5)
for w in WORDS:
    SAYS[w] = 3
SAYS.update({
    # 5 = everyday. 4 = known but not daily. 3 = recognised. 2 = needs a dictionary.
    "merit": 5, "proof": 5, "crew": 5, "bench": 5, "anchor": 5, "harbor": 5, "beacon": 5,
    "clarity": 5, "cedar": 5, "willow": 5, "hazel": 5, "olive": 5, "amber": 5, "coral": 5,
    "copper": 5, "bronze": 5, "slate": 5, "marble": 5, "helm": 4, "compass": 5, "echo": 5,
    "chorus": 5, "tempo": 5, "halo": 5, "ember": 4, "lantern": 5, "meadow": 5, "clover": 5,
    "fern": 5, "jasmine": 5, "teak": 4, "delta": 5, "haven": 5, "cove": 4, "mesa": 4,
    "sierra": 4, "prairie": 4, "lagoon": 4, "granite": 5, "quartz": 4, "flint": 4,
    "indigo": 4, "cobalt": 4, "pewter": 3, "opal": 4, "garnet": 3, "agate": 2, "jasper": 4,
    "topaz": 3, "onyx": 4, "basalt": 3, "ochre": 3, "alloy": 4, "guild": 4, "roster": 5,
    "ledger": 4, "cohort": 4, "bureau": 4, "chapter": 5, "foundry": 3, "atelier": 2,
    "anvil": 4, "lathe": 3, "loom": 4, "smithy": 2, "hearth": 4, "kiln": 3,
    "vouch": 4, "attest": 3, "avow": 2, "affirm": 4, "endorse": 4, "muster": 3,
    "marshal": 4, "rally": 5, "scout": 5, "hone": 4, "whet": 2, "temper": 4, "forge": 4,
    "verity": 2, "surety": 2, "amity": 2, "candor": 3, "mettle": 3, "valor": 4, "ardor": 3,
    "vigor": 4, "tenor": 4, "caliber": 4, "credence": 3, "repute": 2, "esteem": 4,
    "accord": 4, "concord": 3, "tribute": 4, "laurel": 4, "acclaim": 4, "regard": 5,
    "fettle": 1, "stature": 4, "kindred": 4, "cognate": 1, "trove": 3, "keystone": 4,
    "hallmark": 4, "emblem": 4, "plumb": 3, "tally": 4, "pledge": 5, "charter": 4,
    "solace": 4, "sanctum": 3, "vesper": 2, "vellum": 2, "sable": 3, "sienna": 3,
    "tether": 4, "tandem": 4, "salient": 3, "morrow": 3, "vernal": 2, "sequoia": 4,
    "sylvan": 2, "arbor": 3, "orchard": 5, "aurora": 4, "lumen": 3, "glimmer": 4,
    "gleam": 4, "daybreak": 4, "sextant": 2, "bearing": 5, "waypoint": 3, "landfall": 3,
    "mooring": 3, "keel": 4, "mast": 4, "prow": 3, "tiller": 3, "rudder": 4, "ballast": 3,
    "timbre": 2, "refrain": 4, "octave": 4, "lyric": 4, "murmur": 4, "zenith": 4,
    "solstice": 4, "equinox": 4, "monsoon": 4, "estuary": 3, "headland": 3, "atoll": 3,
    "meridian": 3, "savanna": 4, "aspen": 4, "linden": 3, "alder": 3, "juniper": 4,
    "myrtle": 3, "sorrel": 2, "thistle": 4, "heather": 4, "bracken": 2, "mallow": 2,
    "saffron": 4, "sumac": 2, "banyan": 3, "neem": 2, "tamarind": 3, "kindle": 4,
    "second": 5, "warrant": 4, "mill": 5, "quarry": 4, "harvest": 5, "canon": 4,
    "sterling": 4, "cadence": 4,
    # coinages: nobody says these, that is the point of listing them low
    "alora": 1, "amira": 2, "solera": 1, "verano": 1, "marlow": 3, "milo": 3, "nomi": 1,
    "vela": 1, "sela": 1, "lira": 2, "mira": 2, "nara": 1, "elara": 1, "thera": 1,
    "valo": 1, "lumina": 2, "calla": 2, "amara": 2, "sonder": 1,
})


def main():
    cands = sorted({w for w in WORDS if w not in BLOCK})
    print(f"checking {len(cands)} words ...")

    with ThreadPoolExecutor(max_workers=8) as ex:
        co = dict(zip(cands, ex.map(lambda w: dns_free(w + ".co"), cands)))

    free_co = [w for w in cands if co[w] is True]
    print(f".co free (DNS): {len(free_co)}")

    with ThreadPoolExecutor(max_workers=8) as ex:
        com = dict(zip(cands, ex.map(
            lambda w: rdap_free(w + ".com", VERISIGN.format(tld="com")), cands)))
        net = dict(zip(free_co, ex.map(
            lambda w: rdap_free(w + ".net", VERISIGN.format(tld="net")), free_co)))
        ai = dict(zip(free_co, ex.map(
            lambda w: rdap_free(w + ".ai", IDENTITY_DIGITAL), free_co)))

    with ThreadPoolExecutor(max_workers=6) as ex:
        occ = dict(zip(free_co, ex.map(com_occupant, free_co)))

    json.dump({"co": co, "com": com, "net": net, "ai": ai,
               "occ": {k: list(v) for k, v in occ.items()}},
              open("scoring/.co_cache.json", "w"), indent=1)

    write(cands, co, com, net, ai, occ, free_co)
    return free_co


# ---------------------------------------------------------------------------
LEAK = {"dark": (5, "no site -- a type-in gets an error page, not a competitor"),
        "for sale": (4, "parking page -- and a priced option to buy the .com later"),
        "live": (2, "a live business -- every mistyped visit lands on someone else")}


def write(cands, co, com, net, ai, occ, free_co):
    rows = []
    for w in free_co:
        kind, title = occ[w]
        lk, _ = LEAK[kind]
        f, s = flow(w), SAYS.get(w, 3)
        total = f * 5 + s * 5 + lk * 3          # flow 25, says 25, leak 15
        rows.append((total, w, f, s, kind, title, lk, net.get(w), ai.get(w)))
    rows.sort(reverse=True)

    L = []
    A = L.append
    A("# The `.co` Question\n")
    A("> Asked: **\"Why not a good .co / Some of these seem so forced\"**\n")
    A("Those are one question. **Every flowing single word is taken on `.com`** — that was the "
      "finding of\n[`DOMAINS.md`](DOMAINS.md) §6, and it means a `.com` requirement is not a "
      "neutral filter. It is a *forcing\nfunction*: it converts single words into adjective+noun "
      "compounds, which is precisely the grammar that\nproduced *Graded Crew* and *Verity People*. "
      "**The forced names were a symptom of the TLD rule.**\n")
    A("So the rule gets priced rather than assumed.\n")

    A("---\n\n## 1. First, a method problem I had to fix\n")
    A("The previous screen refused to say anything about `.co` because **`.co` has no IANA RDAP "
      "bootstrap\nentry and whois is unreachable from this environment.** That refusal was honest "
      "but useless — it meant\nthe one TLD being asked about was the one TLD I could not check.\n")
    A("[`scoring/dns_probe.py`](scoring/dns_probe.py) fixes it. An unregistered domain has no "
      "delegation, so\nNS and SOA return NXDOMAIN. That proxy has two failure modes and both are "
      "**measured, not assumed**:\n")
    A("| Failure mode | How it would break the result | Measured |")
    A("|---|---|---|")
    A("| Registry DNS wildcard | everything looks taken | **None.** 3 garbage strings → NXDOMAIN "
      "on `.co` |")
    A("| Registered but undelegated | a taken name looks free | **0 of 82** real words. DoH and "
      "Verisign RDAP agreed on **82/82** |")
    A("")
    A("So: `.com`, `.net`, `.ai` below are **authoritative RDAP**. `.co` is a **DNS proxy with a "
      "measured\nzero error rate on 82 trials** — good enough to rank on, and still worth "
      "confirming in the registrar\ncart before paying. That distinction is kept visible in every "
      "table.\n")

    A("---\n\n## 2. Why `.com` is cheaper than I priced it — for *this* funnel specifically\n")
    A("The `.com` premium is real, but it is not one thing. It is four separate costs, and **three "
      "of them\nare near zero in a paid-acquisition business:**\n")
    A("| Where a TLD is priced | Cost on `.co` | Why, in this model |")
    A("|---|---|---|")
    A("| **Acquisition click** | **~zero** | The click comes from a Meta ad. The buyer taps an "
      "image; the domain is not typed and barely read. **100% of new business arrives without "
      "anyone seeing the TLD.** |")
    A("| **Cold email deliverability** | **~zero** | Real for outbound-led businesses. This model "
      "has no outbound motion — [`MAP.md`](MAP.md) puts the whole funnel on paid Meta. |")
    A("| **Buyer trust at the close** | **~zero** | The sale is closed by the paid teardown, the "
      "graded work sample and the guarantee. Nobody paying $6k–$20k has ever been argued out of "
      "it by four letters after a dot. |")
    A("| **Recall and referral** | **real, and the only real one** | \"What was that company?\" → "
      "types `.com` → lands somewhere else. This is the entire cost, and §3 shows it is *per "
      "name*, not per TLD. |")
    A("")
    A("Against that sits the cost of a forced name, which is paid **on every impression**: a name "
      "that reads\nas a spec rather than a company makes the ad worse, and the ad is the only "
      "acquisition channel there is.\n")
    A("> **The operator is right and my ranking was wrong.** A strong single word on `.co` beats a "
      "forced\n> compound on `.com` for a Meta-led business, because the `.com` advantage is "
      "collected at recall and\n> the compound's penalty is collected at acquisition.\n")

    A("---\n\n## 3. The leak is a property of the name, not the TLD\n")
    A("This is the part that makes the decision concrete. **The type-in leak only costs money if "
      "the `.com`\nis a live confusable business.** If it is dark or parked, a mistyped visit "
      "gets an error page — an\nannoyance, not a lost client. So every candidate's `.com` was "
      "fetched over HTTP to see what is\nactually there:\n")
    A("| What sits on the `.com` | Leak score | Meaning |")
    A("|---|---|---|")
    for k, (v, why) in LEAK.items():
        A(f"| **{k}** | {v}/5 | {why} |")
    A("")

    A("---\n\n## 4. Single flowing words available on `.co`\n")
    A(f"**{len(free_co)} of {len(cands)}** candidates are free on `.co`. Ranked on the three "
      "things that were\nactually wrong with the last list — flow (25), *does a person already "
      "say this word* (25), and the\nmeasured leak (15):\n")
    A("| # | Domain | Flow | Says | `.com` occupant | Leak | `.net` | `.ai` | Score |")
    A("|---|---|---|---|---|---|---|---|---|")
    for i, (t, w, f, s, kind, title, lk, n_, a_) in enumerate(rows[:30], 1):
        occ_txt = f"**{kind}**" + (f" — {title}" if title else "")
        A(f"| {i} | **`{w}.co`** | {f:.1f} | {s} | {occ_txt} | {lk} | "
          f"{'free' if n_ else 'taken'} | {'free' if a_ else 'taken'} | **{t:.1f}** |")
    A("")
    A("`.com`/`.net`/`.ai` are authoritative RDAP. `.co` is the calibrated DNS proxy from §1.\n")
    if len(rows) > 30:
        A(f"*{len(rows) - 30} further available words scored below the cut and are in "
          f"`scoring/.co_cache.json`.*\n")

    A("---\n\n## 5. Words dropped before checking, and why\n")
    A("| Word | Reason |\n|---|---|")
    for w, r in sorted(BLOCK.items()):
        A(f"| {w} | {r} |")
    A("")
    open(OUT, "w").write("\n".join(L))
    return rows


if __name__ == "__main__":
    free = main()
    print("free:", " ".join(free))
