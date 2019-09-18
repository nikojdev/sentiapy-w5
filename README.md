# sentiapy-w5

Python week 5 assignment

## Run

```CLI
Debug mode: FLASK_ENV=development FLASK_APP=main.py flask run
```

## Endpoints

* `GET /ticket/` list all tickets with details
* `GET /ticket/:id` Get the specific ticket details
* `PUT /ticket/:id` Update the ticket details
* `POST /ticket/` Create new ticket

* `GET /user/` list all users
* `GET /user/:id` Get the specific user details
* `PUT /user/:id` Update the user details
* `POST /user/` Create new user

## Json examples

#### Create Ticket `POST /ticket/`

```json
{
    "name": "ticket-sentia",
    "status": "open"
}
```

#### Create User `POST /user/`

```json
{
    "name": "Jean-Luc Picard"
}
```

#### Update ticket `PUT /ticket/:id`

```json
{
    "status": "close",
    "ticket_assignee": 3
}
```
