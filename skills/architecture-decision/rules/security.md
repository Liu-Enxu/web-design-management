# Rules: security design (threats, admins, credentials)

Used in stage 3, step 10, and re-checked in `release-retro`. Output: `docs/design/security.md`.

## A. Threat model
1. **Trust boundaries.** From the container diagram, draw where data crosses a boundary: internet ↔ app, app ↔ third party, app ↔ admin tools.
2. **Assets.** Sensitive data (from `data-model.md`), credentials, availability of key flows.
3. **Threats per boundary (STRIDE):** Spoofing · Tampering · Repudiation (no proof who did what) · Information disclosure · Denial of service · Elevation of privilege. For AI features also: prompt injection through retrieved content, data leaking to model providers, unsafe tool actions.
4. **Rate** likelihood × impact (low / medium / high). Decide: mitigate, accept (named approver), or transfer.
5. **Mitigations become NFRs or tasks.** Accepted threats are listed in `docs/project/risks.md`.

## B. Roles and admins
6. **Role matrix**: every human and machine role, what it can do, who grants it.
7. **Admin rules**: at least two named people per admin role; no shared accounts; least privilege; production access time-limited or on request; written offboarding steps.
8. **Environments**: who can deploy, read production data, change infrastructure.

## C. Credential register
9. Every secret: API keys, database credentials, signing keys, OAuth clients, cloud, domain and registrar, repo and design-tool admin accounts.
10. For each: purpose, **owner**, holders, storage location (secret manager path), rotation interval and last rotation, how to revoke, break-glass procedure.
11. **Never write secret values** in docs, code, tickets or chat.

## Re-run when
New external integration · new sensitive data type · new role or admin · auth change · before every release · after any incident.

## Output: docs/design/security.md

```markdown
# Security
Owner: · Audience: engineers, admins · Last reviewed:
Sources: DR-xxxx (auth), data-model.md, api.md

## Trust boundaries
<Mermaid data-flow diagram>

## Threats
| ID | Boundary / asset | STRIDE | Threat | Rating | Decision | Mitigation (NFR/T) | Approver |
|---|---|---|---|---|---|---|---|

## Roles
| Role | Can | Granted by | Holders (named for privileged roles) |
|---|---|---|---|

## Environment access
| Environment | Deploy | Read data | Change infra |
|---|---|---|---|

## Credential register (no values)
| Credential | Purpose | Owner | Holders | Stored at | Rotation | Last rotated | Revoke / break-glass |
|---|---|---|---|---|---|---|---|

## Offboarding checklist
- 
```
