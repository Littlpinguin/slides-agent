# Brand configuration

Two files drive every presentation's visual identity:

- **`tokens.css`** — CSS custom properties (colors, fonts, motion). Inlined into every generated deck.
- **`guidelines.md`** — design rules, voice, do/don'ts. Read by the agent before generating slides.

Both are populated automatically when you first open the project — the agent will ask for your brand's website URL, fetch it, and fill these files. You can edit them by hand at any time afterwards.

## Editing tokens.css by hand

The file ships a neutral example palette (deep blue `#1E40AF`, amber `#F59E0B`, slate `#0F172A` on `#F8FAFC`, Inter and JetBrains Mono) so the starter works before onboarding. Replace those values with your brand's. All colours referenced in the slide templates resolve through these custom properties, so a single edit propagates everywhere.

```css
:root {
  --brand-primary: #YOURCOLOR;
  --brand-secondary: #YOURCOLOR;
  --brand-neutral-light: #YOURCOLOR;
  --brand-neutral-dark: #YOURCOLOR;
  --font-display: 'Your Display Font', system-ui, sans-serif;
  --font-mono: 'Your Mono Font', ui-monospace, monospace;
}
```

Then recompute the derived values next to them (`-deep`, `-soft`, `--rule`, `--rule-light`, `--label-accent`, `--label-accent-dark`): each one carries its formula in a comment, and `python3 scripts/qa.py` on your first deck tells you when a label falls under 4.5:1.

## Editing guidelines.md by hand

This is freeform markdown. Useful sections to maintain:

- Tone of voice (3–5 adjectives, plus banned words)
- Typographic system (size scale, weight pairings)
- Color usage rules (primary/secondary ratios, dark vs light slides)
- Motion principles (easing, stagger, no-go animations)
- Iconography style
- Photography style

The richer this file, the more on-brand the output.
