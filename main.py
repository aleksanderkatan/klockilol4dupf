import pygame
import game_files.globals as g

pygame.init()
screen = pygame.display.set_mode((g.WINDOW_X, g.WINDOW_Y))
import game_files.all_sprites as s
from game_files.game_logic import game_logic
pygame.display.set_icon(s.sprites["block_numeric_1"][0])
pygame.display.set_caption('klockilol4dupf')


clock = pygame.time.Clock()
game = game_logic(screen)
game.set_stage((9, 0))

while True:
    next_move = None
    for event in pygame.event.get():
        game.event_handler(event)

    game.move()
    game.draw()

    pygame.display.update()
    clock.tick(g.FRAMERATE)
