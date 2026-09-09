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

## 2026-09-08 - DFW marketing buyer-intent implementation

- Reconciled local SEO and general marketing pricing with the $495 introductory month / optional $750 continuation model for two new marketing clients total. Centralized numeric pricing and the shared content/social deliverables.
- Added social content/scheduling and DFW marketing pages, two buyer guides, inline fictional work excerpts, resource cross-links, and service/source-aware inquiry preparation.
- Updated homepage, navigation, Services, Pricing, footer, metadata, and public LLM summaries while preserving existing product, website build, and Care offerings.
- Expanded the mobile menu breakpoint for the additional navigation item and simplified the duplicated pricing tab. Reduced redundant decorative binary markup on the homepage while preserving its existing visual style.
- Root exercised local SEO inquiry preparation with synthetic details and inspected desktop plus 390px/768px narrow-frame layouts in Personal Chrome. Narrow frames are responsive layout checks, not physical-device tests. No external message was sent.
- Required validator and production build passed (38 HTML pages; sitemap contains 37 indexable URLs and excludes the 404). Structural review of ten changed routes passed: one H1 each, expected canonical, valid JSON-LD, matching $495/$750 Service offers, sitemap inclusion, and no broken internal links or fragments.
- All four inquiry variants prepared the correct service/source and mailto recipient/body. Social inquiry copy returned success. Pricing tab and comparison-anchor navigation passed; both themes rendered. No application console errors or framework overlay appeared; existing Plausible ignored localhost as expected. Physical mobile devices and new external email delivery were not retested.
- Remote release evidence follows when verified.

## 2026-09-08 - DFW marketing push, merge, and production verified

- First push: `0433a958ba61a7010a7d6fc77c453df70d80d61c` to `origin/feature/dfw-marketing-2026-09-08`. Local HEAD and `git ls-remote` matched. GitHub account/repository permission, branch comparison, staged scope, required validator, and 38-page build were checked before the release.
- Authorized main merge: `2fb497326680c2ed1b7f5a9e1f355fb9bdd650d4`. Vercel Production deployment `6334338852` reported success at 18:28:13 UTC. All six changed service/guide routes, Pricing, and the child sitemap returned HTTP 200 with expected content from Vercel. The production regional page was opened and verified in Personal Chrome.
- Sitemap resubmission at 18:29:08 UTC returned HTTP 204. GET readback returned HTTP 200, zero errors/warnings, and processing pending. Owner identity and access were verified; the token refresh retained all 20 existing scopes with zero removals. Prior sitemap crawl counters are not a current indexing result.
- This documentation follow-up records the verified first push and deployed implementation for the subsequent push. Generated output, temporary QA files, and the temporary dependency link are excluded from Git. Physical-device testing, new client acquisition, and later Google indexing remain outside these verification claims.

## 2026-09-08 - Case study, local SEO guide, and private baseline

- Read the public website source and retained history before rewriting the Wright Wellness case study. Relevant source changes: homepage restructuring `226c9e9`, team carousel `5cad6d8`, image dimensions/targets `6776adf`, and starting-point copy `c52ac15`. Earlier source already had an H1, service sections, and appointment routes; removed contrary claims.
- Captured the public homepage and service section on September 8. Both JPEGs are 1680 by 947 and show current public pages, not historical screenshots. User confirmed Operations Manager as the public relationship disclosure. No private practice records were accessed for the example.
- Added the first-month local SEO guide and resource links, preserved the existing case URL, and added optional updatedDate display/Article data. Fixed the comparison table's narrow-screen overflow with a keyboard-focusable scroll region.
- Captured finalized 28-day Search Console data and eight URL inspections into a private output directory. Account/property access were verified; no OAuth changes were made. Added a read-only snapshot script and manual inquiry-ledger workflow; inquiry counts remain unmeasured. Private metric files are excluded from publication.
- Read README and the standard handoff docs. Updated current context, roadmap, decisions, runbook, and measurement instructions; README's architecture and commands remain accurate.
- Verification passed: required validator, 39-page production build, six-route canonical/sitemap/H1/JSON-LD/internal-link checks, case-study publication/update dates, and both 1680×947 image assets. Personal Chrome checks covered desktop rendering, 390px case/guide layouts, mobile menu, image loading, table scrolling containment, and guide-to-local-SEO inquiry preparation. A wrapped link required clicking its visible text after the browser locator's center point missed it; actual navigation and the correct mailto body were verified. No application console errors were observed. Physical mobile devices were not tested.
- The snapshot script completed authenticated reads and its refusal of existing/public output directories was checked. The initial snapshot has eight URL inspections; future runs also include the newly added first-month guide. Inquiry counts remain unmeasured.

## 2026-09-08 - Proof and guide release verified

- First push verified: local and remote `21643344caa9f53c18d0eb5f97f012035c7f4dcf` on `feature/marketing-proof-2026-09-08`. Main comparison was one commit ahead, zero behind; authorized merge created `c6779b0b8f701f6ea5f09e3cfeaa4a84b2da88a8`.
- Vercel Production deployment `6340934968` succeeded September 9 at 02:01:17 UTC (September 8 local). HTTP 200 and expected content verified for the case study, first-month guide, local SEO resource links, child sitemap, and both current-public-site JPEGs. The live case study was verified in Personal Chrome.
- Sitemap PUT at September 9, 02:03:04 UTC returned 204; GET returned 200 with processing pending and zero errors/warnings. Owner identity/property access were verified; no credentials or scopes were changed, and all 20 scopes remain present.
- This follow-up documents the first push and production receipt for the next documentation push. Private measurement files remain outside Git; no new conversion claims or customer messages were published.

