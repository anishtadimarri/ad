#!/usr/bin/env python3
"""
Calibrate a DNS-based availability probe so that .co can be checked at all.

Why this file exists: `.co` and `.io` have no IANA RDAP bootstrap entry, and whois
is unreachable from this environment. The previous domain screen therefore refused
to make any claim about .co — which is exactly the TLD the operator is asking about.

The only reachable authority is DNS-over-HTTPS. An unregistered domain has no
delegation, so NS/SOA return NXDOMAIN. A *registered* domain normally has NS records
(registrar parking pages count). So NXDOMAIN is a candidate proxy for "unregistered".

That proxy has two failure modes, and both are measurable rather than assumed:

  FALSE AVAILABLE  registered but undelegated (owner removed nameservers) -> NXDOMAIN
  FALSE TAKEN      registry DNS wildcard -> everything resolves

This script measures both against Verisign RDAP on .com, where RDAP *is* authoritative,
then tests .co for a wildcard. The measured error rate is the error bar that gets
attached to every .co claim downstream.

Run:  python3 scoring/dns_probe.py
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

DOH = "https://dns.google/resolve"


def _curl(url, timeout=25):
    try:
        r = subprocess.run(
            ["curl", "-sS", "--max-time", str(timeout), "-w", "\n%{http_code}", url],
            capture_output=True, text=True, timeout=timeout + 10)
        parts = r.stdout.rsplit("\n", 1)
        if len(parts) != 2:
            return None, 0
        return parts[0], int(parts[1] or 0)
    except Exception:
        return None, 0


def doh_status(name, rrtype="NS"):
    """Return DNS rcode: 0 = NOERROR (delegated), 3 = NXDOMAIN, None = probe failed."""
    body, code = _curl(f"{DOH}?name={name}&type={rrtype}")
    if code != 200 or not body:
        return None
    try:
        return json.loads(body).get("Status")
    except Exception:
        return None


def doh_free(name):
    """NXDOMAIN on both NS and SOA. Two records so one flaky answer cannot decide."""
    ns = doh_status(name, "NS")
    if ns is None:
        return None
    if ns != 3:
        return False
    soa = doh_status(name, "SOA")
    if soa is None:
        return None
    return soa == 3


def rdap_free(name, tld="com"):
    """Verisign RDAP. 404 = unregistered, 200 = registered. Authoritative for .com/.net."""
    _, code = _curl(f"https://rdap.verisign.com/{tld}/v1/domain/{name}")
    if code == 404:
        return True
    if code == 200:
        return False
    return None


# --- calibration set: real words, the population we actually care about ---------
CAL = """verity kindred surety amity candor merit mettle vouch muster fathom
willow aspen linden cedar juniper sable onyx cobalt slate marble amber coral
harbor anchor beacon lantern ember orchard meadow quarry alloy copper
guild foundry atelier bench crew cohort roster bureau chapter circle council
poise rally tenor vigil zeal ardor grit nerve clarity cadence
lumen halo lever ashby oyster papaya gusto lattice greenhouse rippling
salient tandem tether tessera vellum vesper virtue warrant wend whetstone
proof pledge warrant charter emblem hallmark keystone plumb tally trove""".split()

GARBAGE = ["qxzvwmplk8734", "zzqqjjxxvv7712", "brmnpltkzq0093"]


def main():
    print("=== 1. Is there a .co DNS wildcard? (would make DoH useless) ===")
    for g in GARBAGE:
        print(f"  {g}.co  NS rcode = {doh_status(g + '.co', 'NS')}   "
              f"{g}.com NS rcode = {doh_status(g + '.com', 'NS')}   (3 = NXDOMAIN)")

    print("\n=== 2. DoH vs Verisign RDAP on .com, same word list ===")
    words = sorted(set(CAL))
    with ThreadPoolExecutor(max_workers=8) as ex:
        doh = list(ex.map(lambda w: doh_free(w + ".com"), words))
    with ThreadPoolExecutor(max_workers=8) as ex:
        rd = list(ex.map(lambda w: rdap_free(w + ".com"), words))

    agree = fa = ft = skip = 0
    fa_list, ft_list = [], []
    for w, d, r in zip(words, doh, rd):
        if d is None or r is None:
            skip += 1
            continue
        if d == r:
            agree += 1
        elif d and not r:
            fa += 1
            fa_list.append(w)
        else:
            ft += 1
            ft_list.append(w)

    n = agree + fa + ft
    print(f"  compared        : {n} words ({skip} unresolved probes)")
    print(f"  agree           : {agree}  ({agree/n*100:.1f}%)" if n else "  no data")
    print(f"  FALSE AVAILABLE : {fa}  -> {fa_list}")
    print(f"  FALSE TAKEN     : {ft}  -> {ft_list}")
    if n:
        print(f"\n  DoH-says-free precision on this set: "
              f"{(0 if not (fa + sum(1 for d,r in zip(doh,rd) if d and r)) else 0)}", end="")
        free_doh = [w for w, d in zip(words, doh) if d]
        really = [w for w, d, r in zip(words, doh, rd) if d and r]
        print(f"\n  of {len(free_doh)} words DoH called free, {len(really)} really were free "
              f"per RDAP")
    return 0


if __name__ == "__main__":
    sys.exit(main())
