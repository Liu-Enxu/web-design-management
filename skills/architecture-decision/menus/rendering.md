# Menu: rendering (user interface delivery)

Decides: where and when the user interface is produced. N/A for projects with no UI (APIs, CLIs, firmware).
Cost to reverse: one-way.

## Questions to answer first
- Must pages be found by search engines or shared with link previews?
- Is it behind a login?
- How often does content change, and is it the same for every user?
- How important is first-load speed on slow devices or networks (NFR)?
- Must it work offline?

## Options
| Option | What it is | Good for | Costs |
|---|---|---|---|
| **Client-side app / SPA (default for logged-in tools)** | Browser downloads the app, which fetches data via API | Dashboards, internal tools, apps behind login | Slower first load, poor SEO |
| Server-side rendering (SSR) | Server builds each page per request | Public, personalized or SEO-critical pages | Server cost, more complex deploys |
| Static generation (SSG) | Pages built ahead of time, served as files | Docs, marketing, content that rarely changes | Rebuild needed when content changes |
| Hybrid (per-page choice) | Mix of the above in one framework | Products with both public pages and an app | More concepts for the team to learn |
| Server-rendered pages, minimal JS | Classic multi-page app with small interactive parts | Forms-heavy, content-heavy, simple interactivity | Rich interactions are harder |
| Native / desktop app | Platform-specific app | Device features, offline-first, app-store presence | Separate codebases or cross-platform toolkit |

## Default
**Client-side app** for products behind login; **static** for content sites.

## Choose another option when
- **SSR** if an NFR requires SEO or fast first load for public, per-user pages.
- **Static** if content is the same for all users and changes less than daily.
- **Hybrid** if the product has both public pages (SEO) and a logged-in app.
- **Server pages, minimal JS** if the team is mostly backend developers and interactivity is light.
- **Native** if a requirement needs device features or offline use a browser cannot provide.

## Common mistakes
- Choosing SSR for an internal tool "for performance" without a measured need.
- Treating this as a framework decision; decide the strategy first, then the framework in the decision record.
