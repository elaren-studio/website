# Roadmap

Last updated: September 8, 2026

## Private-practice marketing batch

- Implemented one content-marketing industry page, linked practice sample, practice-specific inquiry fields, and contextual links from the established offers. Prices, client limits, and service boundaries are unchanged.
- Research found commercial providers for all three query groups; it did not establish keyword volume, an easy ranking opportunity, or price leadership. Use postlaunch Search Console and actual inquiry evidence before adding another industry or city page.
- Local QA passed: validator, 41-page build, structural links/metadata, and Personal Chrome desktop/mobile buyer path. Publication is pending for this batch. Direct inquiry submission, analytics ownership verification, and business-profile eligibility remain separate work.

## Proof and measurement batch

- Implemented: evidence-corrected Wright Wellness case study, two current screenshots, first-month local SEO guide, service cross-links, and visible resource update dates.
- Released as main merge `c6779b0b8f701f6ea5f09e3cfeaa4a84b2da88a8`; Vercel Production `6340934968` succeeded. Public content/assets and sitemap receipt were verified. New-guide indexing is not yet established.
- Baseline captured privately; use `docs/SEARCH_MEASUREMENT.md` for the reporting window, indexed-version limitations, repeatable script, and inquiry qualification. Start comparisons after sufficient postlaunch data is available.
- Private-practice intent research and the resulting page/sample are covered in the batch above. The existing project establishes relevant implementation experience, not market demand or business results.

## DFW buyer-intent batch

- Implemented: reconciled local SEO/content offers, social service page, one DFW regional overview, and two buyer guides. Shared marketing prices, explicit delivery limits, fictional examples, service-specific inquiries, and navigation cross-links support the same buying path.
- Released on main as `2fb497326680c2ed1b7f5a9e1f355fb9bdd650d4`; Vercel Production `6334338852` succeeded. Live routes and sitemap returned expected content. September 8 sitemap resubmission at 18:29:08 UTC was accepted pending processing with zero errors/warnings.
- Next: inspect Search Console discovery and query/page impressions after recrawl, then refine the pages receiving relevant impressions. Track qualified inquiries by source page using prepared email details; there is no new conversion dashboard.
- Add further city or industry pages only when there is distinct useful content and evidence of demand. Use actual delivered work for future case studies with client permission.
- Keep paid advertising, filming, and daily community management outside the publishing package. Review introductory availability after two new marketing clients have joined; do not display an invented remaining-slot counter.

## Immediate

- Four individual indexing requests (homepage, content-marketing offer, campaign example, preparation guide) were accepted into Google's priority crawl queue on September 8. Recheck later crawl/indexing; accepted requests do not establish indexed pages.

- Content-marketing inquiry mailbox delivery and Search Console owner access are verified. The additive OAuth upgrade retained all 19 original scopes and added `https://www.googleapis.com/auth/webmasters` (20 total, zero removals); refresh and identity were verified. The sitemap-index submission completed at 16:49:08 UTC with HTTP 204 and a successful initial GET readback accepted pending processing, with zero errors and zero warnings. Current inspection shows the homepage `Crawled - currently not indexed` with the expected canonical and August 30, 2026 last crawl; the three new pages remain unknown to Google. Recheck discovery/indexing after Google recrawls.

- Keep link validation and the 41-page build green from the active Elaren/website task worktree.
- Keep README, RUNBOOK, and handoff documents aligned with the actual dual content system.
- Website transferred to elaren-studio/website with repository identity and history preserved.
- Vercel project, production branch, selected-repository GitHub App access, production deployment, and elarenstudio.com attachment verified after reconnection.
- First post-transfer Git-triggered Production deployment verified Ready with the elarenstudio.com alias and GitHub success status.

## Maintenance

- Keep public LLM content files synchronized with major copy changes.
- Run the link validator and production build before pushing.
- Keep pricing and CTA sources centralized.
- Replace placeholder or draft brand assets only through an explicit website decision.

## Deferred

- Hosting-provider migration
- Broad content-system consolidation
- Removal of elaren_site_content while current routes still depend on it

## September 7, 2026 content marketing delivery

- Completed: content marketing page, fictional example, resource guide, desktop/mobile browser QA, and inquiry preparation/copy checks.
- Merged to main as `601873983159a660fea4e68dc3e1dd3ffffd20b4`; Vercel Production deployment `6312066835` succeeded. All three new production routes returned HTTP 200 with expected content.
- Verify live search-console/indexing and analytics state separately; this local implementation contains no measured traffic or conversion claim.
