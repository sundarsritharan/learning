name = 'Sundar Sritharan'
age = 43 # it's true 
height = 74 # inches 
weight = 186 # lbs 
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right 
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

#convert inch and weight to centimeter and kilograms 
heigh_cms = height * 2.24 
weight_kilos = weight * 0.453592
print(f"He's {heigh_cms: .2f} cms tall.")
print(f"He's {weight_kilos: .2f} pounds heavy.")
