import pygame
import random
from src.imports.all_sprites import sprites as s
from src.animations.animation import animation
from src.imports.view_constants import global_view_constants as v


class animation_spinning_dog(animation):
    def __init__(self, screen):
        self.screen = screen
        self.pos = (random.randint(0, v.WINDOW_X), random.randint(0, v.WINDOW_Y))
        self.sprite = s["decoration_1x1_dog"][0].copy()

        self.current_angle = random.randrange(0, 360)
        self.angle_advance = random.randrange(1, 6)

        size_cycle_length = int((2 + random.random()) * v.FRAME_RATE)
        min_size = 0.2 + random.random()
        max_size = 1 + min_size * random.random() * 3
        self.sizes = [min_size + i * (max_size - min_size)/size_cycle_length for i in range(size_cycle_length)]
        self.sizes = self.sizes + list(reversed(self.sizes))
        self.current_size_index = random.randrange(0, len(self.sizes))


    def draw(self):
        scalar = self.sizes[self.current_size_index]
        sprite = pygame.transform.scale(self.sprite, tuple(dim * scalar for dim in self.sprite.get_size()))
        sprite = pygame.transform.rotate(sprite, self.current_angle)
        self.screen.blit(sprite, self.pos)

    def advance(self):
        self.current_angle = (self.current_angle + self.angle_advance) % 360
        self.current_size_index = (self.current_size_index + 1) % len(self.sizes)

    def prevents_logic(self):
        return False

    def has_ended(self):
        return False

    def is_persistent(self):
        return True
