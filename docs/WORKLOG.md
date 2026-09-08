# Worklog

## 2026-09-08 - Search Console authorization and Elaren sitemap submission

- Completed the additive Google OAuth upgrade in the verified owner account; all 19 original scopes remained and `https://www.googleapis.com/auth/webmasters` was added, for 20 total scopes with zero removals. Refresh and identity were verified. No credentials, backup paths, or private audit identifiers were recorded in the repository.
- Submitted `https://elarenstudio.com/sitemap-index.xml` at 16:49:08 UTC. The PUT returned HTTP 204; the initial GET readback succeeded and accepted the submission pending processing, with zero errors and zero warnings.
- Current inspection shows the homepage `Crawled - currently not indexed`, with the expected canonical and August 30, 2026 last crawl; the three new content-marketing pages remain unknown to Google. Page indexing and canonical adoption remain pending later recrawl evidence.
- Search Console accepted four individual indexing requests into the priority crawl queue: homepage, content-marketing offer, campaign example, and preparation guide. No later indexing is claimed.
- Verification: link/slug validation and 34-page production build passed; documentation diff checks passed. No public-site source changed during this handoff update.

## 2026-07-22 - Canonical repository relocation

- Created a clean independent clone at /Volumes/Felix-SSD-1/Cursor Projects/Elaren/website.
- Preserved commit history, tags, main branch, and the existing GitHub remote.
- Added repository-native active context, roadmap, decisions, and worklog documents.
- Split master studio brand truth into the private HQ repository.
- Added a website-only brand implementation reference.
- Corrected README documentation for the two active content systems.
- Retired stale SETUP.md, the mixed studio brand kit, and the unused tracked content zip.
- Expanded ignores for generated output, test results, and local AI chat history.
- Installed the locked dependencies in a clean task worktree.
- Passed the link validator across four SEO pages and 13 static-route collision checks.
- Passed the production build, which generated 27 static pages.
- Made no production, GitHub, hosting, DNS, form, or analytics changes.

## 2026-07-22 - Elevated GitHub verification

- Verified elevated GitHub CLI authentication for fdtorres1.
- Verified ADMIN permission on the public fdtorres1/elaren-studio repository.
- Verified live main at c33f0fc and local main one unpushed commit ahead at e6a2e45.
- Verified GitHub Preview and Production environments and a successful Vercel-backed Production deployment for live main.
- Verified that main is unprotected.
- Left the local commit unpushed because the target organization is unresolved and a push is likely to trigger Production deployment.

## 2026-07-22 - GitHub organization boundary recorded

- Recorded creation of the free elaren-studio GitHub organization with fdtorres1 as its active administrator and sole member.
- Confirmed that the website remains in fdtorres1/elaren-studio and that no transfer, rename, push, or deployment change occurred.
- Deferred repository transfer until direct Vercel project and custom-domain verification is complete.

## 2026-07-22 - Website transferred and Vercel reconnected

- Captured the authenticated pre-transfer GitHub repository identity, Vercel project settings, production deployment, and custom-domain state.
- Transferred and renamed the public repository from fdtorres1/elaren-studio to elaren-studio/website while preserving GitHub repository ID 1092039889 and main at c33f0fc.
- Updated the canonical local origin and verified fetch access through the new URL; GitHub continues redirecting the former URL.
- Linked the local checkout to the existing Vercel project without creating a new project.
- Installed the Vercel GitHub App on elaren-studio with selected-repository access limited to website; hq and first-words were excluded.
- Reconnected Vercel to elaren-studio/website and verified repository ID 1092039889, production branch main, project-root builds, Astro, and Node.js 22.x.
- Verified that elarenstudio.com remains attached with intended nameservers and the existing Production deployment remains Ready.
- Triggered no deployment and left the pending website documentation commits unpushed.

## 2026-07-22 - First post-transfer Production deployment verified

- Pushed website main from c33f0fc to 728a060 at elaren-studio/website after link validation and a 27-page production build passed.
- Verified Vercel automatically created Production deployment dpl_8Q7CHcYRb4Ykj9jGMwthhpZcdg8F from the transferred repository connection.
- Verified Vercel Ready status, GitHub deployment success, the elarenstudio.com production alias, and an HTTP 200 response from the custom domain.
- Verified local main and origin/main were identical at 728a060 after the push.

