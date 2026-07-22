# Elaren Studio Website

Public website repository for Elaren Studio and elarenstudio.com.

This repository owns website source, public copy, site-specific design implementation, SEO, analytics configuration, forms, deployment instructions, and website decisions. Company strategy, portfolio planning, and master brand direction belong in the private Elaren HQ repository.

## Stack

- Astro 5
- TypeScript in strict mode
- Tailwind CSS 4
- MDX content collections
- Playwright for PDF generation and browser-oriented tooling

## Commands

    npm ci
    npm run dev
    npm run validate
    npm run build
    npm run preview

Run validate and build before pushing.

## Content systems

The site currently has two intentional content paths:

1. Legacy public pages under elaren_site_content, read by static Astro page modules.
2. Astro content collections under content/resources and content/seo-pages.

Do not describe all content as living in only one folder. See RUNBOOK.md for schemas and authoring instructions.

## Repository structure

    content/                 MDX resources and SEO landing pages
    elaren_site_content/     Markdown used by legacy/static public pages
    public/                  Published static assets
    scripts/                 Validation and PDF-generation tools
    src/                     Astro components, layouts, libraries, and routes
    docs/                    Current context, decisions, roadmap, and worklog
    RUNBOOK.md               Website operating reference

## Integrations

- Production domain configured in Astro: https://elarenstudio.com
- Lead forms: FormSubmit
- Analytics: Plausible
- Sitemap: Astro sitemap integration

The production hosting provider and repository connection must be verified in the authenticated provider portal before a GitHub transfer or rename. No hosting configuration file in this repository proves the live connection.

## Brand boundary

Website implementation details are in docs/brand-implementation.md. Master positioning, naming, and brand-source assets are canonical in:

    /Volumes/Felix-SSD-1/Cursor Projects/Elaren/hq/docs/brand

Keep the website independently buildable. Do not copy private portfolio or company-operating documents into this repository.

## Handoff

Start with docs/ACTIVE_CONTEXT.md and RUNBOOK.md. Record durable changes in docs/DECISIONS.md and append substantial work to docs/WORKLOG.md.
