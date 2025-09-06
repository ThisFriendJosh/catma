"""Graphviz rendering helpers."""

from typing import Any, Dict

try:  # pragma: no cover - optional dependency
    from graphviz import Digraph
except Exception:  # pragma: no cover
    Digraph = None


def render_category(data: Dict[str, Any]):
    """Render a category using Graphviz and return the graph object."""
    if Digraph is None:
        raise RuntimeError("graphviz is required for rendering")
    dot = Digraph()
    for obj in data.get("objects", []):
        dot.node(obj["name"])
    for morph in data.get("morphisms", []):
        dot.edge(morph["source"], morph["target"], label=morph["name"])
    return dot
