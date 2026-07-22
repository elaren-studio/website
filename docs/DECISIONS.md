# Decisions

## D-001 - Keep the website independent from HQ and products

Status: implemented
Date: July 22, 2026

The website remains an independent repository. It does not contain Elaren portfolio strategy or product roadmaps.

## D-002 - Keep implemented brand truth in the website

Status: implemented
Date: July 22, 2026

The website owns the tokens, components, public copy, and published assets it actually uses. Master studio positioning, naming, and source assets belong in HQ.

## D-003 - Preserve both active content systems

Status: accepted
Date: July 22, 2026

Legacy static pages continue reading elaren_site_content while resources and SEO landing pages use Astro content collections. Consolidation is a separate project and is not implied by repository relocation.

## D-004 - Defer remote and deployment changes

Status: accepted
Date: July 22, 2026

Keep the existing GitHub remote until authenticated GitHub and hosting evidence confirms that transfer or rename will not interrupt production.

## D-005 - Retire obsolete local artifacts

Status: implemented
Date: July 22, 2026

Do not migrate generated dependencies, build output, test results, local AI chat history, or generated PDF output. Retire the unused tracked content zip because Git history preserves it and no code references it.
