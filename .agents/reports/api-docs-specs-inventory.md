# API docs and specs inventory — aiscr-api-home

Generated as part of API governance and documentation alignment (api-governance-doc-alignment plan).

## 1. Inventory (Step 1)

### OpenAPI / REST spec files

- **None.** This repository does not contain `openapi.yaml`, `openapi.json`, or other OpenAPI/REST spec files.
- API behaviour is documented in Quarto (`.qmd`) and in the agent-facing config below.

### API documentation (user-facing)

| Location | Content |
|----------|---------|
| `oai-pmh/index.qmd`, `oai-pmh/v2.0.qmd` | OAI-PMH API: endpoints, verbs, versioned URLs, schema links, curl examples |
| `file-api/index.qmd` | File API: base URL, URL pattern from OAI-PMH response, schema explanation, examples |
| `auth-api/index.qmd` | Auth API: token endpoint, userinfo endpoint, request/response, examples (Python, curl) |
| `changelogs/*.qmd` | Version and endpoint changes over time |
| `index.qmd` | Overview and links to the three APIs |

Navigation and structure: `_quarto.yml` (website sidebar, navbar).

### Governance and API-related sections

| File | API-related content |
|------|----------------------|
| `README.md` | Overview of Auth API, File API, OAI-PMH; link to api.aiscr.cz |
| `AGENTS.md` | Verification Sources (Live APIs table), “Never use api.aiscr.cz for File/Auth”, source repos, review instructions |
| `CLAUDE.md` | Short pointer: docs only; Auth → webamcr, File/OAI-PMH → digiarchiv-2; verify via AGENTS.md |
| `CONTRIBUTING.md` | PR step 5: verify endpoints vs live APIs (OAI-PMH, File, Auth with correct base URLs); section “Přesnost dokumentace API” with same hierarchy |

### .agents/ config and prompts mentioning endpoints

| File | Role |
|------|------|
| `.agents/config/review_config.yaml` | **Canonical for agents:** `live_endpoints` — OAI-PMH, file_api, auth_api with `live_base_url`, `url`, `curl`, expected checks. Single source of truth for verification. |
| `.agents/prompts/review_codebase.md` | Full review procedure; curl examples; “Never use api.aiscr.cz as base URL when verifying File API or Auth API”; references review_config.yaml. |
| `.agents/analysis/repository_map.json` | High-level map: auth endpoints, file_api base, OAI-PMH description and endpoints. |
| `.agents/reports/automation_recommendations.md` | Mentions OpenAPI/Context7 for live docs. |
| `.agents/reports/review_reports/*.md` | Audit outputs referencing endpoints and config. |

---

## 2. Sources of truth (Step 2)

| Concern | Canonical location | Others |
|--------|--------------------|--------|
| **Endpoint definitions (user-facing)** | Quarto: `oai-pmh/index.qmd`, `file-api/index.qmd`, `auth-api/index.qmd` | README, index.qmd summarize; no duplication of path/parameter tables elsewhere. |
| **Live URLs and curl (agents/verification)** | `.agents/config/review_config.yaml` → `live_endpoints` | review_codebase.md, repository_map.json reference or duplicate for procedure; must stay in sync with review_config.yaml. |
| **Deprecation / versioning** | Changelogs in `changelogs/`; versioned OAI-PMH endpoints and schema links in `oai-pmh/index.qmd` | review_config.yaml `current_endpoint` / `previous_endpoint`. |
| **Base URL and “docs vs live”** | AGENTS.md “Verification Sources” and note that api.aiscr.cz is documentation only | CONTRIBUTING.md “Přesnost dokumentace API” and PR checklist; CLAUDE.md short pointer. |

Rule: Documentation site = user-facing; agent-facing canonical for live verification = `review_config.yaml`. All other mentions should defer via links or short summaries; no duplicate endpoint tables outside the canonical Quarto sections.

---

## 3. Alignment and validation

- CONTRIBUTING.md already states the correct hierarchy (OAI-PMH at api.aiscr.cz/oai; File at digiarchiv; Auth at amcr) and that api.aiscr.cz is documentation only.
- AGENTS.md and review_config.yaml are aligned (same base URLs and roles).
- AI-generated API doc rules added to AGENTS.md (see below); no OpenAPI spec to validate — validation is manual/curl and source-code checks per AGENTS.md and review_codebase.md.
