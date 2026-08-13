# Arbitrary Word + Category Noun

> **"It doesn't need to mean something. It can be xx talent or yy team or zz hiring… should sound good and not forced · should not confuse people · should allow expansion into all ICPs and roles · should work on Meta ads or when someone spells it out."**

That instruction reopens the space, and it **invalidates the conclusion of [`CO.md`](CO.md) §4.**
Every earlier round required the name to be an attested English phrase or an idiom, which is why
that file found 3.2% attestation and called the namespace exhausted. **`Tiger Talent` needs no
bigram score** — it is a proper name plus a category label, which is how Oyster, Deel, Gusto,
Lattice and Rippling are all built.

**115 first words × 14 head nouns = 1610 authoritative Verisign RDAP checks. 764 are free on
`.com` — 47.5%**, against 0 of 190 single words and 0 of 65 idioms. The pattern was the
constraint, not the vocabulary.

---

## 1. Two things I had to fix first

Both were changing the answer, and both are the same mistake I made earlier in this project:

| Fault | What it did | Fix |
|---|---|---|
| **`CLEAR` was inferred by regexing my own prose notes** for words like *live*, *trademark*, *crowded* | The score depended on which adjectives I happened to type. Circular, and unauditable — the same failure as the invented `SAYS` dict in [`co_names.py`](scoring/co_names.py) | `CLEAR` is now an **explicit integer per word**, printed in §5 so it can be argued with |
| **No check on what a word MEANS** | The first run of this file ranked **`Summer Hiring` #1 and `Bronze Talent` #2.** Bronze is *the third-place medal*; summer and season say *temporary work*. Those are the two worst readings available to a premium permanent-placement business, and both scored clean | Words whose meaning fights the model are **blocked outright with the reason recorded** (§6) |

And one genuinely new automated check, because criterion 4 demanded it:

> **`ARTIFACT`** — concatenation creates words that neither half contained. `cove` + `talent` = **`covetalent.com`**, which contains *covet*; `linden` + `talent` = **`lindentalent.com`**, which contains *dental*. Any 5+ letter word straddling the join is found against a 370,000-word list, then **gated only if it is among the 20,000 most common English words** and is not merely a plural the head noun created. The first version gated on the full list and was useless — it fired on *ambers*, *aspens* and *adret*. A measurement, not a judgement.

---

## 2. The four criteria, weighted

| Criterion | Wt | Your words | How it is scored |
|---|---|---|---|
| **FLOW** | 24 | *should sound good and not forced* | Syllable count, stress collision and **junction clash**: `Cobalt Talent` loses 1.4 for the `t`+`T` pile-up, `Tiger Talent` gains 0.7 for alliteration |
| **SPELL** | 22 | *when someone spells it out* | **Real word frequency** (Datamuse/Google Books — a word you have seen written is one you can spell) **plus rule-based grapheme ambiguity**: `ph`, `ough`, terminal `-a`, soft `c`, doubled consonants, `x`, `z`, and a homophone list |
| **CLEAR** | 20 | *should not confuse people* | Brand collision and sector misread on a cold read, **for the first word and the head noun both** — `Teams` carries −1.5 for Microsoft Teams, `People` −0.8 as the most crowded head noun in staffing. Explicit per word in §5 |
| **EXPAND** | 16 | *expansion into all ICPs and roles* | The head noun must lock nothing — §4 |
| **META** | 18 | *should work on Meta ads* | Legible cold: short, and the **head noun does the explaining** so the ad does not have to |

**Gates, applied after scoring:** `ARTIFACT` (any accidental word across the join), `SPELL` < 3,
`CLEAR` < 3, `EXPAND` < 4.

---

## 3. Top 10

