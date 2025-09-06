from .model import Category

def check_objects_exist(cat: Category) -> list[str]:
    errs = []
    for m in cat.morphisms.values():
        if m.src not in cat.objects: errs.append(f"morphism {m.id}: src {m.src} missing")
        if m.dst not in cat.objects: errs.append(f"morphism {m.id}: dst {m.dst} missing")
    return errs

def check_identities(cat: Category) -> list[str]:
    # v0.1: just ensure each object could have an identity (not enforced creation)
    return []

def validate(cat: Category) -> list[str]:
    errs = []
    errs += check_objects_exist(cat)
    errs += check_identities(cat)
    return errs
