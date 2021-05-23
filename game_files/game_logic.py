import pygame
import sys
import hashlib
from game_files.stage import stage
from game_files.input_box import input_box
import game_files.utils as u
import game_files.all_sprites as s
import game_files.globals as g
import game_files.levels as l
import game_files.commands as c
from game_files.save_state import global_save_state
from game_files.witch.witch import witch
from game_files.log import log


FONT_SIZE_2 = g.LEVEL_FONT_SIZE//2
FONT_2 = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_2)

FONT_SIZE_4 = g.LEVEL_FONT_SIZE//4
FONT_4 = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_4)


class game_logic:
    def __init__(self, screen):
        self.stage = None
        self.screen = screen
        self.keys_registered = []
        self.single_layer = None
        self.input_box = input_box(
            0, g.WINDOW_Y - (g.WITCH_FONT_SIZE + 2*g.WITCH_FONT_OFFSET),
            g.WINDOW_X, g.WITCH_FONT_SIZE + 2*g.WITCH_FONT_OFFSET, self, "empty"
        )
        self.level_index = None
        self.witch = witch(screen)
        self.grayness = s.sprites["grayness"]

    def set_stage(self, level_index):
        new_stage = stage(self.screen, level_index, self.level_index)
        if new_stage.successful is False:
            self.stage.reverse()
            self.stage.change_to = None
            return False
        self.stage = new_stage
        self.single_layer = None
        self.level_index = self.stage.level_index
        return True

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            self.keys_registered.append(event)

    def complete(self):
        if not l.is_level(self.level_index):
            return

        global_save_state.complete(self.level_index)
        self.set_stage(l.next_level(self.level_index))

    def move(self):
        global_save_state.tick_timer()
        if global_save_state.get_timer_ticks() % g.FRAMERATE * g.AUTO_SAVE_INTERVAL == 0:
            global_save_state.save()

        if self.stage.latest_state().completed:
            self.complete()
            return

        if self.stage.change_to is not None:
            self.set_stage(self.stage.change_to)
            return

        self.witch.check_for_events(self.level_index, self.stage)

        next_move_direction = None
        for event in self.keys_registered:
            witch_was_active = self.witch.is_active()
            input_box_was_active = self.input_box.active

            self.input_box.handle_event(event)  # !! ignores until activated
            self.witch.handle_event(event)  # !! ignores until activated

            if witch_was_active or input_box_was_active:
                continue

            key = event.key
            next_move_direction = u.key_to_direction(key)

            if key in [pygame.K_q, pygame.K_RSHIFT]:
                self.stage.reverse()

            if key in [pygame.K_r, pygame.K_SLASH]:
                self.stage.reset()

            if key == pygame.K_ESCAPE:
                if self.level_index[0] == 400:
                    self.stage.reset()
                else:
                    self.set_stage(l.up_in_hierarchy(self.level_index))

            self.single_layer = u.new_single_layer(self.single_layer, key, self.stage.latest_state().z)

        keys = pygame.key.get_pressed()
        g.KBcheat = (keys[pygame.K_b] and keys[pygame.K_k])
        self.stage.move(next_move_direction)
        if g.AUTO_REVERSE and self.stage.latest_state().player.dead:
            self.stage.reverse()
        self.keys_registered = []

    def draw(self):
        self.screen.blit(l.background_of_level(self.level_index), (0, 0))
        self.stage.draw(self.single_layer)

        if self.witch.is_active():
            self.witch.draw()

        if self.input_box.active:
            self.screen.blit(s.sprites['black'], (0, 0))
            self.input_box.draw(self.screen)

        if g.TIMER:
            ticks = global_save_state.get_timer_ticks()
            time = u.ticks_to_time(ticks)
            txt_surface = FONT_2.render(time, True, pygame.Color('black'))
            self.screen.blit(txt_surface,
                             (g.WINDOW_X - len(time) * FONT_SIZE_2 * 0.58 - g.LEVEL_FONT_OFFSET,
                              g.LEVEL_FONT_OFFSET)
                             )
            txt_surface = FONT_4.render(g.VERSION, True, pygame.Color('black'))
            self.screen.blit(txt_surface,
                             (g.WINDOW_X - len(g.VERSION) * FONT_SIZE_4 * g.FONT_RATIO - g.LEVEL_FONT_OFFSET,
                              g.LEVEL_FONT_OFFSET * 2 + FONT_SIZE_2)
                             )

        self.screen.blit(self.grayness, (0, 0))

    def execute_command(self, command):
        if command == '':
            return

        command = command.split(' ')
        command = [word.lower() for word in command]

        if not g.CHEATS:
            if command[0] not in c.public_commands:
                log.info("No such command")
            else:
                log.info("executing: " + command[0])
                c.public_commands[command[0]](self, command)
        else:
            if command[0] in c.root_commands:
                c.root_commands[command[0]](self, command)
            elif command[0] in c.public_commands:
                c.public_commands[command[0]](self, command)        # intentional, command overloading
            else:
                log.info("No such command")

