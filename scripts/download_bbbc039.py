"""Opt-in retrieval of the CC0 BBBC039 teaching case.

The archives are downloaded from the Broad Institute, not mirrored by this
repository. Run this script only when you want the external case-study data.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile


BASE_URL = "https://data.broadinstitute.org/bbbc/BBBC039"
ARCHIVES = ("images.zip", "masks.zip", "metadata.zip")


def safe_extract(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    with ZipFile(archive) as handle:
        for member in handle.infolist():
            target = (destination / member.filename).resolve()
            if destination != target and destination not in target.parents:
                raise ValueError(f"Unsafe archive member: {member.filename}")
        handle.extractall(destination)


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urlopen(url) as response, destination.open("wb") as output:
        while chunk := response.read(1024 * 1024):
            output.write(chunk)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--destination",
        type=Path,
        default=Path("data/external/BBBC039"),
        help="Ignored directory for downloaded and extracted third-party data.",
    )
    parser.add_argument(
        "--download-only",
        action="store_true",
        help="Keep the ZIP archives without extracting them.",
    )
    args = parser.parse_args()

    args.destination.mkdir(parents=True, exist_ok=True)
    for name in ARCHIVES:
        archive = args.destination / name
        if not archive.exists():
            print(f"Downloading {BASE_URL}/{name}")
            download(f"{BASE_URL}/{name}", archive)
        else:
            print(f"Using existing {archive}")
        if not args.download_only:
            safe_extract(archive, args.destination)
    print(f"BBBC039 available under {args.destination}")


if __name__ == "__main__":
    main()