| # | Domain | Reads as | Flow | Spell | Clear | Expand | Meta | Score | The catch |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **`tuesdaytalent.com`** | Tuesday Talent | 4.9 | 3.7 | 4.0 | 5 | 4.4 | **88.0** | clean and arbitrary; the operator already likes it. Note a Facebook page called Tuesday Talent exists for freelance creatives — a real cost on `tuesdaytalent` specifically |
| **2** | **`lindenhiring.com`** | Linden Hiring | 4.7 | 3.2 | 4.0 | 5 | 5.0 | **86.7** | **the only nature word I checked with no recruiting firm on it.** Linden Lab (Second Life) is the notable brand; Linden, New Jersey is a real town, so 'linden staffing' searches surface geography |
| **3** | **`lindenhires.com`** | Linden Hires | 4.7 | 3.2 | 4.0 | 5 | 5.0 | **86.7** | **the only nature word I checked with no recruiting firm on it.** Linden Lab (Second Life) is the notable brand; Linden, New Jersey is a real town, so 'linden staffing' searches surface geography |
| **4** | **`tuesdayhires.com`** | Tuesday Hires | 4.1 | 3.7 | 4.0 | 5 | 5.0 | **86.0** | clean and arbitrary; the operator already likes it. Note a Facebook page called Tuesday Talent exists for freelance creatives — a real cost on `tuesdaytalent` specifically |
| **5** | **`ridgehiring.com`** | Ridge Hiring | 4.4 | 4.1 | 3.0 | 5 | 5.0 | **85.0** | **Blue Ridge Executive Search** and **Ridgeline Talent Partners** are compounds rather than bare 'Ridge', but the space is worked |
| **6** | **`tuesdaystaff.com`** | Tuesday Staff | 3.8 | 3.7 | 4.0 | 5 | 5.0 | **84.7** | clean and arbitrary; the operator already likes it. Note a Facebook page called Tuesday Talent exists for freelance creatives — a real cost on `tuesdaytalent` specifically |
| **7** | **`tuesdayhiring.com`** | Tuesday Hiring | 4.2 | 3.7 | 4.0 | 5 | 4.4 | **84.6** | clean and arbitrary; the operator already likes it. Note a Facebook page called Tuesday Talent exists for freelance creatives — a real cost on `tuesdaytalent` specifically |
| **8** | **`ravenhiring.com`** | Raven Hiring | 4.7 | 3.6 | 3.0 | 5 | 5.0 | **84.3** | a given name, and the Baltimore Ravens |
| **9** | **`ridgehires.com`** | Ridge Hires | 4.2 | 4.1 | 3.0 | 5 | 5.0 | **84.2** | **Blue Ridge Executive Search** and **Ridgeline Talent Partners** are compounds rather than bare 'Ridge', but the space is worked |
| **10** | **`thursdaytalent.com`** | Thursday Talent | 5.0 | 3.7 | 3.0 | 5 | 4.4 | **84.2** | **Thursday is a well-known London and New York dating app** — TechCrunch coverage, guerrilla marketing, and its audience is the same young Western urban professional you are advertising to on Meta |

### 11–30

| # | Domain | Flow | Spell | Clear | Score |
|---|---|---|---|---|---|
| 11 | `ravenhires.com` | 4.6 | 3.6 | 3.0 | 83.6 |
| 12 | `laureltalent.com` | 4.7 | 3.4 | 3.0 | 83.5 |
| 13 | `laurelhiring.com` | 4.7 | 3.4 | 3.0 | 83.5 |
| 14 | `laurelhires.com` | 4.7 | 3.4 | 3.0 | 83.5 |
| 15 | `hawkhires.com` | 4.5 | 3.5 | 3.0 | 83.0 |
| 16 | `lagoontalent.com` | 4.6 | 3.4 | 3.0 | 83.0 |
| 17 | `lagoonhiring.com` | 4.6 | 3.4 | 3.0 | 83.0 |
| 18 | `braidhiring.com` | 3.9 | 3.2 | 4.0 | 82.9 |
| 19 | `tandemhiring.com` | 4.6 | 3.3 | 3.0 | 82.9 |
| 20 | `rowantalent.com` | 4.7 | 3.2 | 3.0 | 82.7 |
| 21 | `rowanhiring.com` | 4.7 | 3.2 | 3.0 | 82.7 |
| 22 | `rowanhires.com` | 4.7 | 3.2 | 3.0 | 82.7 |
| 23 | `lindenpeople.com` | 4.5 | 3.2 | 3.2 | 82.7 |
| 24 | `maplehires.com` | 4.5 | 3.4 | 3.0 | 82.6 |
| 25 | `lagoonhires.com` | 4.5 | 3.4 | 3.0 | 82.4 |
| 26 | `tandemhires.com` | 4.5 | 3.3 | 3.0 | 82.3 |
| 27 | `wrenhiring.com` | 4.6 | 3.2 | 3.0 | 82.3 |
| 28 | `wrenhires.com` | 4.6 | 3.2 | 3.0 | 82.3 |
| 29 | `marlintalent.com` | 4.7 | 3.1 | 3.0 | 82.2 |
| 30 | `marlinhiring.com` | 4.7 | 3.1 | 3.0 | 82.2 |

