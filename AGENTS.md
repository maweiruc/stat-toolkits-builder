# Agent instructions for stat-toolkits-builder

This repository is a factory for creating documentation-first statistical
research workflow toolkits.

It is the lightweight builder in the `stat-toolkits-*` series. Keep it smaller
than the method-specific repositories; its job is to scaffold and guide, not to
contain full statistical theory libraries.

## First files to read

For any request to create or revise a toolkit scaffold, read:

1. `README.md`
2. `MANUAL.md`
3. `builder/interview_questions.md`
4. `builder/toolkit_spec_template.md`
5. `builder/scaffold_workflow.md`
6. `builder/v0_scaffold_checklist.md`
7. `builder/quality_rubric.md`
8. `examples/minimax_toolkit_spec.md`
9. `examples/eif_toolkit_spec.md`

Use the built-in reference specs as examples:

- `examples/minimax_toolkit_spec.md`
- `examples/eif_toolkit_spec.md`

The full reference repositories are external and are not required for normal
builder use:

- https://github.com/maweiruc/stat-toolkits-minimax
- https://github.com/maweiruc/stat-toolkits-eif

## Output rule

Every generated toolkit must be created at:

```text
tools/stat-toolkits-<topic>/
```

Never create a generated toolkit at repository root. Root-level files are for
the factory itself.

## Default workflow

When the user asks to create a new `stat-toolkits-*` toolkit:

1. Normalize the requested topic into a lowercase kebab-case `<topic>` slug.
2. Build or ask for the missing items in `builder/interview_questions.md`.
3. Write a `TOOLKIT_SPEC.md` for the new toolkit.
4. Create the output folder `tools/stat-toolkits-<topic>/`.
5. Copy the v0.1 structure from `templates/`.
6. Replace placeholders with topic-specific content.
7. Ensure `AGENTS.md` has a concrete reading order.
8. Ensure `agent/problem_artifacts.md` defines `problem.tex`, `notes.md`, and
   `solution.md`.
9. Ensure `TRIAL_GUIDE.md` includes at least two runnable trial prompts.
10. Ensure no unresolved placeholders remain outside files that are explicitly
    templates.
11. Summarize the generated files and any known gaps.

## Design standard

Generated v0.1 toolkits should be strong enough for immediate trial use, even
if their theory and registry content are still shallow.

Every toolkit should contain:

- human entry points: `README.md`, `MANUAL.md`, `TRIAL_GUIDE.md`;
- agent entry point: `AGENTS.md`;
- agent protocols under `agent/`;
- theory notes under `theory/`;
- examples, benchmarks, and optional registry under `examples/`;
- durable problem inbox under `problems/latex_inbox/`;
- optional validation scripts and tests.

## Do not overbuild

Do not try to make the first version complete. Prefer a clear scaffold with
honest TODO markers over invented theory depth, fake registry entries, or
overconfident acceptance criteria.
