# Website Brand Implementation

Last updated: July 22, 2026

## Ownership

This document describes website implementation. The private HQ repository owns Elaren Studio positioning, naming, voice, master visual identity, and source-asset decisions.

Canonical HQ location:

    /Volumes/Felix-SSD-1/Cursor Projects/Elaren/hq/docs/brand

## Implemented palette

- Ink: #101317
- Accent: #3A78FF
- Slate 900: #0F1720
- Slate 100: #E6EAF0
- Paper: #FFFFFF

The code under src/styles and the Tailwind configuration are authoritative for rendered values.

## Implemented typography

- Sans: Inter with system fallbacks
- Serif: Source Serif 4 with serif fallbacks

## Website language

The public site currently centers the line Bright, enduring websites. Public copy remains canonical in route and content files, not in this implementation note.

## Asset rule

- Master and draft brand sources belong in HQ.
- Only optimized assets actively published by the website belong in public.
- A local draft logo is not a website asset until code references it and a website decision approves it.

## Accessibility

Maintain WCAG AA contrast, semantic structure, keyboard access, visible focus, and reduced-motion support where animation exists. Run the project validation and production build before pushing.
