# printing 3D models  
def print_models(unprinted_designs):
    """
    simulate each design until none are left. 
    move each design to completed models list.
    
    """
    printed_models = []

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        printed_models.append(current_design)
    
    return printed_models