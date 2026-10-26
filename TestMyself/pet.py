class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 10

    def feed(self,amount):
        if 