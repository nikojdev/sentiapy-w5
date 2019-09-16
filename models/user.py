""" User module
"""
class User:
    """User class
    """
    def __init__(self, name, user_id):
        """comntruct
        """
        self._user_id = user_id
        self._name = name


    def get_user_id(self):
        """this method returns the user id
        """
        return self._user_id

    def get_name(self):
        """this method returns name
        """
        return self._name

    def set_name(self, name):
        """[summary]
        """
        self._name = name
