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

- `docs_agents/repository_map.json`
- `docs_agents/review_cache.json`
- `docs_agents/bugs.md`
- `docs_agents/refactoring_backlog.md`
- `docs_agents/PROMPT.md`

Purpose:

These files contain accumulated knowledge from previous review sessions.
Reading them prevents duplicated work and ensures continuity between agent runs.

If information inside `docs_agents` contradicts governance rules defined in:

- `AGENTS.md`
- `CONTRIBUTING.md`
- repository conventions

those higher-level rules must be treated as authoritative.

Agents should update the affected `docs_agents` files to restore consistency.

---

## AI-Generated Content

All AI-generated artefacts must be stored inside:

```markdown
docs_agents/
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
2. Avoid repeating work already recorded in `docs_agents/`.
3. Prefer small incremental improvements.
4. Record discovered issues in:
   - `docs_agents/bugs.md`
   - `docs_agents/refactoring_backlog.md`
5. Suggest improvements to this file if agent workflows evolve.

---

## Recommended Skills

The following specialised agent skills may be useful when working in this repository.

These skills are optional helpers and not mandatory tools.

### doc

Reviewing and editing documentation artefacts, including:

- Quarto `.qmd` files
- navigation structure
- API descriptions
- examples and code snippets

### gh-fix-ci

Diagnosing and fixing CI failures in:

- GitHub Actions workflows
- Quarto build pipelines
- documentation deployment processes

### gh-address-comments

Incorporating Pull Request review comments and ensuring proposed changes remain consistent with repository conventions.

---

## Critical Requirement: Verify Documentation Against Real Systems

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
4. Record discrepancies in `docs_agents/bugs.md`.
5. Verify OAI-PMH conformance with the official specification:

https://www.openarchives.org/OAI/openarchivesprotocol.html

---

## Endpoint Verification Procedures

Agents should run the following checks when reviewing API documentation.

All discrepancies must be recorded in:

```markdown
docs_agents/bugs.md
```

### OAI-PMH API Verification

Smoke test:

```bash
curl -s 'https://api.aiscr.cz/oai?verb=Identify'
curl -s 'https://api.aiscr.cz/2.2/oai?verb=Identify'
```

Expected:

- HTTP 200
- valid OAI-PMH XML
- `<protocolVersion>2.0</protocolVersion>`

Metadata formats:

```bash
curl -s 'https://api.aiscr.cz/2.2/oai?verb=ListMetadataFormats'
```

Expected prefixes:

```plain
oai_dc
oai_amcr
```

Available sets:

```bash
curl -s 'https://api.aiscr.cz/2.2/oai?verb=ListSets'
```

Verify that all sets documented in `oai-pmh/` exist.

ListRecords:

```bash
curl -s 'https://api.aiscr.cz/2.2/oai?verb=ListRecords&metadataPrefix=oai_dc&set=projekt'
```

Expected:

- valid XML
- `<ListRecords>`
- `<record>`
- `<resumptionToken>`

GetRecord example:

```bash
curl -s 'https://api.aiscr.cz/2.2/oai?verb=GetRecord&identifier=https://api.aiscr.cz/id/M-FT-110598700&metadataPrefix=oai_amcr'
```

Verify XML structure.

Schema availability:

```bash
curl -s -o /dev/null -w "%{http_code}" https://api.aiscr.cz/schema/amcr/2.2/amcr.xsd
```

Expected:

```plain
200
```

---

## File API Verification

The File API is **not** served from `api.aiscr.cz`.

Architecture:

- **Documentation** for File API: `https://api.aiscr.cz/file-api/`
- **Live API** serving files and thumbnails: `https://digiarchiv.aiscr.cz/id/`
- **Backend repository**: `aiscr-digiarchiv-2` (Java / Spring)
- **Authentication**: HTTP Basic Auth only — bearer token from Auth API is **not** (yet) supported

File URLs are obtained from the `<amcr:url>` element inside `<amcr:soubor>` in OAI-PMH responses.
The URL format is: `https://digiarchiv.aiscr.cz/id/{ident_cely}/file/{file_id}` (file_id is a UUID).

**Step 1 — Reachability check:**

```bash
curl -s -o /dev/null -w "%{http_code}" 'https://digiarchiv.aiscr.cz/'
```

