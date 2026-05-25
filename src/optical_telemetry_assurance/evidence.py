from __future__ import annotations

from pathlib import Path
from typing import Any
import json


def write_json_report(report: dict[str, Any], path: str | Path) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return output


def write_markdown_report(report: dict[str, Any], path: str | Path) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    lines = [f"# {report.get('title', 'Validation Report')}", ""]
    if "status" in report:
        lines.append(f"Status: **{report['status']}**")
        lines.append("")
    if "headline" in report:
        lines.append("## Headline")
        for key, value in report["headline"].items():
            lines.append(f"- `{key}`: `{value}`")
        lines.append("")
    if "scope_notes" in report:
        lines.append("## Scope notes")
        for item in report["scope_notes"]:
            lines.append(f"- {item}")
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")
    return output
