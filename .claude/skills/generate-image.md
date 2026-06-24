---
name: generate-image
description: Generate bespoke, on-brand illustrations and hero images for slides via Google Gemini (Nano Banana Pro). Brand-agnostic — every prompt is automatically prefixed with the configured brand's style (palette from brand/tokens.css, illustration style and banned tropes from brand/guidelines.md), built with Nano Banana Pro best practices (natural-language prose, Identity Lock, Keep/Change framing, format last), and journaled as a JSON sidecar for reproducibility. Requires a GOOGLE_AI_API_KEY in .env. Optional but recommended for custom visuals; without a key, decks rely on screenshots, icons and design tokens. Use when the user asks for a custom illustration, hero image, atmospheric background, or section visual for a deck.
---

# Skill — generate-image

Produce custom illustrations and hero images for presentations by calling the
Gemini Nano Banana Pro image API through `scripts/gen-image.py`.

This skill is **brand-agnostic by design**. It carries no hard-coded colours,
fonts or style — instead it reads the brand the user configured in `brand/` and
prefixes every prompt with that brand's visual language. The same skill produces
clean editorial line art for one brand and warm atmospheric illustration for
another, purely from what `brand/` says.

## When to invoke

- "Generate a hero illustration for the opening slide about [topic]"
- "I need a custom section visual / background for [slide]"
- "Make an on-brand illustration of [concept] for this deck"
- Any time a deck needs a bespoke raster visual that icons, screenshots or
  CSS tokens can't provide.

**Not for:** charts (use Chart.js in the deck), icons (use `assets/icons/`),
or product screenshots (capture them and drop in `assets/photos/`).

## Optional capability — read this first

AI image generation is **optional**. It improves decks by adding bespoke,
on-brand illustrations, but it is not required.

- **With a key** → custom illustrations/heroes automatically styled to the
  configured brand.
- **Without a key** → build the deck from screenshots (`assets/photos/`),
  icons (`assets/icons/`), and the design tokens (`brand/tokens.css`). Do not
  block on image generation; say so and proceed with those.

### Prerequisite

`scripts/gen-image.py` reads credentials from `.env` at the repo root:

```
GOOGLE_AI_API_KEY=...                              # required to generate
GOOGLE_AI_IMAGE_MODEL=gemini-3-pro-image-preview   # optional, this is the default
```

Copy `.env.example` to `.env` and add a key from
<https://aistudio.google.com/apikey>. `.env` is git-ignored — never commit a key.
If the key is missing, the script exits with clear setup instructions; relay
them and fall back to screenshots/icons/tokens.

---

## Non-negotiable rule: prefix every prompt with the brand style

**Never send a raw prompt.** Before any generation, read the brand and build a
STYLE block from it, then put that block near the top of the prompt. This is
what makes the output adapt automatically to whatever brand the template user
configured.

Read these two files every time:

1. **`brand/tokens.css`** → the exact palette. Pull the hex values of
   `--brand-primary`, `--brand-primary-deep`, `--brand-secondary`,
   `--brand-secondary-deep`, `--brand-neutral-light`, `--brand-neutral-dark`.
   Name them explicitly in the prompt (hex codes) so the model uses *that*
   palette and nothing else.
