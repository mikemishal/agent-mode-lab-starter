import unittest

from src.sla import calculate_due_at


class SlaTests(unittest.TestCase):
    def test_high_priority_adds_four_business_hours_across_weekend(self):
        due_at = calculate_due_at(
            {
                "priority": "high",
                "created_at": "2026-10-02T15:00:00-07:00",
            }
        )

        self.assertEqual(due_at, "2026-10-05T18:00:00Z")

    def test_normal_priority_rolls_after_hours_work_into_next_business_day(self):
        due_at = calculate_due_at(
            {
                "priority": "normal",
                "created_at": "2026-10-05T16:00:00-07:00",
            }
        )

        self.assertEqual(due_at, "2026-10-06T23:00:00Z")

    def test_low_priority_can_span_multiple_business_days(self):
        due_at = calculate_due_at(
            {
                "priority": "low",
                "created_at": "2026-10-05T10:00:00-07:00",
            }
        )

        self.assertEqual(due_at, "2026-10-07T18:00:00Z")

    def test_tickets_created_on_weekends_begin_counting_monday_morning(self):
        due_at = calculate_due_at(
            {
                "priority": "high",
                "created_at": "2026-10-03T12:00:00-07:00",
            }
        )

        self.assertEqual(due_at, "2026-10-05T20:00:00Z")

    def test_invalid_tickets_fail_loudly(self):
        with self.assertRaisesRegex(ValueError, "created_at is required"):
            calculate_due_at({"priority": "high"})

        with self.assertRaisesRegex(ValueError, "Unsupported priority"):
            calculate_due_at(
                {
                    "priority": "urgent",
                    "created_at": "2026-10-05T10:00:00-07:00",
                }
            )


if __name__ == "__main__":
    unittest.main()
