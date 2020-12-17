pharse = "Don't panic!"
plist = list(pharse)
print(pharse)
print(plist)

#code to extract the word on tap
new_pharse = ''.join(plist[1:3])
new_pharse = new_pharse + ''.join([plist[5],plist[4],plist[7],plist[6]])

print(plist)
print(new_pharse)