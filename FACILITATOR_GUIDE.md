# 20-Minute Facilitator Guide

## Setup

1. Create a new GitHub repository.
2. Copy these starter files into the repository.
3. Commit the starter state.
4. Open the repository in an environment with GitHub Copilot Agent Mode.

## Timing

| Time | Activity |
| --- | --- |
| 0-3 min | Explain the scenario and inspect the file tree. |
| 3-7 min | Ask Agent Mode for a plan only. |
| 7-10 min | Review the task definition and acceptance criteria. |
| 10-16 min | Approve one bounded implementation change. |
| 16-20 min | Run tests, inspect the diff, and decide whether to accept. |

## Demo script

### 1. Baseline

Run:

```powershell
python -m unittest discover -s test
```

Expected result: at least one test fails. Explain that the failure is the lab scenario, not a setup issue.

### 2. Planning-only prompt

Paste the suggested prompt from `AGENT_TASK.md`.

Important: stop the agent after the plan if it tries to edit immediately.

### 3. Review the plan

Check whether the plan:

- Mentions only `src/sla.py` as editable.
- Keeps tests unchanged.
- Describes business-hour rollover.
- Includes validation with `python -m unittest discover -s test`.

### 4. Approve implementation

Example approval:

```text
Approved. Implement only the business-hour calculation in src/sla.py, then run python -m unittest discover -s test.
```

### 5. Validate

Run:

```powershell
python -m unittest discover -s test
git diff
```

Accept the result only if tests pass and the diff is limited to `src/sla.py`.

## Debrief prompts

- What made the task bounded?
- Which acceptance criteria protected against an incomplete fix?
- What would you add before allowing a larger change?
