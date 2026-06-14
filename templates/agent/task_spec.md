# {{TOPIC}} agent task specification

This document defines the standard protocol for an agent working on
{{PRIMARY_OBJECT}}.

The agent must not start from a memorized result. It must normalize the
problem, classify the task, derive or check the result, validate it, and state
caveats.

## Required input

For every task, infer or ask for:

```text
Problem object:
Observed data or mathematical setting:
Target:
Model or assumptions:
Loss, metric, or validity criterion:
Asymptotic or limiting regime:
Desired output:
```

Customize this list for the topic before release.

## Task classification

Assign one of the mode labels from `triage.md`:

- Standard or Known
- Hard
- Research

## Required answer fields

Every answer should contain:

```text
1. Normalized problem
2. Triage label
3. Required assumptions
4. Derivation/proof/check route
5. Validation checks
6. Final result or status label
7. Caveats and unresolved gaps
```

If any required input is missing, state a provisional assumption and mark the
answer conditional on it.
