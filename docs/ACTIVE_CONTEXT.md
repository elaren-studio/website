# Active Context

Last updated: July 22, 2026

## Current state

- This is the canonical local Elaren Studio website checkout.
- Local path: /Volumes/Felix-SSD-1/Cursor Projects/Elaren/website
- Git history and tags were cloned from the former elaren_studio_com checkout.
- Current remote remains https://github.com/fdtorres1/elaren-studio.git.
- Current production domain configured in source is https://elarenstudio.com.
- The site uses Astro, TypeScript, Tailwind, MDX content collections, FormSubmit, and Plausible.
- A clean dependency install, link validation, and production build passed from this relocated checkout on July 22, 2026.
- The production build generated 27 static pages.

## Repository boundary

This repository owns website implementation and public copy. Elaren company strategy, portfolio planning, naming, and master brand-source assets are canonical in the sibling HQ repository.

## Migration boundary

- The clean clone intentionally excluded node_modules, dist, .astro, SpecStory history, test output, and generated PDF output.
- Former untracked raster logo drafts were catalogued in HQ, not added to website public assets because no website code referenced them.
- The tracked legacy zip snapshot was retired; active elaren_site_content files remain because current routes read them.
- The stale SETUP.md was retired in favor of README.md and RUNBOOK.md.

## Verified external state

- Elevated GitHub CLI authentication is active for fdtorres1.
- The live remote is the public fdtorres1/elaren-studio repository, and fdtorres1 has ADMIN permission.
- The live default branch is main at c33f0fc. This local main is one unpushed commit ahead at e6a2e45.
- GitHub records Preview and Production environments.
- The latest Production deployment for c33f0fc completed successfully through a Vercel target URL on March 3, 2026.
- Main is not branch-protected.

## External state not yet verified

- Direct Vercel account ownership and project settings
- Custom-domain attachment for elarenstudio.com
- Production build settings and branch inside Vercel
- FormSubmit account ownership
- Plausible account ownership
- Final GitHub organization and repository name

No GitHub, hosting, DNS, form, or analytics setting was changed during local relocation.

## Next actions

1. Decide whether the repository remains under fdtorres1 temporarily or moves to a newly created Elaren organization.
2. Verify the Vercel project and elarenstudio.com attachment directly.
3. Account for the likely Production deployment before pushing the local documentation commit.
4. Update deployment documentation after direct Vercel verification.
