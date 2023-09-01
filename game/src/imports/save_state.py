import os
import pickle

import src.imports.globals as g
import src.imports.levels as l
import src.imports.utils as u
from src.imports.log import log
from src.imports.view_constants import global_view_constants as v

DATA_PATH = 'data'

PREFERENCE_DEFAULTS = {
    "auto_reverse": False,
    "disappearing_blocks": True,
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


class level_statuses:
    def __init__(self):
        self.statuses = {}

    def _set_level_status(self, level_index, status):
        if level_index not in self.statuses:
            self.statuses[level_index] = l.level_status.UNAVAILABLE
        self.statuses[level_index] = max(status, self.statuses[level_index])

    def _unlock_next(self, level_index):
        level_set, level = l.next_level(level_index)
        # if the next level is really a level and not just a stage
        if level != 0:
            self._set_level_status((level_set, level), l.level_status.AVAILABLE)

    def complete_level(self, level_index):
        self._set_level_status(level_index, l.level_status.COMPLETED)
        self._unlock_next(level_index)

    def skip_level(self, level_index):
        self._set_level_status(level_index, l.level_status.SKIPPED)
        self._unlock_next(level_index)

    def get_level_status(self, level_index):
        if not l.is_level(level_index):
            # raise RuntimeError(f"Attempted to check level status of non-level stage {level_index}")
            return l.level_status.AVAILABLE
            # !! what is this
        if level_index in self.statuses:
            return self.statuses[level_index]
        if level_index[1] == 1:
            return l.level_status.AVAILABLE
        return l.level_status.UNAVAILABLE

    def get_set_status(self, set_index):
        if set_index >= 400:
            return l.level_status.UNAVAILABLE

        if set_index not in l.levs:
            return l.level_status.UNAVAILABLE
            # !! runtime here?

        if l.levs[set_index] == 0:
            return l.level_status.COMPLETED

        status = l.level_status.COMPLETED
        for i in range(1, l.levs[set_index] + 1):
            if (set_index, i) not in self.statuses:
                return l.level_status.UNAVAILABLE
            status = min(status, self.statuses[(set_index, i)])
        if status == l.level_status.AVAILABLE:
            status = l.level_status.UNAVAILABLE
        return status


class save_state:
    def __init__(self, index, read_only=False):
        log.info(f"Save instance created, index: {index}, readonly: {read_only}.")
        self.path = f"{DATA_PATH}/save_slot_{index}/"
        self.cached = {}
        self.read_only = read_only

        if self.read_only:
            return

        self.hard_restore("level_statuses", level_statuses())
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

    def hard_erase_all(self, exceptions=None):
        if exceptions is None:
            exceptions = []

        files = os.listdir(self.path)
        files = [file for file in files if file.endswith(".pk") and file[:-3] not in exceptions]
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

    def set_preset_spawn(self, spawn):
        self.hard_save("preset_spawn", spawn)

    def get_preset_spawn(self):
        return self.get("preset_spawn", None)

    def get_strings_path(self):
        return "src/strings/" + self.get("language", "English").lower() + "/"
    
    # levels

    def complete_level(self, level_index, hard_save):
        statuses = self.get("level_statuses", level_statuses())
        statuses.complete_level(level_index)

        if hard_save:
            self.hard_save("level_statuses", statuses)
            self.hard_save("time", self.get("time", 0))


    def skip_level(self, level_index, hard_save):
        statuses = self.get("level_statuses", level_statuses())
        statuses.skip_level(level_index)

        if hard_save:
            self.hard_save("level_statuses", statuses)
            self.hard_save("time", self.get("time", 0))

    def get_set_status(self, set_index):
        return self.get("level_statuses", level_statuses()).get_set_status(set_index)


    def complete_zone(self, zone_index, hard_save):
        if zone_index not in l.levs:
            log.error("No such zone", zone_index)
            return
        if zone_index >= 400 or (100 < zone_index < 200) or zone_index == 206:
            return
        for i in range(1, l.levs[zone_index] + 1):
            self.complete_level((zone_index, i), hard_save=False)
        if hard_save:
            self.hard_save("level_statuses", self.get("level_statuses", level_statuses()))

    def complete_all(self):
        for key in l.levs.keys():
            self.complete_zone(key, False)
        self.hard_save("level_statuses", self.get("level_statuses", level_statuses()))

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

    def get_level_status(self, level_index):
        return self.get("level_statuses", level_statuses()).get_level_status(level_index)

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
                if self.get_level_status((i, j)) in [l.level_status.COMPLETED]:
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
