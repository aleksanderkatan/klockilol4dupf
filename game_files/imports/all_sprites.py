import pygame
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v

path = "game_files/sprites/"
blocks_path = path + "blocks/"
backgrounds_path = path + "backgrounds/"
other_path = path + "other/"


directed_block_sprites = {}
numeric_block_sprites = {}
block_sprites = {}
background_sprites = {}

sprites = {}

dimmer = pygame.image.load(blocks_path + 'block_black.gif')

# DIRECTED_BLOCK_SPRITES

directed_block_sprites["block_arrow_"] = pygame.image.load(blocks_path + 'block_arrow.gif').convert()
directed_block_sprites["ones_one_"] = pygame.image.load(blocks_path + 'ones_one.gif').convert()
directed_block_sprites["block_piston_"] = pygame.image.load(blocks_path + 'block_piston.gif').convert()
directed_block_sprites["pusher_"] = pygame.image.load(blocks_path + 'pusher.gif').convert()
directed_block_sprites["block_dual_arrow_"] = pygame.image.load(blocks_path + 'block_dual_arrow.gif').convert()
directed_block_sprites["block_birdy_arrow_"] = pygame.image.load(blocks_path + 'block_birdy_arrow.gif').convert()

for name, sprite in directed_block_sprites.items():
    block_sprites[name + "0"] = sprite.copy()
    block_sprites[name + "1"] = sprite.copy()
    block_sprites[name + "2"] = sprite.copy()
    block_sprites[name + "3"] = sprite.copy()
    block_sprites[name + "1"] = pygame.transform.rotate(block_sprites[name + "1"], 90)
    block_sprites[name + "2"] = pygame.transform.rotate(block_sprites[name + "2"], 180)
    block_sprites[name + "3"] = pygame.transform.rotate(block_sprites[name + "3"], 270)

# NUMERIC_BLOCK_SPRITES

numeric_block_sprites["block_numeric_1"] = pygame.image.load(blocks_path + 'block_numeric_1.gif').convert()
numeric_block_sprites["block_numeric_2"] = pygame.image.load(blocks_path + 'block_numeric_2.gif').convert()
numeric_block_sprites["block_numeric_3"] = pygame.image.load(blocks_path + 'block_numeric_3.gif').convert()
numeric_block_sprites["block_numeric_4"] = pygame.image.load(blocks_path + 'block_numeric_4.gif').convert()
numeric_block_sprites["block_numeric_5"] = pygame.image.load(blocks_path + 'block_numeric_5.gif').convert()
numeric_block_sprites["block_numeric_6"] = pygame.image.load(blocks_path + 'block_numeric_6.gif').convert()
numeric_block_sprites["block_numeric_7"] = pygame.image.load(blocks_path + 'block_numeric_7.gif').convert()
numeric_block_sprites["block_numeric_8"] = pygame.image.load(blocks_path + 'block_numeric_8.gif').convert()

for name, sprite in numeric_block_sprites.items():
    block_sprites[name] = sprite.copy()
    s = sprite.copy()
    s.fill((64, 64, 64, 255), special_flags=pygame.BLEND_RGBA_SUB)
    s = pygame.transform.flip(s, True, False)
    block_sprites[name + "_dark"] = s
    s = s.copy()
    s.set_alpha(64)
    block_sprites[name + "_invisible_dark"] = s

# BLOCK_SPRITES (block is everything that needs alpha versions)

block_sprites["block"] = pygame.image.load(blocks_path + 'block.gif').convert()
block_sprites["block_start"] = pygame.image.load(blocks_path + 'block_start.gif').convert()
block_sprites["block_end"] = pygame.image.load(blocks_path + 'block_end.gif').convert()
block_sprites["error"] = pygame.image.load(blocks_path + 'error.gif').convert()
block_sprites["block_ice"] = pygame.image.load(blocks_path + 'block_ice.gif').convert()
block_sprites["block_jump_2"] = pygame.image.load(blocks_path + 'block_jump_2.gif').convert()
block_sprites["block_lift"] = pygame.image.load(blocks_path + 'block_lift.gif').convert()
block_sprites["player"] = pygame.image.load(blocks_path + 'player.gif').convert()
block_sprites["player_shrek"] = pygame.image.load(blocks_path + 'player_shrek.gif').convert()
block_sprites["block_portal"] = pygame.image.load(blocks_path + 'block_portal.gif').convert()
block_sprites["block_dummy"] = pygame.image.load(blocks_path + 'block_dummy.gif').convert()
block_sprites["block_lamp_on"] = pygame.image.load(blocks_path + 'block_lamp_on.gif').convert()
block_sprites["block_lamp_off"] = pygame.image.load(blocks_path + 'block_lamp_off.gif').convert()
block_sprites["block_bridge"] = pygame.image.load(blocks_path + 'block_bridge.gif').convert()
block_sprites["block_entrance_hub"] = pygame.image.load(blocks_path + 'block_entrance_hub.gif').convert()
block_sprites["block_entrance_zone"] = pygame.image.load(blocks_path + 'block_entrance_zone.gif').convert()
block_sprites["block_entrance_level"] = pygame.image.load(blocks_path + 'block_entrance_level.gif').convert()
block_sprites["level_available"] = pygame.image.load(blocks_path + 'level_available.gif').convert()
block_sprites["level_unavailable"] = pygame.image.load(blocks_path + 'level_unavailable.gif').convert()
block_sprites["block_map_bridge_off"] = pygame.image.load(blocks_path + 'block_map_bridge_off.gif').convert()
block_sprites["block_map_bridge_on"] = pygame.image.load(blocks_path + 'block_map_bridge_on.gif').convert()
block_sprites["block_ones"] = pygame.image.load(blocks_path + 'block_ones.gif').convert()
block_sprites["block_jump_3"] = pygame.image.load(blocks_path + 'block_jump_3.gif').convert()
block_sprites["block_blocker"] = pygame.image.load(blocks_path + 'block_blocker.gif').convert()
block_sprites["block_thunder"] = pygame.image.load(blocks_path + 'block_thunder.gif').convert()
block_sprites["block_pink"] = pygame.image.load(blocks_path + 'block_pink.gif').convert()
block_sprites["block_orange"] = pygame.image.load(blocks_path + 'block_orange.gif').convert()
block_sprites["block_yellow"] = pygame.image.load(blocks_path + 'block_yellow.gif').convert()
block_sprites["flavour_orange"] = pygame.image.load(blocks_path + 'flavour_orange.gif').convert()
block_sprites["flavour_lemon"] = pygame.image.load(blocks_path + 'flavour_lemon.gif').convert()
block_sprites["block_reset"] = pygame.image.load(blocks_path + 'block_reset.gif').convert()
block_sprites["chav"] = pygame.image.load(blocks_path + 'chav.gif').convert()
block_sprites["block_invisible"] = pygame.image.load(blocks_path + 'block.gif').convert()
block_sprites["bomb"] = pygame.image.load(blocks_path + 'bomb.gif').convert()
block_sprites["block_fragile_start"] = pygame.image.load(blocks_path + 'block_fragile_start.gif')
block_sprites["block_fragile_end"] = pygame.image.load(blocks_path + 'block_fragile_end.gif')
block_sprites["block_plus"] = pygame.image.load(blocks_path + 'block_plus.gif')
block_sprites["block_minus"] = pygame.image.load(blocks_path + 'block_minus.gif')

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
