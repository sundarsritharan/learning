# Function that accepts any number of aruguments.

def myfunc(*args):
    for a in args:
        print(a, end= ' ')
    if args:
        print()

def myfunc1(**kwargs):
    for k,v in kwargs.items():
        print(k,v,sep='->',end=' ')
    if kwargs:
        print()

def myfunc2(*args,**kwargs):
    if args:
        for a in args:
            print(a, end= ' ')
        print()
    if kwargs:
        for k,v in kwargs.items():
            print(k,v,sep='->',end=' ')
        print()
      
#myfunc('sundar','priya','diya','nidhi')
# myfunc1(hus='sundar',wife='priya',daug_1='diya',daug_2='nidhi')
my_family = { 'hus' : 'sundar',
                'wife': 'priya',
                'daug_1' :'diya',
                'daug_2' : 'nidhi'
}
myfunc2(**my_family)