vowels = vowels = ['a','e','i','o','u']
word = input("Enter a word to find it's vowels: ")
found = []

#check if there are vowels in the given word
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for letter in found:
    print(letter)
