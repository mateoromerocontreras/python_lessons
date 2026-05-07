"""
Inheritance is a fundamental concept in object-oriented programming that allows 
a new class (called a child or subclass) to inherit attributes and methods 
from an existing class (called a parent or superclass). This promotes code reusability 
and establishes a natural hierarchical relationship between classes.
Key points about inheritance:
• A child class can override methods of the parent class to provide specific 
implementations.
• A child class can add new attributes and methods that are not present in the 
parent class.
• The child class can call the parent class's methods using the super() function.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
    
    def info(self):
        return f"{self.name} is an animal."
    
    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
# # Create instances of Dog and Cat
# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# # Call the speak method on both instances
# print(f"{dog.name} says: {dog.speak()}")
# print(f"{cat.name} says: {cat.speak()}")
# print(f"{dog.name} info: {dog.info()}")
# print(f"{cat.name} info: {cat.info()}")
# print(f"{dog.name} eat: {dog.eat()}")
# print(f"{cat.name} eat: {cat.eat()}")
