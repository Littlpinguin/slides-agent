# `scripts/` — index

Helper scripts for building, checking, and exporting decks. Every script is
brand-agnostic and operates on a deck HTML file built from `templates/base.html`.

Most scripts need Python + Playwright once (`pexels.py` also needs `requests` and `Pillow`):

```bash
pip install playwright && playwright install chromium
```

| Script | Purpose | Output |
|---|---|---|
| `serve.sh` | Local static server to preview decks in a browser | — (HTTP server) |
| `qa.py` | The QA gate: engine parity, overflow, chrome safe zone, type floors, brand fonts, contrast, folios | pass/fail report, text or JSON (+ optional PNGs / PDF) |
| `shots.py` | Capture chosen slides with animations neutralised, for visual review | `/tmp/slide-NN.png` |
| `export-pdf.sh` | Wrapper that exports a deck to PDF | `<deck>.pdf` |
| `export_pdf.py` | Headless Chromium PDF renderer (called by `export-pdf.sh`) | `<deck>.pdf` |
| `gen-image.py` | Generate brand illustrations via Nano Banana Pro (needs an API key) | image file(s) |
| `pexels.py` | Search, download, brand-tint and credit Pexels photos (free API key) | `assets/photos/pexels-*` + credits slide HTML |

---

## `serve.sh` — local preview server

Serves the repo root over HTTP so decks load with correct relative paths and
fonts. Uses `python3 -m http.server` (or `npx http-server` as a fallback); no
install required.

```bash
./scripts/serve.sh
# then open http://localhost:5173/presentations/ in Chrome
```

Override the port with `PORT=8080 ./scripts/serve.sh`. Stop with `ctrl-c`.

**Produces:** a running static server on `http://localhost:5173` (default).

---

## `qa.py` — the QA gate

