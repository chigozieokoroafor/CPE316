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
            for item in row:
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
        
        x_pos = self.getSinglePosition(x)
        y_pos = self.getSinglePosition(y)
        unstacked_box_positions = [] # stores positions of items in previous positions while unstcking
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
        count = 0 
        
        fcolumn = fPos[1]
        while first_clear == False:
        
            
            previousboxpos = self.FirstItemInCol(fcolumn)
            previousBox = self.world[previousboxpos[0]][previousboxpos[1]]
            
            self.mov(previousBox)
            self.grab()
            box_pos = self.placeOnTable()
            unstacked_box_positions.insert(0,box_pos)
            first_clear = self.clear(first)
            print(self.getWorld())
            print(f"=====first====={count}===")
            count += 1
        
        second_clear = self.clear(second)
        
        
        scolumn = sPos[1]
        
        while second_clear == False:
            
            
            previousboxpos = self.FirstItemInCol(scolumn)
            previousBox = self.world[previousboxpos[0]][previousboxpos[1]]
            
            self.mov(previousBox)
            self.grab()
            box_pos = self.placeOnTable()
            unstacked_box_positions.insert(0,box_pos)
            second_clear = self.clear(second)
            print(self.getWorld())
            print(f"=====second====={count}===")
            count += 1
            
        # this moves second to table if it isn't on table

        if self.onTable(second) == False:
            self.mov(second)
            self.grab()
            box_pos = self.placeOnTable()
            unstacked_box_positions.insert(0,box_pos)

        first_item_in_column_pos = self.FirstItemInCol(fPos[1])
        first_item_in_column = self.world[first_item_in_column_pos[0]][first_item_in_column_pos[1]]
    
        fPos_onTable = self.getSinglePosition(first)
        sPos_onTable = self.getSinglePosition(second)
        self.stack(first, first_item_in_column)

        # then move second to th first's positio on table
        self.world[fPos_onTable[0]][fPos_onTable[1]] = second
        self.world[sPos_onTable[0]][sPos_onTable[1]] = 0

        
        print(self.getWorld())
        print("=============p===")
        # # using a while loop to stack the boxes.
        while len(unstacked_box_positions) != 0:
            # replace first with second
            # get first item in column
            # put second on box
            # self.world[previousboxpos[0]][previousboxpos[1]]
            
            # after here restack in same order, but swapping the items into different positions
            first_item_in_column_pos = self.FirstItemInCol(fPos[1])
            first_item_in_column = self.world[first_item_in_column_pos[0]][first_item_in_column_pos[1]]
            box_position = unstacked_box_positions[0]
            box = self.world[box_position[0]][box_position[1]]
            if box != 0:
                self.stack(box, first_item_in_column)
            print(self.getWorld())
            print(f"====stack======{count}===")
            count += 1
            unstacked_box_positions.pop(0)
            
        
        
    def placeBoxOnTopanother(self, x, y): # puts y on x
        x_pos = self.getSinglePosition(x)
        firstItemPos = self.FirstItemInCol(x_pos[1])
        firstItem = self.world[firstItemPos[0]][firstItemPos[1]]
        itemOnTable = self.onTable(firstItem)
        while itemOnTable ==False:
            self.mov(firstItem)
            self.grab()
            self.placeOnTable()
            firstItemPos = self.FirstItemInCol(x_pos[1])
            firstItem = self.world[firstItemPos[0]][firstItemPos[1]]
            itemOnTable = self.onTable(firstItem)
        self.mov(y)
        self.grab()
        self.placeOnBox(x)


        
        # y_pos = self.getSinglePosition(y)
        # unstacked_box_positions = [] # stores positions of items in previous positions while unstcking
        # # check which is on top first
        # first = x
        # fPos = x_pos
        # second = y 
        # # sPos = y_pos
        # # if x_pos[0]> y_pos[0]:
        # #     first = y
        # #     fPos = y_pos
        # #     second = x 
        # #     sPos = x_pos
        # fcolumn = fPos[1]
        # clear = self.clear(first)
        # while clear == False:
        #     previousboxpos = self.FirstItemInCol(fcolumn)
        #     previousBox = self.world[previousboxpos[0]][previousboxpos[1]]
        #     # previousbox = self.world[row - 1][column]
        #     self.mov(previousBox)
        #     self.grab()
        #     box_pos = self.placeOnTable()
        #     unstacked_box_positions.insert(0,box_pos)
        #     clear = self.clear(first)
        # self.mov(second)
        # self.grab()
        # self.placeOnBox(first)

    def boxUnderAnother(self, x, y): # puts y under x
        x_pos = self.getSinglePosition(x)
        firstItemPos = self.FirstItemInCol(x_pos[1])
        firstItem = self.world[firstItemPos[0]][firstItemPos[1]]
        itemOnTable = self.onTable(firstItem)
        while itemOnTable ==False:
            self.mov(firstItem)
            self.grab()
            self.placeOnTable()
            firstItemPos = self.FirstItemInCol(x_pos[1])
            firstItem = self.world[firstItemPos[0]][firstItemPos[1]]
            itemOnTable = self.onTable(firstItem)
        self.mov(x)
        self.grab()
        self.placeOnBox(y)

    def sortStack(self, x:list, order:str = "ascending"):
        # 
        onTable = self.onTable(x[0])
        count = 0
        while onTable == False:
            item = x[count]
            self.mov(item)
            self.grab()
            self.placeOnTable()
            count += 1
            try:
                self.onTable(x[count])
            except IndexError:
                break
        if order == "ascending":
            sorted_list = sorted(x)
        else:
            sorted_list = sorted(x,reverse=True)

        count = 1
        while count<len(sorted_list):
            self.mov(sorted_list[count])
            self.grab()
            self.placeOnBox(sorted_list[count-1])
            count += 1

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
        self.placeOnBox(y)
        
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
            # check if space is filled
            if self.world[self.surface[0]][column] == 0:
                self.world[self.surface[0]][column] = self.hold
                filled = False
                return [self.surface[0], column]
            column += 1

    def placeOnBox(self, y): # this puts box in hold on y
        self.prevPos = self.getSinglePosition(y)
        row = self.prevPos[0]
        column = self.prevPos[1]
        self.world[row-1][column] = self.hold
        
        # return [row-1, column], first_item
            
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
        