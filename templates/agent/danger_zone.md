# {{TOPIC}} danger zones

This file lists common ways an agent can misuse familiar results for
{{PRIMARY_OBJECT}}.

Replace the generic items below with topic-specific warnings.

## Common risks

- Confusing similar targets.
- Ignoring assumptions hidden in a theorem statement.
- Applying a result under the wrong model or regime.
- Changing the loss, metric, or validity criterion.
- Treating a heuristic as a proof.
- Treating a registry entry as a source of truth.
- Omitting boundary, support, positivity, or identifiability checks.
- Reporting a final result when only a candidate is justified.

## Required behavior

Before using a familiar result, the agent must state:

```text
What result is being used:
What fields match:
What fields are uncertain:
What warnings apply:
Whether the final answer is verified, conditional, or partial:
```
