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

---

## 9. Quick check: All Hands, Handpicked, and every TLD option

Requested directly, checked in one pass. `.com`/`.net`/gTLDs are authoritative RDAP; `.co` is the
calibrated DNS proxy from [`CO.md`](CO.md) §1.

| Rank | Domain | `.com` | `.co` | `.net` | Why here | The cost |
|---|---|---|---|---|---|---|
| **1** | **`allhandstalent.com`** | **free** | **free** | **free** | The name you have come back to three times. **`All Hands` is an idiom**, so it is not forced, and `Talent` is the most expansion-safe head noun there is — no role, no seniority, no vertical. **Full defensive set free for the price of lunch.** | *"All hands on deck"* leans **emergency and quantity**, which mildly fights premium selection. And the string contains **stale** if you squint at it |
| **2** | **`handpicked.team`** | *(hotels)* | taken | — | **The dot is silent — it reads as "handpicked team".** Structurally the least forced name in nine rounds: nothing is welded on, because the TLD *is* the second word. And it is literally the offer — you grade every placement personally | `.team` is a low-trust nTLD for a $6k–$20k sale. `handpicked.com` is Handpicked Hotels — wrong sector, so a mistyped visit is annoyance not competition. Generic word, weak trademark |
| **3** | **`allhandshiring.com`** | **free** | **free** | **free** | **The only All Hands variant that is completely clean** on every check — no accidental word at all. `H`-alliteration, and `Hiring` states the business cold | Slightly more transactional than `Talent`; 14 characters |
| **4** | **`lindenhires.com`** | **free** | **free** | **free** | Top of the systematic sweep. **The only nature word with no recruiting firm on it** | Linden, NJ surfaces in searches; means nothing, which you have said is fine |
| **5** | **`tuesdayhires.com`** | **free** | **free** | **free** | Arbitrary, warm, **outside the contested nature register entirely** | Means nothing; `Hires` is transactional |
| **6** | **`tuesdaytalent.com`** | **free** | **free** | **free** | Best flow of any Tuesday pairing | **An existing Facebook page uses this exact name** for freelance creatives — on the platform you advertise on |
| **7** | `handpicked.works` | — | — | — | "handpicked works" — the dot is silent here too | Reads as *work samples* rather than as people |
| **8** | `allhandsroster.com` | **free** | **free** | **free** | Names the graded directory — the retention asset | 14 characters, and `Roster` implies a fixed list |
| **9** | `allhandspeople.com` | **free** | **free** | **free** | Clean on every check | **Redundant** — hands *are* people |
| **10** | `allhandsstaff.com` | **free** | **free** | **free** | Clean, plain | `Staff` reads administrative and lower-ticket |

### Killed in this pass

| Domain | Killed by |
|---|---|
| **`allhandscrew.com`** | contains **screw**. `ARTIFACT`, hard gate |
| **`allhandshires.com`** | contains **shire** |
| **`handpickedcrew.com`** | adjective + noun — **the exact shape of `Graded Crew`**, which you rejected |
| `handpickedtalent.com` · `handpickedteam.com` · `handpickedhires.com` · `handpickedpeople.com` | all **taken** on `.com` — which is why `handpicked.team` is the workaround |
| `allhands.co` · `handpicked.co` · `linden.co` · `tuesday.co` | all **taken** — bare words on `.co` are gone, as [`CO.md`](CO.md) §4 found |
| every `.careers` option | **`linden.careers` reads as Linden's own job page.** Wrong direction for a firm that staffs *other* companies |
| `.group` · `.company` · `.agency` · `.studio` | taken for all four bare words |

**Free but weak TLDs**, for completeness: `allhands.house`, `allhands.partners`, `tuesday.house`,
`tuesday.partners`, `handpicked.house`, `handpicked.partners`, `linden.careers`.

> **The answer is `allhandstalent.com`.** It is the only candidate that is simultaneously an idiom
> (not forced), maximally expansion-safe (`Talent` locks nothing), clean when spelled aloud, and
> free across `.com`, `.co` and `.net`. `handpicked.team` is the better *name* and the worse *asset*.

---

## 10. One name, one TLD — so is there a better `.co`?

> **"1 good name on 1 tld is good enough… even if we can find something .co that's good"**

Dropping the defensive-set requirement is the right call, and it changes what to look for. Two
sweeps, run fast:

