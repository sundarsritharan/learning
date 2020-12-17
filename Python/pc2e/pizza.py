def make_pizza(size,*toppings):
    """
    Summarizing the pizza we are about to make 
    
    """
    print(f"\nMaking a {size}-inches pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")