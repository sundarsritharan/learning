data = [1,2,3,4,5,6,7,8,9]
even = []
for num in data:
    if not num % 2:
        even.append(num)

print(even)

#list comprehension 
more_even = [ num for num in data if not num % 2]

print(more_even)

data = [1, 'one', 2 , 'two', 3, 'three']
words = []
for num in data:
    if isinstance(num,str):
        words.append(num)

print(words)

#list comprehension 
more_words = [ num for num in data if isinstance(num,str)]

print(more_words)

data = list('So long and thanks for all the fish'.split())
title = []
for word in data:
    title.append(word.title())

print(title)

#list comprehension 
more_title = [ word.title() for word in data]

print(title)

#set comprehension 

vowels = {'a','e','i','o','u'}
msg = "Don't forget to pack your towel."
found = set() 

for v in vowels:
    if v in msg:
        found.add(v)

print(found)
print()

found2 = { v for v in vowels if v in msg}

print(found2)
print()
