#!/usr/bin/env python3
"""
Generate the shareable ranking page from scoring/model.py.

Design plan
-----------
Color   Cool slate ground (#eff1ef / #101618) with a faint green bias so the
        neutral reads as chosen. Petrol teal (#0e5f63) as the single accent.
        Brass (#8f6217) reserved for the top three ranks and the band marker.
        Clay (#9a4a38) only ever means "knocked out".
Type    Three system stacks, no webfont (CSP blocks CDNs, and a silent
        fallback is worse than an honest stack):
          display  Iowan Old Style / Palatino / Georgia  — headings, role names
          body     system grotesque                      — reasons, prose
          data     ui-monospace / SFMono / Menlo         — ranks, scores, codes
Layout  A scorecard ledger. One graphic — the compression band — carries the
        page's central caveat (these fifteen are near-tied). Then fifteen ruled
        rows: mono rank, serif role, cluster chip, mono score, one-line reason.
        Full 179-row ledger and the 49 knockouts below, both scrollable.

Run:  python3 scoring/build_page.py
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from model import ranked, ROLES, DIMENSIONS, GATES, ORDER, WEIGHTS  # noqa: E402

REASONS = {
    "Recruiter":
        "Your academy trains your own recruiters, and graduates who miss your internal bar get "
        "placed with clients instead of discarded. Quality control, supply pipeline and product "
        "become one asset — nothing else on this list does that.",
    "Bookkeeper":
        "Maxes seat volume, gradeability and trainability simultaneously. Every SMB needs one, a "
        "deliberately broken test ledger grades itself, and 30–35% of firms already offshore it.",
    "Marketing ops (HubSpot)":
        "Platform certifications are objective, portable and externally examined, so quality is a "
        "credential rather than an opinion. Unglamorous work — which is precisely why they stay.",
    "Staff accountant":
        "The bookkeeper engine at a higher fee, sold to a buyer who already understands the "
        "arbitrage. $65k US base against $18–28k offshore.",
    "Email / lifecycle (Klaviyo)":
        "Output is revenue-attributable, so quality is a number the client is already watching. "
        "Deep ecommerce demand and far lower escape risk than portfolio-creative roles.",
    "BI / analytics":
        "A take-home grades cleanly and demand is universal. Sits just below the salary line "
        "where Indian counter-bidding turns serious.",
    "Amazon PPC":
        "ACoS and TACoS are objective scores. Enormous seller base, a self-identifying audience "
        "to target, and the founder can grade the work personally.",
    "Salesforce admin":
        "Trailhead is a free, respected, externally examined academy — the cheapest quality "
        "engine available. Admins are sticky because they know the client's org.",
    "QA automation":
        "Engineering's low attrition without full engineering counter-bid pressure. A test suite "
        "is unambiguously gradeable.",
    "Senior accountant":
        "Highest fee in the finance cluster at $24–48k offshore, with AI durability that "
        "bookkeeping and AP work lack.",
    "Amazon / marketplace ops":
        "Clients hire in multiples rather than singly, the buyer is fully remote-native, and "
        "supply is abundant.",
    "CAD drafter":
        "The best AEC entry point: strongest supply liquidity and volume in a cluster whose real "
        "problem is that its buyers are the least remote-ready in the taxonomy.",
    "Software engineer":
        "Maxes both volume and fee. Ranked only this high because retention scores 2 — the local "
        "Indian market outbids you in year two.",
    "Credentialing specialist":
        "Checklist work with a right answer, genuinely AI-durable because it is liability-bearing, "
        "and no incumbent owns it.",
    "PI case manager":
        "Highest-margin buyer in the taxonomy. Records retrieval and lien chasing is the "
        "AI-resistant part of legal volume.",
}

CAVEATS = {
    "Recruiter":
        "Most hiring-cycle-exposed role here — recruiters are the first cut in a downturn. "
        "Retention scored 3; a case exists for 2, which drops it to ~76.6 and third place.",
    "Software engineer":
        "Included for completeness. The counter-bid problem is real and structural.",
    "Amazon PPC":
        "Agency-dominated; many buyers retain a vendor rather than hire a seat.",
    "Bookkeeper":
        "The most crowded lane on the board — TOA Global and Entigrity both own share here.",
}

CLUSTER_LABEL = {
    "Finance": "Finance", "Legal": "Legal", "Healthcare": "Healthcare",
    "Insurance": "Insurance", "RealEstate": "Real estate", "AEC": "AEC",
    "Manufacturing": "Manufacturing", "Technology": "Technology", "Sales": "Sales",
    "Marketing": "Marketing", "SupplyChain": "Supply chain", "Ecommerce": "Ecommerce",
    "HR": "HR", "Regulated": "Regulated", "Admin": "Admin",
}

DIM_NAME = {k: n for k, _, n, _ in DIMENSIONS}
GATE_REASON = {k: r for k, _, r in GATES}

rows = ranked()
clean = [r for r in rows if not r[4]]
knocked = [r for r in rows if r[4]]
top = clean[:15]

all_lo, all_hi = min(r[0] for r in rows), max(r[0] for r in rows)
t_lo, t_hi = min(r[0] for r in top), max(r[0] for r in top)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def dots(v):
    return ("<span class=on>●</span>" * v) + ("<span class=off>●</span>" * (5 - v))


# ------------------------------------------------------------------ markup

cards = []
for i, (total, cluster, name, vals, _) in enumerate(top, 1):
    tier = "gold" if i <= 3 else ""
    caveat = CAVEATS.get(name)
    key_dims = ["V", "D", "RR", "G", "R", "AI"]
    strip = "".join(
        f'<div class=dim><span class=code title="{esc(DIM_NAME[k])}">{k}</span>'
        f'<span class=dots>{dots(vals[k])}</span></div>'
        for k in key_dims
    )
    cards.append(f"""<article class="row {tier}">
  <div class=rank>{i}</div>
  <div class=main>
    <h3>{esc(name)}</h3>
    <div class=meta><span class=chip>{esc(CLUSTER_LABEL[cluster])}</span></div>
    <p class=reason>{esc(REASONS[name])}</p>
    {f'<p class=caveat><span>Caveat</span>{esc(caveat)}</p>' if caveat else ''}
    <div class=strip>{strip}</div>
  </div>
  <div class=score><b>{total:.1f}</b><span>of 100</span></div>
