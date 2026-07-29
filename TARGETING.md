# TARGETING — Meet Them Mid-Search

Every previous targeting analysis asked *"which vertical's owners happen to browse Facebook?"*
That is the wrong question. The right one:

> **Which companies are, right now, actively trying to fill a remote role — and how do I put an ad
> in front of that specific person while they are still looking?**

A vertical is a *static* attribute. A job posting is a **dated intent signal with an expiry.**
Companies in-market for a remote bookkeeper are in-market for roughly 30–60 days. Reaching them in
that window is not interruption — it is arrival.

---

## 1. The mechanism

Meta cannot target "company that posted a remote bookkeeper job." But it does not have to. You
build the audience yourself:

```
1. SCRAPE      job boards for "remote <role>" postings by US companies
                    ↓ (company name, role, salary, date posted)
2. ENRICH      owner / hiring manager → personal email + mobile
                    ↓ (Apollo, Clay, Findymail, Prospeo)
3. UPLOAD      as a Meta Custom Audience — Meta matches to personal FB/IG accounts
                    ↓
4. RUN ADS     directly at people who are mid-search, right now
                    ↓
5. LOOKALIKE   1% lookalike off that seed → scale far beyond the scraped list
```

**Steps 1–4 solve intent. Step 5 solves scale.** The scraped list might be 2,000 companies; the
lookalike built from it can be millions of profiles who *resemble* people who hire remote
bookkeepers.

### What has to be true, and the honest uncertainty

| Requirement | Reality |
|---|---|
| Custom Audience minimum | ~100 matched users to activate; **1,000+ for a usable lookalike seed** |
| B2B email match rate | **Low — roughly 20–40%** [E]. Business emails often are not the Facebook login |
| **Mobile number match rate** | **Materially better than email** [E]. Prioritise phone enrichment |
| Practical implication | You need **~3,000–5,000 enriched contacts** to yield a ~1,000-match seed |
| Compliance | Meta requires the list be lawfully obtained with a lawful basis. Scraped public job posts plus commercial enrichment is standard practice, but the terms are yours to honour |

⚠️ **The match rate is the load-bearing assumption and it is [E], not [V].** Test it with one
2,000-contact upload before building anything on top of it. Meta shows you the matched size
immediately, so this is a same-day test.

---

## 2. Sources, ranked by intent

### Tier 1 — proven offshore buyers (highest intent that exists)

These people have already decided to hire offshore. There is no education left to do.

| Source | Why it is Tier 1 |
|---|---|
| **OnlineJobs.ph employer postings** | **2M+ worker profiles**; employers pay a flat monthly subscription to post [V]. Every poster is a US company paying money to hire Filipino staff. **The single highest-intent list in this business** |
| **Upwork job posts** filtered to the role + country preference | Public, dated, role-specific |
| **Competitors' live job boards** — Somewhere (`apply.workable.com/jobssomewhere`), Pearl Talent, Wing, MyOutDesk | Their open reqs are *their clients' unfilled roles*. Anonymised, but role, salary and often industry are visible |
| Facebook groups for offshore hiring — OnlineJobs.ph employers, "Hire Filipino VAs", e-comm hiring groups | Native Meta surface. You can engage *and* build audiences |

**The sharpest play in Tier 1:** companies that posted on OnlineJobs.ph or Upwork **and did not
fill the role.** A stale unfilled post is a frustrated buyer with proven offshore intent — the
warmest prospect available anywhere.

### Tier 2 — remote-role intent, offshore not yet decided

| Source | Note |
|---|---|
| **Accountingfly** | Accounting-specific remote job board. Exactly our role, exactly our intent |
| We Work Remotely · RemoteOK · Remotive · JustRemote · Working Nomads · FlexJobs | Remote-first boards; scrapeable |
| **Indeed** with the remote filter | Largest volume by far |
| LinkedIn Jobs (remote) · ZipRecruiter · Google Jobs | Volume, harder to scrape |

### Tier 3 — ICP fit, no hiring intent

