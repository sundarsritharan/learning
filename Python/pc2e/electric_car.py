from car import Car

#Simple version of electric car class 
class ElectricCar(Car):
    """Represents simple version of electric car"""
    
    def __init__(self,make,model,year):
        """Inherit and initialize attributes of car"""
        super().__init__(make,model,year)
        self.battery = Battery()

class Battery:
    """ A simple attempt to model battery class for electric cars"""
    
    def __init__(self,battery_size=75):
        """Initialize batter attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """ Print a statement describing battery size"""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """ Print the range of the battery based on it's size"""
       
        if self.battery_size == 75:
             mileage_range = 260
        elif self.battery_size == 100:
            mileage_range = 315
    
        print(f"This car can go about {mileage_range} miles on a full charge.") 
        
    def upgrade_battery(self):
        """Upgrade battery if it's not 100 kwh"""
        
        if self.battery_size == 75:
            self.battery_size = 100