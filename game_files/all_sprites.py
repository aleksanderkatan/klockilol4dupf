import pygame
import game_files.config as c

temp_sprites = {}

temp_sprites["block"] = pygame.image.load('game_files/sprites/blocks/0.bmp').convert()
temp_sprites["block_start"] = pygame.image.load('game_files/sprites/blocks/start.bmp').convert()
temp_sprites["block_end"] = pygame.image.load('game_files/sprites/blocks/end.bmp').convert()
temp_sprites["block_numeric_1"] = pygame.image.load('game_files/sprites/blocks/1.bmp').convert()
temp_sprites["block_numeric_2"] = pygame.image.load('game_files/sprites/blocks/2.bmp').convert()
temp_sprites["error"] = pygame.image.load('game_files/sprites/blocks/error.bmp').convert()
temp_sprites["block_ice"] = pygame.image.load('game_files/sprites/blocks/ice.bmp').convert()
temp_sprites["block_arrow_0"] = pygame.image.load('game_files/sprites/blocks/arrow.bmp').convert()
temp_sprites["block_arrow_1"] = pygame.image.load('game_files/sprites/blocks/arrow.bmp').convert()
temp_sprites["block_arrow_2"] = pygame.image.load('game_files/sprites/blocks/arrow.bmp').convert()
temp_sprites["block_arrow_3"] = pygame.image.load('game_files/sprites/blocks/arrow.bmp').convert()
temp_sprites["block_arrow_1"] = pygame.transform.rotate(temp_sprites["block_arrow_1"], 90)
temp_sprites["block_arrow_2"] = pygame.transform.rotate(temp_sprites["block_arrow_2"], 180)
temp_sprites["block_arrow_3"] = pygame.transform.rotate(temp_sprites["block_arrow_3"], 270)
temp_sprites["block_jump_2"] = pygame.image.load('game_files/sprites/blocks/jump2.bmp').convert()
temp_sprites["block_lift"] = pygame.image.load('game_files/sprites/blocks/lift.bmp').convert()
temp_sprites["player"] = pygame.image.load('game_files/sprites/player.gif').convert()
temp_sprites["block_portal"] = pygame.image.load('game_files/sprites/blocks/portal.bmp').convert()
temp_sprites["block_dummy"] = pygame.image.load('game_files/sprites/blocks/dummy.bmp').convert()
temp_sprites["block_lamp_on"] = pygame.image.load('game_files/sprites/blocks/lamp_on.bmp').convert()
temp_sprites["block_lamp_off"] = pygame.image.load('game_files/sprites/blocks/lamp_off.bmp').convert()
temp_sprites["block_bridge"] = pygame.image.load('game_files/sprites/blocks/bridge.bmp').convert()
temp_sprites["block_numeric_3"] = pygame.image.load('game_files/sprites/blocks/3.bmp').convert()
temp_sprites["block_numeric_4"] = pygame.image.load('game_files/sprites/blocks/4.bmp').convert()
temp_sprites["block_numeric_5"] = pygame.image.load('game_files/sprites/blocks/5.bmp').convert()
temp_sprites["block_numeric_6"] = pygame.image.load('game_files/sprites/blocks/6.bmp').convert()
temp_sprites["block_numeric_7"] = pygame.image.load('game_files/sprites/blocks/7.bmp').convert()
temp_sprites["block_numeric_8"] = pygame.image.load('game_files/sprites/blocks/8.bmp').convert()
temp_sprites["block_entrance_hub"] = pygame.image.load('game_files/sprites/blocks/entrance_hub.bmp').convert()
temp_sprites["block_entrance_zone"] = pygame.image.load('game_files/sprites/blocks/entrance_zone.bmp').convert()
temp_sprites["block_entrance_level"] = pygame.image.load('game_files/sprites/blocks/entrance_level.bmp').convert()
temp_sprites["level_available"] = pygame.image.load('game_files/sprites/blocks/level_available.bmp').convert()
temp_sprites["level_unavailable"] = pygame.image.load('game_files/sprites/blocks/level_unavailable.bmp').convert()
temp_sprites["block_map_bridge_off"] = pygame.image.load('game_files/sprites/blocks/map_bridge_off.bmp').convert()
temp_sprites["block_map_bridge_on"] = pygame.image.load('game_files/sprites/blocks/map_bridge_on.bmp').convert()
temp_sprites["block_ones"] = pygame.image.load('game_files/sprites/blocks/ones.bmp').convert()
temp_sprites["block_jump_3"] = pygame.image.load('game_files/sprites/blocks/jump3.bmp').convert()
temp_sprites["block_bridge_blocker"] = pygame.image.load('game_files/sprites/blocks/bridge_blocker.gif').convert()
temp_sprites["ones_one_0"] = pygame.image.load('game_files/sprites/blocks/ones_one.gif').convert()
temp_sprites["ones_one_1"] = pygame.image.load('game_files/sprites/blocks/ones_one.gif').convert()
temp_sprites["ones_one_2"] = pygame.image.load('game_files/sprites/blocks/ones_one.gif').convert()
temp_sprites["ones_one_3"] = pygame.image.load('game_files/sprites/blocks/ones_one.gif').convert()
temp_sprites["ones_one_1"] = pygame.transform.rotate(temp_sprites["ones_one_1"], 90)
temp_sprites["ones_one_2"] = pygame.transform.rotate(temp_sprites["ones_one_2"], 180)
temp_sprites["ones_one_3"] = pygame.transform.rotate(temp_sprites["ones_one_3"], 270)

