"""Core functionality for Catma.

The original project exposes a small set of helper functions and data classes
at the package level.  The simplified training version of the repository keeps
those exports minimal and only re-exports the pieces that actually exist in the
code base.
"""

from .model import Obj as Object, Morphism, Category
from .io_yaml import read_catmaml, write_catmaml
from . import validate  # re-export module for convenience
from .validate import is_valid_category

__all__ = [
    "Object",
    "Morphism",
    "Category",
    "read_catmaml",
    "write_catmaml",
    "validate",
    "is_valid_category",
]
