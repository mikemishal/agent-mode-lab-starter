from datetime import datetime, timedelta, timezone


SLA_HOURS_BY_PRIORITY = {
    "high": 4,
    "normal": 8,
    "low": 16,
}


def calculate_due_at(ticket):
    if not ticket or "created_at" not in ticket:
        raise ValueError("ticket.created_at is required")

    priority = ticket.get("priority", "normal")
    sla_hours = SLA_HOURS_BY_PRIORITY.get(priority)
    if sla_hours is None:
        raise ValueError(f"Unsupported priority: {priority}")

    created_at = datetime.fromisoformat(ticket["created_at"])
    if created_at.tzinfo is None:
        raise ValueError("ticket.created_at must include a timezone offset")

    return add_business_hours(created_at, sla_hours).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def add_business_hours(start, hours):
    # BUG: This currently adds clock hours, not business hours.
    return start + timedelta(hours=hours)
