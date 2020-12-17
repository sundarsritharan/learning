# variable that will be used with format function with 4 placeholders
formatter = '{} {} {} {}'



#pass numbers to the format function for printing 
print(formatter.format(1,2,3,4))

#pass strings to the format function for printing 
print(formatter.format('one','two','three','four'))

#pass boolen to the format function for printing 
print(formatter.format(True,False,False,True))

#pass the variable itself to recursively format function for printing 
print(formatter.format(formatter,formatter,formatter,formatter))


#pass string variables in multi line for printing
print(formatter.format("Try your",
                        "Own text here",
                        "Maybe a Poem",
                        "or a song about fear."))

