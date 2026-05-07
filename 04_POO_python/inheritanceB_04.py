# import animal clase from inheritance_03.py and create a new class called Bird that inherits from Animal. Override the speak method to return "Chirp!" and create an instance of Bird to test it.
from inheritance_03 import Animal

class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Create an instance of Bird
bird = Bird("Tweety")
print(f"{bird.name} says: {bird.speak()}")
print(f"{bird.name} info: {bird.info()}")
print(f"{bird.name} eat: {bird.eat()}")