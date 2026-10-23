# Menu: code organization (repository and folder structure)

Decides: how code is split across repositories, and how folders are organized inside each.
Cost to reverse: one-way for repository layout (moving history and CI is costly); two-way for folder conventions early on, one-way once the codebase is large.

Decide after system-shape, rendering and api-style; the structure follows the architecture, not the other way round.

The result replaces the `<code>/` placeholder in `docs/structure.yml` with the chosen top-level folders, each with a one-line description; then run `structure.py render` and `structure.py check` (see `project-flow`). From then on the check enforces the code folders too.

## Questions to answer first
- How many deployable parts (from system-shape) and how many teams?
- Do frontend and backend share code (types, API client, validation)?
- Must parts be released or versioned independently?
- What does the CI/build tooling handle well?

## Part 1: repositories

| Option | What it is | Good for | Costs |
|---|---|---|---|
| **Single repo, one app (default for a simple monolith)** | Everything in one project | One deployable, one team | Mixes concerns if it grows without rules |
| **Monorepo, several packages (default when frontend and backend are separate)** | One repo, folders per app and shared package | Shared types/contract, atomic changes across parts, small to mid teams | Needs workspace tooling; CI must build only what changed |
| Polyrepo | One repo per app or service | Independent teams and release cycles, different access rules | Cross-repo changes are slow; shared code needs versioned packages |

## Part 2: folders inside an app

| Option | What it is | Good for | Costs |
|---|---|---|---|
| **By feature/domain (default)** | `features/search/`, `features/report/`, each with its own UI, logic, data access and tests | Most products; matches how people talk about the app | Shared code needs a clear home |
| By technical layer | `components/`, `services/`, `models/`, `controllers/` | Very small apps, framework conventions that require it | One feature is spread over many folders |
| Layered by feature (Feature-Sliced style, hexagonal/clean) | Strict layers with import rules (domain does not import infrastructure) | Large codebases, complex domain logic, many contributors | More ceremony; overkill when small |

## Default
- **Repository:** single repo for one deployable; monorepo when there are separate frontend and backend apps (so the API contract and generated types live in one place).
- **Folders:** by feature, with one `shared/` area for code used by three or more features, and a small set of top-level folders.

## Reference skeleton (stack-neutral, monorepo)

```
<repo>/
  apps/
    web/                 frontend app
      src/
        features/<feature>/   UI, state, API calls, tests for one feature
        shared/               design-system components, utilities
        app/                  entry point, routing, providers
    api/                 backend app
      src/
        modules/<domain>/     handlers, domain logic, data access, tests
        shared/               cross-cutting: auth, errors, logging, config
        jobs/                 background work (if any)
  packages/
    contract/            API spec and generated types/clients (from design/api)
  infra/                 infrastructure as code, deploy config
  scripts/               developer and CI scripts
  docs/                  product, decisions, design, project docs (see design-doc skill); never deployed
  AGENTS.md              agent instructions (this workflow)
  README.md              how to run, test and deploy in under 5 minutes
```

Rename to the framework's conventions in the decision record (for example `app/` vs `pages/`); keep the principles.

## Rules to record in the decision record
- Where a new feature goes, and where shared code goes (and the "used by 3+ features" rule).
- Import rules: features don't import from each other's internals; shared code does not import features; backend modules talk only through their public interface.
- Test location: next to the code it tests, or a mirrored `tests/` tree. Pick one.
- Naming: file and folder case, one convention.
- Config and secrets: config in one place per app; secrets never in the repo.
- Enforce rules with tooling (lint rules for imports, CODEOWNERS per folder) rather than relying on memory.

## Choose another option when
- **Polyrepo** if teams must release independently and do not share code, or access must be separated by repository.
- **By technical layer** if the app is tiny (fewer than ~5 screens or endpoints) or the framework forces it.
- **Strict layering** if domain logic is large and complex, or many contributors keep breaking boundaries.

## Common mistakes
- A `utils/` or `common/` folder that becomes a dumping ground; shared code needs an owner.
- Copying a big company's structure before having its problems.
- Deciding folders before the system shape is known.
