# IBM Maximo Manage — Hands-On Lab Guide

**Goal:** learn IBM Maximo Manage hands-on, from zero to confident (technical focus). No exam for now.
**Environment:** IBM Maximo Application Suite 14-day free trial (Manage, Health, Visual Inspection)

> **How to use this guide:** each lab gives you *tasks* and *questions*, not answers.
> Do the task, then write your answer to every "❓" in your **lab log** (template at the bottom)
> *before* asking Claude. We review your log together. Explaining *why* matters more than clicking.

---

## 0. Setup (do this once)

1. **Sign up yourself** at <https://www.ibm.com/products/maximo/resources/trial> (you need an IBMid).
   - The 14 days start at signup, so finish Session 1–2 theory first.
   - Do **not** enter payment details. If the form asks for them, stop and check with Claude.
2. Log in, open **Manage**, and find:
   - the **navigation menu** (the list of applications: Work Order Tracking, Assets, Locations…)
   - the **List tab** (search results) vs. the **record tabs** (one record's detail)
   - **Start Center**: your home page with portlets (saved queries, KPIs)
3. **Note the demo data.** Find which **sites** exist (look at any work order's Site field).
   IBM demo data often uses site `BEDFORD`, but your trial may differ. Use whatever is there.
4. **Permissions caveat:** a trial user may not have access to admin apps (Database Configuration,
   Application Designer, Escalations, Automation Scripts). If an app is missing, write that in your log.
   That's fine; Lab 8 is read-only and optional.

❓ 0.1 In one sentence: what is the difference between the List tab and a record tab?
❓ 0.2 Which sites and organizations does your trial have?

---

## Lab 1 — Assets & Locations (the "dimensions")

**Concept:** a **Location** is a *place/function* (Pump Bay 3). An **Asset** is the *physical thing*
(pump serial #12345) installed at a location. Assets can move; locations stay put.

Tasks:
1. Open **Locations**. Pick one location and find its **parent** and its **children** (the hierarchy / system view).
2. Open **Assets**. Pick an asset that has a location. Note: Asset #, Site, Location, Status, Parent asset.
3. On that asset, find its **work order history** and any **spare parts** list.
4. In the Assets List tab, filter to one site and one status (e.g., OPERATING).

❓ 1.1 Draw the hierarchy you found as a tree (3 levels is enough).
❓ 1.2 If a pump is moved from Location A to Location B, which record changes: the asset or the location? Why does Maximo model them separately?
❓ 1.3 Finance analogy: which is more like an *account* and which is more like a *branch/cost centre*? Defend your choice.

---

## Lab 2 — Work Order lifecycle & status rules (⭐ core topic)

**Concept:** statuses are the heart of Maximo work management. The typical out-of-the-box flow:
`WAPPR → APPR → INPRG → COMP → CLOSE`, plus `WMATL`, `WSCH`, `CAN`, and others.

Tasks:
1. Open **Work Order Tracking** → **New Work Order**. Fill: description, site, asset (from Lab 1). Save. Note the **WONUM** and **status**.
2. Try **Change Status** and look at *which statuses are offered* from WAPPR.
3. Move it step by step: WAPPR → APPR → INPRG → COMP → CLOSE. At **each** status, try to:
   - edit the description
   - add a planned material
   - report actual labor
   Record what is **allowed** vs **blocked** (and the exact error message if blocked).
4. Open **View Status History** (in the action menu) and look at the trail.
5. Create a 2nd work order and **cancel** it (CAN). Then try to cancel a work order that already has actuals reported. What happens?
6. Try to reopen a CLOSED work order.

❓ 2.1 Fill in a table: Status | Can edit? | Can add plans? | Can report actuals? | Can go back?
❓ 2.2 Why would a business *want* CLOSE to make the record read-only? (Think: what happens to a posted journal entry in a GL?)
❓ 2.3 Why can't you simply cancel a work order that has actual costs on it?
❓ 2.4 Status history lives in its own table (`WOSTATUS`). Why a separate table instead of just the `STATUS` column on `WORKORDER`?

---

## Lab 3 — Plans vs. Actuals (the cost "fact table")

**Concept:** **Plans** tab = estimate (`WPLABOR`, `WPMATERIAL`). **Actuals** tab = what really happened
(`LABTRANS`, `MATUSETRANS`). Costs roll up to the work order and to the asset.

Tasks:
1. New work order on your asset. On **Plans**: add 1 labor line (e.g., 2 hrs) and 1 material line (an item from a storeroom).
2. Approve it. Note the **estimated** cost fields.
3. On **Actuals**: report 3 hrs of labor and the material actually used. (Or use the "Select Planned Labor/Materials" shortcut.)
4. Open **View Costs** (action menu) and compare estimated vs actual.
5. Check the storeroom: did the item's **current balance** go down? (Inventory app → that item → storeroom.)

❓ 3.1 Estimated vs actual: what are the numbers, and what explains the difference?
❓ 3.2 Which tables did each step write to? (Use your Session 1 table.)
❓ 3.3 Your **Scenario 1** from Session 1: now answer it properly using what you saw here.

---

## Lab 4 — Child, Related & Follow-up work orders (⭐ core topic)

**Concept:**
- **Child WO / task**: part of a hierarchy under a parent WO (costs can roll up to the parent).
- **Follow-up WO**: created *from* an existing WO for extra work discovered on the job.
- **Related record**: a link between records (WO↔WO, WO↔SR) with no hierarchy.

Tasks:
1. Create a parent WO. Add **2 child work orders** and **1 task**. Change the parent's status. What happens to the children?
2. On a WO in progress, create a **follow-up work order** (action menu). Look at what was copied over.
3. On another WO, add a **related record** to an existing WO.
4. Report actuals on a child WO. Check the parent's **View Costs**: does it include the child's cost?

❓ 4.1 Explain the difference between child, follow-up and related in your own words, with a real example for each (e.g., "transformer overhaul").
❓ 4.2 When the parent's status changed, did children follow? Is that always what you'd want? (Look for a "roll down" option.)
❓ 4.3 Data-model question: how do you think Maximo stores the parent link? (Hint: one column on `WORKORDER`.) Write the self-join SQL you'd use to list a parent with its children.

---

## Lab 5 — Job Plans & Preventive Maintenance (the "rule → generated transaction" pattern)

**Concept:** a **Job Plan** is a reusable template. A **PM** is a schedule that *generates* work orders
from that template, like a batch rule generating transactions on a schedule.

Tasks:
1. Open **Job Plans**. Create one: 2 tasks, 1 labor line, 1 material line. Make it **ACTIVE**.
2. Open **Preventive Maintenance**. Create a PM: your asset + your job plan, frequency 30 days.
3. Make the PM active, then **Generate Work Orders** (action menu) for it now.
4. Open the generated WO. What came from the job plan? What is the WO's status?

❓ 5.1 Why have a job plan *and* a PM, instead of putting tasks directly on the PM? (Think reuse and normalisation.)
❓ 5.2 Time-based vs meter-based PM: give one asset where each makes more sense, and why.
❓ 5.3 In real life, PMs generate WOs automatically overnight. What Maximo feature do you think runs that? (Hint: it's a scheduled background task; you'll meet it in Lab 8.)

---

## Lab 6 — Which app for which job? (⭐ core topic)

**Concept:** a key skill is knowing when to use **Work Order Tracking** vs **Quick Reporting** vs the
role-based **Work Orders / technician** apps in MAS.

Tasks:
1. Open **Quick Reporting**. Report a small job (e.g., "replaced fuse") in a single step: create, report actuals, complete.
2. Compare with how many steps the same job took in Work Order Tracking (Lab 2–3).
3. If your trial has the role-based/mobile **Technician** or **Work Supervisor / Work Orders** apps, open them and do one action (e.g., start/complete a work assignment).
4. Open **Service Requests**. Create an SR ("Air-con not working in Room 12"). Create a WO from it. Check the relationship between the two.

❓ 6.1 Make a decision table: Situation → App you'd use → Why. Include at least: a planned overhaul, a 10-minute emergency fix, a field technician on a phone, a user reporting a problem.
❓ 6.2 Why would a company *not* let field technicians use Work Order Tracking?

---

## Lab 7 — Search like a SQL person

**Concept:** Maximo's List tab can take a raw **WHERE clause** (Advanced Search → Where Clause).
This is where your SQL skill shows. Read-only, and safe.

Tasks:
1. In Work Order Tracking → Advanced Search → **Where Clause**, write a clause for: WOs at your site, status INPRG or APPR, reported in the last 90 days.
2. Save it as a **query** and add it to your **Start Center** as a result-set portlet.
3. Write a clause using a **subquery** on another table (e.g., WOs whose asset is at a given location).

❓ 7.1 Paste your WHERE clauses in the log.
❓ 7.2 Why is `siteid` in almost every clause you write?
❓ 7.3 Why is a WHERE clause in the UI safe, while `UPDATE` in SQL Developer is not? (Your Session 1 Scenario 2.)

---

## Lab 8 — Technical peek (optional, read-only; may not be accessible in the trial)

**Do not change anything here.** Look and take notes. This is technical-role and interview territory.

| App | What to look at |
|---|---|
| **Database Configuration** | Open object `WORKORDER`: attributes (`WONUM`, `SITEID`, `STATUS`, `PARENT`), relationships. |
| **Domains** | Find the `WOSTATUS` **synonym domain**: internal values vs. your display values. |
| **Cron Task Setup** | Find the PM work-order generation cron task (Lab 5.3). Look at its schedule. |
| **Escalations** | Open one: what condition (SQL) and what action? |
| **Automation Scripts** | Open one: language (Jython/JavaScript) and launch point type. |
| **Workflow Designer** | Open any workflow (e.g., WO approval) and trace the nodes. |
| **Application Designer** | Open `WOTRACK` and see how a screen is built from XML/controls. |

❓ 8.1 Synonym domain: why does Maximo let a company rename "APPR" to "Approved for Work" but still treat it internally as APPR? (Hint: business logic in code.)
❓ 8.2 Escalation vs Workflow vs Automation Script: one sentence each on *when* you'd use it.
❓ 8.3 OFSAA bridge: which OFSAA concept is most like a Maximo cron task? Like Database Configuration metadata? (Answer honestly from what *you* have used.)

---

## Lab log template

Copy this into `ibm-maximo/lab-log.md` and fill it as you go.

```markdown
# Maximo Lab Log

## Lab N — <title>   (date: YYYY-MM-DD)
**What I did:**
-
**What surprised me / errors I saw (exact message):**
-
**Answers:**
- N.1:
- N.2:
**Still confused about:**
-
```

---

## Suggested 14-day trial schedule

| Day | Lab |
|---|---|
| 1 | Setup + Lab 1 |
| 2–3 | Lab 2 (statuses: repeat until you can predict every allowed/blocked action) |
| 4 | Lab 3 |
| 5 | Lab 4 |
| 6–7 | Lab 5 |
| 8 | Lab 6 |
| 9 | Lab 7 |
| 10 | Lab 8 (if accessible) |
| 11–13 | Redo Labs 2, 4 and 6 **without this guide** |
| 14 | Review weak spots, export or screenshot your saved queries |

**Honesty reminder:** these labs are *training*, not project experience. On a resume, write
"Hands-on lab practice, IBM Maximo Application Suite trial (2026)", never a Maximo implementation.
