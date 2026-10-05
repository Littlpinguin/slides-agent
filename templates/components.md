# Component library

Reusable slide patterns, ready to copy into a new presentation. Each component is a paste-and-adapt block: the structural HTML + the scoped CSS it needs. **Never modify positions, paddings, or animations** — only the textual content. The system was tuned across many iterations and the values are load-bearing.

> All components assume the brand tokens from `brand/tokens.css` are already in `:root`.

## How to use

1. Copy `templates/base.html` to `presentations/<your-deck>.html`.
2. Inline `brand/tokens.css` into the `:root { ... }` block. It carries the label-register tokens (chrome and eyebrow contrast) and the [brand pattern hooks](#brand-pattern-hooks).
3. Embed your logo `<symbol id="brand-logo">` (replace the placeholder in base.html).
4. For each slide you want, copy the matching component block from `templates/components/` (or from this catalogue) into the `<main class="stage">` body, between the existing `<section class="slide">` blocks.
5. Update `data-eyebrow` and `data-heading` on every slide — they drive the overview panel.
6. Run `python scripts/qa.py presentations/<your-deck>.html` after every meaningful change.

## Selection guide — which component for which beat

The deck is a sparkline of emotional beats (Duarte / Reynolds). Pick components that match the beat, not just the data.

| Narrative beat | Component | When to use |
|---|---|---|
| Opening hook | `hero` | Slide 1. One huge number, one tagline. Sets ambition. |
| Pause / breath | `silence` | Every 4–5 slides. One huge number + one short phrase. Resets the eye. |
| Provocation / quote | `bigquote` | Pull quote, full-screen, dark slide. Used once or twice in a deck. |
| Section opener | `section-head` | Eyebrow + display headline + lede. Marks a chapter boundary. |
| Person in focus | `solo` | Portrait left, content right. Founders, key personas. |
| Asymmetric framing | `origin-grid` | Text left, big number right. The classic "X% of Y" slide. |
| Visualised population | `dot-grid` | A grid of dots with one highlighted — the "us amongst the rest" slide. |
| Process / pipeline | `pipeline` | SVG flow diagram with animated path. End-to-end process explanations. |
| Tool stack | `stack-grid` | 6 cells with logos + cost. Show what powers the system. |
| Funnel | `funnel` | 5 stages with bars. Conversion narratives. |
| Lead magnets / artefacts | `leadmags` | 3 mock book/asset covers. The deliverables slide. |
| KPI strata | `kpi-strata` | 3 horizontal bands of metrics. Layered ambitions. |
| Roadmap | `roadmap` | Timeline with phases. Milestone narratives. |
| Budget | `budget-grid` | 2 cards (one-shot vs recurring). Money slide. |
| Engagement / ask | `engage-stage` | Big number left + list right. Time/effort/expectation. |
| Date hero | `date-hero` | The launch date, huge. Ceremony. |
| Decision | `decision-stage` | "Go or no-go?" + meta. Final slide. |
| Person in focus | `solo` | One associate / persona, portrait + content. |
| Calendar / cadence | `cadence-grid` | Visual calendar of months / blocks. |
| Architecture timeline | `chapters` | 4 columns + horizontal timeline. |
| Lead magnets / artefacts | `leadmags` | 3 mock book covers. The deliverables. |
| KPI strata | `kpi-strata` | 3 horizontal bands of stacked metrics. |
| Engagement / ask | `engage-stage` | Big number left + obligations list right. |
| Numbered process | `process-flow` | 1→2→3→4 steps with arrow connectors + synthesis banner. The "how it works" slide. |
| Competitive matrix | `comparison-table` | You vs A vs B, yes/no cells, your column highlighted. The differentiation slide. |
| Dense feature set | `item-wall` | Grid of small icon + label cards + an "and more" highlight card. The "everything we cover" slide. |
| Roadmap board | `kanban-board` | In-progress / Up-next columns, cards with tag + progress bar. The "where we are" slide. |
| Pricing / offer | `pricing` | 2–3 anchored tiers + one "recommended" highlight, or an offer card (year 1 / year 2). The money slide. |
| Vision schema | `three-step` | A → B → C with arrows, highlighted middle box. The "our model" slide. |
| Team | `team-grid` | Round photos / initials + name + role, 3 columns. The "who we are" slide. |
| A photo as evidence | `plate` | One small photo in a large empty field, caption in the margin. A pause after a dense slide. |
| Comparison by images | `diptych` | Two photos, same ratio and height, one shared sentence. Before / after, here / there. |
| A place, a mood | `letterbox-band` | Panoramic 3:1 band at the top, headline and two columns below. Lighter than `fullbleed`. |
| Text-led proof | `margin-figure` | The argument in the lead, a small photo in the margin as a sidenote. |
| Site visit | `field-notes` | Metadata block + photo of the place. Audits and immersions, in series. |
| Material, craft | `scale-contrast` | One large photo and one close-up of its texture. |
| A pattern | `typology-grid` | Eight photos of the same kind of subject in a strict grid. |
| A gesture, a process | `sequence-strip` | Five frames in a row, read as time. |
| Photo credits | `photo-credits` | Last slide of any deck with Pexels photos, generated by `scripts/pexels.py credits`. |

A 24-slide deck typically uses 12–16 components, with 3–4 `silence` slides interleaved.

Every illustrative mark in these components is an **inline Lucide-style SVG** (`stroke: currentColor`), never an emoji. See [Iconography](#iconography) for the rule and the reusable pastille pattern.

Accent-coloured text under 24px (tags, step numbers, column heads, links) takes the label-register accent `--label-accent`, and small grey labels take `opacity: var(--chrome-opacity)`: both are tuned in `brand/tokens.css` to hold WCAG 4.5:1 on the light slide variants, whatever the palette. `--brand-primary-deep` is not: with a light primary (a cyan, a yellow) it falls under 4.5:1 on `--brand-neutral-light` and under 3:1 on a `--brand-primary-soft` tint, so it stays for icons and rules. On a dark card (`--brand-neutral-dark-soft`) use `--brand-secondary`; `--label-accent-dark` is tuned for text set directly on `--brand-neutral-dark`.

## Brand pattern hooks

Optional decoration that carries the brand's own motif: a watermark, a corner motif, an ornamental rule. The engine ships it inert. `--brand-pattern`, `--brand-pattern-light` and `--corner-motif` default to `none` in `brand/tokens.css`, so the classes below draw nothing until the brand provides a motif (onboarding Step 3 in `CLAUDE.md`). A pattern is the brand's or nothing: never stand in a generic decoration.

| Class | Put it on | Draws | Tokens |
|---|---|---|---|
| `.texture` | a light `.slide` | full-slide watermark | `--brand-pattern`, `--pattern-opacity` (0.05) |
| `.motif` | a `.slide.dark` | full-slide watermark, light stroke | `--brand-pattern-light`, `--pattern-opacity-dark` (0.07) |
| `.corner` | a light editorial or decision `.slide` | motif in the top-right corner, 250×250px | `--corner-motif`, `--corner-opacity` (0.09) |
| `.filet-orn` | any block | hairline, brand mark, hairline | `currentColor`: `--brand-primary-deep`, `--brand-secondary` on dark |

```html
<section class="slide texture" data-eyebrow="..." data-heading="...">     <!-- hero on a light slide -->
<section class="slide dark motif" data-eyebrow="..." data-heading="...">  <!-- cover or section opener on a dark slide -->
<section class="slide corner" data-eyebrow="..." data-heading="...">      <!-- editorial or decision slide -->

<div class="filet-orn reveal"><svg viewBox="0 0 100 50"><use href="#brand-logo"/></svg></div>
```

The CSS lives in `templates/base.html` (section "BRAND PATTERN"); nothing to paste.

- **One per slide.** `.motif`, `.texture` and `.corner` share the slide's `::before`: a slide takes one of them.
- **Watermark the heroes**, not every slide: cover, section openers, decision. A motif on every slide stops being a signature. The starter wires `.texture` on its hero and `.corner` on its decision slide, so a brand that sets its motif sees it at once.
- **Under everything.** The class isolates the slide and draws the motif at `z-index: -1`: above the slide background, below text, `.slide-bg` and the chrome. Don't raise it.
- **Faint.** Keep the opacities between 0.04 and 0.10. QA measures text contrast against the slide background, not against the motif, so a louder watermark would erode legibility without any finding.
- **An image, not a gradient.** The tokens take an SVG data URI (the deck stays one file) or a path relative to the deck (`../assets/...`). A CSS gradient bands in the PDF export. For a tiling motif instead of a full-bleed one, override in the deck: `.slide.texture::before { background-size: 240px; background-repeat: repeat; }`.
- **`.filet-orn`** sets its SVG 22px high and keeps the symbol's ratio. Use it above a quote, a breathing number or a closing line, not as a divider on every slide.

## Components

### `hero`

The opening slide. Big number + tagline + breathing animation.

```html
<section class="slide" data-eyebrow="introduction" data-heading="Hero">
  <div class="chrome"><!-- chrome rows from base.html --></div>
  <div class="hero">
    <span class="eyebrow reveal">your eyebrow</span>
    <span class="hero-num gradient-text reveal">78<span class="pct">%</span></span>
    <h2 class="hero-tag reveal">Your one-line tagline lives here.</h2>
    <div class="hero-meta reveal" data-stagger>
      <div><strong>label</strong>value</div>
      <div><strong>label</strong>value</div>
    </div>
  </div>
</section>
```

```css
.hero { display:flex; flex-direction:column; justify-content:center; gap:48px; height:100%; }
.hero-num { font-size:380px; font-weight:200; line-height:1; }
.hero-num .pct { font-size:0.45em; vertical-align:top; }
.hero-tag { font-size:48px; font-weight:300; max-width:1200px; line-height:1.2; }
.hero-meta { display:flex; gap:80px; font-family:var(--font-mono); font-size:13px; letter-spacing:0.06em; }
.hero-meta strong { display:block; font-family:var(--font-display); font-size:18px; font-weight:500; margin-bottom:4px; }
```

> **Add `.hero-num` to `GRADIENT_TEXT_SELECTORS`** in base.html so it rasterises cleanly in PDF.

---

### `silence` — breathing slide

One huge number, one short phrase. No chrome activity, no animations beyond reveal. Use 3–4 per 24-slide deck.

```html
<section class="slide dark" data-eyebrow="breathing" data-heading="Big number">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="silence">
    <span class="silence-num gradient-text reveal">47</span>
    <p class="silence-tag reveal">A short sentence that anchors this number.</p>
  </div>
</section>
```

```css
.silence { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:48px; height:100%; text-align:center; }
.silence-num { font-size:340px; font-weight:200; line-height:1; }
.silence-tag { font-size:32px; font-weight:300; max-width:900px; opacity:0.85; }
```

> **Add `.silence-num`** to `GRADIENT_TEXT_SELECTORS` if it uses `gradient-text`.

---

### `bigquote` — pull-quote

Editorial pull-quote, full-screen dark, italic display.

```html
<section class="slide dark" data-eyebrow="quote" data-heading="Pull quote">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="bigquote">
    <p class="bigquote-text reveal">
      A short, sharp quote that frames <em>the entire deck</em> in a single sentence.
    </p>
    <span class="bigquote-attrib reveal">— Source, role, year</span>
  </div>
</section>
```

```css
.bigquote { display:flex; flex-direction:column; justify-content:center; gap:48px; height:100%; max-width:1500px; }
.bigquote-text { font-size:132px; font-weight:200; line-height:1.1; letter-spacing:-0.025em; }
.bigquote-text em { font-weight:300; font-style:italic; color:var(--brand-secondary); }
.bigquote-attrib { font-family:var(--font-mono); font-size:14px; letter-spacing:0.08em; opacity:0.6; }
```

---

### `section-head`

Chapter boundary: eyebrow + big headline + lede.

```html
<section class="slide" data-eyebrow="01 · chapter" data-heading="Section title">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head">
    <span class="eyebrow reveal">01 · chapter</span>
    <h1 class="display reveal">A clear, declarative headline<br>that names the chapter.</h1>
    <p class="lede reveal">A one-sentence subtitle that frames what follows.</p>
  </div>
</section>
```

```css
.section-head { display:flex; flex-direction:column; justify-content:center; gap:32px; height:100%; max-width:1400px; }
```

---

### `origin-grid` — asymmetric text + big number

Text on the left, number on the right. The "explainer" pattern.

```html
<section class="slide" data-eyebrow="context" data-heading="Origin">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="origin-grid">
    <div class="origin-text reveal">
      <span class="eyebrow">why this number</span>
      <h2>Where the number comes from, in two sentences. Keep it tight.</h2>
      <p class="lede">Optional supporting line, in lighter weight.</p>
    </div>
    <div class="origin-num-pct reveal">
      <span class="num gradient-text">78</span>
      <span class="pct gradient-text">%</span>
    </div>
  </div>
</section>
```

```css
.origin-grid { display:grid; grid-template-columns: 1fr 1fr; gap:120px; align-items:center; height:100%; }
.origin-text { display:flex; flex-direction:column; gap:24px; }
.origin-text h2 { font-size:48px; font-weight:300; line-height:1.25; max-width:560px; }
.origin-num-pct { display:flex; align-items:flex-start; justify-content:center; }
.origin-num-pct .num { font-size:480px; font-weight:200; line-height:0.9; }
.origin-num-pct .pct { font-size:160px; font-weight:200; margin-top:48px; }
```

---

### `dot-grid` — visualised population

200 dots, one highlighted. Use for "1 amongst many" framing.

```html
<section class="slide" data-eyebrow="market" data-heading="Saturation">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="saturation">
    <div class="dot-grid">
      <!-- Repeat 199 dots + 1 .us. JS or hand-write. -->
      <span class="d"></span><span class="d"></span><!-- ... -->
      <span class="d us"></span>
      <!-- ... -->
    </div>
    <div class="saturation-cap reveal">
      <span class="big">1<span class="gradient-text gold-num"> / 200</span></span>
      <p>What the highlighted one represents.</p>
    </div>
  </div>
</section>
```

```css
.saturation { display:grid; grid-template-columns: 1fr 1fr; gap:80px; align-items:center; height:100%; }
.dot-grid { display:grid; grid-template-columns: repeat(20, 1fr); gap:14px; }
.dot-grid .d { width:14px; height:14px; border-radius:50%; background:var(--brand-neutral-dark); opacity:0.18; }
.dot-grid .d.us { background:var(--brand-secondary); opacity:1; box-shadow:0 0 24px var(--brand-secondary-soft); animation:pulseGlow 3s ease-in-out infinite; }
@keyframes pulseGlow { 0%,100% { transform:scale(1); } 50% { transform:scale(1.4); } }
.saturation-cap { display:flex; flex-direction:column; gap:24px; }
.saturation-cap .big { font-size:120px; font-weight:200; }
```

---

### `pipeline` — animated flow

End-to-end process diagram with an animated SVG path. Use for "input → AI → output" stories.

```html
<section class="slide" data-eyebrow="process" data-heading="Pipeline">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">how the pipeline works</span>
    <h1 class="display">Input. Transformation. Output.</h1>
  </div>
  <div class="pipeline-stage reveal">
    <svg class="pipeline-svg" viewBox="0 0 1600 200">
      <path class="pipeline-anim" d="M40,100 L1560,100" stroke="url(#brand-grad)" stroke-width="2" fill="none" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
      <!-- nodes: -->
      <circle cx="40" cy="100" r="14" fill="var(--brand-primary)"/>
      <circle cx="800" cy="100" r="14" fill="var(--brand-primary)"/>
      <circle cx="1560" cy="100" r="14" fill="var(--brand-secondary)"/>
    </svg>
    <div class="pipeline-labels" data-stagger>
      <div>Input</div>
      <div>Transform</div>
      <div>Output</div>
    </div>
  </div>
</section>
```

```css
.pipeline-stage { margin-top:80px; }
.pipeline-svg { width:100%; height:200px; }
.pipeline-anim { animation: drawIn 1.8s cubic-bezier(0.16,1,0.3,1) 0.3s forwards; }
@keyframes drawIn { to { stroke-dashoffset: 0; } }
.pipeline-labels { display:flex; justify-content:space-between; margin-top:24px; font-family:var(--font-mono); font-size:13px; letter-spacing:0.08em; }
```

> Add `body.printing-pdf .pipeline-anim { stroke-dashoffset: 0 !important; animation: none !important; }` to the print block — animations don't run in PDF.

---

### `stack-grid` — tools / technologies

6 cells in a 3×2 grid, each with a logo + label + cost. Plus a total bar.

```html
<section class="slide" data-eyebrow="stack" data-heading="Tool stack">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">what powers the system</span>
    <h1 class="display">Six tools. <span class="gradient-text">€your-total</span> per month.</h1>
  </div>
  <div class="stack-grid" data-stagger>
    <div class="stack-cell"><img class="stack-icon" src="../assets/logos/tool-1.svg" alt=""><strong>Tool 1</strong><span>€xx / mo</span></div>
    <div class="stack-cell"><img class="stack-icon" src="../assets/logos/tool-2.svg" alt=""><strong>Tool 2</strong><span>€xx / mo</span></div>
    <!-- 4 more -->
  </div>
  <div class="stack-total-bar reveal">
    <span>monthly recurring</span>
    <span class="stack-total-num gradient-text">€your-total</span>
  </div>
</section>
```

```css
.stack-grid { display:grid; grid-template-columns: repeat(3, 1fr); gap:24px; margin-top:48px; }
.stack-cell { background:var(--brand-neutral-light-soft); border:1px solid var(--rule); border-radius:8px; padding:24px; display:flex; flex-direction:column; gap:12px; aspect-ratio:1.4; }
.stack-icon { width:40px; height:40px; }
.stack-cell strong { font-size:18px; font-weight:500; }
.stack-cell span { font-family:var(--font-mono); font-size:12px; opacity:0.6; margin-top:auto; }
.stack-total-bar { display:flex; justify-content:space-between; align-items:baseline; padding:24px 0; border-top:1px solid var(--rule); margin-top:32px; }
.stack-total-num { font-size:64px; font-weight:200; }
```

---

### `funnel` — 5-stage conversion bars

```html
<section class="slide" data-eyebrow="funnel" data-heading="Conversion">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">the funnel</span>
    <h1 class="display">From reach to signed contract.</h1>
  </div>
  <div class="funnel" data-stagger>
    <div class="funnel-row"><span>Reach</span><div class="funnel-bar" style="--width:1"></div><span>10,000</span></div>
    <div class="funnel-row"><span>Engaged</span><div class="funnel-bar" style="--width:0.6"></div><span>6,000</span></div>
    <div class="funnel-row"><span>Lead</span><div class="funnel-bar" style="--width:0.25"></div><span>2,500</span></div>
    <div class="funnel-row"><span>MQL</span><div class="funnel-bar" style="--width:0.08"></div><span>800</span></div>
    <div class="funnel-row"><span>Closed</span><div class="funnel-bar" style="--width:0.015"></div><span>150</span></div>
  </div>
</section>
```

```css
.funnel { display:flex; flex-direction:column; gap:18px; margin-top:48px; }
.funnel-row { display:grid; grid-template-columns:160px 1fr 120px; gap:24px; align-items:center; font-family:var(--font-mono); font-size:13px; }
.funnel-bar { height:36px; background:var(--rule); border-radius:4px; position:relative; overflow:hidden; }
.funnel-bar::before { content:''; position:absolute; inset:0; background:var(--brand-gradient); transform-origin:left; transform: scaleX(var(--width, 1)); transition: transform 1.4s cubic-bezier(0.16,1,0.3,1); }
```

---

### `roadmap` — phased timeline

```html
<section class="slide" data-eyebrow="roadmap" data-heading="Plan">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">timeline</span>
    <h1 class="display">12 weeks, five phases.</h1>
  </div>
  <div class="roadmap reveal">
    <div class="roadmap-track"></div>
    <div class="roadmap-phases" data-stagger>
      <div class="roadmap-phase"><strong>W1–2</strong><span>Discovery</span></div>
      <div class="roadmap-phase"><strong>W3–4</strong><span>Design</span></div>
      <div class="roadmap-phase"><strong>W5–8</strong><span>Build</span></div>
      <div class="roadmap-phase"><strong>W9–10</strong><span>Test</span></div>
      <div class="roadmap-phase"><strong>W11–12</strong><span>Launch</span></div>
    </div>
  </div>
</section>
```

```css
.roadmap { position:relative; margin-top:80px; padding:48px 0; }
.roadmap-track { position:absolute; top:50%; left:0; right:0; height:2px; background:var(--rule); }
.roadmap-track::before { content:''; position:absolute; inset:0; background:var(--brand-gradient); transform-origin:left; transform:scaleX(0); animation:trackFill 2.5s cubic-bezier(0.16,1,0.3,1) 0.3s forwards; }
@keyframes trackFill { to { transform:scaleX(1); } }
.roadmap-phases { display:flex; justify-content:space-between; position:relative; }
.roadmap-phase { display:flex; flex-direction:column; align-items:center; gap:8px; position:relative; padding-top:36px; }
.roadmap-phase::before { content:''; position:absolute; top:-6px; width:14px; height:14px; border-radius:50%; background:var(--brand-secondary); transform:scale(0); animation:dotPop 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) 1.5s forwards; }
@keyframes dotPop { to { transform:scale(1); } }
.roadmap-phase strong { font-family:var(--font-mono); font-size:13px; }
.roadmap-phase span { font-size:14px; opacity:0.8; }
```

> Add to print overrides: `.roadmap-track::before { transform:scaleX(1) !important; }` and `.roadmap-phase::before { transform:scale(1) !important; }`.

---

### `budget-grid` — 2 cards, one-shot vs recurring

```html
<section class="slide" data-eyebrow="budget" data-heading="Money">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">investment</span>
    <h1 class="display">What it costs.</h1>
  </div>
  <div class="budget-grid" data-stagger>
    <div class="budget-block">
      <span class="eyebrow">one-shot</span>
      <span class="budget-num">€xx,xxx</span>
      <ul class="budget-list">
        <li>Discovery + design</li>
        <li>Build</li>
        <li>Launch</li>
      </ul>
    </div>
    <div class="budget-block dark">
      <span class="eyebrow">recurring monthly</span>
      <span class="budget-num gradient-text">€x,xxx</span>
      <ul class="budget-list">
        <li>Hosting + tools</li>
        <li>Maintenance</li>
        <li>Iteration</li>
      </ul>
    </div>
  </div>
</section>
```

```css
.budget-grid { display:grid; grid-template-columns:1fr 1fr; gap:32px; margin-top:48px; }
.budget-block { padding:48px; border:1px solid var(--rule); border-radius:8px; display:flex; flex-direction:column; gap:24px; }
.budget-block.dark { background:var(--brand-neutral-dark); color:var(--brand-neutral-light); border:none; }
.budget-num { font-size:96px; font-weight:200; line-height:1; }
.budget-list { list-style:none; font-family:var(--font-mono); font-size:13px; line-height:1.8; opacity:0.7; }
```

---

### `decision-stage` — final slide

The "Go or no-go?" closer.

```html
<section class="slide" data-eyebrow="decision" data-heading="Go or no-go">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="decision-stage">
    <span class="eyebrow reveal">final question</span>
    <h1 class="decision-q reveal"><span class="go gradient-text">Go</span> or <span class="nogo">no-go</span>?</h1>
    <div class="decision-meta reveal" data-stagger>
      <div><strong>budget</strong>your number</div>
      <div><strong>timeline</strong>your timeline</div>
      <div><strong>owner</strong>your name</div>
      <div><strong>start date</strong>YYYY-MM-DD</div>
    </div>
  </div>
</section>
```

```css
.decision-stage { display:flex; flex-direction:column; justify-content:center; gap:48px; height:100%; }
.decision-q { font-size:240px; font-weight:200; line-height:1; letter-spacing:-0.025em; }
.decision-q .nogo { opacity:0.4; }
.decision-meta { display:flex; gap:80px; font-family:var(--font-mono); font-size:13px; }
.decision-meta strong { display:block; font-family:var(--font-display); font-size:18px; font-weight:500; margin-bottom:4px; }
```

> Add `.decision-q .go` to `GRADIENT_TEXT_SELECTORS`.

---

### `solo` — person in focus

Portrait left, content right. For founders, key personas, named decision-makers.

```html
<section class="slide" data-eyebrow="associate" data-heading="Person name">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="solo">
    <div class="solo-portrait reveal">
      <img src="../assets/illustrations/portrait-name.svg" alt="">
    </div>
    <div class="solo-content">
      <span class="eyebrow reveal">role</span>
      <h2 class="solo-name reveal">First Last</h2>
      <p class="solo-territory reveal">Their territory in two short lines. What they own. What they bring.</p>
      <ul class="solo-tags reveal" data-stagger>
        <li>Tag one</li>
        <li>Tag two</li>
        <li>Tag three</li>
      </ul>
    </div>
  </div>
</section>
```

```css
.solo { display:grid; grid-template-columns: 480px 1fr; gap:96px; align-items:center; height:100%; }
.solo-portrait img { width:100%; height:auto; max-height:640px; object-fit:contain; }
.solo-content { display:flex; flex-direction:column; gap:24px; max-width:880px; }
.solo-name { font-size:88px; font-weight:200; line-height:1.05; letter-spacing:-0.025em; }
.solo-territory { font-size:22px; font-weight:300; line-height:1.4; opacity:0.85; }
.solo-tags { list-style:none; display:flex; flex-wrap:wrap; gap:8px; margin-top:16px; }
.solo-tags li { font-family:var(--font-mono); font-size:12px; padding:6px 12px; border:1px solid var(--rule); border-radius:var(--radius-pill); }
```

---

### `cadence-grid` — calendar / cadence visual

A visual rhythm chart (months × blocks per month) with stats on the right.

```html
<section class="slide" data-eyebrow="cadence" data-heading="Production rhythm">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">cadence</span>
    <h1 class="display">One month of output, visualised.</h1>
  </div>
  <div class="cadence-grid reveal">
    <div class="cadence-months" data-stagger>
      <!-- repeat per month -->
      <div class="cadence-month">
        <span class="cadence-month-label">Jan</span>
        <div class="cadence-blocks">
          <span class="b filled"></span><span class="b filled"></span>
          <span class="b filled"></span><span class="b"></span>
        </div>
      </div>
      <!-- ... 7 more -->
    </div>
    <div class="cadence-stats" data-stagger>
      <div><strong>32</strong><span>units / month</span></div>
      <div><strong>4×</strong><span>per week</span></div>
      <div><strong>8 mo</strong><span>steady state</span></div>
    </div>
  </div>
</section>
```

```css
.cadence-grid { display:grid; grid-template-columns: 1fr 280px; gap:80px; margin-top:48px; }
.cadence-months { display:grid; grid-template-columns: repeat(8, 1fr); gap:12px; }
.cadence-month { display:flex; flex-direction:column; gap:8px; }
.cadence-month-label { font-family:var(--font-mono); font-size:11px; opacity:0.6; }
.cadence-blocks { display:grid; grid-template-columns: repeat(2, 1fr); gap:4px; }
.cadence-blocks .b { aspect-ratio:1; background:var(--rule); border-radius:2px; }
.cadence-blocks .b.filled { background:var(--brand-primary); }
.cadence-stats { display:flex; flex-direction:column; gap:24px; padding-left:32px; border-left:1px solid var(--rule); }
.cadence-stats strong { display:block; font-size:48px; font-weight:200; line-height:1; }
.cadence-stats span { font-family:var(--font-mono); font-size:12px; opacity:0.6; }
```

---

### `chapters` — 4-column timeline

Four phases on a horizontal timeline. Used for "the seasons of the project" or "the chapters of a podcast season".

```html
<section class="slide" data-eyebrow="architecture" data-heading="Chapters">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">structure</span>
    <h1 class="display">Four chapters. One arc.</h1>
  </div>
  <div class="chapters reveal" data-stagger>
    <div class="chapter">
      <span class="chapter-num">01</span>
      <h3>Chapter title</h3>
      <p>One short line per chapter — what it covers, no more.</p>
    </div>
    <div class="chapter"><span class="chapter-num">02</span><h3>Chapter</h3><p>Line</p></div>
    <div class="chapter"><span class="chapter-num">03</span><h3>Chapter</h3><p>Line</p></div>
    <div class="chapter"><span class="chapter-num">04</span><h3>Chapter</h3><p>Line</p></div>
  </div>
</section>
```

```css
.chapters { display:grid; grid-template-columns: repeat(4, 1fr); gap:32px; margin-top:64px; position:relative; }
.chapters::before { content:''; position:absolute; top:32px; left:0; right:0; height:1px; background:var(--rule); }
.chapter { display:flex; flex-direction:column; gap:16px; padding-top:56px; position:relative; }
.chapter::before { content:''; position:absolute; top:25px; left:0; width:14px; height:14px; border-radius:50%; background:var(--brand-secondary); }
.chapter-num { font-family:var(--font-mono); font-size:11px; letter-spacing:0.10em; opacity:0.6; }
.chapter h3 { font-size:28px; font-weight:400; line-height:1.2; }
.chapter p { font-size:15px; line-height:1.5; opacity:0.75; }
```

---

### `leadmags` — three deliverable covers

Three mock "book" or document covers, used for the artefacts / lead magnets / deliverables slide.

```html
<section class="slide" data-eyebrow="deliverables" data-heading="Lead magnets">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">artefacts</span>
    <h1 class="display">Three deliverables, three audiences.</h1>
  </div>
  <div class="leadmags reveal" data-stagger>
    <div class="leadmag">
      <div class="leadmag-cover" style="background:var(--brand-primary);">
        <span class="leadmag-tag">guide</span>
        <h4>Cover title</h4>
      </div>
      <p class="leadmag-cap">Who it's for, in one short line.</p>
    </div>
    <div class="leadmag">
      <div class="leadmag-cover" style="background:var(--brand-secondary);color:var(--brand-neutral-dark);">
        <span class="leadmag-tag">checklist</span>
        <h4>Cover title</h4>
      </div>
      <p class="leadmag-cap">Audience.</p>
    </div>
    <div class="leadmag">
      <div class="leadmag-cover" style="background:var(--brand-neutral-dark);color:var(--brand-neutral-light);">
        <span class="leadmag-tag">template</span>
        <h4>Cover title</h4>
      </div>
      <p class="leadmag-cap">Audience.</p>
    </div>
  </div>
</section>
```

```css
.leadmags { display:grid; grid-template-columns: repeat(3, 1fr); gap:32px; margin-top:48px; }
.leadmag { display:flex; flex-direction:column; gap:16px; }
.leadmag-cover { aspect-ratio:3/4; padding:32px; display:flex; flex-direction:column; justify-content:space-between; border-radius:6px; color:var(--brand-neutral-light); }
.leadmag-tag { font-family:var(--font-mono); font-size:11px; letter-spacing:0.10em; text-transform:lowercase; opacity:0.7; }
.leadmag h4 { font-size:32px; font-weight:300; line-height:1.15; }
.leadmag-cap { font-size:14px; opacity:0.7; }
```

---

### `kpi-strata` — three stacked KPI bands

Three horizontal layers, each with its own metrics. Use for "influence / reach / conversion" trios.

```html
<section class="slide" data-eyebrow="kpi" data-heading="Targets">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">targets</span>
    <h1 class="display">Three layers, three metrics each.</h1>
  </div>
  <div class="kpi-strata reveal" data-stagger>
    <div class="kpi-layer">
      <span class="kpi-level">Layer 1 · Influence</span>
      <div class="kpi-stats">
        <div><strong>10k</strong><span>followers</span></div>
        <div><strong>+20%</strong><span>quarterly</span></div>
        <div><strong>3</strong><span>publications</span></div>
      </div>
    </div>
    <div class="kpi-layer">
      <span class="kpi-level">Layer 2 · Reach</span>
      <div class="kpi-stats">
        <div><strong>50k</strong><span>monthly</span></div>
        <div><strong>4 min</strong><span>avg session</span></div>
        <div><strong>12</strong><span>countries</span></div>
      </div>
    </div>
    <div class="kpi-layer">
      <span class="kpi-level">Layer 3 · Conversion</span>
      <div class="kpi-stats">
        <div><strong>2.5%</strong><span>signup rate</span></div>
        <div><strong>€xx</strong><span>LTV</span></div>
        <div><strong>×8</strong><span>ROI 12 mo</span></div>
      </div>
    </div>
  </div>
</section>
```

```css
.kpi-strata { display:flex; flex-direction:column; gap:24px; margin-top:48px; }
.kpi-layer { padding:32px; border:1px solid var(--rule); border-radius:6px; display:grid; grid-template-columns: 240px 1fr; gap:48px; align-items:center; }
.kpi-level { font-family:var(--font-mono); font-size:13px; letter-spacing:0.08em; opacity:0.7; }
.kpi-stats { display:grid; grid-template-columns: repeat(3, 1fr); gap:48px; }
.kpi-stats strong { display:block; font-size:48px; font-weight:200; line-height:1; }
.kpi-stats span { font-family:var(--font-mono); font-size:12px; opacity:0.6; }
```

---

### `engage-stage` — big number + obligations list

Used for the "what you commit to" / "what we ask of you" slide. Big number on the left, list of items on the right.

```html
<section class="slide" data-eyebrow="commitment" data-heading="What we need">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="engage-stage">
    <div class="engage-num-wrap reveal">
      <span class="engage-num gradient-text">3 h</span>
      <span class="engage-num-cap">per month</span>
    </div>
    <ul class="engage-list" data-stagger>
      <li class="engage-item"><strong>One recording session</strong><span>90 min, you talk, we capture.</span></li>
      <li class="engage-item"><strong>One review block</strong><span>30 min on edits.</span></li>
      <li class="engage-item"><strong>One social push</strong><span>One post + reshare on launch day.</span></li>
    </ul>
  </div>
</section>
```

```css
.engage-stage { display:grid; grid-template-columns: 1fr 1fr; gap:96px; align-items:center; height:100%; }
.engage-num-wrap { display:flex; flex-direction:column; align-items:flex-start; gap:8px; }
.engage-num { font-size:280px; font-weight:200; line-height:0.95; }
.engage-num-cap { font-family:var(--font-mono); font-size:14px; letter-spacing:0.08em; opacity:0.6; }
.engage-list { list-style:none; display:flex; flex-direction:column; gap:24px; }
.engage-item { padding:24px 0; border-top:1px solid var(--rule); }
.engage-item strong { display:block; font-size:24px; font-weight:500; margin-bottom:6px; }
.engage-item span { font-size:16px; opacity:0.75; }
```

> Add `.engage-num` to `GRADIENT_TEXT_SELECTORS`.

---

### `date-hero` — launch date

Huge date display + context. Used as the penultimate slide before the decision.

```html
<section class="slide dark" data-eyebrow="launch" data-heading="Launch date">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="date-hero">
    <span class="eyebrow reveal">launch</span>
    <div class="date-mega reveal">
      <span class="day gradient-text">21<span class="month">.09</span></span>
      <span class="year">2026</span>
    </div>
    <p class="date-context reveal">A short line of context — why this date, who's expected, what happens.</p>
  </div>
</section>
```

```css
.date-hero { display:flex; flex-direction:column; justify-content:center; gap:48px; height:100%; }
.date-mega { display:flex; align-items:flex-end; gap:32px; }
.date-mega .day { font-size:380px; font-weight:200; line-height:0.9; letter-spacing:-0.025em; }
.date-mega .month { font-size:0.6em; }
.date-mega .year { font-size:96px; font-weight:200; opacity:0.5; padding-bottom:32px; }
.date-context { font-size:22px; max-width:880px; opacity:0.85; }
```

> Add `.date-mega .day` to `GRADIENT_TEXT_SELECTORS`.

---

### `process-flow` — numbered steps with arrows

Four numbered steps (1 → 2 → 3 → 4) joined by arrow connectors, with a synthesis banner underneath. The canonical "here's how it works, end to end" slide.

```html
<section class="slide" data-eyebrow="how it works" data-heading="Process">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">the method</span>
    <h1 class="display">Four steps, one outcome.</h1>
  </div>
  <div class="process-flow reveal" data-stagger>
    <div class="process-step">
      <span class="process-num">1</span>
      <h3>Capture</h3>
      <p>One short line on what happens at this step.</p>
    </div>
    <div class="process-arrow" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>
    </div>
    <div class="process-step">
      <span class="process-num">2</span>
      <h3>Structure</h3>
      <p>One short line on what happens at this step.</p>
    </div>
    <div class="process-arrow" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>
    </div>
    <div class="process-step">
      <span class="process-num">3</span>
      <h3>Review</h3>
      <p>One short line on what happens at this step.</p>
    </div>
    <div class="process-arrow" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>
    </div>
    <div class="process-step">
      <span class="process-num">4</span>
      <h3>Ship</h3>
      <p>One short line on what happens at this step.</p>
    </div>
  </div>
  <div class="process-banner reveal">
    <span>end to end</span>
    <strong>From raw input to published result in a single loop.</strong>
  </div>
</section>
```

```css
.process-flow { display:grid; grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr; gap:24px; align-items:stretch; margin-top:56px; }
.process-step { background:var(--brand-neutral-light-soft); border:1px solid var(--rule); border-radius:8px; padding:32px; display:flex; flex-direction:column; gap:14px; }
.process-num { display:flex; align-items:center; justify-content:center; width:48px; height:48px; border-radius:var(--radius-pill); background:var(--brand-primary-soft); color:var(--label-accent, var(--brand-primary-deep)); font-family:var(--font-mono); font-size:20px; font-weight:500; }
.process-step h3 { font-size:24px; font-weight:500; line-height:1.2; }
.process-step p { font-size:18px; line-height:1.5; opacity:0.75; }
.process-arrow { display:flex; align-items:center; justify-content:center; color:var(--brand-secondary-deep); }
.process-arrow svg { width:36px; height:36px; }
.process-banner { display:flex; align-items:baseline; gap:24px; margin-top:32px; padding:28px 36px; border-radius:8px; background:var(--brand-neutral-dark); color:var(--brand-neutral-light); }
.process-banner span { font-family:var(--font-mono); font-size:13px; letter-spacing:0.08em; opacity:var(--chrome-opacity, 0.7); white-space:nowrap; }
.process-banner strong { font-size:24px; font-weight:300; line-height:1.3; }
```

> On a dark slide, swap `.process-step` to `background:var(--brand-neutral-dark-soft); border-color:var(--rule-light);`, `.process-num` to `color:var(--brand-secondary);` and the banner to `background:var(--brand-neutral-light); color:var(--brand-neutral-dark);` for contrast. The number takes the secondary there: `--label-accent-dark` is tuned against `--brand-neutral-dark`, not against a tinted chip over dark-soft, where it can fall under 4.5:1.

---

### `comparison-table` — you vs A vs B

A competitive matrix: rows of criteria, one "you" column highlighted, the rest neutral. Cells are yes/no marks (inline SVG, never emoji). The classic differentiation slide.

```html
<section class="slide" data-eyebrow="differentiation" data-heading="Comparison">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">how we compare</span>
    <h1 class="display">What only we do.</h1>
  </div>
  <div class="comparison reveal">
    <table class="comparison-table">
      <thead>
        <tr>
          <th scope="col" class="c-criteria">Capability</th>
          <th scope="col" class="c-you">You</th>
          <th scope="col">Competitor A</th>
          <th scope="col">Competitor B</th>
        </tr>
      </thead>
      <tbody data-stagger>
        <tr>
          <th scope="row">Self-hosted &amp; sovereign</th>
          <td class="c-you"><span class="mark yes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span></td>
          <td><span class="mark no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></span></td>
          <td><span class="mark no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></span></td>
        </tr>
        <tr>
          <th scope="row">Flat per-seat pricing</th>
          <td class="c-you"><span class="mark yes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span></td>
          <td><span class="mark yes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span></td>
          <td><span class="mark no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></span></td>
        </tr>
        <tr>
          <th scope="row">No vendor lock-in</th>
          <td class="c-you"><span class="mark yes"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></span></td>
          <td><span class="mark no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></span></td>
          <td><span class="mark no"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
```

```css
.comparison { margin-top:48px; }
.comparison-table { width:100%; border-collapse:collapse; font-size:20px; }
.comparison-table th, .comparison-table td { padding:22px 28px; text-align:center; border-bottom:1px solid var(--rule); }
.comparison-table thead th { font-family:var(--font-mono); font-size:13px; font-weight:500; letter-spacing:0.06em; text-transform:lowercase; opacity:var(--chrome-opacity, 0.7); border-bottom:1px solid var(--brand-neutral-dark); }
.comparison-table .c-criteria, .comparison-table tbody th { text-align:left; font-weight:400; opacity:1; }
.comparison-table tbody th { font-size:20px; }
.comparison-table .c-you { background:var(--brand-primary-soft); }
.comparison-table thead th.c-you { color:var(--label-accent, var(--brand-primary-deep)); opacity:1; font-weight:700; border-bottom:2px solid var(--brand-primary); }
.comparison-table .mark { display:inline-flex; align-items:center; justify-content:center; width:32px; height:32px; border-radius:var(--radius-pill); }
.comparison-table .mark svg { width:20px; height:20px; }
.comparison-table .mark.yes { background:var(--brand-primary-soft); color:var(--brand-primary-deep); }
.comparison-table .mark.no { color:var(--brand-neutral-dark); opacity:0.28; }
```

> On a dark slide, the highlighted column reads better with `.c-you { background:var(--rule-light); }` and marks using `--brand-secondary` tones.

---

### `item-wall` — dense feature grid + "and more"

A wall of small cards, each an inline icon + a short label, ending on a highlighted "and more" card. Use when you need to show breadth (every use case, every integration, every format) without a wall of text.

```html
<section class="slide" data-eyebrow="coverage" data-heading="Item wall">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">what it covers</span>
    <h1 class="display">One tool, every format.</h1>
  </div>
  <div class="item-wall reveal" data-stagger>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/></svg></span>
      <strong>Documents</strong>
    </div>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg></span>
      <strong>Slides</strong>
    </div>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15V6a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v9"/><rect x="3" y="13" width="18" height="8" rx="2"/></svg></span>
      <strong>Tables</strong>
    </div>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m19 9-5 5-4-4-3 3"/></svg></span>
      <strong>Charts</strong>
    </div>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/></svg></span>
      <strong>Images</strong>
    </div>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2"/></svg></span>
      <strong>Video</strong>
    </div>
    <div class="item-card">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></span>
      <strong>Code</strong>
    </div>
    <div class="item-card more">
      <span class="item-ico"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/><circle cx="5" cy="12" r="1"/></svg></span>
      <strong>and more</strong>
    </div>
  </div>
</section>
```

```css
.item-wall { display:grid; grid-template-columns: repeat(4, 1fr); gap:20px; margin-top:48px; }
.item-card { display:flex; align-items:center; gap:18px; padding:24px 28px; background:var(--brand-neutral-light-soft); border:1px solid var(--rule); border-radius:8px; }
.item-ico { display:flex; align-items:center; justify-content:center; width:44px; height:44px; flex:0 0 44px; border-radius:var(--radius-tight); background:var(--brand-primary-soft); color:var(--brand-primary-deep); }
.item-ico svg { width:24px; height:24px; }
.item-card strong { font-size:20px; font-weight:500; }
.item-card.more { background:var(--brand-neutral-dark); border-color:transparent; color:var(--brand-neutral-light); }
.item-card.more .item-ico { background:var(--rule-light); color:var(--brand-secondary); }
```

> Scales to any count — keep `repeat(4, 1fr)` and let rows grow, but cap at 12 cards (3 rows) so the bottom row clears the chrome safe-zone.

---

### `kanban-board` — roadmap board

Two columns ("In progress" / "Up next"), each a stack of cards. Cards carry a tag + title + description; in-progress cards add a progress bar. The "where we are right now" slide.

```html
<section class="slide" data-eyebrow="roadmap" data-heading="Board">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">what's shipping</span>
    <h1 class="display">In progress, and next.</h1>
  </div>
  <div class="kanban reveal" data-stagger>
    <div class="kanban-col">
      <div class="kanban-col-head">
        <span class="kanban-dot in"></span>
        <span>In progress</span>
      </div>
      <div class="kanban-card">
        <span class="kanban-tag">core</span>
        <h4>Self-hosted runtime</h4>
        <p>Single-binary deploy, no external dependencies.</p>
        <div class="kanban-progress"><span style="--p:0.7"></span></div>
      </div>
      <div class="kanban-card">
        <span class="kanban-tag">api</span>
        <h4>Public REST surface</h4>
        <p>Documented endpoints, token auth, rate limits.</p>
        <div class="kanban-progress"><span style="--p:0.4"></span></div>
      </div>
    </div>
    <div class="kanban-col">
      <div class="kanban-col-head">
        <span class="kanban-dot next"></span>
        <span>Up next</span>
      </div>
      <div class="kanban-card">
        <span class="kanban-tag">collab</span>
        <h4>Shared workspaces</h4>
        <p>Teams, roles, and per-project access control.</p>
      </div>
      <div class="kanban-card">
        <span class="kanban-tag">mobile</span>
        <h4>Companion app</h4>
        <p>Review and approve on the move.</p>
      </div>
    </div>
  </div>
</section>
```

```css
.kanban { display:grid; grid-template-columns: 1fr 1fr; gap:32px; margin-top:48px; align-items:start; }
.kanban-col { display:flex; flex-direction:column; gap:18px; }
.kanban-col-head { display:flex; align-items:center; gap:10px; font-family:var(--font-mono); font-size:13px; letter-spacing:0.06em; text-transform:lowercase; opacity:0.7; padding-bottom:6px; border-bottom:1px solid var(--rule); }
.kanban-dot { width:10px; height:10px; border-radius:var(--radius-pill); }
.kanban-dot.in { background:var(--brand-primary); }
.kanban-dot.next { background:var(--brand-secondary); }
.kanban-card { background:var(--brand-neutral-light-soft); border:1px solid var(--rule); border-radius:8px; padding:24px 28px; display:flex; flex-direction:column; gap:10px; }
.kanban-tag { font-family:var(--font-mono); font-size:12px; letter-spacing:0.08em; text-transform:lowercase; color:var(--label-accent, var(--brand-primary-deep)); }
.kanban-card h4 { font-size:22px; font-weight:500; line-height:1.2; }
.kanban-card p { font-size:18px; line-height:1.45; opacity:0.72; }
.kanban-progress { height:6px; border-radius:var(--radius-pill); background:var(--rule); overflow:hidden; margin-top:6px; }
.kanban-progress span { display:block; height:100%; width:calc(var(--p, 0.5) * 100%); background:var(--brand-gradient); border-radius:var(--radius-pill); }
```

> On a dark slide, swap cards to `background:var(--brand-neutral-dark-soft); border-color:var(--rule-light);` and `.kanban-tag` to `color:var(--brand-secondary);` (`--label-accent-dark` is tuned against `--brand-neutral-dark`, not dark-soft). The progress bars use a static fill (no transition), so they need no print override.

---

### `pricing` — anchored tiers + offer card

Two variants. **Variant A**: 2–3 priced tiers side by side, the middle one marked `recommended` and visually lifted. **Variant B**: a single offer card anchoring two amounts (year 1 vs year 2). The money slide.

**Variant A — tiers**

```html
<section class="slide" data-eyebrow="pricing" data-heading="Plans">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">what it costs</span>
    <h1 class="display">Simple, flat pricing.</h1>
  </div>
  <div class="pricing reveal" data-stagger>
    <div class="price-tier">
      <span class="price-name">Free</span>
      <span class="price-amount"><span class="cur">€</span>0</span>
      <span class="price-period">forever</span>
      <ul class="price-list">
        <li>20 AI credits / month</li>
        <li>Single workspace</li>
        <li>Community support</li>
      </ul>
    </div>
    <div class="price-tier featured">
      <span class="price-badge">recommended</span>
      <span class="price-name">Team</span>
      <span class="price-amount"><span class="cur">€</span>50</span>
      <span class="price-period">per seat / year</span>
      <ul class="price-list">
        <li>Unlimited AI credits</li>
        <li>Shared workspaces</li>
        <li>Priority support</li>
      </ul>
    </div>
    <div class="price-tier">
      <span class="price-name">Sovereign</span>
      <span class="price-amount">Custom</span>
      <span class="price-period">self-hosted</span>
      <ul class="price-list">
        <li>On-premise deploy</li>
        <li>SSO &amp; audit logs</li>
        <li>Dedicated SLA</li>
      </ul>
    </div>
  </div>
</section>
```

```css
.pricing { display:grid; grid-template-columns: repeat(3, 1fr); gap:28px; margin-top:48px; align-items:start; }
.price-tier { position:relative; padding:40px 36px; border:1px solid var(--rule); border-radius:10px; display:flex; flex-direction:column; gap:8px; background:var(--brand-neutral-light-soft); }
.price-tier.featured { background:var(--brand-neutral-dark); color:var(--brand-neutral-light); border-color:transparent; padding-top:52px; }
.price-badge { position:absolute; top:24px; right:28px; font-family:var(--font-mono); font-size:11px; letter-spacing:0.08em; text-transform:lowercase; padding:6px 12px; border-radius:var(--radius-pill); background:var(--brand-secondary); color:var(--brand-neutral-dark); }
.price-name { font-family:var(--font-mono); font-size:14px; letter-spacing:0.06em; text-transform:lowercase; opacity:0.7; }
.price-amount { font-size:84px; font-weight:200; line-height:1; }
.price-amount .cur { font-size:0.45em; vertical-align:super; opacity:0.7; }
.price-period { font-family:var(--font-mono); font-size:13px; opacity:0.6; margin-bottom:16px; }
.price-list { list-style:none; display:flex; flex-direction:column; gap:12px; border-top:1px solid var(--rule); padding-top:24px; font-size:18px; }
.price-tier.featured .price-list { border-top-color:var(--rule-light); }
.price-list li { line-height:1.4; opacity:0.85; }
```

**Variant B — offer card (year 1 / year 2)**

```html
<section class="slide" data-eyebrow="offer" data-heading="Offer">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="offer-stage">
    <div class="offer-intro reveal">
      <span class="eyebrow">launch offer</span>
      <h2 class="offer-head">Locked-in pricing for early adopters.</h2>
      <p class="offer-note">Same flat rate for two years. No usage metering, no surprise renewal.</p>
    </div>
    <div class="offer-card reveal">
      <div class="offer-row">
        <span class="offer-row-label">Year 1</span>
        <span class="offer-row-amount gradient-text">€50</span>
        <span class="offer-row-unit">/ seat</span>
      </div>
      <div class="offer-row">
        <span class="offer-row-label">Year 2</span>
        <span class="offer-row-amount">€50</span>
        <span class="offer-row-unit">/ seat</span>
      </div>
      <div class="offer-foot">until 1 Oct 2026</div>
    </div>
  </div>
</section>
```

```css
.offer-stage { display:grid; grid-template-columns: 1fr 1fr; gap:96px; align-items:center; height:100%; }
.offer-intro { display:flex; flex-direction:column; gap:24px; }
.offer-head { font-size:56px; font-weight:300; line-height:1.2; max-width:640px; }
.offer-note { font-size:20px; line-height:1.5; opacity:0.75; max-width:560px; }
.offer-card { padding:48px; border:1px solid var(--rule); border-radius:12px; background:var(--brand-neutral-light-soft); display:flex; flex-direction:column; gap:28px; }
.offer-row { display:flex; align-items:baseline; gap:16px; padding-bottom:24px; border-bottom:1px solid var(--rule); }
.offer-row:nth-of-type(2) { border-bottom:none; padding-bottom:0; }
.offer-row-label { font-family:var(--font-mono); font-size:14px; letter-spacing:0.06em; opacity:0.6; min-width:90px; }
.offer-row-amount { font-size:96px; font-weight:200; line-height:0.9; }
.offer-row-unit { font-family:var(--font-mono); font-size:15px; opacity:0.6; }
.offer-foot { font-family:var(--font-mono); font-size:13px; letter-spacing:0.06em; opacity:0.55; padding-top:8px; }
```

> **Add `.offer-row-amount.gradient-text`** (variant B) to `GRADIENT_TEXT_SELECTORS` in base.html so it rasterises cleanly in PDF. Variant A has no gradient text.

---

### `three-step` — A → B → C schema

Three boxes joined by arrows, the middle one highlighted. Use for a model / mechanism in three moves (input → transformation → outcome, or problem → product → result) where the centre is the load-bearing idea.

```html
<section class="slide" data-eyebrow="model" data-heading="Schema">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">how it works</span>
    <h1 class="display">Three moves, one model.</h1>
  </div>
  <div class="three-step reveal" data-stagger>
    <div class="ts-box">
      <span class="ts-label">A · Input</span>
      <h3>Scattered knowledge</h3>
      <p>Notes, files, and tools that don't talk to each other.</p>
    </div>
    <div class="ts-arrow" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>
    </div>
    <div class="ts-box ts-feature">
      <span class="ts-label">B · Engine</span>
      <h3>One sovereign workspace</h3>
      <p>Everything in one place, on your own infrastructure.</p>
    </div>
    <div class="ts-arrow" aria-hidden="true">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>
    </div>
    <div class="ts-box">
      <span class="ts-label">C · Outcome</span>
      <h3>Work that compounds</h3>
      <p>Reusable, searchable, and owned end to end.</p>
    </div>
  </div>
</section>
```

```css
.three-step { display:grid; grid-template-columns: 1fr auto 1fr auto 1fr; gap:28px; align-items:stretch; margin-top:64px; }
.ts-box { padding:36px 32px; border:1px solid var(--rule); border-radius:10px; background:var(--brand-neutral-light-soft); display:flex; flex-direction:column; gap:14px; }
.ts-box.ts-feature { background:var(--brand-neutral-dark); color:var(--brand-neutral-light); border-color:transparent; box-shadow:0 24px 60px var(--brand-primary-soft); }
.ts-label { font-family:var(--font-mono); font-size:13px; letter-spacing:0.06em; text-transform:lowercase; color:var(--label-accent, var(--brand-primary-deep)); }
.ts-box.ts-feature .ts-label { color:var(--brand-secondary); }
.ts-box h3 { font-size:26px; font-weight:500; line-height:1.2; }
.ts-box p { font-size:18px; line-height:1.5; opacity:0.78; }
.ts-arrow { display:flex; align-items:center; justify-content:center; color:var(--brand-secondary-deep); }
.ts-arrow svg { width:36px; height:36px; }
```

> The shadow on `.ts-feature` is stripped automatically in PDF (the print block removes all shadows). No extra override needed.

---

### `team-grid` — people, 3 columns

Round portraits (or initials when no photo) + name + role, in a 3-column grid. The "who's behind this" slide for founders or a core team.

```html
<section class="slide" data-eyebrow="team" data-heading="Team">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">who we are</span>
    <h1 class="display">The people behind it.</h1>
  </div>
  <div class="team-grid reveal" data-stagger>
    <div class="team-member">
      <div class="team-photo"><img src="../assets/illustrations/portrait-1.jpg" alt=""></div>
      <strong>First Last</strong>
      <span>Co-founder · CEO</span>
    </div>
    <div class="team-member">
      <!-- No photo? Use initials in the same circle. -->
      <div class="team-photo initials">FL</div>
      <strong>First Last</strong>
      <span>Co-founder · CTO</span>
    </div>
    <div class="team-member">
      <div class="team-photo initials">FL</div>
      <strong>First Last</strong>
      <span>Head of Design</span>
    </div>
  </div>
</section>
```

```css
.team-grid { display:grid; grid-template-columns: repeat(3, 1fr); gap:48px; margin-top:56px; }
.team-member { display:flex; flex-direction:column; align-items:center; text-align:center; gap:14px; }
.team-photo { width:180px; height:180px; border-radius:var(--radius-pill); overflow:hidden; border:1px solid var(--rule); }
.team-photo img { width:100%; height:100%; object-fit:cover; display:block; }
.team-photo.initials { display:flex; align-items:center; justify-content:center; background:var(--brand-primary-soft); color:var(--label-accent, var(--brand-primary-deep)); font-family:var(--font-mono); font-size:48px; font-weight:500; }
.team-member strong { font-size:26px; font-weight:500; line-height:1.1; }
.team-member span { font-family:var(--font-mono); font-size:13px; letter-spacing:0.04em; opacity:var(--chrome-opacity, 0.7); }
```

> For 4–6 people, keep `repeat(3, 1fr)` and let it wrap to a second row; drop `.team-photo` to `140px` square so two rows clear the chrome safe-zone.

---

### Iconography

**Never use emoji** (no ☠️, 💡, ✨, ✅, ❌). Every icon in this system is an **inline Lucide-style SVG**: a 24×24 `viewBox`, `fill: none`, `stroke: currentColor`, `stroke-width: 1.75` (use `2` for small marks under ~24px), with `stroke-linecap: round` and `stroke-linejoin: round`. Because the stroke is `currentColor`, the icon inherits the text colour of whatever pastille or context it sits in — so a single markup works on cream and on dark slides without edits.

The reusable unit is a **pastille**: a tokenised rounded container holding one icon. Drop it anywhere — list bullets, stat headers, feature rows.

```html
<section class="slide" data-eyebrow="iconography" data-heading="Icons">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="section-head reveal" style="height:auto;">
    <span class="eyebrow">the rule</span>
    <h1 class="display">Inline strokes, never emoji.</h1>
  </div>
  <div class="ico-demo reveal" data-stagger>
    <div class="ico-item">
      <span class="pastille"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a7 7 0 0 0-7 7c0 2.4 1.2 4 2.5 5.5.7.8 1 1.3 1 2.5h7c0-1.2.3-1.7 1-2.5C18.8 13 20 11.4 20 9a7 7 0 0 0-7-7Z"/><path d="M9 21h6"/></svg></span>
      <strong>Insight</strong>
      <span class="ico-cap">primary pastille</span>
    </div>
    <div class="ico-item">
      <span class="pastille alt"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.7 8.9a1 1 0 0 1-.6 0C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.2-2.7a1 1 0 0 1 1.5 0C14.5 3.8 17 5 19 5a1 1 0 0 1 1 1Z"/></svg></span>
      <strong>Sovereign</strong>
      <span class="ico-cap">secondary pastille</span>
    </div>
    <div class="ico-item">
      <span class="pastille solid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3-1.9 5.8a2 2 0 0 1-1.3 1.3L3 12l5.8 1.9a2 2 0 0 1 1.3 1.3L12 21l1.9-5.8a2 2 0 0 1 1.3-1.3L21 12l-5.8-1.9a2 2 0 0 1-1.3-1.3Z"/></svg></span>
      <strong>Crafted</strong>
      <span class="ico-cap">solid pastille</span>
    </div>
  </div>
</section>
```

```css
.ico-demo { display:grid; grid-template-columns: repeat(3, 1fr); gap:48px; margin-top:56px; }
.ico-item { display:flex; flex-direction:column; align-items:flex-start; gap:14px; }
.ico-item strong { font-size:24px; font-weight:500; }
.ico-cap { font-family:var(--font-mono); font-size:13px; letter-spacing:0.04em; opacity:0.6; }

/* Reusable pastille — copy this anywhere you need an icon chip */
.pastille { display:inline-flex; align-items:center; justify-content:center; width:56px; height:56px; border-radius:var(--radius-tight); background:var(--brand-primary-soft); color:var(--brand-primary-deep); }
.pastille svg { width:28px; height:28px; }
.pastille.alt { background:var(--brand-secondary-soft); color:var(--brand-secondary-deep); }
.pastille.solid { background:var(--brand-primary); color:var(--brand-neutral-light); }
.slide.dark .pastille { background:var(--rule-light); color:var(--brand-secondary); }
```

> **Where to find icons.** Copy any path from [lucide.dev](https://lucide.dev) — the SVGs are already stroked with `currentColor` and 24×24. Strip the wrapping `<svg>` attributes Lucide ships and replace with the canonical set above (`stroke-width:1.75`). Keep `fill="none"`. The pastille (`.pastille`, `.pastille.alt`, `.pastille.solid`) is shared by `process-flow`, `item-wall`, `team-grid` initials, and the yes/no marks in `comparison-table` — reuse it instead of inventing new chips. No icon ever introduces a hard-coded colour: it is always `currentColor` over a tokenised background.

---

### `photo-credits` — the last slide of any deck with Pexels photos

Pexels asks for a visible link to Pexels and credit to its photographers. This slide does both, once, at the very end of the deck (after `cta-final`), so no photo slide carries a credit line. **Don't write it by hand**: generate it from the deck, which reads each photo's sidecar in `assets/photos/`.

```bash
python3 scripts/pexels.py credits presentations/<deck>.html            # English labels
python3 scripts/pexels.py credits presentations/<deck>.html --lang fr  # French labels
```

Paste the printed `<section>` as the last slide. Re-run it whenever a photo is added, swapped or removed; slide numbers come from DOM order. The output looks like this:

```html
<section class="slide" data-eyebrow="photo credits" data-heading="Photo credits">
  <div class="chrome"><!-- chrome rows (generated) --></div>
  <div class="photo-credits">
    <span class="eyebrow reveal">photo credits</span>
    <h2 class="pc-title reveal">Photographs from <a href="https://www.pexels.com">Pexels</a></h2>
    <ol class="pc-list reveal">
      <li><span class="pc-slide">slide 03</span><a class="pc-name" href="https://www.pexels.com/@name">First Last</a><a class="pc-link" href="https://www.pexels.com/photo/…">view on pexels</a></li>
      <li><span class="pc-slide">slides 07, 15</span><a class="pc-name" href="…">First Last</a><a class="pc-link" href="…">view on pexels</a></li>
    </ol>
  </div>
</section>
```

```css
.photo-credits { display:flex; flex-direction:column; justify-content:center; gap:40px; height:100%; max-width:1440px; }
.pc-title { font-size:64px; font-weight:300; line-height:1.1; letter-spacing:-0.02em; }
.pc-title a { color:inherit; text-decoration:underline; text-decoration-thickness:1px; text-underline-offset:0.14em; }
.pc-list { list-style:none; display:grid; grid-template-columns:1fr; column-gap:80px; border-top:1px solid var(--rule); }
.pc-list.pc-list--two { grid-template-columns:1fr 1fr; }
.pc-list li { display:grid; grid-template-columns:170px 1fr auto; align-items:baseline; gap:24px; padding:16px 0; border-bottom:1px solid var(--rule); }
.pc-slide { font-family:var(--font-mono); font-size:16px; letter-spacing:0.06em; opacity:var(--chrome-opacity, 0.7); }
.pc-name { font-size:24px; color:inherit; text-decoration:none; }
.pc-link { font-family:var(--font-mono); font-size:16px; letter-spacing:0.06em; color:var(--label-accent, var(--brand-primary-deep)); text-decoration:none; }
.slide.dark .pc-list, .slide.dark .pc-list li { border-color:var(--rule-light); }
.slide.dark .pc-link { color:var(--brand-secondary); }
```

> Seven or more photos switch the list to two columns (`pc-list--two`, added by the script). Past about fourteen photos the list reaches the chrome safe-zone: that many photos is a dosage problem, not a layout problem (see the `pexels-photos` skill). The links stay clickable in the exported PDF.

---

## Photography layouts

Eight layouts for slides where a real photograph carries the beat, built for the photos the `pexels-photos` skill fetches (or your own in `assets/photos/`). They are executed on real photos in `reference/catalogue-layouts.html` (plates 105–113, family "Photographie"). None of them puts text over a photo: that is the job of `hero` / `cover` and `fullbleed` (`.slide-bg` + veil).

Rules shared by the whole family, from the editorial references behind it (Cereal, Aperture, NYT Magazine, Businessweek, Tufte, the Bechers, Muybridge):

- **Few formats, native ratios.** 3:2, 4:5, 1:1, and 3:1 for bands only. Pick photos whose original ratio is close, so the crop stays honest.
- **One caption grammar per deck.** A mono lowercase label (`pl. 01 · what it shows`), plus an optional sentence, always in the same place relative to the photo. No credit line on the slide: credits live on the last slide (`photo-credits`).
- **One light, one treatment per deck.** Same colour temperature everywhere; `mono` / `duotone` are baked into the file by `scripts/pexels.py --treatment`, never applied with CSS `filter` or `mix-blend-mode` (they break in the PDF export).
- **Crop on purpose.** `object-fit: cover` plus a per-photo `object-position` (e.g. `style="object-position: 30% 60%"`) to keep the focal point; never cut through a face, a joint or the horizon.
- **Alternate weight.** Follow a photo-heavy slide (`letterbox-band`, `diptych`) with a photo-light one (`plate`, `margin-figure`) or a typographic one.

Shared CSS, needed once per deck by any of the eight:

```css
.ph { position:relative; margin:0; overflow:hidden; background:var(--brand-neutral-light-deep); }
.ph img { width:100%; height:100%; object-fit:cover; display:block; }
.pcap { display:block; font-family:var(--font-mono); font-size:14px; letter-spacing:0.08em; text-transform:lowercase; opacity:0.65; }
.psent { font-size:22px; font-weight:300; line-height:1.45; }
```

Every `src` below points at `../assets/photos/pexels-<slug>-<id>.jpg`: replace with the file `pexels.py get` wrote (or its `-mono` / `-duotone` variant), and write the `alt` from the sidecar's `alt`, in the deck's language.

---

### `plate` — one photograph in a large empty field

The photobook plate: a small photo, off-centre, a caption in the margin, no big headline. A pause after a dense slide, when the image itself is the evidence.

```html
<section class="slide" data-eyebrow="plate" data-heading="One photograph">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="plt">
    <div class="plt-txt">
      <p class="plt-state reveal">One short statement, two lines at most.</p>
      <div class="plt-cap reveal">
        <span class="pcap">pl. 01 · what the photo shows</span>
        <p class="psent">Three lines at most: why this image is the evidence.</p>
        <i class="plt-rule"></i>
      </div>
    </div>
    <figure class="ph plt-ph reveal"><img src="../assets/photos/pexels-slug-1234567.jpg" alt=""></figure>
  </div>
</section>
```

```css
.plt { height:100%; display:grid; grid-template-columns:544px 166px 560px 1fr; align-items:center; }
.plt-txt { align-self:stretch; display:flex; flex-direction:column; justify-content:space-between; padding:95px 0; }
.plt-state { font-size:48px; font-weight:300; line-height:1.15; letter-spacing:-0.01em; }
.plt-cap { display:flex; flex-direction:column; gap:16px; }
.plt-rule { display:block; width:64px; height:1px; background:currentColor; opacity:0.35; }
.plt-ph { grid-column:3; width:560px; height:700px; }
```

> Below ~12% of the frame, or dead centre, the plate reads as unfinished. It needs a simple subject on a calm ground: busy wide shots die at this size. For a landscape photo, use `width:828px; height:552px` and `grid-template-columns:544px 166px 828px 1fr`.

---

### `diptych` — two photos, one meaning

Same ratio, same height, a narrow gutter, one shared sentence. Before / after, here / there, problem / aspiration: comparison without a chart.

```html
<section class="slide" data-eyebrow="diptych" data-heading="Two images">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="dip">
    <div class="dip-head">
      <span class="eyebrow reveal">two images, one question</span>
      <h2 class="dip-title reveal">The pair says what neither photo says alone.</h2>
    </div>
    <div class="dip-pair reveal">
      <div class="dip-it"><figure class="ph"><img src="../assets/photos/pexels-slug-a-1234567.jpg" alt=""></figure><span class="pcap">a · first term</span></div>
      <div class="dip-it"><figure class="ph"><img src="../assets/photos/pexels-slug-b-7654321.jpg" alt=""></figure><span class="pcap">b · second term</span></div>
    </div>
    <p class="psent dip-sent reveal">One sentence for the pair, never one per photo.</p>
  </div>
</section>
```

```css
.dip { height:100%; display:flex; flex-direction:column; justify-content:center; gap:36px; }
.dip-title { margin-top:14px; font-size:56px; font-weight:300; line-height:1.12; letter-spacing:-0.015em; }
.dip-pair { display:grid; grid-template-columns:1fr 1fr; gap:24px; }
.dip-it { display:flex; flex-direction:column; gap:12px; }
.dip-it .ph { aspect-ratio:3/2; }
.dip-sent { max-width:1000px; }
```

> Match tone before subject: two photos with different colour temperatures read as a mistake. Align horizons or eye lines at the same height. Never a third photo.

---

### `letterbox-band` — a panoramic band, text below

A cinematic 3:1 band across the top of the slide, nothing written on it; headline and two short columns underneath. A place or a mood when the veiled `fullbleed` would be too heavy, or the message needs more than one line.

```html
<section class="slide band-top" data-eyebrow="place" data-heading="The place">
  <figure class="ph band-ph" data-bleed><img src="../assets/photos/pexels-slug-1234567.jpg" alt=""></figure>
  <div class="chrome"><!-- chrome rows --></div>
  <span class="pcap band-cap">what the band shows</span>
  <div class="band-body">
    <h2 class="band-title reveal">A place reads better in width.</h2>
    <div class="band-cols reveal">
      <p>First short column, three lines at most.</p>
      <p>Second short column, three lines at most.</p>
    </div>
  </div>
</section>
```

```css
.band-ph { position:absolute; top:0; left:0; width:1920px; height:580px; z-index:0; }
.band-ph::after { content:""; position:absolute; inset:0 0 auto; height:140px; background:linear-gradient(180deg, color-mix(in srgb, var(--brand-neutral-dark) 45%, transparent), transparent); }
.slide.band-top .chrome-row.top { color:var(--brand-neutral-light); }
.slide.band-top .chrome-row.top .meta-label, .slide.band-top .chrome-row.top .nav-num { color:var(--brand-neutral-light); opacity:0.9; }
.band-cap { position:absolute; top:596px; right:120px; }
.band-body { position:absolute; top:650px; left:120px; right:120px; display:grid; grid-template-columns:6fr 1fr 5fr; align-items:start; }
.band-title { font-size:64px; font-weight:300; line-height:1.12; letter-spacing:-0.015em; }
.band-cols { grid-column:3; display:grid; grid-template-columns:1fr 1fr; gap:32px; padding-top:10px; font-size:20px; line-height:1.5; }
```

> `data-bleed` tells `qa.py` the band runs to the frame edge on purpose; never put it on the text. A 3:1 crop keeps half the height of a 3:2 original: download at `--width 3000` or more, and avoid tall subjects and faces. The top gradient only protects the chrome row; if the photo is very bright at the top, pick another photo rather than darkening it further.

---

### `margin-figure` — text leads, a photo in the margin

Tufte's sidenote, applied to a photograph: the argument is written, a small real-world trace makes it credible.

```html
<section class="slide" data-eyebrow="finding" data-heading="What teams say">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="mfig">
    <div class="mfig-lead">
      <span class="eyebrow reveal">what teams say</span>
      <p class="mfig-text reveal">The argument, in five lines at most. This is where the slide is read.</p>
    </div>
    <i class="mfig-rule"></i>
    <div class="mfig-side reveal">
      <span class="pcap">fig. 1 · what the photo shows</span>
      <figure class="ph"><img src="../assets/photos/pexels-slug-1234567.jpg" alt=""></figure>
      <p class="psent">Two lines at most.</p>
    </div>
  </div>
</section>
```

```css
.mfig { height:100%; display:grid; grid-template-columns:970px 1fr 1px 1fr 380px; align-items:center; }
.mfig-text { margin-top:18px; font-size:40px; font-weight:300; line-height:1.35; letter-spacing:-0.01em; }
.mfig-rule { grid-column:3; align-self:stretch; margin:80px 0; background:var(--rule); }
.slide.dark .mfig-rule { background:var(--rule-light); }
.mfig-side { grid-column:5; display:flex; flex-direction:column; gap:14px; }
.mfig-side .ph { width:380px; height:475px; }
```

> Past ~12% of the frame the photo competes with the text: switch to `split-visual`.

---

### `field-notes` — a scouting record

A fixed metadata block (place, date, time, light…) and the photo of the place. Site visits, store audits, immersions; repeat it in the same form across a series.

```html
<section class="slide" data-eyebrow="field notes" data-heading="Visit 03">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="fnote">
    <div class="fnote-meta">
      <span class="eyebrow reveal">field notes · visit 03</span>
      <dl class="fnote-dl reveal">
        <div><dt>site</dt><dd>Site name</dd></div>
        <div><dt>date</dt><dd>14 March</dd></div>
        <div><dt>time</dt><dd>07:40</dd></div>
        <div><dt>light</dt><dd>Low, overcast</dd></div>
        <div><dt>duration</dt><dd>Two days on site</dd></div>
      </dl>
      <p class="fnote-obs reveal">One observation, in one sentence.</p>
    </div>
    <figure class="ph fnote-ph reveal"><img src="../assets/photos/site-03.jpg" alt=""></figure>
  </div>
</section>
```

```css
.fnote { height:100%; display:grid; grid-template-columns:544px 1fr 970px; align-items:center; }
.fnote-dl { margin-top:18px; border-top:1px solid var(--rule); }
.fnote-dl div { display:flex; justify-content:space-between; align-items:baseline; gap:20px; padding:13px 0; border-bottom:1px solid var(--rule); }
.fnote-dl dt { font-family:var(--font-mono); font-size:14px; letter-spacing:0.08em; opacity:0.65; }
.fnote-dl dd { font-size:20px; text-align:right; }
.fnote-obs { margin-top:36px; font-size:30px; font-weight:300; line-height:1.35; }
.fnote-ph { grid-column:3; width:970px; height:647px; }
```

> The metadata must be true. This layout is for **your own** site photos; a Pexels photo can't be passed off as the client's site. With a stock photo, use `plate` or `margin-figure` and caption it as an illustration.

---

### `scale-contrast` — the whole and its detail

One large photo of the place, one small close-up of its texture. Material, craft or quality is the point: "look closer".

```html
<section class="slide" data-eyebrow="detail" data-heading="Look closer">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="scl">
    <figure class="ph scl-big reveal"><img src="../assets/photos/pexels-slug-wide-1234567.jpg" alt=""></figure>
    <div class="scl-side">
      <div class="reveal">
        <span class="eyebrow">look closer</span>
        <h2 class="scl-title">Quality reads in the detail.</h2>
        <p class="lede">A large image for the context, a close-up for the material.</p>
      </div>
      <div class="scl-det reveal">
        <figure class="ph"><img src="../assets/photos/pexels-slug-close-7654321.jpg" alt=""></figure>
        <span class="pcap">detail<br>the material</span>
      </div>
    </div>
  </div>
</section>
```

```css
.scl { height:100%; display:grid; grid-template-columns:970px 1fr 544px; align-items:center; }
.scl-big { width:970px; height:647px; }
.scl-side { grid-column:3; height:647px; display:flex; flex-direction:column; justify-content:space-between; }
.scl-title { margin:14px 0 18px; font-size:44px; font-weight:300; line-height:1.12; }
.scl-det { display:flex; align-items:flex-start; gap:22px; }
.scl-det .ph { width:240px; height:300px; flex-shrink:0; }
```

> Under a 3× size difference the slide reads as hesitation. The small photo must be a real close-up (search `… texture close up`), not the wide shot shrunk.

---

### `typology-grid` — eight of a kind

Eight photos of the same kind of subject, framed alike, in a strict grid (the Bechers' method). The argument is the variation: "it's a pattern", "they all look alike".

```html
<section class="slide" data-eyebrow="typology" data-heading="Eight of a kind">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="typo">
    <div class="typo-txt">
      <span class="eyebrow reveal">typology</span>
      <h2 class="typo-title reveal">Eight subjects, one family.</h2>
      <p class="psent reveal">Same framing, same light, same distance: the differences do the talking.</p>
    </div>
    <div class="typo-grid reveal">
      <div class="typo-it"><figure class="ph"><img src="../assets/photos/pexels-slug-1-1111111-mono.jpg" alt=""></figure><span class="pcap">no. 01</span></div>
      <!-- … seven more .typo-it … -->
    </div>
  </div>
</section>
```

```css
.typo { height:100%; display:grid; grid-template-columns:402px 1fr; gap:48px; align-items:center; }
.typo-title { margin:14px 0 22px; font-size:44px; font-weight:300; line-height:1.12; }
.typo-grid { display:grid; grid-template-columns:repeat(4, 280px); gap:20px 24px; justify-content:end; }
.typo-it { display:flex; flex-direction:column; gap:10px; }
.typo-it .ph { width:280px; height:280px; }
```

> The hardest layout to source: inconsistent angle or light ruins it. Search one precise subject (`blue door facade`, `water tower`), prefer one photographer's series, and apply the same `--treatment mono` to all eight to unify them. Download at `--width 800`: they are small. Ten frames at most.

---

### `sequence-strip` — five frames read as time

Four to six equal frames in one row, read left to right: a gesture, a process, a day (Muybridge). Shows a method with real hands instead of icons.

```html
<section class="slide" data-eyebrow="process" data-heading="The gesture">
  <div class="chrome"><!-- chrome rows --></div>
  <div class="seq">
    <div class="seq-head">
      <span class="eyebrow reveal">step by step</span>
      <h2 class="seq-title reveal">Show the method with real hands.</h2>
    </div>
    <div class="seq-row reveal">
      <div class="seq-it"><figure class="ph"><img src="../assets/photos/pexels-slug-1-1111111.jpg" alt=""></figure><i class="tick"></i><span class="pcap">01</span><p>Six words at most</p></div>
      <!-- … four more .seq-it … -->
    </div>
  </div>
</section>
```

```css
.seq { height:100%; display:flex; flex-direction:column; justify-content:center; gap:40px; }
.seq-title { margin-top:14px; font-size:48px; font-weight:300; line-height:1.12; max-width:1100px; }
.seq-row { display:grid; grid-template-columns:repeat(5, 1fr); gap:24px; background:linear-gradient(var(--rule), var(--rule)) 0 412px / 100% 1px no-repeat; }
.seq-it { display:flex; flex-direction:column; }
.seq-it .ph { aspect-ratio:4/5; }
.seq-it .tick { display:block; width:1px; height:14px; margin-top:10px; background:currentColor; opacity:0.5; }
.seq-it .pcap { margin-top:10px; }
.seq-it p { margin-top:6px; font-size:20px; line-height:1.35; }
```

> All frames from the same distance, ideally one photographer's series (Pexels often has several frames from one shoot: open the photographer's page from the sidecar). The row's hairline sits at `412px` = frame height (5 columns of 316px at 4:5 → 396px) + 16px; recompute it if you change the column count.

---

## Adding a new component

If none of the above fits a beat in your deck, build a new one:

1. Sketch it on paper. One idea, one slide. If it has more than 3 distinct elements, split.
2. Build the CSS scoped under a single root class.
3. Write the HTML with a `data-eyebrow` and `data-heading`.
4. If it uses gradient text via `background-clip: text`, append the selector to `GRADIENT_TEXT_SELECTORS` in base.html — otherwise it'll have artefacts in PDF.
5. Run QA. Verify the bottom-content gap to chrome ≥ 16px on every viewport.

The discipline that keeps the system coherent: copy what's there before inventing something new.

---

## Ported layouts

The eight below were harvested from decks built with this system and rewritten against `brand/tokens.css`. Full index of what else exists, and what is not yet ported: `reference/LAYOUTS.md`. Everything executed and captioned: `reference/catalogue-layouts.html`.

---

### `waterfall` — a total, decomposed

The strongest layout for "where does this number come from". Each step is a floating block; its spacer pushes it up to where the previous one ended. Gains in one colour, a different colour for anything you want read separately, gradient on the total.

```html
<div class="wf reveal">
  <div class="wc up"><div class="v">25 200</div><div class="sp" style="height:244px"></div><div class="blk" style="height:136px"></div></div>
  <div class="wc up"><div class="v">12 857</div><div class="sp" style="height:175px"></div><div class="blk" style="height:69px"></div></div>
  <div class="wc alt"><div class="v">31 416</div><div class="sp" style="height:0"></div><div class="blk" style="height:170px"></div></div>
  <div class="wc total"><div class="v">79 673</div><div class="sp" style="height:0"></div><div class="blk" style="height:380px"></div></div>
</div>
<div class="wf-x"><span>Step one</span><span>Step two</span><span>Step three</span><span><b>Total</b></span></div>
```

```css
.wf { display:flex; align-items:stretch; gap:30px; height:380px; margin-top:44px; border-bottom:2px solid var(--rule-strong); }
.wf .wc { flex:1; display:flex; flex-direction:column; justify-content:flex-end; }
.wf .wc .blk { border-radius:10px; }
.wf .wc .v { text-align:center; font-family:var(--font-display); font-size:27px; margin-bottom:10px; }
.wf .wc .sp { flex-shrink:0; }
.wf .wc.up .blk { background:var(--brand-primary-soft); }
.wf .wc.alt .blk { background:var(--brand-secondary); }
.wf .wc.total .blk { background:var(--brand-gradient); }
.wf-x { display:flex; gap:30px; padding-top:16px; }
.wf-x span { flex:1; text-align:center; font-size:16px; line-height:1.3; }
```

> **Arithmetic to respect.** `spacer + block` must equal the plate height for the first step, and each following spacer equals the running cumulative height. Get this wrong and the staircase reads as noise. Compute the pixel heights before writing the HTML.

---

### `before-after` — selling a transformation

Two mirrored panels. The left one is flat and grey, the right one is raised and accented. Items must mirror one another line by line, otherwise the comparison does not land.

```html
<div class="ba" data-stagger>
  <div class="pane before"><span class="bt">today</span><ul><li>…</li><li>…</li></ul></div>
  <div class="pane after"><span class="bt">with the work</span><ul><li>…</li><li>…</li></ul></div>
</div>
```

```css
.ba { display:grid; grid-template-columns:1fr 1fr; gap:32px; margin-top:44px; }
.ba .pane { border-radius:22px; padding:38px; }
.ba .pane .bt { font-size:18px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; margin-bottom:22px; display:block; }
.ba .before { background:var(--brand-neutral-light-soft); border:1px solid var(--rule); }
.ba .after { background:#fff; border:2px solid var(--brand-primary); box-shadow:var(--shadow-card); }
.ba .after .bt { color:var(--label-accent, var(--brand-primary-deep)); }
.ba ul { list-style:none; display:flex; flex-direction:column; gap:16px; }
.ba li { font-size:18px; line-height:1.45; padding-left:30px; position:relative; }
.ba .before li::before { content:''; position:absolute; left:0; top:9px; width:14px; height:2px; background:var(--rule-strong); }
.ba .after li::before { content:''; position:absolute; left:0; top:6px; width:13px; height:13px; border-radius:50%; background:var(--brand-gradient); }
```

---

### `orbits` — a centre and its satellites

Maps actors, systems or teams by proximity to a centre. Two rings is the maximum that stays readable.

```html
<div class="orbit reveal">
  <div class="oring o2"></div><div class="oring o1"></div>
  <div class="osun">The centre</div>
  <div class="osat" style="left:360px; top:110px">Inner one</div>
  <div class="osat far" style="left:132px; top:72px">Outer one</div>
</div>
```

```css
.orbit { position:relative; width:720px; height:600px; flex-shrink:0; }
.orbit .oring { position:absolute; border:1.5px solid var(--rule); border-radius:50%; }
.orbit .o1 { left:170px; top:110px; width:380px; height:380px; }
.orbit .o2 { left:60px; top:0; width:600px; height:600px; }
.orbit .osun { position:absolute; left:360px; top:300px; transform:translate(-50%,-50%); width:180px; height:180px; border-radius:50%; background:var(--brand-gradient); display:flex; align-items:center; justify-content:center; text-align:center; font-weight:700; font-size:20px; padding:16px; line-height:1.25; }
.orbit .osat { position:absolute; z-index:2; transform:translate(-50%,-50%); border:1px solid var(--rule); border-radius:999px; padding:12px 22px; font-size:17px; font-weight:600; white-space:nowrap; background:#fff; }
.orbit .osat.far { background:transparent; font-weight:500; opacity:.7; }
```

> **Place satellites at the cardinal points of the inner ring and the diagonals of the outer one.** Anything else and the pills collide. Centre is `(360, 300)`; inner radius 190, outer 300. Long labels on the horizontal axis will touch the sun: shorten them or nudge outward.

---

### `y-split` — one trunk, two paths

The most distinctive schema in the library. A shared sequence that forks into two named tracks, with a caption sitting on the fork itself.

```html
<div class="parcours">
  <div class="shared">
    <div class="step-pill"><span class="sp-n">1</span><div><div class="sp-t">Shared step</div></div></div>
    <div class="lk">→</div>
    <div class="step-pill"><span class="sp-n">2</span><div><div class="sp-t">Shared step</div></div></div>
  </div>
  <div class="y-split">
    <div class="ys-stem"></div><div class="ys-bar"></div>
    <div class="ys-leg ys-l"></div><div class="ys-leg ys-r"></div>
    <span class="ys-label">then it forks</span>
  </div>
  <div class="tracks">
    <div class="track a"><div class="track-head"><span class="th-name">Track A</span></div><div class="track-def">…</div></div>
    <div class="track b"><div class="track-head"><span class="th-name">Track B</span></div><div class="track-def">…</div></div>
  </div>
</div>
```

```css
.parcours { display:flex; flex-direction:column; align-items:center; margin-top:18px; }
.shared { display:flex; align-items:stretch; justify-content:center; gap:18px; }
.step-pill { display:flex; align-items:center; gap:16px; background:var(--brand-neutral-light-soft); border:1px solid var(--rule); border-radius:18px; padding:16px 24px; max-width:460px; }
.y-split { position:relative; width:100%; height:58px; margin:6px 0 2px; }
.y-split .ys-stem { position:absolute; top:0; left:50%; transform:translateX(-50%); width:2px; height:22px; background:var(--rule-strong); }
.y-split .ys-bar { position:absolute; top:22px; left:25%; width:50%; height:2px; background:var(--rule-strong); }
.y-split .ys-leg { position:absolute; top:22px; width:2px; height:24px; background:var(--rule-strong); }
.y-split .ys-leg.ys-l { left:25%; } .y-split .ys-leg.ys-r { left:75%; }
.y-split .ys-label { position:absolute; top:11px; left:50%; transform:translateX(-50%); background:var(--plate-bg); padding:0 14px; font-family:var(--font-mono); font-size:12px; letter-spacing:.16em; text-transform:uppercase; white-space:nowrap; }
.tracks { display:grid; grid-template-columns:1fr 1fr; gap:26px; width:100%; }
.track { border-radius:24px; padding:22px 30px 24px; display:flex; flex-direction:column; }
.track.a { background:var(--brand-primary-soft); border:1px solid var(--brand-primary); }
.track.b { background:var(--brand-secondary-soft); border:1px solid var(--brand-secondary); }
.track-def { font-size:18px; line-height:1.4; margin-top:10px; padding-bottom:14px; border-bottom:1px solid var(--rule); }
```

> `.ys-label` needs the **plate background colour**, not transparent — it has to mask the bar it sits on.

---

### `file-tree` — architecture as a tree

An indented tree with an animated rail. Built for site architecture, but works for any hierarchy the audience will navigate.

```html
<div class="sitetree">
  <div class="st-root"><span class="fold">▸</span><span class="rn">root</span></div>
  <div class="st-tree">
    <div class="st-rail"></div>
    <div class="st-row"><span class="st-dot"></span><div class="st-bar"><span class="de">level</span><span class="nm">Name</span><span class="ds">What it holds</span></div></div>
    <div class="st-row child"><span class="st-elbow"></span><div class="st-bar"><span class="nm">Child</span></div></div>
  </div>
</div>
```

```css
.sitetree { position:relative; margin-top:36px; }
.st-root { display:inline-flex; align-items:center; gap:14px; }
.st-tree { position:relative; margin-top:6px; padding-left:18px; }
.st-rail { position:absolute; left:18px; top:30px; width:2px; height:calc(100% - 62px); background:var(--brand-gradient-vertical); transform:scaleY(0); transform-origin:top; transition:transform .85s var(--ease-slow) .15s; }
.plate.active .st-rail { transform:scaleY(1); }
.st-row { position:relative; display:flex; align-items:center; padding:7px 0; }
.st-row::before { content:''; position:absolute; left:18px; top:50%; transform:translateY(-50%); width:32px; height:2px; background:var(--rule-strong); }
.st-dot { position:absolute; left:12px; top:50%; transform:translateY(-50%); width:14px; height:14px; border-radius:50%; background:var(--brand-gradient); box-shadow:0 0 0 5px #fff; z-index:2; }
.st-bar { display:flex; align-items:center; gap:22px; margin-left:50px; background:#fff; border:1px solid var(--rule); border-radius:14px; padding:15px 26px; box-shadow:var(--shadow-card); flex:1; }
.st-row.child { margin-left:64px; }
.st-row.child::before { content:none; }
.st-row.child .st-elbow { position:absolute; left:-46px; top:-34px; width:30px; height:64px; border-left:2px solid var(--brand-primary); border-bottom:2px solid var(--brand-primary); border-bottom-left-radius:14px; }
```

> The rail animates on `.plate.active`. In PDF export, force it to its final state: `body.printing-pdf .st-rail { transform:scaleY(1) !important; }`

---

### `figures-grid` — a factual panorama

Six figures in a hairline grid, each with a one-line caption. Use when the audience needs facts without narration, typically to open a review or close a diagnosis.

```css
.figs { display:grid; grid-template-columns:repeat(3,1fr); margin-top:46px; border-top:1px solid var(--rule-strong); border-left:1px solid var(--rule-strong); }
.fig { padding:36px 40px; border-bottom:1px solid var(--rule-strong); border-right:1px solid var(--rule-strong); }
.fig .n { font-family:var(--font-display); font-size:60px; line-height:1; }
.fig .l { font-size:17px; margin-top:12px; line-height:1.4; }
```

> Six cells, never five or seven: the grid must close. Units go in a smaller inline span inside `.n`, not in the caption.

---

### `pricing-3` — three tiers, anchored

Ticks and absences mirrored across the three columns. **The absence is what sells**: a greyed line in the cheap column does more work than a tick in the expensive one.

```css
.cmp3 { display:grid; grid-template-columns:repeat(3,1fr); gap:28px; margin-top:48px; }
.cmp3 .col { border:1px solid var(--rule); border-radius:20px; padding:34px; background:#fff; box-shadow:var(--shadow-card); position:relative; }
.cmp3 .col.reco { border:2px solid var(--brand-primary); }
.cmp3 .col .badge { position:absolute; top:-16px; left:34px; background:var(--brand-gradient); font-size:13px; font-weight:700; letter-spacing:.08em; text-transform:uppercase; padding:7px 16px; border-radius:999px; }
.cmp3 .price { font-family:var(--font-display); font-size:50px; margin:12px 0 4px; line-height:1; }
.cmp3 .price small { font-size:19px; opacity:.6; }
.cmp3 li { font-size:17px; padding-left:28px; position:relative; line-height:1.4; }
.cmp3 li.y::before { content:'✓'; position:absolute; left:0; color:var(--brand-primary-deep); font-weight:700; }
.cmp3 li.n::before { content:'·'; position:absolute; left:5px; }
.cmp3 li.n { opacity:.55; }
```

---

### `activity-wall` — volume as the argument

A dense wall of small cards that deliberately overflows the plate on one or more edges. The point is not to read every card, it is to feel how many there are.

```css
.wall { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:34px; max-height:600px; overflow:hidden; position:relative; }
.wall::after { content:''; position:absolute; left:0; right:0; bottom:0; height:180px; background:linear-gradient(180deg, transparent, var(--plate-bg)); pointer-events:none; }
.acard { border:1px solid var(--rule); border-radius:14px; padding:18px 20px; background:#fff; }
.acard .ah { font-size:16px; font-weight:700; margin-bottom:6px; }
.acard .ad { font-size:14px; line-height:1.4; opacity:.7; }
```

> The fade-out at the bottom is what makes the overflow read as intentional rather than broken. Match its gradient to the plate background.
