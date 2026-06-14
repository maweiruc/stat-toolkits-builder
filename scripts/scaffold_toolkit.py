#!/usr/bin/env python3
"""Create a v0.1 stat-toolkits-* scaffold from templates.

The output path is always:

    tools/stat-toolkits-<slug>/

The script intentionally creates a strong generic scaffold, not a mature
topic-specific toolkit. After running it, edit TOOLKIT_SPEC.md and the generated
protocol files to add real topic depth.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates"
TOOLS = ROOT / "tools"


DEFAULT_WORKFLOW = (
    "normalize problem -> triage -> derive/check -> validate -> report"
)


def slugify(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    if not slug:
        raise ValueError("slug is empty after normalization")
    return slug


def package_name(slug: str) -> str:
    return f"{slug.replace('-', '_')}_toolkit"


def replace_placeholders(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text()
    for key, value in replacements.items():
        text = text.replace(f"{{{{{key}}}}}", value)
    path.write_text(text)


def iter_text_files(base: Path) -> list[Path]:
    text_suffixes = {
        "",
        ".md",
        ".py",
        ".toml",
        ".yaml",
        ".yml",
        ".tex",
        ".txt",
        ".gitignore",
    }
    files: list[Path] = []
    for path in base.rglob("*"):
        if not path.is_file():
            continue
        if path.name == ".gitignore" or path.suffix in text_suffixes:
            files.append(path)
    return sorted(files)


def build_spec(
    *,
    toolkit_name: str,
    topic: str,
    primary_object: str,
    core_workflow: str,
    slug: str,
) -> str:
    return f"""# TOOLKIT_SPEC.md

## 1. Identity

Toolkit name:

```text
{toolkit_name}
```

One-line description:

```text
A documentation-first toolkit for {primary_object}.
```

Primary statistical object or task:

```text
{primary_object}
```

Topic slug:

```text
{slug}
```

## 2. Core workflow

```text
{core_workflow}
```

## 3. Required input fields

TODO: Replace this section using `builder/interview_questions.md`.

```text
1. Problem setting
2. Target or object
3. Model or assumptions
4. Desired output
```

## 4. Required output fields

TODO: Replace this section with topic-specific answer requirements.

```text
1. Normalized problem
2. Triage label
3. Assumptions
4. Derivation/proof/check route
5. Validation checks
6. Final status
7. Caveats
```

## 5. Modes

| Mode | When to use | Required checks |
| --- | --- | --- |
| Standard / Known | A standard result applies after matching | Applicability checks |
| Hard | Familiar lookup is unsafe | Assumption or component ledger |
| Research | No exact result is available | First-principles derivation record |

## 6. Durable artifacts

Generated problem folders use:

```text
problem.tex
notes.md
solution.md
solution.tex
solution.pdf
```

`notes.md` is the compact state checkpoint. `solution.md` is the detailed
durable answer. Optional TeX/PDF exports are generated only when requested.

## 7. Registry decision

```text
TODO: yes / no / later
```

## 8. Danger zones

TODO: Add topic-specific misuse cases.

## 9. Trial tasks

TODO: Add at least two runnable trials before first serious use.

## 10. v0.1 scope

In scope:

- Strong scaffold and first trial use.

Out of scope:

- Complete theory coverage.
- Mature registry.
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--slug",
        required=True,
        help="Kebab-case topic slug, for tools/stat-toolkits-<slug>/.",
    )
    parser.add_argument(
        "--topic",
        help="Human-readable topic name. Defaults to the slug with spaces.",
    )
    parser.add_argument(
        "--primary-object",
        help="Description used in README/MANUAL. Defaults to the topic.",
    )
    parser.add_argument(
        "--core-workflow",
        default=DEFAULT_WORKFLOW,
        help="One-line workflow shown in docs.",
    )
    parser.add_argument(
        "--author",
        default="Wei Ma",
        help="Author name for LICENSE.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing generated toolkit folder.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        slug = slugify(args.slug)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    topic = args.topic or slug.replace("-", " ")
    primary_object = args.primary_object or topic
    toolkit_name = f"stat-toolkits-{slug}"
    output = TOOLS / toolkit_name

    if not TEMPLATES.is_dir():
        print(f"ERROR: templates directory not found: {TEMPLATES}", file=sys.stderr)
        return 1

    if output.exists():
        if not args.force:
            print(
                f"ERROR: output already exists: {output}\n"
                "Use --force only if you intentionally want to replace it.",
                file=sys.stderr,
            )
            return 1
        shutil.rmtree(output)

    shutil.copytree(TEMPLATES, output)

    replacements = {
        "TOOLKIT_NAME": toolkit_name,
        "TOPIC": topic,
        "TOPIC_SLUG": slug,
        "TOPIC_SLUG_UNDERSCORE": slug.replace("-", "_"),
        "PYTHON_PACKAGE": package_name(slug),
        "PRIMARY_OBJECT": primary_object,
        "CORE_WORKFLOW": args.core_workflow,
        "YEAR": str(dt.date.today().year),
        "AUTHOR": args.author,
    }

    for path in iter_text_files(output):
        replace_placeholders(path, replacements)

    (output / "TOOLKIT_SPEC.md").write_text(
        build_spec(
            toolkit_name=toolkit_name,
            topic=topic,
            primary_object=primary_object,
            core_workflow=args.core_workflow,
            slug=slug,
        )
    )

    print(f"Created {output.relative_to(ROOT)}")
    print("Next steps:")
    print("  1. Edit TOOLKIT_SPEC.md.")
    print("  2. Replace generic protocol text with topic-specific content.")
    print("  3. Run scripts/validate_registry.py and unittest if registry is kept.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
