# Interview questions for a new stat-toolkits-* toolkit

Use these questions before scaffolding a new toolkit. The goal is to produce a
decision-complete `TOOLKIT_SPEC.md`, not to finish all theory content.

## 1. Identity

1. What is the topic slug for `tools/stat-toolkits-<topic>/`?
2. What statistical object, result type, or research task does this toolkit
   support?
3. What is the one-line promise of the toolkit?

## 2. Core workflow

1. What is the default workflow in five to seven steps?
2. What does the agent normalize first?
3. What does the agent triage?
4. What is the main mathematical operation: proof, derivation, theorem
   matching, validation, computation, or audit?
5. What does a successful final answer look like?

## 3. Inputs

1. What must the user provide?
2. What can the agent infer?
3. What missing information should be handled by provisional assumptions?
4. What missing information should stop the task?

## 4. Modes

1. What is the simplest standard mode?
2. What makes a problem hard or unsafe for lookup?
3. What counts as a research or first-principles problem?
4. What status labels should unresolved answers use?

## 5. Artifacts

1. What belongs in `problem.tex`?
2. What belongs in `notes.md`?
3. What belongs in `solution.md`?
4. Should `solution.tex` and `solution.pdf` be optional exports only?
5. What information must survive if a later agent resumes the task?

## 6. Registry

1. Does this topic have reusable known results worth listing in YAML?
2. What fields must every registry entry contain?
3. What fields should strict validation require?
4. What warnings prevent misuse of registry entries?
5. Should the registry be included in v0.1 or postponed?

## 7. Danger zones

1. What familiar formula or theorem is most often misapplied?
2. What assumptions are usually hidden?
3. What changes the answer without looking obvious?
4. What should the agent refuse to overclaim?

## 8. Trial tasks

1. What is the standard easy trial?
2. What is the hard or ambiguous trial?
3. What is the research-style trial, if applicable?
4. What red flags should reviewers look for in trial output?

## 9. Scope control

1. What must v0.1 include?
2. What can wait until v0.2?
3. What should never be generated automatically without review?
