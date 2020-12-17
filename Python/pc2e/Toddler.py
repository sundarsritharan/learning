class Toddler:
    """ Modeling a toddler """

    def __init__(self,name,age):
        """ Initializing the toddler """
        self.name = name 
        self.age = age 
    
    def talk(self):
        """ make the toddler talk sentences """
        print(f"{self.name} is now taking.")
    
    def walk(self):
        """ make the toddler run."""
        print(f"{self.name} is now running")