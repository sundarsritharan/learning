vowels = vowels = ['a','e','i','o','u']
word = input("Enter a word to find it's vowels: ")
found = {}
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

#check if there are vowels in the given word
for letter in word:
    if letter in vowels:
        found[letter] += 1 

for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')
