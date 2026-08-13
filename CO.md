# The `.co` Question

> **"Why not a good .co / Some of these seem so forced"**

You were right on both counts, and they turn out to be **the same point**. Here it is up front:

> **There is no good `.com`.** Across six screens and **1,160 authoritative `.com` checks** — every
> flowing dictionary word, every plain-speech hiring phrase, 704 generated collocations, the 141
> phrases a corpus says are real English, and 65 idioms — **the plain-English namespace for this
> business is exhausted.** Not thin. Exhausted: **zero** single words, **zero** idioms and **zero**
> hand-picked plain phrases are free.
>
> So insisting on `.com` was not a neutral preference. It was a **forcing function**. It is what
> converted single words into `Graded Crew` and `Verity People`. The forced names were a *symptom
> of my TLD rule*, and the rule was wrong.

---

## 1. First I had to make `.co` checkable at all

The previous screen refused to say anything about `.co` because **`.co` has no IANA RDAP bootstrap
entry and whois is unreachable from here.** That was honest and useless — the one TLD you asked
about was the one TLD I could not check.

[`scoring/dns_probe.py`](scoring/dns_probe.py) fixes it. An unregistered domain has no delegation,
so NS and SOA return NXDOMAIN. That proxy has exactly two failure modes, and **both are measured
rather than assumed:**

| Failure mode | Would break the result by | Measured |
|---|---|---|
| Registry DNS wildcard | making everything look taken | **None.** 3 garbage strings → NXDOMAIN on `.co` |
| Registered but undelegated | making a taken name look free | **0 of 82.** DoH and Verisign RDAP agreed on **82/82** real words |

So in every table below: **`.com`, `.net`, `.team`, `.works` and the other gTLDs are authoritative
RDAP.** `.co` is a **DNS proxy with a measured zero error rate over 82 trials** — good enough to
rank on, still worth confirming in the registrar cart before you pay. Two caveats I can't resolve
from here: `.co` reserves some dictionary words as **registry-premium** with a high one-time price,
and I have no price feed.

---

## 2. Why `.com` is worth less than I priced it — for *this* funnel specifically

The `.com` premium is real but it is not one thing. It is four costs, and **three of them are near
zero in a paid-acquisition business:**

| Where a TLD gets priced | Cost on `.co` | Why, in this model |
|---|---|---|
| **The acquisition click** | **~zero** | The click comes from a Meta ad. The buyer taps an image. **100% of new business arrives without anyone typing or really reading the domain.** |
| **Cold email deliverability** | **~zero** | Genuinely real for outbound-led businesses. This one has no outbound motion — [`MAP.md`](MAP.md) puts the entire funnel on paid Meta. |
| **Buyer trust at the close** | **~zero** | The close is done by the paid teardown, the graded work sample and the 12-month guarantee. Nobody paying $6k–$20k has been argued out of it by four letters after a dot. |
| **Recall and referral** | **real — and the only real one** | *"What was that company again?"* → types `.com` → lands somewhere else. §4 shows this cost is **per name**, not per TLD. |

Against that sits the cost of a forced name, which is paid **on every single impression**: a name
that reads as a product spec rather than a company makes the ad worse, and the ad is the only
acquisition channel that exists.

> The `.com` advantage is collected at **recall**. The forced compound's penalty is collected at
> **acquisition**. In a business where acquisition is 100% paid, that trade is not close.

---

## 3. "Forced" is measurable, and I had been guessing

Two rounds of names were scored against a `SAYS` dictionary **I wrote by hand with invented
numbers** — exactly the thing this project isn't supposed to contain. So naturalness got replaced
with two real measurements from Google Books via the Datamuse corpus API
([`scoring/collocation.py`](scoring/collocation.py)):

| What | Measured by | What it catches |
|---|---|---|
| **Common** — does anyone say this word | frequency per million | `verity` (0.5/M) vs `people` (555/M). *Verity flows beautifully and nobody says it.* |
| **Collocation** — do these two words ever co-occur | bigram score | `good hands` is attested. `graded crew` is not. |

