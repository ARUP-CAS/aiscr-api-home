# AMČR API Documentation

[![SWH](https://archive.softwareheritage.org/badge/origin/https://github.com/ARUP-CAS/aiscr-api-home/)](https://archive.softwareheritage.org/browse/origin/?origin_url=https://github.com/ARUP-CAS/aiscr-api-home)

This repository contains the source files for the documentation of the AMČR API (Archaeological Map of the Czech Republic), part of [AIS CR](https://www.aiscr.cz/).  
The documentation is published at **[api.aiscr.cz](https://api.aiscr.cz/)**.

Czech version: see [README.md](README.md)

---

## About

The AMČR API provides machine-readable access to data from the Archaeological Map of the Czech Republic. The documentation covers three main interfaces:

- **Auth API** — authentication and access management
- **File API** — access to files and documents in the Digital Archive
- **OAI-PMH** — metadata harvesting protocol (Open Archives Initiative Protocol for Metadata Harvesting)

The AMČR API is part of the [AIS CR](https://www.aiscr.cz/) ecosystem, operated by the [Institute of Archaeology of the Czech Academy of Sciences, Prague (ARÚP)](https://www.arup.cas.cz/) and [Institute of Archaeology of the Czech Academy of Sciences, Brno (ARÚB)](https://arub.cz/).

---

## Technical Stack

| Layer | Technology |
| ------- | ------------ |
| Documentation framework | [Quarto](https://quarto.org/) |
| Scripts / build | JavaScript, Python |
| Lua filters | Quarto Lua filters |
| Styling | SCSS, CSS (custom theme `theme.scss`, `museo.css`) |
| Quarto extensions | `quarto-ext/fontawesome` |
| Publishing | GitHub Pages (custom domain `api.aiscr.cz`) |
| CI/CD | GitHub Actions |
| Citation | CITATION.cff, Software Heritage |

---

## Repository Structure

```markdown
aiscr-api-home/
├── _quarto.yml            # Main Quarto project configuration
├── index.qmd              # Home page
├── 404.qmd                # 404 not found page
├── theme.scss             # Custom Bootstrap/Quarto SCSS theme
├── museo.css              # Museo font
│
├── about/                 # About the API and documentation
├── auth-api/              # Auth API documentation (authentication)
├── file-api/              # File API documentation (files and documents)
├── oai-pmh/               # OAI-PMH protocol documentation
├── changelogs/            # API and documentation changelog
├── figs/                  # Figures and diagrams
├── fonts/                 # Custom fonts
│
├── _extensions/           # Quarto extensions (fontawesome)
├── _freeze/               # Freeze files (reproducibility)
├── .github/               # GitHub Actions workflows
│
├── CITATION.cff           # Citation metadata
├── CODEOWNERS             # Code ownership
├── AGENTS.md              # Instructions for AI agents
└── .agents/           # AI review infrastructure
```

---

## Local Development

### Prerequisites

- [Quarto CLI](https://quarto.org/docs/get-started/) ≥ 1.4
- Node.js (for build scripts)
- Python ≥ 3.10 (for auxiliary scripts)

### Preview

```bash
quarto preview
```

### Build (render)

```bash
quarto render
```

Output is generated into the `_site/` directory.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Citation

If you use or reference this documentation, please use the metadata in [CITATION.cff](CITATION.cff).

---

## Contact

- **Institute of Archaeology of the Czech Academy of Sciences, Prague**  
  [www.arup.cas.cz](https://www.arup.cas.cz/)
- **Institute of Archaeology of the Czech Academy of Sciences, Brno**  
  [www.arub.cz](https://www.arub.cz/)
- Support: via [GitHub Issues](https://github.com/ARUP-CAS/aiscr-api-home/issues)  
  or [GitHub Discussions](https://github.com/ARUP-CAS/aiscr-api-home/discussions)

---

## Related Repositories

- [aiscr-webamcr](https://github.com/ARUP-CAS/aiscr-webamcr) — AMČR main application (API backend)
- [aiscr-digiarchiv-2](https://github.com/ARUP-CAS/aiscr-digiarchiv-2) — Digital Archive (File API backend)
