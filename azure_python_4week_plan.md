# 4-Week Hands-On Learning Work Stream
### Azure Cloud Fundamentals (AZ-900) → Python for Data
**Built for:** an OFSAA consultant with data-modeling experience
**Commitment:** ~6 hrs/day · learn-by-doing · Azure first, then Python

---

## The strategy (read this first)

You already think in schemas, relationships, financial data, and transformations. That is a huge head start. This plan deliberately uses that strength: the Azure week leans on the data/governance services you'll recognize, and the Python weeks point straight at **data work** (pandas, files, databases) rather than generic app coding. By Week 4 you tie both together in a small data pipeline that lives in a GitHub repo — a real portfolio piece.

> ### ⚠️ Fixing the scenario-question gap (your priority)
> You passed the recall but lost on *application* — "which service fits this situation?" questions. That's a **transfer gap**, not a knowledge gap, and it's the #1 reason people fail AZ-900. Studying harder in recall mode won't fix it; you need a different mode. Three habits do the job, and they're built into Week 1 below:
> 1. **Signal-word mapping** — scenarios hide the answer in trigger phrases ("don't want to manage the OS" → PaaS). Learn to spot them. See **Appendix A**.
> 2. **Decision-boundary thinking** — for every confusable pair, be able to finish "I'd pick A over B *when ___*." See **Appendix B**.
> 3. **Hands-on as the anchor** — once you've *deployed* a VM vs an App Service, the scenario stops being abstract. This is why learn-by-doing is exactly right for your weakness.
> Use the **4-step answering protocol** in **Appendix C** on every practice question until it's automatic.

