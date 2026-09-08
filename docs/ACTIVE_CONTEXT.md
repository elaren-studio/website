# Active Context

Last updated: September 8, 2026

## Search Console authorization and sitemap submission verified September 8, 2026

- The additive Google OAuth upgrade succeeded in the verified owner account: all 19 original scopes were retained and `https://www.googleapis.com/auth/webmasters` was added, for 20 total scopes with zero removals. Refresh and identity were verified. No credentials, backup paths, or private audit identifiers are recorded here.
- The Elaren sitemap index `https://elarenstudio.com/sitemap-index.xml` was submitted at 16:49:08 UTC. The PUT returned HTTP 204; the initial GET readback succeeded and accepted the submission pending processing, with zero errors and zero warnings.
- Current Search Console inspection shows the homepage `Crawled - currently not indexed`, with the expected canonical `https://elarenstudio.com/` and last crawl August 30, 2026. The three new content-marketing pages remain `URL is unknown to Google`.
- Search Console accepted four individual indexing requests into its priority crawl queue: `/`, `/content-marketing/`, `/work-examples/program-campaign/`, and `/resources/guides/what-to-send-a-content-partner/`. Requests are complete; later indexing remains unverified.

## Technical foundation verified September 7, 2026

- The September 7 baseline showed the homepage indexed with the expected canonical and an August 30 crawl. The September 8 inspection above supersedes that index status. Domain owner access remains verified.
- The live sitemap index returns HTTP 200 and points to `sitemap-0.xml`. Search Console lists the index with zero errors/warnings and a February 25 last-download timestamp. The September 8 submission is recorded above; initial readback accepted it pending processing.
- A clearly labeled synthetic inquiry from the owner's external iCloud mailbox reached the Google inbox addressed and delivered to `hello@elarenstudio.com`, with exact body integrity and SPF/DKIM/DMARC passing. The production composer prepared the expected recipient/body. The browser connection became unavailable before a repeat copy test; earlier desktop/mobile preparation/copy checks remain recorded below.
- These checks concern the content-marketing email route. They do not verify the separate legacy FormSubmit integration or establish conversions. Private email identifiers and message evidence stay outside the public repository.

## Production release verified September 7, 2026

The user authorized merging the content marketing branch into `main`. GitHub merge commit `601873983159a660fea4e68dc3e1dd3ffffd20b4` triggered Vercel Production deployment `6312066835`, which completed successfully at 15:49:01 UTC. All three new public routes returned HTTP 200 from Vercel with their expected page content: `/content-marketing/`, `/work-examples/program-campaign/`, and `/resources/guides/what-to-send-a-content-partner/` on `https://elarenstudio.com`.

This production record supersedes earlier feature-branch-only release boundaries below. Actual inquiry delivery, indexing, search appearance, and conversion outcomes were not tested by this release check.

## Current state

- This is the canonical local Elaren Studio website checkout.
- Local path: /Volumes/Felix-SSD-1/Cursor Projects/Elaren/website
- Git history and tags were cloned from the former elaren_studio_com checkout.
- Canonical remote is https://github.com/elaren-studio/website.git.
- Current production domain configured in source is https://elarenstudio.com.
- The site uses Astro 7, TypeScript, Tailwind CSS 4, MDX content collections, FormSubmit, and Plausible.
- The site presents Elaren Studio as an app studio and dev shop per D-007; therapist and local-SEO pages remain live but unlinked from navigation.
- Dependencies were fully updated on July 29, 2026, including the Astro 5-to-7 and MDX 4-to-7 majors; npm audit reports zero vulnerabilities.
- The production build currently generates 34 static pages.
- The therapist offering was repriced on August 9, 2026: Website Launch $500 founding client rate (standard $1,200), Essentials $49/mo (formerly WaaS Starter $99), Care+ $129/mo (formerly WaaS Care+ $199), plus a +$750 copywriting add-on; /therapist-websites gained an AI-builder comparison section, and pricing.ts, the city SEO pages, resource guides, and llms-full.txt were synchronized.
- /studioregister is a Studio Register product landing page added on July 23, 2026 to support Stripe business verification; it follows the product's legal-naming boundary (An Elaren Studio product; owned and operated by Wright Torres Group, LLC; no d/b/a language) and may later grow into a fuller product site.
- Therapist offering repriced August 9, 2026 for Facebook-group promotion: Website Launch $500 founding rate (standard $1,200), Essentials $49/mo (was WaaS Starter $99), Care+ $129/mo (was WaaS Care+ $199), plus a +$750 copywriting add-on; synchronized across the therapist page, src/lib/pricing.ts, city SEO pages, resource guides, and llms-full.txt.

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
- Local main matches origin/main; check git for the current head rather than relying on a pinned commit in this document.
- GitHub records Preview and Production environments.
- The authenticated Vercel project is felixs-projects-a5ff4c9b/elaren-studio, project ID prj_xFdQeKvaDH8l5LeD4smVEUxmM2FX.
- Vercel is connected to GitHub repository ID 1092039889 at elaren-studio/website with production branch main, Astro preset, repository-root builds, and Node.js 22.x.
- The Vercel GitHub App is installed on elaren-studio with selected-repository access limited to website.
- elarenstudio.com remains attached to the Vercel project with the intended Vercel nameservers.
- Pushes to main reliably create Ready Production deployments aliased to elarenstudio.com; the deployment history is recorded in WORKLOG.md.
- Preview deployments are protected by Vercel SSO.
- Main is not branch-protected.

## External state not yet verified

- FormSubmit account ownership
- Plausible account ownership

The repository owner, name, local origin, and Vercel Git connection changed successfully. The Vercel project, domain, DNS, form, and analytics settings did not change.

## Next actions

1. Continue running validation and a production build before pushes to main.
2. Verify FormSubmit and Plausible account ownership separately when needed.

## September 7, 2026 content marketing implementation

- Added `/content-marketing` service page with scoped pricing, boundaries, visible FAQs, Service structured data, and a mailto-only inquiry composer addressed to the existing public `hello@elarenstudio.com` route.
- Added fictional demonstration route `/work-examples/program-campaign` and guide resource `/resources/guides/what-to-send-a-content-partner`.
- Linked the new services from `/services`, the footer, and cross-linked examples and guides. Updated `public/llms.txt` with the new offers/resources.
- This implementation is merged to main and deployed to production as recorded above. Validation/build and root desktop/mobile browser QA passed, including offer navigation, FAQ, inquiry preparation/copy, and both themes. No external inquiry was sent, no indexing/analytics outcome is claimed, and no credentials or third-party integrations were added.

### Source publication

First push verified September 7, 2026 at 15:18 UTC: commit `5d08255483e3b3bd8dea80ca04b6a858854c5fde` is on `origin/feature/marketing-offer-2026-09-07` in `elaren-studio/website`. `git ls-remote` returned the same full SHA as local HEAD after the successful push. This documentation follow-up records that evidence, as requested. Main and production deployment are not part of the branch push; read the remote branch for the latest documentation commit.
