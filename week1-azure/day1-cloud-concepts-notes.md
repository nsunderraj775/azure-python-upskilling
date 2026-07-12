# Week 1 · Day 1 — Cloud Concepts (my notes)

> Written after the "Describe cloud computing" module + a scenario-drill session.
> Focus: **applying** the service models, not just defining them (my known weak spot).

---

## The one mental model: shared responsibility

Cloud = handing layers of the stack to Microsoft. The **service model = how many layers I hand over.**

| Layer (bottom → top) | On-prem | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Physical datacenter / hardware | Me | MS | MS | MS |
| Network / virtualization | Me | MS | MS | MS |
| Operating system | Me | **Me** | MS | MS |
| Runtime / DB engine / middleware | Me | **Me** | MS | MS |
| Application | Me | **Me** | **Me** | MS |
| **Data & identity/access** | Me | **Me** | **Me** | **Me** ← ALWAYS me |

- Move **right** = manage less, control less.
- **I always own my data and who can access it** — in every model. (Exam trap.)

Analogy: **IaaS = empty plot** (I build the house) · **PaaS = furnished apartment** (I bring my furniture/code, landlord maintains building) · **SaaS = hotel** (I just show up).

---

## The 3 anchor examples (memorize one per model)

| Model | Classic example | The tell |
|---|---|---|
| **IaaS** | A **Virtual Machine** I configure | "I need OS control / lift-and-shift / custom drivers" |
| **PaaS** | **Azure App Service** (I deploy *my* code) | "I'm building/deploying an app but don't want to manage servers/OS" |
| **SaaS** | **Microsoft 365 / Outlook / Teams** | "I just want to *use* ready-made software" |

## Two tests that decide any scenario

1. **OS test** — "Do they want to control/manage the OS?"
   - Yes → **IaaS**. No → PaaS or SaaS.
2. **"Who wrote the app?" test** (settles PaaS vs SaaS — my main confusion)
   - Customer built/deployed it → **PaaS** (never SaaS!)
   - Someone else built it, customer just uses it → **SaaS**

> **Iron rule: if *I* wrote/deployed the app, it is NEVER SaaS.**
> Don't react to the word "app" — ask **"who wrote it?"**

---

## New signal words → add to Appendix A

| Scenario says… | Signals | Answer |
|---|---|---|
| "lift and shift" | move app as-is | **IaaS** |
| "specific/older version of the OS", "install X at the OS level", "custom drivers" | OS control | **IaaS** |
| "only runs on Windows Server 2012" (a fixed OS) | OS control | **IaaS** |
| "deploy **our custom** app, let Azure manage the OS/servers" | my code, managed platform | **PaaS** |
| "managed database — just use it, no patching the OS or DB engine" | managed data platform | **PaaS** |
| "give employees email / Office / calendars", ready-made software | just consume | **SaaS** |

---

## Scenario quiz-bank (today's 6 — cover the answers and re-drill later)

1. Bank lift-and-shifts a legacy risk app needing a specific old OS + custom drivers. → **IaaS** ✅
2. Build a brand-new web app, let Azure handle OS/patching/servers. → **PaaS** (I missed → said SaaS)
3. Give employees email, calendars, Office apps, build nothing. → **SaaS** (I missed → said PaaS)
4. Lift-and-shift a 10-yr-old app that only runs on Windows Server 2012. → **IaaS** ✅
5. Deploy our custom Python web app, Azure manages servers/OS. → **PaaS** (I missed → said SaaS)
6. Run PostgreSQL without patching OS or DB engine, just use the DB. → **PaaS** ✅

**Lesson from my misses:** all 3 were the **PaaS↔SaaS** boundary. Fix = the "who wrote the app?" test.

---

## Resource groups (created hands-on in the portal ✅)

- A **logical container** that groups related resources so I can **manage/delete them as a unit**.
- **#1 benefit: shared lifecycle** — delete the resource group → *all resources inside are deleted together* (clean teardown, no stragglers billing me). This is how I protect my free credit: deploy into one RG, then delete the RG.
- Also lets me apply **cost tracking, RBAC, tags, and policies** at the group level.
- **Exam facts:**
  1. Every resource lives in **exactly one** resource group.
  2. An RG has a **region** (for its metadata) **but its resources can be in different regions**. (Trap!)
  3. A resource **can be moved** between resource groups.
- **Did it:** created a sandbox RG, deployed VM + storage + SQL + VNet into it, then **deleted the RG** → all gone at once. Good-habit check: glance at **Cost Management → Cost analysis** to confirm nothing's still billing.

---

## CapEx vs OpEx ✅

| | On-prem OFSAA | Azure cloud |
|---|---|---|
| **Model** | **CapEx** | **OpEx** |
| **Payment** | Big **upfront** purchase | **Pay-as-you-go**, ongoing/monthly |
| **You own** | The hardware (a capital asset) | Nothing — you rent |

- **CapEx** = capital expenditure — pay upfront, before/regardless of usage; own the asset.
- **OpEx** = operational expenditure — ongoing recurring cost, pay only for what you use.
- **Why OpEx/cloud is attractive:** no large upfront investment, cost **scales with usage**, turns big unpredictable purchases into **predictable** operating costs.

**OpEx signal words** (add to Appendix A): "pay only for what you use / month to month" · "no upfront investment / no upfront cost" · "avoid buying hardware that might sit idle" · "consumption-based".

**Scenario I nailed:** startup, no upfront cash, unpredictable load, wants to pay only for compute used → **OpEx**. Proof phrases: *"pay only for what you use, month to month"* + *"avoid buying expensive hardware that might sit idle."*

---

## To review / still to cover on Day 1
- [ ] Public / private / hybrid cloud models + use cases
- [x] ~~CapEx vs OpEx~~ ✅
- [ ] Consumption-based / serverless pricing
- [ ] Benefits: high availability, scalability, elasticity, reliability, predictability (Microsoft's exact wording)
- [x] ~~Build task: create a Resource Group in the portal~~ ✅ (find the cost/billing blade next time)
