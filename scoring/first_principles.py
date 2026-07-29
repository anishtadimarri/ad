#!/usr/bin/env python3
"""
First-principles rebuild: score VERTICALS and SKILLS independently, then score
the INTERACTION, then map.

Why separate them: earlier models mixed buyer properties with work properties
in one score, so the answer moved every time a new consideration was added.
A vertical has properties whatever you place into it. A skill has properties
wherever you place it. And some things only exist at the intersection.

Run:  python3 scoring/first_principles.py > scoring/FIRST-PRINCIPLES.md
"""

# ============================================================ VERTICAL CRITERIA
# Properties of the BUYER. True regardless of which role you place.
VDIM = [
    ("REMOTE", 15, "Already employs remote/offshore staff",
     "5=offshore is normal here  3=growing  1=would need converting. GATE at <4"),
    ("META", 15, "Targetable on Meta ads",
     "Can an ad audience actually be built? 5=strong interest/behaviour signals AND the buyer "
     "lives on Facebook/IG  3=reachable with broad targeting + a self-qualifying hook  "
     "1=the buyer is on LinkedIn, not Meta"),
    ("DECIDE", 12, "Single decision-maker", "5=owner decides today  3=owner+1  1=committee"),
    ("LIST", 10, "Named list exists for cold outbound",
     "5=public/scrapeable register (BuiltWith, Storeleads, SEC ADV, Clutch)  1=1:1 research"),
    ("AFFORD", 9, "Can write a $6k fee without thinking",
     "5=comfortable  3=needs justifying  1=it is a real decision"),
    ("STACK", 11, "One software stack across the vertical",
     "5=same stack every client  3=2-3 systems  1=bespoke"),
    ("EORNEED", 7, "Needs us to employ the person",
     "5=no entity, no appetite, no alternative but Deel"),
    ("COUNT", 7, "Businesses in the hiring band",
     "5=>100k  4=50-100k  3=20-50k  2=10-20k  1=<10k"),
    ("SEATS", 5, "Buys more than one seat over time", "5=builds a team  1=one and done"),
    ("WHITE", 4, "No vertical-specialist incumbent", "5=open  0=dominated"),
    ("CLEAN", 5, "No licensing / regulatory friction",
     "5=none  3=data-handling only  1=UPL, HIPAA, state licensing. Re-added after being "
     "dropped in the META revision — it is exactly what bites on legal and medical"),
]
# vertical: REMOTE META DECIDE LIST AFFORD STACK EORNEED COUNT SEATS WHITE
# META is the new dimension. It is NOT the same as LIST — Storeleads gives a named
# list of Shopify merchants but not a Meta audience, and trucking owners live on
# Facebook while MSP and SaaS buyers live on LinkedIn.
VERTICALS = {
 "E-comm / DTC":        (5,5,5,5,5,5,4,3,3,3,5),
 "Marketing agency":    (5,4,5,4,4,4,4,3,4,4,5),
 "SaaS":                (5,2,3,4,5,5,4,2,4,4,5),
 "Staffing agency":     (5,2,5,4,4,5,4,2,4,4,4),
 "MSP / IT services":   (5,2,5,4,4,5,4,2,4,4,5),
 "Freight / trucking":  (5,4,5,4,2,4,4,3,5,2,4),
 "Insurance agency":    (4,3,4,5,4,5,4,3,4,1,4),
 "PI law firm":         (4,4,5,4,5,4,4,3,3,4,2),
 "Medical practice":    (4,4,4,4,3,4,4,5,4,1,2),
 "Property mgmt":       (4,3,4,4,3,5,4,4,4,3,4),
 "Home services":       (3,5,5,4,3,5,4,4,3,3,4),
 "Dental / DSO":        (3,4,5,4,3,5,4,4,4,2,3),
}

