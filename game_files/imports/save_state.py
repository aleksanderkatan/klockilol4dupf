import os
import pickle
import game_files.imports.levels as l
import game_files.imports.globals as g
from game_files.imports.log import log

SAVE_FILE_PATH = 'game_files/data/completed.txt'

DATA_PATH = 'game_files/data/'

def _save_pickle(key, data):
    file_path = DATA_PATH + key + ".pk"
    with open(file_path, 'wb') as f:
        pickle.dump(data, f)

def _read_pickle(key, default_data):
    file_path = DATA_PATH + key + ".pk"
    if not os.path.isfile(file_path):
        return default_data
    with open(file_path, 'rb') as f:
        return pickle.load(f)


class completed_levels:
    def __init__(self):
        self.completed = {}

    def complete_level(self, level_index):
        level_set, level = level_index
        if level_set not in self.completed:
            self.completed[level_set] = set()
        self.completed[level_set].add(level)

    def is_set_completed(self, level_set):
        if level_set >= 400:
            return False

        if level_set not in l.levs:
            return False

        if l.levs[level_set] == 0:
            return True

        if level_set not in self.completed:
            return False

        for i in range(1, l.levs[level_set] + 1):
            if i not in self.completed[level_set]:
                return False
        return True

    def is_level_completed(self, level_index):
        level_set, level = level_index
        if level == 0:
            return self.is_set_completed(level_set)
        if level_set not in self.completed:
            return False

        return level in self.completed[level_set]

    def is_available(self, level_index):
        level_set, level = level_index
        if level_set >= 300 or level_set == 206:
            return True

        if level == 1 or level == 0:
            return True
        if level_set not in self.completed:
            return False
        return level - 1 in self.completed[level_set]


class new_save_state:
    def __init__(self):
        self.cached = {}
        self.hard_restore("completed", completed_levels())
        self.hard_restore("events", set())
        self.hard_restore("time", 0)
        self.increase_value("time", 0, amount=g.FRAMERATE*g.AUTO_SAVE_INTERVAL, hard_save=True)     # prevent cheesing

    def hard_save(self, key, data):
        self.cached[key] = data
        _save_pickle(key, data)

    def hard_restore(self, key, default_data):
        result = _read_pickle(key, default_data)
        self.cached[key] = result
        return result

    def get(self, key, default_data):
        if key not in self.cached:
            self.hard_restore(key, default_data)
        assert type(self.cached[key]) is type(default_data)
        return self.cached[key]

    def set(self, key, data):
        self.cached[key] = data

    def hard_save_all(self):
        for key, value in self.cached.items():
            self.hard_save(key, value)

    def hard_erase_all(self):
        files = os.listdir(DATA_PATH)
        files = [file for file in files if file.endswith(".pk")]
        for file in files:
            path = os.path.join(DATA_PATH, file)
            os.remove(path)
        self.cached = {}

    # utility uses

    def increase_value(self, key, default_data, amount=1, hard_save=False):
        current_value = self.get(key, default_data)
        new_value = current_value + amount
        self.set(key, new_value)
        if hard_save:
            self.hard_save(key, new_value)

    # levels

    def complete_level(self, level_index, hard_save):
        completed = self.get("completed", completed_levels())
        completed.complete_level(level_index)

        if hard_save:
            self.hard_save("completed", completed)
            self.hard_save("time", self.get("time", 0))

    def complete_zone(self, zone_index, hard_save):
        if zone_index not in l.levs:
            log.error("No such zone", zone_index)
            return
        if zone_index >= 400 or (100 < zone_index < 200):
            log.warning("Not a completable zone:", zone_index)
            return
        for i in range(1, l.levs[zone_index] + 1):
            self.complete_level((zone_index, i), hard_save=False)
        if hard_save:
            self.hard_save("completed", self.get("completed", completed_levels()))

    def complete_all(self):
        for key in l.levs.keys():
            self.complete_zone(key, False)
        self.hard_save("completed", self.get("completed", completed_levels()))

    # events

    def complete_event(self, index):
        events = self.get("events", set())
        events.add(index)
        self.hard_save("events", events)

    # key logging
    # despite the name, this is used for logging actions
    # (multiple key presses in a single frame and text inputting are omitted)

    def log_move(self, direction):
        key = "moves_direction_" + str(direction)
        self.increase_value(key, 0)

    def log_reverse(self):
        self.increase_value("reverses", 0)

    def log_reset(self):
        self.increase_value("resets", 0)

    def log_escape(self):
        self.increase_value("escapes", 0)

    # queries

    def is_set_completed(self, level_set):
        completed = self.get("completed", completed_levels())
        return completed.is_set_completed(level_set)

    def is_level_completed(self, level_index):
        completed = self.get("completed", completed_levels())
        return completed.is_level_completed(level_index)

    def is_level_available(self, level_index):
        completed = self.get("completed", completed_levels())
        return completed.is_available(level_index)

    def is_event_completed(self, index):
        events = self.get("events", set())
        return index in events

    def get_completion(self):
        result = 0
        total = 0
        for i in range(1, 10+1):
            total += l.levs[i]
            for j in range(1, l.levs[i]+1):
                if self.is_level_completed((i, j)):
                    result += 1
        return result/total


global_save_state = new_save_state()
