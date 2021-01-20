import os
import json
import levels as l


class save_data:
    def __init__(self, dic=None):
        print("IMPORTING DICT", dic)
        self.completed = {}
        self.events = []
        if dic is None:
            self.reset()
        else:
            for k, v in dic.items():
                setattr(self, k, v)

    def reset_completed(self):
        self.completed = {}

    def reset_events(self):
        self.events = []

    def reset(self):
        self.reset_events()
        self.reset_completed()

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
        with open('data/completed.txt', 'w') as file:
            json.dump(self.save_data.__dict__, file)

    def restore(self):
        if os.path.exists('data/completed.txt'):
            with open('data/completed.txt', 'r') as file:
                self.save_data = save_data(json.load(file))
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
        self.reset_completed()
        self.reset_events()

    def is_completed(self, level_index):
        level_set, level = level_index
        if level == 0:
            return self.is_set_completed(level_set)
        if level_set not in self.save_data.completed:
            return False

        return level in self.save_data.completed[level_set]

    def is_set_completed(self, level_set):
        if level_set == 2138:
            return False

        if level_set not in self.save_data.completed:
            return False

        for i in range(1, l.levs[level_set] + 1):
            if i not in self.save_data.completed[level_set]:
                return False
        return True

    def is_available(self, level_index):
        level_set, level = level_index
        if level_set >= 1000:
            return True

        if level == 1 or level == 0:
            return True
        if level_set not in self.save_data.completed:
            return False
        return level - 1 in self.save_data.completed[level_set]

    def complete_all(self):
        self.reset_completed()
        for key, val in l.levs.items():
            if key == 2138:
                continue
            for i in range(1, val + 1):
                self.complete((key, i))

    def is_event_completed(self, index):
        return index in self.save_data.events

    def complete_event(self, index):
        if not self.is_event_completed(index):
            self.save_data.events.append(index)
            self.save()


global_save_state = save_state()