# AGENTS.md — Instructions for AI Agents

This file defines the rules, scope and workflows for AI agents (Claude Code, GitHub Copilot, Cursor, etc.) working in this repository.

Rules in this file apply to the entire repository.
A nested `AGENTS.md` in a subdirectory takes precedence for that subtree.

---

## Repository Overview

Repository: `ARUP-CAS/aiscr-api-home`  
Type: Static API documentation site (Quarto / JS / Lua / Python)  
Published at: https://api.aiscr.cz/  
Version: v1.1.1 (December 2025)  
Licence: CC BY-NC 4.0 (content)

This repository contains documentation for the AMČR API, part of AIS CR.

It is a **static documentation project**.
The repository **does not contain the API implementation itself**, only its documentation.

Documented interfaces include:

- OAI-PMH API
- File API
- Authentication API

---

## Repository Orientation (Mandatory First Step)

Before starting any work, agents must gather repository context.

Agents must read the following files first:

- `.agents/analysis/repository_map.json`
- `.agents/config/review_cache.json`
- `.agents/reports/bugs.md`
- `.agents/reports/refactoring_backlog.md`
- `.agents/prompts/review_codebase.md`

Purpose:

These files contain accumulated knowledge from previous review sessions.
Reading them prevents duplicated work and ensures continuity between agent runs.

### Resolving Inconsistencies

If content in `.agents/` contradicts high-level repository rules or governance
defined in this document (`AGENTS.md`), `CONTRIBUTING.md`, or other authoritative
project documentation, agents must treat those higher-level documents as the
**source of truth**.

In such cases agents should:

1. Prefer the high-level governance rules defined in:
   - `AGENTS.md`
   - `CONTRIBUTING.md`
   - repository coding standards
2. Adapt or update affected files in `.agents/` to align with those rules.
3. Record the adjustment in the review history (for example `review_cache.json`
   or `refactoring_backlog.md`) when relevant.

This ensures long-running AI review artefacts remain consistent with
current repository governance.

---

## AI-Generated Content

All AI-generated artefacts must be stored inside:

```markdown
.agents/
```

Typical artefacts include:

- audit reports
- analysis JSON files
- CI diagnostics
- prompt evolution notes
- review session summaries

Agent branches must follow the naming convention:

```markdown
agents/<agent_name>/<topic>
```

Examples:

```markdown
agents/claude/api-verification
agents/copilot/doc-fixes
```

Agent branches must **never push directly to protected branches**.

---

## Goal

Maintain and improve the repository through **small, safe, reviewable changes** aligned with:

- repository conventions
- `CONTRIBUTING.md`
- Quarto documentation structure
- existing AIS CR documentation standards

Agents must avoid large unrelated refactors.

---

## Agent Behaviour

Agents must follow these behavioural rules:

1. Always gather repository context first.
2. Avoid repeating work already recorded in `.agents/`.
3. Prefer small incremental improvements.
4. Record discovered issues in:
   - `.agents/reports/bugs.md`
   - `.agents/reports/refactoring_backlog.md`
5. Suggest improvements to this file if agent workflows evolve.

### Recommended Skills

The following specialised agent skills may be useful when working in this repository.

These skills are optional helpers and not mandatory tools.

#### Documentation (Quarto)