# =============================================================== SKILL CRITERIA
# Properties of the WORK. True wherever you place it.
SDIM = [
    ("HAPPY", 24, "Client is more likely happy than not",
     "Composite, and the heaviest criterion: objective output nobody argues about + visible win "
     "inside 2 weeks + failure is recoverable + output does not depend on the client's team + "
     "an SOP already exists to plug into. 5=all five  1=none"),
    ("ASYNC", 14, "Works fully async",
     "5=no live overlap needed at all  4=one call a week  3=daily overlap  1=US-hours voice. "
     "GATE at <4"),
    ("RETAIN", 14, "Retention",
     "no freelance escape path · weak local counter-bid · year-round · visible career ladder"),
    ("VALUE", 13, "True value created for BOTH sides",
     "Anchored on Somewhere's PUBLISHED savings %: 5=>70% (accountant 78%, bookkeeper 75%) "
     "4=55-70% (Head of Finance 69%, CFO 55%) 3=40-55% 2=30-40% (ops/admin floor) 1=<30%"),
    ("AIDUR", 11, "AI-durable over 5 years",
     "5=judgment/liability-bearing  3=partly exposed  1=being eaten now"),
    ("SUPPLY", 10, "Indian supply already doing this for US clients", "5=thousands  1=must create"),
    ("TRAIN", 8, "Trainable — small delta from adjacent supply", "5=<1wk  3=2wk  1=months"),
    ("FEE", 6, "Fee size", "5=$40k+ placed  3=$20-28k  1=<$14k"),
]
# skill: HAPPY ASYNC RETAIN VALUE AIDUR SUPPLY TRAIN FEE
# VALUE anchored on Somewhere's published savings %: accountant 78, bookkeeper up to 75,
# EA 76, Head of Finance 69, C-suite 53-60, SWE 54, ops/admin/sales floor 30-48.
SKILLS = {
 "AR & Collections":            (5,4,4,4,3,4,5,3),
 "AP & Invoice Processing":     (5,5,4,4,2,5,5,2),
 "Bookkeeping / reconciliation":(5,5,3,5,2,5,4,2),
 "Ledger & Close (senior)":     (4,4,3,5,3,4,2,5),
 "Financial reporting pack":    (4,5,4,4,3,3,4,4),
 "Payroll processing":          (4,5,5,4,3,3,3,3),
 "Reporting & Analytics (BI)":  (4,5,4,4,3,3,4,4),
 "Paid Media Operations":       (4,5,2,4,3,4,5,4),
 "Email / Lifecycle Ops":       (4,5,4,3,3,3,4,3),
 "Compliance & Document Ops":   (4,5,4,3,5,3,3,3),
 "CRM / RevOps data hygiene":   (4,5,3,2,2,4,5,2),
 "Customer support (email)":    (3,3,2,4,2,5,5,1),
 "Fractional CFO / Head of Fin":(3,4,3,4,4,3,2,5),
}

# ========================================================= INTERACTION CRITERIA
# Things that exist ONLY at the intersection. Derived from two sparse inputs
# per vertical rather than hand-scoring 144 cells.
IDIM = [("PAIN", 40, "Is this skill a top-3 felt pain in THIS vertical?"),
        ("COMBO", 35, "Existing offshore supply doing THIS skill FOR THIS vertical"),
        ("FIT", 25, "Does the vertical's stack make this skill gradeable HERE?")]