Storeleads and BuiltWith for Shopify + A2X · Clutch for agencies · state registries. Useful for
cold email, **not** for Meta — a named list is not an audience.

---

## 3. What to actually run on Meta

Three layers, in the order you should build them:

| Layer | Audience | Expected volume | Expected CPL |
|---|---|---|---|
| **1. Intent seed** | Custom Audience from scraped job posters | Small — hundreds to low thousands | **Lowest** — they are mid-search |
| **2. Lookalike** | 1% lookalike off layer 1 | Millions | Low-mid |
| **3. Broad + hook** | Near-broad targeting, creative does the qualifying | Unlimited | Highest, but scales |

**Layer 3 deserves explaining, because it is counter-intuitive.** Meta's B2B interest targeting is
weak — "small business owner" is enormous and imprecise. But Advantage+ with near-broad targeting
plus a **hook that only one person responds to** works better than tight targeting. The creative
does the qualifying, not the audience.

### The hook has to name the moment, not the service

| ❌ Generic | ✅ Names the moment they are in |
|---|---|
| "Hire offshore accountants" | **"Still trying to fill that bookkeeper role?"** |
| "Save 70% on payroll" | **"Your bookkeeper posting has been up 6 weeks. We can fill it in 21 days."** |
| "Top 1% remote talent" | **"You posted for a remote bookkeeper. Here are three, graded, today."** |
| "Offshore staffing solutions" | **"$20,000/yr instead of $75,000. Same QuickBooks, same Xero, same close."** |

The second and third only work at scale if you have the intent list — which is the point of §1.
**On the intent seed you can be specific enough to feel like a coincidence.**

---

## 4. Where the signal is thickest

Not all role × vertical pairs post at the same volume. Ranked by how much scrapeable intent exists:

| Role posted remotely | Signal volume | Where it concentrates |
|---|---|---|
| **Bookkeeper / accountant** | **Very high** | OnlineJobs.ph, Accountingfly, Indeed, Upwork |
| Executive assistant / VA | **Highest of all** | OnlineJobs.ph dominates — but the role fails our gradeability gate |
| **AP / AR specialist** | **High** | Indeed, OnlineJobs.ph |
| Customer support | Very high | OnlineJobs.ph — fails our async gate |
| **Paid media / PPC specialist** | High | Upwork, agency boards |
| **Medical biller / coder** | High | Indeed, healthcare boards |
| Data entry | High | OnlineJobs.ph — fails our AI gate |
| Steel detailer / CAD | **Low** | Scarce postings. Buyers use engineering networks, not job boards |

> **The three that pass our gates AND have thick signal: bookkeeper/accountant, AP/AR specialist,
> paid media operations.** Everything with more signal fails a gate; everything that passes a gate
> more cleanly has thinner signal.

**And note what this does to the AEC question:** steel detailing kept scoring well on worker
economics and kept failing on buyer readiness. Here it fails again, for a new reason — **there is
almost no scrapeable hiring intent.** That is now three independent screens pointing the same way.

---

## 5. What this changes

| # | Change |
|---|---|
| 1 | **The seed audience is a scraping and enrichment problem, not a media-buying problem.** The first build is a job-post scraper plus an enrichment pipeline, not an ad account |
| 2 | **OnlineJobs.ph is the highest-intent source available** and it is not a competitor — it is a directory of proven offshore buyers |
| 3 | **Competitors' job boards are prospect lists.** Somewhere's open reqs are their clients' unfilled roles |
| 4 | **Stale unfilled postings are the warmest segment in the business.** Proven intent plus proven frustration |
| 5 | **`META` as a vertical score matters less than I claimed.** With a custom-audience seed you are targeting *people*, not verticals — so MSP, SaaS and staffing agencies come back into play despite living on LinkedIn |
| 6 | **Test the match rate first.** One 2,000-contact upload, same-day answer. Everything else depends on it |

**Point 5 is the important one.** I gated three verticals out on Meta-targetability. That gate was
right when the plan was interest-based targeting and wrong now — a custom audience built from job
postings does not care whether the owner's *interests* look B2B, only whether their phone number
matches a Facebook account.