**Sequencing**
- **Week 1** — Azure Fundamentals + AZ-900 exam (concept-heavy, but you'll *use* the portal daily)
- **Week 2** — Python core (syntax → functions → data structures), hands-on from day one
- **Week 3** — Python for data (pandas, files, SQL, basic viz)
- **Week 4** — Integration capstone (Python + Azure + your data background) + buffer

**Daily rhythm (your 6 hours)** — never 6 straight hours of video; retention collapses. Use this loop every day:

| Block | Time | What you do |
|---|---|---|
| 1. Learn | ~2 hrs | New concept via official path / a focused video |
| 2. Build | ~3 hrs | Hands-on: deploy in the portal, or write & run code |
| 3. Consolidate | ~1 hr | Notes in your own words, flashcards, a short quiz, commit your code |

> Take a real lunch break and a couple of 10-min breaks. One lighter "review only" day per week is built in and healthy — don't skip it.

---

## Day 0 — Setup (do before Week 1, ~1–2 hrs)

Knock these out so nothing blocks you later:

- [ ] **Create an Azure free account** (free tier + ~$200 credit for 30 days). Use a personal email, not a client tenant.
- [ ] **Register for Microsoft Azure Virtual Training Day: Fundamentals** — completing both parts can earn a **free AZ-900 exam voucher** (check current availability when you register; promos change).
- [ ] **Download the current AZ-900 "Skills measured" outline** from Microsoft Learn — study *only* what's listed.
- [ ] **Install your Python toolkit** (you'll need it Week 2, set it up now): [Python 3.x](https://www.python.org), [VS Code](https://code.visualstudio.com) + the Python extension. Optionally [Anaconda/Miniconda] for environments. Confirm `python --version` works in a terminal.
- [ ] **Create a free GitHub account** + install Git. Make one repo: `azure-python-upskilling`. Everything you build goes here.
- [ ] **Bookmark a flashcard tool** (Anki, or paper). You'll make cards daily.

---

## WEEK 1 — Azure Fundamentals (AZ-900)

**Goal:** Pass AZ-900 by mastering *application*, not just recall — be able to read a business scenario and pick the right service. You'll deploy services hands-on so the scenarios feel concrete.
**Exam map:** Cloud Concepts 25–30% · Architecture & Services 35–40% · Management & Governance 30–35%.

> **Run this loop every Week 1 day:** after you learn a service, (1) deploy or click through it in the portal, then (2) write **one scenario question of your own** for it ("A company needs ___, which service?") and add the trigger word to your signal-word map (Appendix A). By Day 6 you'll have ~25 self-authored scenarios — the exact skill the exam tests.

### Day 1 — Cloud concepts
- **Learn:** What cloud is; IaaS / PaaS / SaaS; public/private/hybrid; CapEx vs OpEx; the **shared responsibility model**; benefits (scalability, elasticity, reliability, predictability — note Microsoft's exact wording).
- **Build:** Log into the Azure portal. Create your first **Resource Group**. Just explore — find the cost/billing blade, the search bar, the Cloud Shell.
- **Consolidate:** Flashcards for every "vs" pairing (these are exam gold).

### Day 2 — Architecture & core structure
- **Learn:** Regions, region pairs, **Availability Zones**, datacenters; **subscriptions, management groups, resource groups, resources** (the hierarchy — this maps neatly to data hierarchies you know).
- **Build:** Deploy a small **Virtual Machine** (B-series, cheapest). Connect to it. Then **delete it** to protect your credit. Deploy a **Storage Account** and upload a file to Blob storage.
- **Consolidate:** Draw the resource hierarchy from memory.

### Day 3 — Compute & networking
- **Learn:** VMs vs Scale Sets vs availability sets; App Service / web apps; **containers** (ACI, AKS at a glance); virtual networks, subnets, peering, VPN Gateway, ExpressRoute.
- **Build:** Create a **Virtual Network** with two subnets. Spin up an **App Service** and deploy the default sample app. Delete what you don't need.
- **Consolidate:** "Which service fits this scenario?" — write 5 of your own scenario Q&As.

### Day 4 — Storage, databases & identity
- **Learn:** Storage tiers (hot/cool/archive), redundancy (LRS/ZRS/GRS); **Azure SQL, Cosmos DB** at a glance; **Microsoft Entra ID** (formerly Azure AD), SSO, MFA, passwordless; RBAC.
- **Build (your wheelhouse):** Deploy an **Azure SQL Database** (serverless/cheapest). Connect with the query editor, create a table, insert rows, run a SELECT. This is where your data modeling clicks in.
- **Consolidate:** Map Azure storage/db options to things you already know in OFSAA/RDBMS terms.

### Day 5 — Management & governance
- **Learn:** Cost Management + pricing/TCO calculators; **Azure Policy**, resource locks, tags, **Azure Advisor**; **Azure Monitor** (Log Analytics, alerts, App Insights); **Service Health vs Azure Status** (classic exam trap); SLAs and composite SLA math; IaC concepts (ARM templates, **Bicep**, Terraform mention).
- **Build:** Apply a **tag** and a **resource lock** to your resource group. Open the **Pricing Calculator** and price a small architecture. Set a **budget alert**.
- **Consolidate:** Practice one composite-SLA calculation by hand.

### Day 6 — Practice exams as a *diagnostic* (this is where you fix the gap)
Don't just score yourself — mine your mistakes. Take the **free Microsoft official practice assessment**, then 1–2 third-party timed tests. For **every scenario question** (right or wrong), run this post-mortem:
- **What was the real requirement?** Restate the scenario in one plain sentence.
- **What signal word pointed to the answer?** Add it to your Appendix A map if it's new.
- **Which two services did I confuse?** Write the decision rule that separates them into Appendix B.
- **Why were the wrong answers wrong?** Each distractor teaches a boundary.

Wrong answers are not failures here — each one permanently upgrades your tables. Re-take until you're consistently 85%+ **and** can explain *why* every option is right or wrong, not just which one.

### Day 7 — Exam day (or review buffer)
- Sit AZ-900 (online proctored or test center), ideally before **July 20, 2026**. If not ready, this is a review day and you book early next week.
- **Milestone:** ✅ Azure Fundamentals done. Push your notes to GitHub.

**Week 1 resources**
- Microsoft Learn — official **AZ-900 learning path** (free, ~10–15 hrs) and the **Skills measured** outline
- **John Savill's AZ-900 Study Cram** (YouTube) — excellent free overview
- freeCodeCamp / Tim Warner AZ-900 full course (YouTube)
- Microsoft Learn **free practice assessment**

---

## WEEK 2 — Python Core (learn by writing, not watching)

**Goal:** Be able to read, write, and debug everyday Python confidently.
**Tool:** VS Code. Type every example yourself — no copy-paste.

### Day 1 — Setup & basics
- Variables, data types (int, float, str, bool), operators, `print`, `input`, comments, f-strings.
- **Build:** A tip/loan-interest calculator that takes input and prints a formatted result.

### Day 2 — Control flow
- `if/elif/else`, comparison & logical operators, `while` and `for` loops, `range`, `break/continue`.
- **Build:** A number-guessing game; a script that classifies a list of transaction amounts as small/medium/large.

### Day 3 — Data structures
- **Lists, dictionaries, tuples, sets** — when to use each. Indexing, slicing, comprehensions.
- **Build:** Model a small "chart of accounts" as a dict; write list comprehensions to filter/transform records. (This *is* data modeling in Python.)

### Day 4 — Functions & modules
- Defining functions, parameters/returns, default & keyword args, scope; `import`; the standard library (`math`, `datetime`, `random`).
- **Build:** Refactor Days 1–3 scripts into clean, reusable functions in a module.

### Day 5 — Files & errors
- Reading/writing text and **CSV** files; `with` blocks; `try/except`; `csv` module.
- **Build:** Read a CSV of transactions, compute totals per category, write a summary CSV. (Bridge to Week 3.)

### Day 6 — Practice & problem-solving
- Grind exercises on **Exercism** (Python track) or easy **HackerRank/Codewars** problems. Aim for ~10 small problems.
- Pick the 3 that taught you the most; commit your solutions with comments.

### Day 7 — Review + mini-project
- **Mini-project:** A command-line **expense tracker** — add/list/summarize expenses, persist to a CSV. Uses everything from the week.
- **Milestone:** ✅ Comfortable with core Python. Push to GitHub with a short README.

**Week 2 resources**
- **"Automate the Boring Stuff with Python"** (free online) — the most practical, hands-on intro
- Official **Python Tutorial** (docs.python.org) for reference
- **Real Python** tutorials · **Exercism** Python track for graded practice

---

## WEEK 3 — Python for Data (your sweet spot)

**Goal:** Manipulate and analyze real datasets — the skill that compounds with your OFSAA background.
**Tool:** Jupyter notebooks (in VS Code) or Google Colab.

### Day 1 — NumPy + pandas intro
- NumPy arrays (briefly); **pandas Series & DataFrame**; reading CSV/Excel; `.head()`, `.info()`, `.describe()`, selecting rows/columns.
- **Build:** Load a public dataset (e.g., a transactions or financial CSV from Kaggle) and explore it.

### Day 2 — Cleaning & transforming
- Handling missing values, dtypes, renaming, filtering (boolean masks), creating derived columns, `apply`.
- **Build:** Clean a deliberately messy CSV into a tidy table.

### Day 3 — Aggregation & joins (think SQL)
- `groupby`, aggregations, pivot tables, **merge/join** (maps directly to your dimensional-modeling instincts), sorting.
- **Build:** Reproduce a SQL-style report — group transactions by account + period, join to a lookup/dimension table.

### Day 4 — Python ↔ databases
- `sqlite3`; running SQL from Python; loading a DataFrame to a table and back (`to_sql` / `read_sql`); intro to SQLAlchemy.
- **Build:** Create a SQLite DB, model 2–3 related tables, load your cleaned data, query it from Python.

### Day 5 — Visualization & summary
- `matplotlib` / pandas plotting basics; bar/line/histogram; exporting charts and an Excel/CSV summary.
- **Build:** A one-notebook "analysis report" with 3–4 charts and written insights.

### Day 6 — Kaggle hands-on
- Complete Kaggle's free **Python** and **Pandas** micro-courses (in-browser, all exercises). They're fast and very hands-on.

### Day 7 — Review + consolidation
- Redo Day 3's report from a blank notebook, no reference. Note what you had to look up → flashcards.
- **Milestone:** ✅ You can ingest → clean → join → analyze → store data in Python.

**Week 3 resources**
- **Kaggle Learn** — free Python + Pandas micro-courses (highly recommended for you)
- pandas docs — **"10 minutes to pandas"**
- Real Python pandas tutorials · public datasets on **Kaggle** / data.gov

---

## WEEK 4 — Integration Capstone + Buffer

**Goal:** Ship one project that combines Python data work with Azure, plus absorb slack from earlier weeks.

### Capstone — "Mini financial data pipeline"
Build it incrementally over the week and commit daily:

1. **Ingest** — Python script reads a raw transactions CSV.
2. **Transform** — pandas cleans, derives columns, aggregates (your Week 3 skills).
3. **Store** — write results to **SQLite** *and* upload the output file to **Azure Blob Storage** using the `azure-storage-blob` SDK (ties back to Week 1).
4. **(Stretch)** Load the cleaned data into the **Azure SQL Database** you built in Week 1 and query it from Python.
5. **(Stretch)** Wrap the transform in an **Azure Function** (timer or HTTP trigger) so it runs in the cloud.
6. **Document** — a clear README: problem, architecture diagram, how to run it, screenshots.

### Suggested day split
- **Days 1–2:** Steps 1–3 working end-to-end locally + to Blob.
- **Day 3:** Stretch goals (Azure SQL / Functions).
- **Day 4:** Polish, error handling, README, architecture diagram.
- **Day 5:** Buffer — finish AZ-900 if you deferred it, or revisit your weakest topic.
- **Days 6–7:** Review everything, clean up the GitHub repo, write a short "what I learned" post (great for LinkedIn).

- **Milestone:** ✅ A portfolio repo demonstrating Azure + Python + data engineering.

**Week 4 resources**
- Azure SDK for Python docs (`azure-storage-blob`)
- Microsoft Learn — "Create serverless logic with Azure Functions" path
- Azure free account portal for all hands-on

---

## How to know you're on track

| End of week | You can… |
|---|---|
| 1 | Read a business scenario and pick the right service *with reasoning*; AZ-900 passed or scheduled |
| 2 | Write, run, and debug everyday Python from scratch |
| 3 | Load, clean, join, analyze, and store real datasets in pandas |
| 4 | Ship a documented Python+Azure data project on GitHub |

**Stay-honest habits:** code every day (no passive watching), explain each concept aloud in your own words, and commit something daily so progress is visible.

---

## What's next (after these 4 weeks)

Given your data background, the natural follow-ups — not part of this plan, just direction:
- **DP-900 (Azure Data Fundamentals)** — bridges Azure + data; highly aligned with OFSAA work and an easy next cert.
- **Azure Data Factory / Synapse / Databricks** — cloud data pipelines at enterprise scale.
- **Pandas → PySpark** — same mental model, big-data scale.
- **AZ-104** only if you want the administrator/ops track.

---

# Appendix A — Signal-Word → Service Map

Scenario questions hide the answer in plain-English cues. Train yourself to spot the cue, and the service is obvious. Keep adding rows as practice tests reveal new ones.

| When the scenario says… | It's signalling… | Answer |
|---|---|---|
| "pay only for what we use", "no upfront cost", "month-to-month" | consumption / OpEx | **Pay-as-you-go (consumption) pricing** |
| "don't want to manage the OS / patching / hardware" | PaaS | **App Service** (PaaS) |
| "need full control of the OS", "install custom software", "lift-and-shift a legacy app" | IaaS | **Virtual Machine** |
| "ready-to-use software", "vendor manages everything" (e.g. email) | SaaS | **SaaS (e.g. Microsoft 365)** |
| "run code on an event / schedule", "don't manage any servers", "pay per execution" | serverless | **Azure Functions** |
| "package an app with its dependencies", "portable", "microservices" | containers | **Container Instances** (small) / **AKS** (orchestration at scale) |
| "globally distributed", "low latency worldwide", "NoSQL / multi-model" | global NoSQL | **Cosmos DB** |
| "managed relational SQL database" | managed RDBMS | **Azure SQL Database** |
| "store files / images / backups / unstructured objects" | object storage | **Blob Storage** |
| "personalized alerts about outages affecting **my** resources" | personalized health | **Azure Service Health** |
| "overall status of all Azure services (public)" | global health | **Azure Status** |
| "recommendations on cost, security, reliability, performance" | guidance | **Azure Advisor** |
| "collect metrics & logs", "set alerts", "app performance telemetry" | observability | **Azure Monitor** (Log Analytics, App Insights) |
| "enforce a rule — all resources must have a tag / only certain regions / approved VM sizes" | governance rule | **Azure Policy** |
| "control who can do what on which resources" | permissions | **RBAC** |
| "prevent accidental delete or change of a resource" | protection | **Resource lock** |
| "organize and govern **many subscriptions** at scale" | hierarchy | **Management groups** |
| "estimate the cost of a planned architecture" | forecasting | **Pricing Calculator** |
| "compare cost of on-prem vs Azure" | migration case | **TCO Calculator** |
| "track and analyze **actual** spend, set budgets" | spend control | **Microsoft Cost Management** |
| "single sign-on, MFA, manage user identities" | identity | **Microsoft Entra ID** |
| "connect on-prem network to Azure over the internet (encrypted)" | hybrid network | **VPN Gateway** |
| "private, dedicated, high-bandwidth link to Azure (not over internet)" | hybrid network | **ExpressRoute** |
| "manage Azure resources as code / repeatable deployments" | IaC | **ARM templates / Bicep** |
| "improve security posture / threat protection across resources" | security | **Microsoft Defender for Cloud** |
| "discover, classify, and govern data across the estate" | data governance | **Microsoft Purview** |

---

# Appendix B — Decision-Boundary Tables (the confusable pairs)

The exam tests the *boundary* between similar services. For each, learn the one-line rule that separates them.

**Hosting / compute**
| Pick this | …over this | …when |
|---|---|---|
| Virtual Machine | App Service | you need full OS control or are lifting-and-shifting a legacy app |
| App Service | Virtual Machine | you just want to run a web app and not manage the OS |
| Azure Functions | App Service | the work is short, event-driven, and you want to pay per execution |
| Container Instances | AKS | you have a few containers and don't need orchestration |
| AKS | Container Instances | you need to orchestrate many containers at scale |

**Resilience (each protects a different blast radius)**
| Concept | Protects against |
|---|---|
| Availability **Set** | hardware/rack failure **within one datacenter** (VMs) |
| Availability **Zone** | a **whole datacenter** failing within a region |
| **Region pair** | a **whole region** failing (disaster recovery) |

**Storage redundancy**
| Option | Copies kept |
|---|---|
| **LRS** | 3 copies in **one** datacenter |
| **ZRS** | across **zones** in one region |
| **GRS** | replicated to a **second region** |

**Governance & identity (a classic trap trio)**
| Service | Answers the question |
|---|---|
| **Azure Policy** | "What is *allowed to exist / how must it be configured*?" (e.g. enforce tags, restrict regions) |
| **RBAC** | "*Who* can do *what* to which resources?" |
| **Resource lock** | "Stop this specific resource being deleted or changed." |

**Health & guidance (another trap group)**
| Service | Use it for |
|---|---|
| **Azure Status** | global, public health of all Azure services |
| **Service Health** | outages affecting **your** specific resources |
| **Azure Monitor** | your metrics, logs, and alerts |
| **Azure Advisor** | recommendations to improve cost/security/reliability/performance |

**Cost tools**
| Tool | Use it for |
|---|---|
| **Pricing Calculator** | estimate cost of a *planned* deployment |
| **TCO Calculator** | compare *on-prem vs Azure* |
| **Cost Management** | monitor *actual* spend + set budgets/alerts |

---

# Appendix C — The 4-Step Scenario Answering Protocol

Run this on every scenario question until it's automatic. It turns guessing into reasoning.

1. **Strip it to the core requirement.** Ignore the fluff; say in one sentence what the company actually needs.
2. **Underline the signal words.** Cost? Control? Management overhead? Global reach? Compliance/governance? Identity? Match them against Appendix A.
3. **Eliminate on hard constraints.** Cross out any option that violates a stated requirement (e.g. "no servers to manage" kills the VM answer). Usually removes 2 of 4.
4. **Pick the best fit for the *dominant* requirement.** Among survivors, choose the one built for the main need. If two remain, the more *managed / purpose-built* option is usually the intended answer at Fundamentals level.

> **Practice drill (do this Days 3–6):** take any practice question, cover the options, and answer from Appendix A first. Only then look at the choices. If your pre-answer matches one option, you've truly learned to apply — not recognize.

---
*Plan dated June 2026. Always download the current AZ-900 "Skills measured" outline before studying, since Microsoft updates it periodically.*