---

## 4. Head nouns, ranked on expansion

**Criterion 3 is decided almost entirely here**, before the first word matters at all.

| Head noun | Expand | Note |
|---|---|---|
| **Hires** | 5 | the outcome; slightly transactional |
| **Hiring** | 5 | verb-as-noun; says what you do and reads clean cold |
| **People** | 5 | warmest and broadest, and the single most crowded head noun in staffing |
| **Staff** | 5 | plainest; reads administrative and lower-ticket |
| **Talent** | 5 | the clearest and most expansion-safe head noun in the category — it names no role, no seniority and no industry |
| **Team** | 5 | warm and singular; says the placed person joins *your* team |
| **Teams** | 5 | plural reads as the product, and it collides with Microsoft Teams |
| **Crew** | 4 | warm, faintly maritime and production-flavoured, so a mild role hint |
| **Group** | 4 | reads as a holding company: good for expansion, cold in an ad |
| **Partners** | 4 | consultancy register; implies equity partners |
| **Roster** | 4 | names the graded directory — the retention asset — but implies a fixed list |
| **Collective** | 3 | implies a co-op the talent owns — the wrong ownership story entirely |
| **Desk** | 3 | agency and newsroom for a specialist team; unknown to many buyers, and it implies **one** desk, which fights expansion |
| **Squad** | 3 | young and informal for a $6k–$20k sale |

---

## 5. Every first word, with its `CLEAR` score stated

This is the table to argue with. `CLEAR` is my read of a cold buyer plus what the web searches
and `.com` fetches turned up — **it is not a USPTO clearance search.**

