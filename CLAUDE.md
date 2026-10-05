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

1. `brand/tokens.css` no longer contains the neutral example palette shipped with the template (`#1E40AF` / `#F59E0B` / `#F8FAFC` / `#0F172A`), AND
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
- **Visual signature**: hairlines vs heavy shapes, photography style, illustration style, animation cues, whitespace density, and any recurring motif (a pattern, a texture, a corner ornament) the brand repeats across pages.
- **Positioning**: who the audience is, the one-line value prop, what the brand evidently is *not*.

### Step 3 — Populate `brand/tokens.css`

Edit `brand/tokens.css`, replace the `--brand-*` and `--font-*` values with what you extracted. Keep the structure unchanged: replace values, never variable names, and never write a `{{...}}` placeholder into a value (an invalid custom property silently disables every rule that uses it). The comment next to each brand variable names the setup placeholder it maps to (`← BRAND_COLOR_PRIMARY`, `← BRAND_COLOR_ACCENT`, `← BRAND_COLOR_LIGHT`, `← BRAND_COLOR_DARK`, `← BRAND_GRADIENT`, `← BRAND_FONT_PRIMARY`, `← BRAND_FONT_SECONDARY`), and the comment next to each derived value (`-deep`, `-soft`, `--rule`, `--rule-light`) gives the `color-mix()` formula to recompute it from the new base colour. If you can't determine a value, leave the default and add a `/* TODO: confirm */` comment next to it.

Two blocks of the file need a decision of their own:

- **Label register.** Chrome text and eyebrows are 12-13px, so they need 4.5:1. Set `--label-accent` to the new primary darkened until it reaches 4.5:1 on `--brand-neutral-light-deep`, and leave `--chrome-opacity` / `--chrome-opacity-dark` at 0.7. QA measures them on the first deck: on a contrast error in the chrome or an eyebrow, retune these tokens (just past the threshold, never to full black), not the slide.
- **Brand pattern.** If Step 2 found a recurring motif, it goes here: `--brand-pattern` (the motif drawn in the dark ink, for light slides), `--brand-pattern-light` (the same motif drawn light, for dark slides), `--corner-motif` (a corner ornament). Write each as an SVG data URI, or as a path relative to the deck (`../assets/illustrations/...`) for a file the user supplied. No motif found: leave them at `none`, never invent a decoration. The classes that draw them (`.texture`, `.motif`, `.corner`, `.filet-orn`) are documented in `templates/components.md`, "Brand pattern hooks".

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

### Step 5b — Offer real photography (Pexels, optional, free)

Skip this step if `python3 scripts/pexels.py check` already succeeds. Otherwise, once the asset conversation is over, offer it once:

> *"One more optional upgrade: I can illustrate some slides with real photographs from Pexels. It's free, and every photographer is credited automatically on a closing slide. It takes a free API key, about 3 minutes, and I'll guide you step by step. Shall we set it up now?"*

If the user says yes, walk them through `docs/pexels-setup.md` as a guided conversation, in their language:

1. **One step per message.** Give only the current step: what to open, what to click, what to type. End with a short question ("Tell me when you see your key"). Wait for the answer before giving the next step. Never paste the whole guide at once.
2. **Do the machine side yourself.** Create `.env` with `cp .env.example .env` if it doesn't exist, and open it for them (`open -e .env` on macOS). The user pastes the key into `.env` **themselves**: never ask for the key in chat and never write it for them. If they paste it in chat anyway, don't repeat it back, and point them to the `PEXELS_API_KEY=` line in `.env`.
3. **Verify.** Run `python3 scripts/pexels.py check`. On success, confirm in one line (key works, remaining quota). On failure, match the message against the troubleshooting table in `docs/pexels-setup.md`, give the single fix, and run `check` again.
4. **Close the loop.** Explain in two sentences what changes now: when a slide calls for a real place, material, object or atmosphere, you'll pick a photo, place it, and credit it on the last slide; they can ask for a swap at any time.

If the user declines or wants to do it later, say how to resume (*"ask me to set up Pexels, or read docs/pexels-setup.md"*) and move on. Pexels never blocks onboarding, and onboarding is complete without it.

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

### Photos in the slide map

When you draft the slide map, mark the beats that call for a real photograph (a place, a material, an object, a gesture, an atmosphere): about one slide in four at most. For each, follow the priority order in the `pexels-photos` skill: the user's `assets/photos/` first, then Pexels, then `generate-image`, then typography.