**Bare single words on `.co`.** 2,600 candidates — every 4-to-7-letter word in the common 20,000,
minus suffixed forms and function words, ranked by flow. **132 free, 5%.** And the survivors are
unusable: the list is web-corpus derived, so what is left is slurs, pharma spam, place names, and
`murder`, `torture`, `cancer`, `cruelty`, `junior`. The only three a business could use are
`refrain`, `radar` and `advance`, and all three are worse than what is already on the table.
**There is no good bare single word left on `.co`.**

**Compounds on `.co`.** 180 combinations of 30 clean first words × 6 head nouns: **175 free — 97%.**

> **So `.co` was never the constraint.** It is wide open. The constraint is that **every word that
> sounds good already has a recruiting firm on it**, and a firm's existence does not care which TLD
> you buy.

Which the checks confirm one more time. Each of these is free on `.co` and dead anyway:

| `.co` candidate | Free on `.co` | Killed by |
|---|---|---|
| `willowtalent.co` | yes | **Willow Staffing Agency LLC**, **Willow Tree Recruiting**, White Willow Staffing. And `willowtalent.com` is live |
| `aspentalent.co` | yes | **Aspen Careers** — legal staffing, 20+ years, four US offices |
| `quorumtalent.co` | yes | **Quorum Recruiting** — Denver, financial-systems talent, 8,000-strong network |
| `mainstaytalent.co` | yes | **Mainstays is Walmart's house brand** for bedding and home decor. Best *meaning* in the whole study — *"the person you rely on most"* — and it reads budget to every US buyer |
| `raventalent.co` | yes | `raventalent.com` is a live site |
| `larktalent.co` | yes | Lark Health |
| `harbortalent.co` | yes | crowded in healthcare and finance, plus the harbor/harbour spelling split |