</article>""")

ledger = "".join(
    f"<tr{' class=ko' if fails else ''}>"
    f"<td class=n>{i}</td><td class=rl>{esc(name)}</td>"
    f"<td class=cl>{esc(CLUSTER_LABEL[cluster])}</td>"
    f"<td class=sc>{total:.1f}</td>"
    + "".join(f"<td class=v>{vals[k]}</td>" for k in ORDER)
    + f"<td class=g>{' '.join(k for k, _ in fails)}</td></tr>"
    for i, (total, cluster, name, vals, fails) in enumerate(rows, 1)
)

ko_rows = "".join(
    f"<tr><td class=rl>{esc(name)}</td><td class=sc>{total:.1f}</td>"
    f"<td class=cl>{esc(CLUSTER_LABEL[cluster])}</td>"
    f"<td class=gr>{'; '.join(f'<b>{k}</b> — {esc(GATE_REASON[k])}' for k, _ in fails)}</td></tr>"
    for total, cluster, name, vals, fails in knocked
)

dim_rows = "".join(
    f"<tr><td class=code2>{k}</td><td class=w>{w}</td><td>{esc(n)}</td></tr>"
    for k, w, n, _ in DIMENSIONS
)

clusters = {}
for total, cluster, name, vals, fails in clean:
    clusters.setdefault(cluster, []).append(total)
cluster_rows = "".join(
    f"<tr><td class=rl>{esc(CLUSTER_LABEL[c])}</td><td class=v>{len(s)}</td>"
    f"<td class=sc>{sum(s)/len(s):.1f}</td></tr>"
    for c, s in sorted(clusters.items(), key=lambda x: -sum(x[1]) / len(x[1]))
)

HTML = f"""<title>Role Ranking — Offshore Talent Placement</title>
<style>
:root {{
  --paper:#eff1ef; --surface:#f7f8f6; --ink:#101618; --body:#394344;
  --dim:#7c8788; --rule:#d3d8d4; --hair:#e3e7e3;
  --accent:#0e5f63; --brass:#8f6217; --clay:#9a4a38;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,"Times New Roman",serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
}}
@media (prefers-color-scheme:dark) {{
  :root {{
    --paper:#0d1113; --surface:#151b1d; --ink:#e9eeec; --body:#aab4b3;
    --dim:#6f7a7a; --rule:#28312f; --hair:#1d2426;
    --accent:#48a5aa; --brass:#c99444; --clay:#c9705c;
  }}
}}
:root[data-theme=dark] {{
  --paper:#0d1113; --surface:#151b1d; --ink:#e9eeec; --body:#aab4b3;
  --dim:#6f7a7a; --rule:#28312f; --hair:#1d2426;
  --accent:#48a5aa; --brass:#c99444; --clay:#c9705c;
}}
:root[data-theme=light] {{
  --paper:#eff1ef; --surface:#f7f8f6; --ink:#101618; --body:#394344;
  --dim:#7c8788; --rule:#d3d8d4; --hair:#e3e7e3;
  --accent:#0e5f63; --brass:#8f6217; --clay:#9a4a38;
}}
* {{ box-sizing:border-box }}
body {{
  margin:0; background:var(--paper); color:var(--body);
  font:16px/1.6 var(--sans); -webkit-font-smoothing:antialiased;
}}
.wrap {{ max-width:840px; margin:0 auto; padding:0 24px }}
header {{ padding:64px 0 40px; display:flex; flex-direction:column; gap:18px }}
.eyebrow {{
  font:600 11px/1 var(--mono); letter-spacing:.16em; text-transform:uppercase;
  color:var(--accent);
}}
h1 {{
  font:400 clamp(32px,5.5vw,48px)/1.1 var(--serif); color:var(--ink);
  margin:0; letter-spacing:-.015em; text-wrap:balance;
}}
.standfirst {{ font-size:18px; max-width:60ch; margin:0 }}
.standfirst b {{ color:var(--ink); font-weight:600 }}

