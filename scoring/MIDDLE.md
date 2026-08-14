# What Actually Ports Across ICP × Role

> The middle slot of `LP → ??? → self-serve calendar`, decided on the dimension the
> enumeration was missing: **does it work unchanged across every cell we need to test?**

---

## 1. The volume calculator was wrong, and for a worse reason than "it's video-only"

It asks: *"what does your studio invoice **per ad**?"*

**No vendor in the study bills per unit.** From [`COMPETITORS.md`](COMPETITORS.md), fetched:

| Vendor | Billing |
|---|---|
| **Vidpros** — video | **$1,000/mo** part-time · **$4,000/mo** full-time |
| **Vidchops** — video | **Monthly subscription**, credits per month |
| Hireframe | **$2,500/mo** |
| GrowthAssistant | **$3,500/mo** |
| Athena · Oceans | Monthly |
| Design subscriptions, agency retainers, BPOs | Monthly |

> **Both video vendors bill monthly.** So the per-unit number the calculator asks for does
> not exist in the buyer's head even in the vertical it was designed for. They would have to
> divide a retainer by an output count to answer, and most cannot.

**And the structural error underneath it:** [`ALLFUNNELS.md`](ALLFUNNELS.md) ranked **149** funnels
with **no portability dimension at all.** I optimised for build simplicity and discovery
signal, and never scored the thing that was actually required.

`PORTABLE` is now a component property, taken as the **weakest link** across a funnel's
parts — because one non-porting component breaks the whole funnel — and weighted at **16**,
the heaviest. What that one change does:

| Offer | Ports | Best rank **before** | Best rank **now** |
|---|---|---|---|
| Volume calculator — units × vendor unit cost | **3** | **1st** | **62th** |
| Get a price / instant quote | **8** | 3rd | **2th** |
| See the graded bench | **5** | 5th | **12th** |
| Book a call | **10** | 8th | **7th** |
| Free document — scorecard, salary data, guide | **4** | 15th | **69th** |
| Watch a video first | **2** | 24th | **85th** |
| Paid micro-trial, $100–250 | **2** | 28th | **53th** |
| Free custom work on their asset | **2** | 60th | **42th** |

**The four options that need an asset rebuilt per role — video, free document, paid trial,
free custom work — were already losing. Portability just makes the reason explicit.**

---

## 2. What ports, ranked

| Offer | Ports | Best rank | Build days | Fields | `PERSUADE` | Score |
|---|---|---|---|---|---|---|
Traceback (most recent call last):
  File "/home/user/ad/scoring/middle.py", line 81, in <module>
    f"| {f.sc['PERSUADE']:.1f} | {f.total:.1f} |")
         ~~~~^^^^^^^^^^^^
KeyError: 'PERSUADE'