And the headline number:

> **Of 4,488 modifier+noun pairs, only 142 — 3.2% — are attested English phrases.**

That is what "forced" is. `Graded Crew` and `Verity People` are two real words that **never occur
together in English**. They sit in the 96.8%. It was never about prosody; I was optimising the
wrong variable, twice.

---

## 4. The measurement: six rounds, and the namespace is gone

| Round | Register searched | Checked | Free on `.com` | Free on `.co` |
|---|---|---|---|---|
| 1 · [`co_names.py`](scoring/co_names.py) | flowing dictionary words — *verity, mettle, willow, sable* | 190 | **0** | 4 |
| 2 · [`plainspeech.py`](scoring/plainspeech.py) | plain workplace + selection speech — *all hands, deep bench, day one* | 60 | **0** | 5 |
| 3 · [`plain_sweep.py`](scoring/plain_sweep.py) | 704 generated collocations | 704 | 128 | — |
| 4 · [`collocation.py`](scoring/collocation.py) | the 141 phrases a **corpus** says are real | 141 | **10** | — |
| 6 · [`idioms.py`](scoring/idioms.py) | idioms — the register `All Hands` is in | 65 | **0** | 9 |
| | | **1,160** | | |

Read rounds 3 and 4 together, because that pair is the whole finding. Round 3 found 128 free names —
and round 4 shows **why** they were free: of the 141 phrases that are *real English*, **131 are
already taken**. The ten survivors are `stout people`, `tall office`, `hires staff`, `backed chair`.

> **Availability and naturalness are almost perfectly anticorrelated on `.com`.** Every name still
> free is free *because* it is not a phrase anyone says. That is the mechanism that produced two
> rounds of forced names, and no amount of further searching fixes it.

---

## 5. What the register you actually liked was

| You liked | You rejected | What separates them |
|---|---|---|
| **All Hands** | *Hold Fast* — "such a not common word" | common vs uncommon |
| **Teammate** | *Open Book* — "doesn't mean anything" | concrete vs decorative |
| **Tuesday**, *Monday Teams* | *Graded Crew*, *Verity People* — "so forced" | **speech vs spec** |

`All Hands` is an **idiom**. `Teammate` is one plain word. `Tuesday` is one plain, arbitrary word.
**None of them describes anything** — the buyer supplies the meaning. Every name you rejected tries
to specify the product *in the name*, which is a name doing a landing page's job. That's what
forced means, and rounds 1–4 had never once searched idioms.

---

## 6. Names killed by real data, not by taste

The most useful output of this screen. Each of these looked good and died on evidence:

| Name | Killed by | Source |
|---|---|---|
| **We Vouch / Us Vouch / Vouch For** | `vouchfor.com` → *"The AI content platform for **talent teams** \| Vouch"* — a live talent-tech brand | HTTP title |
| **Good Hands** | `goodhands.com` → **Allstate Insurance, "You're In Good Hands"** — one of the most famous ad slogans in America | HTTP title |
| **Monday Teams / Monday Talent** | `monday-talent.com` is a **live creative recruitment agency** — nearly your exact ICP. Plus monday.com holds the mark in software and "Teams" collides with Microsoft | web search + RDAP |
| **Sure Hands** | `surehands.com` → home mobility and ceiling lifts. The same US home-care register that killed *Safe Hands* | HTTP title |
| **Deep Bench / Bench Depth / The Whole Bench / Tuesday Bench** | **"bench sales recruiter" is Indian IT staffing's own term for the commodity end of this market.** Plus Bench Accounting and two Bench clothing brands | web search |
| **Tuesday Talent** | an existing **Facebook page** for freelance creatives, by that exact name — same platform you advertise on, adjacent audience | web search |
| **Shoe In** | `shoein` is the common *misspelling* of "shoo-in" | — |
| **The Legwork / Spadework** | both idioms mean *tedious groundwork* — positions premium talent as grunt labour | — |
| Cadence · Compass · Canon · Sterling | large trademarks; **Sterling Check** is adjacent (background screening) | [`scoring/co_names.py`](scoring/co_names.py) |

