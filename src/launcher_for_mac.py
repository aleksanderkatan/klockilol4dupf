import pygame
pygame.init()
from game_files.imports.view_constants import global_view_constants as v

if __name__ == "__main__":
    x, y, _ = 1280//4, 960//4, 0
    resolution = (x, y)
    v.change_resolution(resolution)
    # if combo_lan.current() == 1:
    #     g.WITCH = False

    screen = pygame.display.set_mode((v.WINDOW_X, v.WINDOW_Y))
    import game_files.imports.all_sprites as s
    from game_files.logic.game_logic import game_logic
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

