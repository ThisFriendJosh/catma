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
