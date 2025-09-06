from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from catma_core import io_yaml, validate


def test_read_ak_fsio():
    path = Path(__file__).resolve().parent.parent / "examples" / "ak_fsio.yaml"
    data = io_yaml.read_catmaml(path)
    assert data["objects"][0]["name"] == "A"
    assert validate.is_valid_category(data)
