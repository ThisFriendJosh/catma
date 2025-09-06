"""Core functionality for Catma."""

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

