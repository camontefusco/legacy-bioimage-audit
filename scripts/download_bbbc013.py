"""Opt-in retrieval of the CC BY 3.0 BBBC013 two-channel case."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile


BASE_URL = "https://data.broadinstitute.org/bbbc/BBBC013"
ARCHIVE = "BBBC013_v1_images_bmp.zip"
PLATEMAP = "BBBC013_v1_platemap_all.txt"


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as response, destination.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)


def safe_extract(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    with ZipFile(archive) as handle:
        for member in handle.infolist():
            target = (destination / member.filename).resolve()
            if destination != target and destination not in target.parents:
                raise ValueError(f"Unsafe archive member: {member.filename}")
        handle.extractall(destination)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--destination", type=Path, default=Path("data/external/BBBC013")
    )
    parser.add_argument("--download-only", action="store_true")
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)

    archive = args.destination / ARCHIVE
    if not archive.exists():
        print(f"Downloading {BASE_URL}/{ARCHIVE}")
        download(f"{BASE_URL}/{ARCHIVE}", archive)
    if not args.download_only:
        safe_extract(archive, args.destination)

    plate_map = args.destination / PLATEMAP
    if not plate_map.exists():
        print(f"Downloading {BASE_URL}/{PLATEMAP}")
        download(f"{BASE_URL}/{PLATEMAP}", plate_map)
    print(f"BBBC013 available under {args.destination}")


if __name__ == "__main__":
    main()
