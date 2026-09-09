#!/usr/bin/env python3
"""Submit selected Elaren Studio URL changes to IndexNow.

The default mode only validates and prints the request. ``--submit`` is an
explicit external action and first checks the public ownership key and every
selected URL. This tool deliberately accepts explicit URLs only; it never
submits an entire sitemap.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request


HOST = "elarenstudio.com"
ORIGIN = f"https://{HOST}"
INDEXNOW_ENDPOINT = "https://www.bing.com/indexnow"
MAX_URLS = 10_000
KEY_FILENAME = "d4491462488144a79e557134c68c5c16.txt"
KEY_FILE = Path(__file__).resolve().parents[1] / "public" / KEY_FILENAME


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


NO_REDIRECT_OPENER = urllib.request.build_opener(NoRedirectHandler)


def read_key_file(path: Path | None = KEY_FILE) -> tuple[str, str]:
    """Return (key, public filename), enforcing one valid public key file."""
    if path is None or not path.is_file() or path.parent.name != "public":
        raise ValueError("public IndexNow key file is missing")
    if path.suffix != ".txt" or len(path.stem) < 8 or len(path.stem) > 128:
        raise ValueError("public key filename must contain 8-128 characters")
    key = path.read_text(encoding="utf-8").strip()
    if key != path.stem or not all(c in "0123456789abcdef" for c in key):
        raise ValueError("public key file must contain its lowercase hexadecimal filename")
    if not 8 <= len(key) <= 128:
        raise ValueError("IndexNow key must contain 8-128 hexadecimal characters")
    return key, path.name


def validate_url(value: str) -> str:
    """Validate and return an exact HTTPS production URL."""
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme != "https" or parsed.hostname != HOST or parsed.username or parsed.password:
        raise ValueError(f"URL must use exact HTTPS host {HOST}: {value}")
    if parsed.port is not None:
        raise ValueError(f"URL must not specify a port: {value}")
    if parsed.fragment or parsed.query:
        raise ValueError(f"URL must not contain a query or fragment: {value}")
    if parsed.path and not parsed.path.startswith("/"):
        raise ValueError(f"URL path is malformed: {value}")
    return value


def validate_urls(values: list[str]) -> list[str]:
    if not values:
        raise ValueError("at least one explicit --url is required")
    if len(values) > MAX_URLS:
        raise ValueError(f"at most {MAX_URLS} URLs may be submitted")
    result = [validate_url(value) for value in values]
    if len(set(result)) != len(result):
        raise ValueError("duplicate URLs are not allowed")
    return result


def get_exact(url: str) -> tuple[int, bytes]:
    """GET without following redirects, returning status and response body."""
    request = urllib.request.Request(url, method="GET", headers={"User-Agent": "elaren-indexnow/1"})
    try:
        with NO_REDIRECT_OPENER.open(request, timeout=20) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as error:
        if 300 <= error.code < 400:
            location = error.headers.get("Location", "")
            raise RuntimeError(f"refusing redirect while checking {url}: {location}") from None
        raise RuntimeError(f"GET {url} returned HTTP {error.code}") from None
    except urllib.error.URLError as error:
        raise RuntimeError(f"GET {url} failed: {error.reason}") from None


def verify_public_key(key: str, filename: str) -> None:
    url = f"{ORIGIN}/{filename}"
    status, body = get_exact(url)
    if status != 200 or body.decode("utf-8").strip() != key:
        raise RuntimeError("public IndexNow key did not return an exact HTTP 200 match")


def verify_urls(urls: list[str]) -> None:
    for url in urls:
        status, _ = get_exact(url)
        if status != 200:
            raise RuntimeError(f"production URL did not return HTTP 200: {url}")


def submit(urls: list[str], key: str, key_filename: str) -> int:
    verify_public_key(key, key_filename)
    verify_urls(urls)
    payload = {"host": HOST, "key": key, "keyLocation": f"{ORIGIN}/{key_filename}", "urlList": urls}
    request = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": "elaren-indexnow/1"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"IndexNow returned HTTP {error.code}") from None
    if status == 200:
        print("IndexNow accepted the URL set (HTTP 200; receipt only, not indexing).")
    elif status == 202:
        print("IndexNow accepted the URL set for key validation (HTTP 202; not indexing).")
    else:
        raise RuntimeError(f"IndexNow returned unexpected HTTP {status}")
    return status


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", action="append", required=True, help="one changed production URL; repeat for multiple URLs")
    parser.add_argument("--submit", action="store_true", help="perform live key/URL checks and submit to IndexNow")
    args = parser.parse_args(argv)
    try:
        urls = validate_urls(args.url)
        key, key_filename = read_key_file()
        if not args.submit:
            print(json.dumps({"mode": "dry-run", "host": HOST, "keyLocation": f"{ORIGIN}/{key_filename}", "urlList": urls}, indent=2))
            return 0
        submit(urls, key, key_filename)
        return 0
    except (ValueError, RuntimeError, OSError, UnicodeError) as error:
        print(f"indexnow: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
