def double(arg):
    print('Before: ', arg)
    arg = arg * 2 
    print('After: ', arg)

def change(arg):
    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

numbers = [42,256,16]
double(numbers)
print(numbers)
change(numbers)
print(numbers)