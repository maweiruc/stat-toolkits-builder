# TOOLKIT_SPEC.md template

Copy this file into the generated toolkit as:

```text
tools/stat-toolkits-<topic>/TOOLKIT_SPEC.md
```

Then fill every section before writing the rest of the scaffold.

## 1. Identity

Toolkit name:

```text
stat-toolkits-<topic>
```

One-line description:

```text
A documentation-first toolkit for ...
```

Primary statistical object or task:

```text
[fill in]
```

## 2. Core workflow

Write the default workflow as a single line:

```text
normalize problem -> triage -> derive/check -> validate -> report
```

Then define each step:

| Step | Meaning | Required artifact |
| --- | --- | --- |
| Normalize | [fill in] | `notes.md` |
| Triage | [fill in] | `notes.md` |
| Derive/check | [fill in] | `solution.md` |
| Validate | [fill in] | `solution.md` |
| Report | [fill in] | chat summary + `solution.md` |

## 3. User and agent audience

Primary users:

- [ ] researcher
- [ ] coding agent
- [ ] student
- [ ] reviewer
- [ ] collaborator

Agent expectations:

- [fill in what the agent must read first]
- [fill in what the agent must never skip]

## 4. Required input fields

List the fields the toolkit must infer or ask for before solving a task:

```text
1. ...
2. ...
3. ...
```

## 5. Required output fields

List the fields every answer should contain:

```text
1. Normalized problem
2. Triage label
3. ...
```

## 6. Modes

Define the mode labels. Use only modes that matter for this topic.

| Mode | When to use | Required extra checks |
| --- | --- | --- |
| Known | Standard theorem/formula applies after matching | Applicability checks |
| Hard | Formula/theorem lookup is unsafe | Assumption or component ledger |
| Research | No exact result is available | First-principles derivation record |

## 7. Durable artifacts

Generated problem folders use:

```text
problem.tex
notes.md
solution.md
solution.tex
solution.pdf
```

Define the exact meaning of:

- `problem.tex`:
- `notes.md`:
- `solution.md`:
- optional `solution.tex`:
- optional `solution.pdf`:

## 8. Registry decision

Should v0.1 include a registry?

```text
yes / no / later
```

If yes, define the entry shape:

```yaml
example_key:
  field_1: "..."
  field_2: "..."
  warnings:
    - "..."
```

## 9. Danger zones

List the mistakes the toolkit must prevent:

```text
1. ...
2. ...
3. ...
```

## 10. Trial tasks

Add at least two runnable trials.

| Trial | Purpose | Expected behavior |
| --- | --- | --- |
| Trial A | [standard task] | [expected answer shape] |
| Trial B | [hard or ambiguous task] | [expected answer shape] |

## 11. v0.1 scope

In scope:

- [fill in]

Out of scope:

- [fill in]

Known gaps after v0.1:

- [fill in]
