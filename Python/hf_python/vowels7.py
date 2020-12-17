vowels = set('aeiou')
word = input("Enter a word to find it's vowels: ")
found = {}

#check if there are vowels in the given word
found = vowels.intersection(set(word))

for letter in found:
    print(letter)
