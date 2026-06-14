# {{TOOLKIT_NAME}}

Current version: **v0.1.0**. See `VERSION.md` and `CHANGELOG.md`.

A documentation-first toolkit for {{PRIMARY_OBJECT}}.

This repository is part of the `stat-toolkits-*` series: documentation-first
toolkits for statistical research workflows.

The main goal is not black-box lookup. The goal is an auditable workflow:

```text
{{CORE_WORKFLOW}}
```

## Quick Start

For an inbox problem:

```text
Please read problems/latex_inbox/problem_001/problem.tex and use the
{{TOPIC}} toolkit. If notes.md is missing, create it first. Write the detailed
answer to solution.md.
```

For a problem written in chat:

```text
Please use the {{TOPIC}} toolkit in this folder.

Problem:
...

Goal:
...

Please normalize the problem, choose the correct mode, derive or check the
result, validate it, and state caveats.
```

## Main Files

Human entry points:

- `MANUAL.md`: usage manual.
- `TRIAL_GUIDE.md`: first tests and expected behavior.
- `theory/intro.md`: conceptual introduction.

Agent entry points:

- `AGENTS.md`: operating instructions and reading order.
- `agent/task_spec.md`: standard task workflow.
- `agent/problem_artifacts.md`: `problem.tex`, `notes.md`, and `solution.md`
  artifact contract.
- `agent/triage.md`: mode selection.
- `agent/answer_rubric.md`: acceptance rubric.
- `agent/danger_zone.md`: common misuse cases.

Knowledge and examples:

- `theory/proof_or_derivation_guide.md`
- `theory/heuristics.md`
- `theory/worked_derivations.md`
- `examples/workflow_examples.md`
- `examples/benchmark_tasks.md`
- `examples/registry.yaml`

## Problem Inbox

Use `problems/latex_inbox/` for LaTeX or free-form problems.

Generated artifacts should follow `agent/problem_artifacts.md`: keep
`notes.md` as a compact state checkpoint and put the detailed final answer in
`solution.md`.

## Engineering Checks

If this toolkit includes a registry, run:

```bash
python3 scripts/validate_registry.py --strict
python3 -m unittest discover -s tests
```

The Python layer is only for validation utilities. It is not a theorem prover,
formula engine, or replacement for the workflow.
