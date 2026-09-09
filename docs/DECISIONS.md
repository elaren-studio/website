# Decisions

## D-012 - Direct inquiries and separate discovery receipts

Status: implemented; external verification recorded in ACTIVE_CONTEXT
Date: September 9, 2026

Supersede the marketing composer-only boundary in D-008/D-011 with direct submission through the existing FormSubmit route. Retain a locally prepared email alternative, required reply fields, a honeypot, duplicate prevention, a timeout, and entered text on uncertain failure. Report success only for the documented submission acknowledgement, never an arbitrary HTTP 200 or activation message. Do not automatically retry uncertain sends.

Emit inquiry start, accepted submission, and failed submission events through the existing Plausible installation with fixed service/page properties only. Account ownership and configured goals must be verified before claiming dashboard measurement. Qualified inquiries and collected cash require private inbox/ledger reconciliation.

Use the Bing-issued public ownership meta tag and one public IndexNow key. Notify selected changed production URLs after verifying exact public responses. Keep ownership, sitemap acceptance, URL submission, indexing, and ranking as separate observed states. Preserve existing Google permissions.

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

## D-010 - Evidence-led case study and private measurement

Status: implemented
Date: September 8, 2026

Preserve the existing Wright Wellness teardown URL while replacing unsupported historical and outcome claims with retained-source comparisons, two current public screenshots, and clearly labeled observations. Disclose Felix Torres's user-confirmed Operations Manager role at Wright Wellness alongside Elaren's design credit. No ownership, independent testimonial, clinical authorship, or measured ranking/conversion results are implied. A full website project is not priced as the introductory local SEO month.

Keep original resource publication dates and add an optional updatedDate for substantial revisions. Keep Search Console responses, business metrics, and inquiry records private outside the public repository; commit only the read-only capture tool and operating instructions. Preparation and copy clicks are not inquiries. No row and an unreconciled ledger are not zero demand or zero leads.

## D-011 - One practice-specific content marketing page and inspectable sample

Status: implemented
Date: September 8, 2026

Use `/private-practice-marketing/` as an industry-specific entry to the existing content/social publishing offer. Keep `/local-seo/` and `/therapist-websites/` as the detailed separate alternatives. Search results support the existence of the commercial service category; no volume, low-competition, price-leadership, or conversion claim is justified by that review.

Connect the Wright Wellness website evidence with its Operations Manager disclosure, without implying independent endorsement or clinical credentials. The companion sample is clearly fictional, contains excerpts rather than claiming a complete delivered month, and uses practice logistics instead of medical advice. Practice reviewers approve facts and publication; clinical review stays with a qualified practice clinician. Use Instagram and LinkedIn in this example. Reuse marketing pricing and inquiry behavior; do not introduce a new form service, ad product, or analytics account as part of this content batch.
