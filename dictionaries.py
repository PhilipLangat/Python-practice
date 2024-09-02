# An empty dictionary
empty_dict = {}

# A dictionary with integer keys
numbers = {1: 'one', 2: 'two', 3: 'three'}

# A dictionary with string keys
fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}

# A dictionary with mixed data types
mixed = {"name": "Alice", "age": 30, "is_student": False}

# A dictionary using the dict() constructor
person = dict(name="Alice", age=30, is_student=False)

#Accessing Dictionary Items
#You can access dictionary items by referring to their keys.

fruits = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(fruits["apple"])  # Output: red
#Using the get() method

print(fruits.get("banana"))  # Output: yellow
print(fruits.get("orange", "not found"))  # Output: not found