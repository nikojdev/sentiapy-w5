"""Ticket controller module."""

from models.ticket import Ticket
class TicketController:
    """TicketController class."""

    tickets = []

    @classmethod
    def get_tickets(cls):
        """Return the list of tickets."""
        return cls.tickets

    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        """Get the ticket by ID."""
        tickets_by_id = list(
            filter(lambda d: d['id'] == ticket_id, cls.tickets)
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
        data = new_ticket.ticket_to_dict()
        cls.tickets.append(new_ticket)
        return new_ticket

    @classmethod
    def assign_ticket(cls, data):
        """this method assigns the ticket 
        """

    @classmethod
    def delete_ticket(cls, tick_id):
        """this ticket deletes the ticket
        """

    @classmethod
    def update_ticket(cls, data):
        """this method udpates the ticket
        """

    @classmethod
    def _get_highest_ticket_id(cls):
        """Return the highest ticket id."""
        if not cls.tickets:
            return 0
        else:
            return max([u.get_ticket_id() for u in cls.tickets])