/* ---- compression band: the page's one graphic ---- */
.band {{
  background:var(--surface); border:1px solid var(--rule); border-radius:3px;
  padding:26px 26px 20px; display:flex; flex-direction:column; gap:14px;
}}
.band h2 {{ font:600 13px/1.3 var(--sans); color:var(--ink); margin:0; letter-spacing:.01em }}
.rail {{ position:relative; height:46px }}
.axis {{ position:absolute; left:0; right:0; top:30px; height:1px; background:var(--rule) }}
.tick {{ position:absolute; top:24px; width:1px; height:7px; background:var(--dim) }}
.tick b {{
  position:absolute; top:11px; left:50%; transform:translateX(-50%);
  font:500 10px/1 var(--mono); color:var(--dim); white-space:nowrap;
}}
.pop, .sel {{ position:absolute; border-radius:2px }}
.pop {{ top:12px; height:11px; background:var(--rule) }}
.sel {{ top:9px; height:17px; background:var(--brass); opacity:.9 }}
.sel span {{
  position:absolute; bottom:22px; left:50%; transform:translateX(-50%);
  font:600 10px/1 var(--mono); letter-spacing:.06em; color:var(--brass); white-space:nowrap;
}}
.legend {{ display:flex; flex-wrap:wrap; gap:20px; font-size:13px; color:var(--dim) }}
.legend i {{ width:20px; height:8px; border-radius:2px; display:inline-block; margin-right:7px }}

/* ---- scorecard rows ---- */
.list {{ display:flex; flex-direction:column }}
.row {{
  display:grid; grid-template-columns:52px 1fr 78px; gap:20px;
  padding:26px 0; border-top:1px solid var(--hair); align-items:start;
}}
.row:first-child {{ border-top:1px solid var(--rule) }}
.rank {{
  font:400 26px/1 var(--mono); color:var(--dim); text-align:right;
  padding-top:3px; font-variant-numeric:tabular-nums;
}}
.gold .rank {{ color:var(--brass) }}
.main {{ display:flex; flex-direction:column; gap:9px; min-width:0 }}
h3 {{ font:600 21px/1.25 var(--serif); color:var(--ink); margin:0; letter-spacing:-.005em }}
.meta {{ display:flex; gap:8px; flex-wrap:wrap }}
.chip {{
  font:500 10px/1 var(--mono); letter-spacing:.1em; text-transform:uppercase;
  color:var(--accent); border:1px solid currentColor; border-radius:2px;
  padding:5px 7px 4px;
}}
.reason {{ margin:0; max-width:58ch; font-size:15px }}
.caveat {{
  margin:2px 0 0; font-size:14px; color:var(--clay);
  border-left:2px solid currentColor; padding-left:12px; max-width:56ch;
}}
.caveat span {{
  display:block; font:600 10px/1 var(--mono); letter-spacing:.12em;
  text-transform:uppercase; margin-bottom:4px;
}}
.strip {{ display:flex; flex-wrap:wrap; gap:16px; margin-top:4px }}
.dim {{ display:flex; align-items:center; gap:6px }}
.code {{
  font:600 10px/1 var(--mono); letter-spacing:.06em; color:var(--dim); cursor:help;
}}
.dots {{ font-size:8px; letter-spacing:1.5px; line-height:1 }}
.dots .on {{ color:var(--accent) }}
.dots .off {{ color:var(--rule) }}
.score {{ text-align:right; font-family:var(--mono); font-variant-numeric:tabular-nums }}
.score b {{ display:block; font:500 24px/1 var(--mono); color:var(--ink) }}
.gold .score b {{ color:var(--brass) }}
.score span {{ display:block; font-size:10px; color:var(--dim); margin-top:5px; letter-spacing:.04em }}

