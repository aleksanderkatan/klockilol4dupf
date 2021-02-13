import game_files.all_sprites as s
import numpy as np
import random

class particle:
    def __init__(self, screen, pos):
        self.screen = screen
        self.sprite = s.sprites["particle_" + str(random.randint(1, 3))].copy()
        self.pos = pos
        self.vel = random.randint(5, 25)
        self.angle = random.randint(0, 359)
        self.alpha = 255

    def update_alpha(self):
        self.alpha = max(self.alpha-8, 0)
        self.sprite.set_alpha(self.alpha)

    def update_vel(self):
        self.vel = self.vel*0.8

    def update_pos(self):
        dy = self.vel * np.sin(self.angle)
        dx = self.vel * np.cos(self.angle)
        x, y = self.pos
        self.pos = (x+dx, y+dy)

    def step(self):
        self.update_vel()
        self.update_pos()
        self.update_alpha()

    def draw(self):
        self.screen.blit(self.sprite, self.pos)


class particle_generator:
    def __init__(self, screen):
        self.screen = screen
        self.particles = []

    def draw(self):
        for par in self.particles:
            par.draw()

    def generate(self, amount, pos):
        for i in range(amount):
            self.particles.append(particle(self.screen, pos))

    def step(self):
        clear = False
        for i in range(len(self.particles)):
            self.particles[i].step()
            if self.particles[i].alpha == 0:
                clear = True

        if clear:
            new_particles = []
            for par in self.particles:
                if par.alpha != 0:
                    new_particles.append(par)
            self.particles = new_particles

    def reset(self):
        self.particles = []
