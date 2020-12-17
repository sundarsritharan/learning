
"""
    A model to represent restaurant 
"""

class Restaurant:
    
    """A simple model to represent resturant."""
    
    def __init__(self,restaruant_name,cuisine_type):
        """ Initialize the name and cuisine attributes """
        self.name = restaruant_name.title()
        self.cuisine = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """ Describe the restaurant """
        msg = f"{self.name} restaurant servers delicious {self.cuisine}. "
        print(f"\n{msg}")
        
    def open_restaurant(self):
        """Show if the restaurant is open or not"""
        print(f"{self.name} restaurant is open now.")
        
        
    def set_number_served(self,number_served):
        """Set the number of guests servered"""
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("You can't roll on number of guests served!")
    
    def increment_number_served(self,number_served):
        """Increment the number of guests servered"""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    
    """A simple model to represent Ice Cream Stand."""
    
    def __init__(self,name,cuisine_type = 'Ice Creams'):
        """ Initialize the name and cuisine attributes """
        super().__init__(name,cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        """Print all the flavors of icecreams available in this stand"""
        
        print("\nWe have the following ice cream flavors available.")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")