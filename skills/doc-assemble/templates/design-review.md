# Export: design-review
Audience: engineers, reviewers · Purpose: approve the design gate
Owner: <tech lead> · Sensitivity: internal

## Questions this document must answer
1. What problem are we solving, for whom?
2. What are the main parts and how do they connect?
3. Which hard-to-reverse decisions did we make, and why?
4. What are the contracts (API, data)?
5. What could go wrong (threats, risks)?

## Selection
| Source | Depth | Filter |
|---|---|---|
| product/stories.md | summary | by epic |
| product/requirements.md | key table | Must FRs + all NFRs |
| decisions/ | full | accepted, one-way |
| design/architecture.md | full | |
| design/data-model.md | full | |
| design/api.md | full | |
| design/ux.md | link | |
| design/security.md | key table | threats rated high or medium |
| project/risks.md | key table | open |

## Never include
- Credential register, secret values
- Task status, plan details

## Order
1. Problem and scope 2. Architecture 3. Key decisions 4. Data and API 5. Threats and risks 6. Open questions
