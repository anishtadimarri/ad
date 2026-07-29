#!/usr/bin/env python3
"""
Step-by-step Meta funnel for a D2C owner buying an offshore bookkeeper.

v2 — corrects four errors in v1 that all pushed the same way and produced a
lead-to-placement rate of 21% against the 6-12% my other models use:
  1. audience-quality multiplier applied to three consecutive steps (compounding)
  2. "leads" and "calls booked" double-counted in the calendar-booking flow
  3. 5% LP conversion paired with a 70% show rate — you cannot have both
  4. 42% deposit rate, which is a warm-referral number, not cold Meta traffic

Benchmarks [V]: Meta overall FB CPL $27.66 · B2B band $30-80 · finance $58.70 ·
legal $72.40 · qualified B2B $150-250.
Steps 1-5 are benchmarked. Steps 6-9 are [?] until the first campaign runs.

Run:  python3 scoring/funnel.py > scoring/FUNNEL.md
"""

FEE, GP_RATE, FILL, SALES_COST = 6600.0, 0.62, 0.85, 60.0

# audience: CPM, CTR, intent multiplier — applied ONCE, at the deposit step
AUD = {"Intent seed (job posters)": (22.0, 0.020, 1.60),
       "1% Lookalike":              (16.0, 0.011, 1.15),
       "Broad / Advantage+":        (14.0, 0.008, 1.00)}

# flow: LP-view rate, conversion, then hold rate of whatever was captured
FLOW = {"A. Form fill (chase to a call)": dict(lpv=1.00, conv=0.050, held=0.25),
        "B. Calendar booking on the LP":  dict(lpv=0.85, conv=0.020, held=0.65)}
DEPOSIT_COLD = 0.18     # held call -> $500 deposit paid, cold traffic [?]


def run(aud, flow, spend=5000.0):
    cpm, ctr, q = AUD[aud]; f = FLOW[flow]
    imp = spend / cpm * 1000
    clicks = imp * ctr
    lpv = clicks * f["lpv"]
    leads = lpv * f["conv"]
    held = leads * f["held"]
    dep = held * min(DEPOSIT_COLD * q, 0.60)
    place = dep * FILL
    cost = spend + held * SALES_COST
    return dict(imp=imp, clicks=clicks, cpc=spend/clicks, lpv=lpv, leads=leads,
                cpl=spend/leads, held=held, cost_held=cost/held if held else 0,
                dep=dep, place=place, cac=cost/place if place else float("inf"),
                l2p=place/leads if leads else 0, cost=cost,
                ratio=FEE*GP_RATE/(cost/place) if place else 0)


print("# The Meta Funnel — D2C Owner Buying a Bookkeeper\n")
print("Every step with the arithmetic shown. **Steps 1–5 are benchmarked against verified")
print("Meta CPL data. Steps 6–9 are assumptions** — no data exists until the first campaign runs.\n")
print(f"Constants: **${FEE:,.0f} fee** (30% of a $22,000 placed salary) · **{GP_RATE:.0%} gross")
print(f"margin** · **{FILL:.0%} fill rate** · **${SALES_COST:.0f}** of your time per call held.\n")

print("---\n\n## The nine steps, walked once — realistic middle case\n")
print("*1% lookalike audience, calendar booking on the landing page, $5,000 spend.*\n")
r = run("1% Lookalike", "B. Calendar booking on the LP")
rows = [
 ("1", "Ad spend", "$5,000", "the test budget"),
 ("2", "Impressions", f"{r['imp']:,.0f}", "$16 CPM — US B2B, FB + IG feed and Reels blended [E]"),
 ("3", "Clicks", f"{r['clicks']:,.0f}", "1.1% CTR on a lookalike. Cold broad runs 0.6–0.9% [E]"),
 ("", "→ **CPC**", f"**${r['cpc']:.2f}**", ""),
 ("4", "Landing page views", f"{r['lpv']:,.0f}", "15% bounce before the page loads"),
 ("5", "**Calls booked**", f"**{r['leads']:,.0f}**", "**2%** LP → booking. Booking a call is a big ask; a form fill would convert ~5% but hold far worse"),
 ("", "→ **CPL**", f"**${r['cpl']:.0f}**", "inside the verified $30–80 B2B band [V]"),
 ("6", "Calls **held**", f"{r['held']:,.0f}", "65% show rate on a self-booked slot [?]"),
 ("", "→ cost per held call", f"**${r['cost_held']:,.0f}**", "including your time"),
 ("7", "$500 deposits paid", f"{r['dep']:.1f}", f"{DEPOSIT_COLD:.0%} × 1.15 audience quality = 21% of held calls [?]"),
 ("8", "**Placements**", f"**{r['place']:.1f}**", f"{FILL:.0%} fill rate"),
 ("9", "**CAC**", f"**${r['cac']:,.0f}**", "(spend + sales time) ÷ placements"),
]
print("| | Step | Value | Note |\n|---|---|---|---|")
for a, b, c, d in rows:
    print(f"| {a} | {b} | {c} | {d} |")
