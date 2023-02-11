from game_files.imports.view_constants import global_view_constants as v

h_map = {
    "left": 0,
    "mid": 1,
    "right": 2,
}

v_map = {
    "top": 0,
    "up": 0,
    "mid": 1,
    "down": 2,
    "bottom": 2,
}


class decoration:
    def __init__(self, screen, stage, state_index, pos, sprite, h_align, v_align):
        self.screen = screen
        self.stage = stage
        self.sprite = sprite
        self.state_index = state_index
        self.pos = pos
        self.h_align = h_align  # left, mid, right
        self.v_align = v_align  # up, mid, down
        self.draw_offsets = self.find_draw_offsets()

    def find_draw_offsets(self):
        half_x_block = v.BLOCK_X_SIZE / 2
        half_y_block = v.BLOCK_Y_SIZE / 2
        half_x_sprite, half_y_sprite = self.sprite[0].get_size()
        half_x_sprite /= 2
        half_y_sprite /= 2

        x_offset = h_map[self.h_align] * (half_x_block - half_x_sprite)
        y_offset = v_map[self.v_align] * (half_y_block - half_y_sprite)

        return x_offset, y_offset

    def draw(self, pos, where_is_player):
        # pos - place to draw if right, up was chosen
        x, y = pos
        x_offset, y_offset = self.draw_offsets  # !! change for find_draw_offsets if necessary

        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], (x + x_offset, y + y_offset))

    def copy(self, new_state_index):  # !! copy is only for duplicating states
        return decoration(self.screen, self.stage, new_state_index, self.pos, self.sprite, self.h_align, self.v_align)
