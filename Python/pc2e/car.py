#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""A set of classes that represents gasoline and electric cars."""

class Car:
    """A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe the car"""
        self.make = make
        self.model = model 
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """ Return a neatly formmated descriptive name"""
        long_name = f"{self.year} {self.make} {self.model} "
        return long_name.title()
    
    def read_odometer(self):
        """Print the statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll back the value
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self,mileage):
        """
        Increment the odometer value. 
        """
        self.odometer_reading += mileage

