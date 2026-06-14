# v0.1 scaffold checklist

Use this checklist before declaring a generated toolkit usable.

## Path and layout

- [ ] The toolkit is under `tools/stat-toolkits-<topic>/`.
- [ ] No generated toolkit files were placed at repository root.
- [ ] `TOOLKIT_SPEC.md` exists in the generated toolkit.
- [ ] Root docs exist: `README.md`, `MANUAL.md`, `TRIAL_GUIDE.md`,
      `AGENTS.md`, `VERSION.md`, `CHANGELOG.md`, `CONTRIBUTING.md`.
- [ ] Subdirectories exist: `agent/`, `theory/`, `examples/`,
      `problems/latex_inbox/`.

## Agent usability

- [ ] `AGENTS.md` has a concrete reading order.
- [ ] `agent/task_spec.md` defines required input and output fields.
- [ ] `agent/problem_artifacts.md` defines `problem.tex`, `notes.md`, and
      `solution.md`.
- [ ] `agent/triage.md` defines the mode labels.
- [ ] `agent/answer_rubric.md` states acceptance criteria.
- [ ] `agent/danger_zone.md` names topic-specific misuse cases.

## Trial readiness

- [ ] `TRIAL_GUIDE.md` includes at least two runnable trial prompts.
- [ ] At least one trial is standard or known.
- [ ] At least one trial is hard, ambiguous, or research-style.
- [ ] Trial expected behavior is stated.

## Content quality

- [ ] The core workflow appears in `README.md`, `MANUAL.md`, and `AGENTS.md`.
- [ ] The generated toolkit does not claim mature coverage.
- [ ] TODOs are explicit and honest.
- [ ] No unresolved `{{PLACEHOLDER}}` tokens remain outside intentional
      template files.

## Registry and validation

- [ ] If a registry is included, `examples/registry_schema.md` explains fields.
- [ ] If a registry is included, `scripts/validate_registry.py` runs.
- [ ] If a registry is included, `tests/test_registry.py` runs.
- [ ] Registry entries are marked example/TODO unless verified.
