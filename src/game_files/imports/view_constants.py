from game_files.imports.log import log


class view_constants:
    def __init__(self, x_scale=1, y_scale=1):
        self.X_SCALE = x_scale
        self.Y_SCALE = y_scale

        self.LEVEL_COMPLETION_SCALE = 0.5
        self.LEVEL_COMPLETION_OFFSET = 0

        self.WINDOW_X = self.WINDOW_Y = self.BLOCK_X_SIZE = self.BLOCK_Y_SIZE = self.LAYER_Y_OFFSET = \
            self.LAYER_X_OFFSET = self.WITCH_FONT_SIZE = self.WITCH_FONT_OFFSET = self.LEVEL_FONT_SIZE = \
            self.LEVEL_FONT_OFFSET = self.BLOCK_3D_DIFFERENCE = self.MESSAGE_FONT_SIZE = 0

        self.DECORATION_BASE_SIZE = 32

        self.update()

    def update(self):
        self.WINDOW_X = int(1280 * self.X_SCALE)
        self.WINDOW_Y = int(960 * self.Y_SCALE)
        self.BLOCK_X_SIZE = int(64 * self.X_SCALE)
        self.BLOCK_Y_SIZE = int(64 * self.Y_SCALE)
        self.LAYER_Y_OFFSET = int(8 * self.Y_SCALE)
        self.LAYER_X_OFFSET = int(4 * self.X_SCALE)
        self.WITCH_FONT_SIZE = int(32 * self.Y_SCALE)
        self.WITCH_FONT_OFFSET = int(8 * self.Y_SCALE)
        self.LEVEL_FONT_SIZE = int(48 * self.Y_SCALE)
        self.LEVEL_FONT_OFFSET = int(16 * self.Y_SCALE)
        self.BLOCK_3D_DIFFERENCE = int(16 * self.Y_SCALE)
        self.MESSAGE_FONT_SIZE = int(15 * self.Y_SCALE)

    def set_scales(self, x_scale, y_scale):
        if (x_scale, y_scale) == (self.X_SCALE, self.Y_SCALE):
            return
        self.X_SCALE = x_scale
        self.Y_SCALE = y_scale
        self.update()
        log.info("Rescaling to " + str(self.WINDOW_X) + "x" + str(self.WINDOW_Y))

    def change_resolution(self, resolution):
        x, y = resolution
        self.set_scales(1, 1)
        x_scale = x / self.WINDOW_X
        y_scale = y / self.WINDOW_Y
        self.set_scales(x_scale, y_scale)

    def get_decoration_rescale(self):
        return self.BLOCK_X_SIZE / self.DECORATION_BASE_SIZE, self.BLOCK_Y_SIZE / self.DECORATION_BASE_SIZE


global_view_constants = view_constants()
