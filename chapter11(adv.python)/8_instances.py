class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute

    def speak(self):
        return f"{self.name} says Woof!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!