#!/usr/bin/env python3
"""
Fetch citation counts for the publications listed below via the OpenAlex API
and write the result to _data/stats.yml.

OpenAlex is free and requires no API key.
Polite-pool access (faster) is used by supplying a mailto in the User-Agent.

To add or remove a publication, edit the DOIS list.
"""

import time
from datetime import date
from pathlib import Path

import requests
import yaml

# ── Edit this list to add/remove publications ────────────────────────────────
DOIS = [
    "10.1007/s00138-025-01690-z",   # MobGazeNet
    "10.1007/s10462-025-11431-3",   # Synthetic dataset generation review
    "10.1007/s40747-025-01902-z",   # Eye contact engagement HRI
    "10.1109/ACCESS.2025.3617952",  # Automated 3D dataset generation
    "10.1109/CogSIMA64436.2025.11079517",
    "10.1109/SMC58881.2025.11343553",  # Digital twin TIAGo
    "10.3390/robotics15040069",     # Gaze estimation review
    "10.3390/s25092930",
    "10.1007/s10489-024-05778-3"
]
# ─────────────────────────────────────────────────────────────────────────────

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


def main() -> None:
    print(f"Fetching citations for {len(DOIS)} DOIs:")

    total = 0
    for doi in DOIS:
        count = fetch_cited_by(doi)
        print(f"  {count:>5}  {doi}")
        total += count
        time.sleep(0.2)  # stay well within rate limits

    stats = {
        "citations": total,
        "publications": len(DOIS),
        "last_updated": date.today().isoformat(),
    }

    DATA_FILE.write_text(yaml.dump(stats, default_flow_style=False), encoding="utf-8")
    print(f"\nTotal citations: {total}")
    print(f"Publications:    {len(DOIS)}")
    print(f"Written to {DATA_FILE}")


if __name__ == "__main__":
    main()
