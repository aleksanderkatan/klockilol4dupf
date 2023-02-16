import src.imports.all_sprites as s


class chav:
    def __init__(self, screen, stage, state_index, pos):
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.sprite = s.sprites["chav"]
        self.pos = pos

    def move(self):
        player = self.stage.states[self.state_index].player
        if self.pos == player.pos:
            player.dead = True
        mx, my, mz = self.pos
        px, py, pz = player.pos

        if mz != pz:
            mz += abs((pz - mz)) / (pz - mz)
        elif my != py:
            my += abs((py - my)) / (py - my)
        elif mx != px:
            mx += abs((px - mx)) / (px - mx)
        self.pos = (mx, my, mz)
        if self.pos == player.pos:
            player.dead = True

    def copy(self, new_state_index):
        return chav(self.screen, self.stage, new_state_index, self.pos)

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], pos)
