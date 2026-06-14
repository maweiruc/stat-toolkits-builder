# Agent instructions for the {{TOPIC}} toolkit

This repository is a documentation-first toolkit for {{PRIMARY_OBJECT}}.

Treat the files in `agent/`, `theory/`, `examples/`, and `problems/` as the
working system.

## First files to read

For any {{TOPIC}} task, read:

1. `agent/task_spec.md`
2. `agent/problem_artifacts.md`
3. `agent/triage.md`
4. `agent/hard_problem_protocol.md`
5. `agent/research_problem_protocol.md`
6. `agent/danger_zone.md`
7. `agent/answer_rubric.md`
8. `theory/intro.md`
9. `theory/proof_or_derivation_guide.md`
10. `theory/heuristics.md`
11. `examples/workflow_examples.md`
12. `examples/benchmark_tasks.md`

Use `examples/registry.yaml` only after checking that the problem specification
matches. The registry is a comparison aid, not a substitute for derivation,
proof, or validation.

## Default workflow

When the user gives a problem:

1. Normalize the problem statement.
2. State the required input fields from `agent/task_spec.md`.
3. Assign a mode using `agent/triage.md`.
4. Check danger zones before using familiar results.
5. Follow the relevant standard, hard, or research protocol.
6. Validate the answer using `agent/validation_tests.md`.
7. Check the final response against `agent/answer_rubric.md`.
8. State final result, status, caveats, and unresolved assumptions.

## LaTeX inbox behavior

For problems under `problems/latex_inbox/problem_*/problem.tex`, follow
`agent/problem_artifacts.md`.

If `notes.md` is missing, create it before solving. If `solution.md` exists,
read it before revising or summarizing. After solving, update `notes.md` as a
compact checkpoint and write the detailed answer to `solution.md`.

The chat response should be a concise summary. It is not the only durable
answer.

## Do not overclaim

Do not state a result as final unless the checks in `agent/answer_rubric.md`
are satisfied. If the task is unresolved, use the status labels from the hard or
research protocol and explain the obstruction.
