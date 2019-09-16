"""Assignment week 5 - Ticketing system flask app."""

from flask import Flask, jsonify, request
from controllers.ticket_controller import TicketController
from controllers.user_controller import UserController

app = Flask(__name__)  # pylint: disable=invalid-name

@app.route("/")
def home():
    """Return HW on the  root  path."""
    return "Welcome to the pool."

@app.route("/ticket")
def get_ticket_list():
    """Get a list of all tickets."""
    tickets_array = TicketController.get_tickets()
    return jsonify(tickets_array)

@app.route("/ticket", methods=["POST"])
def create_ticket():
    """Create a new ticket and add it to the ticket pool."""
    data = request.get_json()
    ticket = TicketController.create_ticket(data)
    return jsonify(ticket.ticket_to_dict())

@app.route("/ticket/<int:ticket_id>")
def get_single_ticket(ticket_id):
    """Return a single ticket based on its ID."""
    ticket = TicketController.get_ticket_by_id(ticket_id)
    return jsonify(ticket.ticket_to_dict())

@app.route("/ticket/<int:ticket_id>", methods=["UPDATE"])
def update_ticket(ticket_id):
    """Update a specific ticket."""


@app.route("/ticket/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    """Delete a specific ticket."""

@app.route("/user")
def get_user_list():
    """this method gets the list of all users
    """
    users_array = UserController.get_users()
    return jsonify(users_array)

@app.route("/user", methods=["POST"])
def create_user():
    """this method creates a new user
    """

@app.route("/ticket/<int:user_id>")
def get_single_user(user_id):
    """this method gets the specific user
    """

@app.route("/user/<int:user_id>", methods=["UPDATE"])
def update_user(user_id):
    """this method updates the specific user
    """

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """this method deltes the specific user
    """

def success_response_body(data):
    """Return a successful message."""
    return {
        "result": True,
        "data": data

    }
