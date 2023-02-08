import game_files.imports.all_sprites as s
from game_files.imports.view_constants import global_view_constants as v
import numpy as np
import random


class particle:
    def __init__(self, screen, pos, sprite):
        self.screen = screen
        self.sprite = sprite.copy()
        self.pos = pos
        self.vel = random.randint(5, 25)
        self.angle = random.uniform(0, np.pi * 2)
        self.alpha = 255
        self.acc = 0.8
        self.alpha_dec = 8
        self.lifetime = 100

    def update_alpha(self):
        self.alpha = max(self.alpha - self.alpha_dec, 0)
        self.sprite.set_alpha(self.alpha)

    def update_vel(self):
        self.vel = self.vel * self.acc

    def update_pos(self):
        dy = self.vel * np.sin(self.angle)
        dx = self.vel * np.cos(self.angle)
        x, y = self.pos
        self.pos = (x + dx, y - dy)

    def step(self):
        self.update_vel()
        self.update_pos()
        self.update_alpha()
        self.lifetime -= 1

    def draw(self):
        self.screen.blit(self.sprite, self.pos)


class particle_generator:
    def __init__(self, screen):
        self.screen = screen
        self.particles = []

    def draw(self):
        for par in self.particles:
            par.draw()

    def generate_dust(self, amount, pos):
        for i in range(amount):
            self.particles.append(particle(self.screen, pos, s.sprites["particle_" + str(random.randint(1, 3))]))

    def generate_stars(self, amount, pos):
        for _ in range(amount):
            self.particles.append(particle(self.screen, pos, s.sprites["particle_star_" + str(random.randint(1, 3))]))

    def generate_bomb(self, pos, player_direction):
        par = particle(self.screen, pos, s.sprites["bomb"])
        par.alpha_dec = 0
        par.vel = 32 * v.X_SCALE
        par.acc = 1
        par.angle = random.uniform(0, np.pi / 2) - np.pi / 4 + np.pi / 2 * player_direction.value
        par.sprite = s.sprites["bomb"][0]
        self.particles.append(par)

    def step(self):
        clear_needed = False
        for i in range(len(self.particles)):
            self.particles[i].step()
            if self.particles[i].lifetime == 0:
                clear_needed = True

        if clear_needed:
            new_particles = []
            for par in self.particles:
                if par.alpha != 0:
                    new_particles.append(par)
            self.particles = new_particles

    def reset(self):
        self.particles = []
