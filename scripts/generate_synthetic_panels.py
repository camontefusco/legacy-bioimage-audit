#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.synthetic import generate_synthetic_dataset

print(generate_synthetic_dataset(ROOT / "data" / "synthetic_panels"))

