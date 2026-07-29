#!/usr/bin/env python3
"""
Role x VERTICAL scoring model.

The 179-role model (model.py) scored roles in isolation. But "e-commerce
bookkeeper" beat "bookkeeper" because of the vertical, not the role — the
standardised tool stack is what made the work gradeable, the bench possible and
the buyer reachable. So the unit of analysis is the PAIR.

Criteria are the ones that actually emerged through the analysis, not the
original 14. The new top-weighted dimension is STACK.

Run:  python3 scoring/vertical_model.py > scoring/VERTICALS.md
"""

DIMS = [
    ("STACK", 13, "Vertical tool-stack standardisation",
     "5=one stack every time (Shopify+A2X+QBO, Applied Epic, ServiceTitan)  "
     "3=2-3 competing systems  1=bespoke per client. THE unlock: standard stack = "
     "gradeable work = warm bench = free shortlist"),
    ("SAT", 12, "Satisfiability",
     "Objective output + client SOP exists + fast time-to-value + failure recoverable "
     "+ not dependent on client's team. 5=binary right/wrong  1=judgment call"),
    ("RR", 11, "Buyer remote-readiness",
     "5=already has offshore staff  3=growing  1=culturally resistant"),
    ("REACH", 10, "Buyer reachability",
     "5=public named list (SEC ADV filings, state licence registries, BuiltWith/"
     "Storeleads)  3=targetable with effort  1=needs 1:1 outbound"),
    ("ICP", 10, "Vertical size in the hiring band",
     "5=>150k firms  4=50-150k  3=20-50k  2=8-20k  1=<8k"),
    ("EOR", 8, "EOR attach likelihood",
     "Will they need us to employ the person? 5=no entity, no appetite, no choice"),
    ("SUP", 8, "Offshore supply depth for this role+vertical",
     "5=thousands already doing this exact work for US clients  1=must create it"),
    ("AI", 8, "AI durability, 5-year",
     "5=judgment/regulated/liability-bearing  1=being eaten now"),
    ("RET", 8, "Retention",
     "Async + no night shift + weak local counter-bid + no escape path + year-round"),
    ("FEE", 6, "Salary band / fee size", "5=$40k+ placed  3=$20-28k  1=<$14k"),
    ("CD", 4, "Competitive whitespace (inverse)",
     "5=nobody vertical-specific  0=a dominant incumbent owns it"),
    ("REP", 2, "Seats per client", "5=hires teams  1=one and done"),
]
W = {k: w for k, w, _, _ in DIMS}
ORDER = [k for k, _, _, _ in DIMS]
assert sum(W.values()) == 100, sum(W.values())

GATES = [("RET", 1, "churns faster than it can be replaced"),
         ("AI", 1, "role disappears inside 5 years"),
         ("SAT", 1, "cannot promise a quality you cannot define"),
         ("RR", 1, "buyer will not hire offshore")]

