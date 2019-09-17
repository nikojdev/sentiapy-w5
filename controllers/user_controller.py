"""module user_controller
"""
from models.user import User

class UserController:
    """class UserController"""
    _users = []

    @classmethod
    def get_users(cls):
        """[summary]
            [type] -- [description]
        """
        return list(map(lambda d: d.to_dict(), cls._users))

    @classmethod
    def get_users_by_id(cls, user_id):
        """[summary]."""
        users_by_id = list(
            filter(lambda d: d.get_user_id() == user_id, cls._users)
        )

        return users_by_id[0] if users_by_id else None

    @classmethod
    def create_user(cls, data):
        """[summary]
        """
        highest_user_id = cls._get_highest_user_id()
        new_user = User(
            user_id=highest_user_id,
            name=data["name"]
        )
        cls._users.append(new_user)
        return new_user

    @classmethod
    def delete_user(cls, user_id):
        """[summary]."""
        new_users = list(filter(lambda d: d.get_user_id() != user_id, cls._users))
        cls._users = new_users

    @classmethod
    def _get_highest_user_id(cls):
        """[summary]."""
        return max([u.get_user_id() for u in cls._users])+1 if cls._users else 1

    @classmethod
    def update_user(cls, user, data):
        """update user datails
        """
        #update user
        if data["name"]:
            user.set_name(data["name"])
    