# 6-Week Plan: Build Real Applications on Azure (Python, from zero)

**Goal:** job-ready skills. By the end you can build, deploy, automate, and *explain* three kinds of Azure applications — a web app, a data engineering pipeline, and a DevOps setup — joined into one portfolio project.
**Starting point:** zero programming experience; 15 years of OFSAA, SQL/PL-SQL and data modeling.
**Pace:** ~8 hrs/day, 6 build days + 1 lighter review day per week. Start: October 2026 → finish mid-November 2026, then retake AZ-900.
**Language:** Python throughout (web apps, data tooling, Databricks/PySpark, automation).

---

## How each day works

| Block | Time | What you do |
|---|---|---|
| Learn | ~2.5 hrs | One concept, explained, with small examples you type yourself |
| Build | ~4.5 hrs | Write the day's code or deploy the day's Azure piece. You write it; Claude reviews |
| Consolidate | ~1 hr | Notes in your own words, commit and push, **delete or stop Azure resources**, 3–5 flashcards |

**Rules that make this job-ready rather than tutorial-ready:**
- **Type every line yourself.** No copy-paste. If you can't explain a line, you don't own it yet.
- **Stuck? Ask for a hint, not the answer.** Read the traceback first; we'll practise reading them on purpose.
- **Commit daily** with a clear message. Your GitHub history is part of your portfolio.
- **End every week with interview talking points**: what you built, why you chose it, what went wrong, what you'd change.

---

## Cost guardrails (do these on Day 1, keep them all six weeks)

- **Check your subscription status first.** The $200 free credit lasts 30 days, so yours has expired. Your 12-month free services still apply. Confirm in the portal whether the subscription is active or needs upgrading to pay-as-you-go.
- **Create a budget with email alerts** (Cost Management → Budgets) at 50%, 80% and 100% of a monthly amount you choose.
- **One resource group per week** (`rg-wk3-webapp`, `rg-wk4-data`, …) so teardown is a single delete.
- **Tag everything:** `project`, `week`, `owner`.
- **Databricks is the main cost risk.** Single-node clusters only, auto-terminate after 15–20 minutes, and delete the workspace at the end of Week 4.
- **Before creating anything new, check the Pricing Calculator.** Before logging off, check what's still running.

---

## Repo layout

```
week1-azure/              AZ-900 notes (keep for the retake)
wk1-python/               Week 1 scripts and mini-project
wk2-data/                 Week 2 pandas/SQL work
wk3-webapp/               Flask app
wk4-data-engineering/     Pipeline notebooks, ADF definitions, data generator
wk5-devops/               Pipelines, Bicep, Dockerfile
capstone/                 Week 6 end-to-end project
```

---

## WEEK 1 — Python from zero

**Outcome:** you can write, run, debug and test small Python programs that work with transaction data.

- **Day 1 — Setup + first programs.** Install Python 3.12 (replace 3.8, which is end-of-life), VS Code with the Python extension, Azure CLI; `az login`. Virtual environments (`venv`). Git workflow: `status`, `add`, `commit`, `push`. Cost guardrails above. *Learn:* variables, types, arithmetic, `print`, f-strings. *Build:* a compound-interest calculator.
- **Day 2 — Decisions and loops.** `if/elif/else`, comparisons, `for`, `while`, `range`, `break/continue`. *Build:* classify a list of transaction amounts as small/medium/large; print a monthly loan amortization schedule.
- **Day 3 — Data structures.** Lists, dictionaries, tuples, sets, comprehensions; when to use each. *Build:* a chart of accounts as a dict; filter and total transactions by account type.
- **Day 4 — Functions and modules.** Parameters, return values, defaults, scope, docstrings, `import`. *Build:* refactor Days 1–3 into a `ledger.py` module. *Skill:* read three deliberately broken programs' tracebacks and fix them.
- **Day 5 — Files and errors.** `pathlib`, `csv`, `with`, `try/except`, raising your own errors. *Build:* read `transactions.csv`, total per category, write a summary CSV, handle bad rows without crashing.
- **Day 6 — Classes and tests.** A first look at classes; `pytest`. *Build:* an `Account` class (deposit, withdraw, raise on overdraft) with tests that prove it.
- **Day 7 — Mini-project + review.** Command-line transaction tracker (`argparse`, CSV storage, tests, README).

