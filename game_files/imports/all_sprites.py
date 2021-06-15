import pygame
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v
import os

path = "game_files/sprites/"
blocks_path = path + ("blocks/" if not g.THREED else "blocks_3d/")
backgrounds_path = path + "backgrounds/"
other_path = path + "other/"


block_sprites = {}
background_sprites = {}

sprites = {}

# BLOCK_SPRITES (block is everything that needs alpha versions)

for path, _, files in os.walk(blocks_path):
    for name in files:
        print(name)
        block_sprites[name[:-4]] = pygame.image.load(os.path.join(path, name)).convert()

block_sprites["block_invisible"] = block_sprites["block"]

alphas = {-3: 64, -2: 96, -1: 128, 0: 255, 1: 64, 2: 48, 3: 32}

for name, sprite in block_sprites.items():
    if name in ["level_available", "level_unavailable"]:  # has to have alphas
        new_sprite = pygame.transform.smoothscale(
            sprite, (int(v.BLOCK_X_SIZE * v.LEVEL_COMPLETION_SCALE), int(v.BLOCK_Y_SIZE * v.LEVEL_COMPLETION_SCALE))
        )
    else:
        new_sprite = pygame.transform.scale(sprite, (v.BLOCK_X_SIZE, v.BLOCK_Y_SIZE + 0))

    sprites[name] = {}

    for key, value in alphas.items():
        s = new_sprite.copy()
        alpha = s.get_alpha()
        alpha = 255 if alpha is None else alpha
        alpha = int(alpha * value/255)
        s.set_alpha(alpha)
        sprites[name][key] = s

# BACKGROUND SPRITES

background_sprites["background"] = pygame.image.load(backgrounds_path + 'background.gif').convert()
background_sprites["kono_dio_da"] = pygame.image.load(backgrounds_path + 'kono_dio_da.gif').convert()
background_sprites["you_died"] = pygame.image.load(backgrounds_path + 'you_died.gif').convert()
background_sprites["black"] = pygame.image.load(backgrounds_path + 'black.gif').convert()
background_sprites["black"].set_alpha(192)
background_sprites["witch"] = pygame.image.load(backgrounds_path + 'witch.gif')
background_sprites["duda_chuj"] = pygame.image.load(backgrounds_path + 'background_duda_chuj.gif').convert()
background_sprites["grayness"] = pygame.image.load(backgrounds_path + 'black.gif').convert()
background_sprites["grayness"].set_alpha(g.GRAYNESS * 256)
background_sprites["swamp"] = pygame.image.load(backgrounds_path + 'swamp.gif').convert()
background_sprites["Giszowiec_1"] = pygame.image.load(backgrounds_path + 'giszowiec_1.gif').convert()
background_sprites["Giszowiec_2"] = pygame.image.load(backgrounds_path + 'giszowiec_2.gif').convert()
background_sprites["Giszowiec_3"] = pygame.image.load(backgrounds_path + 'giszowiec_3.gif').convert()

for name, sprite in background_sprites.items():
    sprites[name] = pygame.transform.scale(sprite, (v.WINDOW_X, v.WINDOW_Y))

sprites["particle_1"] = pygame.image.load(other_path + 'particle_1.gif').convert()
sprites["particle_2"] = pygame.image.load(other_path + 'particle_2.gif').convert()
sprites["particle_3"] = pygame.image.load(other_path + 'particle_3.gif').convert()
