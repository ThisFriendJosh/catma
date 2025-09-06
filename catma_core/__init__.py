"""Core functionality for Catma.

This package exposes the primary data structures and helpers used
throughout the project.  Earlier iterations of the library provided
``read_catmaml`` and ``is_valid_category`` helper functions which have
since been replaced with the more explicit ``load_yaml`` and
``validate`` functions.  The exports below mirror the current API so
that consumers can simply import from :mod:`catma_core`.
"""

from .model import Obj, Morphism, Category
from .io_yaml import load_yaml, dump_yaml
from .model import Obj, Morphism, Category
from .io_yaml import load_yaml, dump_yaml
from .validate import validate, is_valid_category
from .validate import validate

__all__ = [
    "Obj",
    "Morphism",
    "Category",
    "load_yaml",
    "dump_yaml",
    "validate",
    "is_valid_category",
]

