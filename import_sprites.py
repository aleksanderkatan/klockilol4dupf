import pygame
import config as c

temp_sprites = {}

temp_sprites["obj_block"] = pygame.image.load('sprites/blocks/0.bmp').convert()
temp_sprites["obj_block_start"] = pygame.image.load('sprites/blocks/start.bmp').convert()
temp_sprites["obj_block_end"] = pygame.image.load('sprites/blocks/end.bmp').convert()
temp_sprites["obj_block_numeric_1"] = pygame.image.load('sprites/blocks/1.bmp').convert()
temp_sprites["obj_block_numeric_2"] = pygame.image.load('sprites/blocks/2.bmp').convert()
temp_sprites["error"] = pygame.image.load('sprites/blocks/error.bmp').convert()
temp_sprites["obj_block_ice"] = pygame.image.load('sprites/blocks/ice.bmp').convert()
temp_sprites["obj_block_arrow_0"] = pygame.image.load('sprites/blocks/arrow.bmp').convert()
temp_sprites["obj_block_arrow_1"] = pygame.image.load('sprites/blocks/arrow.bmp').convert()
temp_sprites["obj_block_arrow_1"] = pygame.transform.rotate(temp_sprites["obj_block_arrow_1"], 90)
temp_sprites["obj_block_arrow_2"] = pygame.image.load('sprites/blocks/arrow.bmp').convert()
temp_sprites["obj_block_arrow_2"] = pygame.transform.rotate(temp_sprites["obj_block_arrow_2"], 180)
temp_sprites["obj_block_arrow_3"] = pygame.image.load('sprites/blocks/arrow.bmp').convert()
temp_sprites["obj_block_arrow_3"] = pygame.transform.rotate(temp_sprites["obj_block_arrow_3"], 270)
temp_sprites["obj_block_jump_2"] = pygame.image.load('sprites/blocks/jump.bmp').convert()
temp_sprites["obj_block_lift"] = pygame.image.load('sprites/blocks/lift.bmp').convert()
temp_sprites["obj_player"] = pygame.image.load('sprites/player3.gif').convert()
temp_sprites["obj_block_portal"] = pygame.image.load('sprites/blocks/portal.bmp').convert()
temp_sprites["obj_block_dummy"] = pygame.image.load('sprites/blocks/dummy.bmp').convert()
temp_sprites["obj_block_lamp_on"] = pygame.image.load('sprites/blocks/lampon.bmp').convert()
temp_sprites["obj_block_lamp_off"] = pygame.image.load('sprites/blocks/lampoff.bmp').convert()
temp_sprites["obj_block_bridge"] = pygame.image.load('sprites/blocks/bridge.bmp').convert()
temp_sprites["obj_block_numeric_3"] = pygame.image.load('sprites/blocks/3.bmp').convert()
temp_sprites["obj_block_numeric_4"] = pygame.image.load('sprites/blocks/4.bmp').convert()
temp_sprites["obj_block_numeric_5"] = pygame.image.load('sprites/blocks/5.bmp').convert()
temp_sprites["obj_block_numeric_6"] = pygame.image.load('sprites/blocks/6.bmp').convert()
temp_sprites["obj_block_numeric_7"] = pygame.image.load('sprites/blocks/7.bmp').convert()
temp_sprites["obj_block_numeric_8"] = pygame.image.load('sprites/blocks/8.bmp').convert()
temp_sprites["obj_block_entrance_hub"] = pygame.image.load('sprites/blocks/entrancehub.bmp').convert()
temp_sprites["obj_block_entrance_zone"] = pygame.image.load('sprites/blocks/entrancezone.bmp').convert()
temp_sprites["obj_block_entrance_level"] = pygame.image.load('sprites/blocks/entrancelevel.bmp').convert()
temp_sprites["level_available"] = pygame.image.load('sprites/blocks/levelavailable.bmp').convert()
temp_sprites["level_unavailable"] = pygame.image.load('sprites/blocks/levelunavailable.bmp').convert()
temp_sprites["obj_block_map_bridge_off"] = pygame.image.load('sprites/blocks/mapbridgeoff.bmp').convert()
temp_sprites["obj_block_map_bridge_on"] = pygame.image.load('sprites/blocks/mapbridgeon.bmp').convert()
temp_sprites["obj_block_ones"] = pygame.image.load('sprites/blocks/ones.bmp').convert()

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
    #!! SYF xD
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

sprites["background"] = pygame.image.load('sprites/background.jpg').convert()
sprites["background"] = pygame.transform.scale(sprites["background"], (c.WINDOW_X, c.WINDOW_Y))
sprites["you_died"] = pygame.image.load('sprites/youdied.jpg').convert()
sprites["you_died"] = pygame.transform.scale(sprites["you_died"], (c.WINDOW_X, c.WINDOW_Y))
sprites["black"] = pygame.image.load('sprites/black.jpg').convert()
sprites["black"] = pygame.transform.scale(sprites["black"], (c.WINDOW_X, c.WINDOW_Y))
sprites["black"].set_alpha(192)
sprites["witch"] = pygame.image.load('sprites/witch.png')
sprites["witch"] = pygame.transform.scale(sprites["witch"], (c.WINDOW_X, c.WINDOW_Y))

alternate = {}
alternate["background"] = pygame.image.load('sprites/dudachuj.png').convert()
alternate["background"] = pygame.transform.scale(alternate["background"], (c.WINDOW_X, c.WINDOW_Y))

def swap(sprite_name):
    temp = sprites[sprite_name]
    sprites[sprite_name] = alternate[sprite_name]
    alternate[sprite_name] = temp