**Interview talking points:** reading and fixing tracebacks; why tests matter; structuring code into modules.

---

## WEEK 2 — Python for data + first contact with Azure

**Outcome:** you can clean, join and analyse data in Python, and push results to Azure from code using identity, not passwords.

- **Day 8 — pandas basics.** DataFrame, Series, `read_csv`, `head/info/describe`, selecting rows and columns. *Build:* a generator script that creates a realistic synthetic transactions dataset; explore it.
- **Day 9 — Cleaning.** Missing values, data types, dates, derived columns, `apply`. *Build:* turn a deliberately messy file into a tidy table.
- **Day 10 — Aggregation and joins (SQL thinking).** `groupby`, pivot tables, `merge` to an account dimension. *Build:* reproduce a SQL-style report — spend by account by month — and check it against the same query in SQL.
- **Day 11 — SQL from Python.** `sqlite3`, parameterised queries (and why string-built SQL is a security hole), `to_sql`/`read_sql`. *Build:* model accounts, transactions and categories as three related tables; load and query.
- **Day 12 — Professional basics.** `requirements.txt`, environment variables, `.env` files kept out of Git, `logging`, calling a JSON API with `requests`.
- **Day 13 — First Azure from code.** Create a storage account with the CLI. Use `azure-identity` (`DefaultAzureCredential`) and `azure-storage-blob` to upload and download. Grant yourself the **Storage Blob Data Contributor** role (RBAC, hands-on). Why identity beats access keys.
- **Day 14 — Mini-project + review.** Pipeline script: raw CSV → clean → SQLite → upload outputs to Blob. Delete the resource group.

**Interview talking points:** pandas vs SQL for the same problem; why you used RBAC and identity instead of storage keys.

---

## WEEK 3 — Web application on Azure

**Outcome:** a live Flask web app on App Service, backed by Azure SQL, with secrets in Key Vault, sign-in through Microsoft Entra ID, and monitoring.

- **Day 15 — How the web works + Flask.** HTTP, requests and responses, HTML, routes, Jinja templates. *Build:* Flask app running locally.
- **Day 16 — A data-driven app.** List transactions from SQLite, a form to add one, input validation. *Build:* working CRUD screens locally.
- **Day 17 — Deploy to App Service.** `az webapp up`, App Service plans (Free vs Basic), app settings, log stream, Gunicorn. This is **PaaS**, hands-on: notice what you no longer manage.
- **Day 18 — Azure SQL Database.** Serverless/free tier, firewall rules, connecting from Python, migrating your schema. Compare with "SQL Server on a VM" (IaaS) — who patches what.
- **Day 19 — Secrets and identity.** Key Vault, a **managed identity** for the web app, RBAC on the vault. Remove every secret from code and config.
- **Day 20 — Sign-in and monitoring.** App Service authentication with **Microsoft Entra ID**; Application Insights for requests and errors; scale up vs scale out on the plan.
- **Day 21 — Governance + review.** Tags, a **resource lock**, an **Azure Policy** (allowed locations) on the resource group. README with an architecture diagram. Stop or delete resources.

**Interview talking points:** PaaS vs IaaS for this app and why; how secrets are handled; how users authenticate.
**AZ-900 payoff:** service types, identity, Key Vault, RBAC, Policy, locks — your three weakest exam areas, all hands-on.

---

## WEEK 4 — Data engineering (the deepest week)

**Outcome:** an end-to-end financial data pipeline on Azure: ingest → lake → transform (bronze/silver/gold) → serve → report, with data quality checks.

