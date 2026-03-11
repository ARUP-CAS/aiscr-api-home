# Documentation Hygiene Audit Report

**Repository:** ARUP-CAS/aiscr-api-home  
**Date:** 2026-03-11  
**Files audited:** 20  
**Fixes applied:** 2026-03-11 (see bottom)

## Summary

| Check | Status | Findings |
|-------|--------|----------|
| C1 File Discovery | OK | 20 instruction-bearing files found |
| C2 Audience Mapping | OK | 0 redundant files; clear audience split |
| C3 Duplication | OK | Contradiction fixed; redundancy reduced (CLAUDE, repo-rules) |
| C4 Drift | OK | CONTRIBUTING verification URLs fixed; soucasti.yml removed from cache |
| C5 Cross-References | OK | 0 broken refs; all targets and sections exist |
| C6 Token Efficiency | OK | CLAUDE.md and repo-rules shortened; cross-refs to AGENTS.md |
| C7 Governance | OK | "Dokumentace a vlastnictví pravidel" added to CONTRIBUTING.md |

---

## C1 — File Discovery

| File | Lines | Language | Apparent audience |
|------|-------|----------|-------------------|
| `README.md` | 115 | Czech | GitHub visitors, contributors |
| `README_en.md` | 124 | English | Same (EN variant) |
| `CONTRIBUTING.md` | 152 | Czech | Human contributors, AI agents |
| `AGENTS.md` | 341 | English | AI agents (all platforms) |
| `CLAUDE.md` | 58 | English | Claude (auto-injected) |
| `CODEOWNERS` | 30 | Mixed | GitHub PR reviewers |
| `.cursor/rules/repo-rules.mdc` | 32 | English | Cursor AI (local; gitignored) |
| `.cursor/rules/arena-model-sync.mdc` | 27 | English | Cursor AI (local; gitignored) |
| `.agents/README.md` | 22 | Czech | Contributors browsing .agents |
| `.agents/prompts/review_codebase.md` | 453 | English | AI agents (review sessions) |
| `.agents/prompts/automation_recommendations.md` | 56 | English | All AI tools / contributors |
| `.agents/prompts/audit_doc_hygiene.md` | 239 | English | AI agents (this audit) |
| `.agents/prompts/prompt_evolution/README.md` | 32 | Czech | Maintainers |
| `.agents/config/review_config.yaml` | 284 | YAML | AI agents, config tooling |
| `.agents/config/review_cache.json` | 39 | JSON | AI review state (machine) |
| `.agents/reports/bugs.md` | 41 | Markdown | AI agents, maintainers |
| `.agents/reports/refactoring_backlog.md` | 51 | Markdown | AI agents, maintainers |
| `.agents/reports/review_reports/README.md` | 42 | Czech | Maintainers (report naming) |

**Note:** `.cursor/` is in `.gitignore`; repo-rules and arena-model-sync exist on disk but are not versioned. No `CODEX.md`, `COPILOT.md`, `.cursorrules`, or `MEMORY.md` present. No `.github/PULL_REQUEST_TEMPLATE.md`. CODEOWNERS is at repo root (not `.github/CODEOWNERS`).

---

## C2 — Audience & Responsibility

