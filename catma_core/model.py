from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass(frozen=True)
class Obj:
    id: str
    labels: Tuple[str, ...] = ()

@dataclass(frozen=True)
class Morphism:
    id: str
    src: str
    dst: str
    kind: str
    attrs: Dict[str, object] = field(default_factory=dict)

@dataclass
class Category:
    name: str
    objects: Dict[str, Obj]
    morphisms: Dict[str, Morphism]

    def obj(self, oid: str) -> Obj:
        return self.objects[oid]

    def hom(self, a: str, b: str) -> List[Morphism]:
        return [m for m in self.morphisms.values() if m.src == a and m.dst == b]

    def compose(self, f: Morphism, g: Morphism, new_id: str) -> Morphism:
        if f.dst != g.src:
            raise ValueError("Cannot compose: codomain(f) != domain(g)")
        return Morphism(id=new_id, src=f.src, dst=g.dst, kind=f"{f.kind}∘{g.kind}")