- **Day 22 — Concepts + the lake.** Data lake vs warehouse, batch vs streaming, ELT, the medallion (bronze/silver/gold) pattern. Create **ADLS Gen2**. Generate a larger dataset (millions of transactions) and load it with **AzCopy** and **Storage Explorer**.
- **Day 23 — Azure Data Factory.** Linked services, datasets, copy activity into bronze, triggers, monitoring runs.
- **Day 24 — Databricks + PySpark.** Workspace, a single-node cluster with auto-terminate, notebooks. PySpark DataFrames mapped to what you know from pandas and SQL.
- **Day 25 — Bronze → silver.** Clean, deduplicate, enforce types; write **Delta** tables; Spark SQL.
- **Day 26 — Silver → gold.** Aggregates: daily balances, spend by category, and simple risk flags such as unusually large or rapid transactions (your AML background is an edge here). Window functions.
- **Day 27 — Orchestrate and serve.** Data Factory triggers the Databricks notebooks; load gold into Azure SQL; build a report in **Power BI Desktop** (free). Overview of **Microsoft Fabric** and where the market is heading.
- **Day 28 — Data quality + review.** Row-count and null checks; reconcile totals between layers (the same idea as GL reconciliation); lineage notes; README. **Delete the Databricks workspace.**

**Interview talking points:** why medallion layers; how you validated data between layers; cost control on Databricks; mapping OFSAA staging/processing/results to bronze/silver/gold.

---

## WEEK 5 — DevOps

**Outcome:** your earlier projects build, test and deploy automatically; infrastructure is defined as code; the web app runs in a container.

- **Day 29 — DevOps foundations.** CI vs CD, feature branches and pull requests, an **Azure DevOps** organisation and project, Boards for tracking work, connecting your GitHub repo.
- **Day 30 — Continuous integration.** `azure-pipelines.yml`: install dependencies, lint (ruff), run `pytest` on every push.
- **Day 31 — Continuous delivery.** Deploy the Flask app from the pipeline using a service connection; dev and prod environments with an approval step.
- **Day 32 — Infrastructure as code with Bicep.** Define the App Service plan, web app, storage and Key Vault in Bicep; `what-if`; parameter files for dev and prod. How this compares with ARM templates and Terraform.
- **Day 33 — Containers.** Dockerfile for the Flask app, run locally, push to **Azure Container Registry**, deploy to **Azure Container Apps**. Where ACI, AKS and Container Apps each fit.
- **Day 34 — Full pipeline + monitoring.** The pipeline builds the container and deploys the Bicep; Azure Monitor alert rules and an availability test.
- **Day 35 — Review.** README for the DevOps setup; tear everything down, then rebuild it from code to prove it works.

**Interview talking points:** walk through the pipeline end to end; why infrastructure as code; how a bad commit gets caught before production.
**AZ-900 payoff:** ARM/Bicep, Monitor, containers, management tools.

---

## WEEK 6 — Capstone + job readiness

**Outcome:** one portfolio project you can demo and talk through in an interview, plus a re-baseline for AZ-900.

**Capstone — mini financial data platform:** Data Factory ingests transactions → lake (bronze/silver/gold in Databricks) → gold in Azure SQL → Flask dashboard/API on App Service or Container Apps → deployed by Azure DevOps from Bicep → secrets in Key Vault, sign-in with Entra ID, monitoring and alerts.

- **Day 36 — Design.** Architecture diagram and a one-page design doc: components, data flow, security, cost.
- **Days 37–39 — Build and integrate.** Reuse Weeks 3–5; get one clean end-to-end run.
- **Day 40 — Harden.** Tests, error handling, data quality checks, a cost review in Cost Management, tags/locks/policy.
- **Day 41 — Portfolio.** README, diagram, screenshots, a short demo recording. Resume bullets for **only what you actually built**. One STAR-format interview story per week.
- **Day 42 — Retrospective + AZ-900 re-baseline.** Take the official Microsoft practice assessment; map each exam domain to what you built; schedule the retake. Tear down all resources.

---

## Tracking

- [ ] Week 1 — Python from zero
- [ ] Week 2 — Python for data + first Azure
- [ ] Week 3 — Web app on Azure
- [ ] Week 4 — Data engineering
- [ ] Week 5 — DevOps
- [ ] Week 6 — Capstone + job readiness
- [ ] AZ-900 retake (first attempt: 606/700 on 2026-09-30)
