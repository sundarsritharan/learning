""" Defines URL patterns for pizza app """ 
from django.urls import path 
from . import views 

app_name = 'pizzas'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    #Page that shows all Pizzas. 
    path('pizzas/', views.pizzas, name='pizzas'),

    #Toppings page for a selected pizza.
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]