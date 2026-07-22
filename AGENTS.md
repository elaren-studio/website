# Repository Guidelines

## Scope

This repository owns the Elaren Studio public website. Keep website source, public copy, site-specific design implementation, SEO, analytics, forms, deployment instructions, and website handoff material here.

Do not place company strategy, product roadmaps, master brand-source assets, or confidential client deliverables here. Link to the private HQ repository when studio context is required.

## Start here

Before substantial work, read:

- docs/ACTIVE_CONTEXT.md
- docs/ROADMAP.md
- docs/DECISIONS.md
- RUNBOOK.md

After substantial work, update current context and append to docs/WORKLOG.md.

## Commands

- npm ci
- npm run validate
- npm run build
- npm run dev

Run validate and build before pushing.

## Safety

- Never commit secrets.
- Treat FormSubmit and Plausible identifiers already present in public source as configuration, not proof of account ownership.
- Verify authenticated hosting and GitHub state before transfer, rename, deployment, or DNS changes.
- Keep generated output, test results, local AI chat history, and dependencies out of Git.
