# Brand configuration

Two files drive every presentation's visual identity:

- **`tokens.css`** — CSS custom properties (colors, fonts, motion). Inlined into every generated deck.
- **`guidelines.md`** — design rules, voice, do/don'ts. Read by the agent before generating slides.

Both are populated automatically when you first open the project — the agent will ask for your brand's website URL, fetch it, and fill these files. You can edit them by hand at any time afterwards.

## Editing tokens.css by hand

Replace placeholder values. All colours referenced in the slide templates resolve through these custom properties, so a single edit propagates everywhere.

```css
:root {
  --brand-primary: #YOURCOLOR;
  --brand-secondary: #YOURCOLOR;
  --brand-accent: #YOURCOLOR;
  --brand-neutral-light: #FAFAFA;
  --brand-neutral-dark: #1B1F25;
  --font-display: 'Your Display Font', sans-serif;
  --font-mono: 'Your Mono Font', ui-monospace, monospace;
}
```

## Editing guidelines.md by hand

This is freeform markdown. Useful sections to maintain:

- Tone of voice (3–5 adjectives, plus banned words)
- Typographic system (size scale, weight pairings)
- Color usage rules (primary/secondary ratios, dark vs light slides)
- Motion principles (easing, stagger, no-go animations)
- Iconography style
- Photography style

The richer this file, the more on-brand the output.
