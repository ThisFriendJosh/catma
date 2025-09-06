"""Validation helpers for :mod:`catma_core`.

This module performs a handful of sanity checks on a :class:`~catma_core.model.Category`.
"""

from .model import Category, Morphism, Obj

def check_objects_exist(cat: Category) -> list[str]:
    errs = []
    for m in cat.morphisms.values():
        if m.src not in cat.objects: errs.append(f"morphism {m.id}: src {m.src} missing")
        if m.dst not in cat.objects: errs.append(f"morphism {m.id}: dst {m.dst} missing")
    return errs

def check_identities(cat: Category) -> list[str]:
    """Ensure every object has a corresponding identity morphism.

    For each object ``o`` in ``cat`` we look for a morphism ``m`` such that

    * ``m.src == o``
    * ``m.dst == o``
    * ``m.kind`` is ``"id"``

    If no such morphism exists an error message is produced describing the
    missing identity.
    """

    errs: list[str] = []
    for oid in cat.objects:
        has_id = any(
            m.src == oid and m.dst == oid and m.kind == "id"
            for m in cat.morphisms.values()
        )
        if not has_id:
            errs.append(f"object {oid}: missing identity morphism")
    return errs

def validate(cat: Category) -> list[str]:
    errs = []
    errs += check_objects_exist(cat)
    errs += check_identities(cat)
    return errs


def is_valid_category(data) -> bool:
    """Return ``True`` if *data* describes a valid category.

    ``data`` may already be a :class:`Category` instance or a mapping similar
    to the JSON/YAML examples used throughout the project.  In the latter case
    the mapping is converted into a :class:`Category` before validation.
    """

    if isinstance(data, Category):
        cat = data
    else:
        objs = {
            o.get("id") or o.get("name"): Obj(
                id=o.get("id") or o.get("name"),
                labels=tuple(o.get("labels", [])),
            )
            for o in data.get("objects", [])
        }
        morphs: dict[str, Morphism] = {}
        for m in data.get("morphisms", []):
            mid = m.get("id") or m.get("name")
            morphs[mid] = Morphism(
                id=mid,
                src=m.get("src") or m.get("source"),
                dst=m.get("dst") or m.get("target"),
                kind=m.get("kind", ""),
                attrs=m.get("attrs", {}),
            )
        cat = Category(name=data.get("category", "Unnamed"), objects=objs, morphisms=morphs)

    return len(validate(cat)) == 0

