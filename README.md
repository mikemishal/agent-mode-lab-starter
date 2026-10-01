# Agent Mode Lab Starter

This small repository is designed for a 20-minute lab on using Agent Mode safely:

1. Ask the agent to inspect the repository and produce a plan only.
2. Define the task with goal, permitted files, tools, constraints, and acceptance criteria.
3. Approve the plan and let the agent implement one bounded change.
4. Validate the result before accepting it.

## Scenario

Contoso Support uses a tiny SLA calculator to estimate when a support ticket is due. The current implementation incorrectly counts non-business time when adding SLA hours.

For deterministic tests, the lab uses Pacific Daylight Time sample timestamps (`-07:00`) and compares results as ISO/UTC strings. Business hours are Monday-Friday, 9:00 AM through 5:00 PM Pacific Daylight Time, which is 16:00 through 00:00 UTC for these sample dates. Weekends are not business time.

## Quick start

```powershell
python -m unittest discover -s test
```

The tests should fail at first. That is intentional.

## Lab task

Use `AGENT_TASK.md` as the prompt for Agent Mode. Do not let the agent edit files during the first inspection step. After reviewing the proposed plan, approve exactly one bounded implementation pass.

## Expected behavior

The `calculate_due_at(ticket)` function should:

- Return an ISO string.
- Add 4 business hours for `priority: "high"`.
- Add 8 business hours for `priority: "normal"`.
- Add 16 business hours for `priority: "low"`.
- Count only Monday-Friday, 9:00 AM-5:00 PM Pacific Daylight Time for the supplied sample dates.
- Move work that would happen after hours or on weekends to the next business window.

## Project shape

```text
src/sla.py          # intentionally broken implementation
src/demo.py         # tiny runnable example
test/test_sla.py    # acceptance tests
```
