# Roadmap

Last updated: September 8, 2026

## DFW buyer-intent batch

- Implemented: reconciled local SEO/content offers, social service page, one DFW regional overview, and two buyer guides. Shared marketing prices, explicit delivery limits, fictional examples, service-specific inquiries, and navigation cross-links support the same buying path.
- Next: inspect Search Console discovery and query/page impressions after recrawl, then refine the pages receiving relevant impressions. Track qualified inquiries by source page using prepared email details; there is no new conversion dashboard.
- Add further city or industry pages only when there is distinct useful content and evidence of demand. Use actual delivered work for future case studies with client permission.
- Keep paid advertising, filming, and daily community management outside the publishing package. Review introductory availability after two new marketing clients have joined; do not display an invented remaining-slot counter.

## Immediate

- Four individual indexing requests (homepage, content-marketing offer, campaign example, preparation guide) were accepted into Google's priority crawl queue on September 8. Recheck later crawl/indexing; accepted requests do not establish indexed pages.

- Content-marketing inquiry mailbox delivery and Search Console owner access are verified. The additive OAuth upgrade retained all 19 original scopes and added `https://www.googleapis.com/auth/webmasters` (20 total, zero removals); refresh and identity were verified. The sitemap-index submission completed at 16:49:08 UTC with HTTP 204 and a successful initial GET readback accepted pending processing, with zero errors and zero warnings. Current inspection shows the homepage `Crawled - currently not indexed` with the expected canonical and August 30, 2026 last crawl; the three new pages remain unknown to Google. Recheck discovery/indexing after Google recrawls.

- Keep link validation and the 38-page production build green from the canonical Elaren/website path.
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
