import turtle
from World import World
from Cell import Cell
from Herbivore_Carnivore import Herbivore, Carnivore

class Turtle:
    def __init__(self, world: World):
        self.world = world
        self.width = world.getWidth()
        self.height = world.getHeight()
        self.myPen = turtle.Turtle()
        self.myPen.speed(0)
        self.myPen.hideturtle()
        self.myScreen = turtle.Screen()
        self.myScreen.tracer(0)

        self.topLeftX = -250
        self.topLeftY = 250
        self.grassColor = "#19CC24"
        self.herbColor = "#0000FF"
        self.carnColor = "#FF0000"
    
    def number(self, value: int, x: int, y: int, turtle: turtle.Turtle()) -> None:
        size = round(500/(5*max(self.width, self.height)))
        FONT = ('Arial', size, 'normal')
        myPen = turtle
        myPen.penup()
        myPen.goto(x,y)    	
        myPen.color("#000000")	  
        myPen.write(value, align="left", font=FONT)

    def creatureCircles(self, creatures: list, cell: Cell, turtle: turtle.Turtle()):
        k = max(self.width, self.height)
        positionMatrix = [[round(-0.75*500/k), 0], [round(-0.25*500/k), 0], 
                          [round(-0.75*500/k), round(-0.50*500/k)], [round(-0.25*500/k), round(-0.50*500/k)]]
        herbColor = self.herbColor
        carnColor = self.carnColor
        x = (500*(self.height - cell.getY()))/k - 250  
        y = ((250/k) + 250) - (500*(self.width - cell.getX()))/k
        myPen = turtle
        myPen.penup()
        for i in range(len(creatures)):
            if isinstance(creatures[i], Herbivore):
                myPen.fillcolor(herbColor)
            else:
                myPen.fillcolor(carnColor)
            myPen.setpos(x + positionMatrix[i][0], y + positionMatrix[i][1])
            myPen.begin_fill()
            myPen.circle(round(0.1*500/k))
            myPen.end_fill()

        
    def grid(self) -> None:
        myPen = self.myPen
        myPen.color("#000000")
        topLeftX = self.topLeftX
        topLeftY = self.topLeftY
        intDim = 500/max(self.width, self.height)

        for row in range(self.width+1):
            myPen.penup()
            myPen.goto(topLeftX, topLeftY-row*intDim)
            myPen.pendown()
            myPen.goto(topLeftX+self.width*intDim, topLeftY-row*intDim)

        for col in range(self.height+1):
            myPen.penup()
            myPen.goto(topLeftX+col*intDim, topLeftY)
            myPen.pendown()
            myPen.goto(topLeftX+col*intDim, topLeftY-self.height*intDim)   
        
    def fillColor(self) -> None:
        myPen = self.myPen
        myPen.color("#FFFFFF")
        myPen.goto(self.topLeftX, self.topLeftY)
        myPen.fillcolor(self.grassColor)
        myPen.begin_fill()
        myPen.penup()
        for _ in range(4):
            myPen.forward(500)
            myPen.right(90)
        myPen.end_fill()

    def getWorld(self) -> World:
        return self.world
    
    def plantValues(self) -> turtle:
        plantsValuesTurtle = turtle
        k = max(self.width, self.height)
        for cell in self.world.getCellList():
            x = (500*(self.height - cell.getY())- 175)/k - 250
            y = (((250 + 75)/k) + 250) - (500*(self.width - cell.getX()))/k
            self.number(cell.getPlants(), x, y, plantsValuesTurtle)
        return plantsValuesTurtle
    
    def creatureValues(self) -> turtle:
        creatureValues = turtle
        for cell in self.world.getCellList():
            creatureList = []
            for creature in cell.getCreatures():
                creatureList.append(creature)
            self.creatureCircles(creatureList, cell, creatureValues)
        return creatureValues
        
            