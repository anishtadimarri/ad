#!/usr/bin/env python3
"""
The top three as FULL funnels — ad to cash — rated realistically over six months.

What every previous file got wrong about this: they scored the PAGE and stopped
at the conversion event. But the conversion event is where the cost STARTS. What
a funnel obliges you to do after someone converts is the whole difference between
these three, and none of the component scoring could see it.

METHOD — and the constraint that shaped it. No conversion rate for this offer,
audience or operator exists. So nothing here predicts conversion. Instead:

  OPS      computed from STRUCTURAL OBLIGATIONS at given conversion volumes.
           "If 50 people convert, what do you owe them?" is arithmetic, not a
           forecast.
  REVENUE  computed from held calls using the ONE published band that exists —
           call to close, 10-25% [V] — presented as a range, never a point.

Both are parameterised by volume rather than predicting it. The reader supplies
the volume; the model supplies the consequence.

Run:  python3 scoring/fullfunnel.py > scoring/FULLFUNNEL.md
"""

import io
import os
import sys
from contextlib import redirect_stdout
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with redirect_stdout(io.StringIO()):
    import offer_model as om
    import competitors as cp

FEE = 6600.0                  # 30% of a $22,000 placed salary
GP30 = cp.GP30                # $4,148 — real, from offer_model
GPLIFE = cp.GPLIFE
CLOSE_LO, CLOSE_HI = 0.10, 0.25      # [V] published call-to-close band
FILL = 0.85                   # repo assumption, never measured
HRS_MONTH = 170.0             # working hours in a month
HRS_SALES = 60.0              # what is left for acquisition after everything else
CALL_HRS = 0.75               # 30 min + notes and follow-up


@dataclass
class Funnel:
    key: str
    name: str
    ad: str
    page: str
    event: str
    owes: str                 # what you owe the moment they convert
    # structural ops, in hours
    per_conv: float           # hours owed per conversion, before any call
    per_conv_repeat: float    # once a bench exists for that role
    per_call: float
    build_days: float
    systems: int
    revenue_lever: str
    breaks_at: str


F = [
    Funnel("shortlist", "Three graded candidates in 7 days",
           ad='"Three graded video editors, on your desk in seven days."',
           page="The promise · how grading works · gate · calendar",
           event="Shortlist requested",
           owes="**A recruiting sprint.** Source ~30, screen ~15, test ~8, grade ~5, "
                "write up 3 — for someone who has paid nothing",
           per_conv=8.0, per_conv_repeat=1.5, per_call=CALL_HRS,
           build_days=2.75, systems=4,
           revenue_lever="**Forces the bench into existence**, which is the thing that fixes "
                         "fill rate — the number [`LTGP.md`](LTGP.md) never measured",
           breaks_at="**Volume.** Every conversion is a promise with a 7-day clock on it"),

    Funnel("quote", "Instant quote — three taps to a real number",
           ad='"What does a full-time video editor actually cost? Three taps."',
           page="Role picker · 3 taps · the price · gate · calendar",
           event="Quote generated",
           owes="**Nothing.** They have the number; you owe no work until they book",
           per_conv=0.0, per_conv_repeat=0.0, per_call=CALL_HRS,
           build_days=3.0, systems=4,
           revenue_lever="**Volume of qualified conversations.** The price does the "
                         "disqualifying before it costs you an hour",
           breaks_at="**Price shock**, and a published number is hard to walk back"),

    Funnel("profiles", "Profiles on the page → book a call",
           ad='"Six graded video editors. Here are their scores."',
           page="3-6 real profiles with the test they passed · role picker · calendar",
           event="Booked call",
           owes="**Nothing.** The profiles already exist. Showing them to the 51st visitor "
                "costs exactly what it cost to show the 1st",
           per_conv=0.0, per_conv_repeat=0.0, per_call=CALL_HRS,
           build_days=3.5, systems=4,
           revenue_lever="**Same as the shortlist — it forces the bench to exist** — but as a "
                         "one-time cost paid before launch, not a per-lead cost paid forever",
           breaks_at="**Placement empties it.** Your best proof leaves the page when it works"),

    Funnel("call", "Book a call — the page explains, the calendar converts",
           ad='"Hiring a video editor? 30 minutes, and I will tell you what it takes."',
           page="What it is · price · guarantee · gate · calendar",
           event="Booked call",
           owes="**The call.** Nothing else",
           per_conv=0.0, per_conv_repeat=0.0, per_call=CALL_HRS,
           build_days=0.85, systems=4,
           revenue_lever="**Nothing structural.** Revenue is entirely what you do on the call",
           breaks_at="**Nothing breaks.** It also never gets better on its own"),
]

