'''
def greet(name="User"):
    
    print(f"Hello {name}")
    
greet("Mary")
greet("Johnson")
greet("Jane")
greet("John")
'''
#Default arguement
#greet("Alice")
'''    
def add_all(a,b,c):
    return a+b+c

print(add_all(1,2,3))
'''
'''
def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5,6,7,8))
'''    

"""
def add(a,b):
    return a+b
print(add(3,2))
"""

"""
#Lambda function - this is a one line function
add = lambda a,b: a+b
add(3,2)
"""


#scope
x=4
def foo():
    x=5
    print(f"Outer: {x}")
    def inner():
        x=3
        print(f"Inner: {x}")
    inner()

def new_func():
    global x
foo()
print(f"Global: {x}")  
