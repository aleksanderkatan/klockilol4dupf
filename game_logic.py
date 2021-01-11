import pygame
import sys
from stage import stage
from input_box import input_box
import utils as u
import import_sprites as s
import config as c
import levels as l
from save_state import global_save_state

class game_logic:
    def __init__(self, screen):
        self.stage = None
        self.screen = screen
        self.keys_registered = []
        self.single_layer = None
        self.input_box = input_box(0, c.WINDOW_Y - 32, c.WINDOW_X, 32, self, "elo")
        self.level_index = None

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

        next_move_direction = None
        for event in self.keys_registered:
            self.input_box.handle_event(event)  # !! ignores until activated

            if self.input_box.active:
                continue

            key = event.key
            next_move_direction = u.key_to_direction(key)

            if key == pygame.K_q:
                self.stage.reverse()

            if key == pygame.K_r:
                self.stage.reset()

            if key == pygame.K_ESCAPE:
                if self.level_index[1] != 0:
                    self.set_stage((self.level_index[0], 0))
                else:
                    self.set_stage(l.hub_of_set(self.level_index[0]))

            self.single_layer = u.new_single_layer(self.single_layer, key)

        self.stage.move(next_move_direction)
        self.keys_registered = []

    def draw(self):
        self.screen.blit(s.sprites['background'], (0, 0))
        self.stage.draw(self.single_layer)

        if self.input_box.active:
            self.screen.blit(s.sprites['black'], (0, 0))
            self.input_box.draw(self.screen)

    def execute_command(self, command):
        if not c.CHEATS:
            return

        #!! some bullshit down here, don't look down
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
            s.swap("background")
        elif command[0] == 'yoffset':
            print("Changing y offset")
            c.LAYER_Y_OFFSET = int(command[1])
        elif command[0] == 'xoffset':
            print("Changing x offset")
            c.LAYER_X_OFFSET = int(command[1])
        elif command[0].lower() in ['exit', 'quit', 'halt', 'shutdown', 'poweroff', 'q']:
            pygame.quit()
            sys.exit(0)
        elif command[0] == 'reset':
            print("Erradicating save file")
            global_save_state.reset()
            self.set_stage((1, 1))
        elif command[0] == 'all':
            print("Completing all levels")
            global_save_state.complete_all()
        elif command[0] == 'c':
            print("Completing current level")
            self.complete()
        else:
            print("No such command")
