import pygame

import src.imports.globals as g
from src.imports.view_constants import global_view_constants as v


def run_game(resolution, save):
    g.save_state = save
    pygame.init()
    x, y = resolution
    resolution = (x, y)
    v.change_resolution(resolution)

    screen = pygame.display.set_mode((v.WINDOW_X, v.WINDOW_Y))
    import src.imports.all_sprites as s
    from src.logic.game_logic import game_logic
    pygame.display.set_icon(s.sprites["block_numeric_1"][0])
    pygame.display.set_caption('klockilol4dupf')

    clock = pygame.time.Clock()
    game = game_logic(screen)
    game.set_stage((400, 1))
    while True:
        for event in pygame.event.get():
            game.event_handler(event)

        game.move()
        game.draw()

        pygame.display.update()
        clock.tick(v.FRAME_RATE)
