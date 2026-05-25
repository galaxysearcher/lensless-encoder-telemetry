from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import json


@dataclass(frozen=True)
class DatasetArtifact:
    """Small metadata record for a dataset artifact or calibration file."""

    name: str
    path: str
    artifact_type: str
    count: int | None = None
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DatasetManifest:
    """Collection of dataset artifacts used in a validation run."""

    title: str
    artifacts: list[DatasetArtifact]

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
        }

    def write_json(self, path: str | Path) -> Path:
        output = Path(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")
        return output