## 2026-07-22 - Documentation review fixes

- Reviewed the five documentation-governance commits; link validation and the 27-page production build passed from the canonical checkout.
- Removed the duplicate trailing .env* pattern in .gitignore that silently re-ignored .env.example after the !.env.example exception; verified with git check-ignore that .env.example is tracked-eligible and .env.local stays ignored.
- Updated the recorded live main head from 728a060 to 510b4c5 in ACTIVE_CONTEXT.
- Recorded that the push of 510b4c5 created Vercel Production deployment dpl_Gr3LTi7ZdgQud5MvSz6CgbzoUozB, verified Ready, aliased to elarenstudio.com, and returning HTTP 200.

## 2026-07-22 - RUNBOOK accuracy audit and active-context unpinning

- Audited RUNBOOK.md against the actual codebase and corrected drift: FAQ section title/subtitle defaults live in the SeoFaq component rather than the Zod schema, the areaServed type enum and strict YYYY-MM-DD date validation are now documented, the lock icon and astro passthrough script are listed, and the project-structure tree gained favicon.svg, styles/, utils/, and a components ellipsis.
- Replaced the pinned live-head commit SHA in ACTIVE_CONTEXT with a non-pinning statement to end self-referential staleness; historical deployment records keep their SHAs.
- Verified CTA presets, pricing, cross-link scoring values, stack table, and remaining schema fields in RUNBOOK match the code exactly.

## 2026-07-23 - Repositioned the site as an app studio and dev shop

- Rewrote the homepage around the new positioning: "Software built with care, made to last," with studio products, client app builds, and websites as the three lanes and a products preview replacing the work preview.
- Added a Products page naming OpusGraph (live), AgentMeter (shipped, open source), Studio Register (in development), and OmniSearch (in development), with unnamed problem-space cards for earlier-stage work and a designed-and-built credit for the Resonance Music Press platform.
- Reframed Services to Product Builds, Custom Applications, and Websites, with conversation-driven inquiries and no public application pricing.
- Rewrote About and the legacy content files for the app-studio story; updated header navigation to Products, Services, Resources, About and refreshed the footer tagline and links.
- Removed therapist and local-SEO banners and navigation links while keeping those pages, pricing, plans, and work case studies live at their URLs.
- Rewrote llms.txt and synchronized llms-full.txt with the new copy, retaining legacy-offer references.
- Recorded D-007 here and D-012 in HQ; validation and the production build passed at 28 pages.

## 2026-07-23 - Repositioning refinement pass

- Replaced the site-wide BaseLayout default meta description and Organization JSON-LD, which still described a web design studio; the 404 page inherits the corrected fallback.
- Updated resources index, RSS feed description, and llms-full.txt to drop the retired bright-and-enduring tagline while keeping the website-focused resource framing.
- Broadened the terms page beyond Website-as-a-Service to cover per-engagement application work.
- Reframed the work index as selected website projects rather than the studio's whole identity, replaced the retired Standard Plan name with a monthly care plan, and aligned every remaining Start a Project CTA (header, work pages) to Start a conversation.
- Generalized the About clarity value from website-layout language to software language.
- Left cta-presets.ts unchanged because only the deliberately retained SEO pages consume it.

## 2026-07-29 - In-range dependency updates

- Updated all in-range dependencies: Astro 5.15.4 to 5.18.2, Tailwind CSS and its Vite plugin 4.1.17 to 4.3.3, and patch/minor bumps for the MDX, RSS, and sitemap integrations, Playwright, and tsx; only the lockfile changed.
- npm audit dropped from 17 vulnerabilities to 4; the remaining four require the Astro 7 major and do not apply to this site: no define:vars or server islands are used, the esbuild advisory is Windows dev-server only, and sharp only processes local trusted images at build time.
- Deferred the Astro 5-to-7 and @astrojs/mdx 4-to-7 major upgrades as a separate migration project.
- Link validation and the production build passed at 29 pages, including the new /studioregister landing page added since the last entry.

