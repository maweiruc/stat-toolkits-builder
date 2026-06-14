# Reference spec: stat-toolkits-minimax

This spec is distilled from `tools/stat-toolkits-minimax/`. It is a reference
example for a proof/rate toolkit.

## 1. Identity

Toolkit name:

```text
stat-toolkits-minimax
```

One-line description:

```text
A documentation-first toolkit for finding, checking, and deriving minimax rates
in statistical theory.
```

Primary statistical object or task:

```text
Minimax rates, upper bounds, lower bounds, theorem matching, and exactness
labels.
```

## 2. Core workflow

```text
normalize problem -> triage -> candidate rate -> upper/lower proof ledgers ->
theorem comparison -> final rate, exactness, caveats
```

## 3. Required input fields

```text
1. Observation model
2. Parameter space
3. Target
4. Loss or risk scale
5. Asptotic regime and growing dimensions
6. Desired output: known rate, proof, comparison, or research derivation
```

## 4. Required output fields

```text
1. Normalized minimax risk
2. Triage label
3. Candidate rate
4. Upper-bound ledger
5. Lower-bound ledger
6. Registry or theorem comparison
7. Exactness status
8. Caveats and proof gaps
```

## 5. Modes

| Mode | When to use | Required checks |
| --- | --- | --- |
| Known | A standard theorem or registry entry matches | Full model/loss/class/regime matching |
| Hard | Familiar rates may not apply | Assumption and regime ledgers |
| Research-Discovery | No exact theorem matches | First-principles upper/lower route |

## 6. Durable artifacts

Problem folders use:

```text
problem.tex
notes.md
solution.md
solution.tex
solution.pdf
```

`notes.md` preserves compact proof state. `solution.md` contains the detailed
final proof or strongest derivation attempt.

## 7. Registry

Registry type:

```text
minimax_rate_registry.yaml
```

Core fields:

```text
model
parameter_class
target
loss
risk_rate / error_rate / separation_rate / regret_rate
upper_bound
lower_bound
exactness
warnings
```

Strict entries add tags, risk scale, source status, theorem anchor,
applicability checks, references, and upper/lower proof blueprints.

## 8. Danger zones

- Risk rate vs error rate.
- Estimation vs testing.
- Wrong loss or norm.
- Fixed vs growing dimension.
- Missing design, sparsity, eigenvalue, or margin assumptions.
- Upper and lower bounds proved under different conditions.
- Up-to-log results reported as exact.

## 9. Trial tasks

| Trial | Purpose | Expected behavior |
| --- | --- | --- |
| Normal mean | Standard known rate | `sigma^2/n`, sample mean, two-point or Cramer-Rao lower bound |
| Holder regression | Nonparametric proof route | bias-variance upper bound and Fano/Assouad lower bound |
| Sparse regression | Hard assumptions | design conditions and parameter/prediction loss distinction |
| Weighted functional | Research-discovery | candidate rate, proof gaps, upper/lower plan |

## 10. v0.1 lesson for the factory

A strong v0.1 rate toolkit needs upper and lower ledgers from the start. The
registry can be small, but it must include warnings and proof blueprints.
