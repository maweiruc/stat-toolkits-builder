# {{TOPIC}} triage

Use this file to choose the workflow mode before solving.

## Standard / Known mode

Use when the problem matches a standard theorem, formula, result class, or
registry entry after full specification matching.

Required behavior:

- state the matched result;
- check all applicability conditions;
- validate the result under the requested target, loss, model, and regime;
- report caveats.

## Hard mode

Use when a familiar result may be unsafe.

Triggers:

- ambiguous target or loss;
- hidden assumptions;
- boundary, nonregular, high-dimensional, restricted, dependent, causal, or
  inverse structure;
- regime changes;
- denominator, support, positivity, or identifiability issues.

Required behavior:

- build an assumption or component ledger;
- state why lookup is unsafe;
- perform the checks in `hard_problem_protocol.md`.

## Research mode

Use when no exact known result is available, or the problem is a new variant.

Required behavior:

- build a first-principles derivation or proof record;
- clearly label candidate, partial, or unresolved status;
- include an obstruction ledger when incomplete.
