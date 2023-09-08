from src.animations.text_message import text_message


class animation_manager:
    def __init__(self):
        self.anims = []
        self.message = None

    def register_message(self, screen, message, lifetime):
        if lifetime < 0:
            lifetime = 10**10
        self.message = text_message(screen, message, lifetime)

    def register_animation(self, anim):
        self.anims.append(anim)

    def draw_and_advance(self):
        # anims
        continued_anims = []
        for anim in self.anims:
            anim.draw()
            anim.advance()
            if not anim.has_ended():
                continued_anims.append(anim)
        self.anims = continued_anims
        # message
        if self.message is not None:
            self.message.draw()
            self.message.advance()
            if self.message.has_ended():
                self.message = None

    def is_logic_prevented(self):
        return True in [anim.prevents_logic() for anim in self.anims]

    def reset(self):
        continued_anims = []
        for anim in self.anims:
            if anim.is_persistent():
                continued_anims.append(anim)
        self.anims = continued_anims
