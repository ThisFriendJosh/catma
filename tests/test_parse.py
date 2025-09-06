from pathlib import Path
import sys

# Ensure the package root is on the path when running tests directly
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from catma_core.io_yaml import load_yaml
from catma_core.validate import validate


def test_load_ak_fsio():
    path = Path(__file__).resolve().parent.parent / "examples" / "ak_fsio.yaml"
    cat = load_yaml(path)
    assert "A" in cat.objects
    assert cat.morphisms["f"].src == "A"
    assert validate(cat) == []
