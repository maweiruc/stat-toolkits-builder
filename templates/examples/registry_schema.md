# {{TOPIC}} registry schema

This file describes `examples/registry.yaml`.

The registry is a matching aid. It does not certify mathematical correctness.

## Entry shape

```yaml
stable_snake_case_key:
  target: "..."
  setting: "..."
  assumptions:
    - "..."
  result: "..."
  validation_checks:
    - "..."
  warnings:
    - "..."
  status: "standard / partial / heuristic / example"
  references:
    - "..."
```

## Required fields

The default validator requires:

- `target`
- `setting`
- `assumptions`
- `result`
- `warnings`
- `status`

Strict mode also requires:

- `validation_checks`
- `references`

## Style rules

- Use stable snake_case keys.
- Use lists for `assumptions`, `validation_checks`, `warnings`, and
  `references`.
- Mark incomplete entries as `partial`, `heuristic`, or `example`.
- Do not add a registry entry without warnings.
- Do not use the registry as a substitute for the protocol in `agent/`.
