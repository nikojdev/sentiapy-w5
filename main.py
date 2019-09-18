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


@app.route("/ticket/<int:ticket_id>", methods=["PUT"])
def update_ticket(ticket_id):
    """Update a specific ticket."""
    ticket_data = request.get_json()
    user_by_id = None
    response = None

    # get ticket by id
    ticket_by_id = TicketController.get_ticket_by_id(ticket_id)

    # check if there is assignee key provided in request
    if "ticket_assignee" in ticket_data:
        user_by_id = UserController.get_users_by_id(ticket_data["ticket_assignee"])
        if user_by_id is None:
            return (
                error_response(404, "Resource Not Found")
            )  # return not found response if wrong user provided

    # check if ticket was found and update accordingly
    if ticket_by_id:
        TicketController.update_ticket(ticket_by_id, ticket_data, user_by_id)
        response = success_response_body(ticket_data)
    else:
        # return no user error
        response = error_response(404, "Resource Not Found")
    return response


@app.route("/ticket/<int:ticket_id>", methods=["DELETE"])
def delete_ticket(ticket_id):
    """Delete a specific ticket."""
    if TicketController.get_ticket_by_id(ticket_id):
        TicketController.delete_ticket(ticket_id)
        response = success_response_body({})
    else:
        response = error_response(404, "Resource Not Found")
    return response


@app.route("/user")
def get_user_list():
    """Return a list of all users."""
    users_array = UserController.get_users()
    return jsonify(users_array)


@app.route("/user", methods=["POST"])
def create_user():
    """Create a user."""
    data = request.get_json()
    user = UserController.create_user(data)
    return jsonify(user.to_dict())


@app.route("/user/<int:user_id>")
def get_single_user(user_id):
    """Return a specific user based on ID."""
    user = UserController.get_users_by_id(user_id)
    return jsonify(user.to_dict())


@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update a user."""
    user_data = request.get_json()
    response = None

    # get user by id
    user_by_id = UserController.get_users_by_id(user_id)

    if user_by_id:
        UserController.update_user(user_by_id, user_data)
        response = success_response_body(user_data)
    else:
        # return no user error
        response = error_response(404, "Resource Not Found")

    return response


@app.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a specific user based on ID."""
    TicketController.unassign_tickets_by_user_id(user_id)
    UserController.delete_user(user_id)
    return jsonify({})


def success_response_body(data):
    """Return a successful message."""
    return {"result": True, "data": data}


def error_response(status_code, error, message=None):
    """Return an error message."""
    body_dict = {"code": status_code, "error": error, "result": False}
    if message:
        body_dict["message"] = message

    return jsonify(body_dict), status_code

@app.errorhandler(Exception)
def page_not_found(error):
    """page not found error"""
    return error_response(error.code, error.description)
