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

        return tickets_by_id[0] if tickets_by_id else None

    @classmethod
    def get_tickets_assigned_to_user(cls, user_id):
        """Get the tickets by assignee"""
        tickets = list(
            filter(lambda d: False if d.get_ticket_assignee() == None else d.get_ticket_assignee().get_user_id() == user_id, cls._tickets)
        )
        return tickets

    @classmethod
    def unassign_tickets_by_user_id(cls, user_id):
        """unassign all tickets from user"""
        tickets = cls.get_tickets_assigned_to_user(user_id)
        for ticket in tickets:
            ticket.unassign()

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
    def delete_ticket(cls, ticket_id):
        """Delete a ticket."""
        new_tickets = list(filter(lambda d: d.get_ticket_id() != ticket_id, cls._tickets))
        cls._tickets = new_tickets

    @classmethod
    def update_ticket(cls, ticket, data, user=None):
        """Update a ticket."""

        #update according to the data provided
        if "name" in data:
            ticket.set_ticket_name(data["name"])
        if "status" in data:
            ticket.set_ticket_status(data["status"])
        if user:
            ticket.assign_person(user)

    @classmethod
    def _get_highest_ticket_id(cls):
        """Return the highest ticket id."""
        if not cls._tickets:
            return 0
        else:
            return max([u.get_ticket_id() for u in cls._tickets])
