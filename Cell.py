from random import normalvariate

class Cell:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.plants = round(max((normalvariate(20,10), 0)))
        self.MAX_PLANTS = 100
        self.creatures = []

    def getX(self) -> int:
        return self.x
    
    def getY(self) -> int:
        return self.y
    
    def getWorld(self):
        return self.world
    
    def getPlants(self) -> int:
        return round(self.plants)

    def changePlants(self, amount: int) -> None:
        # print(f" plants: {self.plants} + {amount}")
        self.plants = self.plants + amount
        if self.plants < 0:
            return ValueError("Amount of plants is a negative number")
        # print(f" plants after update: {round(self.plants)}")
        self.plants = min(round(self.plants), self.MAX_PLANTS)
    
    def addCreatures(self, creature) -> None:
        self.creatures.append(creature)
    
    def removeCreature(self, creature) -> None:
        if creature in self.creatures:
            self.creatures.remove(creature)
    
    def getCreatures(self) -> list:
        return self.creatures