PAIN = {  # the three things this buyer complains about, in order
 "E-comm / DTC":       ["Bookkeeping / reconciliation","Ledger & Close (senior)","Paid Media Operations"],
 "Marketing agency":   ["AR & Collections","Reporting & Analytics (BI)","Paid Media Operations"],
 "SaaS":               ["AR & Collections","Reporting & Analytics (BI)","Ledger & Close (senior)"],
 "Staffing agency":    ["AR & Collections","Payroll processing","Compliance & Document Ops"],
 "MSP / IT services":  ["AR & Collections","AP & Invoice Processing","Reporting & Analytics (BI)"],
 "Freight / trucking": ["AR & Collections","Compliance & Document Ops","AP & Invoice Processing"],
 "Insurance agency":   ["Compliance & Document Ops","AR & Collections","Financial reporting pack"],
 "PI law firm":        ["Compliance & Document Ops","AR & Collections","Bookkeeping / reconciliation"],
 "Medical practice":   ["AR & Collections","Compliance & Document Ops","Bookkeeping / reconciliation"],
 "Property mgmt":      ["AP & Invoice Processing","AR & Collections","Financial reporting pack"],
 "Home services":      ["Bookkeeping / reconciliation","AR & Collections","Compliance & Document Ops"],
 "Dental / DSO":       ["AR & Collections","Compliance & Document Ops","Bookkeeping / reconciliation"],
}
# where Indian supply already does this exact combination at scale
COMBO = {
 "E-comm / DTC":       {"Bookkeeping / reconciliation","AP & Invoice Processing","Customer support (email)",
                        "Paid Media Operations","CRM / RevOps data hygiene"},
 "Marketing agency":   {"Paid Media Operations","Reporting & Analytics (BI)","Email / Lifecycle Ops",
                        "AP & Invoice Processing"},
 "SaaS":               {"AR & Collections","CRM / RevOps data hygiene","Reporting & Analytics (BI)"},
 "Staffing agency":    {"Compliance & Document Ops","CRM / RevOps data hygiene"},
 "MSP / IT services":  {"AP & Invoice Processing","AR & Collections"},
 "Freight / trucking": {"AR & Collections","AP & Invoice Processing","Compliance & Document Ops"},
 "Insurance agency":   {"Compliance & Document Ops","AR & Collections"},
 "PI law firm":        {"Compliance & Document Ops"},
 "Medical practice":   {"AR & Collections","Compliance & Document Ops"},
 "Property mgmt":      {"AP & Invoice Processing","AR & Collections","Bookkeeping / reconciliation"},
 "Home services":      {"Bookkeeping / reconciliation","AR & Collections"},
 "Dental / DSO":       {"AR & Collections","Compliance & Document Ops"},
}

VW = {k: w for k, w, _, _ in VDIM}; VO = [k for k, _, _, _ in VDIM]
SW = {k: w for k, w, _, _ in SDIM}; SO = [k for k, _, _, _ in SDIM]
assert sum(VW.values()) == 100 and sum(SW.values()) == 100


def vscore(v):
    d = dict(zip(VO, VERTICALS[v]))
    return sum(VW[k] * d[k] / 5 for k in VO), d


def sscore(s):
    d = dict(zip(SO, SKILLS[s]))
    return sum(SW[k] * d[k] / 5 for k in SO), d


def iscore(v, s):
    pain = {0: 5, 1: 4, 2: 4}.get(PAIN[v].index(s), 1) if s in PAIN[v] else 1
    combo = 5 if s in COMBO[v] else 2
    fit = min(5, round((dict(zip(VO, VERTICALS[v]))["STACK"] +
                        dict(zip(SO, SKILLS[s]))["HAPPY"]) / 2))
    tot = (40 * pain / 5 + 35 * combo / 5 + 25 * fit / 5)
    return tot, dict(PAIN=pain, COMBO=combo, FIT=fit)


def pair(v, s):
    vs, _ = vscore(v); ss, _ = sscore(s); i, _ = iscore(v, s)
    return 0.35 * vs + 0.35 * ss + 0.30 * i


# ------------------------------------------------------------------- output
print("# First Principles — Verticals, Skills, and the Map\n")
print("Three criteria sets scored **independently**, then combined. Earlier models mixed buyer")
print("properties with work properties into one number, which is why the answer moved every time a")
print("new consideration was introduced.\n")
print("| | What it measures |\n|---|---|")
print("| **Vertical** | Properties of the buyer — true whatever role you place |")
print("| **Skill** | Properties of the work — true wherever you place it |")
print("| **Interaction** | Only exists at the intersection: felt pain, existing combo supply, stack fit |")
print("\n**Pair score = 35% vertical + 35% skill + 30% interaction.**\n")