# (vertical, role, STACK, SAT, RR, REACH, ICP, EOR, SUP, AI, RET, FEE, CD, REP)
PAIRS = [
    # ---------------------------------------------- E-COMMERCE / DTC / AMAZON
    ("E-comm/DTC", "Bookkeeper / accountant (A2X, close)", 5,5,5,5,3,4,4,2,4,3,3,3),
    ("E-comm/DTC", "Inventory & COGS analyst",             5,4,5,5,3,4,3,3,4,3,4,2),
    ("E-comm/DTC", "Amazon PPC / retail media",            5,4,5,5,3,4,4,3,3,3,3,2),
    ("E-comm/DTC", "Email / lifecycle (Klaviyo)",          5,4,5,5,3,4,3,3,4,3,3,2),
    ("E-comm/DTC", "Supply chain / 3PL coordinator",       4,4,5,5,3,4,3,3,4,3,4,2),
    ("E-comm/DTC", "Catalog / listings ops",               5,4,5,5,3,4,5,1,3,1,2,3),
    ("E-comm/DTC", "Customer support (email/chat)",        4,3,5,5,3,4,5,2,3,1,2,4),

    # -------------------------------------------------- INSURANCE AGENCIES
    ("Insurance agency", "COI issuance & tracking",        5,5,4,5,3,4,3,3,5,2,1,4),
    ("Insurance agency", "Policy checking",                5,5,4,5,3,4,3,3,5,2,1,4),
    ("Insurance agency", "Endorsement processing",         5,5,4,5,3,4,3,3,5,2,1,4),
    ("Insurance agency", "Commercial lines processor",     5,4,4,5,3,4,3,3,4,3,2,4),
    ("Insurance agency", "Renewal prep & remarketing",     5,4,4,5,3,4,2,4,5,3,3,3),
    ("Insurance agency", "Claims processing support",      4,4,4,5,3,4,3,3,4,2,2,3),
    ("Insurance agency", "Loss run analysis",              4,5,4,5,2,4,2,3,5,2,4,2),

    # ------------------------------------------------------- PI / LEGAL
    ("PI law firm", "Case manager",                        4,4,4,4,3,4,3,4,4,3,4,3),
    ("PI law firm", "Medical records retrieval",           4,5,4,4,3,4,4,2,4,2,3,4),
    ("PI law firm", "Lien resolution specialist",          4,4,4,4,2,4,2,4,4,3,5,2),
    ("PI law firm", "Demand package preparation",          4,4,4,4,3,4,3,1,4,3,4,3),
    ("PI law firm", "Intake specialist (voice)",           4,3,4,4,3,4,4,2,1,2,3,3),
    ("Immigration law", "Case/petition paralegal",         4,4,4,4,2,4,4,3,4,3,4,3),
    ("Immigration law", "Document collection & RFE prep",  4,5,4,4,2,4,4,3,4,2,4,3),

    # -------------------------------------------------------- DENTAL / DSO
    ("Dental / DSO", "Insurance verification & benefits",  5,5,3,4,4,4,4,2,3,2,2,4),
    ("Dental / DSO", "Claims & billing / AR follow-up",    5,5,3,4,4,4,4,3,4,2,2,4),
    ("Dental / DSO", "Treatment plan follow-up (voice)",   5,3,3,4,4,4,3,3,1,2,3,3),
    ("Dental / DSO", "Recall & scheduling (voice)",        5,3,3,4,4,4,4,2,1,1,2,4),
    ("Dental / DSO", "Multi-location bookkeeping",         4,5,3,4,3,4,3,3,4,3,3,3),

    # --------------------------------------------------- MEDICAL PRACTICES
    ("Medical practice", "Medical biller",                 4,4,5,4,5,4,5,2,4,2,0,4),
    ("Medical practice", "Coder (CPC)",                    4,5,5,4,4,4,5,2,4,2,0,4),
    ("Medical practice", "Prior authorisation",            4,4,5,4,4,4,5,2,2,2,1,4),
    ("Medical practice", "Credentialing specialist",       4,5,4,4,3,4,3,4,4,3,3,3),
    ("Medical practice", "Denial management / appeals",    4,4,5,4,4,4,4,3,4,3,1,4),

    # ------------------------------------------------- BEHAVIORAL HEALTH/ABA
    ("Behavioral health/ABA", "Billing & claims",          5,5,4,3,2,4,3,3,4,3,4,3),
    ("Behavioral health/ABA", "Authorisation & tracking",  5,4,4,3,2,4,2,3,4,3,4,3),
    ("Behavioral health/ABA", "Credentialing",             4,5,4,3,2,4,2,4,4,3,4,2),

    # --------------------------------------------------- PROPERTY MANAGEMENT
    ("Property mgmt", "AP / AR / owner statements",        5,5,4,4,4,4,4,3,4,2,3,4),
    ("Property mgmt", "CAM reconciliation",                5,5,4,4,3,4,2,4,5,3,4,2),
    ("Property mgmt", "Collections & delinquency",         5,4,4,4,4,4,3,3,4,2,3,3),
    ("Property mgmt", "Leasing coordinator (voice)",       5,3,4,4,4,4,4,2,1,2,3,4),
    ("Property mgmt", "Maintenance dispatch (voice)",      5,3,4,4,4,4,4,2,0,1,3,4),
    ("Property mgmt", "HOA administration",                4,4,3,3,2,4,3,3,4,2,4,3),

    # -------------------------------------------------------- RIA / WEALTH
    ("RIA / wealth", "Paraplanner",                        4,4,3,5,2,4,3,4,5,3,4,2),
    ("RIA / wealth", "Account opening & transfers ops",    4,5,3,5,2,4,2,3,5,3,5,3),
    ("RIA / wealth", "Billing & fee calculation",          4,5,3,5,2,4,2,4,5,3,5,2),
    ("RIA / wealth", "Performance reporting",              4,5,3,5,2,4,2,4,5,3,5,2),
    ("RIA / wealth", "CRM & data hygiene",                 4,4,3,5,2,4,3,2,4,2,4,2),

    # ---------------------------------------------------- HOME SERVICES
    ("Home services", "Bookkeeping / job costing",         5,5,3,4,5,4,3,3,4,2,3,3),
    ("Home services", "AR / collections",                  5,4,3,4,5,4,3,3,4,2,3,3),
    ("Home services", "Permit & warranty coordination",    5,4,3,4,5,4,2,3,4,2,4,3),
    ("Home services", "Dispatch (voice, US hours)",        5,3,3,4,5,4,4,2,0,2,2,4),
    ("Home services", "Inbound booking CSR (voice)",       5,3,3,4,5,4,4,2,1,1,2,5),

    # ------------------------------------------------------------ ROOFING
    ("Roofing", "Insurance supplement writer",             4,4,3,4,3,4,2,4,4,4,5,2),
    ("Roofing", "Claims & Xactimate estimator",            4,4,3,4,3,4,2,4,4,4,5,2),
    ("Roofing", "Production coordinator",                  4,3,3,4,3,4,2,3,4,2,4,2),

    # --------------------------------------------------- FREIGHT / TRUCKING
    ("Freight/trucking", "Billing & settlements",          4,5,5,4,4,4,5,3,4,2,1,3),
    ("Freight/trucking", "Safety & compliance documents",  4,5,5,4,4,4,4,4,4,2,2,3),
    ("Freight/trucking", "Load planner",                   4,4,5,4,4,4,5,2,2,2,1,4),
    ("Freight/trucking", "Dispatcher (voice, nights)",     4,3,5,4,4,4,5,2,0,2,1,5),
    ("Freight/trucking", "Carrier sales",                  4,2,5,4,4,4,4,2,0,2,2,4),

    # --------------------------------------------------------- MSP / IT
    ("MSP / IT services", "Billing & invoice reconciliation",5,5,5,4,3,4,3,3,4,2,3,3),
    ("MSP / IT services", "Procurement & quoting",         5,4,5,4,3,4,2,3,4,3,4,3),
    ("MSP / IT services", "L1 helpdesk (shifts)",          5,4,5,4,3,4,5,1,1,2,2,5),
    ("MSP / IT services", "NOC monitoring (shifts)",       5,4,5,4,3,4,4,2,1,2,3,4),
    ("MSP / IT services", "Documentation & asset records", 5,4,5,4,3,4,3,2,4,2,4,3),

    # ------------------------------------------------------ MARKETING AGENCY
    ("Marketing agency", "Reporting & analytics analyst",  4,4,5,4,4,4,3,3,3,3,3,3),
    ("Marketing agency", "Billing & project accounting",   4,5,5,4,4,4,3,3,4,2,4,2),
    ("Marketing agency", "Media buyer",                    4,4,5,4,4,4,4,3,1,3,3,3),
    ("Marketing agency", "Designer / video editor",        3,3,5,4,4,4,4,2,1,2,2,3),
    ("Marketing agency", "Account coordinator",            4,3,5,4,4,4,4,3,3,2,3,3),

    # ------------------------------------------------------------- SAAS
    ("SaaS", "Revenue accountant / rev-rec",               5,4,5,4,3,4,3,4,4,4,3,2),
    ("SaaS", "AR / collections",                           5,4,5,4,3,4,4,3,4,2,3,3),
    ("SaaS", "Sales ops / CRM hygiene",                    5,4,5,4,3,4,3,2,4,3,3,3),
    ("SaaS", "QA automation",                              5,5,5,4,3,4,3,2,3,4,3,3),
    ("SaaS", "Support L1 (shifts)",                        5,3,5,4,3,4,5,1,1,2,2,5),

    # ------------------------------------------------------- VETERINARY
    ("Veterinary", "Billing & insurance claims",           4,4,3,4,3,4,2,3,4,2,3,3),
    ("Veterinary", "Records & referral coordination",      4,4,3,4,3,4,2,3,4,2,4,3),
    ("Veterinary", "Inventory & purchasing",               4,4,3,4,3,4,2,3,4,2,4,2),

    # ------------------------------------------------------ MED SPA / AESTHETIC
    ("Med spa", "Billing & membership admin",              4,4,4,3,3,4,2,3,4,2,4,3),
    ("Med spa", "Inventory & product ops",                 4,4,4,3,3,4,2,3,4,2,4,2),
    ("Med spa", "Front desk / booking (voice)",            4,3,4,3,3,4,3,2,1,1,4,4),

    # -------------------------------------------------- HOME HEALTH / HOSPICE
    ("Home health", "Billing & revenue cycle",             4,5,3,4,3,4,4,3,4,2,2,4),
    ("Home health", "Authorisation & eligibility",         4,4,3,4,3,4,3,3,4,2,3,4),
    ("Home health", "Scheduling & coordination (voice)",   4,3,3,4,3,4,3,2,1,2,3,5),

    # ----------------------------------------------- MORTGAGE / TITLE (cyclical)
    ("Mortgage broker", "Loan processor",                  4,5,4,4,3,4,4,3,1,3,2,3),
    ("Mortgage broker", "Post-closing audit",              4,5,4,4,3,4,3,3,1,2,3,3),
    ("Title / escrow", "Title examiner / abstractor",      4,5,3,4,3,4,3,3,2,3,3,3),
    ("Title / escrow", "Post-closing & policy issuance",   4,5,3,4,3,4,3,3,2,2,3,3),

    # -------------------------------------------------------- CONSTRUCTION
    ("Construction / GC", "Project accounting & AP",       4,5,2,3,4,4,3,3,4,3,4,3),
    ("Construction / GC", "Estimator / takeoff",           4,4,2,3,4,4,3,4,5,3,4,2),
    ("Construction / GC", "Submittal & RFI coordinator",   4,4,2,3,4,4,2,3,4,2,4,2),
    ("Construction / GC", "Certified payroll & compliance",4,5,2,3,3,4,2,4,5,3,5,2),

    # ---------------------------------------------------- STAFFING AGENCIES
    ("Staffing agency", "Back-office payroll & invoicing", 5,5,5,4,3,4,3,3,4,2,4,3),
    ("Staffing agency", "Compliance & onboarding docs",    5,5,5,4,3,4,3,3,4,2,4,3),
    ("Staffing agency", "Recruiting coordinator",          5,4,5,4,3,4,4,2,3,2,3,4),
    ("Staffing agency", "Sourcer",                         5,4,5,4,3,4,5,1,2,1,3,4),

    # ------------------------------------------------- FRANCHISE / MULTI-UNIT
    ("Franchise systems", "Multi-unit bookkeeping",        4,5,3,4,3,4,3,3,4,3,4,5),
    ("Franchise systems", "Royalty reporting & audit",     4,5,3,4,2,4,2,4,5,3,5,4),
    ("Franchise systems", "AP / invoice processing",       4,5,3,4,3,4,4,2,4,2,4,5),

    # -------------------------------------------------------- RESTAURANTS
    ("Restaurant groups", "Bookkeeping (R365/Toast)",      4,5,3,4,4,4,3,3,4,2,4,4),
    ("Restaurant groups", "AP & invoice processing",       4,5,3,4,4,4,4,2,4,1,4,4),
    ("Restaurant groups", "Inventory & food cost",         4,4,3,4,4,4,3,3,4,2,4,3),

    # ------------------------------------------------------- AUTO / DEALERS
    ("Auto repair / dealers", "Warranty claims admin",     4,5,2,3,4,3,2,3,4,2,4,3),
    ("Auto repair / dealers", "Bookkeeping & reconciliation",4,5,2,3,4,3,3,3,4,2,4,3),

    # --------------------------------------------------------- NONPROFIT
    ("Nonprofit", "Grant & fund accounting",               4,5,3,4,3,3,2,4,4,2,4,2),
    ("Nonprofit", "Donor CRM & gift processing",           4,4,3,4,3,3,2,2,4,1,4,2),
]

