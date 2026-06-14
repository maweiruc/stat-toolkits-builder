# {{TOPIC}} problem artifact conventions

This file defines the durable files inside:

```text
problems/latex_inbox/problem_*/
```

## Standard files

```text
problem.tex
notes.md
solution.md
solution.tex
solution.pdf
```

### `problem.tex`

User-provided problem statement. It may be a complete LaTeX document, a paper
excerpt, or a smaller mathematical fragment.

Rules:

- read it first;
- treat it as the source of truth;
- do not rewrite it unless the user explicitly asks.

### `notes.md`

Compact state checkpoint and context index.

If absent, generate it before solving. If present, read it as guidance.

It should include:

- normalized problem;
- mode and triage route;
- assumptions and danger zones;
- candidate or final answer snapshot;
- validation plan;
- unresolved gaps;
- pointer to `solution.md`.

### `solution.md`

Durable detailed answer. It should be complete enough to audit without the chat
transcript.

It should include:

- normalized problem;
- assumptions;
- derivation, proof, theorem match, or validation route;
- final answer or status label;
- checks from `agent/validation_tests.md`;
- caveats and unresolved gaps.

### Optional `solution.tex`

LaTeX export of `solution.md`. Generate only when requested.

### Optional `solution.pdf`

Compiled PDF export of `solution.tex`. Generate only when requested.

## Lifecycle

1. Read `problem.tex`.
2. Read `notes.md` if it exists.
3. Read `solution.md` if it exists.
4. Create `notes.md` if missing.
5. Solve using the toolkit workflow.
6. Write or update `solution.md`.
7. Update `notes.md` as a compact checkpoint.
8. Generate `solution.tex` or `solution.pdf` only when requested.
9. In chat, give a concise summary.
