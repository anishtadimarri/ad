#!/usr/bin/env python3
"""
Role scoring model for the offshore talent placement business.

Methodology:
  1. 14 weighted dimensions, each scored 0-5 (anchors in DIMENSIONS below).
  2. Weighted score = sum(weight * raw/5), normalised to 0-100.
  3. Knockout gates applied AFTER scoring. A weighted average lets a fatal
     flaw be compensated by strengths elsewhere; the gates prevent that.

Run:  python3 scoring/model.py > scoring/RANKING.md
"""

# ---------------------------------------------------------------- dimensions

DIMENSIONS = [
    # key, weight, name, anchors
    ("V",  11, "Seat volume",
     "5=>500k US seats  4=150-500k  3=50-150k  2=15-50k  1=5-15k  0=<5k"),
    ("D",   9, "Fee per placement",
     "35% of offshore salary. 5=$14k+ fee  4=$10-14k  3=$7-10k  2=$5-7k  1=$3.5-5k  0=<$3.5k"),
    ("RR", 11, "Buyer remote-readiness",
     "Will this buyer actually hire an offshore FTE? 5=already default  0=essentially never"),
    ("OP",  7, "Outsourcing precedent",
     "Proven offshore at scale? 5=massive established industry  0=none"),
    ("CD",  5, "Competitive whitespace",
     "INVERSE density. 5=nobody focused on it  0=a $300M+ incumbent owns it"),
    ("G",   9, "Gradeability",
     "5=objective right answer, machine-checkable  2=portfolio/subjective  0=pure relationship"),
    ("T",   7, "Trainability / academy cost",
     "5=free public curriculum exists  3=buildable in-house  0=innate, not trainable"),
    ("R",  12, "Retention",
     "Composite: async + escape risk + local counter-bid + seasonality. 5=all clear  0=three+ negatives"),
    ("AI",  8, "AI durability (5yr)",
     "5=judgment/regulated/liability-bearing  3=partially exposed  0=actively being eaten"),
    ("RP",  5, "Repeat / expansion",
     "Placements per client. 5=clients hire teams  3=2-3  1=one and done"),
    ("BR",  6, "Buyer reachability",
     "Meta / cold email targetability. 5=broad self-identifying audience  1=needs 1:1 outbound"),
    ("SL",  6, "Supply liquidity",
     "Can we fill in <=14 days from India/PH/SA? 5=abundant  1=scarce"),
    ("RF",  3, "Regulatory freedom",
     "INVERSE friction. 5=none  3=contractual/data only  1=licensing/UPL/HIPAA heavy"),
    ("FF",  1, "Founder fit",
     "5=founder is the domain expert  0=no connection"),
]

WEIGHTS = {k: w for k, w, _, _ in DIMENSIONS}
assert sum(WEIGHTS.values()) == 100, sum(WEIGHTS.values())

ORDER = [k for k, _, _, _ in DIMENSIONS]

# Knockout gates: a fatal flaw that strengths elsewhere cannot compensate.
GATES = [
    ("R",  1, "retention fatal — role churns faster than it can be replaced"),
    ("AI", 1, "role disappears under you inside 5 years"),
    ("G",  1, "quality cannot be tested, so it cannot be promised"),
]

# ------------------------------------------------------------------- roles
# (cluster, role, V, D, RR, OP, CD, G, T, R, AI, RP, BR, SL, RF, FF)

