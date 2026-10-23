# Menu: authentication and authorization

Decides: who users are (authentication) and what they may do (authorization).
Cost to reverse: one-way.

## Questions to answer first
- Who are the users: staff of one organization, customers, other systems?
- Does the organization already have an identity provider (single sign-on)?
- How sensitive is the data (data requirements, compliance NFRs)?
- Do permissions depend on roles only, or also on the specific record (for example, "only my clients")?

## Authentication options
| Option | Good for | Costs |
|---|---|---|
| **Managed identity provider / SSO (default)** | Almost everything; existing org accounts | Vendor dependency, cost per user |
| Self-hosted identity server | Data must stay in-house, many apps | You operate security-critical software |
| Build your own (passwords in our DB) | Rarely justified | Security risk, password resets, MFA, audits all on you |
| API keys / service credentials | Machine-to-machine | Rotation and storage of secrets |

## Authorization options
| Option | Good for | Costs |
|---|---|---|
| **Role-based (RBAC) (default)** | Few, stable roles | Gets clumsy with many exceptions |
| Attribute / relationship-based | Access depends on ownership, team, record | More complex to design and test |
| Per-resource sharing lists | Document-style sharing | Hard to audit at scale |

## Default
**Managed identity provider with SSO, plus role-based access control enforced on the server.**

## Choose another option when
- **Self-hosted identity** if a compliance or data-residency requirement forbids a managed provider.
- **Attribute/relationship-based** if requirements say access depends on who owns or is assigned to a record.
- **API keys** in addition, for machine clients.

## Common mistakes
- Checking permissions only in the UI. The server must always check.
- Building your own password handling.
- No audit log when the data is sensitive.
