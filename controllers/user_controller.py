"""user controller module
"""

from models.user import User

class UserController:
    """User controller class
    """

    _users = []

    @classmethod
    def get_users(cls):
        """[summary]
            [type] -- [description]
        """
        return cls._users

    @classmethod
    def get_users_by_id(cls, user_id):
        """[summary]
        """
        user_by_id = None

        print(user_id)

        #find user
        for user in cls._users:
            if int(user.get_user_id()) == int(user_id):
                user_by_id = user
        return user_by_id


    @classmethod
    def create_user(cls, data):
        """[summary]
        """
        highest_user_id = cls.get_highest_user_id()
        new_user = User(
            user_id=highest_user_id + 1,
            name=data["name"]
        )
        cls._users.append(new_user)
        return new_user

    @classmethod
    def get_highest_user_id(cls):
        """[summary]
        """
        return len(cls._users)

    @classmethod
    def update_user(cls, user, data):
        """update user datails
        """
        #update user
        if data["name"]:
            user.set_name(data["name"])
