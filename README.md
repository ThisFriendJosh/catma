# Catma

Prototype tools for experimenting with category theory modeling.

## Installation

```bash
pip install -e .
```

## Usage

Load a YAML description of a category and run the basic validator:

```python
from catma_core.io_yaml import load_yaml
from catma_core.validate import validate

cat = load_yaml("examples/ak_fsio.yaml")
print(validate(cat))
from catma_core.validate import is_valid_category

cat = load_yaml("examples/ak_fsio.yaml")
print(is_valid_category(cat))
from catma_core.validate import validate

cat = load_yaml("catma.yaml")
errors = validate(cat)
print(errors or "Category is valid")
```
