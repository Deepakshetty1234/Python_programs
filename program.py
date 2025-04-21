class Dog:
    # Class variable
    species = "Canine"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating instances of the Dog class
buddy = Dog("Buddy", 3)
charlie = Dog("Charlie", 5)

# Accessing attributes and methods
print(f"{buddy.name} is a {buddy.species}") # Output: Buddy is a Canine
print(buddy.description()) # Output: Buddy is 3 years old
print(charlie.speak("Woof!")) # Output: Charlie says Woof!