The mandatory gate before delivery. Reads the deck for engine parity with
`templates/base.html` (the canonical feature list is `docs/engine-parity.md`),
then activates each slide in headless Chromium, in its
settled state, and measures in native 1920×1080 pixels: overflow out of the
`#stage-frame`, the bottom chrome safe zone (≥ 16px gap), type floors (content
≥ 18px, label register ≥ 12px), brand fonts, WCAG AA contrast (opacity
included) and folios. Prints a per-slide report and exits 1 on any error
(warnings don't fail), 2 on a usage error.

```bash
python3 scripts/qa.py presentations/your-deck.html
python3 scripts/qa.py reference/catalogue-layouts.html --no-engine-check
```

The label register (12px floor) is: anything inside `.chrome`, the label
classes (`.eyebrow`, `.meta-label`, `.signature`, `.nav-num`, `.tag-meta`,
`.tag-folio`, `.tag-signature`) and any text set in a monospace stack. Brand
fonts come from `--font`, a DTCG tokens file (`--tokens`, `brand/tokens.json`,
`01-brand/tokens.json`), or the deck's `--font-display` / `--font-body` /
`--font-mono` variables.

Full-bleed images are exempt by design: anything inside `.slide-bg`, `.aurora`,
`.dust-grid` and any element with a `data-bleed` attribute (a photo that runs
to the frame edge) is skipped; the text on top is still checked.

Useful flags:

- `--min-font 18` / `--min-font-chrome 12` — the two type floors.
- `--viewport 1920x1080`, `--frame 1920x1080` — window and native frame sizes.
- `--format json` — machine-readable report with totals by finding type.
- `--max-per-slide 8` — findings listed per slide and type (`0` lists all).
- `--screenshots [DIR]` — also save per-slide PNGs (default `/tmp/slides-qa/`).
- `--with-pdf` — additionally render a PDF and fail if the average page weight
  is implausibly small (symptom of print CSS collapsing pages);
  tune with `--min-kb-per-slide`.
- `--lang CODE`, `--bleed SELECTOR`, `--folio SELECTOR` / `--no-folio`,
  `--no-engine-check`, `--wait MS`: see `--help`.

**Produces:** a pass/fail report on stdout (`All slides clean · N / N` on
success). With the optional flags, PNGs and/or a PDF under `/tmp/slides-qa/`.

Tests: `python3 -m pytest tests -q` (the deck tests skip cleanly without
Playwright or Chromium).

---

## `shots.py` — control screenshots

Fast visual check of specific slides. Activates each requested slide, forces its
`.reveal` and `[data-stagger]` elements to their final visible state (so the PNG
isn't caught mid-animation), and screenshots the rendered frame.

```bash
python scripts/shots.py presentations/your-deck.html          # all slides
python scripts/shots.py presentations/your-deck.html 3 8 18    # slides 3, 8, 18
```

`--viewport 1920x1080` overrides the capture size.

**Produces:** one PNG per captured slide at `/tmp/slide-NN.png` (NN = 1-based
slide index).

---

## `export-pdf.sh` — PDF export (wrapper)

Convenience wrapper around `export_pdf.py`. Exports a deck to a clean 1920×1080
PDF, one slide per page.

```bash
./scripts/export-pdf.sh presentations/your-deck.html              # → presentations/your-deck.pdf
./scripts/export-pdf.sh presentations/your-deck.html leave-behind.pdf
```

The output path defaults to the input path with a `.pdf` extension.

**Produces:** a PDF next to the deck (or at the path you pass as the second
argument).

---

## `export_pdf.py` — PDF renderer

The headless Chromium renderer that `export-pdf.sh` calls. Loads the deck, waits
for fonts, triggers the deck's print-mode hooks (`__enablePrintMode` and
`__rasterizeGradients`, which fix gradient-on-text artefacts and freeze the
animation final state), then prints each slide to a 1920×1080 page. Call it
directly if you want to skip the wrapper.

```bash
python scripts/export_pdf.py input.html output.pdf
```

**Produces:** the PDF at the second argument path.

---

## `gen-image.py` — brand illustration generator

Generates brand-compliant illustrations via Nano Banana Pro (Google Gemini
image model). Documented separately — see the script's own header and the
`image-generation` skill for prompt conventions. **Requires an API key in
`.env`** (not committed).

```bash
python scripts/gen-image.py "<prompt>"
```

**Produces:** generated image file(s) for use as deck backgrounds or section
art. Never paste the API key into a chat or commit; keep it in `.env`.

---

## `pexels.py` — real photography from Pexels

The engine behind the `pexels-photos` skill. Searches the free Pexels API,
builds a numbered contact sheet so a whole search can be judged in one look,
downloads the chosen photo with a credit sidecar, optionally bakes a
brand-tinted variant, and generates the deck's closing credits slide. Photos are
always downloaded (never hotlinked), so decks stay offline-functional.

**Requires a free `PEXELS_API_KEY` in `.env`** (step-by-step:
`docs/pexels-setup.md`) and `python3 -m pip install requests pillow`.

```bash
python3 scripts/pexels.py check                                   # key works? quota left?
python3 scripts/pexels.py search "harbour at dawn fog"            # + --orientation, --color brand-primary, --per-page
python3 scripts/pexels.py get 1234567 --slug harbour-dawn         # + --treatment mono|duotone, --width 1600
python3 scripts/pexels.py credits presentations/your-deck.html    # + --lang fr
```

- `search` writes `.cache/pexels/<query>/sheet.jpg` (numbered contact sheet)
  and `results.json` (git-ignored cache).
- `get` writes `assets/photos/pexels-<slug>-<id>.jpg`, the optional
  `-mono` / `-duotone` variant (colours from `brand/tokens.css`, baked into the
  file so screen and PDF match), and a `.json` sidecar with the photographer
  and source.
- `credits` prints the `photo-credits` slide (see `templates/components.md`)
  listing each photographer with the slides where their photo appears.

Offline tests: `python3 -m pytest tests/test_pexels.py -q`.

**Produces:** photos + sidecars in `assets/photos/`, contact sheets in
`.cache/pexels/`, credits slide HTML on stdout. Never paste the API key into a
chat or commit it; keep it in `.env`.
