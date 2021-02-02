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
        self.stage = stage(self.screen, level_index, self.level_index)
        self.single_layer = None
        self.level_index = level_index

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
            self.input_box.handle_event(event)  # !! ignores until activated
            self.witch.handle_event(event)  # !! ignores until activated

            if self.input_box.active:
                continue

            if self.witch.is_active():
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
            self.hasher.digest()
            self.hasher.update(bytes(command, "utf-16"))
            pw_hash = self.hasher.digest()
            if pw_hash != g.PASSWORD_HASH:
                print("WRONG PASSWORD!")
            else:
                print("Cheats enabled")
                g.CHEATS = True
            return

        # !! some bullshit down here, don't look down
        print("executing:", command)
        if command == '':
            return

        command = command.split(' ')

        if command[0] == 'lv' or command[0] == 'cd':
            if len(command) == 2:
                print("Changing level to:", 0, command[1])
                self.set_stage((0, int(command[1])))
            else:
                print("Changing level to:", command[1], command[2])
                self.set_stage((int(command[1]), int(command[2])))
        elif command[0] == 'n':
            print("Next level")
            self.set_stage(l.next_level(self.stage.level_index))
        elif command[0] == 'p':
            print("Previous level")
            self.set_stage(l.previous_level(self.stage.level_index))
        elif command[0].lower() == 'duda' and command[1].lower() == 'chuj':
            print("Swapping background")
            g.DUDA_CHUJ = not g.DUDA_CHUJ
        elif command[0] == 'yoffset':
            print("Changing y offset")
            g.LAYER_Y_OFFSET = int(command[1])
        elif command[0] == 'xoffset':
            print("Changing x offset")
            g.LAYER_X_OFFSET = int(command[1])
        elif command[0].lower() in ['exit', 'quit', 'halt', 'shutdown', 'poweroff', 'q']:
            pygame.quit()
            sys.exit(0)
        elif command[0] == 'reset_all':
            print("Erradicating save file")
            global_save_state.reset()
            self.set_stage((400, 1))
        elif command[0] == 'reset_events':
            print("Resetting events")
            global_save_state.reset_events()
        elif command[0] == 'complete_all':
            print("Completing all levels")
            global_save_state.complete_all()
        elif command[0] == 'c':
            print("Completing current level")
            self.complete()
        elif command[0] == 'r':
            print("Resetting current level")
            self.set_stage(self.level_index)
        else:
            print("No such command")
