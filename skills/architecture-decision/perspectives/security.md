# Security perspective

## Exposure
- Does this add or move a trust boundary (new public endpoint, new third party, new admin tool)?
- What sensitive data does it touch, store or send out?
- Does any data leave our control (third-party APIs, model providers, analytics)?

## Access
- Who can use it, and how is that enforced on the server?
- Does it create a new privileged role or credential? Who will hold it?
- How are secrets for it stored and rotated?

## Abuse and failure
- Which STRIDE threats does it introduce? (See `rules/security.md`.)
- Can it be abused at scale (rate limits, cost explosion, enumeration)?
- Is there an audit trail for sensitive actions?

## Red flags
- Authorization checked only in the client.
- Shared or personal credentials used by the system.
- Sensitive data in logs, URLs or analytics events.
- A third party receiving data that the data requirements mark as restricted.

Outcome: new threats go into `docs/design/security.md`; the security design (`rules/security.md`) is redone if the decision adds a boundary, role or credential.
