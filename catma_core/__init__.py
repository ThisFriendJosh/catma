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
    "read_catmaml",
    "write_catmaml",
    "load_yaml",
    "dump_yaml",
    "validate",
    "is_valid_category",
]

