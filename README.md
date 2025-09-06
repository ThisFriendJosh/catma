# Catma

Prototype tools for experimenting with category theory modeling.

## Installation

```bash
pip install -e .
```

## Usage

```python
from catma_core.io_yaml import read_catmaml
from catma_core.validate import is_valid_category

cfg = read_catmaml("examples/ak_fsio.yaml")
print(is_valid_category(cfg))
```
