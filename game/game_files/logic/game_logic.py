import pygame
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
from game_files.logic.direction import direction as d

FONT_SIZE_2 = v.LEVEL_FONT_SIZE // 2
FONT_2 = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_2)

FONT_SIZE_4 = v.LEVEL_FONT_SIZE // 4
FONT_4 = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_4)


def key_to_direction(key):
    if k.is_right(key):
        return d.RIGHT
    if k.is_up(key):
        return d.UP
    if k.is_left(key):
        return d.LEFT
    if k.is_down(key):
        return d.DOWN
    return d.NONE


class game_logic:
    def __init__(self, screen):
        self.stage = None
        self.screen = screen
        self.keys_registered = []
        self.single_layer = None
        self.input_box = input_box(
            0, v.WINDOW_Y - (v.WITCH_FONT_SIZE + 2 * v.WITCH_FONT_OFFSET),
            v.WINDOW_X, v.WITCH_FONT_SIZE + 2 * v.WITCH_FONT_OFFSET, self, "empty"
        )
        self.level_index = None
        self.witch = witch(screen)
        self.grayness = s.sprites["background_grayness"]
        self.speedrun = None

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
        log.info("Setting stage to", new_stage.level_index)
        self.stage = new_stage
        self.single_layer = None
        self.level_index = self.stage.level_index
        return True

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            c.exit_game()

        if event.type == pygame.KEYDOWN:
            self.keys_registered.append((event.key, event.unicode))

    def perform_speedrun_check(self):
        if self.speedrun is not None and self.speedrun.is_condition_met():
            global_save_state.hard_save_all()
            name = self.speedrun.get_name()
            log.print(f"Speedrun {name} completed! Deaths reset: {self.speedrun.does_death_reset()}")
            log.print(global_save_state.get_all_stats())
            global_save_state.set("is_timer_stopped", True)
            global_save_state.hard_save_all()

    def complete(self):
        if not l.is_level(self.level_index):
            return False

        completed = self.level_index
        global_save_state.complete_level(completed, hard_save=True)
        self.set_stage(l.next_level(completed))
        if self.speedrun is not None:
            time = u.ticks_to_time(global_save_state.get("time", -1))
            log.print(f"Level {completed} completed at {time}")
            self.perform_speedrun_check()
        return True

    def move(self):
        if not global_save_state.get("is_timer_stopped", False):
            global_save_state.increase_value("time", default_data=0)
            if global_save_state.get("time", 0) % (g.FRAME_RATE * g.AUTO_SAVE_INTERVAL) == 0:
                global_save_state.hard_save_all()

        # now this part is bullshit and I will rework it at some point
        # bruh
        if self.stage.latest_state().completed and not self.stage.animation_manager.is_logic_prevented():
            if self.complete():
                return

        if self.stage.change_to is not None:
            self.set_stage(self.stage.change_to)
            return

        self.witch.check_for_events(self.level_index, self.stage)

        # has to iterate over every key, imagine pressing at once K, B and W, this should work
        next_move_direction = d.NONE
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
            if next_move_direction == d.NONE and direction != d.NONE:
                next_move_direction = direction
                continue

            if g.CHEATS:
                if g.FAST_LEVEL_SKIP:
                    if k.is_next_cheat(key):
                        c.execute_command(self, "c")
                        continue
                    if k.is_prev_cheat(key):
                        c.execute_command(self, "p")
                        continue
                if g.FAST_LEVEL_SWAP:
                    if k.is_next_swap(key):
                        c.execute_command(self, "swap next")
                        continue
                    if k.is_prev_swap(key):
                        c.execute_command(self, "swap prev")
                        continue

            if k.is_reverse(key):
                self.stage.reverse()
                global_save_state.log_reverse()
                if self.speedrun is not None and self.speedrun.settings.does_death_reset:
                    self.stage.reset()
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

            self.single_layer = u.new_single_layer(self.single_layer, key,
                                                   self.stage.latest_state().z)  # returns none or integer

        g.KBcheat = k.is_KB_cheat(pygame.key.get_pressed())
        if not self.witch.is_active():
            self.stage.move(next_move_direction)  # has to be called, d.NONE if no move pressed
            if next_move_direction != d.NONE:
                global_save_state.log_move(next_move_direction)

        if self.stage.speedrun_check_needed:
            self.stage.speedrun_check_needed = False
            self.perform_speedrun_check()

        if self.stage.latest_state().player.dead:
            if g.AUTO_REVERSE:
                self.stage.animation_manager.register_message(self.screen, "You died, reversed lase move.", g.FRAME_RATE * 3)
                global_save_state.log_auto_reverse()
                self.stage.reverse()
            if self.speedrun is not None and self.speedrun.settings.does_death_reset:
                self.stage.reset()
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
            self.screen.blit(txt_surface,
                             (v.WINDOW_X - txt_surface.get_rect().width - v.LEVEL_FONT_OFFSET,
                              v.LEVEL_FONT_OFFSET)
                             )
            txt_surface = FONT_4.render(g.VERSION, True, pygame.Color('black'))
            self.screen.blit(txt_surface,
                             (v.WINDOW_X - txt_surface.get_rect().width - v.LEVEL_FONT_OFFSET,
                              v.LEVEL_FONT_OFFSET * 2 + FONT_SIZE_2)
                             )

        self.screen.blit(self.grayness, (0, 0))

    def execute_command(self, command):
        return c.execute_command(self, command)