2. **`brand/guidelines.md`** → the prose direction. Use, in particular:
   - **Photography & illustration → Illustration style** (line / flat /
     atmospheric, etc.)
   - **Photography & illustration → Banned visual tropes / What we never use**
     (e.g. "3D renders", "stock photography of people in suits", "cliché AI
     gradients")
   - **Iconography → Style**, **Design philosophy**, and **Reference aesthetic**
     for overall restraint and mood.

If those fields still read `TODO`, the brand hasn't been onboarded for imagery
yet. Either ask the user to fill the *Illustration style* and *Banned visual
tropes* lines in `brand/guidelines.md`, or proceed with a sensible, restrained
default and tell the user it wasn't brand-tuned.

### How to assemble the STYLE block

Translate the brand fields into one or two prose paragraphs that read like a
brief to a human illustrator. Example shape (fill from the actual brand):

```
[STYLE]
Work in <BRAND>'s visual language: <illustration style from guidelines.md,
e.g. "flat editorial illustration, clean monoline detail, no 3D">.
Use only the <BRAND> palette: primary <--brand-primary hex>, deep primary
<--brand-primary-deep hex>, secondary <--brand-secondary hex>, light neutral
<--brand-neutral-light hex> for backgrounds, dark neutral <--brand-neutral-dark
hex> for fine linework and text. No colours outside this palette.
Avoid: <banned tropes from guidelines.md, e.g. "cliché AI violet→neon
gradients, robot mascots, brain-circuit motifs, corporate stock photography,
generic 3D renders, lens flare">.
```

---

## Nano Banana Pro prompting doctrine (apply to every prompt)

Synthesised from Google's Nano Banana Pro guide. These patterns are mandatory,
not optional.

### 1. Natural language, not tag soup

Brief the model like a human illustrator: full sentences, descriptive
adjectives, a hierarchy of importance.

- Bad: "cool hero, brand blue, flat, 16:9, no gradient"
- Good: "A calm editorial hero illustration of two figures reviewing a chart
  together, rendered in flat shapes with the brand primary blue #23B5D3 as the
  dominant fill and a thin dark outline for detail."

### 2. Identity Lock with explicit "Image N"

When you pass reference images, refer to each one explicitly by number and
assign it a role: "Image 1 is the character to keep", "Image 2 is the
background style to imitate". The model needs the pointer — "the attached
reference" is too vague.

### 3. "Keep X exactly. Change ONLY Y" framing

For variations of an existing asset, split the prompt into two explicit blocks:
an identity-lock list (features that must stay identical to Image 1) and a
change list (the single thing that varies — expression, posture, lighting,
background). This yields far more consistent series than free-form prompts.

### 4. Edit, don't re-roll

For a small fix (remove an artifact, recolour one element, adjust a pose), pass
the existing image back as a reference (`--ref`) with a short edit instruction
instead of regenerating from scratch. The model preserves coherence with the
rest of the asset set.

### 5. Prose preamble for style

Give style as descriptive prose paragraphs (the STYLE block above), not bullet
lists of all-caps "FORBIDDEN" lines. Hex codes are fine inside the prose.

### 6. Format last

Put technical constraints (aspect ratio, framing, margins, background colour,
"no text in image") in the **last** section, after style and content. The model
weights later instructions more heavily for technical specs. Pass the aspect
ratio both in the prompt and via `--aspect`.

### 7. Reframe negations positively

The model handles "no X" poorly. Prefer "solid colour fill" over "no gradient",
"flat 2D illustration" over "no 3D". Keep explicit negation only for sharply
banned cultural tropes (cliché AI gradient, robot, brain-circuit) that the model
recognises as shorthand.

### 8. Reference image capacity

Up to ~14 reference images per request (a few at high fidelity). For decks, 0–2
is usually enough: one to anchor a recurring character, one for a
background/mood. More only for multi-element scenes.

---

## Prompt template (use this for every generation)

```
[CONTEXT]
Why this visual exists, which slide it goes on, who will see it.

[STYLE]
<the brand STYLE block assembled from brand/tokens.css + brand/guidelines.md>

[CONTENT]
What is depicted — subject, composition, mood. Positive, concrete description.

[REFERENCE]            (only if using --ref)
Image 1 is <role>. Image 2 is <role>.

[IDENTITY LOCK]        (only for variations)
Keep these EXACTLY identical to Image 1: <(a), (b), (c)…>.

[CHANGE]               (only for variations)
The only thing that changes vs Image 1: <…>, described positively.

[FORMAT]
Aspect ratio <16:9 | 1:1 | 9:16>. Framing, margins, background colour.
Usually: no text in the image (overlay copy in the deck instead).
```

Write this prompt to a text file, then call the script.

---

## Operational workflow

1. **Check existing assets first.** Look in `assets/illustrations/`,
   `assets/photos/`, `assets/icons/`. If something fits, reuse it — don't burn
   API quota on a visual you already have.
2. **Read the brand** (`brand/tokens.css` + `brand/guidelines.md`) and assemble
   the STYLE block.
3. **Write the full prompt** to a prompt file (the doctrine + template above).
   A scratch path or a kept brief under `presentations/` are both fine; the
   sidecar records the path either way.
4. **Generate:**
   ```
   python3 scripts/gen-image.py --slug <slug> --prompt-file <path> [--ref ...] [--aspect 16:9]
   ```
   Output lands in `assets/illustrations/YYYY-MM-DD-<slug>.png` with a JSON
   sidecar beside it.
5. **Conformance check.** Inspect the PNG:
   - Only the brand palette is visible (the hex codes you specified).
   - Illustration style matches `guidelines.md`.
   - No banned trope present.
   - Aspect ratio and framing correct; no unwanted baked-in text.
   - For variations: identity preserved, only the intended thing changed.
   If one axis is off, prefer a targeted edit (pass the image back via `--ref`
   with a short instruction) over a full re-roll.
6. **Use it in the deck** by referencing the file from your slide HTML.

---

## Journaling (non-negotiable)

`scripts/gen-image.py` writes a **JSON sidecar** next to every image
(`assets/illustrations/YYYY-MM-DD-<slug>.json`) containing: slug, timestamp,
model, aspect ratio, reference images, the prompt file path, the **full prompt
sent**, the prompting method, and the brand source. This is the audit and replay
trail — it lets anyone reproduce or iterate on a visual later, and supports AI
disclosure. Never delete sidecars; treat them as part of the asset.

If you ever add another script that calls Gemini for an image, replicate the
sidecar so the generation stays reproducible.

---

## Gemini technical limits

- **Text in image** may render imperfectly — prefer "no text in the image" and
  overlay copy in the deck. If you do bake in a number/word, check spelling.
- **Real logos** aren't reliably reproduced — composite your logo
  (`assets/logos/`) over the generated image in the deck instead of asking the
  model to draw it.
- **Negations** — reframe positively where possible (doctrine #7).
- **Reference fidelity** is strong on shapes, colours and signature traits, but
  weak on poses or backgrounds the source image never shows.

## Usage rules

- Don't generate a recognisable real person's face without consent.
- Don't reproduce a third party's logo or a named living artist's protected
  style.
- Keep output consistent with the brand voice in `brand/guidelines.md`.
- Follow your brand's AI-disclosure policy when publishing AI-generated visuals;
  the sidecar preserves the provenance regardless.
