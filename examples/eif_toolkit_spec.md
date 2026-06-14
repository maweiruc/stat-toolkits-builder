# Reference spec: stat-toolkits-eif

This spec is distilled from the external `stat-toolkits-eif` reference
repository. It is a self-contained reference example for a derivation/validation
toolkit.

## 1. Identity

Toolkit name:

```text
stat-toolkits-eif
```

One-line description:

```text
A documentation-first toolkit for deriving, checking, and validating influence
functions and efficient influence functions in semiparametric statistics.
```

Primary statistical object or task:

```text
Influence functions, efficient influence functions, pathwise derivatives,
tangent-space projection, validation, and optional implementation guidance.
```

## 2. Core workflow

```text
normalize problem -> triage target -> check identification/regularity ->
derive pathwise derivative -> find IF/EIF -> verify -> implement if needed
```

## 3. Required input fields

```text
1. Observed data unit
2. Target parameter
3. Statistical model
4. Identification assumptions
5. Nuisance functions, if known
6. Desired output: IF/EIF, derivation, validation, or implementation
```

## 4. Required output fields

```text
1. Observed-data structure
2. Target parameter
3. Identification formula
4. Regularity/pathwise differentiability status
5. Nuisance functions
6. Likelihood factorization and score decomposition
7. Candidate IF, valid IF, EIF, or nonregular status
8. Mean-zero and derivative identity checks
9. Warnings and unresolved projection issues
```

## 5. Modes

| Mode | When to use | Required checks |
| --- | --- | --- |
| Fast | Exact standard problem after matching | Identification, nuisance, positivity, validation |
| Hard | Formula lookup is unsafe | Component ledger and support/regularity checks |
| Research | No exact formula is available | First-principles derivative/projection record |

## 6. Durable artifacts

Problem folders use:

```text
problem.tex
notes.md
solution.md
solution.tex
solution.pdf
```

`notes.md` is an intake brief and derivation checkpoint. `solution.md` is the
detailed derivation record.

## 7. Registry

Registry type:

```text
eif_formula_registry.yaml
```

Core fields:

```text
observed_data
target
assumptions
nuisances
eif or status
estimator or recommendation
warnings
```

The registry is only a formula-matching aid. It is not a substitute for
checking observed data, target, assumptions, nuisances, positivity, and
regularity.

## 8. Danger zones

- Copying an ATE formula for an ATT or restricted model.
- Calling a full-model IF efficient under a restricted model.
- Ignoring positivity or denominator conditions.
- Giving EIFs for nonregular targets.
- Skipping tangent-space projection.
- Skipping mean-zero and pathwise derivative checks.
- Stopping at a candidate IF when verification or projection is still visible.

## 9. Trial tasks

| Trial | Purpose | Expected behavior |
| --- | --- | --- |
| Restricted moment model | Projection and efficient score | Distinguish raw score from efficient score |
| Partially linear single index | Nuisance tangent space | Projection/normal equations or obstruction |
| User LaTeX problem | Inbox workflow | Generate notes, write solution, status label |

## 10. v0.1 lesson for the factory

A strong v0.1 derivation toolkit needs status labels, validation checks, and
danger zones from the start. Formula lookup must be explicitly subordinated to
problem normalization and verification.
