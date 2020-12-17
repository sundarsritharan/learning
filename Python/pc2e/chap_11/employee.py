class Employee:
    """ simple model to blueprint an employee"""

    def __init__(self,fname,lname,salary):
        """ set employee name and salary"""
        self.first_name = fname
        self.last_name = lname
        self.salary = salary

    def give_raise(self,amount=5000):
        """ give $5000 raise as default or raise as per inout """
        self.salary +=  amount