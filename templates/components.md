# Component library

Reusable slide patterns, ready to copy into a new presentation. Each component is a paste-and-adapt block: the structural HTML + the scoped CSS it needs. **Never modify positions, paddings, or animations** — only the textual content. The system was tuned across many iterations and the values are load-bearing.

> All components assume the brand tokens from `brand/tokens.css` are already in `:root`.

## How to use

1. Copy `templates/base.html` to `presentations/<your-deck>.html`.
2. Inline `brand/tokens.css` into the `:root { ... }` block.
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

A 24-slide deck typically uses 12–16 components, with 3–4 `silence` slides interleaved.

Every illustrative mark in these components is an **inline Lucide-style SVG** (`stroke: currentColor`), never an emoji. See [Iconography](#iconography) for the rule and the reusable pastille pattern.

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
.process-num { display:flex; align-items:center; justify-content:center; width:48px; height:48px; border-radius:var(--radius-pill); background:var(--brand-primary-soft); color:var(--brand-primary-deep); font-family:var(--font-mono); font-size:20px; font-weight:500; }
.process-step h3 { font-size:24px; font-weight:500; line-height:1.2; }
.process-step p { font-size:18px; line-height:1.5; opacity:0.75; }
.process-arrow { display:flex; align-items:center; justify-content:center; color:var(--brand-secondary-deep); }
.process-arrow svg { width:36px; height:36px; }
.process-banner { display:flex; align-items:baseline; gap:24px; margin-top:32px; padding:28px 36px; border-radius:8px; background:var(--brand-neutral-dark); color:var(--brand-neutral-light); }
.process-banner span { font-family:var(--font-mono); font-size:13px; letter-spacing:0.08em; opacity:0.6; white-space:nowrap; }
.process-banner strong { font-size:24px; font-weight:300; line-height:1.3; }
```

> On a dark slide, swap `.process-step` to `background:var(--brand-neutral-dark-soft); border-color:var(--rule-light);` and the banner to `background:var(--brand-neutral-light); color:var(--brand-neutral-dark);` for contrast.

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
.comparison-table thead th { font-family:var(--font-mono); font-size:13px; font-weight:500; letter-spacing:0.06em; text-transform:lowercase; opacity:0.6; border-bottom:1px solid var(--brand-neutral-dark); }
.comparison-table .c-criteria, .comparison-table tbody th { text-align:left; font-weight:400; opacity:1; }
.comparison-table tbody th { font-size:20px; }
.comparison-table .c-you { background:var(--brand-primary-soft); }
.comparison-table thead th.c-you { color:var(--brand-primary-deep); opacity:1; font-weight:700; border-bottom:2px solid var(--brand-primary); }
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
.kanban-tag { font-family:var(--font-mono); font-size:12px; letter-spacing:0.08em; text-transform:lowercase; color:var(--brand-primary-deep); }
.kanban-card h4 { font-size:22px; font-weight:500; line-height:1.2; }
.kanban-card p { font-size:18px; line-height:1.45; opacity:0.72; }
.kanban-progress { height:6px; border-radius:var(--radius-pill); background:var(--rule); overflow:hidden; margin-top:6px; }
.kanban-progress span { display:block; height:100%; width:calc(var(--p, 0.5) * 100%); background:var(--brand-gradient); border-radius:var(--radius-pill); }
```

> On a dark slide, swap cards to `background:var(--brand-neutral-dark-soft); border-color:var(--rule-light);`. The progress bars use a static fill (no transition), so they need no print override.

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
.ts-label { font-family:var(--font-mono); font-size:13px; letter-spacing:0.06em; text-transform:lowercase; color:var(--brand-primary-deep); }
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
.team-photo.initials { display:flex; align-items:center; justify-content:center; background:var(--brand-primary-soft); color:var(--brand-primary-deep); font-family:var(--font-mono); font-size:48px; font-weight:500; }
.team-member strong { font-size:26px; font-weight:500; line-height:1.1; }
.team-member span { font-family:var(--font-mono); font-size:13px; letter-spacing:0.04em; opacity:0.65; }
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

## Adding a new component

If none of the above fits a beat in your deck, build a new one:

1. Sketch it on paper. One idea, one slide. If it has more than 3 distinct elements, split.
2. Build the CSS scoped under a single root class.
3. Write the HTML with a `data-eyebrow` and `data-heading`.
4. If it uses gradient text via `background-clip: text`, append the selector to `GRADIENT_TEXT_SELECTORS` in base.html — otherwise it'll have artefacts in PDF.
5. Run QA. Verify the bottom-content gap to chrome ≥ 16px on every viewport.

The discipline that keeps the system coherent: copy what's there before inventing something new.