## 2026-07-29 - Astro 7 and MDX 7 major upgrade

- Upgraded astro 5.18.2 to 7.1.5 and @astrojs/mdx 4.3.14 to 7.0.5 on a branch with a Vercel preview build before merging.
- The only code break was a manual Fragment import in ServiceCard.astro that collided with the new Rust compiler's auto-injection; removed it.
- Moved the z import in content.config.ts from astro:content to astro/zod per the v6 deprecation; the existing schemas required no Zod 4 changes.
- Verified v7 output against a v5 snapshot: rendered text, JSON-LD blocks, rss.xml, and sitemap are identical across representative pages including MDX resources and SEO pages under the new Sätteri markdown pipeline.
- npm audit now reports zero vulnerabilities; production builds dropped from about 20 seconds to about 6.
- Updated the README and RUNBOOK stack references from Astro 5 to Astro 7.

## 2026-07-30 - Product landing pages and structured data

- Added /opusgraph and /agentmeter landing pages following the /studioregister pattern: product hero with the An Elaren Studio product kicker, feature grid, a product-specific trust section (OpusGraph audiences, AgentMeter privacy facts), status, and the D-010 legal attribution line.
- Added SoftwareApplication JSON-LD to all three product landing pages and an ItemList to /products; AgentMeter's schema records the MIT license and free pricing.
- Product cards on the homepage and /products now link to the on-site landing pages, which in turn link out to the live app and GitHub.
- Updated llms.txt (product URLs, Key Pages) and llms-full.txt (three new page sections) to include all product landing pages.
- Link validation and the production build passed at 31 pages.

## 2026-07-30 - Named CareLedger, OrchestraOS, and Mileage Pilot

- Added CareLedger, OrchestraOS, and Mileage Pilot to the products page as named in-development products per HQ decision D-013, with stage-accurate summaries and no landing pages yet.
- Retired the unnamed pet-care workshop entry now that CareLedger is named; music notation intelligence and bilingual early childhood remain unnamed.
- Extended the products ItemList JSON-LD to seven products and updated llms.txt and llms-full.txt to match.

## 2026-07-23 - Studio Register landing page for Stripe verification

- Added /studioregister, a Studio Register product landing page intended to support Stripe business verification and serve as the basis for a fuller product site later.
- Copy was sourced from the canonical product repository (README, PRODUCT.md, BRAND_AND_LEGAL.md): features, payments (deposit-per-booking through Stripe-hosted Checkout, no card data stored, agreement-governed cancellation/refund terms), in-development status, and hello@elarenstudio.com as booking/product support.
- Followed the product's legal-naming boundary: attribution reads "An Elaren Studio product," Wright Torres Group, LLC is identified as owner-operator, and no d/b/a language is used.
- Linked the Studio Register card on the Products page to /studioregister.
- Link validation and the production build passed at 29 pages, including /studioregister/index.html.

## 2026-08-09 - Therapist website repricing for the AI-builder era

- Repriced the unlinked therapist offering after market research against 2026 competitors (Brighter Vision, TherapySites, WebsiteTherapy, Empathysites, Wix/Squarespace/Durable AI builders): Website Launch stays $500 but is now framed as a founding client rate against a $1,200 standard rate; WaaS Starter $99/mo became Essentials $49/mo; WaaS Care+ $199/mo became Care+ $129/mo; added a +$750 "We write your pages" copywriting add-on.
- Research conclusion: the old monthly band was market-normal for therapist WaaS, but $500 was below the boutique floor and the "WaaS" naming plus hosting framing read as a required tax; the new structure lowers the monthly floor, differentiates on done-for-you copy, and supports promotion in a DFW counseling Facebook group.
- Added an honest "Couldn't I just use Wix or an AI site builder?" comparison section and FAQ to /therapist-websites, dropped WaaS jargon, and updated the JSON-LD offer catalog.
- Synchronized src/lib/pricing.ts (feeds the SEO city pages and their offer catalogs), the Dallas/Fort Worth/Houston MDX FAQs and trust lines, llms-full.txt, and the three resource guides' Elaren examples with recomputed totals (Essentials year 1 $1,088, 24 months $1,676; Care+ year 1 $2,048, 24 months $3,596); third-party market figures were left untouched. llms.txt had no therapist plan references.
- The /pricing, /plans, and /local-accelerator pages belong to the separate local-business offering and were intentionally not changed.
- Link validation and the production build passed at 31 pages.