/* ---- sections & tables ---- */
section {{ padding:52px 0 0 }}
h2.sec {{
  font:600 12px/1 var(--mono); letter-spacing:.15em; text-transform:uppercase;
  color:var(--accent); margin:0 0 8px;
}}
h2.sec + p {{ margin:0 0 20px; max-width:62ch; font-size:15px }}
.scroll {{ overflow-x:auto; border:1px solid var(--rule); border-radius:3px; background:var(--surface) }}
table {{ border-collapse:collapse; width:100%; font-size:13px }}
th {{
  text-align:left; font:600 10px/1 var(--mono); letter-spacing:.09em; text-transform:uppercase;
  color:var(--dim); padding:12px 9px; border-bottom:1px solid var(--rule);
  position:sticky; top:0; background:var(--surface); white-space:nowrap;
}}
td {{ padding:9px; border-bottom:1px solid var(--hair); vertical-align:top }}
tr:last-child td {{ border-bottom:0 }}
.n, .v, .sc, .w {{ font-family:var(--mono); font-variant-numeric:tabular-nums; text-align:right }}
.n, .v {{ color:var(--dim) }}
.sc {{ color:var(--ink); font-weight:500 }}
.rl {{ color:var(--ink); white-space:nowrap }}
.cl, .code2 {{ color:var(--dim); white-space:nowrap }}
.code2 {{ font-family:var(--mono); font-weight:600 }}
.g, .gr {{ color:var(--clay); font-family:var(--mono); font-size:11px }}
.gr {{ font-family:var(--sans); font-size:12px; min-width:22em }}
tr.ko .rl, tr.ko .sc {{ color:var(--dim); text-decoration:line-through; text-decoration-thickness:1px }}
.limits {{ display:flex; flex-direction:column; gap:0; border-top:1px solid var(--rule) }}
.limit {{ padding:16px 0; border-bottom:1px solid var(--hair); font-size:15px }}
.limit b {{ color:var(--ink); font-weight:600 }}
footer {{
  margin-top:56px; padding:26px 0 72px; border-top:1px solid var(--rule);
  font-size:13px; color:var(--dim);
}}
footer code {{ font-family:var(--mono); color:var(--body); font-size:12px }}
@media (max-width:620px) {{
  .row {{ grid-template-columns:36px 1fr; gap:14px }}
  .rank {{ font-size:20px }}
  .score {{ grid-column:2; text-align:left; display:flex; align-items:baseline; gap:8px }}
  .score b {{ font-size:20px }}
  .score span {{ margin:0 }}
  header {{ padding:44px 0 32px }}
}}
</style>

<div class=wrap>

<header>
  <p class=eyebrow>Offshore talent placement · role screen</p>
  <h1>Which role to place first</h1>
  <p class=standfirst>
    <b>{len(ROLES)} roles</b> scored across <b>{len(DIMENSIONS)} weighted dimensions</b>,
    then filtered by knockout gates applied after scoring — because a weighted average lets a
    fatal flaw be compensated by strengths elsewhere. <b>{len(clean)}</b> came through clean;
    <b>{len(knocked)}</b> were eliminated by a single fatal dimension.
  </p>

  <div class=band>
    <h2>Read this before you trust the order</h2>
    <div class=rail>
      <div class=axis></div>
      <div class=pop style="left:{all_lo}%;width:{all_hi - all_lo}%"></div>
      <div class=sel style="left:{t_lo}%;width:{t_hi - t_lo}%"><span>top 15 · {t_hi - t_lo:.1f} pts</span></div>
      {"".join(f'<div class=tick style="left:{v}%"><b>{v}</b></div>' for v in (0, 25, 50, 75, 100))}
    </div>
    <div class=legend>
      <span><i style="background:var(--rule)"></i>all {len(ROLES)} roles — {all_lo:.1f} to {all_hi:.1f}</span>
      <span><i style="background:var(--brass);opacity:.9"></i>the top 15 — {t_lo:.1f} to {t_hi:.1f}</span>
    </div>
    <p style="margin:0;font-size:14px">
      The fifteen below are separated by <b style="color:var(--ink)">{t_hi - t_lo:.1f} points out of
      100</b>. The model reliably tells a top-quartile role from a bottom-quartile one. It does not
      reliably tell #1 from #12. Treat these as a tied band and choose within it on judgment.
    </p>
  </div>
