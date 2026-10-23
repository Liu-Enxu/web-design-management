# Frontend perspective

## Data needs
- Can each Must screen get its data in a reasonable number of calls?
- Are loading, empty, error and permission states possible to show (does the API say why something failed)?
- Are real-time or pushed updates needed by any screen?

## User experience
- Effect on first load and navigation speed (rendering NFRs)?
- Does it work on the required devices, browsers and network conditions?
- Does auth (login, session expiry, roles) produce a usable flow?

## Code and team
- Does it fit the state-management rules (server state in a cache, little global state)?
- Can the frontend be developed against a mock or contract before the backend is ready?
- Does it add a framework or build complexity the team must learn?

## Red flags
- Business rules that only exist in the UI.
- Screens that need data the API contract does not provide.
- A rendering choice made for fashion, not for a requirement.
