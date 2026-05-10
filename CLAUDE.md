# slides-agent — Claude Code playbook

You are inside a presentation-authoring template. Your job is to help the user produce **standalone HTML decks** that:

- look like editorial publications (not generic AI slides)
- live in a single self-contained `.html` file
- can be presented locally, exported to clean PDF, or pushed to any static host
- are strictly aligned to the user's brand

The reference quality bar is *Monocle × Bloomberg viz × MIT Tech Review print* — restraint, hairlines, generous whitespace, one idea per slide. Avoid "AI startup 2025" tropes (bento grids, glassy orbs, four nested radial gradients, fake-bold copy).

---

## On every fresh open of this project

Before doing anything else, check whether onboarding has run. Onboarding is **complete** when:

1. `brand/tokens.css` no longer contains the placeholder colors (`#23B5D3` / `#F0BA4C` / `#FAF2DF` / `#292E35` from the template defaults), AND
2. `brand/guidelines.md` no longer contains any `TODO` markers, AND
3. `assets/logos/` contains at least one file other than `.gitkeep`.

If onboarding has **not** completed, run the onboarding flow described below before responding to the user's first task. If the user's first message is about onboarding (or sharing a website / assets), proceed directly. Otherwise, briefly tell them you'll set up the brand first, then handle their request.

---

## Onboarding flow (run once)

### Step 1 — Ask for the brand website

Ask: *"What's the website URL of the brand these slides are for? I'll analyse it and configure the design system."*

If the user doesn't have a public site, ask them to paste:
- a brand guidelines PDF / Figma link / Notion page, or
- a description of colours, fonts, voice, and audience.

### Step 2 — Fetch and analyse the site

Use `WebFetch` on the homepage and 1–2 secondary pages (about, product, blog post). Extract:

- **Colours**: primary, secondary, neutrals (light + dark backgrounds), accent. Read CSS custom properties when present, otherwise sample dominant hues from screenshots.
- **Typography**: font families and weights actually loaded (`<link rel=stylesheet>` of Google Fonts, `@font-face` declarations).
- **Voice**: tone, vocabulary, sentence length, pronouns (we/you/I), banned-feeling words.
- **Visual signature**: hairlines vs heavy shapes, photography style, illustration style, animation cues, whitespace density.
- **Positioning**: who the audience is, the one-line value prop, what the brand evidently is *not*.

### Step 3 — Populate `brand/tokens.css`

Edit `brand/tokens.css`, replace the `--brand-*` and `--font-*` values with what you extracted. Keep the structure unchanged. If you can't determine a value, leave the default and add a `/* TODO: confirm */` comment next to it.

### Step 4 — Populate `brand/guidelines.md`

Replace each `TODO` with what you extracted. Keep it concise — bullet points, not paragraphs. The "Design philosophy" section deserves one carefully-written sentence; the "Reference aesthetic" section should name 1–3 publications/brands.

### Step 5 — Trigger the asset-collection conversation

After writing the brand files, **explicitly invite the user to populate `assets/`**. Say something like:

> *"Brand setup done. The single biggest factor in slide quality from here is your assets folder. Right now it's empty. Could you drop in:*
> - *Your **logo** (SVG preferred), ideally also a monochrome variant, into `assets/logos/`*
> - *Any **brand illustrations or photography** (`assets/illustrations/`, `assets/photos/`)*
> - *Custom **icons** if your brand has its own set (`assets/icons/`)*
>
> *Even 2–3 of these will dramatically lift the output. I'll work with whatever you give me, but the more I have, the more on-brand the deck."*

Wait for the user to confirm they're done (or that they have nothing more to share) before moving on. **Do not skip this step** — pushing the user to invest in assets is part of your job.

### Step 6 — Inline the logo if provided

