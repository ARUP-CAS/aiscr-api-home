# Dokumentace AMČR API

[![SWH](https://archive.softwareheritage.org/badge/origin/https://github.com/ARUP-CAS/aiscr-api-home/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/ARUP-CAS/aiscr-api-home)

Repozitář obsahuje zdrojové soubory dokumentace API systému AMČR (Archeologická mapa České republiky), součásti [AIS CR](https://www.aiscr.cz/).  
Web je publikován na adrese **[api.aiscr.cz](https://api.aiscr.cz/)**.

➡ [ENGLISH VERSION HERE](README_en.md)

---

## O projektu

AMČR API poskytuje strojově čitelný přístup k datům Archeologické mapy České republiky.  
Dokumentace pokrývá tři hlavní rozhraní:

- **Auth API** — autentizace a správa přístupu
- **File API** — přístup k souborům a dokumentům Digitálního archivu
- **OAI-PMH** — protokol pro sklízení metadat (Open Archives Initiative Protocol for Metadata Harvesting)

AMČR API je součástí ekosystému [AIS CR](https://www.aiscr.cz/), který provozuje [Archeologický ústav AV ČR, Praha, v. v. i. (ARÚP)](https://www.arup.cas.cz/) a [Archeologický ústav AV ČR, Brno, v. v. i. (ARÚB)](https://arub.cz/).

---

## Technický stack

| Vrstva | Technologie |
| -------- | ------------- |
| Dokumentační framework | [Quarto](https://quarto.org/) |
| Scripty / build | JavaScript, Python |
| Lua filtry | Quarto Lua filters |
| Styling | SCSS, CSS (vlastní téma `theme.scss`, `museo.css`) |
| Quarto extensions | `quarto-ext/fontawesome` |
| Publikace | GitHub Pages (vlastní doména `api.aiscr.cz`) |
| CI/CD | GitHub Actions |
| Citace | CITATION.cff, Software Heritage |

---

## Struktura repozitáře

```markdown
aiscr-api-home/
├── _quarto.yml            # Hlavní konfigurace Quarto projektu
├── index.qmd              # Úvodní stránka
├── 404.qmd                # Stránka pro nenalezené URL
├── theme.scss             # Vlastní Bootstrap/Quarto SCSS téma
├── museo.css              # Font Museo
│
├── about/                 # Informace o API a dokumentaci
├── auth-api/              # Dokumentace Auth API (autentizace)
├── file-api/              # Dokumentace File API (soubory a dokumenty)
├── oai-pmh/               # Dokumentace OAI-PMH protokolu
├── changelogs/            # Changelog API a dokumentace
├── figs/                  # Obrázky a diagramy
├── fonts/                 # Vlastní fonty
│
├── _extensions/           # Quarto extensions (fontawesome)
├── _freeze/               # Freeze soubory (reproducibilita)
├── .github/               # GitHub Actions workflows
│
├── CITATION.cff           # Citační metadata
├── CODEOWNERS             # Vlastníci kódu
├── AGENTS.md              # Pokyny pro AI agenty
└── docs_agents/           # AI review infrastruktura
```

---

## Lokální spuštění

### Předpoklady

- [Quarto CLI](https://quarto.org/docs/get-started/) ≥ 1.4
- Node.js (pro případné build skripty)
- Python ≥ 3.10 (pro případné pomocné skripty)

### Náhled dokumentace

```bash
quarto preview
```

### Sestavení (render)

```bash
quarto render
```

Výstup je generován do složky `_site/`.

---

## Přispívání

Viz [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Citace

Pokud tuto dokumentaci citujete, použijte prosím metadata v souboru [CITATION.cff](CITATION.cff).

---

## Kontakt

- **Archeologický ústav AV ČR, Praha, v. v. i.**  
  [www.arup.cas.cz](https://www.arup.cas.cz/)
- **Archeologický ústav AV ČR, Brno, v. v. i.**  
  [www.arub.cz](https://www.arub.cz/)
- Podpora: prostřednictvím [GitHub Issues](https://github.com/ARUP-CAS/aiscr-api-home/issues)  
  nebo [GitHub Discussions](https://github.com/ARUP-CAS/aiscr-api-home/discussions)

---

## Související repozitáře

- [aiscr-webamcr](https://github.com/ARUP-CAS/aiscr-webamcr) — hlavní aplikace AMČR (backend API)
- [aiscr-digiarchiv-2](https://github.com/ARUP-CAS/aiscr-digiarchiv-2) — Digitální archiv (File API backend)