| Word | Register | Clear | Freq/M | Note |
|---|---|---|---|---|
| birch | tree | **4** | 3.0 | clean; faintly Scandinavian-furniture |
| braid | abstract | **4** | 1.1 | strands woven into one thing; clean and uncrowded |
| daybreak | sky | **4** | 1.3 | clean; long |
| linden | tree | **4** | 1.0 | **the only nature word I checked with no recruiting firm on it.** Linden Lab (Second Life) is the notable brand; Linden, New Jersey is a real town, so 'linden staffing' searches surface geography |
| sycamore | tree | **4** | 0.5 | clean but long, and the spelling splits |
| tuesday | time | **4** | 6.2 | clean and arbitrary; the operator already likes it. Note a Facebook page called Tuesday Talent exists for freelance creatives — a real cost on `tuesdaytalent` specifically |
| willow | tree | **4** | 2.8 | warm; Willow is a cricket-streaming service, niche |
| alora | coined | **3** | 0.0 | pleasant and meaningless — the point is that it cannot survive being read aloud |
| aspen | tree | **3** | 1.3 | Aspen, Colorado — luxury ski, which is a *premium* signal |
| ballad | abstract | **3** | 2.4 | music |
| bellwether | abstract | **3** | 0.1 | the leader of the flock; long, and slightly literary |
| candor | abstract | **3** | 0.9 | several HR-tech uses, and the candor/candour split |
| clarity | abstract | **3** | 8.1 | many small consultancies use it |
| cohort | abstract | **3** | 3.5 | a group moving together; heavily used in edtech |
| elara | coined | **3** | 0.0 | as above |
| finch | animal | **3** | 1.4 | Finch is a live HR/payroll **API company** — adjacent enough to matter |
| garnet | mineral | **3** | 1.2 | jewellery |
| harbor | place | **3** | 10.7 | clean meaning — shelter — but healthcare and finance use it heavily, and the harbor/harbour split costs a spelling point |
| hawk | animal | **3** | 3.5 | sports mascots, and 'hawking' means peddling |
| ibex | animal | **3** | 0.2 | obscure, and `x` costs a spelling point |
| keel | abstract | **3** | 1.4 | **Keel** is a London no-code/ERP startup that raised $6M in 2024. Not in recruiting; 'on an even keel' still reads well |
| kira | coined | **3** | 0.3 | as above; Kira Systems is legal-tech |
| lagoon | place | **3** | 2.0 | reads as leisure |
| larch | tree | **3** | 0.4 | obscure; reads as timber |
| lark | animal | **3** | 1.0 | Lark Health is a funded US health app |
| laurel | tree | **3** | 2.4 | a given name; 'resting on laurels' is the wrong idiom |
| luma | coined | **3** | 0.1 | as above; Luma AI exists |
| maia | coined | **3** | 0.3 | as above |
| maple | tree | **3** | 2.7 | Canada and syrup |
| marlin | animal | **3** | 0.4 | reads as sportfishing |
| mesa | place | **3** | 1.8 | Mesa, Arizona |
| northstar | sky | **3** | 0.0 | aspirational and spellable, but used loosely everywhere |
| novara | coined | **3** | 0.1 | as above, and it is an Italian city |
| oak | tree | **3** | 8.9 | furniture and banking |
| orca | animal | **3** | 0.1 | whales; Orca is used in marine and in software |
| ovation | abstract | **3** | 0.5 | applause — acclaim without claiming it. Ovation Healthcare exists |
| pelican | animal | **3** | 0.9 | Pelican cases; clean otherwise |
| pewter | mineral | **3** | 0.6 | tableware; otherwise clean and uncrowded |
| raven | animal | **3** | 4.0 | a given name, and the Baltimore Ravens |
| redwood | tree | **3** | 1.0 | Redwood Software and Redwood Logistics are both sizeable |
| ridge | place | **3** | 12.4 | **Blue Ridge Executive Search** and **Ridgeline Talent Partners** are compounds rather than bare 'Ridge', but the space is worked |
| rowan | tree | **3** | 1.0 | a given name, and Rowan University |
| solara | coined | **3** | 0.0 | as above |
| sona | coined | **3** | 0.1 | as above |
| sparrow | animal | **3** | 1.7 | small — reads as minor, which is the wrong signal |
| stanza | abstract | **3** | 3.1 | clean but literary |
| tandem | abstract | **3** | 1.8 | two moving as one, which is the model. Tandem Bank and Tandem Diabetes both exist |
| teak | tree | **3** | 0.6 | furniture — though it is a South Asian hardwood, which is a quiet nod to where the talent is |
| thursday | time | **3** | 6.1 | **Thursday is a well-known London and New York dating app** — TechCrunch coverage, guerrilla marketing, and its audience is the same young Western urban professional you are advertising to on Meta |
| topaz | mineral | **3** | 0.4 | jewellery, and `z` splits the spelling |
| wren | animal | **3** | 1.1 | **Wren** is a Y Combinator carbon-offset startup with real name recognition in startup circles, and Wren Kitchens is large in the UK. Neither is in recruiting |
| altair | sky | **2** | 0.1 | engineering software |
| amber | mineral | **2** | 2.6 | a given name, and jewellery |
| aurora | sky | **2** | 1.8 | crowded brand token, **and heard as Arora, a common Indian surname** — which misrepresents a company as a person |
| banyan | tree | **2** | 0.4 | used in logistics and software; also specifically Indian |
| basin | place | **2** | 13.7 | plumbing |
| beacon | sky | **2** | 3.6 | crowded — healthcare, edtech, several staffing firms |
| bison | animal | **2** | 1.2 | **Iron Bison Talent Partners** and **The Bison Group** (IT staffing) both exist |
| cadre | abstract | **2** | 1.6 | exactly the right meaning — a trained core of personnel — but unspellable from speech and politically loaded |
| canyon | place | **2** | 6.1 | Canyon bicycles |
| clover | tree | **2** | 1.8 | Clover is a large POS brand |
| condor | animal | **2** | 0.5 | Condor is an airline |
| copper | mineral | **2** | 21.4 | metals trading, and British slang for police |
| coral | mineral | **2** | 4.7 | a given name, and reefs |
| crane | animal | **2** | 4.4 | reads as construction plant |
| dawn | sky | **2** | 12.8 | dish soap, and a given name |
| decade | time | **2** | 23.3 | reads as a span of time |
| dolphin | animal | **2** | 1.4 | leisure and pools |
| dune | place | **2** | 1.2 | the films |
| dusk | sky | **2** | 3.4 | faintly ominous |
| egret | animal | **2** | 0.2 | **Egret Consulting** is in executive search; Egret is also an e-scooter brand and Egret Technology in HTML5 games |
| elm | tree | **2** | 1.5 | the **Elm programming language**, **Elm Company** (a large Saudi digital firm) and **West Elm** furniture |
| emerald | mineral | **2** | 1.5 | jewellery |
| epoch | time | **2** | 3.7 | reads as machine-learning jargon |
| esteem | abstract | **2** | 9.8 | self-help register |
| falcon | animal | **2** | 1.5 | aerospace and heavy plant |
| fern | tree | **2** | 1.7 | a given name |
| friday | time | **2** | 11.0 | reads as the end of the week, and 'his man Friday' is a servant reference — actively wrong for a labour business |
| gazelle | animal | **2** | 0.5 | Gazelle is a US device-trade-in brand |
| haven | place | **2** | 11.5 | Haven was the Amazon/JPMorgan/Berkshire healthcare venture; also refuges and caravan parks |
| hawthorn | tree | **2** | 0.6 | **Hawthorne Lane** is a DC recruiting firm, and the hawthorn/hawthorne split costs a spelling point on top |
| hazel | tree | **2** | 2.2 | a given name |
| hickory | tree | **2** | 0.9 | smoked meat |
| highland | place | **2** | 3.0 | whisky |
| iron | mineral | **2** | 49.9 | ironmongery; reads industrial and cold for a people business |
| ivy | tree | **2** | 2.4 | a given name, and Ivy League implies elite universities |
| kite | animal | **2** | 1.3 | toys, and heard as the surname Kyte |
| lowland | place | **2** | 1.8 | reads as low |
| meridian | place | **2** | 2.2 | healthcare, and crowded generally |
| midland | place | **2** | 1.3 | banking |
| morning | time | **2** | 88.1 | reads as a time of day rather than a company |
| myrtle | tree | **2** | 1.0 | reads as an elderly given name |
| olive | tree | **2** | 6.7 | food, and a given name |
| onyx | mineral | **2** | 0.3 | faintly gothic, and `x` costs a spelling point |
| opal | mineral | **2** | 0.8 | jewellery |
| orion | sky | **2** | 1.0 | aerospace |
| osprey | animal | **2** | 0.3 | Osprey backpacks, and the aircraft |
| panther | animal | **2** | 1.4 | sports mascots |
| prairie | place | **2** | 5.0 | hard to spell |
| robin | animal | **2** | 6.2 | a given name, and Robinhood owns the bird space |
| sapphire | mineral | **2** | 0.9 | jewellery |
| sierra | place | **2** | 5.1 | vehicles and the Sierra Club |
| solstice | sky | **2** | 0.6 | hard to spell, and reads as annual |
| sonnet | abstract | **2** | 2.0 | also a Claude model name |
| sorrel | tree | **2** | 0.4 | obscure and hard to spell |
| spruce | tree | **2** | 2.2 | Spruce is a fintech; also 'spruce up' means superficial |
| steel | mineral | **2** | 39.0 | steel |
| summit | place | **2** | 7.6 | conferences — it would fight your own event marketing |
| swallow | animal | **2** | 4.8 | also a verb; awkward in a sentence |
| valley | place | **2** | 36.2 | Silicon Valley |
| vega | sky | **2** | 1.1 | crowded in finance and tech |
| verse | abstract | **2** | 19.6 | crowded |
| wednesday | time | **2** | 5.8 | the Netflix series, and the hardest weekday to spell |
| amity | abstract | **1** | 0.6 | **Amity University is one of India's largest private universities** — and you are selling Indian talent |
| magnolia | tree | **1** | 0.7 | the film, and the paint colour |

