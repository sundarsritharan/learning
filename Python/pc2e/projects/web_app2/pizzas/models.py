from django.db import models

# Create your models here.
class Pizza(models.Model):
    """ A pizza the user likes to order """ 
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return a string representation of the model """ 
        return self.name

class Topping(models.Model):
    """ A model to represent all the toppings to be added to the pizza"""
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'
    
    def __str__(self):
        """ Return a string representation of the model """ 
        return self.name