# ------------------------------------------------------------------ scoring


def score(row):
    v = dict(zip(ORDER, row[2:]))
    total = sum(W[k] * v[k] / 5 for k in ORDER)
    fails = [(k, r) for k, t, r in GATES if v[k] <= t]
    return total, v, fails


rows = sorted((score(r)[0], r[0], r[1], score(r)[1], score(r)[2]) for r in PAIRS)[::-1]
clean = [r for r in rows if not r[4]]
ko = [r for r in rows if r[4]]

# ------------------------------------------------------------------- output

print("# Role × Vertical Ranking\n")
print(f"**{len(PAIRS)} role × vertical pairs across {len(set(p[0] for p in PAIRS))} verticals.** "
      "Generated by [`vertical_model.py`](vertical_model.py).\n")

print("## Why the unit of analysis changed\n")
print("[`model.py`](model.py) scored 179 roles in isolation. But **\"e-commerce bookkeeper\" beat")
print("\"bookkeeper\" because of the vertical, not the role.** The standardised tool stack is what")
print("made the work gradeable, the bench possible and the buyer reachable. So the unit is the")
print("**pair**, and the top-weighted dimension is now `STACK`.\n")

print("| Dim | Wt | Dimension | Anchors |")
print("|---|---|---|---|")
for k, w, n, a in DIMS:
    print(f"| `{k}` | **{w}** | {n} | {a} |")