sprites = {}
for name, sprite in temp_sprites.items():
    print(name, sprite)
    if name in ["level_available", "level_unavailable"]:
        new_sprite = pygame.transform.scale(
            sprite, (int(c.BLOCK_SIZE*c.LEVEL_COMPLETION_SCALE), int(c.BLOCK_SIZE*c.LEVEL_COMPLETION_SCALE))
        )
    else:
        new_sprite = pygame.transform.scale(sprite, (c.BLOCK_SIZE, c.BLOCK_SIZE))

    sprites[name] = {}
    # !! SYF xD
    sprites[name][0] = new_sprite
    sprites[name][1] = new_sprite.copy()
    sprites[name][1].set_alpha(64)
    sprites[name][2] = new_sprite.copy()
    sprites[name][2].set_alpha(48)
    sprites[name][3] = new_sprite.copy()
    sprites[name][3].set_alpha(32)
    sprites[name][-1] = new_sprite.copy()
    sprites[name][-1].set_alpha(128)
    sprites[name][-2] = new_sprite.copy()
    sprites[name][-2].set_alpha(96)
    sprites[name][-3] = new_sprite.copy()
    sprites[name][-3].set_alpha(64)

sprites["background"] = pygame.image.load('game_files/sprites/background.jpg').convert()
sprites["background"] = pygame.transform.scale(sprites["background"], (c.WINDOW_X, c.WINDOW_Y))
sprites["you_died"] = pygame.image.load('game_files/sprites/you_died.jpg').convert()
sprites["you_died"] = pygame.transform.scale(sprites["you_died"], (c.WINDOW_X, c.WINDOW_Y))
sprites["black"] = pygame.image.load('game_files/sprites/black.jpg').convert()
sprites["black"] = pygame.transform.scale(sprites["black"], (c.WINDOW_X, c.WINDOW_Y))
sprites["black"].set_alpha(192)
sprites["witch"] = pygame.image.load('game_files/sprites/witch.png')
sprites["witch"] = pygame.transform.scale(sprites["witch"], (c.WINDOW_X, c.WINDOW_Y))

alternate = {}
alternate["background"] = pygame.image.load('game_files/sprites/background_duda_chuj.png').convert()
alternate["background"] = pygame.transform.scale(alternate["background"], (c.WINDOW_X, c.WINDOW_Y))

def swap(sprite_name):
    temp = sprites[sprite_name]
    sprites[sprite_name] = alternate[sprite_name]
    alternate[sprite_name] = temp
