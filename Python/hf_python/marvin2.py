paranoid_andriod = 'Marvin, the paranoid Andriod'
letters = list(paranoid_andriod)
for char in letters[:6]:
    print('\t',char)
print()
for char in letters[-7:]:
    print('\t' * 2,char)
print()
for char in letters[12:20]:
    print('\t' * 3,char)