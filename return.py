
''''
def greet(name):
    print(f"Hello {name}")
    print("How are you?")
    
greet("Mary")
'''
def double(num):
    return num*2

print(double(5))

#Alternatively
def double(num):
    dub = num*2
    return dub

print(double(5))

#returning multiple functions
def  arithmetic_operations(a, b):
    return a + b, a - b, a*b, a/b
print(arithmetic_operations(10,2))
    