ROLES = [
    # ---------------------------------------------- FINANCE & ACCOUNTING
    ("Finance", "Bookkeeper",                    5,2,5,5,1,5,5,3,2,3,5,5,4,2),
    ("Finance", "AP clerk",                      4,1,5,5,1,5,5,3,1,3,4,5,4,2),
    ("Finance", "AR / collections",              4,2,4,4,2,4,4,3,2,3,4,4,4,2),
    ("Finance", "Payroll specialist",            3,2,3,3,3,5,4,5,3,2,3,3,3,1),
    ("Finance", "Staff accountant",              5,3,4,5,1,5,4,3,3,3,5,4,4,2),
    ("Finance", "Senior accountant",             4,4,4,5,1,5,3,3,4,2,4,3,4,2),
    ("Finance", "Controller",                    2,5,2,2,4,4,2,4,5,1,2,2,4,1),
    ("Finance", "Financial analyst",             3,3,4,3,3,4,3,3,3,2,3,4,4,2),
    ("Finance", "FP&A analyst",                  2,4,3,2,4,4,3,3,3,2,2,3,4,1),
    ("Finance", "Tax preparer",                  4,3,4,5,1,5,4,1,3,3,4,4,3,1),
    ("Finance", "Audit associate",                3,3,3,4,1,4,3,2,3,3,3,3,3,1),
    ("Finance", "Paraplanner (RIA)",             2,3,3,2,4,4,5,5,4,2,3,3,3,1),
    ("Finance", "Fund accountant",               2,4,3,5,1,4,3,3,4,3,1,3,3,0),
    ("Finance", "Billing specialist",            4,1,4,4,2,4,5,3,2,3,3,5,4,1),
    ("Finance", "Credit analyst",                2,3,3,3,3,4,3,4,3,2,2,3,3,0),
    ("Finance", "Cost accountant",               2,3,2,2,4,4,3,4,4,1,2,2,4,0),
    ("Finance", "Revenue accountant",            2,4,4,3,4,4,3,4,4,2,2,2,4,0),
    ("Finance", "Treasury analyst",              1,4,2,2,4,4,3,4,4,1,1,2,3,0),
    ("Finance", "Expense auditor",               2,1,4,4,3,5,5,3,1,2,2,5,4,1),
    ("Finance", "Reconciliation specialist",     3,1,4,5,2,5,5,3,2,3,3,5,4,1),

    # ------------------------------------------------------------- LEGAL
    ("Legal", "Litigation paralegal",            3,3,3,3,3,4,4,4,3,2,3,4,2,1),
    ("Legal", "PI case manager",                 3,3,4,3,4,4,4,4,4,3,4,4,2,1),
    ("Legal", "Immigration paralegal",           2,3,4,4,3,4,4,4,3,3,3,4,2,1),
    ("Legal", "Estate planning paralegal",       2,3,3,2,4,4,4,4,3,2,3,3,2,0),
    ("Legal", "Corporate / IP paralegal",        2,3,3,4,3,4,3,4,3,2,2,3,2,0),
    ("Legal", "Legal intake specialist",         3,1,3,3,3,3,5,2,2,2,4,5,3,1),
    ("Legal", "Docketing clerk",                 2,2,3,4,3,5,5,4,2,2,2,4,3,0),
    ("Legal", "E-discovery reviewer",            2,2,4,5,1,4,4,3,0,3,2,4,2,0),
    ("Legal", "Contract analyst / CLM",          2,3,4,3,3,4,3,4,2,2,2,3,3,0),
    ("Legal", "Title examiner / abstractor",     3,2,3,4,2,5,4,2,3,3,3,3,3,0),
    ("Legal", "Lien / subrogation specialist",   2,2,4,4,3,4,4,4,4,3,2,4,3,0),
    ("Legal", "Medical record retrieval",        3,1,4,5,2,4,5,3,2,4,3,5,2,0),
    ("Legal", "Deposition summarizer",           2,2,4,4,2,4,4,3,1,3,2,4,3,0),
    ("Legal", "Demand letter writer",            2,2,4,3,3,3,4,3,1,3,3,4,2,0),
    ("Legal", "Patent search / illustration",    1,3,4,5,2,5,3,4,3,2,1,3,3,0),

    # -------------------------------------------------- HEALTHCARE ADMIN
    ("Healthcare", "Medical biller",             5,1,5,5,0,4,5,3,2,4,4,5,2,1),
    ("Healthcare", "Medical coder (CPC)",        4,2,5,5,0,5,5,3,2,4,3,5,2,1),
    ("Healthcare", "Prior authorization",        4,1,5,5,1,4,5,2,2,4,4,5,2,1),
    ("Healthcare", "Denial management / RCM",    4,2,5,5,0,4,4,3,3,4,3,4,2,1),
    ("Healthcare", "Credentialing specialist",   3,2,4,4,3,5,5,4,4,3,3,4,2,0),
    ("Healthcare", "Virtual scribe",             4,1,5,5,1,3,4,2,0,4,4,5,2,0),
    ("Healthcare", "Insurance verification",     4,1,5,5,1,4,5,2,1,4,4,5,2,0),
    ("Healthcare", "ROI / records",              3,1,4,5,2,4,5,3,2,3,2,5,2,0),
    ("Healthcare", "Chart auditor",              2,2,4,4,2,5,4,4,3,2,2,3,2,0),
    ("Healthcare", "HEDIS abstractor",           2,2,4,4,2,5,4,2,3,3,1,3,2,0),
    ("Healthcare", "Utilization review",         2,3,3,3,3,4,3,4,4,2,2,2,1,0),
    ("Healthcare", "Care coordinator",           3,2,3,3,3,3,4,2,3,3,3,4,2,0),
    ("Healthcare", "DME billing",                2,1,4,4,2,4,5,3,2,3,2,4,2,0),
    ("Healthcare", "Dental insurance verif.",    3,1,4,4,2,4,5,2,1,3,4,5,2,1),

    # --------------------------------------------------------- INSURANCE
    ("Insurance", "COI issuance",                3,1,4,4,1,5,5,5,2,4,3,5,4,0),
    ("Insurance", "Policy checking",             3,2,4,4,1,5,5,5,2,4,3,4,4,0),
    ("Insurance", "Endorsement processing",      3,2,4,4,1,5,5,5,2,4,3,4,4,0),
    ("Insurance", "Commercial lines processor",  3,2,4,4,2,4,4,4,3,4,3,4,3,0),
    ("Insurance", "Personal lines CSR",          4,1,4,4,2,3,4,1,2,4,3,5,2,0),
    ("Insurance", "Claims processor",            4,2,4,5,1,4,4,3,2,4,2,4,3,0),
    ("Insurance", "Subrogation specialist",      2,2,4,4,3,4,4,4,4,3,2,3,3,0),
    ("Insurance", "Loss run analysis",           2,2,4,3,4,5,5,5,3,3,2,4,4,0),
    ("Insurance", "Underwriting assistant",      3,2,3,4,3,4,4,4,3,3,2,4,3,0),
    ("Insurance", "Premium audit",               2,2,3,3,4,4,4,4,4,2,2,3,3,0),
    ("Insurance", "Medical bill review",         2,2,4,4,3,5,4,4,3,3,2,3,2,0),
    ("Insurance", "IME coordination",            1,1,3,3,4,3,5,2,2,3,1,4,2,0),
    ("Insurance", "Benefits analyst",            2,3,3,3,4,4,4,4,4,2,2,3,2,0),

    # ------------------------------------------------ REAL ESTATE & LENDING
    ("RealEstate", "Transaction coordinator",    4,1,5,5,1,4,5,3,2,3,5,5,3,1),
    ("RealEstate", "Leasing coordinator",        3,1,4,4,2,3,5,2,2,4,4,5,3,0),
    ("RealEstate", "Property mgmt admin",        4,1,4,4,2,3,5,3,2,4,4,5,3,1),
    ("RealEstate", "HOA admin",                  2,1,3,3,4,4,5,4,3,3,2,4,3,0),
    ("RealEstate", "Maintenance dispatch",       3,1,4,4,2,3,5,1,2,4,3,5,3,0),
    ("RealEstate", "Real estate ISA",            3,1,4,4,2,2,3,1,2,3,4,5,2,1),
    ("RealEstate", "Mortgage processor",         3,2,4,5,1,5,4,1,3,4,3,4,2,0),
    ("RealEstate", "Mortgage underwriting asst", 2,3,3,4,2,5,4,1,3,3,2,3,2,0),
    ("RealEstate", "Post-closing auditor",       2,1,4,5,2,5,5,1,3,3,2,4,2,0),
    ("RealEstate", "Escrow assistant",           2,2,3,3,3,4,4,1,3,3,2,3,2,0),
    ("RealEstate", "CAM reconciliation",         1,2,3,3,4,5,4,4,4,2,1,3,4,0),
    ("RealEstate", "RE acquisitions analyst",    1,4,4,2,4,4,3,3,4,1,2,3,4,0),
    ("RealEstate", "Property accountant",        3,2,4,4,2,5,4,4,3,3,3,4,4,0),
    ("RealEstate", "Appraisal support",          2,2,3,3,3,4,4,2,3,2,2,3,2,0),

    # ------------------------------------------------- AEC / CONSTRUCTION
    ("AEC", "Construction estimator / takeoff",  4,3,2,3,4,5,3,5,4,2,3,3,5,0),
    ("AEC", "Steel detailer (Tekla/SDS2)",       2,4,3,5,3,5,3,5,4,2,2,3,5,0),
    ("AEC", "Rebar detailer",                    1,3,3,5,3,5,4,5,4,2,1,3,5,0),
    ("AEC", "MEP designer",                      3,4,3,4,3,5,3,5,4,2,2,3,5,0),
    ("AEC", "CAD drafter",                       4,2,3,5,2,5,4,4,3,3,3,5,5,0),
    ("AEC", "BIM modeler",                       3,3,3,5,2,5,4,4,3,3,2,4,5,0),
    ("AEC", "Clash detection / coordination",    2,3,3,4,3,5,4,5,4,2,1,3,5,0),
    ("AEC", "Shop drawing specialist",           2,3,3,4,3,5,4,5,4,2,1,3,5,0),
    ("AEC", "Scheduler (P6)",                    2,3,3,3,4,4,3,4,4,1,2,2,5,0),
    ("AEC", "Submittal / RFI coordinator",       3,2,3,3,4,4,5,4,3,2,2,4,5,0),
    ("AEC", "As-built drafter",                  2,2,3,5,2,5,5,4,3,2,1,5,5,0),
    ("AEC", "Architectural production / CD",     3,3,3,5,2,5,3,4,3,3,2,4,5,0),
    ("AEC", "Solar PV design / permit sets",     2,2,4,5,2,5,5,1,3,4,3,4,4,0),
    ("AEC", "Fiber / OSP design",                2,3,3,3,4,5,4,4,4,3,2,3,4,0),
    ("AEC", "Civil site design",                 3,3,2,3,4,4,3,4,4,2,2,3,4,0),
    ("AEC", "Energy modeling / LEED",            1,3,3,3,4,5,4,4,4,1,1,2,4,0),
    ("AEC", "Architectural rendering",           2,2,4,5,2,3,3,2,1,2,2,4,5,0),

    # ---------------------------------------------------- MANUFACTURING
    ("Manufacturing", "Mechanical drafter",      3,2,2,4,3,5,4,4,3,2,2,4,5,0),
    ("Manufacturing", "GD&T checker",            1,3,2,3,4,5,3,4,4,1,1,2,5,0),
    ("Manufacturing", "Tool designer",           1,3,2,3,4,5,2,4,4,1,1,2,5,0),
    ("Manufacturing", "CNC programming",         2,3,1,2,4,5,3,4,3,2,2,3,5,0),
    ("Manufacturing", "PLM admin",               1,3,3,3,4,4,4,4,4,1,1,2,5,0),
    ("Manufacturing", "Aviation MRO / tech pubs",1,2,3,4,3,5,4,4,3,2,1,2,2,0),
    ("Manufacturing", "QC documentation",        2,1,2,3,4,4,5,4,3,2,1,4,4,0),

    # ------------------------------------------------------- TECHNOLOGY
    ("Technology", "Software engineer",          5,5,5,5,1,4,2,2,2,4,4,3,5,1),
    ("Technology", "QA manual",                  3,2,5,5,2,5,5,3,1,4,3,5,5,1),
    ("Technology", "QA automation",              3,4,5,5,2,5,4,3,2,4,3,3,5,1),
    ("Technology", "DevOps / SRE",               3,5,5,4,3,4,2,2,3,3,3,2,5,0),
    ("Technology", "Data engineer",              3,5,5,4,3,4,3,2,3,3,3,3,5,1),
    ("Technology", "BI / analytics",             4,3,5,4,3,5,4,3,2,3,4,4,5,2),
    ("Technology", "ML engineer",                2,5,5,3,4,4,2,1,4,2,2,2,5,0),
    ("Technology", "SOC analyst",                3,4,4,4,3,4,4,1,3,3,2,3,3,0),
    ("Technology", "IT helpdesk L1/L2",          5,1,5,5,1,4,5,1,1,5,4,5,4,0),
    ("Technology", "Salesforce admin",           3,4,5,4,3,5,5,3,3,2,3,3,5,1),
    ("Technology", "NetSuite / ERP admin",       2,4,4,4,3,4,4,3,4,2,2,2,5,0),
    ("Technology", "Integration specialist",     2,4,5,3,4,4,3,2,3,2,2,3,5,1),
    ("Technology", "Database administrator",     2,4,4,4,3,4,3,3,3,2,2,3,5,0),
    ("Technology", "Technical writer",           2,2,5,4,3,4,4,3,1,2,2,4,5,0),
    ("Technology", "Marketing ops (HubSpot)",    3,3,5,3,4,5,5,4,3,2,4,4,5,3),

    # ------------------------------------------------------ SALES & GTM
    ("Sales", "SDR / BDR",                       5,2,5,5,1,2,3,0,1,5,5,5,2,2),
    ("Sales", "List building / research",        4,1,5,5,1,4,5,2,0,4,4,5,3,2),
    ("Sales", "CRM hygiene",                     3,1,5,4,2,5,5,3,1,3,3,5,4,2),
    ("Sales", "RevOps analyst",                  2,4,5,3,4,4,4,3,3,2,3,3,5,2),
    ("Sales", "Proposal / RFP writer",           2,3,4,3,4,4,4,3,2,2,2,3,4,1),
    ("Sales", "Quote desk",                      2,2,3,3,4,5,5,4,2,3,2,4,4,0),
    ("Sales", "Customer success manager",        4,3,4,3,3,2,2,2,3,3,3,4,4,1),
    ("Sales", "Renewals specialist",             2,3,4,3,4,3,3,2,3,2,2,3,4,1),
    ("Sales", "Onboarding specialist",           3,2,4,3,3,3,4,3,3,3,3,4,4,1),

    # ------------------------------------------------ MARKETING & CREATIVE
    ("Marketing", "Paid media analyst",          4,3,5,3,4,5,5,1,2,2,4,4,4,5),
    ("Marketing", "PPC analyst (search)",        3,3,5,4,3,5,5,2,2,2,4,4,4,5),
    ("Marketing", "SEO specialist",              3,2,5,5,2,3,4,2,1,2,4,5,4,3),
    ("Marketing", "Content / copywriter",        4,1,5,5,1,3,3,2,0,3,4,5,4,2),
    ("Marketing", "Email / lifecycle (Klaviyo)", 3,3,5,3,4,5,5,4,3,2,4,4,4,4),
    ("Marketing", "Social media manager",        4,1,5,4,2,2,2,2,1,2,4,5,3,2),
    ("Marketing", "Graphic designer",            4,1,5,5,1,3,3,1,1,3,4,5,4,2),
    ("Marketing", "Video editor",                4,2,5,4,2,4,3,1,2,3,5,5,4,3),
    ("Marketing", "Motion designer",             2,3,5,3,3,4,3,1,2,2,3,4,4,2),
    ("Marketing", "UI / UX designer",            3,4,5,4,3,3,2,1,3,2,3,3,5,1),
    ("Marketing", "Webflow / WordPress dev",     3,2,5,5,1,4,4,1,2,2,4,5,4,2),
    ("Marketing", "3D product render",           2,2,5,4,3,4,3,2,1,2,3,4,4,1),
    ("Marketing", "Podcast producer",            2,2,5,2,4,4,4,2,2,2,3,4,4,2),

    # ------------------------------------------- SUPPLY CHAIN & LOGISTICS
    ("SupplyChain", "Freight dispatcher",        4,2,5,5,1,3,4,0,2,4,4,5,3,0),
    ("SupplyChain", "Carrier sales",             3,2,4,4,2,2,3,0,2,4,3,4,3,0),
    ("SupplyChain", "Load planner",              2,2,4,4,3,4,4,2,2,3,2,4,3,0),
    ("SupplyChain", "Customs / trade compliance",2,3,3,3,4,5,4,4,4,2,2,3,2,0),
    ("SupplyChain", "Import-export documentation",2,1,3,4,3,5,5,4,2,3,2,4,3,0),
    ("SupplyChain", "Procurement analyst",       3,3,3,3,4,4,4,4,3,2,2,3,4,0),
    ("SupplyChain", "Demand planner",            2,3,3,3,4,4,3,4,3,2,2,3,4,0),
    ("SupplyChain", "Inventory analyst",         3,2,4,3,3,4,4,4,3,3,3,4,4,0),
    ("SupplyChain", "Order management",          3,1,4,4,2,4,5,3,2,4,3,5,4,0),
    ("SupplyChain", "3PL coordinator",           2,2,4,4,3,3,4,2,2,3,2,4,3,0),

    # ------------------------------------------------------- E-COMMERCE
    ("Ecommerce", "Amazon / marketplace ops",    3,2,5,4,3,4,5,3,3,3,4,5,4,3),
    ("Ecommerce", "Catalog management",          3,1,5,5,2,5,5,3,1,4,3,5,4,2),
    ("Ecommerce", "Amazon PPC",                  3,3,5,3,4,5,5,3,3,2,4,4,4,5),
    ("Ecommerce", "Listing optimization",        3,1,5,4,2,4,4,2,1,3,4,5,4,3),
    ("Ecommerce", "Product retouching",          3,1,5,5,2,4,4,2,0,3,3,5,4,1),
    ("Ecommerce", "Returns / disputes",          3,1,5,4,2,3,5,2,2,4,3,5,3,1),
    ("Ecommerce", "Shopify admin",               3,2,5,4,3,4,5,2,2,2,4,5,4,3),
    ("Ecommerce", "Sourcing agent",              1,2,3,3,4,3,3,3,3,2,2,2,3,0),

    # -------------------------------------------------------- HR / TALENT
    ("HR", "Recruiter",                          4,3,5,4,3,5,5,3,3,3,4,5,4,5),
    ("HR", "Sourcer",                            4,1,5,5,2,5,5,2,1,4,4,5,4,5),
    ("HR", "Recruiting coordinator",             3,1,5,4,3,4,5,3,2,3,3,5,4,4),
    ("HR", "HR generalist",                      3,2,3,2,4,3,4,4,3,2,3,4,2,2),
    ("HR", "Benefits administrator",             2,2,2,2,4,4,4,4,3,2,2,3,1,0),
    ("HR", "HRIS admin",                         2,3,4,3,4,5,5,4,4,1,2,3,4,1),
    ("HR", "Immigration / visa coordinator",     1,2,3,3,4,4,4,4,3,2,1,3,2,0),
    ("HR", "L&D coordinator",                    2,2,3,2,4,3,4,3,2,1,2,3,4,1),

    # ------------------------------------------------ REGULATED / SCIENTIFIC
    ("Regulated", "Pharmacovigilance",           2,3,4,5,1,5,5,3,5,4,1,4,1,0),
    ("Regulated", "Clinical data management",    2,3,4,5,1,5,4,3,4,4,1,4,1,0),
    ("Regulated", "CRC / CRA support",           2,3,3,4,2,4,3,3,4,3,1,3,1,0),
    ("Regulated", "Regulatory affairs",          1,4,3,4,3,4,3,4,5,2,1,2,1,0),
    ("Regulated", "Medical writing",             2,3,4,4,3,4,3,3,1,2,1,3,2,0),
    ("Regulated", "AML / KYC analyst",           4,3,4,5,1,5,5,1,3,5,2,4,2,0),
    ("Regulated", "Compliance analyst",          3,3,3,3,3,4,4,4,4,2,2,3,2,0),
    ("Regulated", "Actuarial analyst",           1,4,3,4,3,5,4,3,4,1,1,3,3,0),
    ("Regulated", "GIS analyst",                 2,2,4,4,3,5,4,4,3,2,2,3,5,0),

    # ------------------------------------------------------------- ADMIN
    ("Admin", "Executive assistant",             5,2,5,5,0,1,1,5,3,2,5,4,4,1),
    ("Admin", "General VA",                      5,1,5,5,0,2,3,3,2,3,5,5,4,1),
    ("Admin", "Chief of staff",                  1,4,4,2,4,1,1,3,4,1,2,2,4,0),
    ("Admin", "Project coordinator",             4,2,4,4,2,3,4,3,3,3,3,5,4,1),
    ("Admin", "Data entry",                      4,1,5,5,1,5,5,2,0,4,4,5,4,0),
    ("Admin", "Transcription",                   3,1,5,5,1,5,5,2,0,3,3,5,4,0),
    ("Admin", "Translation / localization",      3,2,5,5,2,4,3,3,1,2,3,4,4,0),
]

