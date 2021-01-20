import all_blocks as o
import config as c
import utils as u

class layer:
    def __init__(self, sizex, sizey, screen, stage, stateindex):
        self.sizex = sizex
        self.sizey = sizey
        self.screen = screen
        self.stage = stage
        self.stateindex = stateindex
        self.grid = []
        for i in range(sizex):
            array = []
            for j in range(sizey):
                array.append(o.block_empty(screen, stage, stateindex, (i, j, stateindex)))
            self.grid.append(array)

        # print(self.grid)
        # for i in range(sizex):
        #     for j in range(sizey):
        #         self.grid[i][j]= (o.block_empty(screen, stage) if (i+j)%2==0 else o.block(screen, stage))

    def draw(self, height, layersamount, whereisplayer):
        for i in range(self.sizex):
            for j in range(self.sizey):
                self.grid[i][j].draw(u.index_to_position(i, j, height, self.sizex, self.sizey, layersamount), whereisplayer)

    def update(self, x, y, block):
        self.grid[x][y] = block
        block.state_index = self.stateindex

    def copy(self, newstateindex):
        lay = layer( self.sizex, self.sizey, self.screen, self.stage, newstateindex)
        for i in range(self.sizex):
            for j in range(self.sizey):
                lay.update(i, j, self.grid[i][j].copy(newstateindex))
        return lay
