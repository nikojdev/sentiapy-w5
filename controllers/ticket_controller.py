"""ticket controller module
"""

from models.ticket import Ticket
class TicketController:
    """TicketController class
    """
    
    _tickets = []

    @classmethod
    def get_tickets(cls):
        """this method returns the list of tickets
        """
        return cls._tickets
    
    @classmethod
    def get_ticket_by_id(cls, ticket_id):
        """this method gets ticket by id
        """
        tickets_by_id = list(
            filter(lambda d: d['id'] == ticket_id, cls._tickets)
        )

        return tickets_by_id[0]
    
    @classmethod
    def create_ticket(cls, data):
        """this method creates the ticket
        """
        highest_ticket_id = cls._get_highest_ticket_id()
        new_ticket = Ticket(
            ticket_id = highest_ticket_id + 1,
            name=data["name"]
        )
        cls._tickets.append(new_ticket)
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
        """this methiod returns the highest ticket id
        """
        return max([u.get_ticket_id() for u in cls._tickets])
    
    
    
