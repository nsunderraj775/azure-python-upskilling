# Week 1 Hands-On Lab — See Day 1, 2 & 3 Concepts Live

> Goal: build a small set of resources in the Azure portal so the concepts from
> Days 1–3 become **concrete**. Everything goes in ONE resource group so cleanup
> is a single action.

## 🛡️ Cost-safety rules (read first)
- Put **everything** in one resource group: **`rg-week1-lab`**.
- Use only the **free/cheapest tiers** noted below.
- **Do NOT create** VPN Gateway or ExpressRoute (they cost real money + deploy slowly). Just open their create blades to *see* the options, then cancel.
- **Delete the resource group** when finished → removes everything at once.
- After deleting, glance at **Cost Management → Cost analysis** to confirm nothing lingers.

---

## STEP 0 — Resource Group  *(Day 1: resource groups · Day 2: hierarchy + regions)*
1. Portal → search **Resource groups** → **Create**.
2. Name: `rg-week1-lab`. **Region:** pick one near you (e.g., East US).
3. Create.

👀 **What to notice / concepts seen:**
- **Region dropdown** = Day 2 *regions*. See how many there are.
- Breadcrumb shows **Subscription → Resource group** = Day 2 *hierarchy* (MG → Subscription → RG → Resource).

---

## STEP 1 — Storage Account  *(Day 1: SaaS/PaaS storage, cloud benefits · Day 2: redundancy/AZ)*
1. In `rg-week1-lab` → **Create** → **Storage account**.
2. Cheapest: **Performance = Standard**, **Redundancy = LRS** (cheapest).
3. Create → then open it → **Containers** → upload any small file (Blob storage).

👀 **Concepts seen:**
- **Redundancy dropdown (LRS / ZRS / GRS)** = Day 2 *storage redundancy + region pairs*. Read each option's description — ZRS spreads across **availability zones**, GRS copies to the **paired region**.
- You uploaded a file without managing any server = **PaaS/consumption** (Day 1).

---

## STEP 2 — App Service (PaaS web app)  *(Day 1: PaaS · Day 3: App Service vs VM)*
1. In `rg-week1-lab` → **Create** → **Web App**.
2. **Runtime**: pick any (e.g., .NET or Node). **OS**: Linux.
3. **Pricing plan**: choose the **Free F1** tier (no cost!).
4. Create → browse to the app's default URL — it's live.

👀 **Concepts seen:**
- You deployed a running web app and **never touched the OS or servers** = **PaaS** (Day 1) and **App Service** (Day 3).
- Compare mentally to Step 3's VM, where you *do* get the OS.

---

## STEP 3 — Virtual Machine (IaaS)  *(Day 1: IaaS · Day 2: availability zones · Day 3: VM, vertical scaling)*
1. In `rg-week1-lab` → **Create** → **Virtual machine**.
2. **Size**: click "See all sizes" → pick **B1s** (cheapest burstable). *(A B1s is free-tier eligible for 750 hrs/month for 12 months on a free account.)*
3. **Availability options** dropdown → look at **Availability zone** vs **Availability set** vs **No infrastructure redundancy**.
4. Create (or just review and cancel to save credit).

👀 **Concepts seen:**
- **Availability options dropdown** = Day 2 *availability zones* + Day 3 *availability sets* — see them as real choices.
- **VM sizes list** = Day 3 *vertical scaling* (scale up = pick a bigger size).
- You get to choose the **OS** = **IaaS** (Day 1) — the opposite of Step 2's App Service.
- ⚠️ If you create it, it **bills hourly** — delete the whole RG soon after.

---

## STEP 4 — Virtual Network with 2 subnets  *(Day 3: VNet, subnets)*
1. In `rg-week1-lab` → **Create** → **Virtual network**.
2. On the **IP addresses** tab, add **two subnets** (e.g., `subnet-web`, `subnet-data`).
3. Create.

👀 **Concepts seen:**
- A **VNet** carved into **subnets** = Day 3 networking. This is like segmenting a network — maps to how you'd separate tiers (web vs data), similar to logical separation in data design.
- (VNets are free — safe to keep briefly.)

---

## STEP 5 — LOOK-ONLY: VPN Gateway & ExpressRoute  *(Day 3: hybrid networking trap)*
> ⚠️ **Do NOT create these** — expensive + slow. Just open the create blade to *see* them, then **Cancel**.
1. Search **VPN Gateway** → **Create** → read the options (note it connects **over the internet**, encrypted) → **Cancel**.
2. Search **ExpressRoute** → **Create** → note it's a **private, dedicated** circuit (bandwidth options, provider) → **Cancel**.

👀 **Concepts seen:**
- Seeing the two create screens side by side cements the **VPN Gateway (internet) vs ExpressRoute (private/dedicated)** distinction (Day 3).

---

## STEP 6 — See the hierarchy & benefits  *(Day 2: hierarchy · Day 1: manageability)*
1. Open `rg-week1-lab` → the **Overview** lists ALL your resources (storage, web app, VM, VNet) in one container.
2. Notice: one container, many resource types, possibly different regions = Day 2 *"resources in an RG can be in different regions."*
3. Open **Subscriptions** blade → see your subscription (the billing/access boundary above the RG).

---

## STEP 7 — 🧹 TEAR DOWN (the most important step!)  *(Day 1: RG shared lifecycle)*
1. Open `rg-week1-lab` → **Delete resource group** → type its name to confirm.
2. Watch **every** resource disappear in one action = Day 1 *"delete the RG = delete everything, no stragglers billing me."*
3. **Cost Management → Cost analysis** → confirm nothing is still accruing.

---

## Concept → where you saw it (quick map)
| Concept | Step |
|---|---|
| Resource group / shared lifecycle (Day 1) | 0, 7 |
| PaaS vs IaaS (Day 1) | 2 (App Service) vs 3 (VM) |
| Serverless/consumption (Day 1) | (optional: add an Azure Function, Consumption plan) |
| Regions (Day 2) | 0 |
| Availability zones / sets (Day 2/3) | 3 (VM availability options) |
| Storage redundancy / region pairs (Day 2) | 1 (LRS/ZRS/GRS dropdown) |
| Management hierarchy (Day 2) | 0, 6 |
| VM / vertical scaling (Day 3) | 3 |
| VNet / subnets (Day 3) | 4 |
| VPN Gateway vs ExpressRoute (Day 3) | 5 (look-only) |
