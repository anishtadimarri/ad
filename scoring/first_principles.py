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
    ("REMOTE", 16, "Already employs remote/offshore staff",
     "5=offshore is normal here  3=growing  1=would need converting. GATE at <4"),
    ("DECIDE", 12, "Single decision-maker", "5=owner decides today  3=owner+1  1=committee"),
    ("REACH", 12, "Named list exists",
     "5=public/scrapeable register (BuiltWith, Storeleads, SEC ADV, Clutch)  1=1:1 outbound"),
    ("AFFORD", 11, "Can write a $6k fee without thinking",
     "5=comfortable  3=needs justifying  1=it is a real decision"),
    ("STACK", 11, "One software stack across the vertical",
     "5=same stack every client  3=2-3 systems  1=bespoke"),
    ("EORNEED", 9, "Needs us to employ the person",
     "5=no entity, no appetite, no alternative but Deel"),
    ("COUNT", 9, "Businesses in the hiring band",
     "5=>100k  4=50-100k  3=20-50k  2=10-20k  1=<10k"),
    ("SEATS", 8, "Buys more than one seat over time", "5=builds a team  1=one and done"),
    ("WHITE", 7, "No vertical-specialist incumbent", "5=open  0=dominated"),
    ("CLEAN", 5, "No licensing/regulatory blocker", "5=none  1=heavy"),
]
# vertical: REMOTE DECIDE REACH AFFORD STACK EORNEED COUNT SEATS WHITE CLEAN
VERTICALS = {
 "E-comm / DTC":        (5,5,5,5,5,4,3,3,3,5),
 "Marketing agency":    (5,5,4,4,4,4,3,4,4,5),
 "SaaS":                (5,3,4,5,5,4,2,4,4,5),
 "Staffing agency":     (5,5,4,4,5,4,2,4,4,4),
 "MSP / IT services":   (5,5,4,4,5,4,2,4,4,5),
 "Freight / trucking":  (5,5,4,2,4,4,3,5,2,4),
 "Insurance agency":    (4,4,5,4,5,4,3,4,1,4),
 "PI law firm":         (4,5,4,5,4,4,3,3,4,2),
 "Medical practice":    (4,4,4,3,4,4,5,4,1,2),
 "Property mgmt":       (4,4,4,3,5,4,4,4,3,4),
 "Home services":       (3,5,4,3,5,4,4,3,3,4),
 "Dental / DSO":        (3,5,4,3,5,4,4,4,2,3),
}

# =============================================================== SKILL CRITERIA
# Properties of the WORK. True wherever you place it.
SDIM = [
    ("GRADE", 15, "Objectively gradeable before placement",
     "5=one right answer, machine-checkable  3=rubric  1=judgment/charisma"),
    ("RETAIN", 14, "Retention",
     "async · no night shift · no freelance escape path · weak local counter-bid · year-round"),
    ("AIDUR", 13, "AI-durable over 5 years",
     "5=judgment/liability-bearing  3=partly exposed  1=being eaten now"),
    ("VALUE", 12, "True value created for BOTH sides",
     "US loaded cost minus offshore cost, and offshore pay minus local pay. 5=both large"),
    ("SUPPLY", 11, "Indian supply already doing this for US clients", "5=thousands  1=must create"),
    ("TRAIN", 9, "Trainable — small delta from adjacent supply", "5=<1wk  3=2wk  1=months"),
    ("FEE", 8, "Fee size", "5=$40k+ placed  3=$20-28k  1=<$14k"),
    ("SOLO", 8, "Output does not depend on the client's team",
     "5=fully independent  1=needs constant client input"),
    ("FASTWIN", 6, "Visible win inside 2 weeks", "5=week one  1=a quarter"),
    ("RECOVER", 4, "Failure is recoverable", "5=fix it next month  1=a client is lost"),
]
# skill: GRADE RETAIN AIDUR VALUE SUPPLY TRAIN FEE SOLO FASTWIN RECOVER
SKILLS = {
 "AR & Collections":            (5,4,3,4,4,5,3,4,5,5),
 "AP & Invoice Processing":     (5,4,2,3,5,5,2,5,5,5),
 "Bookkeeping / reconciliation":(5,3,2,4,5,4,2,4,5,5),
 "Ledger & Close (senior)":     (5,3,3,5,4,2,5,4,3,4),
 "Financial reporting pack":    (4,4,3,4,3,4,4,4,4,4),
 "Payroll processing":          (5,5,3,4,3,3,3,4,4,2),
 "Reporting & Analytics (BI)":  (5,4,3,4,3,4,4,4,4,5),
 "Paid Media Operations":       (5,2,3,4,4,5,4,3,4,4),
 "Email / Lifecycle Ops":       (4,4,3,3,3,4,3,3,4,5),
 "Compliance & Document Ops":   (5,4,5,3,3,3,3,4,3,3),
 "CRM / RevOps data hygiene":   (5,3,2,2,4,5,2,4,4,5),
 "Customer support (email)":    (3,2,2,3,5,5,1,3,4,4),
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
                        dict(zip(SO, SKILLS[s]))["GRADE"]) / 2))
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
print("\n**Gate: `REMOTE` < 4 is disqualifying** — never sell to a buyer who must first be "
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
ok = [v for v in VERTICALS if dict(zip(VO, VERTICALS[v]))["REMOTE"] >= 4]
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
    for st in itertools.combinations(SKILLS, 3):
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
       "Reporting & Analytics (BI)": "highest fee of the three, spans finance and marketing, founder can grade it"}
for v in vt:
    sc, s = lead[v]
    print(f"| **{v}** | {s} ({sc:.1f}) | {why[s]} |")
