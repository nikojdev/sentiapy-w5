"""User module."""
class User:
    """User class."""

    def __init__(self, name, user_id):
        """Construct."""
        self._user_id = user_id
        self._name = name


    def get_user_id(self):
        """Return the user ID."""
        return self._user_id

    def get_name(self):
        """Return the name."""
        return self._name

    def set_name(self, name):
        """Set a name."""
        self._name = name

    def to_dict(self):
        """Return a dict of User."""
        return {
            "user_id": self.get_user_id(),
            "name": self.get_name()
        }