If some beats want a photo, nothing in `assets/photos/` fits, and `python3 scripts/pexels.py check` fails for lack of a key, offer the setup **once**, next to the slide map: *"Slides 1, 6 and 14 would be stronger with a real photo. I can fetch them from Pexels (free, about 3 minutes, I'll guide you), or build them with typography and illustrations instead."* If they accept, run the guided flow of onboarding Step 5b. Otherwise continue without photos and don't ask again for this deck.

### In both cases, follow the slide-craft rules below.

---

## Slide-craft rules (non-negotiable)

These survived contact with multiple real decks. Don't rationalise around them.

### 1. Format & frame

- Native frame is **1920×1080**. Every slide is positioned inside `.stage-frame`. Scaling to viewport is handled by the JS at the bottom of `templates/base.html`.
- One idea per slide. If you're tempted to add a second column of bullet points: split the slide.
- Insert "breathing" slides every 4–5 slides — a single big number or short phrase, dark-on-light or vice-versa. They reset the eye.

### 2. Brand strict

- Colours come **only** from `brand/tokens.css` custom properties. Never hardcode hex.
- Typography: load only the families declared in `tokens.css`. Do not sneak in a third family.
- Logo lives in the bottom-right chrome, every slide, via `<use href="#brand-logo">`.

### 3. Editorial restraint

- Hairlines: 1px rules, `var(--rule)` on light, `var(--rule-light)` on dark.
- Captions: monospace 12–13px (never below 12), all-lowercase, generous letter-spacing.
- Margins: 80–120px slide padding. Don't crowd the edges.
- No `glassmorphism`. No huge radial-gradient orbs. No `box-shadow: 0 0 80px rgba(...)`.

### 4. QA gate (anti-overflow, type floors, contrast)

The frame is fixed. Anything below `y=1000` collides with the bottom chrome row.

- After every meaningful change, run `python3 scripts/qa.py presentations/<your-deck>.html`. It opens the deck in headless Chromium, activates every slide in its settled state and measures, in native 1920×1080 pixels: engine parity with `templates/base.html`, overflow out of the frame, the chrome safe zone (16px gap above the bottom row), the type floors (rule in "Minimum on-screen type size" below), brand fonts, WCAG AA contrast on every text (chrome included, `opacity` counts) and folios.
- Don't ship a deck that returns anything other than `All slides clean`. Warnings (`tight-body`, `long-label`, contrast on a gradient background, an undeclared monospace) don't fail the gate, but read them: they usually mean a slide wants splitting or a colour pair wants checking by eye.
- Full-bleed images are exempt by design: `.slide-bg` blocks and elements marked `data-bleed` (a photo column running to the frame edge) are skipped by every check, and so are `.aurora` and `.dust-grid`. Use `data-bleed` only on the image container, never on a text block, or QA stops protecting that text.
- Never game a finding: no `data-bleed` on text, no monospace to slip a sentence under the content floor, no raising `--min-font-chrome` or lowering `--min-font` to get a green run. Fix the slide.

### 4b. Print rendering pitfalls (Chromium PDF pipeline)

Some CSS features that look right on screen render broken in the exported PDF. The print CSS in `templates/base.html` already neutralises these globally — do not re-introduce them under `body.printing-pdf`:

- **All shadows** (`box-shadow`, `text-shadow`, `filter: drop-shadow(...)`, `backdrop-filter: blur(...)`) — banding, halos, mis-positioned blur. Removed in print via a global `* { ...: none }` reset.
- **Background grids** (`.dust-grid`, `.graticule`, repeating linear-gradients, mask-image radial fades) — 1px gradient lines render thicker, mask fades aren't honoured. Hidden in print via class allow-list. If you invent a new grid class, EITHER name it from the list below OR add `data-pdf-hide` on the element.

  Pre-listed grid classes that are auto-hidden in PDF:
  `.aurora` · `.dust-grid` · `.graticule` · `.grid-bg` · `.bg-grid` · `.grid-pattern` · `.background-grid` · `.dot-grid-bg` · `.ambient-grid` · `.pattern-bg` · `[data-pdf-hide]`

- **`filter: blur(...)` halos / aurora** — same family. Use `display: none` in `body.printing-pdf`, do not try to "make them work in print".
- **Animations and CSS keyframes** — must be forced to final state under `body.printing-pdf .my-component { animation: none !important; ...stable-final-state... }`. The base template covers `.reveal`, `[data-stagger]`, `.pipeline-anim`, `.roadmap-track::before`, `.roadmap-phase::before`, `.funnel-bar::before`, `.dot-grid .d.us`. Add an entry for any new animated component you build.

