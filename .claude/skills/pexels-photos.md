---
name: pexels-photos
description: Illustrate slides with real photographs from Pexels (free API) without falling into stock-photo clichés. Searches with concrete queries, judges results on a numbered contact sheet, downloads the chosen photo into assets/photos/ with a credit sidecar, optionally bakes a brand-tinted variant (mono / duotone from brand/tokens.css), places it in the slide, checks legibility, and generates the closing photo-credits slide. Requires a free PEXELS_API_KEY in .env (docs/pexels-setup.md walks the user through it). Use when a slide beat calls for a real place, material, object, gesture or atmosphere, or when the user asks for a photo on a slide.
---

# Skill — pexels-photos

Find, place and credit real photographs from Pexels through
`scripts/pexels.py`. The script does the mechanics; this skill carries the
judgement: which slides deserve a photo, which photo, and how it sits in an
editorial deck.

## When to invoke

- "Put a photo on slide 5" / "illustrate the cover with a photo"
- "Find a picture of [place / object / scene] for this deck"
- While building a deck, when a beat is concrete (a place, a material, an
  object, a gesture, an atmosphere) and its layout takes an image.

**Not for:** concepts and metaphors ("growth", "trust", "AI"), characters,
mascots, diagrams (use `generate-image` or typography), product screenshots
(capture them), logos (see `create-slides`, phase 4).

## Optional capability — read this first

Pexels is **optional**. Check for the key before promising photos:

```bash
python3 scripts/pexels.py check
```

- **Key works** → proceed.
- **Key missing** → the script prints the setup steps. Offer once to walk the
  user through `docs/pexels-setup.md`, one step at a time (see "Step 5b" in
  `CLAUDE.md`). Never ask for the key in chat: the user pastes it into `.env`
  themselves. If they decline, build the slide without a photo and move on;
  never block a deck on Pexels.

---

## Visual priority order

For every slide that wants an image, walk this list and stop at the first
match:

1. **The user's own photos** in `assets/photos/` (non-`pexels-*` files). Real
   material from the brand always beats stock.
2. **A photo already downloaded** for this deck (`assets/photos/pexels-*`),
   when it genuinely fits. Reuse before searching.
3. **Pexels**, for the real: places, materials, objects, hands at work,
   weather, light, landscapes, architecture, documentary scenes.
4. **`generate-image`**, for what can't be photographed: concepts, metaphors,
   recurring characters, brand illustrations.
5. **Typography alone.** A strong sentence on a clean plate beats a weak photo.

## Where photos belong, and how many

- Layouts that take a photo: **Family 8 — Photography** in
  `reference/LAYOUTS.md` (`plate`, `diptych`, `letterbox-band`,
  `margin-figure`, `scale-contrast`, `typology-grid`, `sequence-strip`; code
  in `templates/components.md` → "Photography layouts"), plus `cover`,
  `fullbleed`, `split-visual`, `quote-portrait` and `split-illus`.
- Match the search to the layout: `--orientation portrait` for `plate`,
  `margin-figure` and `sequence-strip` (4:5), `landscape` for `diptych`,
  `letterbox-band` and `scale-contrast`, `square` for `typology-grid`.
  `field-notes` is for the user's own site photos only: a Pexels photo can't
  be passed off as the client's site.
- **Dosage:** at most about one slide in four carries a photo. Never two photo
  slides in a row unless the rhythm is deliberate (a photo essay beat).
- A photo must carry the slide's idea or its mood. Decoration is a reason to
  cut, not to add.

## Anti-stock doctrine (non-negotiable)

Reject, every time, even if nothing better turns up on the first search:

- handshakes, people in suits, smiling faces looking at the camera, teams
  laughing around a laptop, thumbs up, high fives
- lightbulbs, puzzle pieces, chess pieces, dartboards, arrows, ladders,
  mountain summits with raised arms
- robot hands, glowing brains, blue circuit boards, blurred code on screens
- heavy HDR, tilted "dynamic" angles, obvious staging, watermark-like
  overlays, text baked into the photo

Prefer: documentary framing, natural light, a single clear subject, negative
space where the text will sit, textures and materials, places without people
or with people absorbed in what they're doing.

### Writing queries

- **English, concrete nouns + light + material:** `concrete stairwell morning
  light`, `harbour at dawn fog`, `hands kneading bread flour`, `empty
  library oak tables`. English queries return far better results even for a
  French deck.
- Never abstract nouns (`success`, `innovation`, `teamwork`, `future`): they
  return exactly the clichés above.
- Too literal and nothing good comes back? Go one step more atmospheric
  (`warehouse light shafts` instead of `logistics`).
- Match the frame: `--orientation landscape` for full-bleed and covers,
  `portrait` for a tall split column, `square` for mosaics.