print("---\n\n## 1. Vertical criteria\n")
print("| Dim | Wt | Criterion | Anchors |\n|---|---|---|---|")
for k, w, n, a in VDIM:
    print(f"| `{k}` | **{w}** | {n} | {a} |")
print("\n**Gates: `REMOTE` < 4 (vertical) and `ASYNC` < 4 (skill) are disqualifying** — never sell to a buyer who must first be "
      "convinced that remote hiring works.\n")
print("| # | Vertical | Score | " + " | ".join(f"`{k}`" for k in VO) + " | |")
print("|---|---|---|" + "---|" * (len(VO) + 1))
vr = sorted(((vscore(v)[0], v) for v in VERTICALS), reverse=True)
for i, (t, v) in enumerate(vr, 1):
    d = dict(zip(VO, VERTICALS[v]))
    gate = "" if d["REMOTE"] >= 4 else "⛔ REMOTE"
    print(f"| {i} | {'**'+v+'**' if not gate else v} | **{t:.1f}** | "
          + " | ".join(str(d[k]) for k in VO) + f" | {gate} |")

print("\n---\n\n## 2. Skill criteria\n")
print("| Dim | Wt | Criterion | Anchors |\n|---|---|---|---|")
for k, w, n, a in SDIM:
    print(f"| `{k}` | **{w}** | {n} | {a} |")
print("\n| # | Skill | Score | " + " | ".join(f"`{k}`" for k in SO) + " |")
print("|---|---|---|" + "---|" * len(SO))
sr = sorted(((sscore(s)[0], s) for s in SKILLS), reverse=True)
for i, (t, s) in enumerate(sr, 1):
    d = dict(zip(SO, SKILLS[s]))
    print(f"| {i} | **{s}** | **{t:.1f}** | " + " | ".join(str(d[k]) for k in SO) + " |")

print("\n---\n\n## 3. Interaction criteria\n")
print("| Dim | Wt | Criterion |\n|---|---|---|")
for k, w, n in IDIM:
    print(f"| `{k}` | **{w}** | {n} |")
print("\nThe interaction is what the earlier single-score models kept losing. A skill can be")
print("excellent and a vertical can be excellent while the *pair* is weak — because the buyer does")
print("not feel that particular pain, or no one offshore has done that exact combination before.\n")

print("---\n\n## 4. THE MAP\n")
# TWO vertical gates now: already hires remote, AND targetable on Meta.
# The second was hidden inside REACH until it was split out.
ok = [v for v in VERTICALS
      if dict(zip(VO, VERTICALS[v]))["REMOTE"] >= 4
      and dict(zip(VO, VERTICALS[v]))["META"] >= 4]
sok = [s for s in SKILLS if dict(zip(SO, SKILLS[s]))["ASYNC"] >= 4]
top_v = [v for _, v in vr if v in ok][:6]
top_s = [s for _, s in sr][:8]
print("Rows = verticals passing the `REMOTE` gate, best first. Columns = skills, best first.\n")
print("| | " + " | ".join(s.split(" (")[0].split(" / ")[0][:14] for s in top_s) + " |")
print("|---|" + "---|" * len(top_s))
best = []
for v in top_v:
    cells = []
    for s in top_s:
        p = pair(v, s)
        best.append((p, v, s))
        cells.append(f"**{p:.1f}**" if p >= 76 else f"{p:.1f}")
    print(f"| **{v}** | " + " | ".join(cells) + " |")

best.sort(reverse=True)
print("\n### Top 12 pairs\n")
print("| # | Vertical | Skill | Pair | Vertical | Skill | Interaction |")
print("|---|---|---|---|---|---|---|")
for i, (p, v, s) in enumerate(best[:12], 1):
    print(f"| {i} | {v} | **{s}** | **{p:.1f}** | {vscore(v)[0]:.0f} | {sscore(s)[0]:.0f} "
          f"| {iscore(v,s)[0]:.0f} |")

