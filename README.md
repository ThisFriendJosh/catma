# Catma

Prototype tools for experimenting with category theory modeling.

## Installation

```bash
pip install -e .
```

## Usage

```python
from catma_core.io_yaml import load_yaml
from catma_core.validate import validate

cat = load_yaml("examples/ak_fsio.yaml")
print(validate(cat))
```
