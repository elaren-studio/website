#!/usr/bin/env python3
"""Read Elaren Search Console data into a private directory outside this repo.

Requires a refreshed OAuth JSON file with access_token and Search Console read
permission. This script never refreshes credentials or submits indexing requests.
"""
import argparse
import csv
import datetime as dt
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

SITE = "sc-domain:elarenstudio.com"
ORIGIN = "https://elarenstudio.com"
ROUTES = ["/", "/content-marketing/", "/social-media-marketing/", "/local-seo/",
          "/marketing-dallas-fort-worth/", "/resources/guides/content-social-marketing-cost/",
          "/resources/guides/seo-or-social-media-for-small-business/",
          "/resources/teardowns/wright-wellness-before-after-teardown/",
          "/resources/guides/first-month-local-seo/"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token-file", type=Path, required=True)
    parser.add_argument("--expected-account", required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--end-date", type=dt.date.fromisoformat)
    args = parser.parse_args()
    output = args.output.resolve()
    repo = Path(__file__).resolve().parents[1]
    if output == repo or repo in output.parents:
        parser.error("Choose a private output directory outside the public repository.")
    if output.exists():
        parser.error("Use a new output directory so earlier snapshots cannot be overwritten.")
    token = json.loads(args.token_file.read_text())["access_token"]

    def api(url, payload=None):
        request = urllib.request.Request(url, headers={"Authorization": "Bearer " + token,
            "Content-Type": "application/json"},
            data=json.dumps(payload).encode() if payload is not None else None)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(f"Google API returned HTTP {error.code}; no credential output logged.") from None

    identity = api("https://www.googleapis.com/drive/v3/about?fields=user(emailAddress)")
    if identity["user"]["emailAddress"] != args.expected_account:
        raise RuntimeError("Authenticated account does not match expected account.")
    endpoint = "https://www.googleapis.com/webmasters/v3/sites/" + urllib.parse.quote(SITE, safe="")
    permission = api(endpoint).get("permissionLevel")
    if permission not in {"siteOwner", "siteFullUser", "siteRestrictedUser"}:
        raise RuntimeError("Search Console property access is not verified.")
    end = args.end_date or (dt.datetime.now(ZoneInfo("America/Los_Angeles")).date() - dt.timedelta(days=3))
    start = end - dt.timedelta(days=27)
    base = {"startDate": str(start), "endDate": str(end), "type": "web", "dataState": "final"}
    responses = {}
    for label, dimensions in [("site_totals", []), ("daily", ["date"]), ("pages", ["page"]),
                               ("page_queries", ["page", "query"])]:
        responses[label] = api(endpoint + "/searchAnalytics/query", {
            **base, "dimensions": dimensions, "rowLimit": 25000})
    inspections = []
    for route in ROUTES:
        result = api("https://searchconsole.googleapis.com/v1/urlInspection/index:inspect", {
            "inspectionUrl": ORIGIN + route, "siteUrl": SITE, "languageCode": "en-US"})
        inspections.append({"route": route, "result": result.get("inspectionResult", {})})
    snapshot = {"captured_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "property": SITE, "permission": permission, "window": base,
        "notes": ["Baseline includes dates before the September 8 marketing launch.",
            "Finalized Google web-search data; reporting dates use Pacific time.",
            "No returned row means no reportable row, not proof of zero demand.",
            "Query rows omit anonymized searches and may omit additional rows; do not sum them as site totals.",
            "Average position is a historical aggregate, not a current ranking check.",
            "URL inspection describes Google's indexed version, not a live URL test.",
            "Qualified inquiries are unmeasured until the separate private inquiry ledger is reconciled."],
        "row_limit_reached": {k: len(v.get("rows", [])) == 25000 for k, v in responses.items()},
        "search_analytics": responses, "url_inspections": inspections}
    output.mkdir(parents=True, mode=0o700)
    (output / "search-console.json").write_text(json.dumps(snapshot, indent=2) + "\n")
    page_rows = {}
    for row in responses["pages"].get("rows", []):
        page_rows.setdefault(row["keys"][0].rstrip("/"), []).append(row)
    with (output / "landing-pages.csv").open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["page", "start_date", "end_date", "reporting_status", "clicks", "impressions", "ctr", "average_position", "index_coverage", "qualified_inquiries_status"])
        for item in inspections:
            variants = page_rows.get((ORIGIN + item["route"]).rstrip("/"), [])
            row = variants[0] if len(variants) == 1 else None
            index = item["result"].get("indexStatusResult", {})
            writer.writerow([ORIGIN + item["route"], start, end,
                "reported" if row else ("multiple_url_variants_see_json" if variants else "no_reportable_row"),
                *[row.get(key) if row else "" for key in ["clicks", "impressions", "ctr", "position"]],
                index.get("coverageState", "unavailable"), "unmeasured"])
    with (output / "inquiry-ledger.csv").open("w", newline="") as file:
        csv.writer(file).writerow(["received_date", "inquiry_id", "source_page", "service", "qualified", "qualification_reason", "stage", "cash_collected", "notes"])
    print(json.dumps({"output": str(output), "start_date": str(start), "end_date": str(end),
        "reported_page_rows": len(responses["pages"].get("rows", [])),
        "inspection_count": len(inspections), "inquiries_status": "unmeasured"}))


if __name__ == "__main__":
    main()
