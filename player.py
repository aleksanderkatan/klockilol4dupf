import import_sprites as s
import utils as u


class player:
    def __init__(self, pos, screen, stage, state_index):
        self.pos = pos
        self.sprite = s.sprites["obj_player"][0]
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.last_move_direction = None
        self.this_move_direction = None
        self.dead = False
        self.enqueued_moves = []
        self.next_move_length = 1

    def draw(self, screen_pos):
        self.screen.blit(self.sprite, screen_pos)

    def copy(self, new_state_index):
        pla = player(self.pos, self.screen, self.stage, new_state_index)
        pla.last_move_direction = self.last_move_direction
        pla.this_move_direction = self.this_move_direction
        pla.dead = self.dead
        pla.enqueued_moves = []
        pla.next_move_length = self.next_move_length
        for i in range(len(self.enqueued_moves)):
            pla.enqueued_moves.append(self.enqueued_moves[i])
        return pla

    def enqueue_move(self, direction):
        if direction is None:
            return
        self.enqueued_moves.append(direction)

    def boost_next_move(self, amount):
        self.next_move_length = amount

    def set_next_move_direction(self, direction_suggestion):
        if len(self.enqueued_moves) > 0:
            direction = self.enqueued_moves[0]
            self.enqueued_moves = self.enqueued_moves[1:]
            self.this_move_direction = direction
        else:
            self.this_move_direction = direction_suggestion
        
    def move(self): #!!set_next_move_direction must be called first
        x, y, z = self.pos
        move_length = self.next_move_length
        move_direction = self.this_move_direction

        if move_direction == 0:
            x += move_length
        elif move_direction == 1:
            y -= move_length
        elif move_direction == 2:
            x -= move_length
        else:
            y += move_length

        self.next_move_length = 1
        self.last_move_direction = move_direction
        self.this_move_direction = None
        while z >= 0 and not self.stage.states[self.state_index].standable((x, y, z)):
            z -= 1
            self.last_move_direction = None
        if z < 0:
            self.dead = True
        self.pos = (x, y, z)

    def has_something_enqueued(self):
        return len(self.enqueued_moves) != 0
