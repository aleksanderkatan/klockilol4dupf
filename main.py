def run():
    import pygame       # initialized somewhere else
    import game_files.imports.globals as g
    from game_files.imports.view_constants import global_view_constants as v
    screen = pygame.display.set_mode((v.WINDOW_X, v.WINDOW_Y))
    import game_files.imports.all_sprites as s
    from game_files.logic.game_logic import game_logic
    pygame.display.set_icon(s.sprites["block_numeric_1"][0])
    pygame.display.set_caption('klockilol4dupf')
    # screen.blit(s.sprites["background_loading"], (0, 0))

    clock = pygame.time.Clock()
    game = game_logic(screen)
    game.set_stage((400, 1))

    while True:
        for event in pygame.event.get():
            game.event_handler(event)

        game.move()
        game.draw()

        pygame.display.update()
        clock.tick(g.FRAMERATE)

