# stat-toolkits-builder

Current version: **v0.1.0**. See `VERSION.md` and `CHANGELOG.md`.

A lightweight factory for creating first-version `stat-toolkits-*` research
workflow repositories. Give it a statistical topic, and it helps produce a
documentation-first, agent-ready v0.1 scaffold under:

```text
tools/stat-toolkits-<topic>/
```

This repository is part of the `stat-toolkits-*` series:

- https://github.com/maweiruc/stat-toolkits-eif
- https://github.com/maweiruc/stat-toolkits-minimax
- https://github.com/maweiruc/stat-toolkits-builder

The two method-specific repositories are external references. This builder
stays small and self-contained by keeping only distilled example specs.

## Quick Start Prompt

Open this repository in Codex, Claude Code, or another coding agent and paste:

```text
Please use stat-toolkits-builder to create a v0.1 toolkit for [topic].

Output path: tools/stat-toolkits-[topic-slug]/

Read README.md, AGENTS.md, MANUAL.md, builder/interview_questions.md,
builder/toolkit_spec_template.md, builder/scaffold_workflow.md, and
builder/v0_scaffold_checklist.md.

Use only examples/minimax_toolkit_spec.md and examples/eif_toolkit_spec.md as
built-in reference examples. First write TOOLKIT_SPEC.md inside the output
folder, then scaffold the required v0.1 files from templates/.

The toolkit must include README.md, MANUAL.md, TRIAL_GUIDE.md, AGENTS.md,
agent/, theory/, examples/, and problems/latex_inbox/. The problem artifact
contract must define problem.tex, notes.md, and solution.md. TRIAL_GUIDE.md
must include at least two runnable trial prompts.

Do not create generated toolkit files at repo root. Run the scaffold checklist
and summarize remaining topic-specific gaps.
```

If the topic is still unclear, use this instead:

```text
I want to create a new stat-toolkits-* toolkit, but the structure is not fully clear yet.

Please use builder/interview_questions.md to interview me first.
Do not create files until you can write a complete TOOLKIT_SPEC.md.
```

## What It Creates

A generated v0.1 toolkit is intentionally incomplete in theory depth, but it
should be strong enough for first-day trials. It includes:

- human entry points: `README.md`, `MANUAL.md`, `TRIAL_GUIDE.md`;
- agent entry point: `AGENTS.md`;
- agent protocols under `agent/`;
- theory notes under `theory/`;
- examples, benchmark tasks, and optional registry files under `examples/`;
- a durable problem inbox under `problems/latex_inbox/`;
- optional lightweight validation scripts and tests.

For the full workflow, see `MANUAL.md`, `AGENTS.md`, and the files in
`builder/`.

## Output Rule

Generated toolkits must be created only at:

```text
tools/stat-toolkits-<topic>/
```

Do not create a generated toolkit at the repository root.

## Reference Specs

The two built-in reference specs are:

- `examples/minimax_toolkit_spec.md`
- `examples/eif_toolkit_spec.md`

They define the target shape: documentation-first, agent-ready, auditable, and
easy to improve after the first version. The full reference repositories are
external:

- https://github.com/maweiruc/stat-toolkits-minimax
- https://github.com/maweiruc/stat-toolkits-eif

## Optional Script Scaffold

Use this when you want to create the initial file tree before asking an agent to
fill in topic-specific content.

```bash
python3 scripts/scaffold_toolkit.py \
  --slug [topic-slug] \
  --topic "[Human readable topic]" \
  --primary-object "[what the toolkit helps derive/check/validate]"
```

This creates:

```text
tools/stat-toolkits-[topic-slug]/
```

The script gives a generic v0.1 scaffold. After it runs, use an agent to edit
`TOOLKIT_SPEC.md`, strengthen the agent protocols, and add topic-specific trial
tasks.

## Repository Layout

```text
VERSION.md     Current release version and scope.
CHANGELOG.md   Release history.
CONTRIBUTING.md Contribution and validation guidance.
builder/       Factory workflow, questions, spec template, checklist, rubric.
scripts/       Lightweight scaffold automation.
templates/     Generic v0.1 toolkit scaffold templates.
examples/      Self-contained specs distilled from the two reference toolkits.
tools/         Output location for generated stat-toolkits-* repositories.
```

## Checks

Run:

```bash
python3 templates/scripts/validate_registry.py templates/examples/registry.yaml --strict
python3 -m unittest discover -s templates/tests
python3 scripts/scaffold_toolkit.py --help
```

This factory does not generate a complete mature toolkit in one pass. The
intended workflow is iterative: generate a strong v0.1 scaffold, test it on
trial tasks, then deepen the theory, examples, registry, and validation over
time.
