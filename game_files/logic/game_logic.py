import pygame
import sys
from game_files.logic.stage import stage
from game_files.logic.input_box import input_box
import game_files.imports.utils as u
import game_files.imports.all_sprites as s
import game_files.imports.globals as g
import game_files.imports.levels as l
import game_files.logic.commands as c
import game_files.imports.keybindings as k
from game_files.imports.view_constants import global_view_constants as v
from game_files.imports.save_state import global_save_state
from game_files.witch.witch import witch
from game_files.imports.log import log


FONT_SIZE_2 = v.LEVEL_FONT_SIZE//2
FONT_2 = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_2)

FONT_SIZE_4 = v.LEVEL_FONT_SIZE//4
FONT_4 = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_4)

def key_to_direction(key):
    if k.is_right(key):
        return 0
    if k.is_up(key):
        return 1
    if k.is_left(key):
        return 2
    if k.is_down(key):
        return 3
    return None

class game_logic:
    def __init__(self, screen):
        self.stage = None
        self.screen = screen
        self.keys_registered = []
        self.single_layer = None
        self.input_box = input_box(
            0, v.WINDOW_Y - (v.WITCH_FONT_SIZE + 2*v.WITCH_FONT_OFFSET),
            v.WINDOW_X, v.WITCH_FONT_SIZE + 2*v.WITCH_FONT_OFFSET, self, "empty"
        )
        self.level_index = None
        self.witch = witch(screen)
        self.grayness = s.sprites["background_grayness"]

    def set_stage(self, level_index):
        # update invisible visibility
        new_visibility = ((g.INVISIBLE_BLOCK_1_VISIBILITY - g.INVISIBLE_BLOCK_0_VISIBILITY)
                          * global_save_state.get_completion() + g.INVISIBLE_BLOCK_0_VISIBILITY) * 255
        s.sprites["block_invisible"][0].set_alpha(new_visibility)

        new_stage = stage(self.screen, level_index, self.level_index)
        if new_stage.successful is False:
            self.stage.reverse()
            self.stage.change_to = None
            return False
        log.info("setting stage to", new_stage.level_index)
        self.stage = new_stage
        self.single_layer = None
        self.level_index = self.stage.level_index
        return True

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            c.exit_game()

        if event.type == pygame.KEYDOWN:
            self.keys_registered.append((event.key, event.unicode))

    def complete(self):
        if not l.is_level(self.level_index):
            return False

        global_save_state.complete_level(self.level_index, hard_save=True)
        self.set_stage(l.next_level(self.level_index))
        return True

    def move(self):
        # might be a little... hard to understand
        global_save_state.increase_value("time", default_data=0)
        if global_save_state.get("time", 0) % (g.FRAMERATE * g.AUTO_SAVE_INTERVAL) == 0:
            global_save_state.hard_save_all()

        if self.stage.latest_state().completed:
            if self.complete():
                return

        if self.stage.change_to is not None:
            self.set_stage(self.stage.change_to)
            return

        self.witch.check_for_events(self.level_index, self.stage)

        # has to iterate over every key, imagine pressing at once K, B and W, this should work
        next_move_direction = None
        for key, unicode in self.keys_registered:
            witch_was_active = self.witch.is_active()
            input_box_was_active = self.input_box.active

            if not witch_was_active:
                self.input_box.handle_key_pressed(key, unicode)  # !! ignores unless active
            if not input_box_was_active:
                self.witch.handle_key_pressed(key)  # !! ignores unless active

            if witch_was_active or input_box_was_active:
                continue

            direction = key_to_direction(key)
            if next_move_direction is None and direction is not None:
                next_move_direction = direction
                continue

            if k.is_reverse(key):
                self.stage.reverse()
                global_save_state.log_reverse()
                continue

            if k.is_reset(key):
                log.info("Resetting")
                self.stage.reset()
                global_save_state.log_reset()
                continue

            if k.is_back_in_hierarchy(key):
                target = l.up_in_hierarchy(self.level_index)
                log.info("Going back to", target)
                if target == self.level_index:
                    self.stage.reset()
                else:
                    self.set_stage(l.up_in_hierarchy(self.level_index))
                global_save_state.log_escape()
                continue

            self.single_layer = u.new_single_layer(self.single_layer, key, self.stage.latest_state().z)     # returns none or integer

        g.KBcheat = k.is_KB_cheat(pygame.key.get_pressed())
        self.stage.move(next_move_direction)    # has to be called, None if no move pressed
        if g.AUTO_REVERSE and self.stage.latest_state().player.dead:
            self.stage.reverse()
        self.keys_registered = []

    def draw(self):
        self.screen.blit(s.sprites[l.background_of_level(self.level_index)], (0, 0))
        self.stage.draw(self.single_layer)

        if self.witch.is_active():
            self.witch.draw()

        if self.input_box.active:
            self.screen.blit(s.sprites['background_black'], (0, 0))
            self.input_box.draw(self.screen)

        if g.TIMER:
            ticks = global_save_state.get("time", 0)
            time = u.ticks_to_time(ticks)
            txt_surface = FONT_2.render(time, True, pygame.Color('black'))
            # txt_surface.get_rect().right = 100
            self.screen.blit(txt_surface,
                             (v.WINDOW_X - len(time) * FONT_SIZE_2 * 0.58 - v.LEVEL_FONT_OFFSET,
                              v.LEVEL_FONT_OFFSET)
                             )
            txt_surface = FONT_4.render(g.VERSION, True, pygame.Color('black'))
            self.screen.blit(txt_surface,
                             (v.WINDOW_X - len(g.VERSION) * FONT_SIZE_4 * g.FONT_RATIO - v.LEVEL_FONT_OFFSET,
                              v.LEVEL_FONT_OFFSET * 2 + FONT_SIZE_2)
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

