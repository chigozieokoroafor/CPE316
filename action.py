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
        self.prevPos = [-1, -1]
        

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

    def getSinglePosition(self,x):
        pos = [-1,-1]
        for row in self.world:
            # print("================================")    
            for item in row:
                # print(item)
                if item ==  x:
                    pos[1] = row.index(x)
                    pos[0] = self.world.index(row)
                    
        return pos

    def FirstItemInCol(self, col) :
        pos = [-1,-1]
        for row in self.world:    
            if row[col] != 0:
                pos[1] = col
                pos[0] = self.world.index(row)
                return pos

    def swap(self, x, y):
        # positions = self.getPosition(x, y)    
        x_pos = self.getSinglePosition(x)
        y_pos = self.getSinglePosition(y)

        # check which is on top first
        first = x
        fPos = x_pos
        second = y 
        sPos = y_pos
        if x_pos[0]> y_pos[0]:
            first = y
            fPos = y_pos
            second = x 
            sPos = x_pos

        first_clear = self.clear(first)
        first_count = 0
        fcolumn = fPos[1]
        while first_clear == False:
            # row = x_pos[0]
            
            previousboxpos = self.FirstItemInCol(fcolumn)
            previousBox = self.world[previousboxpos[0]][previousboxpos[1]]
            # previousbox = self.world[row - 1][column]
            self.mov(previousBox)
            self.grab()
            self.placeOnTable()
            first_clear = self.clear(first)
            first_count += 1
        
        second_clear = self.clear(second)
        # print(self.getWorld())
        # print(first, second)
        # print(fPos, sPos)
        
        scolumn = sPos[1]
        second_count = 0
        while second_clear == False:
            # row = x_pos[0]
            
            previousboxpos = self.FirstItemInCol(scolumn)
            previousBox = self.world[previousboxpos[0]][previousboxpos[1]]
            # previousbox = self.world[row - 1][column]
            self.mov(previousBox)
            self.grab()
            self.placeOnTable()
            second_clear = self.clear(second)
            second_count += 1
        # this moves second to table if it isn't on table

        if self.onTable(second) == False:
            self.mov(second)
            self.grab()
            self.placeOnTable()

        
        # replace first with second
        # get first item in column
        # put second on box
        # self.world[previousboxpos[0]][previousboxpos[1]]
        
        # after here restack in same order, but swapping the items into different positions
        



    # def boxOnAnotherCheck(self, x, y):
    #     pass

    # def boxUnderAnother(self, x, y):
    #     pass

    # def sortAscending(self, x:list):
    #     pass

    # def sortDescending(self, x:list):
    #     pass

    def clear(self, x): # this part checks if there is any box on top of x
        # self.mov(x)
        # self.grab()
        # self.placeOnTable()
        current_position = self.getSinglePosition(x)
        row = current_position[0]
        column = current_position[1]

        if self.world[row-1][column] != 0:
            return False
        else:
            return True
    
    def stack(self, x, y): # this part places box labelled x on stack
        self.mov(x)
        self.grab()

    def onTable(self, x): # this part check if x is on table
        pos = self.getSinglePosition(x)
        if pos[0] == self.surface[0]:
            return True
        else:return False

            
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

    def placeOnBox(self, y):
        self.prevPos = self.getSinglePosition(y)
        row = self.prevPos[0]
        column = self.prevPos[1]
        self.world[row-1][column] = self.hold
        
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
        