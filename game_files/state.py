import traceback
from game_files.layer import layer
from game_files.player import player
from game_files.charmap import charmap
import game_files.utils as u
import game_files.all_blocks as o
import game_files.all_sprites as s
from game_files.log import log


class state:
    def __init__(self, screen, stage, state_index):
        self.layers = []
        self.player = None
        self.screen = screen
        self.stage = stage
        self.x = -1
        self.y = -1
        self.z = -1
        self.state_index = state_index
        self.completed = False

    def copy(self, new_state_index):
        sta = state(self.screen, self.stage, new_state_index)
        sta.x = self.x
        sta.y = self.y
        sta.z = self.z
        sta.player = self.player.copy(new_state_index)
        sta.layers = []
        sta.completed = self.completed
        for lay in self.layers:
            sta.layers.append(lay.copy(new_state_index))
        return sta

    def move(self, direction):  # !!modifies current state instead of returning copy
        self.player.set_next_move_direction(direction)  # if something is enqueued, this will be ignored
        self.get_block(self.player.pos).on_step_out()
        self.player.move()
        step_in_block = self.get_block(self.player.pos)
        if step_in_block is not None:
            step_in_block.on_step_in()

    def draw(self):
        for i in range(len(self.layers)):
            self.layers[i].draw(i, len(self.layers), u.relative_to_player(i, self.player.pos[2]))
        if not self.player.dead:
            self.draw_player()
        if self.player.dead:
            self.screen.blit(s.sprites['you_died'], (0, 0))

    def draw_one_layer(self, layer_index):  # !! can't be used above
        if self.player.dead or layer_index >= len(self.layers):
            self.draw()
            return

        self.layers[layer_index].draw(layer_index, len(self.layers), 0)
        if self.player.pos[2] == layer_index:
            self.draw_player()

    def draw_player(self):
        pos = self.player.pos
        self.player.draw(u.index_to_position(pos[0], pos[1], pos[2], self.x, self.y, self.z))

    def enqueue_move(self, direction):
        self.player.enqueue_move(direction)

    def is_next_move_forced(self):
        return len(self.player.enqueued_moves) != 0

    def standable(self, pos):
        x, y, z = pos
        if u.out_of_range(x, y, self.x, self.y):
            return False
        if type(self.layers[z].grid[x][y]) in o.standables:
            return True
        return False

    def get_block(self, pos):
        x, y, z = pos
        if u.out_of_range(x, y, self.x, self.y) or z < 0 or z > len(self.layers):
            return None
        return self.layers[z].grid[x][y]

    def set_block(self, pos, block):
        x, y, z = pos
        if u.out_of_range(x, y, self.x, self.y):
            return
        self.layers[z].grid[x][y] = block

    def get_size(self):
        return self.x, self.y, len(self.layers)

    def teleport_player(self, pos, activate_step_in=True):
        self.player.pos = pos

        if activate_step_in:
            step_in_block = self.get_block(self.player.pos)
            if step_in_block is not None:
                step_in_block.on_step_in()

    def find_level_entrance(self, level_index):
        if level_index is None:
            return None

        for lay in self.layers:
            for arr in lay.grid:
                for blo in arr:
                    if type(blo) is o.block_entrance and blo.target_level == level_index:
                        return blo.pos
        return None

    def fill(self, filename, last_level_index=None):
        log.info("loading level from: " + filename)

        try:
            f = open(filename)
            self.x = int(f.readline())
            self.y = int(f.readline())
            self.z = int(f.readline())
            self.player = player((0, 0, 0), self.screen, self.stage, self.state_index)

            blocks = {}

            for i in range(self.z):
                new_layer = layer(self.x, self.y, self.screen, self.stage, self.state_index)

                for j in range(self.y):
                    line = f.readline()
                    if line[-1] == '\n':
                        line = line[:-1]
                    if len(line) != self.x:
                        log.error("Missing or excessive chars in level " + filename)
                        return False

                    for k in range(self.x):
                        char = line[k]
                        try:
                            obj = charmap[char]
                        except KeyError:
                            log.error("Key error: " + str(char))
                            return False

                        blo = obj(self.screen, self.stage, self.state_index, (k, j, i))

                        if obj == o.block_start:
                            self.teleport_player((k, j, i), False)
                        if obj == o.block_numeric:
                            blo.options(str(char))
                        if obj == o.block_arrow:
                            blo.options(str(char))
                        if obj == o.block_jump:
                            blo.options(2)
                        if obj == o.block_lamp:
                            if char == 'B':
                                blo.change_state()

                        if obj not in blocks:
                            blocks[obj] = []
                        blocks[obj].append(blo)

                        new_layer.update(k, j, blo)

                self.layers.append(new_layer)
                f.readline()

            options = {}
            line = f.readline()
            while len(line) > 2:
                line = line.split()
                options[line[0]] = line[1:]
                line = f.readline()
            f.close()

            option_map = {
                o.block_portal: 'portals',
                o.block_jump: 'jumps',
                o.block_entrance: 'entrances',
                o.block_map_bridge: 'map_bridges',
                o.block_ones: 'ones',
            }

            for key, value in blocks.items():
                if key in option_map:
                    log.info("Configuring: " + option_map[key])

                    if option_map[key] not in options:
                        log.warning("No " + option_map[key] + " options")
                        continue

                    current_options = options[option_map[key]]

                    if len(current_options) != len(value):
                        log.warning("Wrong length " + option_map[key] + " options")

                    if option_map[key] == 'portals':
                        for i in range(len(value)):
                            value[i].set_destination(value[int(current_options[i])])
                    else:
                        for i in range(len(value)):
                            value[i].options(current_options[i])

            starting_point = self.find_level_entrance(last_level_index)
            if starting_point is not None:
                self.teleport_player(starting_point, False)
            return True
        except:
            log.error("Undefined error while loading stage")
            traceback.print_exc()
            return False
