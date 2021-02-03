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
        self.player.set_next_move_direction(direction) #if something is enqueued, this will be ignored
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
            portals = []
            jumps = []
            entrances = []
            map_bridges = []
            ones = []

            for i in range(self.z):
                new_layer = layer(self.x, self.y, self.screen, self.stage, self.state_index)

                for j in range(self.y):
                    line = f.readline()
                    if len(line) != self.x+1: # !! \n at the end
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
                            blo.set_number(int(char) - int('0'))
                        if obj == o.block_arrow:
                            blo.set_direction(u.char_to_direction(char))
                        if obj == o.block_jump:
                            blo.set_boost(2)
                            jumps.append(blo)
                        if obj == o.block_portal:
                            portals.append(blo)
                        if obj == o.block_lamp:
                            if char == 'B':
                                blo.change_state()
                        if obj == o.block_entrance:
                            entrances.append(blo)
                        if obj == o.block_map_bridge:
                            map_bridges.append(blo)
                        if obj == o.block_ones:
                            ones.append(blo)

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

            if 'portals' in options:
                log.info("Configuring portals")
                portal_options = options['portals']
                if len(portal_options) != len(portals):
                    log.warning("Wrong amount of portal options")
                    return False
                for i in range(len(portals)):
                    portals[i].destination = portals[int(portal_options[i])]
            elif len(portals) != 0:
                log.warning("No portal options")

            if 'jumps' in options:
                log.info("Configuring jumps")
                jump_options = options['jumps']
                if len(jump_options) != len(jumps):
                    log.warning("Wrong amount of jumps options")
                for i in range(len(jump_options)):
                    jumps[i].set_boost(int(jump_options[i]))
            elif len(jumps):
                log.warning("No jump options")

            if 'entrances' in options:
                log.info("Configuring entrances")
                entrance_options = options["entrances"]
                if len(entrance_options) != len(entrances):
                    log.warning("Wrong amount of entrances options")
                for i in range(len(entrance_options)):
                    target_level = entrance_options[i].split('/')
                    target_level = (int(target_level[0]), int(target_level[1]))
                    entrances[i].set_target_level(target_level)
            elif len(entrances) != 0:
                log.warning("No entrance options")

            if 'map_bridges' in options:
                log.info("Configuring map bridges")
                map_bridge_options = options["map_bridges"]
                if len(map_bridge_options) != len(map_bridges):
                    log.warning("Wrong amount of map bridges options")
                for i in range(len(map_bridge_options)):
                    map_bridges[i].set_level_set(int(map_bridge_options[i]))
            elif len(map_bridges) != 0:
                log.warning("No map bridges options")

            if 'ones' in options:
                log.info("Configuring ones")
                ones_options = options['ones']
                if len(ones_options) != len(ones):
                    log.warning("Wrong amount of ones options")
                for i in range(len(ones_options)):
                    ones[i].set_ones(int(ones_options[i]))
            elif len(ones) != 0:
                log.warning("No ones options")

            starting_point = self.find_level_entrance(last_level_index)
            if starting_point is not None:
                self.teleport_player(starting_point, False)
            return True
        except:
            log.error("Undefined error while loading stage")
            return False
