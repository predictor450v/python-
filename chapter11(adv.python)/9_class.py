class Animal:
    species = "Mammal"  # Class attribute

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species  # Modifies class attribute

    @classmethod
    def get_species(cls):
        return cls.species

print(Animal.get_species())  # Mammal
Animal.set_species("Reptile")
print(Animal.get_species())  # Reptile

# You can also call class methods on instances, but it's less common:
a = Animal()
print(a.get_species()) # Reptile