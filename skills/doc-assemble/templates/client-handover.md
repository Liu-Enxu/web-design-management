# Export: client-handover
Audience: client or operator taking over · Purpose: run, change and support the system
Owner: <project lead> · Sensitivity: client

## Questions this document must answer
1. What does the system do and what is out of scope?
2. How is it built and deployed?
3. How do we operate, monitor and recover it?
4. How do we change it safely?
5. Who holds which role after handover?

## Selection
| Source | Depth | Filter |
|---|---|---|
| product/requirements.md | full | scope, NFRs |
| design/architecture.md | full | |
| decisions/ | key table | accepted |
| design/api.md | link | link to spec |
| design/data-model.md | summary | |
| design/security.md | key table | roles only; names only if agreed |

## Never include
- Credential register and secret values (hand over secrets through the secret manager)
- Internal risks, retros, change log, team details

## Order
1. Overview 2. Scope 3. Architecture 4. Changing the system 5. Roles
