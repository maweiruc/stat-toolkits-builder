# Contributing

This repository is the lightweight builder for the `stat-toolkits-*` series.
Contributions should make it easier to create strong first-version statistical
research workflow toolkits without turning the builder into a heavy framework.

## Principles

- Keep the builder self-contained.
- Keep full reference toolkits external; update `examples/*_toolkit_spec.md`
  when a reusable pattern should be copied into the builder.
- Prefer small, auditable templates over large generated theory content.
- Do not add fake registry entries, invented examples, or overconfident
  mathematical claims.
- Generated toolkits should always be created under
  `tools/stat-toolkits-<topic>/`.

## Before submitting changes

Run:

```bash
python3 templates/scripts/validate_registry.py templates/examples/registry.yaml --strict
python3 -m unittest discover -s templates/tests
```

For script edits, also run:

```bash
python3 scripts/scaffold_toolkit.py --help
```

If you change the public scaffold shape, update:

- `README.md`
- `MANUAL.md`
- `AGENTS.md`
- `builder/v0_scaffold_checklist.md`
- `CHANGELOG.md`
