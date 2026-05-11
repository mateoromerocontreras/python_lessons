# Por convención usamos mayúscula para nombrar las clases
class Dog:          
    """A simple attempt to model a dog."""
    # Constructor __init__():
    def __init__(self, name, age): 
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    
    # Funciones: metodos o comportamientos
    # Se crea un metodo seter para modificar el atributo
    def actualizarEdad(self, nuevaEdad):
        if (nuevaEdad > self.age):
            self.age = nuevaEdad
        else:
            print("La nueva edad debe ser mayor a la edad actual")
    
    # Se crean getters para acceder a los atributos
    def getEdad(self):
        return self.age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Instancias de la clase Dog
# Una instancia es un objeto en particular de la clase
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.name = "Pancho"
print(f"Mi perro ahora se llama {my_dog.name}")

my_dog.actualizarEdad(3)
print(f"La edad de mi perro ahora es {my_dog.getEdad()} años")