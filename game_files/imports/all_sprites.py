import pygame
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v

directed_block_sprites = {}
numeric_block_sprites = {}
block_sprites = {}
background_sprites = {}

sprites = {}

dimmer = pygame.image.load('game_files/sprites/blocks/black_block.gif')

# DIRECTED_BLOCK_SPRITES

directed_block_sprites["block_arrow_"] = pygame.image.load('game_files/sprites/blocks/arrow.gif').convert()
directed_block_sprites["ones_one_"] = pygame.image.load('game_files/sprites/blocks/ones_one.gif').convert()
directed_block_sprites["block_piston_"] = pygame.image.load('game_files/sprites/blocks/piston.gif').convert()
directed_block_sprites["pusher_"] = pygame.image.load('game_files/sprites/pusher.gif').convert()
directed_block_sprites["block_dual_arrow_"] = pygame.image.load('game_files/sprites/blocks/dual_arrow.gif').convert()
directed_block_sprites["block_birdy_arrow_"] = pygame.image.load('game_files/sprites/blocks/birdy_arrow.gif').convert()

for name, sprite in directed_block_sprites.items():
    block_sprites[name + "0"] = sprite.copy()
    block_sprites[name + "1"] = sprite.copy()
    block_sprites[name + "2"] = sprite.copy()
    block_sprites[name + "3"] = sprite.copy()
    block_sprites[name + "1"] = pygame.transform.rotate(block_sprites[name + "1"], 90)
    block_sprites[name + "2"] = pygame.transform.rotate(block_sprites[name + "2"], 180)
    block_sprites[name + "3"] = pygame.transform.rotate(block_sprites[name + "3"], 270)

# NUMERIC_BLOCK_SPRITES

numeric_block_sprites["block_numeric_1"] = pygame.image.load('game_files/sprites/blocks/1.gif').convert()
numeric_block_sprites["block_numeric_2"] = pygame.image.load('game_files/sprites/blocks/2.gif').convert()
numeric_block_sprites["block_numeric_3"] = pygame.image.load('game_files/sprites/blocks/3.gif').convert()
numeric_block_sprites["block_numeric_4"] = pygame.image.load('game_files/sprites/blocks/4.gif').convert()
numeric_block_sprites["block_numeric_5"] = pygame.image.load('game_files/sprites/blocks/5.gif').convert()
numeric_block_sprites["block_numeric_6"] = pygame.image.load('game_files/sprites/blocks/6.gif').convert()
numeric_block_sprites["block_numeric_7"] = pygame.image.load('game_files/sprites/blocks/7.gif').convert()
numeric_block_sprites["block_numeric_8"] = pygame.image.load('game_files/sprites/blocks/8.gif').convert()

for name, sprite in numeric_block_sprites.items():
    block_sprites[name] = sprite.copy()
    s = sprite.copy()
    s.fill((64, 64, 64, 255), special_flags=pygame.BLEND_RGBA_SUB)
    s = pygame.transform.flip(s, True, False)
    block_sprites[name + "_dark"] = s
    s = s.copy()
    s.set_alpha(64)
    block_sprites[name + "_invisible_dark"] = s

# BLOCK_SPRITES

