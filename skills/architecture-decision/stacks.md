# Common stacks (team defaults)

The menus stay stack-neutral. This file is where the team names the concrete stacks it knows well, so stage 3 can offer them as default options. One row per profile; keep 1–6 profiles. Anything marked "stage 3" is decided per project in a decision record.

**These profiles are starting points, not templates.** Never copy one as the project's architecture. Work the real architecture out with this skill (`SKILL.md`): propose from the requirements, decide each menu, and record every choice in a decision record. A profile only saves time where it already fits.

## Frontend baseline (every profile)

| Part | Tool | Rule |
|---|---|---|
| Framework | React 18 | |
| Language | TypeScript | |
| Build | Vite | |
| Package manager | npm | Commit `package-lock.json`; CI installs with `npm ci` |
| Code quality | ESLint | Finds bugs and risky code |
| CSS | Tailwind CSS | |

## Profiles

| Profile | Use when | Shape | Backend | Database, auth, files | Cache | Hosting |
|---|---|---|---|---|---|---|
| A. Supabase only (default) | Login, user-owned records, files; nothing secret or heavy on the server | Page → Supabase | none | Supabase | none | Frontend on Vercel or Cloudflare Pages |
| B. Supabase + Railway backend | A server-only secret (such as an AI API key), scraping or integrations, or logic row-level security can't express | Page → backend → Supabase; the backend calls external APIs | stage 3 | Supabase | Redis when triggered | Frontend on Vercel or Cloudflare Pages; backend and Redis on Railway |
| C. Own database | Data must stay in a specific region or on-premise, company single sign-on, or compliance needs full control of the database | Page → backend → PostgreSQL | stage 3 | PostgreSQL on Railway; auth: stage 3 | Redis when triggered | Frontend on Vercel or Cloudflare Pages; backend, PostgreSQL and Redis on Railway |

Client state in every profile: React state; Redux Toolkit when triggered (see below); query layer: stage 3.

## How to choose

Read the stories, requirements and data requirements, then match:

| If they say… | Choose |
|---|---|
| Standard email or social login; "users only see their own X"; image or file uploads; live chat or notifications | **A**: row-level security covers "only their own X", Realtime covers live updates |
| A secret key the browser must never see (AI or paid APIs); scraping or integrations that retry; server logic beyond row-level security | **B**: keep Supabase, put a backend on Railway in front of it |
| Data must stay on-premise or in a specific region or provider; company single sign-on; compliance needs full control of the database | **C** |
| A rate limit, sessions shared across servers, a job queue, fast counters or leaderboards, repeated expensive external or AI calls, or a speed target still missed after fixing queries | **Add Redis** (B or C). Never the only copy of data; never added "to be fast" without a measurement |
| Editors, multi-step wizards sharing state across screens, undo/redo, offline drafts, many components changing the same data | **Add Redux Toolkit**. Otherwise server data goes through a query layer and screen state stays in the component |

Supabase is a hosted PostgreSQL, so all three profiles share the data-type rules in `rules/data.md`. By kind of data:

| Data | Store |
|---|---|
| Related records (users, orders) | PostgreSQL tables |
| Images and files | Supabase Storage (A, B) or S3-compatible storage (C) |
| Flexible extra fields | PostgreSQL `jsonb` |
| Text or semantic search | PostgreSQL full-text or pgvector first, before a separate store |

## Per-category preferences

| Category (menu) | Preferred tool | Why | Avoid when |
|---|---|---|---|
| rendering | React 18 + Vite | Team baseline | |
| state-management | React state; Redux Toolkit when triggered; query layer: stage 3 | Keep global state small | |
| data-storage | PostgreSQL (Supabase in A and B, Railway in C) | Relational default | |
| caching | None; Redis on Railway when triggered | No cache without a measurement | |
| background-work | stage 3 | | |
| auth | Supabase Auth (A, B); stage 3 (C) | | Company single sign-on needed |
| deployment | Vercel or Cloudflare Pages (frontend); Railway (backend, PostgreSQL, Redis) | Team has shipped with all three | |
| observability | UptimeRobot health check on the backend (B, C); the rest: stage 3 | | |
| testing | stage 3 | | |

## Services we've shipped with

Options for stage 3 when a requirement needs them, not defaults.

| Need | Service |
|---|---|
| Maps | Mapbox |
| AI model API | DeepSeek (called from the backend only; key never in the browser) |
| Uptime checks | UptimeRobot |

## Rules
- Add a tool only if at least one person on the team has shipped with it.
- Changing a default is a pull request to the skills repo, reviewed by someone who has shipped with the tool.
