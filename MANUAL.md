# stat-toolkits-builder manual

This manual explains how to use the factory to create a first version of a new
`stat-toolkits-*` repository.

This repository is the lightweight builder in the `stat-toolkits-*` series. The
full method-specific reference repositories are:

- https://github.com/maweiruc/stat-toolkits-minimax
- https://github.com/maweiruc/stat-toolkits-eif

## Short version

Use this repository to produce a new scaffold at:

```text
tools/stat-toolkits-<topic>/
```

The generated scaffold should be immediately usable for trial prompts, but it
does not need to be theoretically complete.

## Recommended prompt

```text
Use stat-toolkits-builder to create a v0.1 toolkit for [topic].

Use only examples/minimax_toolkit_spec.md and examples/eif_toolkit_spec.md as
built-in reference examples.

Output the generated toolkit at tools/stat-toolkits-[topic-slug]/.
First create TOOLKIT_SPEC.md in the generated toolkit, then scaffold the root
docs, agent protocols, theory docs, examples, problem inbox, and validation
files.
```

## Creation workflow

1. Answer the factory questions in `builder/interview_questions.md`.
2. Convert the answers into the spec format in
   `builder/toolkit_spec_template.md`.
3. Follow `builder/scaffold_workflow.md` to create files from `templates/`.
4. Use `builder/v0_scaffold_checklist.md` before calling the scaffold complete.
5. Use `builder/quality_rubric.md` to decide whether v0.1 is strong enough.

## What the first version should prioritize

The first version should prioritize:

- the core workflow;
- mode labels and triage;
- agent reading order;
- durable problem artifacts;
- answer acceptance rubric;
- danger zones;
- trial prompts;
- registry schema only if the topic has reusable known results.

It should not pretend to contain a mature theory library or complete result
registry.

## Reference examples

Use `examples/minimax_toolkit_spec.md` as the built-in reference for a
proof/rate toolkit with upper and lower bound ledgers.

Use `examples/eif_toolkit_spec.md` as the built-in reference for a
derivation/validation toolkit with target triage, regularity checks, and status
labels.

Full reference repositories are external and optional:

- https://github.com/maweiruc/stat-toolkits-minimax
- https://github.com/maweiruc/stat-toolkits-eif

Do not introduce additional reference examples unless they actually exist in
`tools/`.

## Output contract

Every generated toolkit must include:

```text
README.md
MANUAL.md
TRIAL_GUIDE.md
AGENTS.md
VERSION.md
CHANGELOG.md
CONTRIBUTING.md
agent/
theory/
examples/
problems/latex_inbox/
```

If a registry is included, also include:

```text
examples/registry.yaml
examples/registry_schema.md
scripts/validate_registry.py
tests/test_registry.py
```

## Public trial checklist

Before sharing with a new user, check:

- the user can understand the first prompt in `README.md`;
- the user knows generated toolkits go under `tools/stat-toolkits-<topic>/`;
- `examples/minimax_toolkit_spec.md` and `examples/eif_toolkit_spec.md` are
  enough as style references;
- the scaffold script is presented as optional, not as the main workflow.