- **README / README_en:** GitHub visitors; project overview, tech stack, repo structure, links. Distinct by language; no redundancy.
- **CONTRIBUTING.md:** Human contributors + agents; branch/PR/commit/Quarto rules, verification guidance. Single source for contribution workflow.
- **AGENTS.md:** All AI agents; governance, scope, verification sources, .agents layout, skills, branch rules. Canonical agent governance.
- **CLAUDE.md:** Claude-only; short context and pointers to AGENTS.md / CONTRIBUTING.md. Purpose: fast load, defer to canonicals.
- **CODEOWNERS:** GitHub; ownership and auto-reviewers. No overlap with other files.
- **.cursor/rules/*.mdc:** Cursor only (local); gotchas and model sync. Points to AGENTS.md / CONTRIBUTING.md; no full duplication of rules.
- **.agents/README.md:** Explains .agents layout; points to AGENTS.md. Clear.
- **.agents/prompts/review_codebase.md:** Review-session procedure and API verification. Unique.
- **.agents/prompts/automation_recommendations.md:** MCP, skills, hooks; shared list. Points to AGENTS.md for “Recommended skills”.
- **.agents/prompts/audit_doc_hygiene.md:** Portable audit prompt. Unique.
- **.agents/config/*:** Config and cache; no audience overlap with prose docs.
- **.agents/reports/*.md:** Bugs, backlog, report conventions. Clear responsibility.

**Result:** No two files share the same audience with the same responsibility. **OK.**

---

## C3 — Content Duplication Detection

### Topic matrix (abbreviated)

| Topic | README | README_en | CONTRIBUTING | AGENTS | CLAUDE | repo-rules | review_codebase | automation_recs |
|-------|--------|-----------|--------------|--------|--------|------------|-----------------|------------------|
| Branch naming / workflow | — | — | ✓ full | ✓ full | ref | ✓ brief | ref | ref |
| Do not edit _freeze/ _site/ | — | — | ✓ | ✓ | ✓ | ✓ | — | — |
| api.aiscr.cz = docs only | — | — | **wrong** | ✓ | ✓ | ✓ | ✓ | — |
| Tech stack (Quarto, etc.) | ✓ | ✓ | — | ✓ | — | ✓ | — | — |
| Verify against live/source | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| .agents layout / key files | — | — | — | ✓ | ✓ | — | — | — |

**Classification:**

1. **Acceptable:** README/README_en repeating tech stack and structure for visitors. CONTRIBUTING and AGENTS both describing branch workflow for different readers (human vs agent).
2. **Redundant:** “Do not modify _freeze/ _site/” appears in AGENTS.md, CLAUDE.md, and repo-rules.mdc. AGENTS is canonical; CLAUDE and repo-rules could shorten to a cross-reference to reduce tokens (C6).
3. **Contradictory (drift):** CONTRIBUTING.md says verify “vůči živému API na https://api.aiscr.cz/” (lines 73, 140). AGENTS.md (and others) state that api.aiscr.cz is **documentation only**; File API = digiarchiv.aiscr.cz, Auth API = amcr.aiscr.cz. Same topic, different (and misleading) guidance in CONTRIBUTING → **FAIL**.

---

## C4 — Drift Detection

### 1. CONTRIBUTING.md vs AGENTS.md (and verification sources)

- **CONTRIBUTING.md** (lines 73, 119–122): “Ověřte správnost dokumentovaných endpointů vůči živému API na https://api.aiscr.cz/” and “Živému API: https://api.aiscr.cz/” as first verification source.
- **AGENTS.md** (and review_codebase.md, CLAUDE.md): api.aiscr.cz is documentation site only; File API live = digiarchiv.aiscr.cz; Auth API live = amcr.aiscr.cz; “Never use api.aiscr.cz as base URL when verifying File API or Auth API endpoints.”

**Which is correct:** AGENTS.md and live_endpoints in review_config.yaml (and backend repos). CONTRIBUTING should list the same hierarchy: OAI-PMH at api.aiscr.cz/oai; File API at digiarchiv.aiscr.cz; Auth API at amcr.aiscr.cz; and optionally “documentation site” at api.aiscr.cz.

**Action:** Update CONTRIBUTING.md § “Přesnost dokumentace API” and the PR checklist to align with AGENTS.md verification sources (or cross-refer “viz AGENTS.md — Verification Sources”).

### 2. review_cache.json — reference to non-existent file

- **review_cache.json** (`content_checksums`): includes `"soucasti.yml": null`. There is no `soucasti.yml` in the repository (search returns 0 files).
- **Likely:** Placeholder or leftover from another project. Creates false expectation of a tracked file.

**Which is correct:** Repo has no soucasti.yml. Either remove the key from content_checksums or add a note that it’s reserved/unused.

**Action:** Remove `soucasti.yml` from `content_checksums` in review_cache.json, or document it as “reserved” in a comment/note in the same file or in review_config.yaml.

---

## C5 — Cross-Reference Integrity

Checked:

- CONTRIBUTING.md → CONTRIBUTING.md (self), review_codebase.md, AGENTS.md. Files and sections exist.
- CLAUDE.md → AGENTS.md, CONTRIBUTING.md, automation_recommendations.md, bugs.md, refactoring_backlog.md, repository_map.json, review_cache.json, review_codebase.md. All exist.
- AGENTS.md → review_codebase.md, automation_recommendations.md, CONTRIBUTING.md, Verification Sources, Recommended skills, .agents structure. All exist; “Recommended skills” is present.
- automation_recommendations.md → AGENTS.md (“Recommended skills”), review_codebase.md, CONTRIBUTING.md. All exist.
- .agents/README.md → AGENTS.md. Exists.
- review_reports/README.md → bugs.md, refactoring_backlog.md. Exist.
- prompt_evolution/README.md → review_codebase.md. Exists.

No broken or stale cross-references. **OK.**

---

## C6 — Token Efficiency (AI-specific)

Files typically auto-injected or frequently loaded for AI: **CLAUDE.md**, **AGENTS.md**, **.cursor/rules (repo-rules.mdc, arena-model-sync.mdc)**.

- **CLAUDE.md (58 lines):** “Key files” and “Gotchas” repeat information that is already in AGENTS.md (e.g. do not edit _freeze/_site, where to record issues, api.aiscr.cz vs digiarchiv/amcr). Replacing 4–6 lines with “See AGENTS.md for scope, verification URLs, and gotchas” would save roughly **150–250 tokens** per session while preserving pointers.
- **repo-rules.mdc (32 lines):** “Do not modify _freeze/ _site/”, “static API documentation only”, branch workflow — all stated in AGENTS.md/CONTRIBUTING. Keeping one-line pointers and dropping the repeated sentences would save roughly **100–150 tokens**.
- **AGENTS.md:** Long but authoritative; trimming would require moving sections to on-demand files (e.g. verification URLs to review_config or review_codebase). Not recommended without a larger restructure.

**Estimated token savings:** ~250–400 from CLAUDE.md + repo-rules by replacing repeated gotchas with cross-references. Optional further saving (~100–200) if CLAUDE “Key files” is shortened to a single pointer to AGENTS.md § Key files / .agents structure.

**Result:** WARN — meaningful redundancy in auto-injected files; no critical bloat.

---

## C7 — Governance Rules Presence

- **AGENTS.md:** “Resolving Inconsistencies” defines that AGENTS.md, CONTRIBUTING.md, and repository standards are source of truth; .agents/ must align. Implicit doc governance.
- **.cursor/rules/repo-rules.mdc:** “Canonical sources of truth” and “Do not duplicate rules here—keep details in the canonical documents.” Explicit pointer to AGENTS, CONTRIBUTING, README, .agents.
- **CONTRIBUTING.md:** No dedicated “Documentation governance” or “Which file owns which information” section. Branch/content ownership is spread across CONTRIBUTING and AGENTS.

**Result:** Governance is present but scattered. **WARN** — suggest adding a short “Documentation governance” subsection to CONTRIBUTING (or AGENTS) stating: (1) AGENTS.md owns agent rules and verification; (2) CONTRIBUTING.md owns contribution workflow and branch/PR/Quarto; (3) no duplication of those rules elsewhere except brief pointers.

---

## Recommended Fixes

### Critical (FAIL)

1. **CONTRIBUTING.md verification URLs** — **File:** `CONTRIBUTING.md`  
   **Action:** In the section “Přesnost dokumentace API” and in the PR checklist (step 5), replace “živému API na https://api.aiscr.cz/” with the correct hierarchy: OAI-PMH at api.aiscr.cz (or api.aiscr.cz/oai), File API at https://digiarchiv.aiscr.cz/, Auth API at https://amcr.aiscr.cz/. Add a note that api.aiscr.cz is the documentation site; live API bases are digiarchiv and amcr. Optionally add: “Viz AGENTS.md — Verification Sources.”

2. **review_cache.json content_checksums** — **File:** `.agents/config/review_cache.json`  
   **Action:** Remove the `soucasti.yml` key from `content_checksums`, or add a short note in the existing `"note"` field that `soucasti.yml` is reserved/unused (if you intend to keep it for future use).

### Important (WARN)

1. **CLAUDE.md redundancy** — **File:** `CLAUDE.md`  
   **Action:** Replace the “Gotchas” bullet list (and optionally “Key files”) with one line: “See AGENTS.md for gotchas, key paths, and verification URLs.” Keep the Commands and Architecture table if useful for quick context.

2. **repo-rules.mdc redundancy** — **File:** `.cursor/rules/repo-rules.mdc` (if/when versioned)  
   **Action:** Keep “Canonical sources of truth” and “Branch workflow (brief)”; shorten “Repo-specific gotchas” to 1–2 lines that point to AGENTS.md for “do not edit _freeze/_site” and static-docs clarification.

3. **Documentation governance** — **File:** `CONTRIBUTING.md` or `AGENTS.md`  
   **Action:** Add a short “Documentation governance” or “Which file owns what” subsection stating that AGENTS.md owns agent rules and verification, CONTRIBUTING.md owns contribution workflow, and other docs should only reference (not duplicate) these.

### Optional improvements

1. Add a one-line mention in CONTRIBUTING (or README) that CODEOWNERS is at repo root (for discoverability).
2. If .cursor/rules are ever committed, add a one-line note in README or CONTRIBUTING that Cursor-specific rules live in `.cursor/rules/` and point to AGENTS.md/CONTRIBUTING.md.
3. In automation_recommendations.md, add a reference to `.agents/prompts/audit_doc_hygiene.md` under “Prompts” or “References” so agents can discover the hygiene audit.

---
## Fixes applied (2026-03-11)

| Recommendation | Action taken |
|----------------|--------------|
| **Critical 1** — CONTRIBUTING verification URLs | Updated PR step 5 and section "Přesnost dokumentace API" with correct hierarchy (OAI-PMH at api.aiscr.cz/oai, File API at digiarchiv.aiscr.cz, Auth API at amcr.aiscr.cz); added "Viz AGENTS.md — Verification Sources". |
| **Critical 2** — review_cache.json | Removed soucasti.yml from content_checksums. |
| **Important 1** — CLAUDE.md redundancy | Replaced "Key files" and "Gotchas" sections with one line pointing to AGENTS.md. |
| **Important 2** — repo-rules.mdc | Shortened "Repo-specific gotchas" to one line pointing to AGENTS.md. |
| **Important 3** — Documentation governance | Added section "Dokumentace a vlastnictví pravidel" to CONTRIBUTING.md. |
| **Optional 1** — CODEOWNERS location | Clarified in PR step 7: "viz soubor CODEOWNERS v kořeni repozitáře". |
| **Optional 3** — audit_doc_hygiene | Added reference in automation_recommendations.md References. |
