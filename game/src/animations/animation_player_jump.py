from src.animations.animation import animation
from src.animations.animation_jump import animation_jump


class animation_player_jump(animation):
    def __init__(self, screen, stage, state_index, translation, height, duration):
        self.screen = screen
        self.player = stage.states[state_index].player

        self.animation = animation_jump(screen, stage, state_index, self.player.get_current_sprite()[0],
                                        self.player.pos, translation, height, duration)

        self.player.ignore_draw = True

    def draw(self):
        self.animation.draw()

    def advance(self):
        self.animation.advance()
        self.player.ignore_draw = not self.animation.has_ended()

    def prevents_logic(self):
        return True

    def has_ended(self):
        return self.animation.has_ended()

    def is_persistent(self):
        return False
