#!/usr/bin/env python3
"""
Fetch citation counts for all publication posts via the OpenAlex API
and write the result to _data/stats.yml.

Every post in _posts/ with "Publication" in its categories counts as a
publication. Its DOI is read from the `doi` front matter field; posts without
a DOI are still counted as publications, but contribute no citations.

OpenAlex is free and requires no API key.
Polite-pool access (faster) is used by supplying a mailto in the User-Agent.
"""

import time
from datetime import date
from pathlib import Path

import requests
import yaml

POSTS_DIR = Path(__file__).parent.parent / "_posts"
DATA_FILE = Path(__file__).parent.parent / "_data" / "stats.yml"

OPENALEX_BASE = "https://api.openalex.org/works"
HEADERS = {"User-Agent": "ENABLING-website/1.0 (mailto:thorsten.hempel@ovgu.de)"}


def fetch_cited_by(doi: str) -> int:
    url = f"{OPENALEX_BASE}/doi:{doi}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            return r.json().get("cited_by_count", 0)
        if r.status_code == 404:
            print(f"  [not found] {doi}")
        else:
            print(f"  [HTTP {r.status_code}] {doi}")
    except requests.RequestException as exc:
        print(f"  [error] {doi}: {exc}")
    return 0


def load_publications() -> list[dict]:
    """Return the front matter of every publication post."""
    pubs = []
    for post in sorted(POSTS_DIR.glob("*.md")):
        text = post.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        front = yaml.safe_load(text.split("---", 2)[1]) or {}
        if "Publication" in (front.get("categories") or []):
            front["_file"] = post.name
            pubs.append(front)
    return pubs


def main() -> None:
    pubs = load_publications()
    print(f"Fetching citations for {len(pubs)} publications:")

    total = 0
    missing = []
    for pub in pubs:
        doi = pub.get("doi")
        if not doi:
            missing.append(pub["_file"])
            continue
        count = fetch_cited_by(doi)
        print(f"  {count:>5}  {doi}")
        total += count
        time.sleep(0.2)  # stay well within rate limits

    if missing:
        print("\nPublications without DOI (counted, but no citations):")
        for name in missing:
            print(f"  - {name}")

    stats = {
        "citations": total,
        "publications": len(pubs),
        "last_updated": date.today().isoformat(),
    }

    DATA_FILE.write_text(yaml.dump(stats, default_flow_style=False), encoding="utf-8")
    print(f"\nTotal citations: {total}")
    print(f"Publications:    {len(pubs)}")
    print(f"Written to {DATA_FILE}")


if __name__ == "__main__":
    main()