</header>

<div class=list>
{"".join(cards)}
</div>

<section>
  <h2 class=sec>What the model weighs</h2>
  <p>Weights sum to 100. Founder fit is deliberately set at 1 so enthusiasm cannot drive a
  result. Buyer remote-readiness is the dimension the earlier binary-filter method lacked
  entirely — it is what moved AEC from first place to twelfth.</p>
  <div class=scroll>
    <table>
      <thead><tr><th>Dim</th><th>Weight</th><th>Dimension</th></tr></thead>
      <tbody>{dim_rows}</tbody>
    </table>
  </div>
</section>

<section>
  <h2 class=sec>Cluster averages</h2>
  <p>Clean roles only. Marketing and Technology lead — both clusters that an earlier pass
  dismissed or omitted outright.</p>
  <div class=scroll>
    <table>
      <thead><tr><th>Cluster</th><th>Clean roles</th><th>Mean</th></tr></thead>
      <tbody>{cluster_rows}</tbody>
    </table>
  </div>
</section>

<section>
  <h2 class=sec>Eliminated by a gate — {len(knocked)} roles</h2>
  <p>A fatal dimension cannot be averaged away. Eleven of these scored inside the top-30 band and
  were still cut — including the executive assistant, the role both Somewhere and Oceans lead
  with, on the grounds that its quality cannot be tested before placement.</p>
  <div class=scroll>
    <table>
      <thead><tr><th>Role</th><th>Score</th><th>Cluster</th><th>Gate</th></tr></thead>
      <tbody>{ko_rows}</tbody>
    </table>
  </div>
</section>

<section>
  <h2 class=sec>All {len(ROLES)} roles, all scores</h2>
  <p>Struck-through rows failed a gate. Scroll sideways for the full dimension matrix.</p>
  <div class=scroll>
    <table>
      <thead><tr><th>#</th><th>Role</th><th>Cluster</th><th>Score</th>
      {"".join(f'<th title="{esc(DIM_NAME[k])} · weight {WEIGHTS[k]}">{k}</th>' for k in ORDER)}
      <th>Gate</th></tr></thead>
      <tbody>{ledger}</tbody>
    </table>
  </div>
</section>

<section>
  <h2 class=sec>Where this model is weak</h2>
  <div class=limits>
    <div class=limit><b>Scores are judgment, not measurement.</b> Around 2,500 cells were assigned
    from research and reasoning. Buyer remote-readiness in particular is an informed guess for
    most clusters.</div>
    <div class=limit><b>Dimensions correlate.</b> Gradeability and trainability move together, as
    do volume and reachability. Clusters strong on a correlated pair get inflated.</div>
    <div class=limit><b>Fourteen dimensions capped at 5 compress toward the mean.</b> The real
    range is {all_lo:.0f}–{all_hi:.0f} out of a theoretical 0–100.</div>
    <div class=limit><b>No interaction terms.</b> High volume combined with low reachability
    should penalise more than additively. It doesn't.</div>
    <div class=limit><b>Recruiter's cyclicality is under-weighted.</b> Recruiting demand is among
    the most hiring-cycle-sensitive functions in the economy. Retention scored 3; a case exists
    for 2.</div>
  </div>
</section>

<footer>
  Generated from <code>scoring/model.py</code> — weights are editable and the ranking
  regenerates. Full methodology, market data, unit economics and the decision history sit in
  <code>MASTER.md</code>. Nothing here has met a customer.
</footer>

</div>
"""

out = pathlib.Path(__file__).parent / "ranking.html"
out.write_text(HTML)
print(f"wrote {out} ({len(HTML):,} bytes) — {len(ROLES)} roles, {len(clean)} clean, {len(knocked)} knocked out")
