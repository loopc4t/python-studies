class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor method
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    def get_info(self):
        return f"{self.name} is {self.age} years old"


# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Luna", 5)

print(dog1.bark())
print(dog2.get_info())
print(Dog.species)
