import pygame

import src.imports.all_sprites as s
import src.imports.globals as g
import src.imports.keybindings as k
import src.imports.levels as l
import src.imports.utils as u
import src.logic.commands as c
from src.logic.modes.logic_mode import mode
from src.imports.log import log
from src.imports.view_constants import global_view_constants as v
from src.logic.direction import direction as d
from src.logic.modes.input.input_box import input_box
from src.logic.stage import stage
from src.logic.modes.witch.events import load_events
from src.logic.modes.witch.witch import witch
from src.logic.modes.controls_display.control_display import control_display

FONT_SIZE_2 = v.LEVEL_FONT_SIZE // 2
FONT_2 = pygame.font.Font(v.FONT_PATH, FONT_SIZE_2)

FONT_SIZE_4 = v.LEVEL_FONT_SIZE // 4
FONT_4 = pygame.font.Font(v.FONT_PATH, FONT_SIZE_4)


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
        self.mode = mode.GAME
        self.keys_registered = []
        self.escape_counter = 0
        self.single_layer = None
        self.input_box = input_box(
            0, v.WINDOW_Y - (v.WITCH_FONT_SIZE + 2 * v.WITCH_FONT_OFFSET),
            v.WINDOW_X, v.WITCH_FONT_SIZE + 2 * v.WITCH_FONT_OFFSET, ""
        )
        self.witch = witch(screen, load_events(g.save_state.get_language()))
        self.controls_display = control_display("AAAAAAAAAAAAAAA")
        self.level_index = None
        self.grayness = s.sprites["background_grayness"]
        self.speedrun = None

    def move(self):
        if not g.save_state.get("is_timer_stopped", False):
            g.save_state.increase_value("time", default_data=0)
            if g.save_state.get("time", 0) % (v.FRAME_RATE * g.AUTO_SAVE_INTERVAL) == 0:
                g.save_state.hard_save_all()

        # now this part is bullshit and I will rework it at some point
        # bruh
        # it is not necessarily good now, but I can say it has been wor... no I can't even say that
        if self.stage.latest_state().completed and not self.stage.animation_manager.is_logic_prevented():
            if self.complete():
                return

        if self.stage.change_to is not None:
            self.set_stage(self.stage.change_to)
            return


        next_move_direction = d.NONE
        # we always have to iterate over every key bec multiple may be pressed
        # imagine pressing K, B and W at once, this should work
        # those methods do that, and also they do stuff like updating the mode to a new one
        match self.mode:
            case mode.GAME:
                next_move_direction = self._mode_game_move()
            case mode.INPUT:
                self._mode_input_move()
            case mode.WITCH:
                self._mode_witch_move()
            case mode.CONTROLS_DISPLAY:
                self._mode_controls_display_move()

        g.KBcheat = k.is_KB_cheat(pygame.key.get_pressed())
        if self.mode == mode.GAME:
            self.stage.move(next_move_direction)  # has to be called, d.NONE if no move pressed
            if next_move_direction != d.NONE:
                g.save_state.log_move(next_move_direction)

        if self.stage.speedrun_check_needed:
            self.stage.speedrun_check_needed = False
            self.perform_speedrun_check()

        if self.stage.latest_state().player.dead:
            if self.speedrun is not None and self.speedrun.settings.does_death_reset:
                self.stage.reset()
                self.stage.animation_manager.register_message(self.screen, "You died, stage reset.", v.FRAME_RATE * 3)
            elif g.save_state.get_preference("auto_reverse"):
                self.stage.animation_manager.register_message(self.screen, "You died, reversed last move.",
                                                              v.FRAME_RATE * 3)
                g.save_state.log_auto_reverse()
                self.stage.reverse()
        self.keys_registered = []

    def _mode_game_move(self):
        next_move_direction = d.NONE
        for key, unicode in self.keys_registered:
            if k.is_input_box_enable(key):
                self.mode = mode.INPUT
                return
        if self.witch.check_for_events(self.level_index, self.stage.get_player_pos()):
            self.mode = mode.WITCH
            return
        for key, unicode in self.keys_registered:
            if k.is_display_controls(key):
                self.mode = mode.CONTROLS_DISPLAY
                return
        else:
            for key, unicode in self.keys_registered:
                if not k.is_back_in_hierarchy(key):
                    self.escape_counter = 0

                direction = key_to_direction(key)
                if next_move_direction == d.NONE and direction != d.NONE:
                    next_move_direction = direction
                    continue

                if g.save_state.get_preference("cheats"):
                    if k.is_next_cheat(key):
                        c.execute_command(self, "c")
                        continue
                    if k.is_prev_cheat(key):
                        c.execute_command(self, "p")
                        continue
                    if k.is_next_swap(key):
                        c.execute_command(self, "swap next")
                        continue
                    if k.is_prev_swap(key):
                        c.execute_command(self, "swap prev")
                        continue

                if k.is_reverse(key):
                    self.stage.reverse()
                    g.save_state.log_reverse()
                    if self.speedrun is not None and self.speedrun.settings.does_death_reset:
                        self.stage.reset()
                    continue

                if k.is_reset(key):
                    log.info("Resetting")
                    self.stage.reset()
                    g.save_state.log_reset()
                    continue

                if k.is_back_in_hierarchy(key):
                    target = l.up_in_hierarchy(self.level_index)
                    log.trace("Going back to", target)
                    if target == self.level_index:
                        self.escape_counter += 1
                        if self.escape_counter == 1:
                            self.register_message("Press escape twice to exit.", 5)
                        if self.escape_counter == 2:
                            self.register_message("Press escape once more to exit.", 5)
                        if self.escape_counter == 3:
                            c.exit_game()
                    else:
                        self.set_stage(l.up_in_hierarchy(self.level_index))
                    g.save_state.log_escape()
                    continue

                self.single_layer = u.new_single_layer(self.single_layer, key,
                                                       self.stage.latest_state().z)  # returns none or integer
        return next_move_direction

    def _mode_input_move(self):
        for key, unicode in self.keys_registered:
            if k.is_input_box_disable(key):
                self.mode = mode.GAME
                self.input_box.clear()
                return
        for key, unicode in self.keys_registered:
            if k.is_input_box_confirm(key):
                command = self.input_box.text
                self.execute_command(command)
                self.mode = mode.GAME
                self.input_box.clear()
                return
        for key, unicode in self.keys_registered:
            self.input_box.handle_key_pressed(key, unicode)

    def _mode_witch_move(self):
        for key, unicode in self.keys_registered:
            self.witch.handle_key_pressed(key)
        if not self.witch.is_active():
            self.mode = mode.GAME

    def _mode_controls_display_move(self):
        for key, unicode in self.keys_registered:
            if k.is_display_controls(key):
                self.mode = mode.GAME
                return


    def draw(self):
        self.screen.blit(s.sprites[l.background_of_level(self.level_index)], (0, 0))
        self.stage.draw(self.single_layer)

        match self.mode:
            case mode.WITCH:
                self.witch.draw()
            case mode.INPUT:
                self.input_box.draw(self.screen)
            case mode.CONTROLS_DISPLAY:
                self.controls_display.draw(self.screen)

        if g.save_state.get_preference("timer"):
            ticks = g.save_state.get("time", 0)
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

    def set_stage(self, level_index):
        # update invisible visibility
        new_visibility = ((v.INVISIBLE_BLOCK_1_VISIBILITY - v.INVISIBLE_BLOCK_0_VISIBILITY)
                          * g.save_state.get_completion() + v.INVISIBLE_BLOCK_0_VISIBILITY) * 255
        s.sprites["block_invisible"][0].set_alpha(new_visibility)

        log.info("Filling stage", level_index)
        new_stage = stage(self.screen, level_index, self.level_index)
        if new_stage.successful is False:
            log.error("Stage " + str(level_index) + " failed to load")
            self.stage.reverse()
            self.stage.change_to = None
            self.stage.animation_manager.register_message(self.screen, g.LAST_ERROR, 10 * v.FRAME_RATE)
            g.LAST_ERROR = None
            return False
        log.trace("Setting stage to", new_stage.level_index)
        self.stage = new_stage
        self.single_layer = None
        self.level_index = self.stage.level_index
        self.escape_counter = 0
        return True

    def event_handler(self, event):
        if event.type == pygame.QUIT:
            c.exit_game()

        if event.type == pygame.KEYDOWN:
            self.keys_registered.append((event.key, event.unicode))

    def perform_speedrun_check(self):
        if self.speedrun is not None and self.speedrun.is_condition_met():
            g.save_state.hard_save_all()
            name = self.speedrun.get_name()
            log.write(f"Speedrun {name} completed! Deaths reset: {self.speedrun.does_death_reset()}")
            log.write(g.save_state.get_all_stats())
            g.save_state.set("is_timer_stopped", True)
            g.save_state.hard_save_all()

    def complete(self):
        if not l.is_level(self.level_index):
            return False

        completed = self.level_index
        g.save_state.complete_level(completed, hard_save=True)
        self.set_stage(l.next_level(completed))
        if self.speedrun is not None:
            time = u.ticks_to_time(g.save_state.get("time", -1))
            log.write(f"Level {completed} completed at {time}")
            self.perform_speedrun_check()
        return True

    def execute_command(self, command):
        return c.execute_command(self, command)

    def register_message(self, message, seconds):
        anim_manager, screen = self.stage.animation_manager, self.screen
        anim_manager.register_message(screen, message, v.FRAME_RATE * seconds)
        log.info(f"Displaying message: {message}")
