from sla import calculate_due_at


sample_ticket = {
    "id": "TICKET-1001",
    "priority": "high",
    "created_at": "2026-10-02T15:00:00-07:00",
}

print(f"Ticket {sample_ticket['id']} is due at {calculate_due_at(sample_ticket)}")