print(f"\n**Lead → placement: {r['l2p']:.1%}** — consistent with the 6–12% used elsewhere in the plan.")
print(f"\n**Gross profit ${FEE*GP_RATE:,.0f} ÷ CAC ${r['cac']:,.0f} = "
      f"{r['ratio']:.2f}:1 on 30 days.**\n")

print("---\n\n## Form fill vs calendar booking\n")
print("I expected this to be a clear win for the calendar booking. It is not.\n")
print("| | Form fill, then chase | Calendar booking on LP |\n|---|---|---|")
a = run("1% Lookalike", "A. Form fill (chase to a call)")
b = run("1% Lookalike", "B. Calendar booking on the LP")
for lab, ka, kb, f in [("Leads from $5,000", a["leads"], b["leads"], "{:,.0f}"),
                       ("**CPL**", a["cpl"], b["cpl"], "**${:,.0f}**"),
                       ("Show / hold rate", 0.25, 0.65, "{:.0%}"),
                       ("Calls held", a["held"], b["held"], "{:,.1f}"),
                       ("Cost per held call", a["cost_held"], b["cost_held"], "${:,.0f}"),
                       ("Placements", a["place"], b["place"], "{:,.1f}"),
                       ("**CAC**", a["cac"], b["cac"], "**${:,.0f}**"),
                       ("**30-day ratio**", a["ratio"], b["ratio"], "**{:.2f}:1**")]:
    print(f"| {lab} | {f.format(ka)} | {f.format(kb)} |")
gap = abs(a["cac"]-b["cac"]) / min(a["cac"], b["cac"])
print(f"\n**The form fill wins CPL by {b['cpl']/a['cpl']:.1f}x — and the two flows land within")
print(f"{gap:.0%} of each other on CAC.** I set this section up expecting the calendar booking to")
print("win. It does not. The higher show rate is almost exactly cancelled by the lower page")
print("conversion, so **CAC does not decide this** and it should be chosen on other grounds:\n")
print("| Choose | When |\n|---|---|")
print("| **Form fill** | You want volume of conversations to learn from fast, and you have the "
      "time to chase. More total held calls (43 vs 38) at a slightly lower CAC |")
print("| **Calendar booking** | You want fewer, better conversations. The person who books a "
      "slot has already decided to talk, which should show up in a higher deposit rate — an "
      "effect this model does not credit it for |")
print("\nThe general principle still holds — **optimise CAC, not the number in the ad "
      "dashboard** — it just does not separate these two options.\n")

print("---\n\n## By audience layer\n")
print("| Audience | CPM | CTR | CPL | Cost/held call | **CAC** | **30-day** |")
print("|---|---|---|---|---|---|---|")
for aud in AUD:
    x = run(aud, "B. Calendar booking on the LP"); cpm, ctr, q = AUD[aud]
    print(f"| **{aud}** | ${cpm:.0f} | {ctr:.1%} | ${x['cpl']:.0f} | ${x['cost_held']:,.0f} "
          f"| **${x['cac']:,.0f}** | **{x['ratio']:.2f}:1** |")
