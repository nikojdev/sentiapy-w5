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

    def to_dict(self):
        """[summary]. """
        return {
            "user_id": self.get_user_id(),
            "name": self.get_name()
        }
