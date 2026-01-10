class Person:
    def __init__(self, name):
        self._name = name  # Convention: underscore (_) denotes a private attribute.

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name 

p = Person("Alice")
print(p.get_name())  # Alice
p.set_name("Bob")
print(p.get_name())  # Bob 