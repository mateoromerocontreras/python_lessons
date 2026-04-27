## Lesson 1: Introduction to Objects and Object-Oriented Programming in Python

### Goal
In this lesson, you will learn the basic building blocks of Object-Oriented Programming (OOP): `class`, `object`, `instance`, `attribute`, and `method`.

### Why OOP?
OOP helps us organize code by grouping data and behavior together. Instead of working only with separate variables and functions, we model real-world things as objects.

### Core Concepts

#### Class
A class is a blueprint for creating objects. It defines what data the objects will have and what they can do.

#### Object
An object is a real thing created from a class. It contains actual values.

#### Instance
An instance is another word for object. If we create a `Dog` object from the `Dog` class, that object is an instance of `Dog`.

#### Attribute
An attribute is a piece of data stored inside an object.

#### Method
A method is a function defined inside a class. Methods describe actions that an object can perform.

---

### I do
We start with a simple class that represents a student.

```python
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def introduce(self):
		print(f"Hi, I'm {self.name} and I am {self.age} years old.")


student1 = Student("Ana", 20)
print(student1.name)
student1.introduce()
```

What is happening here:
- `Student` is the class.
- `student1` is an object or instance.
- `name` and `age` are attributes.
- `introduce()` is a method.
- `self` refers to the current object.

### We do
Now let's build a `Car` class together.

```python
class Car:
	def __init__(self, brand, model, fuel_level):
		self.brand = brand
		self.model = model
		self.fuel_level = fuel_level

	def drive(self):
		if self.fuel_level > 0:
			print(f"The {self.brand} {self.model} is driving.")
			self.fuel_level -= 1
		else:
			print(f"The {self.brand} {self.model} needs fuel.")

	def refuel(self, amount):
		self.fuel_level += amount
		print(f"Fuel level is now {self.fuel_level}.")


car1 = Car("Toyota", "Corolla", 2)
car1.drive()
car1.drive()
car1.drive()
car1.refuel(3)
car1.drive()
```

### You do
Create a `Book` class with these requirements:
- attributes: `title`, `author`, `pages`
- method `describe()` that prints the book information
- create at least two book objects

Then try this challenge:
- add a method named `is_long()` that returns `True` if the book has more than 300 pages, otherwise `False`

---

### Key ideas to remember
- A class is the blueprint.
- An object is created from a class.
- An instance is an object.
- Attributes store data.
- Methods define behavior.

### Practice files
- See [examples](01_examples.py) for runnable examples.
- See [exercises](02_exercises.py) for practice tasks.
