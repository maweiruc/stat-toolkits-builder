# v0.1 quality rubric

Use this rubric to grade a generated toolkit scaffold.

## Score 5: strong v0.1

- The output path is correct: `tools/stat-toolkits-<topic>/`.
- The toolkit has a clear identity and core workflow.
- `AGENTS.md` gives a concrete reading order and default behavior.
- The artifact contract is clear enough for a later agent to resume work.
- Trial prompts are runnable and have expected behavior.
- Danger zones are specific to the topic.
- The rubric prevents overclaiming.
- Registry and validation files exist if they are useful, or the spec explains
  why they are postponed.

## Score 4: usable v0.1

- All required files exist.
- The workflow is clear.
- Some topic-specific content is shallow but honest.
- Trial prompts exist.
- Minor TODOs remain, but they do not block first use.

## Score 3: weak scaffold

- The structure exists but reads like generic boilerplate.
- Modes, artifacts, or danger zones are under-specified.
- Trial prompts are vague.
- A later agent could use it, but would need substantial interpretation.

## Score 2: incomplete scaffold

- Required files or directories are missing.
- The agent workflow is not executable.
- Artifact roles are unclear.
- No meaningful trial guide exists.

## Score 1: not usable

- The output path is wrong.
- The scaffold is mostly empty or generic.
- It leaves major decisions to the implementer.
- It cannot guide a first task without reading the original chat.
