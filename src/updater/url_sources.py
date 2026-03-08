"""Shared helpers for reading and writing the URL sources JSON file."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


URL_SOURCES_PATH = Path("data/url_sources.json")


def load_url_sources() -> List[Dict[str, Any]]:
    """Load URL sources from JSON file."""
    if not URL_SOURCES_PATH.exists():
        return []
    try:
        with open(URL_SOURCES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading URL sources: {e}")
        return []


def save_url_sources(sources: List[Dict[str, Any]]) -> None:
    """Save URL sources to JSON file."""
    try:
        with open(URL_SOURCES_PATH, "w", encoding="utf-8") as f:
            json.dump(sources, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving URL sources: {e}")