Expected: HTTP 200.

**Step 2 — Verify known public endpoints:**

Small thumbnail (publicly accessible for role-A files):

```bash
curl -s -o /dev/null -w "%{http_code}" \
"https://digiarchiv.aiscr.cz/id/M-202301215-N00001/file/aa0cdd95-4bc4-4358-a831-2cf8672a3e4b/thumb"
```

Expected: `200`

Large thumbnail (page 2 of a document, auth required for restricted files):

```bash
curl -s -o /dev/null -w "%{http_code}" \
"https://digiarchiv.aiscr.cz/id/C-TX-198603094/file/3e28c562-17f6-48dc-b8f5-787d14fb55af/thumb/page/2"
```

Original file:

```bash
curl -s -o /dev/null -w "%{http_code}" \
"https://digiarchiv.aiscr.cz/id/M-202301215-N00001/file/aa0cdd95-4bc4-4358-a831-2cf8672a3e4b"
```

Expected status codes: `200` (accessible), `401` (auth required), `403` (insufficient permissions), `404` (invalid ID), `429` (rate limit — use ≥1 s between requests).

**Step 3 — Verify against source code:**

Inspect Spring controller routes in `web/src/main/java/` in the `aiscr-digiarchiv-2` repository.
Verify that documented endpoint patterns match actual controller mappings.

**Step 4 — Compare documentation:**

Check that endpoint paths, parameters and example URLs in `file-api/` match
what the live `digiarchiv.aiscr.cz` application actually serves.

Record any discrepancy in `docs_agents/bugs.md`.

---

## Auth API Verification

The Auth API is **not** served from `api.aiscr.cz`.

Architecture:

- **Documentation** for Auth API: `https://api.aiscr.cz/auth-api/`
- **Live API**: `https://amcr.aiscr.cz/`
- **Backend repository**: `aiscr-webamcr` (Django REST Framework / Python)

> **Important:** The bearer token from Auth API is used **only** for `uzivatel-info`.
> OAI-PMH API and File API use HTTP Basic Authentication directly.

**Step 1 — Reachability check:**

```bash
curl -s -o /dev/null -w "%{http_code}" 'https://amcr.aiscr.cz/'
```

Expected: HTTP 200.

**Step 2 — Verify token endpoint:**

```bash
curl -s -o /dev/null -w "%{http_code}" -X POST \
-H "Content-Type: application/json" \
-d '{"username":"invalid","password":"invalid"}' \
'https://amcr.aiscr.cz/api/token-auth/'
```

Expected: `400` (invalid credentials format) or `403` (wrong credentials).

**Step 3 — Verify unauthenticated access to protected endpoint:**

```bash
curl -s -o /dev/null -w "%{http_code}" 'https://amcr.aiscr.cz/api/uzivatel-info/'
```

Expected: `401`

**Step 4 — Verify against source code:**

Inspect:

```markdown
webclient/urls.py
webclient/*/urls.py
webclient/*/views.py
webclient/*/serializers.py
```

Verify endpoint paths and schemas match documentation in `auth-api/`.

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

Changes to `docs_agents/` require **human review before merge**.

---

## docs_agents Structure

The `docs_agents` directory stores persistent AI review artefacts.

```markdown
docs_agents/
├── PROMPT.md
├── PROMPT_RUN.md
├── review_config.yaml
├── repository_map.json
├── dependency_graph.json
├── review_cache.json
├── bugs.md
├── refactoring_backlog.md
├── review_reports/
├── prompt_evolution/
├── cicd_analysis.json
└── frontend_analysis.json
```

Purpose of individual files:

- `PROMPT.md` — instructions for long-running AI review sessions
- `PROMPT_RUN.md` — how to execute a review session
- `review_config.yaml` — enabled review modules
- `repository_map.json` — high-level repository structure
- `dependency_graph.json` — dependencies and technologies
- `review_cache.json` — persistent review session state
- `bugs.md` — structured list of discovered issues
- `refactoring_backlog.md` — long-term improvement backlog
- `review_reports/` — generated technical audit reports
- `prompt_evolution/` — prompt development history
- `cicd_analysis.json` — CI/CD diagnostics
- `frontend_analysis.json` — documentation frontend analysis

Additional analysis artefacts may be generated during review sessions.

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
