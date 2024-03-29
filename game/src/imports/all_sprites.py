import os

import pygame

import src.imports.globals as g
from src.imports.view_constants import global_view_constants as v
from src.logic.modes.text_display_utils import create_text_surfaces

path = "src/sprites/"
blocks_path = path + ("blocks/" if not g.THREED else "blocks_3d/")
backgrounds_path = path + "backgrounds/"
decorations_path = path + "decorations/"
other_path = path + "other/"
alphas = {-3: 64, -2: 96, -1: 128, 0: 255, 1: 64, 2: 48, 3: 32}

sprites = {}

# BLOCK_SPRITES (block is everything that needs alpha versions)
block_sprites = {}

for path, _, files in os.walk(blocks_path):
    for name in files:
        block_sprites[name[:-4]] = pygame.image.load(os.path.join(path, name)).convert()

block_sprites["block_invisible"] = block_sprites["block"].copy()

for name, sprite in block_sprites.items():
    if name in ["level_completed", "level_skipped", "level_unavailable"]:  # has to have alphas
        new_sprite = pygame.transform.smoothscale(
            sprite, (int(v.BLOCK_X_SIZE * v.LEVEL_COMPLETION_SCALE), int(v.BLOCK_Y_SIZE * v.LEVEL_COMPLETION_SCALE))
        )
    else:
        new_sprite = pygame.transform.scale(sprite, (
            v.BLOCK_X_SIZE, v.BLOCK_Y_SIZE + (0 if not g.THREED else v.BLOCK_3D_DIFFERENCE)))

    sprites[name] = {}

    for key, value in alphas.items():
        s = new_sprite.copy()
        alpha = s.get_alpha()
        alpha = 255 if alpha is None else alpha
        alpha = int(alpha * value / 255)
        s.set_alpha(alpha)
        sprites[name][key] = s

# BACKGROUND SPRITES
background_sprites = {}

for path, _, files in os.walk(backgrounds_path):
    for name in files:
        background_sprites[name[:-4]] = pygame.image.load(os.path.join(path, name)).convert()

background_sprites["background_blacker"] = background_sprites["background_black"].copy()
background_sprites["background_blacker"].set_alpha(224)
background_sprites["background_black"].set_alpha(192)
background_sprites["background_grayness"] = background_sprites["background_black"].copy()
background_sprites["background_grayness"].set_alpha(v.GRAYNESS * 256)

for name, sprite in background_sprites.items():
    sprites[name] = pygame.transform.scale(sprite, (v.WINDOW_X, v.WINDOW_Y))

# DECORATION SPRITES
decoration_sprites = {}

for path, _, files in os.walk(decorations_path):
    for name in files:
        decoration_sprites[name[:-4]] = pygame.image.load(os.path.join(path, name)).convert()

rescale_x, rescale_y = v.get_decoration_rescale()

for name, sprite in decoration_sprites.items():
    sprites[name] = {}

    arr = name.split("_")
    sizes = arr[1].split("x")
    x = int(sizes[0]) * v.BLOCK_X_SIZE
    y = int(sizes[1]) * v.BLOCK_Y_SIZE

    new_sprite = pygame.transform.scale(sprite, (x, y))
    for key, value in alphas.items():
        s = new_sprite.copy()
        alpha = s.get_alpha()
        alpha = 255 if alpha is None else alpha
        alpha = int(alpha * value / 255)
        s.set_alpha(alpha)
        sprites[name][key] = s

# OTHER SPRITES

sprites["particle_1"] = pygame.image.load(other_path + 'particle_1.gif').convert()
sprites["particle_2"] = pygame.image.load(other_path + 'particle_2.gif').convert()
sprites["particle_3"] = pygame.image.load(other_path + 'particle_3.gif').convert()

sprites["particle_star_1"] = pygame.image.load(other_path + 'particle_star_1.gif').convert()
sprites["particle_star_2"] = pygame.image.load(other_path + 'particle_star_2.gif').convert()
sprites["particle_star_3"] = pygame.image.load(other_path + 'particle_star_3.gif').convert()


