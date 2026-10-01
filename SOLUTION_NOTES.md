# Facilitator Solution Notes

Keep this file out of the learner prompt if you want the exercise to remain discovery-based.

The intended fix is to replace the naive clock-hour addition in `src/sla.py` with logic that:

1. Normalizes the starting time to the next business minute.
2. Counts available time until 5:00 PM Pacific Daylight Time for the sample dates.
3. Moves to the next weekday at 9:00 AM when the work day ends.
4. Skips Saturday and Sunday.
5. Uses UTC date operations or equivalent deterministic logic so results do not depend on the developer machine's local timezone.

The learner should accept the change only after `python -m unittest discover -s test` passes and the diff is limited to `src/sla.py`.
