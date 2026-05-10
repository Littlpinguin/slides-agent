# Brand assets

> **The richer this folder, the better your presentations will look.**
> Slide quality is bottlenecked by the visual material the agent has access to.
> A logo alone is the bare minimum. A full asset library produces editorial-grade decks.

## What to put here

```
assets/
├── logos/          ← your logo (SVG preferred), wordmark, favicon, monogram variants
├── illustrations/  ← brand illustrations, portraits, scenes, hand-drawn marks
├── photos/         ← product photography, team portraits, lifestyle, atmospheres
└── icons/          ← brand-specific icon set (SVG), pictograms, symbols
```

## Format priorities

| Format | Use for | Notes |
|---|---|---|
| `.svg` | Logos, icons, simple illustrations | First choice — scalable, embeddable inline, cleanest in PDF |
| `.png` (transparent) | Complex illustrations, portraits | Use 2x or 3x density for projection |
| `.webp` / `.jpg` | Photography | Compressed, web-optimised |
| `.pdf` | Brand guidelines references | Read-only inputs for the agent |

## Naming convention

Use kebab-case, descriptive, lowercase: `logo-primary.svg`, `logo-monochrome-dark.svg`, `portrait-founder-jane.png`, `icon-feature-search.svg`.

## What the agent will do with these

When you ask Claude to generate a presentation, it will scan this folder and:

- Embed your **logo SVG inline** in the deck so it appears in the chrome (bottom-right corner of every slide) and as an ambient watermark on hero slides.
- Pick **illustrations and photos** that match the slide's emotional beat (hero, breathing, decision moments).
- Use your **icons** for stack/feature/tool grids instead of generic emoji or downloaded marks.

## What you should add — checklist

- [ ] **Primary logo** as `logos/logo-primary.svg` — the main mark on a transparent background
- [ ] **Monochrome variants** as `logos/logo-mono-light.svg` and `logos/logo-mono-dark.svg` — for dark/light slide backgrounds
- [ ] **Wordmark** if separate from the symbol, as `logos/wordmark.svg`
- [ ] **3–6 brand illustrations** in `illustrations/` covering different moods (hero, abstract, atmospheric)
- [ ] **Portraits** of key team members or personas if relevant, as SVG or transparent PNG
- [ ] **5–15 brand-specific icons** in `icons/` — your custom pictogram language
- [ ] **3–5 hero photos** in `photos/` with editorial quality (avoid stock-looking imagery)

## When you don't have an asset

Tell the agent. It will fall back to typography-driven layouts (which often look better than a bad image anyway) or fetch logos for third-party tools from `cdn.simpleicons.org` / `iconify.design`.

But: **investing 15 minutes here saves hours of art-direction iteration later.**