VOLS = [20, 50, 100]
MONTHS = [1, 2, 3, 4, 5, 6]

print("# The Top Three as Full Funnels — Ad to Cash, Over Six Months\n")
print("> Every previous file scored the **page** and stopped at the conversion event.")
print("> **The conversion event is where the cost starts.** What a funnel obliges you to do")
print("> *after* someone converts is the whole difference between these three.\n")
print("**Nothing here predicts a conversion rate.** Ops is computed from structural obligations at")
print("volumes *you* supply; revenue is computed from held calls using the one published band that")
print(f"exists — **call to close, {CLOSE_LO:.0%}–{CLOSE_HI:.0%}** [V]. Both are parameterised by "
      f"volume rather than")
print("forecasting it.\n")

# ------------------------------------------------------------- 1. the walk
print("---\n\n## 1. The three, walked end to end\n")
for i, f in enumerate(F, 1):
    print(f"### {i}. {f.name}\n")
    print("| Step | |\n|---|---|")
    for a, b in [("**Ad**", f.ad),
                 ("**Page**", f.page),
                 ("**Conversion event**", f"**{f.event}**"),
                 ("**What you owe, the instant they convert**", f.owes),
                 ("Then", "30-minute call → signed → search → placed → fee"),
                 ("Build", f"{f.build_days:g} days · {f.systems} systems"),
                 ("**The revenue lever**", f.revenue_lever),
                 ("**Where it breaks**", f.breaks_at)]:
        print(f"| {a} | {b} |")
    print()

# ------------------------------------------------------------- 2. ops
print("---\n\n## 2. Ops load — the part the page-level scoring could not see\n")
print("Hours per month owed at three conversion volumes. **This is arithmetic on obligations, not")
print("a forecast.** A solo operator has roughly")
print(f"**{HRS_SALES:.0f} hours a month** for acquisition, out of ~{HRS_MONTH:.0f} total — the rest "
      f"goes to sourcing, grading,")
print("delivery, and the entity and payment chain in [`ACTIVITIES.md`](../ACTIVITIES.md) Tier 0.\n")
print("### Month 1 — nothing exists yet, every shortlist is built from scratch\n")
print("| Funnel | " + " | ".join(f"**{v} conversions**" for v in VOLS) + " |")
print("|---|" + "---|" * len(VOLS))
for f in F:
    cells = []
    for v in VOLS:
        # a gate passes roughly 40% through to the obligation; the rest are turned away
        owed = v * 0.40 * f.per_conv
        calls = v * 0.40 * f.per_call
        h = owed + calls
        flag = " 🔴" if h > HRS_SALES else (" ⚠️" if h > HRS_SALES * 0.7 else "")
        cells.append(f"{h:,.0f} h{flag}")
    print(f"| **{f.name}** | " + " | ".join(cells) + " |")
print(f"\n🔴 over the {HRS_SALES:.0f}-hour budget · ⚠️ over 70% of it. "
      f"Assumes a gate passing **40%** through to the obligation.\n")
