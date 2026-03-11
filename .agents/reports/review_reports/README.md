# Review Reports

Tato složka obsahuje výsledky AI review sessions repozitáře `aiscr-api-home`.

## Konvence pojmenování

```markdown
YYYY-MM-DD-<tema>.md
```

Příklady:

```markdown
2026-03-07-bootstrap.md
2026-03-20-oai-pmh-accuracy.md
2026-04-05-auth-api-review.md
2026-04-15-changelog-review.md
```

## Typy sessions

| Typ | Popis |
| ----- | ------- |
| `bootstrap` | Úvodní bootstrap session |
| `general-review` | Celý repozitář — struktura, obsah, navigace |
| `oai-pmh-accuracy` | OAI-PMH verbs, sety a schémata vs. živé API a zdrojový kód |
| `auth-api-accuracy` | Auth API endpointy vs. zdrojový kód aiscr-webamcr |
| `file-api-accuracy` | File API endpointy vs. zdrojový kód aiscr-digiarchiv-2 |
| `changelog-review` | Úplnost changelogů vs. GitHub releases |
| `linkcheck` | Rozbité interní a externí odkazy |
| `cicd-review` | GitHub Actions workflows |

## Struktura reportu

Každý report musí obsahovat:

1. **Metadata** — datum, typ session, agent, větev
2. **Výsledky Step 0** — výstup všech ověřovacích curl příkazů
3. **Rozsah** — co bylo reviewováno
4. **Použité zdroje** — ověřené verze live API, commity backendů
5. **Zjištění** — co bylo nalezeno
6. **Nové bugy** — přidané do `bugs.md` (s ID)
7. **Nové backlog položky** — přidané do `refactoring_backlog.md` (s ID)
8. **Opraveno v session** — položky vyřešené během session