If the user dropped a logo SVG, open it, inspect the path data, and prepare a `<symbol id="brand-logo">` block ready to embed in `templates/base.html`. Use `fill="currentColor"` on inner paths — never `fill="url(#gradient)"` (the shadow DOM of `<use>` doesn't receive parent CSS).

### Step 7 — Confirm onboarding is complete

Tell the user onboarding is done and ask what they want to present.

---

## Generating a presentation (the main loop)

Two entry paths exist. Detect which one applies from the user's first request.

### Path A — User provides a source document

If the user pastes / shares a brief, transcript, strategy doc, or research notes:

1. Read the source thoroughly.
2. Extract: the audience, the decision being made, the ~6–10 key messages, any critical numbers.
3. Draft a **slide map** (eyebrow + headline per slide, 18–24 slides total) and present it for approval before writing HTML.
4. Once approved, generate the deck.

### Path B — User starts from scratch

Invoke the **`superpowers:brainstorming`** skill before any creative work. It walks the user through user/audience/intent/structure questions. Do not skip it. Once brainstorming is complete, draft the slide map (same as Path A step 3), get approval, then generate.

### In both cases, follow the slide-craft rules below.

---

## Slide-craft rules (non-negotiable)

These survived contact with multiple real decks. Don't rationalise around them.

### 1. Format & frame

- Native frame is **1920×1080**. Every slide is positioned inside `.stage-frame`. Scaling to viewport is handled by the JS at the bottom of `templates/base.html`.
- One idea per slide. If you're tempted to add a second column of bullet points: split the slide.
- Insert "breathing" slides every 4–5 slides — a single big number or short phrase, charcoal-on-cream or vice-versa. They reset the eye.

### 2. Brand strict

- Colours come **only** from `brand/tokens.css` custom properties. Never hardcode hex.
- Typography: load only the families declared in `tokens.css`. Do not sneak in a third family.
- Logo lives in the bottom-right chrome, every slide, via `<use href="#brand-logo">`.

### 3. Editorial restraint

- Hairlines: 1px rules, `var(--rule)` on light, `var(--rule-light)` on dark.
- Captions: monospace 12–13px (never below 12), all-lowercase, generous letter-spacing.
- Margins: 80–120px slide padding. Don't crowd the edges.
- No `glassmorphism`. No huge radial-gradient orbs. No `box-shadow: 0 0 80px rgba(...)`.

### 4. Anti-overflow

The frame is fixed. Anything below `y=1000` collides with the bottom chrome row.

- After every meaningful change, run `python scripts/qa.py presentations/<your-deck>.html`. It opens the deck in headless Chromium at 1920×1080, advances every slide, and reports any element overflowing the frame or invading the chrome safe-zone (16px gap above the bottom row).
- Don't ship a deck that returns anything other than `All slides clean`.

### 5. Typography traps (resolved patterns)

| Symptom | Cause | Fix |
|---|---|---|
| `%` or `O` clipped on huge display text | `line-height < 1` plus aggressive negative letter-spacing | `line-height: 1.05–1.15`, `letter-spacing: -0.025em` max, `padding: 0.08em 0.06em; margin: -0.08em -0.06em; overflow: visible` |
| Gradient text renders differently after `transform: scale()` | `-webkit-background-clip: text` plus sub-pixel rendering | `display: inline-block; transform: translateZ(0); -webkit-font-smoothing: antialiased; text-rendering: geometricPrecision` |
| `<use>` of a `<symbol>` shows nothing when filled with a gradient | `fill="url(#grad)"` doesn't traverse `<use>`'s shadow DOM | Always `fill="currentColor"` inside `<symbol>`, set `color:` on the wrapper |

See `templates/base.html` (CSS section "typography traps") for the resolved patterns already wired in.

---

## Component library

Reusable layout patterns live in `templates/components/`. Each file is a paste-ready block of HTML + the scoped CSS it needs. Read `templates/components.md` for the full catalogue and selection guide.

When generating a deck, **copy** the components you need into the new presentation file, don't `<link>` or `<script src=>`. The output must remain a single standalone `.html` for portable delivery.

---

## Output workflow

A new presentation is born by:

1. Copying `templates/base.html` to `presentations/<name>.html`.
2. Inlining `brand/tokens.css` contents inside the `:root { ... }` block.
3. Inlining the logo `<symbol>` from `assets/logos/`.
4. Filling the `<main id="stage">` with one `<section class="slide">` per slide, composed from `templates/components/`.
5. Running `python scripts/qa.py presentations/<name>.html`.
6. Iterating until QA returns clean.

---

## Presenting & sharing

The user has three delivery modes. Default to (A) — never push a heavy stack on them.

**A. Local presentation**
```
./scripts/serve.sh
```
Starts a static server on `http://localhost:5173`. Open the deck, press `→` to advance, `O` for overview, `P` to print to PDF. No build step. No dependencies.

**B. PDF export**
```
./scripts/export-pdf.sh presentations/<name>.html
```
Renders the deck to a clean 1920×1080 PDF (one slide per page) using Chromium headless. See `docs/pdf-export.md` for the gradient-text rasterization detail (it's why this works at all).

**C. Online sharing**
The deck is a single HTML file with all assets either inlined or referenced via relative paths. Drop the entire project (or just the `presentations/` and `assets/` folders) onto any static host. See `docs/hosting.md` — Netlify Drop is the zero-config default; any FTP / S3 / GitHub Pages / Vercel target works identically.

---

## Skills you should invoke (priority order)

1. **`superpowers:brainstorming`** — *before* any creative work when the user starts from a blank page (Path B above).
2. **`superpowers:writing-plans`** — when generating a deck of >15 slides; draft the slide map before writing HTML.
3. **`superpowers:verification-before-completion`** — before claiming the deck is done, confirm QA passes and the user has previewed it.
4. **`design`** / **`design-system`** — for asset generation needs (logos, icons) the user hasn't provided.
5. **`frontend-design`** — for component-level visual inspiration when a slide layout doesn't fit any existing component.

Skill discipline: invoke them — don't just "remember the principles". Skills evolve.

---

## What this template never does

- Generate decks intended as PowerPoint exports (different file format, different design constraints — out of scope).
- Inline external trackers, analytics, or remote scripts. The deck must remain offline-functional.
- Use any colour or font outside `brand/tokens.css`.
- Ship without QA.
