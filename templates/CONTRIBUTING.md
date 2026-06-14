# Contributing

Contributions should improve the toolkit without weakening its auditability.

## Principles

- Keep problem statements, proof state, and final answers separate.
- Do not add registry entries without warnings and applicability checks.
- Do not cite private local paths in public files.
- Do not claim complete coverage unless the supporting files justify it.
- Prefer small, reviewable updates.

## Before submitting changes

If a registry is included, run:

```bash
python3 scripts/validate_registry.py --strict
python3 -m unittest discover -s tests
```

Update `CHANGELOG.md` when changing public behavior, protocols, or validation
rules.
