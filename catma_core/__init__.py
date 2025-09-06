"""Core functionality for Catma."""

from .model import Object, Morphism, Functor
from .io_yaml import read_catmaml, write_catmaml
from .validate import is_valid_category

__all__ = [
    "Object",
    "Morphism",
    "Functor",
    "read_catmaml",
    "write_catmaml",
    "is_valid_category",
]