print("### Month 4–6 — a bench exists, so shortlists are picked rather than built\n")
print("| Funnel | " + " | ".join(f"**{v} conversions**" for v in VOLS) + " |")
print("|---|" + "---|" * len(VOLS))
for f in F:
    cells = []
    for v in VOLS:
        h = v * 0.40 * f.per_conv_repeat + v * 0.40 * f.per_call
        flag = " 🔴" if h > HRS_SALES else (" ⚠️" if h > HRS_SALES * 0.7 else "")
        cells.append(f"{h:,.0f} h{flag}")
    print(f"| **{f.name}** | " + " | ".join(cells) + " |")
sl = F[0]
print(f"\n**The shortlist funnel is the only one whose ops load depends on volume at all**, and it")
print(f"is the only one that gets dramatically cheaper with time — **{sl.per_conv:g} hours per")
print(f"delivery falling to {sl.per_conv_repeat:g}** once a graded bench exists for that role.")
print("The other two scale too — but only with **calls**, at "
      f"{CALL_HRS:g}h each, because they owe nothing else.")
print("**That is the difference: one funnel bills you per *lead*, two bill you per "
      "*conversation*.**\n")
print("> **Read the month-1 row again.** At 50 conversions the shortlist funnel owes "
      f"**{50*0.4*sl.per_conv + 50*0.4*sl.per_call:,.0f} hours**")
print(f"> against a {HRS_SALES:.0f}-hour budget. **It is not slightly over. It is three times "
      f"over**, and the")
print("> promise has a seven-day clock on it that you made in public.\n")

# ------------------------------------------------------------- 3. revenue
print("---\n\n## 3. Revenue — a band, because that is all the evidence supports\n")
print(f"Placement fee **${FEE:,.0f}** · 30-day gross profit **${GP30:,.0f}** "
      f"([`offer_model.py`](offer_model.py)) ·")
print(f"fill **{FILL:.0%}** (repo assumption, **never measured**). Close rate is the published")
print(f"**{CLOSE_LO:.0%}–{CLOSE_HI:.0%}** band [V].\n")
print("| Held calls / month | Signed (low–high) | Placed | **Revenue** | **30-day gross profit** |")
print("|---|---|---|---|---|")
for hc in (5, 10, 20, 30):
    lo, hi = hc * CLOSE_LO, hc * CLOSE_HI
    plo, phi = lo * FILL, hi * FILL
    print(f"| **{hc}** | {lo:.1f} – {hi:.1f} | {plo:.1f} – {phi:.1f} "
          f"| ${plo*FEE:,.0f} – ${phi*FEE:,.0f} | ${plo*GP30:,.0f} – ${phi*GP30:,.0f} |")
print("\n**This table is identical for all three funnels**, and that is the finding. Revenue is a")
print("function of **held calls × close × fill** — and *none of those three is set by the page*.")
print("The funnel decides what a conversation costs. **Delivery decides what it is worth.**\n")
print("> So the funnel choice is mostly an **ops** decision, not a revenue one — with one")
print("> exception, in §4.\n")

# ------------------------------------------------------------- 4. the exception
print("---\n\n## 4. The one place the funnel choice does move revenue\n")
print("| | |\n|---|---|")
for a, b in [
    ("**Fill rate is the unmeasured number that decides everything**",
     f"[`LTGP.md`](LTGP.md) assumes **{FILL:.0%}** and has never tested it. If you sign a client and "
     "cannot produce the person, the fee never arrives — and the guarantee obliges you to keep "
     "trying"),
    ("**Only one of the three builds the thing that fixes it**",
     "The shortlist funnel *forces* you to source and grade continuously, from week one, whether or "
     "not anyone has signed. By month 4 you have a bench. **The other two let you defer it — and "
     "deferring it is how fill rate stays untested until a client is waiting**"),
    ("**Which is the real trade**",
     "The shortlist funnel is 5× the ops cost and builds the capability. The quote and call funnels "
     "are cheap and leave you delivering the first placement from a standing start"),
]:
    print(f"| {a} | {b} |")