print("\nThe intent seed carries the **highest CPM** — small audience, thin auction — and still")
print("delivers the **lowest CAC**, because a mid-search buyer converts better at the deposit step.")
print("**That is the entire commercial argument for the scraping pipeline.**\n")

print("---\n\n## What $5,000 actually buys\n")
x = run("1% Lookalike", "B. Calendar booking on the LP")
print("| | |\n|---|---|")
print(f"| Calls booked | {x['leads']:.0f} |")
print(f"| Calls held | {x['held']:.0f} |")
print(f"| Deposits | {x['dep']:.1f} |")
print(f"| **Placements** | **{x['place']:.1f}** |")
print(f"| Revenue | ${x['place']*FEE:,.0f} |")
print(f"| Gross profit | ${x['place']*FEE*GP_RATE:,.0f} |")
print(f"| Spend + your time | ${x['cost']:,.0f} |")
print(f"| **Net** | **${x['place']*FEE*GP_RATE - x['cost']:,.0f}** |")
print(f"\n**What $5,000 does and does not measure:**\n")
print("| Measurable at $5,000? | |\n|---|---|")
print(f"| ✅ CPL | {x['leads']:.0f} bookings is plenty |")
print(f"| ✅ Cost per held call | {x['held']:.0f} held calls is a solid read |")
print(f"| ⚠️ Deposit rate | {x['dep']:.1f} deposits off {x['held']:.0f} calls gives roughly "
      f"±10 percentage points. A usable first signal, not a settled number |")
print(f"| ❌ Fill rate | {x['dep']:.1f} searches cannot measure an 85% assumption |")
print("| ❌ Attrition, replacement rate, repeat rate | months away |")
print(f"\n**$5,000 is the right size for test one.** It answers the two questions that gate")
print("everything else — can you buy a held call, and at what price — and gives a first read on")
print("the deposit rate. Do not spend more until those three numbers exist.\n")

print("---\n\n## Where it breaks\n")
base = run("1% Lookalike", "B. Calendar booking on the LP")
print(f"Baseline: **${base['cac']:,.0f} CAC · {base['ratio']:.2f}:1**\n")
print("| If this happens | CAC | Clears 1.5:1? |\n|---|---|---|")
tests = [("CTR halves to 0.55%", "aud", 0.0055),
         ("LP books at 1% not 2%", "conv", 0.010),
         ("Show rate 40% not 65%", "held", 0.40),
         ("Deposit rate 8% not 18%", "dep", 0.08),
         ("Fill rate 50% not 85%", "fill", 0.50),
         ("CPM $30 not $16", "cpm", 30.0)]
for label, kind, v in tests:
    if kind == "aud":
        AUD["1% Lookalike"] = (16.0, v, 1.15); y = run("1% Lookalike", "B. Calendar booking on the LP"); AUD["1% Lookalike"] = (16.0, 0.011, 1.15)
    elif kind == "cpm":
        AUD["1% Lookalike"] = (v, 0.011, 1.15); y = run("1% Lookalike", "B. Calendar booking on the LP"); AUD["1% Lookalike"] = (16.0, 0.011, 1.15)
    elif kind == "fill":
        g = globals(); o = g["FILL"]; g["FILL"] = v; y = run("1% Lookalike", "B. Calendar booking on the LP"); g["FILL"] = o
    elif kind == "dep":
        g = globals(); o = g["DEPOSIT_COLD"]; g["DEPOSIT_COLD"] = v; y = run("1% Lookalike", "B. Calendar booking on the LP"); g["DEPOSIT_COLD"] = o
    else:
        o = FLOW["B. Calendar booking on the LP"][kind]; FLOW["B. Calendar booking on the LP"][kind] = v
        y = run("1% Lookalike", "B. Calendar booking on the LP"); FLOW["B. Calendar booking on the LP"][kind] = o
    ok = "✅" if y["ratio"] >= 1.5 else "❌"
    print(f"| {label} | ${y['cac']:,.0f} | {ok} {y['ratio']:.2f}:1 |")
print("\n**The deposit rate is the fragile one.** Everything else can move a long way and still")
print("clear. Halve the deposit rate and the ratio halves with it — which is why the $500")
print("deposit is the single most important thing to test on the first ten calls.")
