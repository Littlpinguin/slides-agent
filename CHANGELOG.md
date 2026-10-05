# Changelog

Earlier releases are described by their git tags (`v0.1.0` to `v0.3.0`).

## Unreleased

### Changed: `scripts/qa.py` is now a full QA gate

- **Type floors made measurable.** Content text must be at least 18px (`--min-font`, was 16px). The label register (text inside `.chrome`, the eyebrow / meta-label / signature / folio classes, and any text set in a monospace stack) has its own floor of 12px (`--min-font-chrome`) instead of being exempt. Uppercase tracked text is no longer exempt either. New warnings: `tight-body` (content under 24px) and `long-label` (a label-register text under 18px longer than 12 words).
- **New checks:** engine parity with `templates/base.html` (read from the file, `--no-engine-check` to skip, for the catalogue), brand fonts (from `--font`, a DTCG `brand/tokens.json` / `01-brand/tokens.json`, or the deck's `--font-display` / `--font-body` / `--font-mono` variables), WCAG AA contrast on every text with opacity folded in, folios present and increasing.
- **Measurement:** geometry in native frame pixels at any `--viewport` (`--frame` for another native size), slides audited in their settled state (transition delays zeroed), `.slide` and `.plate` (catalogue) detected automatically, `.slide-bg`, `[data-bleed]`, `.aurora`, `.dust-grid` and the catalogue's `.legend` skipped by every check.
- **Reporting:** stable finding ids (`overflow`, `chrome-gap`, `type-floor`, `tight-body`, `long-label`, `font`, `contrast`, `folio`, `truncated`, `lang`, `pdf-weight`), `--format json` with totals by type and a `target` per finding, per-slide cap (`--max-per-slide`), `--lang` for bilingual decks, `--screenshots [DIR]`. `--with-pdf` / `--min-kb-per-slide` are kept.
- Exit codes: 0 clean (warnings allowed), 1 errors, 2 usage error or missing Playwright.

### Added

- `tests/test_qa.py`: pure-Python tests (colour, contrast, fonts, tokens, registers, folios, cap, engine parity) and deck tests on fictional decks driven by headless Chromium, skipped when Playwright or Chromium is missing.