print("\n**Gates** (⛔ regardless of score): " +
      " · ".join(f"`{k}`≤{t} — {r}" for k, t, r in GATES) + "\n")

print("---\n\n## The insight that reframes the search\n")
print("The most acute US labour shortages are in roles that **cannot be offshored**:")
print("dental hygienists (60–90 days to fill, ~90% of practices struggling, 11% capacity")
print("reduction) [V] · ~110,000 HVAC technicians and a projected 550,000 plumber shortfall [V] ·")
print("~82,000 truck drivers, with 92% of carriers running ten trucks or fewer [V] ·")
print("530,000+ construction workers [V].\n")
print("**89% of small-business owners hiring reported few or no qualified applicants; one third")
print("had openings they could not fill** [V].\n")
print("> You cannot offshore the hygienist. You *can* offshore the insurance verification and")
print("> claims follow-up eating the front desk's day, which is how the practice gets capacity")
print("> back. **Sell into verticals whose acute shortage is un-offshorable, by taking the")
print("> offshorable load off the people they cannot replace.**\n")

print("---\n\n## Top 20 after gates\n")
print("| # | Vertical | Role | Score | " + " | ".join(f"`{k}`" for k in ORDER) + " |")
print("|---|---|---|---|" + "---|" * len(ORDER))
for i, (t, vert, role, v, _) in enumerate(clean[:20], 1):
    star = " ⭐" if vert == "E-comm/DTC" and role.startswith("Bookkeeper") else ""
    print(f"| {i} | {vert} | **{role}**{star} | **{t:.1f}** | "
          + " | ".join(str(v[k]) for k in ORDER) + " |")

