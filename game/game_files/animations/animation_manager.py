# from game_files.animations import animation

class animation_manager:
    def __init__(self):
        self.anims = []

    def register_animation(self, anim):
        self.anims.append(anim)

    def draw_and_advance(self):
        continued_anims = []
        for anim in self.anims:
            anim.draw()
            anim.advance()
            if not anim.has_ended():
                continued_anims.append(anim)
        self.anims = continued_anims

    def is_logic_prevented(self):
        return True in [anim.prevents_logic() for anim in self.anims]

    def reset(self):
        continued_anims = []
        for anim in self.anims:
            if anim.is_persistent():
                continued_anims.append(anim)
        self.anims = continued_anims
