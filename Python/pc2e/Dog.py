class Dog:
    """ A simple attempt to model a dog """

def __init__(self,name,age):
    """ Initialize the name and age attributes """
    self.name = name 
    self.age = age 

def sit(self):
    """ simualte a dog sitting in response to a command """
    print(f"{self.name} is now sitting.")

def roll_over(self):
    """ simulate a dog rolling over in response to a command """
    print(f"{self.name} is now rolling over.")

###########

my_dog = Dog("Willie",6)
    
print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
