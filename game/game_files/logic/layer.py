import game_files.imports.all_blocks as o
import game_files.imports.globals as g
import game_files.imports.utils as u


class layer:
    def __init__(self, size_x, size_y, screen, stage, state_index):
        self.size_x = size_x
        self.size_y = size_y
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.grid = []
        for i in range(size_x):
            array = []
            for j in range(size_y):
                array.append(o.block_empty(screen, stage, state_index, (i, j, state_index)))
            self.grid.append(array)

    def draw_once(self, height, layers_amount, where_is_player, x_offset, y_offset):
        for j in range(self.size_y):
            for i in range(self.size_x):
                x, y = u.index_to_position(i, j, height, self.size_x, self.size_y, layers_amount)
                self.grid[i][j].draw((x + x_offset, y + y_offset), where_is_player)

    def draw(self, height, layers_amount, where_is_player):
        self.draw_once(height, layers_amount, where_is_player, 0, 0)

    def update(self, x, y, block):
        self.grid[x][y] = block
        block.state_index = self.state_index

    def copy(self, new_state_index):
        lay = layer(self.size_x, self.size_y, self.screen, self.stage, new_state_index)
        for i in range(self.size_x):
            for j in range(self.size_y):
                lay.update(i, j, self.grid[i][j].copy(new_state_index))
        return lay