## 2026-09-07 - Local offer and demonstration pages

- Added `/content-marketing` with visible scope, pricing, FAQs, Service JSON-LD, and a mailto-only inquiry composer.
- Added the fictional Northside Arts Workshop campaign example at `/work-examples/program-campaign`; no real-client, registration, award, or outcome claims are made.
- Added the content-partner guide and cross-linked services, example, resources, footer, and `public/llms.txt`.
- Pending `npm run validate`, `npm run build`, root browser QA, and any later deployment/indexing checks. No external messages or submissions were made.

- Final verification: `npm run validate`, `npm run build` (34 pages), and `git diff --check` passed. Root reviewed the production build in the in-app browser at desktop and 390px mobile widths, including both themes, mobile menu, offer CTA, FAQ expansion, prepared inquiry text, and successful copy feedback. No browser console errors; existing Plausible deliberately ignores localhost events. All three new routes render without horizontal overflow. Deployment, indexing, and actual email delivery remain untested external steps.

## 2026-09-07 - Prepare authorized source pushes

- Updated active context, roadmap, decision D-008, and runbook to describe the completed 34-page implementation, offer pricing, and local-only email preparation behavior.
- User requested implementation/documentation push followed by a documentation update recording that push and a second push. The target is `origin/feature/marketing-offer-2026-09-07`; no main merge, production deployment, or social post is included.
- Remote success is not yet asserted in this entry; the follow-up entry will record the confirmed commit and branch.

## 2026-09-07 - First push verified; documentation follow-up

- Committed implementation and documentation as `5d08255483e3b3bd8dea80ca04b6a858854c5fde` (`feat: add scoped content marketing offer and work example`).
- Pushed successfully to `origin/feature/marketing-offer-2026-09-07` in `elaren-studio/website`; upstream tracking was established.
- Remote readback at 15:18 UTC returned the identical full SHA via `git ls-remote`. Required validator and 34-page production build passed before pushing; the initial sandbox IPC error was resolved by rerunning the validator with local IPC access.
- This second, documentation-only commit records that first-push evidence and updates current context/roadmap. No main merge, production deployment, external inquiry, or LinkedIn post was performed.

## 2026-09-07 - Authorized main merge and production verification

- User explicitly authorized the merge. Verified the exact feature head, main comparison, repository permissions, and successful Vercel preview status before merging through GitHub.
- Main merge: `601873983159a660fea4e68dc3e1dd3ffffd20b4`. Production deployment: `6312066835`, successful at 15:49:01 UTC.
- Verified HTTP 200 and expected content on the public content-marketing offer, program-campaign example, and content-partner guide. Responses were served by Vercel on `elarenstudio.com`.
- Recorded release evidence in current context and roadmap using a clean checkout of merged main. No email or LinkedIn post was sent; indexing, actual inquiry delivery, and conversion outcomes remain unmeasured.

## 2026-09-07 - Technical foundation and external inquiry delivery

- Verified domain owner access in Search Console, homepage index/canonical status, and existing error-free sitemap index registration. Three newly added routes remain unknown in the inspected URL variants; sitemap freshness requires a later Google crawl.
- Verified live sitemap-index HTTP 200. Resubmission returned HTTP 403 because the existing OAuth grant has only `webmasters.readonly`; submission remains pending through the owner UI or separately consented write access.
- Exercised production content-marketing inquiry preparation with synthetic data. Sent the prepared content as a clearly labeled self-test through the owner's external iCloud SMTP account, then verified exact recipient, inbox placement, body integrity, and passing SPF/DKIM/DMARC in Google.
- The browser connection was lost before a repeat copy check; prior local desktop/mobile copy checks remain valid historical evidence. No legacy FormSubmit or analytics claim, prospect outreach, or social posting is implied.
- Updated current context, roadmap, and runbook; private mailbox evidence remains outside the public repository.