## 2026-09-08 - Private-practice marketing page and sample

- Reviewed live commercial search results for therapist SEO, private-practice content marketing, and therapist social media management, including Texas/Dallas modifiers. Provider pages establish category evidence, not query volume or results; some advertised starting prices are lower and scopes differ. Private research notes stay outside this public repository. No paid research tool was purchased.
- Added `/private-practice-marketing/` with shared $495/$750 pricing, existing two-client limit, published service boundaries, practice approval responsibilities, disclosed Wright Wellness experience, and separate local SEO/website alternatives. Added practice-specific inquiry fields without changing the email-only behavior.
- A native worker requested as Luna medium implemented only the fictional sample page; root inspected it and corrected audience targeting in several social posts, the breadcrumb destination, an overbroad appointment-format statement, and fictional disclosure placement in the email. The sample contains a monthly map, article outline/opening, existing-page excerpt, six finished sample posts, and one referral email; no actual campaign or clinical outcomes are represented.
- Linked the page from Services, therapist websites, and shared marketing resources. Synchronized LLM summaries and added both new routes to the existing private measurement script. Read README, runbook, and handoff docs; README remains accurate and unchanged. Updated current context, roadmap, decisions, and runbook, including an old website-care price table to match the existing pricing source. No service price was changed.
- Required validator and production build passed (41 pages). Seven-route review passed for one H1, self-canonical, parseable JSON-LD, internal links/fragments, and new-route sitemap inclusion. Measurement script syntax passed; no new private baseline run was needed immediately after the earlier capture.
- Personal Chrome QA covered 1680×947 desktop and 390×844 mobile, service/sample content, both themes on the service page, mobile menu, service-to-sample-to-practice-inquiry navigation, correct synthetic mailto service/source/recipient/body, and copy success feedback. Neither page overflowed at 390px; no application console errors or framework overlay appeared. Plausible's localhost-ignore warning is expected. A navigation assertion initially expected a trailing slash while the development route used none; the actual destination and inquiry DOM were verified. A status locator was scoped to main after a browser extension added other status regions. Neither issue was an application failure.
- Screenshots and research are private output artifacts, not repository files. Physical devices, new email delivery, Google indexing, and actual qualified inquiries are unverified by this batch. GitHub account `fdtorres1`, target `elaren-studio/website`, and ADMIN access were verified before publication. Release receipts follow after readback.

## 2026-09-08 - Private-practice release verified

- First push: `8137dd2e07addba748d67456e3e427906ff11623` on `feature/private-practice-marketing-2026-09-08`; local and remote SHA matched. Main comparison was one ahead and zero behind. Authorized main merge: `388a5f282eae66e18b9b9f1437daa11c3a5ef913`.
- Vercel Production deployment `6342750325` reported success at September 9, 04:48:31 UTC (September 8 local). Both new routes, Services, therapist websites, and the child sitemap returned HTTP 200 with expected content. Both new canonical URLs appear in the sitemap. A production browser attempt timed out and reset its connection before readback; local rendered QA and HTTP deployment verification are the completed evidence.
- Direct Google owner identity/property access verified. Routine access-token refresh checked the returned scope set before writing it; all 20 existing scopes were preserved exactly. Sitemap PUT returned 204 and GET 200 at September 9, 04:49:44.062 UTC, pending processing with zero errors/warnings. No authorization scope was added or removed.
- This documentation follow-up records the verified push and release for the second push. Later indexing and actual inquiries remain unverified; no social post, outreach message, or new Google Business Profile was created.

## 2026-09-09 - Direct inquiries and discovery implementation

- Replaced the shared marketing email composer with direct FormSubmit submission and an email/copy alternative. Added required reply fields, honeypot, disabled pending/accepted state, bounded timeout, explicit new-inquiry reset, and preserved text on failure. Synchronized regional copy, privacy information, and the public summary. Prices and service boundaries remain unchanged.
- Activated the existing domain-matched FormSubmit route and verified a labeled synthetic AJAX submission both at the provider and in the intended inbox. No customer or patient information was used. Existing Google authorization scopes were unchanged.
- Added three production-only inquiry events with fixed service/page properties. Plausible login remains pending owner action; no dashboard goal or ownership claim is made.
- Bing sign-in succeeded in the owner's Personal Chrome profile. Added the manually requested Elaren site and its issued ownership meta tag, without importing other Google properties. Verification and sitemap submission follow deployment.
- A native Luna-medium worker implemented only the public IndexNow key, explicit-URL script, five focused tests, and operating instructions. Root reviewed the output and ran its tests. No automatic submission job was created.
- Required validator, 41-page build, three inquiry tests, and five IndexNow tests passed. Personal Chrome desktop QA confirmed page identity, required-field validation, rendered content without an overlay, unavailable-provider failure feedback, message preservation, retry availability, and copied fallback details. The local test endpoint was restored before final build. Screenshots remain outside Git. Console warnings about ignored localhost analytics are expected; the deliberate unavailable endpoint produces an expected request failure. Mobile and physical-device checks are not yet part of this batch.
- Release and external receipts will be appended after verification.
