from src.animations.animation import animation


class chained_animation(animation):
    def __init__(self, screen, animations,
                 prevent_logic=False, persistent=False):
        self.screen = screen
        self.animations = animations
        self.current_index = 0
        self.prevent_logic = prevent_logic
        self.persistent = persistent

    def draw(self):
        if self.current_index < len(self.animations):
            self.animations[self.current_index].draw()

    def advance(self):
        if self.has_ended():
            return
        anim = self.animations[self.current_index]
        anim.advance()
        if anim.has_ended():
            self.current_index += 1

    def prevents_logic(self):
        return self.prevent_logic

    def has_ended(self):
        return self.current_index >= len(self.animations)

    def is_persistent(self):
        return self.persistent

