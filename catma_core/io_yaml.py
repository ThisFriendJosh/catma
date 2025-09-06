"""Simple YAML helpers used throughout the examples and tests.

Two sets of helpers are provided:

``load_yaml``/``dump_yaml`` operate on the :class:`~catma_core.model.Category`
dataclasses, while ``read_catmaml``/``write_catmaml`` simply return or accept
plain ``dict`` objects.  The latter mirrors the very lightweight JSON/YAML
examples shipped with the training repository and keeps the public API stable
for the tests.
"""

import yaml
from .model import Obj, Morphism, Category

def load_yaml(path: str) -> Category:
    with open(path, "r", encoding="utf-8") as f:
        y = yaml.safe_load(f)
    objs = {o["id"]: Obj(id=o["id"], labels=tuple(o.get("labels", []))) for o in y["objects"]}
    morphs = {
        m["id"]: Morphism(id=m["id"], src=m["src"], dst=m["dst"], kind=m["kind"], attrs=m.get("attrs", {}))
        for m in y.get("morphisms", [])
    }
    return Category(name=y.get("category", "Unnamed"), objects=objs, morphisms=morphs)

def dump_yaml(cat: Category, path: str) -> None:
    y = {
        "version": "0.1",
        "category": cat.name,
        "objects": [{"id": o.id, "labels": list(o.labels)} for o in cat.objects.values()],
        "morphisms": [{"id": m.id, "src": m.src, "dst": m.dst, "kind": m.kind, "attrs": m.attrs}
                      for m in cat.morphisms.values()],
    }
    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(y, f, sort_keys=False)


def read_catmaml(path: str) -> dict:
    """Read a Catma configuration file and return the raw mapping.

    The function is intentionally lightweight and performs no validation – that
    is delegated to :func:`catma_core.validate.is_valid_category`.
    """

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def write_catmaml(data: dict, path: str) -> None:
    """Write *data* to *path* in YAML format."""

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, sort_keys=False)
