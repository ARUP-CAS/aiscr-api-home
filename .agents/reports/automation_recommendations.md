# Automation recommendations — shared rules (AGENTS.md / .agents/)

This file lists recommended automations for AI-assisted work in this repository.
**Canonical shared rules live in AGENTS.md and .agents/** — not in `.cursor/`, `.claude/`, or `.codex/` (gitignored).

Implement these in your local editor or CLI config as needed.

---

## MCP servers

| Server | Why | Install (local) |
|--------|-----|-----------------|
| **context7** | Live docs for Quarto, OpenAPI, OAI-PMH, JS/Lua. Fits API-docs and verification workflow. | `claude mcp add context7` or your editor's MCP setup |
| **GitHub** | PRs target `main`, CI in GitHub Actions; aligns with gh-fix-ci, gh-address-comments. | Add via your editor's MCP / plugin-github-github |

---

## Skills

Canonical list and when to use: [AGENTS.md](../../AGENTS.md) — "Recommended skills".

| Skill / workflow | When to use |
|------------------|--------------|
| **Documentation (Quarto)** | Editing `.qmd`, `_quarto.yml`, API text, or examples: follow CONTRIBUTING.md, verify against live APIs, use [review_codebase.md](../prompts/review_codebase.md) for full reviews. No external skill. |
| **gh-fix-ci** | User asks to fix failing GitHub PR checks (GitHub Actions); uses `gh` to inspect logs and propose fixes. |
| **gh-address-comments** | Address review comments on the open PR for the current branch; uses `gh` to fetch and apply selected comments. |

**Custom procedure (no separate skill path):** "API doc verify" — run verification steps from [review_codebase.md](../prompts/review_codebase.md) and AGENTS.md when changing endpoint docs.

---

## Hooks (document desired behaviour; implement locally)

| Hook | Purpose | Shared rule |
|------|---------|-------------|
| **PostToolUse** | After editing `.qmd` or `_quarto.yml`, run `quarto render` (or equivalent) so breakages are caught. | Document in repo; add hook in your local Cursor/Claude config if supported. |
| **PreToolUse** | Block edits to `_freeze/`, `_site/`, and lockfiles (AGENTS.md "Out of scope"). | Prefer a hook that blocks these paths in your local setup. |

---

## Subagents (document recommended use; config local)

| Subagent | Why | Shared rule |
|----------|-----|-------------|
| **doc-reviewer** | Many `.qmd` files and strict "verify against live API"; dedicated pass for docs and examples. | Use procedure in [review_codebase.md](../prompts/review_codebase.md) or a doc-reviewer subagent if your tool supports it. |
| **security-reviewer** (optional) | Auth API and token handling; check docs don't suggest unsafe usage. | One-line mention; implement locally if desired. |

---

## References

- [AGENTS.md](../../AGENTS.md) — governance, scope, verification, skills
- [review_codebase.md](../prompts/review_codebase.md) — review session procedure and API verification
- [audit_doc_hygiene.md](../prompts/audit_doc_hygiene.md) — documentation hygiene audit prompt (run via "Read .agents/prompts/audit_doc_hygiene.md and run the audit")
- [CONTRIBUTING.md](../../CONTRIBUTING.md) — branches, Quarto, PR process
