import src.imports.all_blocks as o
import src.imports.all_sprites as s
import src.imports.globals as g
import src.imports.utils as u
from src.logic.direction import direction as d


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
        self.decorations = []
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
        decorations = []
        for decoration in self.decorations:
            decorations.append(decoration.copy(new_state_index))
        sta.decorations = decorations
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
            self.player.enqueue_move(d.FORCED_SKIP)

        step_out_block = self.get_block(self.player.pos)
        if step_out_block is not None and direction != d.FORCED_SKIP:
            step_out_block.on_step_out()

        self.player.move()

        self.update_dark_visibility()

        if g.KBcheat and g.save_state.get_preference("cheats"):
            return

        # if not self.player.has_something_enqueued():
        for chav in self.chavs:
            chav.move()

        new_bombs = []
        for bomb in self.bombs:
            bomb.move()
            if not bomb.finished:
                new_bombs.append(bomb)
        self.bombs = new_bombs

        step_in_block = self.get_block(self.player.pos)
        if step_in_block is not None and direction != d.FORCED_SKIP:
            if type(step_in_block) in o.standables:
                self.player.flight = -1
            step_in_block.on_step_in()

    def draw(self):  # !! update so that blocks from layer 2 overlap bombs and other stuff from layer 1
        # or not...
        for i in range(len(self.layers)):
            self.layers[i].draw(i, len(self.layers), u.relative_to_player(i, self.player.pos[2]))
        for decoration in self.decorations:
            x, y = u.index_to_position(decoration.pos[0], decoration.pos[1], decoration.pos[2], self.x, self.y,
                                       len(self.layers))
            decoration.draw((x, y), u.relative_to_player(decoration.pos[2], self.player.pos[2]))
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
            self.screen.blit(s.sprites['background_you_died'], (0, 0))

    def draw_one_layer(self, layer_index):  # !! can't be used above
        if self.player.dead or layer_index >= len(self.layers):
            self.draw()
            return

        self.layers[layer_index].draw(layer_index, len(self.layers), 0)
        for decoration in self.decorations:
            x, y, z = decoration.pos
            if z != layer_index:
                continue
            screen_pos = u.index_to_position(x, y, z, self.x, self.y, len(self.layers))
            decoration.draw(screen_pos, 0)
        for pusher in self.pushers:
            x, y, z = pusher.pos
            if z != layer_index:
                continue
            screen_pos = u.index_to_position(pusher.pos[0], pusher.pos[1], pusher.pos[2], self.x, self.y,
                                             len(self.layers))
            pusher.draw(screen_pos)
        for chav in self.chavs:
            x, y, z = chav.pos
            if z != layer_index:
                continue
            screen_pos = u.index_to_position(chav.pos[0], chav.pos[1], chav.pos[2], self.x, self.y, len(self.layers))
            chav.draw(screen_pos, u.relative_to_player(chav.pos[2], self.player.pos[2]))
        for bomb in self.bombs:
            x, y, z = bomb.pos
            if z != layer_index:
                continue
            screen_pos = u.index_to_position(bomb.pos[0], bomb.pos[1], bomb.pos[2], self.x, self.y, len(self.layers))
            bomb.draw(screen_pos, u.relative_to_player(bomb.pos[2], self.player.pos[2]))

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
        if u.out_of_range_3(pos, self.get_size()):
            return False
        if type(self.get_block(pos)) in o.standables:
            return True
        return False

    def has_barrier(self, pos, direction):
        if g.KBcheat and g.save_state.get_preference("cheats"):
            return False
        if not direction.is_cardinal():
            return False
        pos2 = u.move_pos(pos, direction)
        blo1 = self.get_block(pos)
        blo2 = self.get_block(pos2)

        if blo1 is None and blo2 is None:
            return False
        if blo2 is None:
            return blo1.has_barrier(direction, False)
        if blo1 is None:
            return blo2.has_barrier(u.reverse_direction(direction), True)
        return blo1.has_barrier(direction, False) or blo2.has_barrier(u.reverse_direction(direction), True)

    def get_block(self, pos):
        x, y, z = pos
        if u.out_of_range_3(pos, self.get_size()):
            return None
        return self.layers[z].grid[x][y]

    def set_block(self, pos, block):
        x, y, z = pos
        if u.out_of_range_3(pos, self.get_size()):
            return
        self.layers[z].grid[x][y] = block
        block.pos = pos

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

        for blo in self.block_iterator():
            if (issubclass(type(blo), o.block_entrance) or issubclass(type(blo), o.block_entrance_random)) \
                    and blo.get_target_level() == level_index:
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
