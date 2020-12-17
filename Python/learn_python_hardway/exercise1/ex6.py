# set a variable 
types_of_people = 10
# create a sentence and assign the variable with f'string formatting 
x = f"There are {types_of_people} types of people."

# set a variable 
binary = "binary"
# set a variable and make sure to use double qoutes 
do_not =  "don't"
# create a sentence and assign the variable with f'string formatting 
y = f"Those who know {binary} and those who {do_not}."

#print the sentences 
print(x)
print(y)

#print the sentences with f'string formatting 
print(f"I said: {x}")
print(f"I also said: {y}")

#set boolen variable
hillarious = False

#use empty {} to fill in the value after evaluation.
joke_evalution = "Isn't that joke so funny?! {}"
print(joke_evalution.format(not(hillarious)))

w = "This is the left side of ... "
e  = "a string with a right side."
print(w+e)

print(f"{w} {e}")