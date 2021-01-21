import pygame
import game_files.config as c

pygame.init()
screen = pygame.display.set_mode((c.WINDOW_X, c.WINDOW_Y))
pygame.display.set_caption('klockilol4dupf')

from game_files.game_logic import game_logic

clock = pygame.time.Clock()
game = game_logic(screen)
game.set_stage((2138, 0))

while True:
    next_move = None
    for event in pygame.event.get():
        game.event_handler(event)

    game.move()
    game.draw()

    pygame.display.update()
    clock.tick(c.FRAMERATE)
