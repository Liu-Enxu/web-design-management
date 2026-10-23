# Menu: deployment and hosting

Decides: where the system runs and how changes reach it.
Cost to reverse: mixed (hosting is one-way-ish; pipeline details are two-way).

## Questions to answer first
- Data residency, compliance or "must run on our hardware" constraints?
- Expected load and how spiky it is (NFR)?
- Who on the team can operate infrastructure?
- Special hardware (GPUs, devices on-site)?

## Hosting options
| Option | Good for | Costs |
|---|---|---|
| **Managed platform (PaaS / managed containers) (default)** | Small teams, standard web apps | Less control, platform limits |
| Serverless functions | Spiky or low traffic, event-driven work | Cold starts, time limits, vendor lock-in |
| Containers on an orchestrator (Kubernetes-style) | Many services, dedicated ops skills | High operational cost |
| Virtual machines | Simple, full control, legacy software | Patching and scaling are on you |
| On-premises / edge devices | Data cannot leave, hardware on-site | Hardware lifecycle, remote updates |

## Pipeline (always)
- Automated build and tests on every change (CI).
- Automated deploy to a staging environment; production deploy is one command or one click.
- Environments: at least staging and production, configured the same way.
- Configuration and secrets outside the code.
- Infrastructure described as code where practical.

## Default
**Managed platform with CI/CD, staging + production.**

## Choose another option when
- **Serverless** for background or spiky workloads with short tasks.
- **Orchestrator** only with several services and someone whose job includes operating it.
- **VMs** for software that needs full OS control.
- **On-prem/edge** if a constraint or requirement demands it.

## Common mistakes
- Manual production deploys.
- Staging that differs from production in important ways.
