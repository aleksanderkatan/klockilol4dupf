import pygame
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v
import os

path = "game_files/sprites/"
blocks_path = path + ("blocks/" if not g.THREED else "blocks_3d/")
backgrounds_path = path + "backgrounds/"
other_path = path + "other/"
alphas = {-3: 64, -2: 96, -1: 128, 0: 255, 1: 64, 2: 48, 3: 32}


block_sprites = {}
background_sprites = {}
sprites = {}

# BLOCK_SPRITES (block is everything that needs alpha versions)

for path, _, files in os.walk(blocks_path):
    for name in files:
        block_sprites[name[:-4]] = pygame.image.load(os.path.join(path, name)).convert()

block_sprites["block_invisible"] = block_sprites["block"].copy()

for name, sprite in block_sprites.items():
    if name in ["level_available", "level_unavailable"]:  # has to have alphas
        new_sprite = pygame.transform.smoothscale(
            sprite, (int(v.BLOCK_X_SIZE * v.LEVEL_COMPLETION_SCALE), int(v.BLOCK_Y_SIZE * v.LEVEL_COMPLETION_SCALE))
        )
    else:
        new_sprite = pygame.transform.scale(sprite, (v.BLOCK_X_SIZE, v.BLOCK_Y_SIZE + (0 if not g.THREED else v.BLOCK_3D_DIFFERENCE)))

    sprites[name] = {}

    for key, value in alphas.items():
        s = new_sprite.copy()
        alpha = s.get_alpha()
        alpha = 255 if alpha is None else alpha
        alpha = int(alpha * value/255)
        s.set_alpha(alpha)
        sprites[name][key] = s

# BACKGROUND SPRITES

for path, _, files in os.walk(backgrounds_path):
    for name in files:
        background_sprites[name[:-4]] = pygame.image.load(os.path.join(path, name)).convert()


background_sprites["background_grayness"] = background_sprites["background_black"].copy()
background_sprites["background_grayness"].set_alpha(g.GRAYNESS * 256)
background_sprites["background_black"].set_alpha(192)

for name, sprite in background_sprites.items():
    sprites[name] = pygame.transform.scale(sprite, (v.WINDOW_X, v.WINDOW_Y))

# OTHER SPRITES

sprites["particle_1"] = pygame.image.load(other_path + 'particle_1.gif').convert()
sprites["particle_2"] = pygame.image.load(other_path + 'particle_2.gif').convert()
sprites["particle_3"] = pygame.image.load(other_path + 'particle_3.gif').convert()