When editing Quarto content (`.qmd` files, `_quarto.yml`, API descriptions, or code examples): follow CONTRIBUTING.md, verify against live APIs and source code (see [Verification Sources](#verification-sources)), and use the procedure in [.agents/prompts/review_codebase.md](.agents/prompts/review_codebase.md) for full review sessions. No external skill required — this is the primary documentation workflow for the repo.

#### gh-fix-ci

Use when a user asks to **debug or fix failing GitHub PR checks** (GitHub Actions). The skill uses `gh` to inspect checks and logs, summarize failures, and propose a fix after approval. Relevant for:

- GitHub Actions workflows
- Quarto build and deploy pipelines
- Documentation deployment failures

Requires `gh` CLI and authentication with repo/workflow scopes.

#### gh-address-comments

Use when addressing **review or issue comments on the open PR for the current branch**. The skill uses `gh` to fetch comments and review threads, then apply fixes for comments the user selects. Ensures changes stay consistent with repository conventions. Requires `gh` CLI and authentication.

### Automation and shared rules

Shared automation recommendations (MCP servers, skills, hooks, subagents) are versioned in this repository so all tools (Cursor, Claude Code, Copilot, etc.) and contributors use one source of truth.

- **Canonical locations:** `AGENTS.md` and `.agents/` — **not** `.cursor/`, `.claude/`, or `.codex/` (those directories are gitignored and not shared).
- **Full list:** [`.agents/reports/automation_recommendations.md`](.agents/reports/automation_recommendations.md) — recommended MCP servers, skills, hooks, and subagents; implement in your local editor config as needed.

---

This repository documents **live APIs used by external developers**.

Documentation must always be verified against authoritative sources.

Priority hierarchy:

1. live systems / APIs
2. source code repositories
3. technical documentation
4. repository documentation

Incorrect documentation may break third-party integrations and must be avoided.

---

## Verification Sources

### Live APIs

| Source | URL | Purpose |
| --- | --- | --- |
| OAI-PMH API | https://api.aiscr.cz/oai?verb=Identify | Smoke-test API |
| OAI-PMH versioned | https://api.aiscr.cz/2.2/oai?verb=Identify | Version verification |
| OAI-PMH schema v2.2 | https://api.aiscr.cz/schema/amcr/2.2/ | XML schema |
| OAI-PMH schema v2.1 | https://api.aiscr.cz/schema/amcr/2.1/ | Previous schema |
| File API (live) | https://digiarchiv.aiscr.cz/ | File download endpoints (served by digiarchiv-2) |
| Auth API (live) | https://amcr.aiscr.cz/ | Authentication endpoints (served by webamcr) |
| AMCR info site | https://amcr-info.aiscr.cz/ | Terminology |
| AIS CR main site | https://www.aiscr.cz/ | System context |
| Digital Archive | https://digiarchiv.aiscr.cz/ | File API context |

> **Important:** `https://api.aiscr.cz/` is the **documentation site** only.
> The actual live File API runs at `https://digiarchiv.aiscr.cz/`.
> The actual live Auth API runs at `https://amcr.aiscr.cz/`.
> Never use `api.aiscr.cz` as the base URL when verifying File API or Auth API endpoints.

---

### Source Code Repositories

| Repository | URL |
| --- | --- |
| aiscr-webamcr | https://github.com/ARUP-CAS/aiscr-webamcr |
| aiscr-digiarchiv-2 | https://github.com/ARUP-CAS/aiscr-digiarchiv-2 |
| aiscr-webamcr-help | https://github.com/ARUP-CAS/aiscr-webamcr-help |
| aiscr-amcr-home | https://github.com/ARUP-CAS/aiscr-amcr-home |
| aiscr-home | https://github.com/ARUP-CAS/aiscr-home |

Source code is authoritative for:

- endpoint paths
- parameters
- response schemas
- HTTP status codes

---

### Technical Documentation

| Source | URL |
| --- | --- |
| AMČR technical docs | https://aiscr-webamcr.readthedocs.io/ |

This documentation is authoritative for:

- architecture
- system behaviour
- data model

---

## Specific Review Instructions

When reviewing or modifying API documentation, agents must:

1. Verify endpoints against the live API.
2. Verify parameter names and schemas against source code.
3. Execute example `curl` commands from documentation.
4. Record discrepancies in `.agents/reports/bugs.md`.
5. Verify OAI-PMH conformance with the official specification:

https://www.openarchives.org/OAI/openarchivesprotocol.html

---

For detailed verification procedures, curl commands and expected responses
for all three APIs, see [`.agents/prompts/review_codebase.md`](.agents/prompts/review_codebase.md).

---

## AI-generated API documentation

When generating or updating API documentation (including examples, endpoint descriptions, or parameter tables), agents must follow these rules:

1. **Read canonical sources first.** User-facing endpoint definitions live in the Quarto API sections (`oai-pmh/`, `file-api/`, `auth-api/`). Live URLs and verification curl commands are canonical in [`.agents/config/review_config.yaml`](.agents/config/review_config.yaml) under `live_endpoints`. Use these as the single source of truth; do not rely on ad-hoc or out-of-date copies elsewhere.
2. **Do not invent endpoints or parameters.** Only document endpoints, parameters, and response shapes that appear in the canonical Quarto docs or in the live API (verified via `review_config.yaml` curl commands or source code). If in doubt, verify against the live system or the backend repos (see [Verification Sources](#verification-sources)).
3. **Match authentication and base URLs in examples.** Generated examples (e.g. curl, Python) must use the same base URLs and auth method as in the canonical source: OAI-PMH at `https://api.aiscr.cz/` (or versioned `/2.2/oai`); File API at `https://digiarchiv.aiscr.cz/`; Auth API at `https://amcr.aiscr.cz/`. Never use `api.aiscr.cz` as the base URL for File API or Auth API requests.

An inventory and mapping of canonical sources is maintained in [`.agents/reports/api-docs-specs-inventory.md`](.agents/reports/api-docs-specs-inventory.md).

---

## Scope

### In Scope

Agents may modify:

- `.qmd` documentation files
- `_quarto.yml`
- CSS/SCSS themes
- Lua filters
- Python scripts
- JavaScript helper scripts
- GitHub workflows

### Out of Scope

Generated artefacts must not be modified.

Examples:

```markdown
_freeze/
_site/
```

Binary assets:

```markdown
figs/
fonts/
```

---

## Tech Stack

Detected technologies in this repository:

- Quarto documentation framework
- JavaScript
- Lua filters
- Python helper scripts
- SCSS/CSS styling
- GitHub Actions CI
- GitHub Pages hosting

The repository does **not** contain:

- backend services
- databases
- API implementations
- container infrastructure

---

## Branch and PR Rules

Repository workflow:

All development targets the `main` branch.

Rules:

- Never push directly to `main`
- Always open a Pull Request
- Changes must pass CI before merge

Branch naming convention:

```markdown
agents/<agent>/<topic>
docs/<topic>
fix/<topic>
chore/<topic>
```

Examples:

```markdown
agents/claude/api-validation
docs/update-oai-examples
fix/broken-endpoint-link
```

Changes to `.agents/` require **human review before merge**.

---

## Repository Context

This repository is part of the AIS CR ecosystem.

Related repositories:

| Repository | Description |
| --- | --- |
| aiscr-webamcr | AMČR application (Auth API implementation) |
| aiscr-digiarchiv-2 | Digital Archive (File API + OAI-PMH) |
| aiscr-api-home | API documentation |
| aiscr-webamcr-help | User documentation |
| aiscr-home | AIS CR main site |
