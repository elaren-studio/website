# Active Context

Last updated: July 22, 2026

## Current state

- This is the canonical local Elaren Studio website checkout.
- Local path: /Volumes/Felix-SSD-1/Cursor Projects/Elaren/website
- Git history and tags were cloned from the former elaren_studio_com checkout.
- Canonical remote is https://github.com/elaren-studio/website.git.
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
- The public repository was transferred and renamed from fdtorres1/elaren-studio to elaren-studio/website. GitHub preserved repository ID 1092039889, history, main, environments, and the former-path redirect; fdtorres1 retains ADMIN permission.
- The live default branch is main at 510b4c5, and local main matches origin/main.
- GitHub records Preview and Production environments.
- The authenticated Vercel project is felixs-projects-a5ff4c9b/elaren-studio, project ID prj_xFdQeKvaDH8l5LeD4smVEUxmM2FX.
- Vercel is connected to GitHub repository ID 1092039889 at elaren-studio/website with production branch main, Astro preset, repository-root builds, and Node.js 22.x.
- The Vercel GitHub App is installed on elaren-studio with selected-repository access limited to website.
- elarenstudio.com remains attached to the Vercel project with the intended Vercel nameservers.
- The first post-transfer Git push of 728a060 created Vercel Production deployment dpl_8Q7CHcYRb4Ykj9jGMwthhpZcdg8F. Vercel and GitHub report success, the deployment is Ready, and elarenstudio.com is attached and returns HTTP 200.
- The push of 510b4c5 created Vercel Production deployment dpl_Gr3LTi7ZdgQud5MvSz6CgbzoUozB, which is Ready and aliased to elarenstudio.com.
- Main is not branch-protected.

## External state not yet verified

- FormSubmit account ownership
- Plausible account ownership

The repository owner, name, local origin, and Vercel Git connection changed successfully. The Vercel project, domain, DNS, form, and analytics settings did not change.

## Next actions

1. Continue running validation and a production build before pushes to main.
2. Verify FormSubmit and Plausible account ownership separately when needed.
