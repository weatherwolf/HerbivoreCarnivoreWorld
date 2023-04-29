from World import World
from Cell import Cell
from Creature import Creature
from Herbivore_Carnivore import Herbivore, Carnivore
from Turtle import Turtle
from random import randint, normalvariate
import turtle as tur

class Simulation:
    def __init__(self, turtle: Turtle, pHerb: int, pCarn: int):
        self.turtle = turtle
        self.world = turtle.getWorld()
        self.width = turtle.getWorld().getWidth()
        self.height = turtle.getWorld().getHeight()
        self.plantTurtle = tur
        self.creatureTurtle = tur

        self.pHerb = pHerb
        self.pCarn = pCarn 

    def CreateCreatures(self):
        for cell in self.world.getCellList():
            if randint(0,100) < self.pHerb:
                for _ in range(randint(1,3)):
                    randSize = sorted([0,round(normalvariate(30, 10)), 70])[1]  
                    Herbivore(randSize, self.world).moveTo(cell)
            elif randint(0, 100) < self.pCarn:
                Carnivore(self.world).moveTo(cell)
    
    def Iteration(self) -> bool:
        self.removeTurtle()
        herbList = []
        carnList = []
        for cell in self.world.getCellList():
            for creature in cell.getCreatures():
                if type(creature) == Herbivore:
                    herbList.append(creature)
                else:
                    carnList.append(creature)
            plantChange = sorted([0,normalvariate(1,1), 10])[1]
            cell.changePlants(round(plantChange))
        self.createTurtle()
        for herb in herbList:
            herb.move()
            herb.act()
        for carn in carnList:
            carn.move()
            carn.act()
        
        tur.update()
        tur.hideturtle()
        return herbList and carnList

    def removeTurtle(self):
        self.plantTurtle.clear()
        self.creatureTurtle.clear()
    
    def createTurtle(self):
        self.plantTurtle = self.turtle.plantValues()
        self.creatureTurtle = self.turtle.creatureValues()
        

    