**The two that survive on `.co`:** `braidtalent.co` (uncrowded, `braidtalent.com` is dark, but *braid*
means nothing for talent) and `besthands.co` (`besthands.com` is dark, but it reads as derivative of
Allstate's *"you're in good hands"*).

### And the check `allhandstalent.com` still needed

**There is no recruiting or staffing firm called All Hands.** Searched directly — the nearest
neighbours are AllStaff, AllSource Talent and The All Star Agency, none of which is the same name.
That is the one test it had not been put through, and it is the test that killed Heron, Alder,
Kestrel, Lantern, Trellis, Bison, Hawthorn, Willow, Aspen and Quorum.

> **`allhandstalent.com`.** It is the only candidate that is an idiom rather than a spec, carries
> **no recruiting firm on the word**, uses the most expansion-safe head noun in the category, spells
> cleanly when read aloud, and sits on `.com`. Nine rounds and roughly 6,000 domain checks did not
> produce anything better, and the `.co` sweep above shows the shortfall was never availability.
>
> Its two real costs, stated plainly: *"all hands on deck"* leans **emergency and quantity** against
> a premium selective positioning, and at 18 characters it is not short.

---

## 11. Top 20, consolidated

Every row **re-verified free in one pass** — `.com`/`.team`/`.works` by Verisign and Identity Digital
RDAP, `.co` by the calibrated DNS proxy. Ranked on your four criteria, with the cost of each stated
rather than buried.

| # | Domain | Reads as | Why it is here | What you accept |
|---|---|---|---|---|
| **1** | **`allhandstalent.com`** | All Hands Talent | **An idiom, so not forced**, and **no recruiting firm is called All Hands** — the test that killed ten other candidates. `Talent` locks no role, seniority or vertical | *"All hands on deck"* leans **emergency and quantity** against premium selection. 18 characters |
| **2** | **`allhandshiring.com`** | All Hands Hiring | Same word, and **the only All Hands variant with no accidental word in it at all.** `H`-alliteration; `Hiring` states the business cold | More transactional than `Talent` |
| **3** | **`lindenhires.com`** | Linden Hires | **The only nature word of eleven checked with no recruiting firm on it.** Warm, two syllables, one spelling | Linden, NJ surfaces in searches; Linden Lab made Second Life |
| **4** | **`lindenhiring.com`** | Linden Hiring | As above, with the stronger head noun | Same |
| **5** | **`tuesdayhires.com`** | Tuesday Hires | Arbitrary and warm, **outside the contested nature register entirely**, and it is the word you keep returning to | Means nothing — which you have said is fine |
| **6** | **`tuesdayhiring.com`** | Tuesday Hiring | As above | Same |
| **7** | **`handpicked.team`** | Handpicked Team | **The dot is silent.** Structurally the least forced name in nine rounds — nothing is welded on, because the TLD *is* the second word. And it is literally the offer | `.team` is a low-trust nTLD for a $6k–$20k sale; `handpicked.com` is Handpicked Hotels; generic word, weak trademark |
| **8** | `keeltalent.com` | Keel Talent | *"On an even keel."* Short, spellable, **no recruiting firm found** | Keel is a London no-code startup that raised $6M in 2024; two stresses collide |
| **9** | `keelhires.com` | Keel Hires | As above | Same |
| **10** | `allhandsroster.com` | All Hands Roster | **Names the graded directory** — the retention asset worth +$9,022 per client | `Roster` implies a fixed list; 18 characters |
| **11** | `tuesdayroster.com` | Tuesday Roster | Same logic, shorter first word | *"The Tuesday roster"* can read as a shift rota |
| **12** | `lindenroster.com` | Linden Roster | Same, on the cleanest first word | Same |
| **13** | `wrenhires.com` | Wren Hires | **No recruiting firm found.** Short and warm | **Wren** is a Y Combinator carbon-offset startup with real name recognition, and Wren Kitchens is large in the UK |
| **14** | `wrenhiring.com` | Wren Hiring | As above | Same |
| **15** | `tuesdaytalent.com` | Tuesday Talent | **The best-flowing Tuesday pairing** of the fourteen | **An existing Facebook page uses this exact name** for freelance creatives — on the platform you advertise on |
| **16** | `laureltalent.com` | Laurel Talent | No recruiting firm found; `LAU-rel TAL-ent` flows well | A given name, and *"resting on your laurels"* is the wrong idiom |
| **17** | `lindenpeople.com` | Linden People | Warmest head noun, on the cleanest word | `People` is **the most crowded head noun in staffing** |
| **18** | `handpicked.works` | Handpicked Works | The dot is silent here too | Reads as *work samples* rather than as people |
| **19** | `handpickedhiring.com` | Handpicked Hiring | `.com`, and *handpicked* is the promise | 16 characters, and it edges toward a spec |
| **20** | `allhandsstaff.com` | All Hands Staff | Clean on every check | `Staff` reads administrative and lower-ticket |

### Free, and deliberately left out

| Domain | Left out because |
|---|---|
| `wrentalent.com` | contains **rental** — w`REN-TAL`ent. `ARTIFACT`, hard gate |
| `birchhiring.com` · `birchhires.com` | **Birch Agency** is a live nationwide education staffing firm |
| `ridgehiring.com` | **Blue Ridge Executive Search** and **Ridgeline Talent Partners** |
| `thursdaytalent.com` | **Thursday is a well-known London and New York dating app** aimed at your exact ad audience |
| `tuesdaydesk.com` | `Desk` implies **one** desk, which fights expansion into all ICPs |
| `allhandspeople.com` | **redundant** — hands *are* people |
| `braidtalent.co` | free and uncrowded, but *braid* means nothing for talent |
| `besthands.co` | reads as derivative of Allstate's *"you're in good hands"* |
| `tenhands.co` | *ten hands* is five people — it **caps the offer** in the name |
| `allhandscrew.com` | contains **screw** |
| `allhandshires.com` | contains **shire** |
| `lindentalent.com` | contains **dental** |

---

## 12. `allhandstalent.com` bought — what to reserve now

### First: confirm the registration actually landed

At the time of writing, **Verisign RDAP still returns 404 and DNS returns NXDOMAIN** for
`allhandstalent.com`. `.com` registry propagation is normally seconds, so this is probably a
registrar-side queue or a pending payment check — but until the registry shows it, the name is not
yours and is still visible as available to anyone else running the check I have been running all
session. **Log into the registrar and confirm before doing anything below.**

### Tier 1 — squattable, and it blocks the business (today)

| What | Status | Why it cannot wait |
|---|---|---|
| **Facebook Page + username `/allhandstalent`** | **could not verify** — Facebook returns HTTP 400 to non-browser requests | **You cannot run a Meta ad without a Page.** The Page *is* the advertiser identity on every impression. Lose the username and you are `/allhandstalent.official` forever, which reads cheap in the exact ad a $6k–$20k buyer is judging. Check in the app now |
| **Instagram `@allhandstalent`** | **could not verify** — HTTP 429, rate-limited | IG placements carry a large share of Meta delivery, and the handle is on every one. Same reasoning, same urgency |
| **LinkedIn company page `/company/allhandstalent`** | **free** (404) | The single biggest trust asset for a Western buyer checking whether an unknown Indian operator is real — and where placement proof accumulates. Free |

### Tier 2 — cheap, with real downside if lost (this week)

| What | Status | Why |
|---|---|---|
| **`allhandstalent.co`** and **`.net`** | both **free** | Not brand vanity. A squatter or competitor on `.co` can run a **lookalike** — and a credibility attack is the one thing an operator with no Western track record cannot absorb. ~$40/yr for both |
| **YouTube `@allhandstalent`** | **free** (404) | Matters more here than for most businesses: the work sample in [`MODEL-V2.md`](MODEL-V2.md) gap 6 is *a recut ad with 3-second and 15-second retention measured against the original*. That is video. This is where the graded proof lives |
| **X `@allhandstalent`** | **free** (404) | 14 characters, inside the 15-character limit. And X is the launch-month media motion |
| **Google Workspace on the domain** | — | `name@allhandstalent.com` before the first ad runs. A gmail.com reply-to on a $6k–$20k offer is a conversion leak you never see |
| **`allhandtalent.com`** — singular *hand* | **free** | The one typo worth $12. Every other misspelling tested (`alhandstalent`, `allhandsstalent`, `allhandstalant`) is implausible |

### Skip

`.team`, `.works`, `.agency`, `.group`, `.company`, `.careers`, `.partners`, `.house`, `.studio` are
**all free for `allhandstalent`** — and all worthless. Nobody types them. Nine TLDs is ~$150/yr of
theatre. `.org` is free too; buy it only if a hostile complaints site is a fear you actually hold.
You said one good name on one TLD was enough and that was the right call — Tier 2 is about
*impersonation*, not coverage.

`allhandstalents.com`, `allhandtalents.com` and the rest: skip.

### Not a reservation, but the largest remaining exposure

**USPTO Class 35 clearance search, then an intent-to-use filing.** This has been outstanding for
three rounds. *All Hands* is close to generic, which is exactly why someone else can register it for
staffing services — and this study turned up **twelve live collisions** on other candidates by web
search alone. Search first, file second. Budget roughly $250–350 per class plus the search.

**One thing my check cannot tell you:** I verified there is no recruiting firm *called* All Hands,
but a registered mark can exist without a website that ranks. That gap is what the paid search closes.

---

## 13. Correction: my search method was the weak link, not the names

Asked whether people would have to type the domain, I searched the brand name plainly —
`all hands talent` — instead of my usual OR-joined query. That surfaced, immediately:

| What | Where | What it is |
|---|---|---|
| **All Hands** | [`all-hands.us`](https://www.all-hands.us/) | **A talent platform.** A curated candidate bank connecting talent with hiring partners, with a job board at `jobs.all-hands.us` and a *Companies* page for employers |
| **All Hands Technologies** | [`allhands-tech.com`](https://www.allhands-tech.com/) | **Recruitment services** — "finding perfect candidates who suit the company's work culture" |
| **All Hands & Hearts** | `allhandsandhearts.org` | A well-known disaster-relief nonprofit with real link equity for the phrase |

**So §10's claim — "there is no recruiting or staffing firm called All Hands" — was wrong.** The
query I used there was `"All Hands" recruiting staffing talent agency company OR "Mainstay" brand
company known for`, and OR-joined multi-term queries systematically under-surface the second and
third terms. It returned AllStaff, AllSource and All Star and missed two direct hits.

Re-testing the top alternative the same plain way, `linden talent hiring company`, produced
**[Linden Recruitment](https://uk.linkedin.com/company/lindenrecuitment)** (UK, IT and tech) and
**[Linden Staub Talent Agency](https://www.linkedin.com/company/lindenstaub)**. So §11's claim that
Linden was *"the only nature word of eleven with no recruiting firm on it"* was also wrong, and for
the same reason.

> **Every `no firm found` verdict in rounds six through eleven is unreliable** — Linden, Keel, Wren,
> Laurel, Mainstay and All Hands all received it from that query style, and two of the three I have
> now re-tested properly turned out to have live firms.

### Which makes the register finding stronger, not weaker

It was never about nature words. **There are tens of thousands of staffing agencies in the US
alone**, so a name collision in this industry is the *base rate*, not the exception. "Nobody else
uses this word" is not an achievable standard, and I spent three rounds implicitly treating it as
one. The achievable tests are narrower:

| Test | `allhandstalent.com` |
|---|---|
| **Does anyone hold the exact phrase?** | **No.** `all-hands.us` is *All Hands*; `allhands-tech.com` is *All Hands Technologies*; the nonprofit is *All Hands & Hearts*. **You own the `.com` of the exact phrase** |
| **Is there a registered mark in Class 35?** | **Unknown — and now urgent.** Two live users of *All Hands* in talent services materially raises the odds of an existing mark or an opposition |
| **Is there a domain conflict?** | **No** |

Against those three, **`allhandstalent.com` holds up, and switching is not clearly better** — the
alternatives are contaminated by the same base rate, and Linden fails the exact-phrase test *worse*,
because Linden Recruitment uses the bare word.

### The real cost of the name is the search result, not the character count

Yes, people will type it — at recall and referral, which is exactly the cost priced in
[`CO.md`](CO.md) §2 and which I should not have waved away with *"nobody types it"*. But the cost
lands as **SEO, not length**: typing *all hands talent* today returns three other organisations and
not you.

| Fix | Cost | Why it works |
|---|---|---|
| **Bid your own brand name on Google Search** — exact match `all hands talent` | a few dollars a month | Nobody else bids on it, so you are the top result for anyone who half-remembers you. This is the standard fix and it is near-free |
| **LinkedIn company page** | free | Exact-match brand queries rank a LinkedIn page fast, and it is already Tier 1 in §12 |
| **One consistent string everywhere** — `AllHandsTalent` camel-cased in writing, *All Hands Talent* spoken | free | The phrase accumulates as a single entity instead of three common words |

And the containment argument still holds: **acquisition is 100% paid Meta**, so the search problem
touches only recall and referral — the smaller half of the cost, as §2 of `CO.md` measured.

**On the original question:** 18 characters is not the problem. `velocityglobal.com` is 18;
`manpowergroup.com`, `kellyservices.com` and `insightglobal.com` are 17; the median of sixteen live
staffing and EOR domains is 14 and the max is 26. The handle at 14 clears every platform cap
including X's 15. **The name's weakness is that its words are common, not that its string is long.**

---

## 14. `.ai` — available, and the wrong signal

`allhandstalent.ai` is **free** (Identity Digital RDAP). So are `allhandshiring.ai`, `lindenhires.ai`
and `tuesdayhires.ai`. `allhands.ai` and `handpicked.ai` are taken.

**Cost:** `.ai` is an Anguilla ccTLD with a **mandatory two-year minimum**, roughly **$80–90/year at
registrar level, so ~$160–180 up front**, renewing in two-year blocks. The registry wholesale rose
$20 per registration on 5 March. That is **13–15× the price of the `.com` you already own**, which
raises the bar for what it has to buy you.

### The argument against is not cost, it is the comparator

The reason V2 beat V1 in [`MODEL-V2.md`](MODEL-V2.md) §8 is `TRUECLAIM` — **the arbitrage is true
against the video vendor invoice**, which is **$5,000–16,500 per month for a studio**, a 4.0–13.2×
claim and the largest in the study. That comparator is the entire justification for a $6,600
placement fee.

> **A `.ai` domain moves the comparator.** Read as an AI company, the buyer's mental reference class
> becomes AI video tools at **$20–100 a month** — not a studio at $5,000–16,500. You would be paying
> ~$170 to anchor yourself against a price point **50–800× below** the one your fee depends on.

Three smaller versions of the same problem:

| | |
|---|---|
| **It advertises your weakest score** | `DURABLE` = 3 was V2's lowest, because **generative video is the fastest-moving substitution risk in the study** ([`MODEL-V2.md`](MODEL-V2.md) gap 12). `.ai` does not hedge that — it invites the exact question you least want asked in a cold ad: *"so are these AI editors, and why do I need a person?"* |
| **It reads as bait-and-switch** | Click an `.ai` domain, land on a human-placement offer. Best case mild confusion; worst case the buyer feels misled — expensive when you have no Western track record and trust *is* the sale |
| **Defensive value is near zero** | `.ai` squatting targets AI-sounding names. *All Hands Talent* is not one. Nobody is racing you for it |

**The fair counter**, stated properly: recruiting-adjacent companies do use `.ai` — Metaview, Chorus,
Otter. But every one of those **sells software**. You sell a person. That difference is precisely
why the price anchor flips, rather than being an exception to it.

### Verdict

**Skip it.** If you want a third domain at all, `.co` and `.net` are both free for
`allhandstalent`, cost ~$40/year combined, and carry **no positioning cost** — strictly better uses
of the same money, and already Tier 2 in [`SUPPLY-DEMAND.md`](SUPPLY-DEMAND.md)'s sibling checklist
at §12 above.

**When it flips:** if the graded directory ever becomes *software* — a scoring or matching product —
that is a legitimate `.ai` sub-brand. Month twelve at the earliest, and even then it would be a
**product** name, not the company's.

*Unlike most of this repo, §14 is a judgement rather than a measurement. The availability and the
pricing are checked; the claim that `.ai` re-anchors the buyer is reasoning from the model's own
`TRUECLAIM` logic, not something I have data on.*