---

## 6. Blocked before checking — the meaning fights the model

| Word | Reason |
|---|---|
| **accord** | a Honda |
| **alder** | **Alder Koten** and **Alder Bowman Search Consultants** are both executive search firms. It was #5 |
| **atlas** | **Atlas is a live global-employment/EOR brand** — direct competitor |
| **autumn** | the season, plus a given name |
| **badger** | **'to badger' means to pester.** Actively wrong |
| **basalt** | quarrying |
| **beeline** | **Beeline is a large contingent-workforce management platform** |
| **bench** | 'bench sales' is Indian IT staffing's own term for the commodity end of this market |
| **bluff** | **'bluff' means to deceive.** Actively wrong for a trust business |
| **brass** | instruments, and 'brass' means senior officers |
| **bronze** | **the third-place medal.** Fatal for a premium talent brand — and it was #2 in the first draft of this screen |
| **cadence** | Cadence Design Systems |
| **canon** | Canon Inc. |
| **cascade** | dishwasher tablets |
| **chorus** | Chorus.ai — sales intelligence |
| **cobalt** | cobalt mining is synonymous with **child labour in the DRC**. For a labour business that is not a risk worth carrying |
| **comet** | cleaning products |
| **compass** | Compass Inc. |
| **cornerstone** | **Cornerstone OnDemand** — one of the largest HR software companies |
| **cove** | `covetalent.com` contains **covet** across the join — see the ARTIFACT check |
| **cypress** | Cypress Semiconductor, and the Cypress test framework |
| **delta** | an airline |
| **echo** | Amazon Echo |
| **eclipse** | the IDE |
| **ember** | the JavaScript framework |
| **equinox** | the gym chain |
| **flint** | Flint, Michigan — the water crisis |
| **granite** | worktops |
| **halo** | the video game |
| **heron** | **herontalent.com is a live executive search firm** (data/AI leadership, Nordics), plus Heron Global Recruitment, Heron Staffing and Heron Search. It was #1 and #2 in the first ranking of this file |
| **indigo** | **IndiGo is India's largest airline** — and you are selling Indian talent |
| **jaguar** | cars |
| **jasper** | **Jasper is a well-funded AI-writing brand** |
| **juniper** | **Juniper Networks** — large trademark |
| **kestrel** | **Kestrel Associates**, **Kestrel Recruitment**, **Kestrel Bay** and **Kestrel Partners** are all in recruitment |
| **lantern** | **Lantern Partners** (retained executive search, Chicago, founded 2003), **Lantern Recruitment** (UK creative) and **Lantern Staffing** all exist |
| **lattice** | **Lattice is a large HR platform** — direct adjacency |
| **lumen** | **Lumen Technologies** |
| **lynx** | **heard as 'links'** — a different word entirely |
| **lyric** | a health-tech brand |
| **marble** | stone worktops |
| **merlin** | reads as the wizard rather than the falcon |
| **monday** | monday-talent.com is a live creative recruitment agency at our ICP |
| **mulberry** | Mulberry — luxury handbags |
| **noon** | **Noon is a large Gulf e-commerce marketplace** |
| **nova** | extremely crowded |
| **otter** | **Otter.ai** — adjacent enough to confuse |
| **parity** | a blockchain firm |
| **plateau** | **'plateau' means growth stopped.** Actively wrong, and unspellable |
| **polaris** | vehicles |
| **poplar** | **heard as 'popular'.** Fatal for word of mouth and for radio |
| **puma** | sportswear |
| **quartz** | worktops and Quartz media |
| **savanna** | a cider brand, and the savanna/savannah split |
| **season** | same — 'seasonal staff' is the exact opposite of what is being sold |
| **sequoia** | **Sequoia Capital, and Sequoia Consulting Group is an HR/benefits firm** |
| **slate** | Slate magazine, and roofing |
| **spring** | the season, plus the Java framework |
| **stallion** | breeding, and it is male-gendered |
| **sterling** | Sterling Check — background screening, adjacent |
| **summer** | **says seasonal and temporary work**, the worst possible reading for a permanent-placement business. It was #1 in the first draft |
| **tempo** | an Atlassian-ecosystem brand |
| **tenor** | Google's GIF service |
| **titan** | crowded |
| **trellis** | **Trellis Talent** and **Talent Trellis** are both live recruiting firms |
| **tribute** | **funeral and memorial services** |
| **tundra** | a Toyota |
| **twilight** | the films |
| **unity** | the game engine |
| **vantage** | **Vantage Circle is an HR-tech company** |
| **vouch** | vouchfor.com is a live talent-tech brand |
| **zenith** | watches |

