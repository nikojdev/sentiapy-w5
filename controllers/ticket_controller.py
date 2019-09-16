"""Ticket controller module."""

from models.ticket import Ticket

class TicketController:
    """TicketController class."""

    _tickets = []

    @classmethod
    def get_tickets(cls):
        """Return the list of tickets."""
        return list(map(lambda d: d.ticket_to_dict(), cls._tickets))

    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        """Get the ticket by ID."""
        tickets_by_id = list(
            filter(lambda d: d.get_ticket_id() == ticket_id, cls._tickets)
        )

        return tickets_by_id[0]

    @classmethod
    def create_ticket(cls, data):
        """Create a new ticket."""
        highest_ticket_id = cls._get_highest_ticket_id() + 1
        new_ticket = Ticket(
            ticket_id=highest_ticket_id,
            name=data["name"],
            status=data["status"]
        )
        cls._tickets.append(new_ticket)
        return new_ticket

    @classmethod
    def assign_ticket(cls, data):
        """Assign a ticket."""

    @classmethod
    def delete_ticket(cls, tick_id):
        """Delete a ticket."""

    @classmethod
    def update_ticket(cls, data):
        """Update a ticket."""

    @classmethod
    def _get_highest_ticket_id(cls):
        """Return the highest ticket id."""
        if not cls._tickets:
            return 0
        else:
            return max([u.get_ticket_id() for u in cls._tickets])
