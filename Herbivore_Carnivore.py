from Creature import Creature
from World import World
from random import randint


class Herbivore(Creature):
    def __init__(self, size: int, world: World):
        self.size = size
        super().__init__(1, world)

    def getSize(self) -> int:
        if self.size <= 0:
            ValueError("Size of herbivore should always be positive")
        return self.size
    
    def move(self) -> None:
        bestCell = self.getCurrentCell()
        for cell in super().getVisibleCells():
            if cell.getPlants() > bestCell.getPlants():
                bestCell = cell
        self.moveTo(bestCell)
    
    def act(self) -> None:
        maxEat = round(min(self.getCurrentCell().getPlants(), ((2*self.size*self.size)/(1 + self.size))))
        self.getCurrentCell().changePlants(-maxEat)
        self.changeEnergy(maxEat - self.size)

    def biggestHerb(self):
        biggestSize = 0
        biggestHerb = None
        for creature in self.getCurrentCell().getCreatures():
            if type(creature) != Herbivore:
                continue
            if creature.getSize() > biggestSize:
                biggestSize = creature.getSize()
                biggestHerb = creature
        return biggestHerb

class Carnivore(Creature):
    def __init__(self, world: World):
        super().__init__(2, world)
        self.energy = 30
        self.successRate = 70

    def move(self) -> None:
        bestSize = 0
        bestCount = 0 
        bestCell = self.getCurrentCell()
        for cell in super().getVisibleCells():
            currentSize = 0
            herbCount = 0
            creatureList = cell.getCreatures()
            for creature in creatureList:
                if type(creature) == Herbivore and creature != None:
                    herbCount += 1
                    currentSize = creature.biggestHerb().getSize()
            if herbCount > bestCount:
                bestCell = cell
                bestCount = herbCount
                bestSize = currentSize
            if herbCount == bestCount:
                if currentSize > bestSize:
                    bestCell = cell

        self.moveTo(bestCell)
    
    def act(self) -> None:
        biggestSize = 0
        toBeEatenHerbivore = None
        if self.getCurrentCell() == None:
            return
        for creature in self.getCurrentCell().getCreatures():
            if type(creature) == Herbivore:
                toBeEatenHerbivore = creature.biggestHerb()
                biggestSize = toBeEatenHerbivore.getSize()
                break
        if toBeEatenHerbivore != None:
            if self.successRate >= randint(0,100):
                self.changeEnergy(biggestSize)
                toBeEatenHerbivore.die()
        self.changeEnergy(-5)

    