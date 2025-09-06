"""Validation helpers."""

from typing import Any, Dict


def is_valid_category(data: Dict[str, Any]) -> bool:
    """Check that morphisms reference defined objects."""
    objects = {obj["name"] for obj in data.get("objects", [])}
    for morph in data.get("morphisms", []):
        if morph.get("source") not in objects or morph.get("target") not in objects:
            return False
    return True