---

## 8. The finding that matters more than the ranking

**Pretty-nature-word + Talent is the recruiting industry's default naming convention.** It is the
first place every founder in this market reaches, which makes it simultaneously the most obvious
register and the most contested. I scored five of these `CLEAR` 5 — *nothing to explain* — and then
found live firms on every one:

| Word | I scored it | What is actually there |
|---|---|---|
| **Heron** | 5 — *#1 and #2 in the first ranking* | **herontalent.com is a live executive search firm** (data/AI leadership, Nordics), plus Heron Global Recruitment, Heron Staffing, Heron Search |
| **Alder** | 5 — *#5* | **Alder Koten** and **Alder Bowman Search Consultants**, both executive search |
| **Kestrel** | 5 | **Kestrel Associates**, **Kestrel Recruitment**, **Kestrel Bay**, **Kestrel Partners** |
| **Lantern** | 4 | **Lantern Partners** (retained search, Chicago, 2003), **Lantern Recruitment**, **Lantern Staffing** |
| **Trellis** | 4 | **Trellis Talent** *and* **Talent Trellis** |
| **Bison** | 4 | **Iron Bison Talent Partners**, **The Bison Group** |
| **Hawthorn** | 4 | **Hawthorne Lane**, DC recruiting |

> **The `.com` being free told me nothing about whether the name was taken.** These firms hold
> `herontalent.com`, `lanternpartners.com`, `trellistalent.io` — so the *pair* I was testing was
> free while the *word* was thoroughly occupied. RDAP cannot see that. Only searching for the
> business can.

