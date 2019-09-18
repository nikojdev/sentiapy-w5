"""The UserController module."""
from models.user import User

class UserController:
    """The UserController class."""

    _users = []

    @classmethod
    def get_users(cls):
        """Return all users."""
        return list(map(lambda d: d.to_dict(), cls._users))

    @classmethod
    def get_users_by_id(cls, user_id):
        """Return a user based on ID."""
        users_by_id = list(
            filter(lambda d: d.get_user_id() == user_id, cls._users)
        )

        return users_by_id[0] if users_by_id else None

    @classmethod
    def create_user(cls, data):
        """Create a user."""
        highest_user_id = cls._get_highest_user_id()
        new_user = User(
            user_id=highest_user_id,
            name=data["name"]
        )
        cls._users.append(new_user)
        return new_user

    @classmethod
    def delete_user(cls, user_id):
        """Delete a user."""
        new_users = list(filter(lambda d: d.get_user_id() != user_id, cls._users))
        cls._users = new_users

    @classmethod
    def _get_highest_user_id(cls):
        """Return the highest ID available."""
        return max([u.get_user_id() for u in cls._users])+1 if cls._users else 1

    @classmethod
    def update_user(cls, user, data):
        """Update user details."""
        #update user
        if data["name"]:
            user.set_name(data["name"])
    