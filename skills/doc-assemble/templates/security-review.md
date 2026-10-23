# Export: security-review
Audience: security reviewer, auditor · Purpose: assess threats and controls
Owner: <security owner> · Sensitivity: internal

## Questions this document must answer
1. Where are the trust boundaries and what crosses them?
2. What threats exist and how are they handled?
3. Who can access what, and who is admin?
4. Who owns each credential, where is it stored, how is it rotated?
5. How is sensitive data handled?

## Selection
| Source | Depth | Filter |
|---|---|---|
| design/security.md | full | trust boundaries, threats, roles, environment access |
| design/security.md | key table | credential register: owner, storage, rotation only |
| decisions/ | full | category auth, plus any decision touching data or integrations |
| design/data-model.md | key table | sensitivity and retention columns |
| design/architecture.md | key table | container diagram only |
| project/risks.md | key table | accepted threats |

## Never include
- Secret values (always)

## Order
1. Boundaries 2. Threats 3. Access and admins 4. Credentials 5. Data handling 6. Accepted risks
