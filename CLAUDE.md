# CLAUDE.md — Project context for Claude

This repo is **static API documentation only** (Quarto, JS, Lua, Python helpers). No backend or API implementation here. Published at https://api.aiscr.cz/.

**Canonical agent governance:** [AGENTS.md](AGENTS.md) — scope, verification sources, branch rules, .agents usage.  
**Contributing:** [CONTRIBUTING.md](CONTRIBUTING.md) — branches, PRs, Quarto workflow, commit conventions.

---

## Commands

```bash
quarto preview          # Live preview of the doc site
quarto render           # Build site → _site/
quarto render --execute # Re-run computations and refresh _freeze/
```

**Requirements:** Quarto CLI ≥ 1.4; Node.js and Python ≥ 3.10 for scripts if needed.

---

## Architecture

| What | Where |
|------|--------|
| Source content | `.qmd` files; navigation and structure in `_quarto.yml` |
| Rendered site | `_site/` (generated; do not hand-edit) |
| Freeze / reproducibility | `_freeze/` (do not hand-edit; regenerate with `quarto render --execute`) |
| API doc sections | `auth-api/`, `file-api/`, `oai-pmh/`, `changelogs/`, `about/` |
| AI review artefacts | `.agents/` — prompts, config, analysis, reports (versioned) |

Documented APIs are implemented elsewhere: **Auth API** → aiscr-webamcr, **File API** and **OAI-PMH** → aiscr-digiarchiv-2. Always verify docs against live APIs or source repos (see AGENTS.md).

For key files, gotchas, verification URLs, and where to record issues, see [AGENTS.md](AGENTS.md).

---

## Automation

Shared automation (MCP, skills, hooks, subagents) is documented in [.agents/prompts/automation_recommendations.md](.agents/prompts/automation_recommendations.md). Canonical locations for shared rules: **AGENTS.md** and **.agents/** — not `.cursor/`, `.claude/`, or `.codex/`.
