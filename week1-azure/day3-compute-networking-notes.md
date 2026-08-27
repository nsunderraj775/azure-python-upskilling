# Week 1 · Day 3 — Compute & Networking (my notes)

> Module: "Describe Azure compute and networking services." Focus: **apply**, not recall.

---

## Compute options

| Option | Its job | Signal words |
|---|---|---|
| **Single VM** | One machine, full OS control (IaaS) | "one server," "lift-and-shift," "custom OS/drivers" |
| **VM Scale Set (VMSS)** | **Auto-scale** identical VMs up/down with demand (= elasticity for VMs) | "**automatically add/remove** instances," "handle traffic spikes" |
| **Availability Set** | **High availability** — spread VMs across fault/update domains to survive hardware failure/maintenance | "**stay available**," "avoid downtime," "if one VM goes down the other serves" |
| **App Service** | PaaS web app hosting — just deploy code, no OS to manage | "web app," "don't manage OS/servers," "just deploy code" |
| **Azure Functions** | Serverless, event/schedule-triggered, pay-per-execution (Day 1) | "run on a trigger," "pay per execution," "no infra" |

> **Scale Set vs Availability Set (my miss → fixed):** Scale Set = handle *demand*; Availability Set = avoid *downtime*. Different problems. The scenario about "auto add/remove VMs for holiday traffic" = **Scale Set** (I wrongly said Availability Set first).

### Containers
- **ACI (Container Instances)** — a **few simple containers**, fast, no orchestration. "just run a container or two."
- **AKS (Kubernetes Service)** — **orchestrate many containers** at scale: deployment, scaling, self-healing, load balancing. "dozens of microservices working together." ✅ got this first try.

---

## Networking

- **Virtual Network (VNet)** — private network in Azure; segmented into **subnets**.
- **Peering** — connect two VNets so they communicate.
- **Azure DNS** — name resolution.

### ⭐ VPN Gateway vs ExpressRoute (the hybrid trap — my miss → fixed)

| | Connects via | Use when… |
|---|---|---|
| **VPN Gateway** | **Public internet**, encrypted tunnel | Lower cost, occasional/site-to-site, OK going over internet if secure |
| **ExpressRoute** | **Private, dedicated line — NOT over the internet** | High bandwidth, consistent low latency, large sensitive data volumes |

> **Deciding tell:** "private / dedicated / NOT over the internet / high bandwidth" → **ExpressRoute**. "over the internet but encrypted / cheaper / occasional" → **VPN Gateway**.
> I first picked VPN Gateway for a "never touch the public internet" scenario — wrong; that phrase forces **ExpressRoute**.

---

## Day 3 drill record
- Scale Set vs Availability Set → ❌ then ✅
- VPN Gateway vs ExpressRoute → ❌ then ✅
- ACI vs AKS → ✅ first try
- **Lesson:** each miss became solid once I found the deciding clue. Keep asking "which word forces the answer?"

## App Service vs VM (✅ nailed it)
- **App Service** (PaaS) → "just deploy code," "don't want to manage OS/servers," standard web app.
- **Virtual Machine** (IaaS) → "need OS control," "install custom software at OS level," "lift-and-shift," "specific OS version."
- **Tell:** don't want to manage the OS → App Service. Need OS control → VM. (Same IaaS/PaaS split from Day 1.)

## Day 3 checklist
- [x] VM / Scale Set / Availability Set
- [x] Containers (ACI vs AKS)
- [x] VNet / subnets / peering
- [x] VPN Gateway vs ExpressRoute
- [x] App Service vs VM
- [ ] Build task: create a VNet with 2 subnets; deploy an App Service sample app, then delete
- [ ] Consolidate: write 5 of my own scenario Q&As (plan task)
