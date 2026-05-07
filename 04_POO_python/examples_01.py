"""
Topic: Introduction to Objects and OOP in Python
I do: simple class, object, attributes, and methods.
"""

# I do:
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name} and I am {self.age} years old. I am {self.gender}.")
        print("Nice to meet you!")

    def estudiar(self):
        print("estoy estudiando...")

    def dormir(self):
        print("estoy durmiendo...")


student1 = Student("Ana", 20, "female")
student2 = Student("Luis", 22, "male")

print("--- Students ---")
print(student1.name)
print(student1.gender)
genero = student1.gender
print(student2.name)
student1.introduce()
student2.introduce()

student1.estudiar()
student1.estudiar()

"""
We do: a more complete example using a Car class.
This example shows how methods can change object attributes.
"""

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
        print(f"The {self.brand} {self.model} now has {self.fuel_level} fuel units.")


car1 = Car("Toyota", "Corolla", 2)
print("--- Car demo ---")
car1.drive()
car1.drive()
car1.drive()
car1.refuel(3)
car1.drive()

"""
Another quick example: a BankAccount class.
This reinforces the idea of data + behavior together.
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. Balance: {self.balance}")
        else:
            print(f"{self.owner} does not have enough money.")


account = BankAccount("Marta", 100)
print("--- Bank account demo ---")
account.deposit(50)
account.withdraw(30)
account.withdraw(200)
