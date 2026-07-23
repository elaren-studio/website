# Elaren Studio — Runbook

Operational reference for [elarenstudio.com](https://elarenstudio.com). Start here when working on the site.

---

## Stack

| Layer        | Tool                          |
|-------------|-------------------------------|
| Framework   | Astro 5 (static output)       |
| Styling     | Tailwind CSS 4                |
| Content     | MDX via `@astrojs/mdx`        |
| RSS         | `@astrojs/rss`                |
| Sitemap     | `@astrojs/sitemap` (auto)     |
| Forms       | FormSubmit (third-party)      |
| PDF gen     | Playwright (dev only)         |
| Hosting     | Vercel                       |

Config: `astro.config.mjs` — site URL, integrations, Vite plugins.

---

## Commands

```
npm run dev        # Local dev server (typically localhost:4321)
npm run build      # Production build → dist/
npm run preview    # Preview production build locally
npm run validate   # Check SEO page links + slug collisions
npm run astro      # Astro CLI passthrough
```

Always run `build` and `validate` before pushing.

---

## Deployment and Git Integration

- Canonical repository: `https://github.com/elaren-studio/website`
- Vercel scope and project: `felixs-projects-a5ff4c9b/elaren-studio`
- Vercel project ID: `prj_xFdQeKvaDH8l5LeD4smVEUxmM2FX`
- Production branch: `main`
- Project root: repository root
- Framework preset: Astro
- Node.js version: 22.x
- Production domain: `https://elarenstudio.com`

The Vercel GitHub App is installed on the `elaren-studio` organization with selected-repository access limited to `website`. A push to `main` is expected to create a Production deployment. Run `npm run validate` and `npm run build` first, then verify the resulting deployment and domain alias.

The local `.vercel/` link metadata and `.env*` files are ignored. Never commit Vercel tokens or downloaded environment files.

Useful authenticated checks:

```
vercel project inspect elaren-studio
vercel inspect https://elarenstudio.com
vercel domains inspect elarenstudio.com
```

---

## Project Structure

```
├── content/
│   ├── resources/            # MDX content for resource articles
│   └── seo-pages/            # MDX content for SEO landing pages
├── public/
│   ├── favicon.svg
│   ├── robots.txt            # Crawl directives + sitemap + LLMs-Txt
│   ├── llms.txt              # Structured summary for AI models
│   └── llms-full.txt         # Full Markdown content for AI models
├── scripts/
│   ├── validate-links.ts     # Link + slug collision validator
│   └── generate-pdf.mjs      # PDF generation via Playwright
├── src/
│   ├── components/
│   │   ├── seo/              # Reusable components for SEO pages
│   │   ├── Breadcrumbs.astro # Breadcrumb nav + BreadcrumbList JSON-LD
│   │   ├── ResourceCard.astro # Resource card for index grid
│   │   ├── RelatedResources.astro # Related resources section
│   │   ├── TableOfContents.astro  # Auto-generated TOC from headings
│   │   ├── Header.astro
│   │   ├── Footer.astro
│   │   ├── TherapistCta.astro
│   │   └── ...               # Cards, headings, and section components
│   ├── layouts/
│   │   └── BaseLayout.astro  # Global layout (head, meta, OG, RSS)
│   ├── lib/
│   │   ├── cta-presets.ts    # CTA preset definitions + resolver
│   │   ├── pricing.ts        # Centralized plan pricing
│   │   ├── resources.ts      # Resource utilities, scoring, formatting
│   │   ├── seo-pages.ts      # Related pages scoring + structured data
│   │   └── icons.ts          # Shared SVG icon registry
│   ├── pages/
│       ├── [slug].astro      # Dynamic route for SEO content pages
│       ├── resources.astro   # Resource index (card grid + filtering)
│       ├── resources/[...slug].astro  # Resource article template
│       ├── rss.xml.ts        # RSS feed endpoint
│       ├── index.astro
│       ├── therapist-websites.astro  # Main money page
│       └── ...               # Static pages
│   ├── styles/
│   │   └── global.css
│   └── utils/                # markdown helpers
└── src/content.config.ts     # Content collection schemas (Zod)
```

---

## SEO Content System

SEO landing pages use Astro's content collections. Content lives in MDX files; the template and shared sections are handled by components.

### How it works

1. **Content entries** live in `content/seo-pages/*.mdx`
2. **Schema** is defined in `src/content.config.ts` (validated by Zod at build time)
3. **Dynamic route** `src/pages/[slug].astro` renders each entry
4. The filename (minus `.mdx`) becomes the URL slug: `therapist-website-design-dallas.mdx` → `/therapist-website-design-dallas`

### Adding a new SEO page

1. Create `content/seo-pages/your-page-slug.mdx`
2. Add required frontmatter (see schema below)
3. Write the MDX body using shared components
4. Add the slug to `relatedPages` in related entries (for cross-linking)
5. Run `npm run validate` to check links
6. Run `npm run build` to verify

### Frontmatter schema

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| `title` | string | yes | — | Page title (BaseLayout appends " \| Elaren Studio") |
| `description` | string | yes | — | Meta description |
| `h1` | string | yes | — | Main heading |
| `heroKicker` | string | yes | — | Small text above H1 |
| `heroSubtitle` | string | yes | — | Paragraph below H1 |
| `trustLine` | string | no | "Clear scope. No surprises. No long-term contracts." | Below subtitle |
| `ctaPreset` | "audit" \| "call" \| "contact" | no | "audit" | Selects CTA text + href from presets |
| `ctaText` | string | no | — | Overrides preset text for this page only |
| `ctaHref` | string | no | — | Overrides preset href for this page only |
| `finalCtaHeadline` | string | yes | — | Bottom CTA section heading |
| `finalCtaSubtext` | string | no | — | Supports HTML (rendered with `set:html`) |
| `vertical` | string | yes | — | Topic cluster (e.g., "therapist") |
| `geo` | string | no | — | City/area slug (e.g., "dallas") |
| `region` | string | no | — | Broader region (e.g., "dfw") |
| `pageType` | "geo" \| "vertical" \| "practice-type" | yes | — | Determines pricing variant + cross-link scoring |
| `relatedPages` | string[] | no | [] | Slugs of manually linked pages |
| `areaServed` | object | no | — | Schema.org structured data: `{ type, name, state? }` — `type` must be one of "City", "State", "Country", "AdministrativeArea" |
| `faqs` | array | no | [] | `{ q, a }` pairs — generates FAQ section + FAQPage schema |
| `faqSectionTitle` | string | no | — (SeoFaq component default: "Frequently asked questions") | Custom FAQ heading |
| `faqSectionSubtitle` | string | no | — (SeoFaq component default: "Straightforward answers. No fine print.") | Custom FAQ subhead |

### Page type behavior

| `pageType` | Pricing variant | Use case |
|---|---|---|
| `geo` | stacked (3 cards) | City-specific pages |
| `vertical` | stacked | Topic/niche pages |
| `practice-type` | stepped (2-step flow) | Practice-type pages (e.g., group) |

### Cross-linking

Related pages are computed automatically via a scoring algorithm in `src/lib/seo-pages.ts`:

- Same `vertical`: +3 points
- Same `region`: +3 points
- Same `pageType`: +1 point

Manual `relatedPages` entries always appear first. Up to 4 related pages are shown per page.

The `validate` script checks that all `relatedPages` slugs resolve to actual MDX files and that no slug collides with an existing static page in `src/pages/`.

---

## Resource Content System

Resource articles (guides, teardowns, templates) use a second Astro content collection. Content lives in MDX files under `content/resources/`.

### How it works

1. **Content entries** live in `content/resources/*.mdx`
2. **Schema** is defined in `src/content.config.ts` (the `resources` collection)
3. **Dynamic route** `src/pages/resources/[...slug].astro` renders each entry
4. URLs are built from `type` + filename: `wright-wellness-before-after-teardown.mdx` with `type: teardown` → `/resources/teardowns/wright-wellness-before-after-teardown`

### Adding a new resource

1. Create `content/resources/your-slug.mdx`
2. Add required frontmatter (see schema below)
3. Write the MDX body (the template renders the H1 — don't include one in the body)
4. Run `npm run build` to verify

### Frontmatter schema

| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| `title` | string | yes | — | Article title (rendered as H1 by template) |
| `description` | string | no | "" | Meta description + card excerpt |
| `date` | string | no | — | Strict YYYY-MM-DD (Zod-validated). Enables Article schema + RSS |
| `type` | "teardown" \| "guide" \| "template" | yes | — | Determines URL prefix + grouping on index |
| `tags` | string[] | no | [] | For filtering, related scoring, and display |
| `vertical` | string | no | — | Maps to SEO page verticals for cross-system linking |
| `draft` | boolean | no | false | Set `true` to exclude from build |

### Type → URL mapping

| Type | URL prefix | Index section |
|---|---|---|
| `teardown` | `/resources/teardowns/` | Teardowns |
| `guide` | `/resources/guides/` | Guides |
| `template` | `/resources/templates/` | Templates |

### Features included automatically

- **Breadcrumbs** — UI + BreadcrumbList JSON-LD schema
- **Table of contents** — auto-generated from H2/H3 headings (shown when 3+ headings)
- **Reading time** — estimated from word count (200 wpm)
- **Publish date** — displayed if `date` is set
- **Related resources** — scored by shared type (+2), vertical (+3), and tags (+2 each)
- **Article JSON-LD** — emitted if `date` is present
- **RSS feed** — resources with dates appear at `/rss.xml`

### Cross-system linking

- **SEO pages → Resources:** SEO pages automatically show related resources that share the same `vertical`
- **Resources → SEO pages:** Add contextual links in the MDX body (e.g., link to `/therapist-websites`)

### Resource index

The index page at `/resources` features:

- Full-width card list (no grid)
- Client-side type filtering (buttons + URL parameter `?type=teardown`)
- Each card shows: type badge, date, reading time, title, description (tags hidden on index by default; `showTags` prop available)

---

## CTA Presets

**File:** `src/lib/cta-presets.ts`

| Preset | Text | Href |
|--------|------|------|
| `audit` (default) | Get a Free 10-Minute Website Audit | /therapist-websites#audit |
| `call` | Book a 15-Minute Call | /contact |
| `contact` | Start a Project | /contact |

### Changing the CTA site-wide

Edit the preset in `cta-presets.ts`. Every page using that preset updates automatically.

### Overriding for one page

In the MDX frontmatter:

```yaml
ctaPreset: audit
ctaText: "Custom Button Text Here"
```

The `ctaHref` stays from the preset unless also overridden.

---

## Pricing

**File:** `src/lib/pricing.ts`

Single source of truth for plan names, prices, descriptions, and billing periods. Used by:

- `src/components/seo/SeoPricing.astro` — rendered pricing cards
- `src/lib/seo-pages.ts` → `buildOfferCatalog()` — JSON-LD structured data

### Current plans

| Key | Name | Price | Billing |
|-----|------|-------|---------|
| `launch` | Website Launch | $500 | one-time |
| `starter` | WaaS Starter | $99 | monthly |
| `carePlus` | WaaS Care+ | $199 | monthly |

To change a price, edit `pricing.ts`. Both the visible UI and structured data update from that one file.

---

## Shared Components (SEO Pages)

All in `src/components/seo/`. Import them in MDX body content.

### Page-level (rendered by template, not MDX)

| Component | Purpose |
|-----------|---------|
| `SeoHero` | Hero section with H1, subtitle, trust line, CTA buttons |
| `SeoPricing` | Pricing section (stacked or stepped variant) |
| `SeoFaq` | Accordion FAQ section (from frontmatter `faqs`) |
| `SeoCta` | Final CTA section with primary + secondary buttons |
| `CrossLinks` | Auto-computed related pages grid |

### Body components (used in MDX)

| Component | Purpose | Key props |
|-----------|---------|-----------|
| `IconList` | Vertical list with icons | `items: { icon, title, desc? }[]` |
| `CardGrid` | 2-column card layout | `items: { title, desc, icon? }[]` |
| `CheckList` | Checkmark list | `items: string[]`, subtitle supports HTML |
| `StepTimeline` | Horizontal numbered steps | `steps: string[]`, subtitle supports HTML |
| `NumberedList` | Vertical numbered list | `items: string[]`, subtitle supports HTML |
| `Callout` | Bordered callout box | Uses `<slot />` for body content |
| `CtaBridge` | Inline mid-page CTA line | `text`, `linkText`, `href`, `suffix?` |
| `InteractiveChecklist` | Checkbox self-assessment | `items: string[]`, `footnote?` (HTML) |

### Common props (most body components)

- `bg`: `"paper"` (white) or `"muted"` (light gray) — alternate for visual rhythm
- `kicker`: Small uppercase label above the heading
- `title`: Section heading (H2)
- `subtitle`: Optional text below heading (some support HTML via `set:html`)

### Icon registry

**File:** `src/lib/icons.ts`

Named icon keys: `user`, `users`, `refresh`, `check`, `building`, `phone`, `globe`, `shield`, `box`, `chat`, `expand`, `frown`, `search`, `clock`, `lock`.

Use named keys in `IconList` and `CardGrid` items. Raw SVG path strings also work as a fallback.

---

## SEO Artifacts

### Sitemap

Auto-generated by `@astrojs/sitemap` on every build.

- Index: `https://elarenstudio.com/sitemap-index.xml`
- Pages: `https://elarenstudio.com/sitemap-0.xml`

Registered in `robots.txt`. Google Search Console can be pinged after significant page additions, but routine crawling picks up changes.

### Structured data (JSON-LD)

Each SEO page emits two schemas (injected by `[slug].astro`):

1. **ProfessionalService** — service type, area served, offer catalog
2. **FAQPage** — only if `faqs` array is non-empty

Built by `buildStructuredData()` and `buildFaqSchema()` in `src/lib/seo-pages.ts`.

Resource articles emit:

1. **Article** — headline, description, date, author/publisher (if `date` is set)
2. **BreadcrumbList** — navigation trail (via `Breadcrumbs` component)

### RSS feed

Auto-generated at `/rss.xml` from resources with dates. Discoverable via `<link rel="alternate">` in the HTML head (BaseLayout).

### LLM content

- `public/llms.txt` — structured summary (studio overview, services, values)
- `public/llms-full.txt` — full Markdown content of key pages
- `robots.txt` includes `LLMs-Txt:` directive

Update these manually when significant content changes are made.

### Meta / OG tags

Handled by `src/layouts/BaseLayout.astro`. Accepts `title`, `description`, and optional `ogImage` props. The title tag renders as `{title} | Elaren Studio`.

---

## Forms

The therapist websites page (`/therapist-websites`) uses [FormSubmit](https://formsubmit.co/) for lead capture. The form POSTs to FormSubmit's endpoint and redirects on success. Fields: name, email, practice name, current website URL, team size, timeline.

---

## Validation & Guardrails

### Link validator (`npm run validate`)

Checks two things:

1. Every slug in `relatedPages` frontmatter resolves to an actual `.mdx` file in `content/seo-pages/`
2. No SEO page slug collides with an existing static page in `src/pages/` (e.g., creating `pricing.mdx` would conflict with `pricing.astro`)

### Build-time schema validation

Zod validates all frontmatter fields at build time. Missing required fields or wrong types cause a build error with a clear message.

---

## Deployment Checklist

When adding new pages or making significant changes:

1. `npm run validate` — check links and slug collisions
2. `npm run build` — verify clean build
3. Spot-check locally with `npm run dev`
4. Push to GitHub
5. If new pages were added: consider pinging Google Search Console with the sitemap URL
6. If content changed significantly: update `public/llms.txt` and `public/llms-full.txt`

---

## Key Files Quick Reference

| What | Where |
|------|-------|
| Site config | `astro.config.mjs` |
| Content schemas | `src/content.config.ts` |
| SEO page content | `content/seo-pages/*.mdx` |
| SEO page template | `src/pages/[slug].astro` |
| Resource content | `content/resources/*.mdx` |
| Resource index | `src/pages/resources.astro` |
| Resource template | `src/pages/resources/[...slug].astro` |
| Resource utilities | `src/lib/resources.ts` |
| RSS feed | `src/pages/rss.xml.ts` |
| Breadcrumbs | `src/components/Breadcrumbs.astro` |
| Table of contents | `src/components/TableOfContents.astro` |
| CTA presets | `src/lib/cta-presets.ts` |
| Pricing config | `src/lib/pricing.ts` |
| Related pages logic | `src/lib/seo-pages.ts` |
| Icon registry | `src/lib/icons.ts` |
| Link validator | `scripts/validate-links.ts` |
| Global layout | `src/layouts/BaseLayout.astro` |
| Main money page | `src/pages/therapist-websites.astro` |
| Robots / LLM files | `public/robots.txt`, `public/llms.txt`, `public/llms-full.txt` |
