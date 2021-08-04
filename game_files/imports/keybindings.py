import pygame

def is_left(key):
    return key in [pygame.K_a, pygame.K_LEFT]

def is_right(key):
    return key in [pygame.K_d, pygame.K_RIGHT]

def is_up(key):
    return key in [pygame.K_w, pygame.K_UP]

def is_down(key):
    return key in [pygame.K_s, pygame.K_DOWN]

def is_reverse(key):
    return key in [pygame.K_q, pygame.K_RSHIFT]

def is_reset(key):
    return key in [pygame.K_r, pygame.K_SLASH]

def is_back_in_hierarchy(key):
    return key in [pygame.K_ESCAPE]


def is_input_box_enable(key):
    return key in [pygame.K_RETURN]

def is_input_box_disable(key):
    return key in [pygame.K_RSHIFT, pygame.K_ESCAPE]

def is_input_box_delete(key):
    return key in [pygame.K_BACKSPACE]


def is_witch_continue(key):
    return key in [pygame.K_SPACE]


def is_KB_cheat(keys):      # keys is an bit mask
    return keys[pygame.K_b] and keys[pygame.K_k]

