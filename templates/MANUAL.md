# {{TOPIC}} toolkit manual

This toolkit helps a researcher or coding agent work on {{PRIMARY_OBJECT}}.

The core workflow is:

```text
{{CORE_WORKFLOW}}
```

The toolkit is intentionally documentation-first. The most important output is
a clean, auditable record, not a black-box answer.

## Quick start

For an inbox problem:

```text
Please read problems/latex_inbox/problem_001/problem.tex and use the
{{TOPIC}} toolkit. If notes.md is missing, create it first. Write the detailed
answer to solution.md.
```

For a new problem in chat:

```text
Please use the {{TOPIC}} toolkit in this folder.

[Paste problem here.]

Please return:
1. normalized problem
2. triage label
3. derivation or proof route
4. validation checks
5. final answer or unresolved status
6. caveats
```

## What the agent should read

For ordinary use:

1. `AGENTS.md`
2. `agent/task_spec.md`
3. `agent/problem_artifacts.md`
4. `agent/triage.md`
5. `agent/hard_problem_protocol.md`
6. `agent/research_problem_protocol.md`
7. `agent/danger_zone.md`
8. `agent/answer_rubric.md`
9. `theory/intro.md`
10. `theory/proof_or_derivation_guide.md`
11. `theory/heuristics.md`
12. `examples/workflow_examples.md`
13. `examples/benchmark_tasks.md`

For registry maintenance, also read:

1. `examples/registry_schema.md`
2. `scripts/validate_registry.py`
3. `tests/test_registry.py`

## Modes

Define and use the modes from `agent/triage.md`. Do not use the registry or a
familiar theorem/formula until the problem specification matches.

## A good final answer

A good answer contains:

1. problem specification;
2. mode and triage route;
3. derivation, proof, theorem match, or validation route;
4. checks required by `agent/answer_rubric.md`;
5. final statement or status label;
6. caveats and unresolved assumptions.

For inbox problems, also update:

- `notes.md`: compact state checkpoint;
- `solution.md`: detailed durable answer;
- optional `solution.tex` and `solution.pdf` only when requested.
