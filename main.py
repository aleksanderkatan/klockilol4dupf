import pygame
import game_files.globals as g

pygame.init()
screen = pygame.display.set_mode((g.WINDOW_X, g.WINDOW_Y))
pygame.display.set_caption('klockilol4dupf')

from game_files.game_logic import game_logic

clock = pygame.time.Clock()
game = game_logic(screen)
game.set_stage((7, 0))

while True:
    next_move = None
    for event in pygame.event.get():
        game.event_handler(event)

    game.move()
    game.draw()

    pygame.display.update()
    clock.tick(g.FRAMERATE)
