from .model import Category, Morphism


def check_objects_exist(cat: Category) -> list[str]:
    """Ensure that every morphism references existing objects.

    Parameters
    ----------
    cat:
        Category whose morphisms are to be checked.

    Returns
    -------
    list[str]
        Error messages for morphisms with missing source or destination
        objects.
    """
    errs = []
    for m in cat.morphisms.values():
        if m.src not in cat.objects:
            errs.append(f"morphism {m.id}: src {m.src} missing")
        if m.dst not in cat.objects:
            errs.append(f"morphism {m.id}: dst {m.dst} missing")
    return errs


def check_identities(cat: Category) -> list[str]:
    """Placeholder for identity checks.

    Intended to verify that each object has an identity morphism.  Currently
    returns an empty list.
    """
    # v0.1: just ensure each object could have an identity (not enforced creation)
    return []


def validate(cat: Category) -> list[str]:
    """Run all validation helpers and collect their error messages.

    Parameters
    ----------
    cat:
        Category to validate.

    Returns
    -------
    list[str]
        All accumulated error strings from individual checks.
    """
    errs = []
    errs += check_objects_exist(cat)
    errs += check_identities(cat)
    return errs
