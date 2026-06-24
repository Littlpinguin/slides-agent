# `scripts/` — index

Helper scripts for building, checking, and exporting decks. Every script is
brand-agnostic and operates on a deck HTML file built from `templates/base.html`.

Most scripts need Python + Playwright once:

```bash
pip install playwright && playwright install chromium
```

| Script | Purpose | Output |
|---|---|---|
| `serve.sh` | Local static server to preview decks in a browser | — (HTTP server) |
| `qa.py` | Verify slides fit the 1920×1080 frame and respect the chrome safe-zone | pass/fail report (+ optional PNGs / PDF) |
| `shots.py` | Capture chosen slides with animations neutralised, for visual review | `/tmp/slide-NN.png` |
| `export-pdf.sh` | Wrapper that exports a deck to PDF | `<deck>.pdf` |
| `export_pdf.py` | Headless Chromium PDF renderer (called by `export-pdf.sh`) | `<deck>.pdf` |
| `gen-image.py` | Generate brand illustrations via Nano Banana Pro (needs an API key) | image file(s) |

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

## `qa.py` — overflow + chrome safe-zone QA

The mandatory gate before delivery. Activates each slide in headless Chromium
and checks that no element overflows the `#stage-frame` (1920×1080) and that no
content invades the bottom chrome safe-zone (needs a ≥ 16px gap). Prints a
per-slide report and exits non-zero if any slide has issues.

```bash
python scripts/qa.py presentations/your-deck.html
```

Useful flags:

- `--viewport 1920x1080` — change the test viewport (default `1920x1080`).
- `--screenshots` — also save per-slide PNGs to `/tmp/slides-qa/`.
- `--with-pdf` — additionally render a PDF and fail if the average page weight
  is implausibly small (symptom of print CSS collapsing pages);
  tune with `--min-kb-per-slide`.

**Produces:** a pass/fail report on stdout (`All slides clean · N / N` on
success). With the optional flags, PNGs and/or a PDF under `/tmp/slides-qa/`.

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
