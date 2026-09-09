# Search and inquiry measurement

## Baseline and interpretation

The September 8, 2026 baseline uses finalized Google web-search data for August 9–September 5 (28 days, Pacific reporting dates), plus eight URL inspections captured on September 8. This window precedes the new marketing pages and must not be presented as their performance. The private snapshot and CSV files are kept outside this public repository.

Google reported the homepage, content-marketing page, and Wright Wellness case study indexed at capture time. The slash-canonical local SEO URL was discovered but not indexed; the four September 8 social/regional/buyer-guide URLs were unknown. This supersedes earlier dated homepage/content-marketing inspection results, but does not prove Google crawled the latest deployed copy.

## Repeatable capture

Refresh the existing authorized Google token through the owner's established credential helper. Do not regenerate OAuth or change its scopes. Then run:

```sh
python3 scripts/search-baseline.py \
  --token-file /absolute/private/path/to/refreshed-token.json \
  --expected-account YOUR_VERIFIED_ACCOUNT \
  --output /absolute/private/path/to/a-new-snapshot-directory
```

The standard-library script verifies account identity and property access, reads Search Analytics and URL Inspection, and creates `search-console.json`, `landing-pages.csv`, and an empty `inquiry-ledger.csv`. It refuses an existing output directory or one inside this public repository. It never refreshes credentials, changes scopes, submits indexing requests, or sends email. Reuse the ongoing inquiry ledger separately; do not replace it with a new empty snapshot ledger.

Default reporting ends three days before today and requests finalized data. `--end-date YYYY-MM-DD` supports reproducible comparisons. Review data freshness and available daily rows before interpreting a change. A successful API response with no row is not proof of zero search demand. Query-level rows omit anonymized searches and may be incomplete; property totals are separate. Average position is an aggregate, not a live ranking.

## Weekly review

1. Inspect discovery, index status, and Google-selected canonical for the priority URLs. A URL Inspection response concerns Google's stored version, not a live render.
2. Compare the same 28-day window length: property totals, landing-page impressions/clicks, and available search phrases. Keep brand searches separate from service/buying-topic queries. Do not attribute prelaunch activity to new pages.
3. Record actual received inquiries in the private ledger. Use a nonidentifying ID, the service and source page from the prepared email, qualification, stage, and collected cash. A qualified inquiry describes an actual business need within scope and a plausible buying timeframe. Record the reason; do not infer qualification from a click.
4. Deduplicate follow-ups under one inquiry ID. Exclude synthetic tests, spam, and vendors. Leave counts unmeasured until the owner's inbox/ledger reconciliation is complete; an empty template is not a zero-inquiry baseline. An email source page identifies the composer used, not necessarily the visitor's original acquisition channel.
5. Choose one improvement based on evidence: discovery/canonical repair, clearer matching copy, a stronger example, or a distinct new page where search intent and relevant experience support it.

This is a manual review workflow, not a scheduled automation. The September 9 direct inquiry form additionally emits `Inquiry Started`, `Inquiry Submitted`, and `Inquiry Submission Failed` through the existing Plausible installation, on the production hostname only. Properties contain the fixed service key and source pathname, never entered form details or prepared email URLs. Starts indicate interaction; submitted indicates the provider's documented acceptance; failed indicates an unconfirmed request that might still arrive. None establishes a qualified buyer.

Plausible account ownership and matching custom-event goals remain pending owner sign-in. Do not report these as a verified conversion dashboard until both goal setup and event readback succeed. Existing pageviews and the private ledger remain distinct. Exclude labeled synthetic form checks from conversion interpretation. Source page means the form used, not necessarily the original acquisition channel.

API references: [Search Analytics query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query), [URL Inspection](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect).
