"""Shared utility functions for the RAG pipeline."""

from __future__ import annotations

import hashlib


def hash_content(content: str) -> str:
    """Generate a stable SHA-256 hash from document content.

    Used for incremental indexing to detect changed documents.
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
