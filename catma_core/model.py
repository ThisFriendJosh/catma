"""Category-theory data structures (stubs)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class Object:
    """A categorical object."""
    name: str


@dataclass
class Morphism:
    """A morphism between two objects."""
    name: str
    source: Object
    target: Object


class Functor:
    """Very small functor stub mapping object names."""

    def __init__(self, mapping: Dict[str, str]):
        self.mapping = mapping

    def __call__(self, obj: Object) -> Object:
        return Object(self.mapping.get(obj.name, obj.name))