# ---------------------------------------------------------------- scoring


def score(row):
    vals = dict(zip(ORDER, row[2:]))
    total = sum(WEIGHTS[k] * vals[k] / 5 for k in ORDER)
    fails = [(k, reason) for k, thresh, reason in GATES if vals[k] <= thresh]
    return total, vals, fails


def bar(v):
    return "█" * v + "·" * (5 - v)


def ranked():
    out = []
    for row in ROLES:
        total, vals, fails = score(row)
        out.append((total, row[0], row[1], vals, fails))
    out.sort(key=lambda r: -r[0])
    return out


results = ranked()

# ---------------------------------------------------------------- output

def report():
    print("# Role Ranking — Weighted Model\n")
    print(f"**{len(ROLES)} roles scored across {len(DIMENSIONS)} weighted dimensions.**")
    print("Generated by [`scoring/model.py`](model.py). Re-run to change weights.\n")

    print("## Method\n")
    print("Weighted score (0–100), then knockout gates applied **after** scoring — because a")
    print("weighted average lets a fatal flaw be compensated by strengths elsewhere.\n")

    print("| Dim | Weight | Dimension | Anchors |")
    print("|---|---|---|---|")
    for k, w, name, anchors in DIMENSIONS:
        print(f"| `{k}` | **{w}** | {name} | {anchors} |")

    print("\n**Knockout gates** — flagged ⛔ regardless of score:\n")
    print("| Gate | Trips when | Why it's fatal |")
    print("|---|---|---|")
    for k, thresh, reason in GATES:
        print(f"| `{k}` | ≤ {thresh} | {reason} |")

    print("\n---\n")
    print("## Full ranking\n")
    print("| # | Role | Cluster | Score | " + " | ".join(f"`{k}`" for k in ORDER) + " | Gate |")
    print("|---|---|---|---|" + "---|" * len(ORDER) + "---|")
    for i, (total, cluster, name, vals, fails) in enumerate(results, 1):
        gate = "⛔ " + "; ".join(k for k, _ in fails) if fails else ""
        cells = " | ".join(str(vals[k]) for k in ORDER)
        print(f"| {i} | {'**' + name + '**' if not fails and i <= 25 else name} "
              f"| {cluster} | **{total:.1f}** | {cells} | {gate} |")

    clean = [r for r in results if not r[4]]
    print("\n---\n")
    print("## Top 25 after knockouts\n")
    print("| # | Role | Cluster | Score | Volume | Fee | Retention | Gradeable | AI |")
    print("|---|---|---|---|---|---|---|---|---|")
    for i, (total, cluster, name, vals, _) in enumerate(clean[:25], 1):
        print(f"| {i} | **{name}** | {cluster} | **{total:.1f}** | {bar(vals['V'])} "
              f"| {bar(vals['D'])} | {bar(vals['R'])} | {bar(vals['G'])} | {bar(vals['AI'])} |")

    print("\n---\n")
    print("## Knocked out\n")
    print("| Role | Score | Gate tripped |")
    print("|---|---|---|")
    for total, cluster, name, vals, fails in results:
        if fails:
            print(f"| {name} | {total:.1f} | " + "; ".join(f"**{k}** — {r}" for k, r in fails) + " |")

    print("\n---\n")
    print("## Cluster averages (clean roles only)\n")
    clusters = {}
    for total, cluster, name, vals, fails in clean:
        clusters.setdefault(cluster, []).append(total)
    print("| Cluster | Clean roles | Mean | Best |")
    print("|---|---|---|---|")
    for c, scores in sorted(clusters.items(), key=lambda x: -sum(x[1]) / len(x[1])):
        best = max((t, n) for t, cl, n, _, _ in clean if cl == c)
        print(f"| {c} | {len(scores)} | **{sum(scores)/len(scores):.1f}** | {best[1]} ({best[0]:.1f}) |")

    print(f"\n---\n\n*{len(ROLES)} roles · {len(clean)} clean · {len(ROLES)-len(clean)} knocked out*")


if __name__ == "__main__":
    report()
