# Agent Mode Task

## Goal

Fix the SLA due-date calculation so all tests pass and the calculator only counts business hours.

For this lab, all sample timestamps are in Pacific Daylight Time (`-07:00`) and test assertions compare ISO/UTC output. Business hours are Monday-Friday, 9:00 AM through 5:00 PM Pacific Daylight Time, equivalent to 16:00 through 00:00 UTC for these sample dates.

## Required first step

Inspect the repository and produce a short plan. Do not edit files yet.

## Permitted files

You may edit only:

- `src/sla.py`

You may read any repository file.

## Allowed tools

- File read/search tools
- Code editing tools
- `python -m unittest discover -s test`

Do not install packages. Do not edit tests unless explicitly asked.

## Constraints

- Keep the public API unchanged.
- Do not introduce external dependencies.
- Preserve existing priority values and SLA durations.
- Keep the implementation deterministic across developer machines; do not depend on the machine's local timezone.
- Use clear, simple Python.
- Implement one bounded change only: business-hour addition.

## Acceptance criteria

- `python -m unittest discover -s test` passes.
- `calculate_due_at(ticket)` returns an ISO timestamp.
- High-priority tickets created Friday at 3:00 PM are due Monday at 11:00 AM.
- Normal-priority tickets created Monday at 4:00 PM are due Tuesday at 4:00 PM.
- Tickets created on Saturday start counting Monday at 9:00 AM.

## Suggested Agent Mode prompt

You are working in this repository. First, inspect the code and tests and produce a plan only. Do not edit files yet.

Task:
Fix the SLA due-date calculation so it counts only business hours: Monday-Friday, 9:00 AM through 5:00 PM Pacific Daylight Time for the supplied sample dates. The tests compare ISO/UTC output, so keep the implementation deterministic across developer machines.

Permitted files:
- You may edit only `src/sla.py`.

Allowed tools:
- Read/search files.
- Edit code.
- Run `python -m unittest discover -s test`.

Constraints:
- Do not install dependencies.
- Do not edit tests.
- Keep the exported API unchanged.
- Make one bounded implementation pass.
- Do not depend on the machine's local timezone.

Acceptance criteria:
- `python -m unittest discover -s test` passes.
- Friday 3:00 PM plus 4 business hours returns Monday 11:00 AM.
- Monday 4:00 PM plus 8 business hours returns Tuesday 4:00 PM.
- Saturday tickets begin counting Monday at 9:00 AM.
