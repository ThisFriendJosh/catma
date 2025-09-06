from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from catma_core import io_yaml
from catma_core.validate import is_valid_category


def test_read_ak_fsio():
    path = Path(__file__).resolve().parent.parent / "examples" / "ak_fsio.yaml"
    cat = io_yaml.load_yaml(path)
    assert "A" in cat.objects
    assert cat.objects["A"].labels == ("source",)
    f = cat.morphisms["f"]
    assert f.src == "A" and f.dst == "B"
    assert f.attrs["weight"] == 1
    assert is_valid_category(cat)
