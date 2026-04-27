"""
Topic: Functions with Return Values
I do: I explain the concept and provide a simple example.
To let a function return a value back to the caller instead of just printing it, use the `return` statement.
This allows you to store the result of a function in a variable and use it later.
"""

# I do:
def add_numbers(a, b):
    result = a + b
    return result

# Calling the function and storing the returned value in a variable
sum_result = add_numbers(5, 7)
print("The sum is:", sum_result)

"""
We do: We work together on a slightly more complex example.
Let's create a function that checks if a number is even, returning a Boolean (True/False).
"""
# We do:
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num_to_check = 10
if is_even(num_to_check):
    print(f"{num_to_check} is an even number.")
else:
    print(f"{num_to_check} is an odd number.")

"""
You do: I give you a problem to solve on your own.
Create a function named `multiply` that takes two parameters, multiplies them together, and RETURNS the result.
Then, call the function, save the result in a new variable, and print the variable.
"""
# You do:
# Write your code below this line

