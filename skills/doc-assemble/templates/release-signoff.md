# Export: release-signoff
Audience: release approver · Purpose: approve or stop a release
Owner: <project lead> · Sensitivity: internal

## Questions this document must answer
1. What changes in this release?
2. Are all Must requirements met and tested?
3. Is it secure and fast enough?
4. What open risks remain, and how do we roll back?

## Selection
| Source | Depth | Filter |
|---|---|---|
| project/releases/<version>.md | full | |
| product/requirements.md | key table | Must FRs of this release, with test status |
| design/security.md | key table | changes since last release |
| design/performance.md | key table | budgets |
| project/risks.md | key table | open |

## Never include
- Design detail unrelated to this release
- Secret values

## Order
1. Summary 2. Requirements status 3. Security check 4. Performance 5. Risks and rollback 6. Decision
