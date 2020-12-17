from user import User
from privileges import Privileges

""" Adding an admin user type to our class """
class Admin(User):
    """A simple model to represent admin user."""
    
    def __init__(self,first_name,last_name,usr_name,email,location):
        """Initialize the user profile details"""
        super().__init__(first_name,last_name,usr_name,email,location)
        self.privileges = Privileges()