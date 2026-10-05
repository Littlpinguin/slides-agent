# slides-agent

> A Claude Code template for generating editorial-grade HTML presentations
> tightly aligned to your brand, exportable to clean PDF, and shareable
> as a single standalone `.html` file.

**Reference quality bar:** Monocle × Bloomberg viz × MIT Tech Review print.
What you get out is a long way from "AI startup 2025" generic.

**Built on top of two excellent design intelligence skills** that the agent invokes during slide generation:
- [`ui-ux-pro-max`](https://github.com/the-ai-toolkit/ui-ux-pro-max) by [@the-ai-toolkit](https://github.com/the-ai-toolkit) — 50+ design styles, 161 colour palettes, 57 font pairings, 99 UX heuristics, 25 chart types
- [21st.dev MCP tools](https://21st.dev) (`mcp__magic__21st_magic_component_*`) — production-grade UI component inspiration, refinement and search

Both are used as **inspiration sources** during art direction (Phase 2) and component design (Phase 3). Their output is always reworked into the 1920×1080 frame and re-tokenised through `brand/tokens.css` before landing in a slide. Credit and respect to both teams — without them, the output of this template would be markedly more generic.

---

## Example output

[`presentations/examples/qiplim-launch.pdf`](presentations/examples/qiplim-launch.pdf) — a real public-launch deck for [Qiplim](https://qiplim.com), generated end-to-end with this template. Periwinkle/Golden/Cream brand, GT Walsheim Pro Condensed typography, full editorial chrome system, gradient text, blob mascots, exported PDF.

---

## What this template gives you

- A **brand-aware design system** that auto-configures from your website (colours, typography, voice).
- A **layout library of 113 editorial slide layouts** in 8 families, indexed with a "reach for it when" line each, all **executed and self-captioned** in a browsable catalogue deck.
- A **standalone HTML output** — one file, no dependencies, fits on a USB stick, opens in any modern browser.
- **Three navigation modes** baked in: arrow keys, drag bar, overview grid (`O`), quick-jump.
- **Presentation mode** — fullscreen via the `F` key or the ⛶ button: the slide fills the screen and the nav-rail auto-hides.
- **Real photography, optional and free** — connect a Pexels key (guided, about 3 minutes) and the agent picks editorial photos for the slides that need one, rejects stock clichés, tints them to your palette on request, and credits every photographer on a closing slide.
- **Clean PDF export** at 1920×1080 (gradient text rasterised to PNG to avoid Chromium PDF artefacts).
- **A measured QA gate** via Playwright: every slide is checked for overflow, the chrome safe zone, type floors (18px content, 12px labels), brand fonts, WCAG contrast and folios before delivery.
- **Zero-config hosting** — drop the folder on Netlify Drop, GitHub Pages, S3, or any static host.

---

## The layout library

Most decks fail the same way: three card grids, two tables, and a wall of bullets. The library exists to make that harder.

- **`reference/LAYOUTS.md`** indexes 113 layouts across 8 families — opening, editorial, data-viz, schemas, tables, proof, closing, photography. Each row says what the layout does and when to reach for it, so you choose by narrative beat rather than by browsing.
- **`reference/catalogue-layouts.html`** is a deck where every one of them is executed on a fictional brand. Every slide carries its own caption: the layout name and its use case. Open it, press `O` for the grouped overview, and pick.
- **`templates/components.md`** holds paste-ready HTML and scoped CSS for the ported ones, each with the traps that cost time the first time — waterfall spacer arithmetic, orbit collision points, rails that need forcing to their final state in PDF.

**The variety rule the agent applies:** no layout twice in a row, none more than twice in a deck.

The catalogue is deliberately built on an invented brand with invented figures. That is what lets it be read as a layout reference without contaminating a new deck with someone else's narrative, and what keeps this repository free of client material.

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
git clone https://github.com/Littlpinguin/slides-agent.git my-decks
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
4. **Offer to connect Pexels** for real photography (optional): it walks you through the free API key one step at a time and tests it for you.
5. **Confirm setup**, then ask what you want to present.

> The single biggest factor in slide quality is your **`assets/` folder**.
> Logos, illustrations, photos, custom icons — the more you provide, the more on-brand the output.
> 15 minutes of asset preparation saves hours of art-direction iteration.

---

## Optional — AI illustrations (Nano Banana Pro)

The biggest lever on render quality is your `assets/` folder. To go further, connect a **Gemini Nano Banana Pro** API key and let the agent generate **on-brand illustrations on demand** (heroes, scene illustrations, mascots, metaphors). Every prompt is auto-prefixed with *your* configured brand style — palette from `brand/tokens.css`, illustration style and banned tropes from `brand/guidelines.md` — so the output adapts to whatever brand you set up. It is **optional**: without a key, decks rely on your assets, inline icons, and tokens.

```bash
cp .env.example .env
# then set GOOGLE_AI_API_KEY=...   (a Google AI Studio key)
# GOOGLE_AI_IMAGE_MODEL defaults to gemini-3-pro-image-preview
```

The `generate-image` skill builds every prompt with the Nano Banana Pro doctrine (natural-language prose, identity lock, keep/change), journals each generation, and saves outputs to `assets/illustrations/`. See `scripts/gen-image.py` and `.claude/skills/generate-image.md`.

---

## Optional — Real photography (Pexels)

Some beats want a real image: a place, a material, an object, a gesture, an atmosphere. Connect a free [Pexels](https://www.pexels.com/api/) key and the agent handles those slides end to end:

1. **Searches** with concrete queries (`harbour at dawn fog`, never `success`) and reads a numbered contact sheet of the results.
2. **Curates** against an anti-stock doctrine: no handshakes, suits, smiling faces at the camera, lightbulbs or robot hands. About one slide in four at most.
3. **Downloads** the chosen photo into `assets/photos/` with a JSON sidecar (photographer, source, alt text). Never hotlinked: the deck stays offline-functional.
4. **Tints** it to your palette on request (`mono` or `duotone`, colours read from `brand/tokens.css`, baked into the file so screen and PDF match).
5. **Credits** every photographer on a generated closing slide, as the Pexels guidelines ask.

The photos land in a dedicated **photography family** of eight layouts (plate, diptych, letterbox band, margin figure, field notes, scale contrast, typology grid, sequence strip) plus the credits slide, all executed on real Pexels photos in the catalogue (plates 105–113) and paste-ready in `templates/components.md`.

Setup is guided: during onboarding (or the first time a slide needs a photo), the agent walks you through [`docs/pexels-setup.md`](docs/pexels-setup.md) one step at a time: create a free account, get the key, paste it into `.env` yourself, test it.

```bash
cp .env.example .env
# then set PEXELS_API_KEY=...   (free key from https://www.pexels.com/api/)
python3 scripts/pexels.py check
```

Free tier: 200 requests per hour, 20,000 per month; a 24-slide deck typically uses 10 to 30. See `scripts/pexels.py` and `.claude/skills/pexels-photos.md`.

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

# QA — overflow, chrome safe zone, type floors, fonts, contrast, folios
python3 scripts/qa.py presentations/your-deck.html

# Capture specific slides for a quick visual check
python scripts/shots.py presentations/your-deck.html 3 8 18
```

Press **`F`** (or the ⛶ button) for fullscreen **presentation mode**: the slide fills the screen and the nav-rail auto-hides (it reappears when the cursor nears the bottom edge).

For online sharing, the deck is a single self-contained HTML file. See [`docs/hosting.md`](docs/hosting.md) for Netlify Drop, GitHub Pages, S3, and other targets.

---

## Quality gate (QA)

`scripts/qa.py` opens the deck in headless Chromium, activates every slide in its settled state (transitions finished, no half-played stagger) and measures what is actually rendered, in native 1920×1080 pixels. A deck ships only when it ends with `All slides clean`.

| Check (`type`) | Rule | Level |
|---|---|---|
| engine parity | the deck embeds every feature of `templates/base.html`: fullscreen, overview, auto folios, PDF hooks | error |
| `overflow` | nothing leaves the frame | error |
| `chrome-gap` | content stays at least 16px above the bottom chrome row | error |
| `type-floor` | content text ≥ 18px, label register ≥ 12px (see below) | error |
| `tight-body` | content text under 24px, headings excepted | warning |
| `long-label` | a label-register text under 18px that runs past 12 words | warning |
| `font` | every text uses a brand family | error (undeclared monospace: warning) |
| `contrast` | WCAG AA, 4.5:1 or 3:1 from 24px (18.66px bold); opacity counts | error (gradient or image background: warning) |
| `folio` | present and increasing on every slide | error |
| `pdf-weight` | with `--with-pdf`, the PDF averages at least 40 KB per slide | error |

**The type floor, made measurable.** A slide is read from across a room, so the doctrine in `CLAUDE.md` becomes two numbers checked on the computed font size:

- **Content text: 18px minimum** (`--min-font`). Comfortable body is 24px and up, hence the `tight-body` warning.
- **Label register: 12px minimum** (`--min-font-chrome`). A text is a label when it sits inside `.chrome`, carries a label class (`.eyebrow`, `.meta-label`, `.signature`, `.nav-num`, and the catalogue's `.tag-meta`, `.tag-folio`, `.tag-signature`), or is set in a monospace stack (folio, signature and caption register). Labels stay short: a sentence shrunk to caption size, in mono or not, is still flagged.

**Brand fonts** come from `--font`, else from a DTCG tokens file (`--tokens`, or the first `brand/tokens.json` / `01-brand/tokens.json` found up to the repository root), else from the deck's own `--font-display`, `--font-body` and `--font-mono` variables, which is where `brand/tokens.css` puts them in this template. No tokens file is needed.

```bash
python3 scripts/qa.py presentations/your-deck.html                        # the gate
python3 scripts/qa.py presentations/your-deck.html --with-pdf             # + PDF weight check (/tmp/slides-qa/)
python3 scripts/qa.py presentations/your-deck.html --format json          # totals by type, findings with their target
python3 scripts/qa.py reference/catalogue-layouts.html --no-engine-check  # the catalogue: a specimen book, not a full deck
```

Other flags: `--viewport` / `--frame` (window and native frame sizes), `--bleed SELECTOR` (an intentional full-bleed layer; `.slide-bg` and `[data-bleed]` are exempt by default), `--folio SELECTOR` / `--no-folio`, `--lang CODE` (audit a bilingual deck in each language through `window.__setLang`), `--wait MS`, `--max-per-slide N` (listing cap, 0 for all), `--screenshots [DIR]`, `--min-kb-per-slide KB`. Exit codes: 0 clean (warnings allowed), 1 errors, 2 usage error. `python3 scripts/qa.py --help` documents each one.

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
├── .env.example               # optional keys: GOOGLE_AI_API_KEY (AI illustrations), PEXELS_API_KEY (photos)
├── .claude/skills/            # create-slides, generate-image, pexels-photos
├── templates/
│   ├── base.html              # Standalone deck skeleton (chrome, nav, fullscreen, print)
│   └── components.md          # Paste-ready HTML + CSS for the ported layouts
├── reference/
│   ├── photos/                # Pexels photos used by the catalogue's photography plates (+ credit sidecars)
│   ├── LAYOUTS.md             # Index of 113 layouts in 8 families, with selection guidance
│   └── catalogue-layouts.html # 113 layouts executed and captioned, on a fictional brand
├── presentations/             # Your generated decks live here
├── scripts/
│   ├── README.md              # Index of every script
│   ├── qa.py                  # Playwright QA gate: overflow, chrome, type floors, fonts, contrast, folios
│   ├── shots.py               # Capture specific slides for visual review
│   ├── gen-image.py           # AI illustration generation (needs an API key)
│   ├── pexels.py              # Pexels search, download, tint and credits (free key)
│   ├── serve.sh               # Local static server
│   └── export-pdf.sh          # Headless Chromium PDF export
├── tests/                     # pytest: scripts/pexels.py offline, scripts/qa.py (deck tests need Chromium)
└── docs/
    ├── design-system.md
    ├── hosting.md
    ├── pdf-export.md
    └── pexels-setup.md        # step-by-step Pexels key setup
```

---

## Requirements

- **Claude Code** (or another agent that respects `CLAUDE.md`)
- **Node.js ≥ 18** (for the local server and PDF export, both via `npx`)
- **Python ≥ 3.10 + Playwright** for QA: `pip install playwright && playwright install chromium`
- A modern browser (Chrome / Chromium / Edge) for presenting
- *(Optional)* A free **Pexels API key** + `pip install requests pillow` for real photography — see [Optional — Real photography](#optional--real-photography-pexels)
- *(Optional)* A **Google AI Studio API key** (Gemini Nano Banana Pro) for on-brand AI illustrations — see [Optional — AI illustrations](#optional--ai-illustrations-nano-banana-pro)

---

## Credits

- **[`ui-ux-pro-max`](https://github.com/the-ai-toolkit/ui-ux-pro-max)** — design intelligence skill that informs colour systems, font pairings, and visual style choices when the brand guidelines are sparse. Citation in `CLAUDE.md` and `.claude/skills/create-slides.md`.
- **[21st.dev](https://21st.dev)** (`mcp__magic__21st_magic_*`) — UI component inspiration and refinement, especially for hero treatments, complex tables, and navigation chrome details.
- **[Pexels](https://www.pexels.com)** — free photography and API; every photographer used in a deck is credited on its closing slide.
- **Editorial print magazines** — Monocle, Bloomberg Businessweek, Aeon, MIT Tech Review — for the visual quality bar.
- **Nancy Duarte** (sparkline narrative arcs) and **Garr Reynolds** (presentation Zen) for the narrative-craft principles documented in `CLAUDE.md`.

## License

MIT — see [`LICENSE`](LICENSE).
