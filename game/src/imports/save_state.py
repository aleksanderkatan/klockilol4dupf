import os
import pickle
import src.imports.levels as l
import src.imports.globals as g
from src.imports.log import log
import src.imports.utils as u
from src.imports.view_constants import global_view_constants as v

DATA_PATH = 'src/data'

PREFERENCE_DEFAULTS = {
    "auto_reverse": False,
    "timer": False,
    "witch": True,
    "shrek": False,
    "cheats": False,
}

# how are preferences different from above?
PREFERENCE_SPEEDRUN_CHANGES = {
    "auto_reverse": True,
    "timer": True,
    "witch": False,
}



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


class save_state:
    def __init__(self, index, read_only=False):
        log.info(f"Save instance created, index: {index}, readonly: {read_only}.")
        self.path = f"{DATA_PATH}/save_slot_{index}/"
        self.cached = {}
        self.read_only = read_only

        if self.read_only:
            return

        self.hard_restore("completed", completed_levels())
        self.hard_restore("events", set())
        self.hard_restore("time", 0)
        if self.get("time", 0) > 0:
            self.increase_value("time", 0, amount=v.FRAME_RATE * g.AUTO_SAVE_INTERVAL)  # prevent cheesing

    def _save_pickle(self, key, data):
        if self.read_only:
            log.warning(f"Trying to save in a readonly save instance! key: {key}, data: {data}")
            return

        file_path = self.path + key + ".pk"
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

    def _read_pickle(self, key, default_data):
        file_path = self.path + key + ".pk"
        if not os.path.isfile(file_path):
            return default_data
        with open(file_path, 'rb') as f:
            return pickle.load(f)

    def hard_save(self, key, data):
        self.cached[key] = data
        self._save_pickle(key, data)

    def hard_restore(self, key, default_data):
        result = self._read_pickle(key, default_data)
        self.cached[key] = result
        return result

    def get(self, key, default_data):
        if key not in self.cached:
            self.hard_restore(key, default_data)
        # !! fails because I fell for double import trap. TODO: resolve this
        # ??
        # if not (self.cached[key], type(default_data)):
        #     log.error(
        #         f"Wrong data type. Cached: {self.cached[key]} of type {type(self.cached[key])}, expected {type(default_data)}")
            # self.cached[key] = default_data
        return self.cached[key]

    def set(self, key, data):
        self.cached[key] = data

    def hard_save_all(self):
        for key, value in self.cached.items():
            self.hard_save(key, value)

    def hard_erase_all(self):
        files = os.listdir(self.path)
        files = [file for file in files if file.endswith(".pk")]
        for file in files:
            path = os.path.join(self.path, file)
            os.remove(path)
        self.cached = {}

    # utility uses

    def increase_value(self, key, default_data, amount=1, hard_save=False):
        current_value = self.get(key, default_data)
        new_value = current_value + amount
        self.set(key, new_value)
        if hard_save:
            self.hard_save(key, new_value)

    # new save
    def set_name(self, name):
        self.hard_save("name", name)

    def get_name(self):
        return self.get("name", None)

    def set_language(self, language):
        self.hard_save("language", language)

    def get_language(self):
        return self.get("language", "English")

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
        if zone_index >= 400 or (100 < zone_index < 200) or zone_index == 206:
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
        key = "moves_direction_" + str(direction.value)
        self.increase_value(key, 0)

    def log_reverse(self):
        self.increase_value("reverses", 0)

    def log_auto_reverse(self):
        self.increase_value("auto_reverses", 0)

    def log_reset(self):
        self.increase_value("resets", 0)

    def log_escape(self):
        self.increase_value("escapes", 0)

    # queries

    def get_preference(self, preference):
        if preference not in PREFERENCE_DEFAULTS:
            raise RuntimeError(f"Unknown preference {preference}")
        return self.get(preference, PREFERENCE_DEFAULTS[preference])

    def set_preference(self, preference, value):
        if preference not in PREFERENCE_DEFAULTS:
            raise RuntimeError(f"Unknown preference {preference}")
        self.hard_save(preference, value)

    def load_speedrun_preferences(self):
        for preference, value in PREFERENCE_DEFAULTS.items():
            if preference in PREFERENCE_SPEEDRUN_CHANGES:
                self.set_preference(preference, PREFERENCE_SPEEDRUN_CHANGES[preference])
            else:
                self.set_preference(preference, value)

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

    def get_completion(self, true=False):
        if not true:
            zones = l.base_zones
        else:
            zones = l.base_zones + l.extra_zones

        result = 0
        total = 0
        for i in zones:
            total += l.levs[i]
            for j in range(1, l.levs[i] + 1):
                if self.is_level_completed((i, j)):
                    result += 1
        return result / total

    def get_logged_keys(self):
        message = "Remembered key presses:\n"
        t = {0: "right", 1: "up", 2: "left", 3: "down"}
        for key, value in t.items():
            message += value + ": " + str(self.get("moves_direction_" + str(key), 0)) + "\n"
        message += "reverses: " + str(self.get("reverses", 0)) + "\n"
        message += "auto-reverses: " + str(self.get("auto_reverses", 0)) + "\n"
        message += "resets: " + str(self.get("resets", 0)) + "\n"
        message += "escapes: " + str(self.get("escapes", 0)) + "\n"
        return message

    def get_all_stats(self):
        message = f"Completion: {int(self.get_completion() * 100)}%\n"
        message += f"True completion: {int(self.get_completion(True) * 100)}%\n"
        message += f"In-game time: " + u.ticks_to_time(self.get("time", 0)) + "\n"
        message += self.get_logged_keys()
        return message

