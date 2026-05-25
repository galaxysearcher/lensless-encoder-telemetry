from __future__ import annotations

from pathlib import Path
from typing import Iterable
import hashlib
import re

import numpy as np
from PIL import Image


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    """Return a SHA-256 digest without loading the full file into memory."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_homography(matrix: np.ndarray) -> dict:
    """Validate a candidate 3x3 homography matrix."""
    arr = np.asarray(matrix)
    result = {
        "shape": list(arr.shape),
        "finite": bool(np.isfinite(arr).all()),
        "is_3x3": bool(arr.shape == (3, 3)),
        "determinant": None,
        "status": "CHECK",
    }
    if result["is_3x3"] and result["finite"]:
        determinant = float(np.linalg.det(arr))
        result["determinant"] = determinant
        result["status"] = "PASS" if abs(determinant) > 1e-12 else "CHECK"
    return result


def probe_image(path: str | Path) -> dict:
    """Load an image artifact and return basic integrity statistics."""
    p = Path(path)
    with Image.open(p) as image:
        arr = np.asarray(image)
    return {
        "name": p.name,
        "shape": list(arr.shape),
        "dtype": str(arr.dtype),
        "min": float(np.nanmin(arr)),
        "max": float(np.nanmax(arr)),
        "mean": float(np.nanmean(arr)),
        "std": float(np.nanstd(arr)),
        "finite": bool(np.isfinite(arr).all()),
        "status": "PASS" if np.isfinite(arr).all() else "FAIL",
    }


def extract_numeric_id(path_or_name: str | Path) -> int | None:
    """Extract a numeric image ID from common names such as img_000123.tiff."""
    name = Path(path_or_name).name
    match = re.search(r"(\d+)", name)
    return int(match.group(1)) if match else None


def paired_ids(left: Iterable[int], right: Iterable[int]) -> dict:
    """Compare two collections of sample IDs."""
    left_set = set(left)
    right_set = set(right)
    shared = left_set & right_set
    return {
        "left_count": len(left_set),
        "right_count": len(right_set),
        "shared_count": len(shared),
        "left_only_count": len(left_set - right_set),
        "right_only_count": len(right_set - left_set),
        "status": "PASS" if left_set == right_set else "CHECK",
    }
