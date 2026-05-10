# slides-agent

> A Claude Code template for generating editorial-grade HTML presentations
> tightly aligned to your brand, exportable to clean PDF, and shareable
> as a single standalone `.html` file.

**Reference quality bar:** Monocle × Bloomberg viz × MIT Tech Review print.
What you get out is a long way from "AI startup 2025" generic.

---

## What this template gives you

- A **brand-aware design system** that auto-configures from your website (colours, typography, voice).
- A **component library** of editorial slide layouts (hero, breathing-number, big quote, KPI strata, roadmap, decision, etc.).
- A **standalone HTML output** — one file, no dependencies, fits on a USB stick, opens in any modern browser.
- **Three navigation modes** baked in: arrow keys, drag bar, overview grid (`O`), quick-jump.
- **Clean PDF export** at 1920×1080 (gradient text rasterised to PNG to avoid Chromium PDF artefacts).
- **Anti-overflow QA** via Playwright — every slide is verified to stay within frame before delivery.
- **Zero-config hosting** — drop the folder on Netlify Drop, GitHub Pages, S3, or any static host.

---

## Use this template

### Option 1 — GitHub template (recommended)

1. Click **Use this template** at the top of the GitHub repo.
2. Clone your new repo locally.
3. Open it in [Claude Code](https://claude.ai/code).
4. Claude will walk you through onboarding (website analysis → brand tokens → asset collection).
5. Tell Claude what you want to present.

### Option 2 — Manual copy

```bash
git clone https://github.com/<your-org>/slides-agent.git my-decks
cd my-decks
rm -rf .git && git init
```

Then open in Claude Code and follow the same flow.

---

## First-run experience

When you open the project in Claude Code, the agent will:

1. **Ask for your brand's website URL** and analyse it (colours, fonts, voice).
2. **Populate `brand/tokens.css` and `brand/guidelines.md`** automatically.
3. **Ask you to drop assets** into `assets/logos/`, `assets/illustrations/`, `assets/photos/`, `assets/icons/`.
4. **Confirm setup**, then ask what you want to present.

> The single biggest factor in slide quality is your **`assets/` folder**.
> Logos, illustrations, photos, custom icons — the more you provide, the more on-brand the output.
> 15 minutes of asset preparation saves hours of art-direction iteration.

---

## Generating a deck

Two ways:

**From a source document** — Paste a brief, transcript, strategy memo, or research notes. Claude will extract key messages, draft a slide map, and ask for approval before writing HTML.

**From scratch** — Just say *"I want to present X to Y"*. Claude will invoke the `superpowers:brainstorming` skill, walk you through structure and intent, then generate.

---

## Presenting & sharing

```bash
# Local presentation (static server on :5173)
./scripts/serve.sh

# Export a deck to clean 1920×1080 PDF
./scripts/export-pdf.sh presentations/your-deck.html

# QA — verify no overflow on any slide
python scripts/qa.py presentations/your-deck.html
```

For online sharing, the deck is a single self-contained HTML file. See [`docs/hosting.md`](docs/hosting.md) for Netlify Drop, GitHub Pages, S3, and other targets.

---

## Project layout

```
.
├── CLAUDE.md                  # Agent playbook (read first if you're Claude)
├── brand/
│   ├── tokens.css             # CSS custom properties (auto-filled at onboarding)
│   └── guidelines.md          # Voice, typography, restraint rules
├── assets/
│   ├── logos/                 # Your logo (SVG preferred)
│   ├── illustrations/         # Brand illustrations
│   ├── photos/                # Editorial photography
│   └── icons/                 # Custom icon set
├── templates/
│   ├── base.html              # Standalone deck skeleton (chrome, nav, print mode)
│   ├── components.md          # Component library catalogue
│   └── components/            # Paste-ready slide layouts
├── presentations/             # Your generated decks live here
├── scripts/
│   ├── qa.py                  # Playwright overflow check
│   ├── serve.sh               # Local static server
│   └── export-pdf.sh          # Headless Chromium PDF export
└── docs/
    ├── design-system.md
    ├── hosting.md
    └── pdf-export.md
```

---

## Requirements

- **Claude Code** (or another agent that respects `CLAUDE.md`)
- **Node.js ≥ 18** (for the local server and PDF export, both via `npx`)
- **Python ≥ 3.10 + Playwright** for QA: `pip install playwright && playwright install chromium`
- A modern browser (Chrome / Chromium / Edge) for presenting

---

## License

MIT — see [`LICENSE`](LICENSE).