### 5. Typography traps (resolved patterns)

| Symptom | Cause | Fix |
|---|---|---|
| `%`, `O` or the descenders of `g j p q` clipped on display text | `background-clip: text` only paints inside the inline-block box, whose height is the line-height; tight display leading pushes glyphs out of it | `line-height` ≥ 1.1 on text titles, `letter-spacing: -0.025em` max, and on the gradient span `padding: 0.22em 0.08em; margin: -0.22em -0.08em; overflow: visible` (never reduce it) |
| Gradient text renders differently after `transform: scale()` | `-webkit-background-clip: text` plus sub-pixel rendering | `display: inline-block; transform: translateZ(0); -webkit-font-smoothing: antialiased; text-rendering: geometricPrecision` |
| `<use>` of a `<symbol>` shows nothing when filled with a gradient | `fill="url(#grad)"` doesn't traverse `<use>`'s shadow DOM | Always `fill="currentColor"` inside `<symbol>`, set `color:` on the wrapper |

See `templates/base.html` (CSS section "typography traps") for the resolved patterns already wired in.

---

## Layout library

Three files, in the order you should reach for them:

1. **`reference/LAYOUTS.md`** — the index. 120 layouts in 8 families, each with a "reach for it when" line. **Start here**, and pick layouts by the beat you need rather than by scrolling.
2. **`reference/catalogue-layouts.html`** — all 120 executed and self-captioned in a single deck. Open it, press `O`, and look. The brand and every figure in it are fictional, which is what makes it safe to read as a layout reference (see the exception in "What this template never does").
3. **`templates/components.md`** — paste-ready HTML and scoped CSS for the patterns that have been ported, with their known traps.

**The variety rule.** No layout twice in a row, and no layout more than twice in a deck. A deck that repeats card grids reads as generated; one that uses eight different layouts reads as authored. Before building, write the beat sequence, then assign one layout per beat. If two adjacent beats want the same layout, one of them is the wrong beat.

Every layout in the index is built. To add one, follow the procedure at the bottom of `LAYOUTS.md`.

**QA on the catalogue.** The catalogue is a specimen book, not a full deck (it has no headless PDF hooks), so skip the engine parity check: `python3 scripts/qa.py reference/catalogue-layouts.html --no-engine-check`. Its `.plate` slides and `.tag-folio` folios are detected automatically, and its `.legend` cartouche (the self-caption) is not audited. A layout taken from the catalogue must still pass the gate inside your deck.

**Screenshots.** The catalogue ships a `.shotph` placeholder (browser chrome around a labelled empty frame). Use it instead of embedding an image while the real capture is missing: it shows the aspect ratio needed and keeps the slide legible.

When generating a deck, **copy** the components you need into the new presentation file, don't `<link>` or `<script src=>`. The output must remain a single standalone `.html` for portable delivery.

---

## Output workflow

A new presentation is born by:

