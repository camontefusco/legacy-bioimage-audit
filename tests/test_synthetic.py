from PIL import Image
import pandas as pd
from src.synthetic import generate_synthetic_dataset


def test_generate_synthetic_dataset(tmp_path):
    metadata_path = generate_synthetic_dataset(tmp_path)
    metadata = pd.read_csv(metadata_path)
    assert len(metadata) == 12
    assert set(metadata["biological_interpretation_permitted"]) == {"no"}
    assert Image.open(tmp_path / metadata.iloc[0]["file_name"]).size == (256, 256)

