# Scaffold workflow

This workflow creates a v0.1 toolkit at:

```text
tools/stat-toolkits-<topic>/
```

## 1. Prepare the spec

1. Normalize the topic into a lowercase kebab-case slug.
2. Answer `builder/interview_questions.md`.
3. Fill `builder/toolkit_spec_template.md`.
4. Save the filled spec as:

```text
tools/stat-toolkits-<topic>/TOOLKIT_SPEC.md
```

Alternatively, create the initial scaffold with:

```bash
python3 scripts/scaffold_toolkit.py \
  --slug <topic> \
  --topic "<human readable topic>" \
  --primary-object "<what the toolkit helps derive/check/validate>"
```

The script creates a starter `TOOLKIT_SPEC.md`; edit it before serious use.

## 2. Create the output folder

Create only this folder:

```text
tools/stat-toolkits-<topic>/
```

Do not create a generated toolkit at repository root.

## 3. Copy templates

Copy the `templates/` tree into the output folder, preserving relative paths.

The generated folder should contain:

```text
README.md
MANUAL.md
TRIAL_GUIDE.md
AGENTS.md
VERSION.md
CHANGELOG.md
CONTRIBUTING.md
pyproject.toml
agent/
theory/
examples/
problems/latex_inbox/
scripts/
tests/
references/
```

## 4. Replace placeholders

Replace every placeholder of the form:

```text
{{TOOLKIT_NAME}}
{{TOPIC}}
{{TOPIC_SLUG}}
{{TOPIC_SLUG_UNDERSCORE}}
{{PYTHON_PACKAGE}}
{{CORE_WORKFLOW}}
{{PRIMARY_OBJECT}}
{{YEAR}}
{{AUTHOR}}
```

Use topic-specific language. Do not leave unresolved placeholders in generated
toolkit files.

The v0.1 scaffold uses generic file names such as `agent/task_spec.md` and
`theory/intro.md`. Mature toolkits may later rename these to topic-specific
names after the protocols stabilize.

## 5. Strengthen v0.1 content

Before calling the scaffold complete:

1. Write a concrete agent reading order in `AGENTS.md`.
2. Define `problem.tex`, `notes.md`, and `solution.md` in
   `agent/problem_artifacts.md`.
3. Add at least two runnable trial prompts in `TRIAL_GUIDE.md`.
4. Add an answer acceptance checklist in `agent/answer_rubric.md`.
5. Add danger zones specific to the topic in `agent/danger_zone.md`.
6. Add minimal examples or TODO-marked registry entries.

## 6. Validate

Run the checks in `builder/v0_scaffold_checklist.md`.

If a registry is included, run:

```bash
python3 scripts/validate_registry.py --strict
python3 -m unittest discover -s tests
```

from inside the generated toolkit folder.