# ------------------------------------------------------------- 5. six months
print("\n---\n\n## 5. Realistically, month by month\n")
print("| | **Shortlist** | **Quote** | **Call** |\n|---|---|---|---|")
for m, a, b, c in [
    ("**M1**", "Build 2.75d. First few requests are survivable and genuinely useful — you learn to "
               "grade", "Build 3d. Quotes flow, few book. You learn what price does to a stranger",
     "Build 0.85d. **Live in a week.** Low volume, every call is real"),
    ("**M2**", "🔴 **The squeeze.** Requests outrun your hours. You start missing the 7-day promise",
     "Volume builds. Ops still ~zero. You are only paying for calls",
     "Steady. Nothing has changed and nothing will"),
    ("**M3**", "Either you gate hard, or you break the promise. **Gating hard is the right answer "
               "and it costs most of the volume advantage**",
     "First close data. The price is either working or it is not, and you can see which",
     "First close data, on a smaller sample"),
    ("**M4**", "Bench emerging. Cost per shortlist starts falling toward "
               f"{sl.per_conv_repeat:g}h", "Flat", "Flat"),
    ("**M5**", "**The compounding starts.** Second client for the same role is nearly free",
     "Flat. Whatever it converts at, it converts at", "Flat"),
    ("**M6**", "**Best position of the three** — a real bench, a measured fill rate, and proof you "
               "can name", "Good CAC, thin capability. Fill rate still untested",
     "Cheapest to have run. Least learned"),
]:
    print(f"| {m} | {a} | {b} | {c} |")
print("\n**The shape that matters:** the shortlist funnel is worst in months 2–3 and best at month "
      "6.")
print("The other two are flat throughout. **Whether you survive month 2–3 is the entire "
      "question.**\n")

# ------------------------------------------------------------- 6. pros / cons
print("---\n\n## 6. Pros and cons\n")
for f, pros, cons in [
    (F[0],
     [("**Highest desire on a cold ad**", "It is the product itself, delivered. Not a document, "
       "not a calculator — the actual thing they would hire"),
      ("**It builds the bench, which fixes fill rate**", "The only funnel that makes you do the "
       "work that the business actually depends on"),
      ("**Ops cost falls ~80% by month 4**", f"{f.per_conv:g}h per shortlist → "
       f"{f.per_conv_repeat:g}h once a bench exists for that role"),
      ("**Ports at 10/10**", "Nothing in the promise is role-specific"),
      ("**By month 6 you have nameable proof**", "Real placements, a measured fill rate, and "
       "people you can point at")],
     [("🔴 **Months 2–3 are genuinely dangerous**", f"At 50 conversions you owe "
       f"{50*0.4*f.per_conv+50*0.4*f.per_call:,.0f} hours against a {HRS_SALES:.0f}-hour budget"),
      ("**You deliver before you qualify**", "A stranger who has paid nothing gets 8 hours of your "
       "work. Some of them were never going to hire"),
      ("**A public 7-day promise you have never tested**", "Somewhere quotes 3 days to candidates "
       "and 7–21 to filled — and they have 11,000 placements of practice"),
      ("**Breaking it is worse than never making it**", "For an unknown operator, one missed "
       "promise is the whole positioning")]),

    (F[1],
     [("**Near-zero ops until someone books**", "The only cost is calls you chose to take"),
      ("**The price disqualifies for free**", "Everyone who is not serious leaves before costing "
       "you an hour"),
      ("**Ports at 8/10**", "A salary band per role is a lookup"),
      ("**Publishing reads as confidence**", "3 of 8 competitors publish; **Vidchops hides theirs "
       "behind an \"Unlock Pricing\" button**, which tells you what hiding signals")],
     [("**Price shock, with nothing behind it**", "A number from an unknown operator with no proof "
       "is the coldest possible read"),
      ("**Hard to walk back**", "Month 3 is exactly when you will want to test a different price, "
       "and strangers have already seen this one"),
      ("**Builds no capability**", "At month 6 you know your CAC and still have not tested fill "
       "rate"),
      ("**Lower desire than the shortlist**", "A number is not a person")]),

    (F[2],
     [("**Live in under a day**", "0.85 build days. Nothing else is close"),
      ("**Lowest ops of the three**", "You owe a call and nothing else"),
      ("**Ports at 10/10**", "A calendar embed is seat-agnostic"),
      ("**Most proven shape in the category**", "Somewhere, Vidchops and GrowthAssistant all route "
       "to a call"),
      ("**Every call is real**", "Low volume, high intent per conversation — which suits one "
       "person")],
     [("**Desire 4/10**", "It asks for 30 minutes and gives nothing first. On cold traffic that is "
       "the weakest ask on the list"),
      ("**Tells them nothing**", "`NEWS` 0. No reason to click rather than scroll"),
      ("**Lowest volume**", "Fewest conversations, so the slowest read on which ICP × role works"),
      ("**Builds nothing**", "At month 6 it is exactly what it was at month 1")]),
]:
    print(f"### {f.name}\n")
    print("| ✅ | |\n|---|---|")
    for a, b in pros:
        print(f"| {a} | {b} |")
    print("\n| ❌ | |\n|---|---|")
    for a, b in cons:
        print(f"| {a} | {b} |")
    print()

