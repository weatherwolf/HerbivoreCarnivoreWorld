from Cell import Cell

class World:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cell_dict = {}

    def getWidth(self) -> int:
        return self.width
    
    def getHeight(self) -> int:
        return self.height
    
    def getCell(self, x: int, y: int) -> Cell:
        if x not in range(0, self.width):
            raise ValueError("x outside of world borders")
        elif y not in range(0, self.height):
            raise ValueError("y outisde of world borders")

        if (x, y) not in self.cell_dict:
            self.cell_dict[(x, y)] = Cell(self, x, y)
        return self.cell_dict[(x, y)]
    
    def getCreatures(self) -> list:
        creatureList = []
        cellList = self.getCellList()
        for cell in cellList:
            temp = cell.getCreatures()
            for creature in temp:
                creatureList.append(creature)
        return creatureList
    
    def getCellList(self) -> list:
        cellList = []
        for i in range(self.width):
            for j in range(self.height):
                cellList.append(self.getCell(i,j))
        return cellList


# from Cell import Cell

# class World:
#     def __init__(self, width: int, height: int):
#         self.width = width
#         self.height = height

#     def getWidth(self) -> int:
#         return self.width
    
#     def getHeight(self) -> int:
#         return self.height
    
#     def getCell(self, x: int, y: int) -> Cell:
#         if x not in range(0, self.width):
#             raise ValueError("x outside of world borders")
#         elif y not in range(0, self.height):
#             raise ValueError("y outisde of world borders")
#         return Cell(self, x, y)
    
#     def getCreatures(self) -> list:
#         creatureList = []
#         cellList = self.getCellList()
#         for cell in cellList:
#             temp = Cell.getCreatures(cell)
#             for creature in temp:
#                 creatureList.append(creature)
#         return creatureList
    
#     def getCellList(self) -> list:
#         cellList = []
#         for i in range(self.width):
#             for j in range(self.height):
#                 cellList.append(self.getCell(i,j))
#         return cellList

