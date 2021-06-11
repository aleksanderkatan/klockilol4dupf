import traceback
import os
from game_files.logic.layer import layer
from game_files.other.bomb import bomb
from game_files.logic.player import player
from game_files.imports.charmap import charmap
from game_files.other.chav import chav
import game_files.imports.utils as u
import game_files.imports.all_blocks as o
import game_files.imports.all_sprites as s
import game_files.imports.globals as g
from game_files.imports.log import log


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
        self.invalid = False
        self.pushers = []
        self.chavs = []
        self.bombs = []
        self.dark_visibility = 1

    def copy(self, new_state_index):
        sta = state(self.screen, self.stage, new_state_index)
        sta.x = self.x
        sta.y = self.y
        sta.z = self.z
        sta.player = self.player.copy(new_state_index)
        sta.layers = []
        sta.completed = self.completed
        sta.invalid = self.invalid
        for lay in self.layers:
            sta.layers.append(lay.copy(new_state_index))
        pushers = []
        for pusher in self.pushers:
            pushers.append(pusher.copy(new_state_index))
        sta.pushers = pushers
        chavs = []
        for chav in self.chavs:
            chavs.append(chav.copy(new_state_index))
        sta.chavs = chavs
        bombs = []
        for bomb in self.bombs:
            bombs.append(bomb.copy(new_state_index))
        sta.bombs = bombs
        sta.dark_visibility = self.dark_visibility
        return sta

    def block_iterator(self):
        for l in self.layers:
            for row in l.grid:
                for blo in row:
                    yield blo

    def update_dark_visibility(self):
        for blo in self.block_iterator():
            if issubclass(type(blo), o.block_numeric_dark):
                blo.update_visibility()

    def move(self, direction):  # !!modifies current state instead of returning copy
        self.player.set_next_move_direction(direction)  # if something is enqueued, this will be ignored
        direction = self.player.this_move_direction

        new_pushers = []
        for pusher in self.pushers:
            pusher.move()
            if not pusher.finished:
                new_pushers.append(pusher)
        self.pushers = new_pushers

        if len(self.pushers) > 0 and not self.player.has_something_enqueued():
            self.player.enqueue_move(5)

        step_out_block = self.get_block(self.player.pos)
        if step_out_block is not None and direction != 5:
            step_out_block.on_step_out()

        self.player.move()

        self.update_dark_visibility()

        if g.CHEATS and g.KBcheat:
            return

        if not self.player.has_something_enqueued():
            for chav in self.chavs:
                chav.move()

        new_bombs = []
        for bomb in self.bombs:
            bomb.move()
            if not bomb.finished:
                new_bombs.append(bomb)
        self.bombs = new_bombs

        step_in_block = self.get_block(self.player.pos)
        if step_in_block is not None and direction != 5:
            step_in_block.on_step_in()

    def draw(self):
        for i in range(len(self.layers)):
            self.layers[i].draw(i, len(self.layers), u.relative_to_player(i, self.player.pos[2]))
        for pusher in self.pushers:
            x, y = u.index_to_position(pusher.pos[0], pusher.pos[1], pusher.pos[2], self.x, self.y, len(self.layers))
            pusher.draw((x, y))
        for chav in self.chavs:
            x, y = u.index_to_position(chav.pos[0], chav.pos[1], chav.pos[2], self.x, self.y, len(self.layers))
            chav.draw((x, y), u.relative_to_player(chav.pos[2], self.player.pos[2]))
        for bomb in self.bombs:
            x, y = u.index_to_position(bomb.pos[0], bomb.pos[1], bomb.pos[2], self.x, self.y, len(self.layers))
            bomb.draw((x, y), u.relative_to_player(bomb.pos[2], self.player.pos[2]))

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
        return self.player.has_something_enqueued()

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

    def find_portal(self, index):
        for i in range(self.z):
            for j in range(self.y):
                for k in range(self.x):
                    blo = self.get_block((k, j, i))
                    if type(blo) is o.block_portal:
                        if blo.my_index == index:
                            return blo
        return None

    def fill(self, filename, last_level_index=None):
        log.info("loading level from: " + filename)

        if not os.path.exists(filename):
            log.error("No such file " + str(filename))
            return False

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

                        if issubclass(obj, o.block_start):
                            self.teleport_player((k, j, i), False)
                        if issubclass(obj, o.block_numeric):
                            blo.options(str(char))
                        if issubclass(obj, o.block_arrow):
                            blo.options(str(char))
                        if issubclass(obj, o.block_birdy_arrow):
                            blo.options(str(char))
                        if issubclass(obj, o.block_jump):
                            blo.options(2)
                        if issubclass(obj, o.block_numeric_dark):
                            print(char)
                            blo.options(str(char))
                        if issubclass(obj, o.block_lamp):
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
                o.block_piston: 'pistons',
                o.block_dual_arrow: 'dual_arrows'
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
                            value[i].options(str(i) + " " + current_options[i])
                    else:
                        for i in range(len(value)):
                            value[i].options(current_options[i])

            self.chavs = []
            if 'chavs' in options:
                for option in options['chavs']:
                    pos = option.split('/')
                    x = int(pos[0])
                    y = int(pos[1])
                    z = int(pos[2])
                    self.chavs.append(chav(self.screen, self.stage, self.state_index, (x, y, z)))

            self.bombs = []
            if 'bombs' in options:
                for option in options['bombs']:
                    option = option.split('/')
                    x = int(option[0])
                    y = int(option[1])
                    z = int(option[2])
                    ticks = int(option[3])
                    self.bombs.append(bomb(self.screen, self.stage, self.state_index, (x, y, z), ticks))

            starting_point = self.find_level_entrance(last_level_index)
            if starting_point is not None:
                self.teleport_player(starting_point, False)

            if type(self.get_block(self.player.pos)) not in o.standables:
                log.warning("Player is not standing, finding nearest standable...")
                for blo in self.block_iterator():
                    typ = type(blo)
                    if typ in o.standables and typ != o.block_invisible:
                        self.teleport_player(blo.pos, False)
                        break
            return True
        except:
            log.error("Undefined error while loading stage")
            traceback.print_exc()
            return False