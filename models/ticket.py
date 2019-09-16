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
        """this method closes the ticket
        """
        self._ticket_open = False

    def open_ticket(self):
        """this method makes ticket open
        """
        self._ticket_open = True

    def ticket_to_dict(self):
        """Return a dict of the ticket."""
        ticket_dict = {
            "name": self._name,
            "ticket_id": self._ticket_id,
            "status": self._status,
            "ticket_assignee": self._ticket_assignee
        }

        return ticket_dict

    def assign_person(self, person):
        """this method assigns a person to a ticket and stores the reference to it
        """
        self._ticket_assigne = person

    def get_ticket_status(self):
        """this method returns the status of a ticket
        Returns:
            Bool -- ticket open status
        """
        return self._ticket_open

    def get_ticket_id(self):
        """this method returns the id of a ticket

        Returns:
            Int -- ticket id
        """
        return self._ticket_id

    def get_ticket_assigne(self):
        """this method returns the Person assigned to a ticket
        Returns:
            Person -- assigne
        """
        return self._ticket_assigne

    def get_ticket_name(self):
        """this method returns the name of the ticket
        Returns:
            String -- name of a ticket
        """
        return self._name
