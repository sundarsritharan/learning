""" Adding a spearate class for an admin user privileges """
class Privileges():
    """A simple model representing admin user privileges"""
    
    def __init__(self,privileges=[]):
        """Initilize the set of privileges"""
        
        #Initialize an empty set of privileges.
        self.privileges = privileges
    
    def show_privileges(self):
        """Print the privileges for admin user."""
        
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"-{privilege.title()}")
        else:
            print(" - The user has no privileges.")