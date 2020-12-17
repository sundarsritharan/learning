# city function 

def get_city_name(city,country,population=""):

    if population:
        full_city_name = f"{city.title()}, {country.title()}"
        full_city_name += f" - population {population}"
    else: 
        full_city_name = f"{city.title()}, {country.title()}"
    return full_city_name