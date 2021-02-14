import pygame
import sys
import hashlib
from game_files.stage import stage
from game_files.input_box import input_box
import game_files.utils as u
import game_files.all_sprites as s
import game_files.globals as g
import game_files.levels as l
from game_files.save_state import global_save_state
from game_files.witch.witch import witch
from game_files.log import log

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
        self.hasher = hashlib.sha256()
        self.grayness = s.sprites["grayness"]

    def set_stage(self, level_index):
        new_stage = stage(self.screen, level_index, self.level_index)
        if new_stage.successful is False:
            self.stage.reverse()
            return False
        self.stage = new_stage
        self.single_layer = None
        self.level_index = level_index
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
        if self.stage.latest_state().completed:
            self.complete()

        if self.stage.change_to is not None:
            self.set_stage(self.stage.change_to)

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

            if key == pygame.K_q:
                self.stage.reverse()

            if key == pygame.K_r:
                self.stage.reset()

            if key == pygame.K_ESCAPE:
                if self.level_index[0] == 400:
                    self.stage.reset()
                elif self.level_index[1] != 0:
                    self.set_stage((self.level_index[0], 0))
                else:
                    self.set_stage(l.hub_of_set(self.level_index[0]))

            self.single_layer = u.new_single_layer(self.single_layer, key)

        self.stage.move(next_move_direction)
        self.keys_registered = []

    def draw(self):
        self.screen.blit(u.background_of_level(self.level_index), (0, 0))
        self.stage.draw(self.single_layer)

        if self.witch.is_active():
            self.witch.draw()

        if self.input_box.active:
            self.screen.blit(s.sprites['black'], (0, 0))
            self.input_box.draw(self.screen)

        self.screen.blit(self.grayness, (0, 0))

    def execute_command(self, command):
        if not g.CHEATS:
            pw_hash = u.hash_string(command)
            if pw_hash != g.PASSWORD_HASH:
                log.info("WRONG PASSWORD!")
            else:
                log.info("Cheats enabled")
                g.CHEATS = True
            return

        # !! some bullshit down here, don't look down
        log.info("executing: " + command)
        if command == '':
            return

        command = command.split(' ')

        if command[0] == 'lv' or command[0] == 'cd':
            if len(command) == 2:
                log.info("Changing level to: 0 " + command[1])
                self.set_stage((0, int(command[1])))
            else:
                log.info("Changing level to: " + command[1] + " " + command[2])
                self.set_stage((int(command[1]), int(command[2])))
        elif command[0] == 'n':
            log.info("Next level")
            self.set_stage(l.next_level(self.stage.level_index))
        elif command[0] == 'p':
            log.info("Previous level")
            self.set_stage(l.previous_level(self.stage.level_index))
        elif command[0].lower() == 'duda' and command[1].lower() == 'chuj':
            log.info("Swapping background")
            g.DUDA_CHUJ = not g.DUDA_CHUJ
        elif command[0] == 'yoffset':
            log.info("Changing y offset")
            g.LAYER_Y_OFFSET = int(command[1])
        elif command[0] == 'xoffset':
            log.info("Changing x offset")
            g.LAYER_X_OFFSET = int(command[1])
        elif command[0].lower() in ['exit', 'quit', 'halt', 'shutdown', 'poweroff', 'q']:
            log.info("Quitting")
            pygame.quit()
            sys.exit(0)
        elif command[0] == 'reset_all':
            log.warning("Erradicating save file")
            global_save_state.reset()
            self.level_index = None
            self.set_stage((400, 1))
        elif command[0] == 'reset_events':
            log.info("Resetting events")
            global_save_state.reset_events()
        elif command[0] == 'complete_all':
            log.info("Completing all levels")
            global_save_state.complete_all()
        elif command[0] == 'c':
            log.info("Completing current level")
            self.complete()
        elif command[0] == 'r':
            log.info("Resetting current level")
            self.set_stage(self.level_index)
        elif command[0] == 'load_all':
            old_level_index = self.level_index
            old_stage = self.stage
            problems = []
            for level_index in l.all_levels_iterator():
                if not self.set_stage(level_index):
                    problems.append(level_index)
            self.stage = old_stage
            self.level_index = old_level_index
            log.error("Errors in stages: " + str(problems))
        else:
            log.info("No such command")
