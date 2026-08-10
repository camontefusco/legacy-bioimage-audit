"""Generate redistributable synthetic fluorescence-like teaching panels."""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd
from PIL import Image
from scipy.ndimage import gaussian_filter


def generate_synthetic_dataset(output_dir: str | Path, seed: int = 20260810) -> Path:
    """Create 12 images for mechanics teaching, not biological simulation."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    rows = []
    categories = ["sparse", "dense", "large_regions", "gradient_background"]
    yy, xx = np.mgrid[:256, :256]

    for index in range(12):
        category = categories[index % len(categories)]
        green = rng.normal(8, 3, (256, 256))
        count = {"sparse": 18, "dense": 70, "large_regions": 10, "gradient_background": 35}[category]
        for _ in range(count):
            cy, cx = rng.integers(10, 246, size=2)
            sy, sx = rng.uniform(6, 18, size=2) if category == "large_regions" else rng.uniform(1.5, 6, size=2)
            amplitude = rng.uniform(70, 220)
            green += amplitude * np.exp(-(((yy - cy) / sy) ** 2 + ((xx - cx) / sx) ** 2) / 2)
        if category == "gradient_background":
            green += np.linspace(0, 65, 256)[None, :]
        green = gaussian_filter(green, sigma=rng.uniform(0.4, 1.2))
        green = np.clip(green, 0, 255).astype(np.uint8)
        blue = np.clip(rng.normal(15, 5, green.shape), 0, 255).astype(np.uint8)
        red = np.clip(rng.normal(10, 4, green.shape), 0, 255).astype(np.uint8)
        filename = f"synthetic_panel_{index + 1:02d}.png"
        Image.fromarray(np.stack([red, green, blue], axis=-1)).save(output_dir / filename)
        rows.append({
            "image_id": f"synthetic_{index + 1:02d}",
            "file_name": filename,
            "panel": index + 1,
            "case_category": category,
            "provenance": "deterministic synthetic teaching image",
            "biological_interpretation_permitted": "no",
        })

    metadata_path = output_dir / "metadata_fig34.csv"
    pd.DataFrame(rows).to_csv(metadata_path, index=False)
    return metadata_path

