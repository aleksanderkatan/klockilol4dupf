import os
import json
import game_files.levels as l
import game_files.globals as g
from game_files.log import log

SAVE_FILE_PATH = 'game_files/data/completed.txt'

class save_data:
    def __init__(self, dic=None):
        log.info("Importing save file")
        self.completed = {}
        self.events = []
        self.is_shrek = False
        self.time = 0
        if dic is None:
            self.reset()
        else:
            for k, v in dic.items():
                setattr(self, k, v)

    def reset_completed(self):
        self.completed = {}

    def reset_events(self):
        self.events = []

    def reset_timer(self):
        self.time = 0

    def reset(self):
        self.reset_events()
        self.reset_completed()
        self.reset_timer()
        self.is_shrek = False

    def de_string(self):
        new_completed = {}
        for level_set, levels in self.completed.items():
            new_completed[int(level_set)] = []
            for level in levels:
                new_completed[int(level_set)].append(int(level))
        self.completed = new_completed

        new_events = []
        for event_index in self.events:
            new_events.append(int(event_index))
        self.completed = new_completed


class save_state:
    def __init__(self):
        self.save_data = save_data()
        self.restore()

    def complete(self, level_index):
        level_set, level = level_index
        if level_set not in self.save_data.completed:
            self.save_data.completed[level_set] = []
        if level not in self.save_data.completed[level_set]:
            self.save_data.completed[level_set].append(level)

        self.save()

    def save(self):
        with open(SAVE_FILE_PATH, 'w') as file:
            json.dump(self.save_data.__dict__, file)

    def restore(self):
        if os.path.exists(SAVE_FILE_PATH):
            with open(SAVE_FILE_PATH, 'r') as file:
                self.save_data = save_data(json.load(file))
                self.save_data.time += g.FRAMERATE*g.AUTO_SAVE_INTERVAL          # to prevent cheesing with TASes
                self.save()
        else:
            self.reset()
        self.save_data.de_string()

    def reset_completed(self):
        self.save_data.reset_completed()
        self.save()

    def reset_events(self):
        self.save_data.reset_events()
        self.save()

    def reset(self):
        self.save_data.reset()
        self.save()

    def is_completed(self, level_index):
        level_set, level = level_index
        if level == 0:
            return self.is_set_completed(level_set)
        if level_set not in self.save_data.completed:
            return False

        return level in self.save_data.completed[level_set]

    def is_set_completed(self, level_set):
        if level_set == 400:
            return False

        if level_set not in self.save_data.completed:
            return False

        for i in range(1, l.levs[level_set] + 1):
            if i not in self.save_data.completed[level_set]:
                return False
        return True

    def is_available(self, level_index):
        level_set, level = level_index
        if level_set >= 300:
            return True

        if level == 1 or level == 0:
            return True
        if level_set not in self.save_data.completed:
            return False
        return level - 1 in self.save_data.completed[level_set]

    def complete_all(self):
        self.reset_completed()
        for key, val in l.levs.items():
            if key == 400:
                continue
            for i in range(1, val + 1):
                self.complete((key, i))

    def is_event_completed(self, index):
        return index in self.save_data.events

    def complete_event(self, index):
        if not self.is_event_completed(index):
            self.save_data.events.append(index)
            self.save()

    def is_shrek(self):
        return self.save_data.is_shrek

    def change_shrek(self):
        self.save_data.is_shrek = not self.save_data.is_shrek
        self.save()

    def tick_timer(self):       # !! doesn't save
        self.save_data.time += 1

    def get_timer_ticks(self):
        return self.save_data.time

    def reset_timer(self):
        self.save_data.reset_timer()
        self.save()


global_save_state = save_state()
