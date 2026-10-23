# Rules: security testing

Used in stage 6 for every change, and in full before each release.
Team TODO: frontend lead to extend with the team's own test approach.

## Per pull request (reviewer checks)
- [ ] Every new or changed operation checks authorization **on the server**, per the role matrix in `security.md`.
- [ ] All input validated on the server (type, length, format); output encoded for its context (HTML, SQL, shell).
- [ ] Mitigations linked to this task (`TH-xx`) are actually implemented and tested.
- [ ] No secrets in code, config files, logs, URLs or error messages; new credentials added to the register (no values).
- [ ] Sensitive data not logged; personal data handled per its retention rule.
- [ ] File uploads: type and size checked, stored in object storage, served with safe content type.
- [ ] New dependencies: known, maintained, no known critical vulnerabilities.

## Automated (in CI)
| Check | What it catches |
|---|---|
| Dependency scan | Libraries with known vulnerabilities |
| Secret scan | Keys or passwords committed by mistake |
| Static analysis (security rules) | Injection, unsafe functions, weak crypto |
| Authorization tests | One test per role per sensitive operation: allowed and denied |

## Before release
- [ ] Re-run the threat review in `architecture-decision/rules/security.md` for anything new.
- [ ] Test the top threats directly (for example: access another user's record by changing an ID; call an admin operation as a normal user; upload a wrong file type; send oversized input).
- [ ] For AI features: try prompt injection through retrieved content; confirm restricted data is not sent to model providers.
- [ ] Access list current; leavers removed.

## Team additions
- 
