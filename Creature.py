from World import World
from Cell import Cell

class Creature:
    def __init__(self, sight: int, world: World):
        self.sight = sight
        self.energy = 20
        self.world = world

    def moveTo(self, newCell: Cell) -> None:
        currentCell = self.getCurrentCell()
        if currentCell is not None:
            currentCell.removeCreature(self)
        if newCell is not None:
            newCell.addCreatures(self)
    
    def getCurrentCell(self) -> Cell:
        for cell in self.world.getCellList():
            temp = cell.getCreatures()
            if self in temp:
                return cell
        return None
    
    def move(self) -> None:
        return
    
    def act(self) -> None:
        return
    
    def getSight(self) -> int:
        return self.sight
    
    def die(self) -> None:
        self.moveTo(None)
    
    def isAlive(self) -> bool:
        if self.getCurrentCell() != None:
            return True
        return False
    
    def getEnergy(self) -> int:
        return self.energy
    
    def changeEnergy(self, energy: int):
        if self.energy + energy <= 0:
            self.die()
        self.energy = self.energy + energy
    
    def getVisibleCells(self) -> list:
        visibleCells = []
        currentCell = self.getCurrentCell()
        x = currentCell.getX()
        y = currentCell.getY()
        for cell in self.world.getCellList():
            xcell = cell.getX()
            ycell = cell.getY()
            if max(abs(x-xcell), abs(y-ycell)) <= self.sight:
                visibleCells.append(cell)
        return visibleCells