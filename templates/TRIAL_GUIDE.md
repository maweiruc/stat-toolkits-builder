# {{TOPIC}} toolkit trial guide

This guide is for first-time testing of the toolkit.

The shortest trial prompt is:

```text
Please read problems/latex_inbox/problem_001/problem.tex and use the
{{TOPIC}} toolkit. If notes.md is missing, create it first. Write the detailed
answer to solution.md.
```

## Trial A: standard task

Problem:

```text
[Write a standard or known problem for {{TOPIC}}.]
```

Expected output:

- normalized problem;
- correct mode;
- final answer or known result;
- validation checks;
- warnings about common misuse.

## Trial B: hard or ambiguous task

Problem:

```text
[Write a hard, ambiguous, or easy-to-misapply problem for {{TOPIC}}.]
```

Expected output:

- no unsafe lookup as final answer;
- explicit assumptions and danger zones;
- hard-mode checks;
- final answer or conditional status.

## Trial C: research-style task

Problem:

```text
[Optional: write a novel or modified problem where no exact result is expected.]
```

Expected output:

- first-principles derivation or proof attempt;
- status label;
- obstruction ledger if unresolved;
- clear caveats.

## Feedback template

```text
Problem tested:
Was the problem normalized correctly?
Was the mode correct?
Were required assumptions stated?
Were validation checks performed?
Was the answer overconfident?
Were notes.md and solution.md used correctly?
What should improve in the next version?
```
