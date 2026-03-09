# Přispívání do repozitáře

Děkujeme za zájem o přispění do dokumentace AMČR API.  
Níže jsou popsány pracovní postupy pro přispěvatele.

---

## Větve (branches)

| Větev | Účel |
| ------- | ------ |
| `main` | Jediná větev — publikovaná dokumentace na api.aiscr.cz; všechny PR cílí do `main` |

> **Poznámka:** Repozitář používá **single-branch workflow** — pull requesty se otevírají vždy do `main`. Nikdy nepushujte přímo do `main` bez PR.

---

## Konvence pojmenování větví

```markdown
<typ>/<popis-v-kebab-case>
```

Příklady:

```markdown
docs/aktualizace-oai-pmh-endpointu
fix/oprava-auth-api-prikladu
chore/aktualizace-fontawesome-extension
ci/oprava-deploy-workflow
agents/claude/review-api-sections
agents/copilot/update-changelogs
```

### Větve pro AI agenty

AI-generované větve musí dodržovat konvenci:

```markdown
agents/<jmeno-agenta>/<tema>
```

Příklady:

```markdown
agents/claude/review-oai-pmh
agents/claude-code/update-cicd-analysis
agents/copilot/fix-endpoint-examples
```

Větve agentů vždy cílí na `main` přes PR — **nikdy přímý push**.

---

## Typy příspěvků

```markdown
docs:    Nový nebo aktualizovaný obsah dokumentace API
fix:     Oprava chyby (nesprávné endpointy, překlepy, rozbité příklady)
style:   Změny stylů (SCSS/CSS), bez změn obsahu
chore:   Údržba projektu (aktualizace Quarto, extensions, závislostí)
ci:      Změny GitHub Actions workflows
```

---

## Pull Request proces

1. **Vytvořte větev** z `main`
2. **Proveďte změny** v `.qmd` souborech nebo konfiguračních souborech
3. **Lokálně sestavte** dokumentaci: `quarto render`
4. **Zkontrolujte výstup** v `_site/` — ověřte, že se stránky správně generují
5. **Ověřte správnost dokumentovaných endpointů** vůči živému API na https://api.aiscr.cz/ nebo vůči zdrojovému kódu backendů
6. **Otevřete PR do `main`** s popisem změn
7. **Počkejte na review** od vlastníků (viz `CODEOWNERS`)
8. Po schválení bude PR mergován

### Co kontrolovat před odesláním PR

- [ ] `quarto render` proběhne bez chyb
- [ ] Nové obrázky jsou uloženy do `figs/`
- [ ] Nové stránky jsou zahrnuty v `_quarto.yml`
- [ ] Dokumentované API endpointy odpovídají skutečnosti — ověřit vůči live API nebo zdrojovému kódu
- [ ] Příklady kódu (`curl`) jsou funkční
- [ ] Changelog v `changelogs/` je aktualizován při změně popisu endpointů

---

## Commit messages

Formát:

```markdown
<typ>: <stručný popis v češtině nebo angličtině>
```

Příklady:

```markdown
docs: aktualizace popisu OAI-PMH ListRecords endpoint
fix: oprava příkladu Auth API token requestu
chore: upgrade quarto-ext/fontawesome na v1.1.0
ci: přidat validaci odkazů do deploy workflow
```

---

## Quarto specifika

### Freeze

Repozitář používá `_freeze/` pro reproducibilitu výpočtů.  
Freeze soubory jsou verzovány v Gitu — při změně výpočetního kódu spusťte:

```bash
quarto render --execute
```

### Extensions

Quarto extensions jsou uloženy v `_extensions/`.  
Pro aktualizaci:

```bash
quarto add quarto-ext/fontawesome
```

### Lua filtry

Repozitář obsahuje Lua filtry. Při úpravách Lua kódu otestujte render výstup.

---

## Přesnost dokumentace API

> **Kritické:** Dokumentace API musí vždy přesně odrážet chování živého API.

Při úpravě popisu endpointů nebo parametrů vždy ověřte vůči:

- Živému API: https://api.aiscr.cz/
- Zdrojovému kódu Auth API: https://github.com/ARUP-CAS/aiscr-webamcr
- Zdrojovému kódu File API + OAI-PMH: https://github.com/ARUP-CAS/aiscr-digiarchiv-2

---

## AI-asistované přispívání

Větve vytvořené AI agenty musí:

1. Dodržovat konvenci pojmenování `agents/<jmeno-agenta>/<tema>`
2. Cílit výhradně na větev `main` přes PR
3. Obsahovat v popisu PR jasné označení, že jde o AI-generovaný obsah
4. Projít standardním code review — změny v `.agents/` vyžadují **lidský review**

### Jak spustit review session

Otevřete nový kontext AI agenta a jako první zprávu vložte:

```
Přečti .agents/prompts/review_codebase.md a spusť review session.
```

Agent si načte `AGENTS.md`, kontext z `.agents/` a zahájí session dle instrukcí
v `.agents/prompts/review_codebase.md`. Typy sezení (general-review, oai-pmh-accuracy,
file-api-accuracy, auth-api-accuracy aj.) jsou popsány tamtéž.

---

## Hlášení problémů

Chyby a návrhy hlašte prostřednictvím [GitHub Issues](https://github.com/ARUP-CAS/aiscr-api-home/issues)  
nebo [GitHub Discussions](https://github.com/ARUP-CAS/aiscr-api-home/discussions).

U issues uveďte:

- URL stránky nebo název endpointu, které se problém týká
- Popis problému (dokumentované chování vs. skutečné chování)
- Případný `curl` příkaz a výstup prokazující chybu
