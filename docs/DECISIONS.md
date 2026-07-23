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

Status: satisfied and superseded by D-006
Date: July 22, 2026

Keep the existing GitHub remote until authenticated GitHub and hosting evidence confirms that transfer or rename will not interrupt production.

## D-005 - Retire obsolete local artifacts

Status: implemented
Date: July 22, 2026

Do not migrate generated dependencies, build output, test results, local AI chat history, or generated PDF output. Retire the unused tracked content zip because Git history preserves it and no code references it.

## D-006 - Place the website under the Elaren GitHub organization

Status: implemented
Date: July 22, 2026

The canonical public website repository is `elaren-studio/website`. Preserve the existing repository identity, history, default branch, and deployment project. Vercel remains connected to the same GitHub repository ID with `main` as the production branch, and its GitHub App access is limited to the `website` repository rather than all Elaren repositories.

## D-007 - Reposition the public site as an app studio and dev shop

Status: implemented
Date: July 23, 2026

The site presents Elaren Studio as a product studio with a select client-build lane, per HQ decision D-012. Navigation is Products, Services, Resources, About. OpusGraph, AgentMeter, Studio Register, and OmniSearch are named publicly; earlier-stage work appears only as unnamed problem spaces; Resonance Music Press is credited as designed and built by Elaren Studio. The therapist, local-SEO, pricing, and plans pages remain live but are removed from navigation, and no public pricing is shown for application work.