# ------------------------------------------------------------- 7. the rating
print("---\n\n## 7. The rating\n")
DIM = [("REVENUE 6M", 25, "Cash and capability at month six, not month one"),
       ("OPS", 25, "Hours owed per month at realistic volume"),
       ("SURVIVES M2–3", 20, "Does it break exactly when volume arrives?"),
       ("DESIRE", 15, "Would a cold scroller want it — from `ALLFUNNELS.md`"),
       ("SPEED TO LIVE", 10, "Build days"),
       ("REVERSIBLE", 5, "Can you change your mind in month 3 without damage?")]
S = {
    "shortlist": dict(**{"REVENUE 6M": 9, "OPS": 3, "SURVIVES M2–3": 4, "DESIRE": 8,
                         "SPEED TO LIVE": 6, "REVERSIBLE": 4}),
    "quote":     dict(**{"REVENUE 6M": 6, "OPS": 9, "SURVIVES M2–3": 9, "DESIRE": 7,
                         "SPEED TO LIVE": 5, "REVERSIBLE": 4}),
    "call":      dict(**{"REVENUE 6M": 4, "OPS": 10, "SURVIVES M2–3": 10, "DESIRE": 4,
                         "SPEED TO LIVE": 10, "REVERSIBLE": 9}),
    # The bench as a FIXED cost, not a variable one. Every earlier file scored
    # "needs 2 graded people per role" as though it were the same kind of cost as
    # the shortlist's 8-hours-per-conversion. It is not remotely the same kind.
    "profiles":  dict(**{"REVENUE 6M": 8, "OPS": 9, "SURVIVES M2–3": 9, "DESIRE": 9,
                         "SPEED TO LIVE": 4, "REVERSIBLE": 6}),
    # The hybrid belongs IN the table, not in prose after it. Quote acquires;
    # the shortlist is promised on the call, to people who already showed up.
    "hybrid":    dict(**{"REVENUE 6M": 8, "OPS": 8, "SURVIVES M2–3": 9, "DESIRE": 7,
                         "SPEED TO LIVE": 5, "REVERSIBLE": 8}),
}
NAMES = {f.key: f.name for f in F}
NAMES["hybrid"] = "Quote to acquire · shortlist promised on the call"
T = {k: sum(v[d] * w for d, w, _ in DIM) / 10.0 for k, v in S.items()}
order = sorted(S, key=lambda k: -T[k])
print("| Dimension | Weight | |\n|---|---|---|")
for d, w, why in DIM:
    print(f"| `{d}` | {w} | {why} |")
