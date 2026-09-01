# Week 1 · Day 4 — Storage, Databases & Identity (my notes)

> Modules: "Describe Azure storage services" + "Describe Azure identity, access, and security."
> Focus: **apply**, not recall. This is my data wheelhouse.

---

## STORAGE

### Storage services (in a storage account)
- **Blob** — objects / unstructured files (images, backups). *Signal: "store files/images/backups/unstructured objects."*
- **File** — managed file shares (SMB), mountable like a network drive.
- **Queue** — messaging between app components.
- **Table** — NoSQL key-value store.

### ⭐ Storage tiers (all about ACCESS FREQUENCY + retrieval speed)
| Tier | Access | Storage cost | Retrieval | Use for |
|---|---|---|---|---|
| **Hot** | frequent | highest | instant | active data |
| **Cool** | rare (30+ days) | lower | instant | backups, older data |
| **Cold** | very rare (90+ days) | lower still | instant | seldom-touched data |
| **Archive** | almost never | **lowest** | **hours (rehydrate)** | long-term compliance/archival |

> **Trade-off:** hot → archive = cheaper storage, but pricier + slower to retrieve.
> **Fastest tell = RETRIEVAL SPEED:** "must load instantly" → **Hot**. "OK to wait hours / not time-sensitive" → **Archive** (only archive has hours-long retrieval).
> **Drilled:** 7-yr compliance records, rarely accessed, OK to wait hours, cheapest → **Archive** ✅. Photos viewed constantly, load instantly → **Hot** ✅.

### ⭐ Redundancy (blast-radius ladder — same "count the regions" logic as Day 2)
| Option | Protects against | Copies |
|---|---|---|
| **LRS** | one datacenter failing | 3 copies, 1 datacenter |
| **ZRS** | a zone/datacenter failing | across **zones** in 1 region |
| **GRS** | an entire **region** failing | replicated to a **2nd region** |
| **GZRS** | zone + region failure | zones + 2nd region |

> **Tell:** "survive whole region / disaster / another region" → **GRS/GZRS**. "stay in one region" → **LRS/ZRS**.
> **Drilled:** survive complete regional disaster, data in another region → **GRS** ✅.

### Migration / data movement tools
- **Azure Data Box** — **physical device** Microsoft ships for **huge (TBs+) transfers / slow internet**. ✅ drilled (500 TB, slow internet).
- **AzCopy** — command-line/scripted copy.
- **Azure Storage Explorer** — GUI, drag-and-drop.
- **Azure File Sync** — keep on-prem file server synced with Azure.

---

## IDENTITY, ACCESS & SECURITY

### Authentication vs Authorization (classic trap)
| | Question | Service |
|---|---|---|
| **Authentication (AuthN)** | "**Who** are you?" (prove identity) | **Microsoft Entra ID** |
| **Authorization (AuthZ)** | "**What** can you do?" (permissions) | **RBAC** |

> Sequence: **authenticate first (Entra ID), then authorize (RBAC).** AuthN = who, AuthZ = what.

### Entra ID authentication methods
- **SSO** — log in once, access many apps.
- **MFA** — two+ *different* factors: know (password) · have (phone) · are (biometric).
- **Passwordless** — e.g., Windows Hello, authenticator app, security key.
- **Conditional Access** — rules that grant/block based on conditions (location, device, risk).

### Governance trio (who/what/protect)
| Service | Answers |
|---|---|
| **RBAC** | "**Who** can do **what**?" — grant a person/group permissions |
| **Azure Policy** | "**What's allowed to exist / how configured**?" — enforce tags, regions, sizes |
| **Resource lock** | "Stop this resource being deleted/changed" |

### Security concepts
- **Zero Trust** — "never trust, always verify." Principles: **verify explicitly · least privilege · assume breach.** (Tell: "least privilege," "verify even inside the network.")
- **Defense in depth** — **layered** security; if one layer fails, the next protects. (Tell: "layers," "multiple defenses.")
- **Encryption** — at rest (stored) + in transit (moving). **Azure Key Vault** = securely store **keys/secrets/certificates** (not hardcoded). *Will use in Week 4 capstone.*
- **Microsoft Defender for Cloud** — security **posture score + threat alerts/recommendations** across resources. (Tell: "security score," "threat protection across resources.")

> **Key Vault vs Defender:** Key Vault **stores** secrets; Defender **watches & scores** security.

---

## Day 4 checklist — COMPLETE ✅
- [x] Storage services (Blob/File/Queue/Table)
- [x] Storage tiers (hot/cool/archive)
- [x] Redundancy (LRS/ZRS/GRS/GZRS)
- [x] Migration tools (Data Box, AzCopy, Storage Explorer, File Sync)
- [x] Entra ID, SSO, MFA, passwordless, Conditional Access
- [x] Authentication vs Authorization; RBAC; RBAC vs Policy
- [x] Zero Trust, defense in depth, encryption/Key Vault, Defender for Cloud
- [ ] Optional build task: deploy Azure SQL DB (serverless), create a table, insert + SELECT (my wheelhouse)
