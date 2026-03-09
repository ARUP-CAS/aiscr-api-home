# Prompt Evolution

Tato složka eviduje historii vývoje promptů používaných pro AI review sessions repozitáře `aiscr-api-home`.

## Účel

Sledování verzí promptů umožňuje:

- Reprodukovat výsledky starších sessions
- Iterativně zlepšovat kvalitu review (zejména ověřování přesnosti API dokumentace)
- Dokumentovat, co fungovalo a co ne

## Konvence pojmenování

```markdown
YYYY-MM-DD-v<verze>-<popis>.md
```

Příklady:

```markdown
2026-03-07-v1.0-initial-bootstrap.md
2026-04-15-v1.1-improved-endpoint-verification.md
```

## Aktuální prompt

Vždy v: `.agents/prompts/review_codebase.md`

## Historie verzí

| Verze | Datum | Shrnutí |
|-------|-------|---------|
| v1.0 | 2026-03-07 | Úvodní bootstrap — review prompt s ověřováním živých endpointů přes curl |