block_sprites["block"] = pygame.image.load('game_files/sprites/blocks/0.gif').convert()
block_sprites["block_start"] = pygame.image.load('game_files/sprites/blocks/start.gif').convert()
block_sprites["block_end"] = pygame.image.load('game_files/sprites/blocks/end.gif').convert()
block_sprites["error"] = pygame.image.load('game_files/sprites/blocks/error.gif').convert()
block_sprites["block_ice"] = pygame.image.load('game_files/sprites/blocks/ice.gif').convert()
block_sprites["block_jump_2"] = pygame.image.load('game_files/sprites/blocks/jump2.gif').convert()
block_sprites["block_lift"] = pygame.image.load('game_files/sprites/blocks/lift.gif').convert()
block_sprites["player"] = pygame.image.load('game_files/sprites/player.gif').convert()
block_sprites["player_shrek"] = pygame.image.load('game_files/sprites/player_shrek.gif').convert()
block_sprites["block_portal"] = pygame.image.load('game_files/sprites/blocks/portal.gif').convert()
block_sprites["block_dummy"] = pygame.image.load('game_files/sprites/blocks/dummy.gif').convert()
block_sprites["block_lamp_on"] = pygame.image.load('game_files/sprites/blocks/lamp_on.gif').convert()
block_sprites["block_lamp_off"] = pygame.image.load('game_files/sprites/blocks/lamp_off.gif').convert()
block_sprites["block_bridge"] = pygame.image.load('game_files/sprites/blocks/bridge.gif').convert()
block_sprites["block_entrance_hub"] = pygame.image.load('game_files/sprites/blocks/entrance_hub.gif').convert()
block_sprites["block_entrance_zone"] = pygame.image.load('game_files/sprites/blocks/entrance_zone.gif').convert()
block_sprites["block_entrance_level"] = pygame.image.load('game_files/sprites/blocks/entrance_level.gif').convert()
block_sprites["level_available"] = pygame.image.load('game_files/sprites/level_available.gif').convert()
block_sprites["level_unavailable"] = pygame.image.load('game_files/sprites/level_unavailable.gif').convert()
block_sprites["block_map_bridge_off"] = pygame.image.load('game_files/sprites/blocks/map_bridge_off.gif').convert()
block_sprites["block_map_bridge_on"] = pygame.image.load('game_files/sprites/blocks/map_bridge_on.gif').convert()
block_sprites["block_ones"] = pygame.image.load('game_files/sprites/blocks/ones.gif').convert()
block_sprites["block_jump_3"] = pygame.image.load('game_files/sprites/blocks/jump3.gif').convert()
block_sprites["block_blocker"] = pygame.image.load('game_files/sprites/blocks/blocker.gif').convert()
block_sprites["block_thunder"] = pygame.image.load('game_files/sprites/blocks/thunder.gif').convert()
block_sprites["block_pink"] = pygame.image.load('game_files/sprites/blocks/pink.gif').convert()
block_sprites["block_orange"] = pygame.image.load('game_files/sprites/blocks/orange.gif').convert()
block_sprites["block_yellow"] = pygame.image.load('game_files/sprites/blocks/yellow.gif').convert()
block_sprites["flavour_orange"] = pygame.image.load('game_files/sprites/flavour_orange.gif').convert()
block_sprites["flavour_lemon"] = pygame.image.load('game_files/sprites/flavour_lemon.gif').convert()
block_sprites["block_reset"] = pygame.image.load('game_files/sprites/blocks/reset.gif').convert()
block_sprites["chav"] = pygame.image.load('game_files/sprites/chav.gif').convert()
block_sprites["block_invisible"] = pygame.image.load('game_files/sprites/blocks/0.gif').convert()
block_sprites["bomb"] = pygame.image.load('game_files/sprites/bomb.gif').convert()
block_sprites["block_fragile_start"] = pygame.image.load('game_files/sprites/blocks/fragile_start.gif')
block_sprites["block_fragile_end"] = pygame.image.load('game_files/sprites/blocks/fragile_end.gif')
block_sprites["block_plus"] = pygame.image.load('game_files/sprites/blocks/plus.gif')
block_sprites["block_minus"] = pygame.image.load('game_files/sprites/blocks/minus.gif')

if g.THREED:
    alphas = {-3: 255, -2: 255, -1: 255, 0: 255, 1: 64, 2: 48, 3: 32}
else:
    alphas = {-3: 64, -2: 96, -1: 128, 0: 255, 1: 64, 2: 48, 3: 32}

for name, sprite in block_sprites.items():
    if name in ["level_available", "level_unavailable"]:  # has to have alphas
        new_sprite = pygame.transform.smoothscale(
            sprite, (int(v.BLOCK_X_SIZE * v.LEVEL_COMPLETION_SCALE), int(v.BLOCK_Y_SIZE * v.LEVEL_COMPLETION_SCALE))
        )
    else:
        new_sprite = pygame.transform.scale(sprite, (v.BLOCK_X_SIZE, v.BLOCK_Y_SIZE))

    sprites[name] = {}

    for key, value in alphas.items():
        s = new_sprite.copy()
        alpha = s.get_alpha()
        alpha = 255 if alpha is None else alpha
        alpha = int(alpha * value/255)
        s.set_alpha(alpha)
        sprites[name][key] = s

# BACKGROUND SPRITES

background_sprites["background"] = pygame.image.load('game_files/sprites/background.jpg').convert()
background_sprites["kono_dio_da"] = pygame.image.load('game_files/sprites/kono_dio_da.jpg').convert()
background_sprites["you_died"] = pygame.image.load('game_files/sprites/you_died.jpg').convert()
background_sprites["black"] = pygame.image.load('game_files/sprites/black.jpg').convert()
background_sprites["black"].set_alpha(192)
background_sprites["witch"] = pygame.image.load('game_files/sprites/witch.png')
background_sprites["duda_chuj"] = pygame.image.load('game_files/sprites/background_duda_chuj.png').convert()
background_sprites["grayness"] = pygame.image.load('game_files/sprites/black.jpg').convert()
background_sprites["grayness"].set_alpha(g.GRAYNESS * 256)
background_sprites["swamp"] = pygame.image.load('game_files/sprites/swamp.jpg').convert()
background_sprites["Giszowiec_1"] = pygame.image.load('game_files/sprites/giszowiec_1.jpg').convert()
background_sprites["Giszowiec_2"] = pygame.image.load('game_files/sprites/giszowiec_2.jpg').convert()
background_sprites["Giszowiec_3"] = pygame.image.load('game_files/sprites/giszowiec_3.jpg').convert()

for name, sprite in background_sprites.items():
    sprites[name] = pygame.transform.scale(sprite, (v.WINDOW_X, v.WINDOW_Y))

sprites["particle_1"] = pygame.image.load('game_files/sprites/particle_1.bmp').convert()
sprites["particle_2"] = pygame.image.load('game_files/sprites/particle_2.bmp').convert()
sprites["particle_3"] = pygame.image.load('game_files/sprites/particle_3.bmp').convert()