- `--color brand-primary` (any token name from `brand/tokens.css`, or a hex)
  biases results towards the brand palette. Useful for covers; don't
  over-use it, it narrows results fast.

## Deck consistency

- **One treatment per deck.** Read `brand/guidelines.md → Photography &
  illustration → Photo treatment` (`raw`, `mono` or `duotone`) and apply it to
  every photo in the deck. If the field is empty, use `raw` and say so.
- **One light.** Keep the colour temperature and contrast coherent across
  photos (all soft daylight, or all low warm light). A cold blue office next to
  a golden-hour field reads as two decks.
- **One distance.** Mix wide and close shots on purpose, not at random.

---

## The autonomous loop

For each slide that needs a photo:

1. **Search**

   ```bash
   python3 scripts/pexels.py search "harbour at dawn fog" --orientation landscape
   ```

   Prints one line per result (`#n  id  WxH  photographer · alt`) and writes
   `.cache/pexels/<query>/sheet.jpg`, a numbered contact sheet of every
   result, plus `results.json`.

2. **Look at the sheet.** Read `sheet.jpg` (one image, all candidates). Apply
   the doctrine, then judge: does it carry the slide's idea, is there calm
   space where the text goes, is the subject strong at slide size, does it
   match the deck's light and treatment? If nothing passes, **re-query** with
   different concrete words (up to 3 queries); settling for a cliché is
   never acceptable. Still nothing: fall back to the priority order above.

3. **Download**

   ```bash
   python3 scripts/pexels.py get 1234567 --slug harbour-dawn --treatment duotone
   ```

   Writes `assets/photos/pexels-harbour-dawn-1234567.jpg` (2400px wide by
   default; `--width 1600` is plenty for a half-frame column), the brand-tinted
   variant `…-duotone.jpg` when `--treatment` is set, and the sidecar
   `pexels-harbour-dawn-1234567.json` (photographer, links, alt text, query).
   Keep the sidecar: the credits slide is generated from it.

4. **Place it** (see below), then **check it**:

   ```bash
   python3 scripts/shots.py presentations/<deck>.html <slide-number>
   ```

   Read the PNG. The text must read at a glance; the subject must not sit under
   the title; the crop must not cut a face or the key object. Adjust
   `object-position` or the veil, or pick another photo.

5. **Report.** In your end-of-deck summary, list each photo: slide number,
   photographer, Pexels URL (from the sidecar). The user can then ask for a
   swap in one sentence ("slide 5: something emptier").

## Placing a photo in the deck

- Reference it with a **relative path** from the deck:
  `../assets/photos/pexels-<slug>-<id>.jpg` (or the `-mono` / `-duotone`
  variant). The deck ships alongside its `assets/` folder.
- **Full-bleed:** use the `.slide-bg` block already in `templates/base.html`
  (it carries the readability veil and the z-index discipline):

  ```html
  <div class="slide-bg"><img src="../assets/photos/pexels-harbour-dawn-1234567-duotone.jpg" alt="Fishing boats moored in a foggy harbour at dawn"></div>
  ```

- **In a column or frame:** `<img>` with `width:100%; height:100%;
  object-fit:cover;` and set `object-position` (e.g. `30% 60%`) to keep the
  focal point in frame.
- **`alt`:** take the sidecar's `alt`, rewrite it as one short, factual sentence
  in the deck's language.
- **No CSS `filter`, `mix-blend-mode` or `backdrop-filter` on photos.** They
  render differently in the PDF export. Brand tinting is baked into the file
  by `--treatment`.
- Never put a credit line on the photo slide itself: credits live on the
  closing slide.

## Credits (mandatory when any Pexels photo is used)

Generate the closing slide from the deck itself, then paste it as the **last**
slide (after `cta-final`), with the `photo-credits` CSS from
`templates/components.md`:

```bash
python3 scripts/pexels.py credits presentations/<deck>.html --lang fr
```

It lists each photographer with the slide numbers where their photo appears
and links to Pexels, which is what the Pexels API guidelines ask for. Re-run
it after any photo change. A warning means a `pexels-*` file has no sidecar:
credit that photo by hand or re-download it with `get`.

## Quota and cache

- 200 requests per hour, 20,000 per month. `check` shows what's left.
- `search` costs one request (thumbnails are free); `get` costs one.
- Results are cached in `.cache/pexels/<query>/`. Before re-running a search,
  reread the cached `results.json` and `sheet.jpg`.

## Licence and usage rules

- The [Pexels License](https://www.pexels.com/license/) allows free use,
  including commercial use and modification. Attribution is appreciated; the
  credits slide provides it.
- Never show identifiable people in a negative or misleading context, never
  suggest that a person in a photo endorses the brand, and never use a photo
  as a logo or trademark.
- Downloaded photos belong to the deck's project. If you are working in the
  public `slides-agent` template itself rather than a copy of it, don't commit
  them there.
