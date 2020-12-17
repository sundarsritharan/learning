from django.shortcuts import render
from .models import Pizza,Topping

# Create your views here.
def index(request):
    """ The home page for Pizza app"""
    return render(request,'pizzas/index.html')

def pizzas(request):
    """ Show all available pizzas """
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas' : pizzas}
    return render(request,'pizzas/pizzas.html', context)

def pizza(request,pizza_id):
    """ Show the selected pizza and all it's toppings """
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-name')
    context = {'pizza':pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)