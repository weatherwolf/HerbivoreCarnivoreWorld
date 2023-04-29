from World import World
from Herbivore_Carnivore import Herbivore, Carnivore
import turtle
from Turtle import Turtle
from Simulation import Simulation
import time

w = World(25,25)
t= Turtle(w)
s = Simulation(t, 15, 2)
t.fillColor()
t.grid()
s.CreateCreatures()

while s.Iteration():
    time.sleep(1)

turtle.Screen().exitonclick()
