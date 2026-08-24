# Week 1 · Day 2 — Azure Architecture & Core Structure (my notes)

> Module: "Describe the core architectural components of Azure."
> Focus (as always): **apply**, not just recall.

---

## Physical infrastructure (top → bottom)

- **Geography** — a discrete market/area (often a country); contains regions; used for **data residency & compliance**.
- **Region** — a set of datacenters within a latency-defined perimeter, connected by a low-latency network. (e.g., East US, West Europe.)
- **Availability Zone (AZ)** — **physically separate datacenters *within a region***, each with independent power, cooling, networking.
- **Datacenter** — the physical building of servers.

### Ways to use zones
- **Zonal** — resource pinned to a *specific* zone (you pick).
- **Zone-redundant** — resource replicated *across* zones automatically.
- **Non-regional** — service isn't tied to one region (global).

### Region pairs & sovereign regions
- **Region pair** — each region paired with **another region in the SAME geography** (100+ miles apart) for disaster recovery / data residency. Some services replicate to the pair automatically; sequential updates roll out one region at a time.
- **Sovereign regions** — isolated Azure instances for special compliance (e.g., Azure Government, Azure China).

---

## ⭐ THE key exam trap: Availability Zone vs Region Pair

> **Decision rule: COUNT THE REGIONS.**
> - Scenario stays in **ONE** region → **Availability Zone**
> - Scenario needs a **SECOND** region / failover to another region → **Region Pair**

| Protection | Guards against… | Regions involved |
|---|---|---|
| **Availability Zone** | a **single datacenter** failing | **One** region (zones are inside it) |
| **Region Pair** | an **entire region** failing (disaster) | **Two** regions |

**Signal words:**
- "one datacenter" / "stay within [region]" / "low latency, single region" → **AZ**
- "entire region down" / "disaster/earthquake/hurricane" / "fail over to another region" / "replicate to a second region" → **Region Pair**

**Scenarios I drilled:**
1. App survives a hurricane wiping the whole region, replicates to a 2nd region → **Region Pair** ✅
2. DB stays online if one datacenter fails, no 2nd region wanted → **AZ** ✅
(Started by missing these, then got both right once I applied "count the regions.")

---

## Management infrastructure — the hierarchy

> **Management Group → Subscription → Resource Group → Resource**
> (broadest → narrowest; each contains the one below; **settings cascade DOWN**)

| Level | Contains | Purpose |
|---|---|---|
| **Management Group** | subscriptions (and other MGs) | Govern **many subscriptions** at once (policy/RBAC at scale). Top = **tenant root group**. |
| **Subscription** | resource groups | A **billing + access boundary** (costs roll up here). |
| **Resource Group** | resources | Logical container to **manage resources as a unit** (delete RG = delete all inside). |
| **Resource** | — | The actual service (VM, storage account, database, VNet…). |

- **Cascade rule:** apply a policy/RBAC role at any level → it flows to everything beneath it (current + future). Apply once at the top, govern everything below.
- **My earlier slip (fixed):** a management group manages **subscriptions**, NOT resource groups directly.
- **OFSAA analogy:** nested parent→child containers where governance flows downhill.

---

## Day 2 checklist
- [x] Regions, region pairs, sovereign regions
- [x] Availability zones (+ the AZ vs Region Pair trap)
- [x] Datacenters
- [x] Resources, resource groups, subscriptions, management groups + hierarchy
- [ ] Build task: deploy a cheap VM (B-series) + storage account, then delete (protect credit!)
- [ ] Draw the resource hierarchy from memory (plan's consolidate task)