---

## 7. The finalists

Availability confirmed as of this run. `.com`/`.net`/`.team`/`.works` are RDAP; `.co` is the
calibrated DNS proxy.

| # | Domain | Why it isn't forced | The trade you're accepting |
|---|---|---|---|
| **1** | **`handpicked.team`** | **The dot is silent — it reads as "handpicked team".** Nothing is welded on, because the TLD *is* the second word. One everyday word that already means graded selection by a person, which is literally the offer (`FOUNDERGRADE` — you personally grade every placement). | `.team` is a low-trust nTLD. `handpicked.com` is Handpicked Hotels — unrelated sector, so a mistyped visit is an annoyance, not a competitor. "Handpicked" is generic, so trademark protection is weak. |
| **2** | **`tuesdaydesk.com`** | Plain arbitrary word + **"desk"**, which in agency, newsroom and trading speech means *a specialist team*. Arbitrary is not forced — Monday.com, Oyster, Deel and Gusto are all arbitrary. **Free on `.com` + `.co` + `.net` + `.team` + `.works`** — the whole defensive set, cheap. | *"The Tuesday desk"* can read as a shift rota. "Desk" reads as furniture to some. |
| **3** | **`tuesdayroster.com`** | **"Roster" names the retention asset** — the graded directory worth **+$9,022 per client** ([`HUNGRY.md`](HUNGRY.md) §9) — and carries none of the "bench" baggage. Same full availability set. | *"The Tuesday roster"* literally means who is working Tuesday. Slightly longer. |
| **4** | **`topdrawer.co`** | The strongest **pure premium idiom** still obtainable. Everyday British English for first-rate, and premium *is* the positioning. `.co`, `.team`, `.works` all free. | `topdrawer.com` sits behind a Cloudflare challenge — **live, contents unverified**, so I can't price the leak. British-flavoured. "Drawer" is furniture. |
| **5** | **`handiwork.co`** | One plain word meaning *the work of one's hands* — and it **contains "hand"**, the root of the one name you kept coming back to. `HAN-di-work` flows. Says craft without claiming it. | Same Cloudflare problem on `handiwork.com`. Points at output rather than at people. |
| **6** | **`tuesdayhires.com`** | The plainest and most literal of the set. No ambiguity at all. | Also the least distinctive — closest to a spec, which is where this started. |

Also free and worth knowing: `readymade.team`, `handpicked.works`, `wholenew.co`, `thursdaycrew.com`,
`tuesdaystaff.com`, `tuesdayhands.com`, `steadyhires.com`.

---

## 8. What I'd do

**`handpicked.team`** is the least forced name in six rounds, and it is the only one where the
domain *is* the phrase rather than a phrase plus a suffix. If the nTLD bothers you, **`tuesdaydesk.com`**
gets you a `.com`, your own preferred word, and every defensive TLD for the price of lunch.

Two things worth being explicit about:

- **`.co` turned out not to be the answer, but not for the reason I originally gave.** It is a
  perfectly good TLD for this funnel — my ranking was wrong and your instinct was right. It loses
  here on **supply**: only 4 of 190 dictionary words and 9 of 65 idioms are free on `.co` either.
  Fifteen years of exactly this reasoning got there first.
- **"No collision found" is not "no collision exists."** I searched the web and fetched each `.com`;
  I did not run a USPTO clearance search. Before you print anything, one paid trademark search in
  Class 35 (employment and staffing services) on whichever name you pick.

*Screens: [`dns_probe.py`](scoring/dns_probe.py) · [`co_names.py`](scoring/co_names.py) ·
[`plainspeech.py`](scoring/plainspeech.py) · [`plain_sweep.py`](scoring/plain_sweep.py) ·
[`collocation.py`](scoring/collocation.py) · [`finalists.py`](scoring/finalists.py) ·
[`idioms.py`](scoring/idioms.py)*