print("\n---\n\n## 5. Picking winners separately does not work\n")
print("The top three verticals have **different** best skills:\n")
print("| Vertical | Best skill | 2nd |\n|---|---|---|")
for v in [x for _, x in vr if x in ok][:3]:
    row = sorted(((pair(v, s), s) for s in SKILLS), reverse=True)[:2]
    print(f"| {v} | **{row[0][1]}** ({row[0][0]:.1f}) | {row[1][1]} ({row[1][0]:.1f}) |")
print("\nSo a naive top-3 × top-3 grid contains weak cells — e-comm's AR is only 74.0 while MSP's")
print("is 88.7. **The right optimisation is to maximise the WORST cell**, because one bench has to")
print("serve every cell in the grid.\n")

import itertools
best_grid = []
for vt in itertools.combinations(ok, 3):
    for st in itertools.combinations(sok, 3):
        cells = [pair(v, s) for v in vt for s in st]
        best_grid.append((min(cells), sum(cells) / 9, vt, st))
best_grid.sort(reverse=True)
print("| # | Verticals | Skills | Worst cell | Mean |\n|---|---|---|---|---|")
for i, (mn, mean, vt, st) in enumerate(best_grid[:5], 1):
    print(f"| {i} | {' + '.join(x.split(' / ')[0] for x in vt)} "
          f"| {' + '.join(s.split(' (')[0] for s in st)} | **{mn:.1f}** | {mean:.1f} |")

mn, mean, vt, st = best_grid[0]
print("\n---\n\n## 6. THE ANSWER\n")
print(f"### Verticals — {' · '.join(vt)}\n")
print(f"### Skills — {' · '.join(st)}\n")
print("| | " + " | ".join(vt) + " |\n|---|" + "---|" * 3)
for s in st:
    print(f"| **{s}** | " + " | ".join(f"**{pair(v,s):.1f}**" for v in vt) + " |")
mx = max(pair(v, s) for v in vt for s in st)
print(f"\n**Worst cell {mn:.1f} · mean {mean:.1f} · spread {mx-mn:.1f}.** Optimising the grid rather")
print("than picking winners separately lifts the worst cell from 68.9 to "
      f"{mn:.1f} and cuts the spread from 19.9 to {mx-mn:.1f}.\n")
print("**All three skills are the transactional finance layer plus BI — not the senior close.**")
print("Ledger & Close scores 4th on skill and carries the highest fee, but it is the least")
print("portable, so it belongs as a per-vertical add-on rather than in the shared grid.\n")
print("**Read the grid by column, not by row.** Each vertical has a natural entry skill:\n")
print("| Vertical | Lead with | Why |\n|---|---|---|")
lead = {v: max(((pair(v, s), s) for s in st))for v in vt}
why = {"AR & Collections": "billing volume is the felt pain and cash is the language owners speak",
       "AP & Invoice Processing": "highest existing offshore supply, zero switch cost, fastest to fill",
       "Reporting & Analytics (BI)": "highest fee of the three, spans finance and marketing, founder can grade it",
       "Bookkeeping / reconciliation": "78% savings on Somewhere's own data, deepest Indian supply, fully async",
       "Compliance & Document Ops": "most AI-durable of all — liability-bearing work nobody delegates to a model",
       "Financial reporting pack": "async, gradeable, mid-fee",
       "Payroll processing": "best retention of any skill — deadline-driven and sticky",
       "Paid Media Operations": "the founder can grade this personally in twenty minutes",
       "Email / Lifecycle Ops": "revenue-attributable output",
       "CRM / RevOps data hygiene": "zero switch cost",
       "Ledger & Close (senior)": "highest fee, but least portable"}
for v in vt:
    sc, s = lead[v]
    print(f"| **{v}** | {s} ({sc:.1f}) | {why.get(s, '—')} |")
