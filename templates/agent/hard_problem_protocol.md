# {{TOPIC}} hard-problem protocol

Use hard mode when standard lookup is unsafe.

## Required ledgers

Create the ledgers needed for this topic:

```text
Assumption | Where stated | Why needed | Checked? | Issue
Component | Role | Dependency | Validation check | Status
```

Customize the ledgers for the toolkit before release.

## Steps

1. Normalize all inputs and notation.
2. Identify the exact target and validity criterion.
3. List explicit and implicit assumptions.
4. Check danger zones from `danger_zone.md`.
5. Compare against known results only after matching all fields.
6. Validate the result using `validation_tests.md`.
7. State final answer as verified, conditional, partial, or unresolved.

## Output status

Use one of:

```text
verified under stated assumptions
conditionally verified
partial result
candidate result
unresolved after hard-mode checks
not identifiable / not regular / not applicable
```
