from __future__ import annotations

import argparse
from pathlib import Path
import json


def count_files(root: Path, patterns: list[str]) -> dict:
    return {pattern: len(list(root.rglob(pattern))) if root.exists() else 0 for pattern in patterns}


def main():
    parser = argparse.ArgumentParser(description="Create a local dataset inventory without moving or loading raw data.")
    parser.add_argument("--waller-root", default=None, help="Optional path to a local Waller dataset root.")
    parser.add_argument("--idtoolkit-root", default=None, help="Optional path to a local IDToolkit dataset root.")
    parser.add_argument("--out", default="artifacts/dataset_inventory.json")
    args = parser.parse_args()

    report = {
        "title": "Dataset Stack Inventory",
        "status": "CHECK_LOCAL_PATHS",
        "datasets": [],
        "scope_notes": [
            "File counts do not validate model performance.",
            "Pairing, calibration, and split discipline must be tested separately.",
        ],
    }

    if args.waller_root:
        root = Path(args.waller_root)
        report["datasets"].append({
            "name": "Waller lensless imaging local root",
            "root_exists": root.exists(),
            "counts": count_files(root, ["*.tiff", "*.tif", "*.npy", "*.npz", "*.json"]),
            "role": "lensless optical measurement-to-target benchmark",
        })

    if args.idtoolkit_root:
        root = Path(args.idtoolkit_root)
        report["datasets"].append({
            "name": "IDToolkit local root",
            "root_exists": root.exists(),
            "counts": count_files(root, ["*.csv", "*.json", "*.yaml", "*.yml"]),
            "role": "nanophotonic proxy adapter and stress-test dataset",
        })

    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
