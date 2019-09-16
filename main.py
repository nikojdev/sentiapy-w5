""" Assignment week 5
    Ticketing system flask app
"""

from flask import Flask, jsonify, request
from controllers.ticket_controller import TicketController
from controllers.user_controller import UserController

app = Flask(__name__)  # pylint: disable=invalid-name

@app.route("/ticket")
def get_ticket_list():
    """this methods gets the list of all tickets
    """
    tickets_array = TicketController.get_tickets()
    return jsonify(tickets_array)

@app.route("/ticket", methods=["POST"])
def create_ticket():
    """this methods creates the new ticket
    """

@app.route("/ticket/<int:ticket_id>")
def get_single_ticket(ticket_id):
    """this method returns the single ticket
    """

@app.route("/ticket/<int:ticket_id>", methods=["UPDATE"])
def update_ticket(ticket_id):
    """this method updates the specific ticket
    """

@app.route("/ticket/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    """this method deletes the specific ticket
    """

@app.route("/user")
def get_user_list():
    """this method gets the list of all users
    """
    users_array = UserController.get_users()
    return jsonify(users_array)

@app.route("/user", methods=["POST"])
def create_user():
    """this method creates a new user."""
    data = request.get_json()
    user = UserController.create_user(data)
    return jsonify(user.to_dict())

@app.route("/user/<int:user_id>")
def get_single_user(user_id):
    """this method gets the specific user."""
    user = UserController.get_users_by_id(user_id)
    return jsonify(user.to_dict())

@app.route("/user/<int:user_id>", methods=["UPDATE"])
def update_user(user_id):
    """this method updates the specific user
    """

@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """this method deltes the specific user."""
    UserController.delete_user(user_id)
    return jsonify({})

def success_response_body(data):
    """success body response
    """

    return {
        "result": True,
        "data": data

    }