Which produces the actual conclusion: **the two safest names are the ones that are not in that
register at all.**

| Pick | Why | Watch |
|---|---|---|
| **`lindenhires.com`** or **`lindenhiring.com`** | **Linden is the only nature word I checked with no recruiting firm on it.** Warm, two syllables, one spelling, and `Hires` / `Hiring` are the most expansion-safe head nouns there are — they name no role, no seniority, no industry | `lindentalent.com` is free but contains **dental** — do not buy it. Linden, New Jersey is a real town, so 'linden staffing' searches surface geography. Linden Lab made Second Life |
| **`tuesdayhires.com`** or **`tuesdayroster.com`** | Arbitrary, warm, **outside the contested register entirely**, and you already like the word. Arbitrary is not forced — Monday.com, Oyster, Deel and Gusto are all arbitrary | **`tuesdaytalent.com` is free but an existing Facebook page uses that exact name** for freelance creatives — the same platform you advertise on. `tuesdayteams.com` collides with Microsoft Teams |

`thursdaytalent.com` scores top of §3 and I would still not buy it: **Thursday is a well-known
London and New York dating app** whose audience is the same young urban professional you are
buying impressions against.

---

## 7. `ARTIFACT` hits — words the join invented

Gated. Each of these reads as a word that is in neither half of the name.

| Domain | Accidental word |
|---|---|
| `aspenteams.com` | **spent** |
| `daybreaksquad.com` | **breaks** |
| `daybreakstaff.com` | **breaks** |
| `decadeteam.com` | **cadet** |
| `decadeteams.com` | **cadet** |
| `egretroster.com` | **retro** |
| `fernstaff.com` | **ernst** |
| `hawthornsquad.com` | **horns** |
| `hawthornstaff.com` | **horns** |
| `highlandsquad.com` | **lands** |
| `lindentalent.com` | **dental** |
| `lowlandsquad.com` | **lands** |
| `lowlandstaff.com` | **lands** |
| `midlandsquad.com` | **lands** |
| `midlandstaff.com` | **lands** |
| `northstarroster.com` | **starr** |
| `northstarsquad.com` | **stars** |
| `oliveroster.com` | **oliver** |
| `olivestaff.com` | **lives** |
| `redwoodsquad.com` | **woods** |
| `stanzapartners.com` | **apart** |
| `swallowsquad.com` | **allows** |
| `swallowstaff.com` | **allows** |
| `wrentalent.com` | **rental** |

**`lindentalent.com` is the one that matters** — `linden` is otherwise the best-scoring first word
in the study, and `Linden Talent` is free. It contains **dental**. Use `lindenhiring.com` or
`lindenhires.com` instead, both of which are also free.
