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

## D-008 - Scoped content marketing offer and demonstration

Status: implemented and locally verified; branch push authorized
Date: September 7, 2026

The new content marketing page uses explicit scope, pricing, approval, and no-guarantee boundaries from the implementation brief. Its inquiry composer only prepares a mailto draft to the existing public business email and never claims delivery. The Northside Arts Workshop example is prominently fictional, with no active registration, client endorsement, award, or achieved-result claims. Deployment, external sends, indexing, and analytics verification remain separate gates.

The first two new clients may start at $495 for the first month and continue at $750/month, held for six months. The user authorized two source pushes: implementation/documentation first, then documentation recording the verified first push. This does not imply a production deployment or LinkedIn publication.

## D-009 - DFW marketing buyer-intent pages and consistent introductory offers

Status: implemented
Date: September 8, 2026

The user approved reconciling local SEO with the current introductory offer and expanding marketing buyer-intent pages for Arlington, Dallas–Fort Worth, and remote Texas work. Marketing now appears prominently alongside website services and existing software products, partially superseding D-007's navigation and homepage positioning.

The first two new marketing clients total across both options can start at $495 for month one and optionally continue at $750/month, held six months. Content and social are two entry pages for one publishing package. Local SEO is a separately scoped alternative for one website and primary location. No setup fee, no automatic renewal, advance payment after written scope. Website builds and Care retain their separate prices and scope.

Centralize marketing prices and publishing deliverables in `src/lib/marketing.ts`; synchronize guide prose and public LLM summaries when changing them. Distinguish approved creation/scheduling from paid ads, filming, and daily community management. Keep examples fictional until there is permission and evidence for a real case study. Use one regional overview rather than thin replicated city pages, factual service areas rather than invented offices, and visible scope matching Service structured data. Indexing and lead outcomes require separate evidence.
