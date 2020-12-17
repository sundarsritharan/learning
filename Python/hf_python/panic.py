pharse = "Don't panic!"
plist = list(pharse)
print(pharse)
print(plist)

#code to extract the word on tap
for i in range(4):
    plist.pop()

plist.pop(0)
plist.remove("'")

plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))

new_pharse = ''.join(plist)
print(plist)
print(new_pharse)