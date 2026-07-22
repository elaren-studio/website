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

## External state not yet verified

- Live GitHub visibility and remote freshness
- Authenticated hosting project and repository connection
- Production build branch
- FormSubmit account ownership
- Plausible account ownership

No GitHub, hosting, DNS, form, or analytics setting was changed during local relocation.

## Next actions

1. Restore authenticated GitHub access.
2. Verify the hosting project and deployment connection.
3. Decide whether to transfer or rename the remote into an Elaren GitHub organization.
4. Update deployment documentation from authenticated evidence.
