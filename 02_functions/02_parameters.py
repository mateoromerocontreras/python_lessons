"""
Topic: Functions with Parameters
I do: I explain the concept and provide a simple example.
Information can be passed into functions as arguments (variables placed inside the parentheses).
These are called parameters when defined in the function declaration, and arguments when passed in during the function call.
"""

# I do:
# Function with parameters
def greet_person(name):
    # 'name' is a parameter
    print(f"Hello, {name}!")

# "Alice" and "Bob" are arguments
greet_person("Alice")
greet_person("Bob")

"""
We do: We work together on a slightly more complex example.
Let's create a function that takes two parameters to calculate and print the area of a rectangle.
"""
# We do:
def calculate_area_and_print(length, width):
    area = length * width
    print(f"The area of a rectangle with length {length} and width {width} is {area}.")

calculate_area_and_print(5, 10)
calculate_area_and_print(3.5, 2)

"""
You do: I give you a problem to solve on your own.
Create a function named `introduce` that takes two parameters: `name` and `age`. 
Make the function print a sentence like "My name is [name] and I am [age] years old.".
Then, call the function with your own name and age as arguments.
"""
# You do:
# Write your code below this line