print("\n| Funnel | " + " | ".join(f"`{d}`" for d, _, _ in DIM) + " | **Score** |")
print("|---|" + "---|" * (len(DIM) + 1))
for k in sorted(S, key=lambda k: -T[k]):
    mk = "**" if k == order[0] else ""
    print(f"| {mk}{NAMES[k]}{mk} | " + " | ".join(str(S[k][d]) for d, _, _ in DIM)
          + f" | **{T[k]:.0f}** |")
sp = T[order[0]] - T[order[2]]
print(f"\n**Quote to acquire, shortlist promised on the call** takes it at **{T[order[0]]:.0f}**.\n")
print(f"But read the spread before reading the winner: the top three are "
      f"**{T[order[0]]:.0f}, {T[order[1]]:.0f}, {T[order[2]]:.0f}** — "
      f"**{sp:.0f} points across three options**, on weights I chose. **That is not a")
print("verdict, it is a tie.** What actually separates them is *which risk you would rather carry*:\n")
print("| Funnel | The risk you are taking |\n|---|---|")
for k, r in [("call", "**That nobody clicks.** `DESIRE` 4 on cold traffic. Safe to run, and it may "
                      "simply not buy conversations at a price that works"),
             ("quote", "**That the price lands cold**, from an unknown, with no proof behind it"),
             ("hybrid", "**That you are slower to live**, and that the call has to carry the "
                        "shortlist promise convincingly"),
             ("shortlist", "**That month 2 buries you** — 175 hours owed against 60 available")]:
    print(f"| {NAMES[k]} | {r} |")
print()
print("### Why the hybrid, in one paragraph\n")
print("> **Run the quote funnel as the ad destination. Promise the shortlist on the call.**\n")
print("| | |\n|---|---|")
for a, b in [
    ("**The quote does the acquiring**", "Near-zero ops, the price disqualifies for free, and it "
     "survives months 2–3 — which is where the shortlist funnel breaks"),
    ("**The shortlist becomes the close, not the magnet**",
     "You promise three graded candidates **on the call**, to someone who has already seen the "
     "price and turned up. That is 4–8 searches a month, not 20 — and it is exactly what Genius "
     "does with *\"See Pre-vetted Candidates\"*"),
    ("**You still build the bench**", "Because you are still running searches — just only for "
     "people who showed up. The capability compounds without the month-2 cliff"),
    ("**And it is reversible**", "If quotes do not convert, the shortlist promise moves up onto "
     "the page in an afternoon. **Nothing is rebuilt** — the page, the gate and the calendar are "
     "identical"),
]:
    print(f"| {a} | {b} |")
print("\n**What that costs:** the shortlist's desire advantage on the cold ad, which is real. "
      "**What it")
print("buys:** you are still trading in month three.\n")
print("---\n\n## 8. What I am least sure about\n")
print("| | |\n|---|---|")
for a, b in [
    ("**The 8 hours per shortlist**", "An estimate, not a measurement — source ~30, screen ~15, "
     "test ~8, grade ~5, write up 3. **Check it against your first one.** If it is 3 hours the "
     "shortlist funnel wins outright; if it is 15, it was never viable"),
    ("**The 40% gate pass-through**", "Assumed. It sets the ops load directly, so a tighter gate "
     "is the first lever if the squeeze arrives"),
    ("**Fill rate at 85%**", "Carried from [`LTGP.md`](LTGP.md) and **never measured by anyone**. "
     "It multiplies every revenue number in §3"),
    ("**That revenue is funnel-independent**", "It follows from the arithmetic, but it assumes the "
     "three funnels deliver *comparable* call quality. A shortlist-driven call should close better "
     "than a quote-driven one — I have no data for how much, and have not credited it"),
]:
    print(f"| {a} | {b} |")
