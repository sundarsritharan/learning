""" class representing users in a system"""
class User:
    
    """A simple model to represent a user profile"""
    
    def __init__(self,first_name,last_name,usr_name,email,location):
        """Initialize the user profile details"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.usr_name = usr_name
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """Display the user information."""
        full_name = f"{self.first_name} {self.last_name}."
        print(f"\n{full_name.title()}")
        print(f"{self.usr_name}")
        print(f"{self.email}")
        print(f"{self.location}")
        
    def greet_user(self):
        """display a personalized message for the user."""
        msg = f"Welcome back, {self.usr_name}"
        print(f"{msg}")
        
    def increment_login_attempts(self):
        """increment login attempts for the user account."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """reset login attempts for the user account."""
        self.login_attempts = 0
