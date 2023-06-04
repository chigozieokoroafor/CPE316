import numpy

class Bot:
    # position is [row, column]
    def __init__(self, world:list):
        self.surface = [len(world)-1, len(world[0])-1]
        self.world = world
        self.xpos = [-1,-1] 
        self.ypos = [-1,-1]
        self.hold = 0
        self.pos = [-1, -1]
        

    def getPosition(self,x, y):
        # get the positions from of x and y
        xpos = [-1,-1] 
        ypos = [-1,-1]

        # "Get the position of x"
        for row in self.world:    
            for item in row:
                if item ==  x:
                    xpos[1] = row.index(x) + 1
                    xpos[0] = self.world.index(row) + 1

        # "Get the position of y"
        for row in self.world:
            for c in row:
                if c ==  y:
                    ypos[1] = row.index(y) + 1
                    ypos[0] = self.world.index(row) + 1
                # print(ypos)
        
        if self.xpos[1] == xpos[1]:
            return(f"Box labelled {x} not found")
        if self.ypos == ypos[1] :
            return(f"Box labelled {y} not found")
        else: return (xpos, ypos)
        
    def swap(self, xpos, ypos):
        pass    

    # def boxOnAnother(self, x, y):
    #     pass

    # def boxUnderAnother(self, x, y):
    #     pass

    # def sortAscending(self, x:list):
    #     pass

    # def sortDescending(self, x:list):
    #     pass

    def clear(self, x): # this part removes box labelled x
        pass

    def stack(self, x, y): # this part places box labelled x on
        pass
            
    def placeOnTable(self):
        column = self.pos[1] - 1
        # row = self.pos[0] - 1
        # self.hold = self.world[row][column]
        filled = True
        while filled == True:
            # check if spcae is filled
            if self.world[self.surface[0]][column] == 0:
                self.world[self.surface[0]][column] = self.hold
                filled = False
            column += 1
        

    def mov(self, x): # this moves to the position of box x
        pos = [-1,-1]
        for row in self.world:    
            for item in row:
                if item ==  x:
                    pos[1] = row.index(x) + 1
                    pos[0] = self.world.index(row) + 1
        self.pos = pos
        return (self.pos)

    def grab(self): # this grabs item at self.pos
        column = self.pos[1] - 1
        row = self.pos[0] - 1
        self.hold = self.world[row][column]
        self.world[row][column] = 0
        
    def getWorld(self):
        return numpy.array(self.world)