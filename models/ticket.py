"""The ticket module containing definition of a ticket."""
class Ticket:
    """The ticket class."""

    def __init__(self, name, ticket_id, status, ticket_assignee=None):
        """Construct a new person."""
        self._name = name
        self._ticket_open = True
        self._ticket_id = ticket_id
        self._status = status
        self._ticket_assignee = ticket_assignee

    def close_ticket(self):
        """Close a ticket."""
        self._ticket_open = False

    def open_ticket(self):
        """Return an open ticket."""
        self._ticket_open = True

    def ticket_to_dict(self):
        """Return a dict of the ticket."""
        return {
            "name": self.get_ticket_name(),
            "ticket_id": self.get_ticket_id(),
            "status": self.get_ticket_status(),
            "ticket_assignee": self.get_ticket_assignee()
        }

    def assign_person(self, person):
        """Assign a person to a ticket."""
        self._ticket_assignee = person

    def get_ticket_status(self):
        """Return the ticket status."""
        return self._ticket_open

    def get_ticket_id(self):
        """Return the ID of a ticket.

        Returns:
            Int -- ticket id

        """
        return self._ticket_id

    def get_ticket_assignee(self):
        """Return the person assigned to a ticket.

        Returns:
            Person -- assignee

        """
        return self._ticket_assignee

    def get_ticket_name(self):
        """Return the ticket name.

        Returns:
            String -- name of a ticket

        """
        return self._name