ref = next(r for r in rows if r[1] == "E-comm/DTC" and r[2].startswith("Bookkeeper"))
ref_rank = clean.index(ref) + 1
print(f"\n⭐ = the current pick. **E-comm bookkeeper ranks #{ref_rank} at {ref[0]:.1f}.**\n")

print("---\n\n## Vertical averages (clean pairs only)\n")
by = {}
for t, vert, role, v, f in clean:
    by.setdefault(vert, []).append((t, role))
print("| Vertical | Clean roles | Mean | Best role |")
print("|---|---|---|---|")
for vert, lst in sorted(by.items(), key=lambda x: -sum(t for t, _ in x[1]) / len(x[1])):
    best = max(lst)
    print(f"| {vert} | {len(lst)} | **{sum(t for t,_ in lst)/len(lst):.1f}** | {best[1]} ({best[0]:.1f}) |")

print("\n---\n\n## Gated out\n")
print("| Vertical | Role | Score | Gate |")
print("|---|---|---|---|")
for t, vert, role, v, fails in ko:
    print(f"| {vert} | {role} | {t:.1f} | " + "; ".join(f"**{k}** — {r}" for k, r in fails) + " |")

print("\n---\n\n## The 10 next best — best role per vertical, e-comm excluded\n")
_b = {}
for t, vert, role, v, f in clean:
    if vert == "E-comm/DTC":
        continue
    if vert not in _b or t > _b[vert][0]:
        _b[vert] = (t, role, v)
