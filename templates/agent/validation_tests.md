# {{TOPIC}} validation tests

Use this file to validate answers before final reporting.

## Generic checks

- Does the normalized problem match the user request?
- Are all required inputs stated?
- Are assumptions explicit?
- Does the mode match the difficulty?
- Does the result address the stated target?
- Are danger zones checked?
- Is the final status honest?

## Special-case checks

Add topic-specific checks:

```text
1. [special case]
2. [limiting case]
3. [known benchmark]
```

## Registry checks

If using `examples/registry.yaml`, verify:

- same model or mathematical setting;
- same target;
- same assumptions;
- same loss, metric, or validity criterion;
- same regime;
- warnings addressed.
