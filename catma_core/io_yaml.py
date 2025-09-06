"""YAML I/O for CatmaML."""

from pathlib import Path
from typing import Any, Dict

try:  # pragma: no cover - optional dependency
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # type: ignore
    import json
else:
    json = None  # type: ignore


def read_catmaml(path: str | Path) -> Dict[str, Any]:
    """Read CatmaML YAML into a dictionary."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if yaml is not None:  # pragma: no branch
        return yaml.safe_load(text) or {}
    assert json is not None  # pragma: no cover
    return json.loads(text)


def write_catmaml(data: Dict[str, Any], path: str | Path) -> None:
    """Write dictionary as CatmaML YAML."""
    with open(path, "w", encoding="utf-8") as fh:
        if yaml is not None:  # pragma: no branch
            yaml.safe_dump(data, fh)
        else:
            assert json is not None  # pragma: no cover
            json.dump(data, fh, indent=2)