_ref = next(v for t, vert, role, v, f in clean
            if vert == "E-comm/DTC" and role.startswith("Bookkeeper"))
print("| # | Vertical | Best role | Score | Beats e-comm on | Loses on |")
print("|---|---|---|---|---|---|")
for i, (vert, (t, role, v)) in enumerate(sorted(_b.items(), key=lambda x: -x[1][0])[:10], 1):
    up = ", ".join(f"`{k}`" for k in ORDER if v[k] > _ref[k]) or "—"
    dn = ", ".join(f"`{k}`" for k in ORDER if v[k] < _ref[k]) or "—"
    print(f"| {i} | **{vert}** | {role} | **{t:.1f}** | {up} | {dn} |")

print("\n---\n\n## Anchoring test\n")
print("E-comm scores 5 on `STACK`, `RR` and `REACH` — **the three dimensions this analysis")
print("derived from the e-comm case.** That is partly circular, so the ranking was re-run with")
print("`STACK` and `REACH` halved (13→5, 10→5) and the weight moved to `ICP`, `FEE` and `CD`,")
print("which favour bigger, richer, less-contested verticals.\n")
_W2 = dict(W); _W2["STACK"], _W2["REACH"], _W2["ICP"], _W2["FEE"], _W2["CD"] = 5, 5, 14, 10, 9
assert sum(_W2.values()) == 100
_alt = sorted(((sum(_W2[k] * dict(zip(ORDER, r[2:]))[k] / 5 for k in ORDER), r[0], r[1])
               for r in PAIRS
               if not any(dict(zip(ORDER, r[2:]))[k] <= t for k, t, _ in GATES)), reverse=True)
_br = {(vert, role): i for i, (t, vert, role, v, f) in enumerate(clean, 1)}
print("| # | Vertical | Role | Reweighted | Base rank |")
print("|---|---|---|---|---|")
for i, (t, vert, role) in enumerate(_alt[:12], 1):
    print(f"| {i} | {vert} | {role} | **{t:.1f}** | {_br[(vert, role)]} |")
_ec = next(i for i, (t, vert, role) in enumerate(_alt, 1) if vert == "E-comm/DTC")
print(f"\n**E-comm bookkeeper falls from #1 to #{_ec} under the reweight, but stays top-3, and the")
print("same verticals dominate the band.** Read that as: e-comm's *lead* is partly an artefact of")
print("how the criteria were derived; its *membership in the top tier* is not. Treat the top ~12")
print("as a tied band, as with the role model (MASTER §7.10).\n")

print("---\n\n## CONSENSUS RANKING — all verticals including e-comm\n")
print("Because the base weights are partly circular (see the anchoring test above), the")
print("defensible single ordering is the **average of both weightings**. A pair that ranks well")
print("under both is robust; one that only ranks well under the base weights was flattered by")
print("criteria derived from the e-comm case.\n")
_altr = {(vert, role): i for i, (t, vert, role) in enumerate(_alt, 1)}
_cons = sorted(((( _br[(vert, role)] + _altr[(vert, role)]) / 2, _br[(vert, role)],
                 _altr[(vert, role)], vert, role, t)
                for t, vert, role, v, f in clean), key=lambda x: x[0])
print("| # | Vertical | Role | Base | Reweighted | Swing |")
print("|---|---|---|---|---|---|")
for i, (avg, b, a, vert, role, t) in enumerate(_cons[:22], 1):
    sw = a - b
    tag = " 🔻" if sw >= 6 else (" 🔺" if sw <= -6 else "")
    ec = " ⭐" if vert == "E-comm/DTC" else ""
    print(f"| {i} | **{vert}**{ec} | {role} | {b} | {a} | {sw:+d}{tag} |")
print("\n⭐ e-comm · 🔺 undervalued by the base weights · 🔻 flattered by them\n")
_ecc = [i for i, c in enumerate(_cons, 1) if c[3] == "E-comm/DTC"]
print(f"**E-comm pairs occupy consensus ranks {', '.join(str(x) for x in _ecc[:6])}** "
      f"— {len([x for x in _ecc if x <= 10])} of the top 10.\n")

print(f"---\n\n*{len(PAIRS)} pairs · {len(clean)} clean · {len(ko)} gated out*")
