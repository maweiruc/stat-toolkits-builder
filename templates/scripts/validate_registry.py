#!/usr/bin/env python3
"""Validate the toolkit registry YAML file.

This checks structure and metadata only. It does not certify mathematical
correctness.
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ModuleNotFoundError:  # pragma: no cover - fallback for fresh systems
    yaml = None


DEFAULT_REGISTRY = Path("examples/registry.yaml")
KEY_RE = re.compile(r"^[a-z][a-z0-9_]*$")
REQUIRED_FIELDS = {
    "target",
    "setting",
    "assumptions",
    "result",
    "warnings",
    "status",
}
STRICT_FIELDS = {"validation_checks", "references"}
LIST_FIELDS = {"assumptions", "validation_checks", "warnings", "references"}
STRING_FIELDS = {"target", "setting", "result", "status"}


def is_nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_list(key: str, field: str, value: object) -> list[str]:
    if not isinstance(value, list) or not value:
        return [f"{key}: `{field}` must be a nonempty list"]
    if not all(is_nonempty_string(item) for item in value):
        return [f"{key}: `{field}` must contain nonempty strings"]
    return []


def validate_entry(key: str, entry: object, *, strict: bool) -> list[str]:
    errors: list[str] = []

    if not KEY_RE.match(key):
        errors.append(f"{key}: key must be snake_case")

    if not isinstance(entry, dict):
        return errors + [f"{key}: entry must be a mapping"]

    for field in sorted(REQUIRED_FIELDS - entry.keys()):
        errors.append(f"{key}: missing required field `{field}`")

    if strict:
        for field in sorted(STRICT_FIELDS - entry.keys()):
            errors.append(f"{key}: strict mode missing `{field}`")

    for field in STRING_FIELDS:
        if field in entry and not is_nonempty_string(entry[field]):
            errors.append(f"{key}: `{field}` must be a nonempty string")

    for field in LIST_FIELDS:
        if field in entry:
            errors.extend(validate_list(key, field, entry[field]))

    return errors


def parse_scalar(value: str) -> str:
    value = value.strip()
    if not value:
        return ""
    if value[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError):
            return value.strip("'\"")
        return str(parsed)
    return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used by the scaffolded registry template."""

    data: dict[str, Any] = {}
    current_key: str | None = None
    current_field: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        if not line.startswith(" "):
            if not line.endswith(":"):
                raise ValueError(f"unsupported top-level line: {line}")
            current_key = line[:-1].strip()
            data[current_key] = {}
            current_field = None
            continue

        if current_key is None:
            raise ValueError(f"field before entry: {line}")

        stripped = line.strip()
        if stripped.startswith("- "):
            if current_field is None:
                raise ValueError(f"list item without field: {line}")
            data[current_key].setdefault(current_field, []).append(
                parse_scalar(stripped[2:])
            )
            continue

        if ":" not in stripped:
            raise ValueError(f"unsupported field line: {line}")

        field, value = stripped.split(":", 1)
        current_field = field.strip()
        if value.strip():
            data[current_key][current_field] = parse_scalar(value)
        else:
            data[current_key][current_field] = []

    return data


def load_registry(path: Path) -> dict[str, Any]:
    text = path.read_text()
    data = yaml.safe_load(text) if yaml is not None else parse_simple_yaml(text)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: registry must be a mapping")
    return data


def validate_registry(path: Path, *, strict: bool) -> list[str]:
    try:
        data = load_registry(path)
    except Exception as exc:
        return [f"{path}: failed to parse YAML: {exc}"]

    errors: list[str] = []
    for key, entry in data.items():
        if str(key).startswith("_"):
            continue
        errors.extend(validate_entry(str(key), entry, strict=strict))
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", default=str(DEFAULT_REGISTRY))
    parser.add_argument("--strict", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    errors = validate_registry(Path(args.path), strict=args.strict)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    mode = "strict" if args.strict else "default"
    print(f"OK: {args.path} passed {mode} validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
