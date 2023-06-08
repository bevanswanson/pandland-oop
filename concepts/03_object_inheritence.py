class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement the 'speak' method.")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

    @staticmethod
    def fly():
        return "The bird is flying."

# Creating instances of different animals
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

# Calling instance methods
print(dog.speak())   # Output: Woof!
print(cat.speak())   # Output: Meow!
print(bird.speak())  # Output: Chirp!
# Calling the static method
print(Bird.fly())    # Output: The bird is flying.

# Polymorphism example
def make_animal_speak(animal):
    print(animal.speak())

make_animal_speak(dog)   # Output: Woof!
make_animal_speak(cat)   # Output: Meow!
make_animal_speak(bird)  # Output: Chirp!