1. Copying `templates/base.html` to `presentations/<name>.html`. It carries the full engine (the canonical list is `docs/engine-parity.md`): never strip or rewrite it.
2. Inlining `brand/tokens.css` contents inside the `:root { ... }` block.
3. Inlining the logo `<symbol>` from `assets/logos/`.
4. Filling the `<main id="stage">` with one `<section class="slide">` per slide, composed from `templates/components.md` and the catalogue. Each slide carries `data-family` (the catalogue's keys: `ouverture`, `editorial`, `dataviz`, `schema`, `tableau`, `preuve`, `conclusion`, `photo`), `data-eyebrow` and `data-heading`, and an empty `.nav-num` span: the engine numbers the folios.
5. Running `python3 scripts/qa.py presentations/<name>.html`.
6. Iterating until QA returns clean.

---

## Presenting & sharing

The user has three delivery modes. Default to (A) — never push a heavy stack on them.

**A. Local presentation**
```
./scripts/serve.sh
```
Starts a static server on `http://localhost:5173`. Open the deck, press `→` to advance, `O` for the overview (grouped by `data-family`), `F` for fullscreen, `P` to print to PDF. No build step. No dependencies.

**B. PDF export**
```
./scripts/export-pdf.sh presentations/<name>.html
```
Renders the deck to a clean 1920×1080 PDF (one slide per page) using Chromium headless. See `docs/pdf-export.md` for the gradient-text rasterization detail (it's why this works at all).

**C. Online sharing**
The deck is a single HTML file with all assets either inlined or referenced via relative paths. Drop the entire project (or just the `presentations/` and `assets/` folders) onto any static host. See `docs/hosting.md` — Netlify Drop is the zero-config default; any FTP / S3 / GitHub Pages / Vercel target works identically.

---

## Skills and tools you should invoke

The template assumes you have access to a typical Claude Code skill set. Invoke these proactively — don't just "remember the principles". They evolve and are tuned beyond what this CLAUDE.md captures.

### Process discipline (always)

1. **`superpowers:brainstorming`** — *before* any creative work when the user starts from a blank page (Path B above). Non-skippable.
2. **`superpowers:writing-plans`** — when generating a deck of >15 slides; draft the slide map before writing HTML.
3. **`superpowers:verification-before-completion`** — before claiming the deck is done, confirm QA passes and the user has previewed the deck in a browser.

### Visual / UX quality (during phases 2–3, art direction and components)

4. **`ui-ux-pro-max`** — primary reference for visual direction. Use it to pick a colour system, font pairing, design style (editorial, brutalism, minimalism, etc.) that matches the brand and the deck's emotional arc. Especially valuable when `brand/guidelines.md` is sparse or the brand has no strong existing visual identity. Also covers chart styles for data slides.
5. **`frontend-design`** — for component-level visual inspiration when a slide beat doesn't fit any layout in `reference/LAYOUTS.md`. Use it to design a new pattern, then port the result into a slide-shaped (1920×1080, chrome-aware) version.
6. **`mcp__magic__21st_magic_component_*`** (21st.dev MCP tools) — when you need polished component variants beyond what frontend-design produces. Useful for hero treatments, complex tables, navigation chrome details. Treat the output as inspiration, not a drop-in: rework geometry to fit the 1920×1080 frame and the chrome safe-zone, and re-apply the brand tokens.

### Asset generation (when the user has gaps in `assets/`)

7. **`design`** — generate brand-aligned assets (logos, banners, icons, social photos) when the user hasn't provided them. Especially valuable for icon sets and atmospheric hero imagery. Save outputs into the right `assets/` subfolder.
8. **`design-system`** — when the brand has no token discipline yet, use it to formalise primitive → semantic → component tokens before populating `brand/tokens.css`.
9. **`pexels-photos`** (project skill, `.claude/skills/pexels-photos.md`) — real photographs from Pexels for the beats that call for a place, a material, an object or an atmosphere. It carries the anti-stock doctrine, the autonomous search → contact sheet → download → placement loop, brand treatments baked into the file, and the closing credits slide. Needs a free key: guide the user with onboarding Step 5b.

### Discipline

- If a skill is relevant, invoke it. The fastest way to ship a generic-looking deck is to skip these.
- Don't stack skills redundantly. `frontend-design` covers most component needs; reach for `21st_magic_*` only when you need a richer reference.
- Output from any visual skill must still pass through `brand/tokens.css` and the chrome system. Never paste a generated component verbatim if it violates brand restraint.

---

## Recent techniques (apply by default)

Validated on real projected decks (mid-2026). They matter for professional, room-readable output.

### Overview grouped by family
The overview (`O`) groups the thumbnails by `data-family`, in the order of the catalogue's families, so a 24-slide deck reads as its structure. Keys are the catalogue's (`ouverture`, `editorial`, `dataviz`, `schema`, `tableau`, `preuve`, `conclusion`, `photo`); a slide without a known family lands in a last "Other slides" group. While the panel is open only `O` and `Esc` act, and a click outside the thumbnails closes it.

### Presentation mode (fullscreen)
`templates/base.html` ships a `⛶` button and the `F` shortcut. They request OS fullscreen; while active, `body.presenting` is set, the slide scales to fill the whole screen (no nav reserved), and the nav-rail auto-hides — it reappears when the cursor nears the bottom edge. Nothing to wire per deck.

### Minimum on-screen type size (enforced by `scripts/qa.py`)
A slide is read from across a room. Two registers, measured on the computed font size in the 1920×1080 frame:

- **Content text: 18px minimum** (`type-floor` error; an 18pt projected floor). Comfortable body is 24px and up: content text under 24px, headings excepted, is a `tight-body` warning.
- **Label register: 12px minimum** (`type-floor` error under 12px). A text is in the label register when it sits inside `.chrome`, carries a label class (`.eyebrow`, `.meta-label`, `.signature`, `.nav-num`; `.tag-meta`, `.tag-folio`, `.tag-signature` in the catalogue), or is set in a monospace stack. These are the folio, signature, eyebrow and caption labels, and they sit at 12-14px.

Never shrink a real sentence to caption size to make it fit: split the slide or cut words instead. Setting a sentence in mono does not make it a label: a label-register text under 18px that runs past 12 words is a `long-label` warning.

### Block-centering to kill empty middles
For a "title + content" slide, center the whole block (title + grid/table/cards) as one unit, not "title pinned to the top + content centered in the leftover space" (which leaves a void between them). Give the slide `justify-content: center` and make the content wrapper `flex: 0 0 auto`, so the title and its content read as one centered group.

### Icons: inline stroke SVG, not emoji
Use inline Lucide-style SVGs (`stroke: currentColor; stroke-width: 1.75; fill: none`) tinted with a brand token, inside a soft tinted chip. They stay crisp at any scale and on-brand. Never paste OS emoji into slides.

### Static decorative elements
Decorative illustrations / mascots stay still: no looping float/bob animation (it distracts during a talk). Only the one-shot reveal-on-enter transition is allowed.

### Ambient aurora, sparingly
`templates/base.html` ships an optional `.aurora` layer (two blurred brand-colour discs, first child of the slide), used on its breathing slide. Rhythm slides only (cover, breathers, closing), two or three per deck, never behind a paragraph or a chart. QA skips it and the PDF export hides it. See "Ambient aurora" in `templates/components.md`.

---

## What this template never does

- Generate decks intended as PowerPoint exports (different file format, different design constraints — out of scope).
- Inline external trackers, analytics, or remote scripts. The deck must remain offline-functional.
- Use any colour or font outside `brand/tokens.css`.
- Ship without QA.
- **Cite a previous deck file as a "reference to study" or "starter inspiration".** Even citing a past deck as "gold standard" contaminates new productions — Claude re-reads it and duplicates its arc, components, metaphor, and visual through-line, even when told not to. The only authorised references are the current `templates/base.html` skeleton, the layout library (`reference/LAYOUTS.md`, `reference/catalogue-layouts.html`, `templates/components.md`) and `brand/guidelines.md`. **The catalogue is an authorised exception precisely because it has no arc**: its slides are independent, self-captioned specimens on a fictional brand, so there is a geometry to copy and no narrative to absorb. Take geometry from it, never content, never sequence. Each new deck invents its own metaphor and compositions from the brief, not from a past deck. If a similar topic was decked before, do not look at the previous output — start fresh from the brief.

---

## Pre-delivery checklist (mandatory)

Before declaring a deck done, every item must pass:

- [ ] `python3 scripts/qa.py presentations/<deck>.html` returns `All slides clean` (no overflow, no text under 18px of content or 12px of label, every text on a brand font and at WCAG AA contrast, folios in order), and its warnings have been read
- [ ] `python3 scripts/qa.py presentations/<deck>.html --with-pdf` passes and the PDF weight it prints is plausible: a real deck averages around 150 KB per slide (the gate itself fails under 40 KB; raise it with `--min-kb-per-slide` for image-heavy decks). A 20-slide deck with a 250 KB PDF means most pages collapsed to nothing; investigate before shipping. The PDF goes through the same print hooks as `scripts/export_pdf.py`.
- [ ] Every CSS rule that uses `background-clip: text` has its selector listed in `GRADIENT_TEXT_SELECTORS` (search the file for `background-clip: text` and cross-check). Missing entries = silent blank text in PDF, no error.
- [ ] No em-dash `—` in user-visible text. Run: `grep "—" presentations/<deck>.html | grep -v "<!--"` — should return nothing or only matches inside CSS comments.
- [ ] The chrome `tag-folio` (`Plate 0X / N` or equivalent) is correct on every slide. Auto-counter in the nav-rail and the in-slide folios are both auto-numbered from DOM order by JS (no manual edits needed).
- [ ] Manually opened in Chrome, navigated all slides ←/→, tested O / P / F (fullscreen) / drag bar / wheel / 1-9+Enter / Esc.
- [ ] Each `<section class="slide">` has `data-family`, `data-eyebrow` and `data-heading` attributes (the overview groups thumbnails by family and labels them with the other two — empty thumbs or an "Other slides" group mean an attribute was forgotten).
- [ ] If the deck uses any `pexels-*` photo: the last slide is the `photo-credits` slide, regenerated with `python3 scripts/pexels.py credits presentations/<deck>.html` after the final photo change, and the command prints no `warning:` line.
