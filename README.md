# stat-toolkits-builder

A lightweight factory for creating first-version `stat-toolkits-*` research
workflow repositories.

This repository does not try to be another statistical toolkit. Its job is to
turn a statistical topic or research task into a strong v0.1 scaffold under:

```text
tools/stat-toolkits-<topic>/
```

The two canonical reference toolkits are:

- `tools/stat-toolkits-minimax/`
- `tools/stat-toolkits-eif/`

They define the target shape: documentation-first, agent-ready, auditable, and
easy to improve after the first version.

## Factory Goal

A generated v0.1 toolkit should be incomplete in depth but strong in structure.
It should include:

- root docs for humans and agents;
- an agent workflow with task specification, triage, rubrics, and danger zones;
- a durable problem workflow using `problem.tex`, `notes.md`, and `solution.md`;
- theory and examples folders ready for expansion;
- benchmark/trial prompts that make first-day testing possible;
- optional registry, schema, validator, and tests when the topic has reusable
  known results.

## Output Rule

Generated toolkits must be created only at:

```text
tools/stat-toolkits-<topic>/
```

Do not create a generated toolkit at the repository root.

## Recommended User Prompts

This builder is currently an agent-driven, semi-automated process. There is no
one-command scaffold script yet. Use Codex, Claude Code, or another coding agent
with this repository open.

### If the topic is clear

```text
Please use stat-toolkits-builder to create a v0.1 toolkit for [topic].

Output path: tools/stat-toolkits-[topic-slug]/

Requirements:
1. Use only tools/stat-toolkits-minimax and tools/stat-toolkits-eif as reference examples.
2. First read README.md, AGENTS.md, and MANUAL.md.
3. Then read builder/interview_questions.md, builder/toolkit_spec_template.md,
   builder/scaffold_workflow.md, and builder/v0_scaffold_checklist.md.
4. First create TOOLKIT_SPEC.md inside tools/stat-toolkits-[topic-slug]/.
5. Then scaffold the required v0.1 files from templates/.
6. The toolkit must include README.md, MANUAL.md, TRIAL_GUIDE.md, AGENTS.md,
   agent/, theory/, examples/, and problems/latex_inbox/.
7. The problem artifact contract must define problem.tex, notes.md, and solution.md.
8. TRIAL_GUIDE.md must include at least two runnable trial prompts.
9. Do not create generated toolkit files at repo root.
10. Run the scaffold checklist and summarize remaining gaps.
```

### If the topic is still unclear

```text
I want to create a new stat-toolkits-* toolkit, but the structure is not fully clear yet.

Please use builder/interview_questions.md to interview me first.
Do not create files until you can write a complete TOOLKIT_SPEC.md.
```

### Short version

```text
Please use stat-toolkits-builder to create a v0.1 toolkit for [topic].
Output it to tools/stat-toolkits-[topic-slug]/.
Only use stat-toolkits-minimax and stat-toolkits-eif as reference examples.
First write TOOLKIT_SPEC.md, then scaffold all required files, then run the checklist.
```

## How To Use

1. Start with `builder/interview_questions.md`.
2. Convert the answers into `builder/toolkit_spec_template.md`.
3. Follow `builder/scaffold_workflow.md`.
4. Copy and customize the files in `templates/`.
5. Check the result with `builder/v0_scaffold_checklist.md`.
6. Grade the first scaffold using `builder/quality_rubric.md`.

## Repository Layout

```text
builder/       Factory workflow, questions, spec template, checklist, rubric.
templates/     Generic v0.1 toolkit scaffold templates.
examples/      Specs distilled from the two reference toolkits.
tools/         Existing and future stat-toolkits-* repositories.
```

## What This Factory Does Not Do

- It does not prove statistical theorems.
- It does not generate a complete mature toolkit in one pass.
- It does not replace human review of agent protocols, registries, or examples.
- It does not treat registry entries as a substitute for derivation or theorem
  matching.

The intended workflow is iterative: generate a strong v0.1 scaffold, test it on
trial tasks, then deepen the theory, examples, registry, and validation over
time.
