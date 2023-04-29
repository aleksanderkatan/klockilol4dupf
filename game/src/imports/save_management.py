import os

from src.imports.log import log
from src.imports.save_state import save_state


def get_completion(save):
    s = ""
    completion = save.get_completion()
    s += str(int(completion * 100)) + "% completion"
    if completion == 1:
        true_completion = save.get_completion(True)
        s += "\n"
        s += str(int(true_completion * 100)) + "% true completion"
    return s


def _does_save_exist(index):
    return os.path.exists(f"src/data/save_slot_{index}")


def create_new_save(index, new_save_data):
    os.mkdir(f"src/data/save_slot_{index}")
    log.info(f"Creating save {index} with data {str(new_save_data)}")
    save = save_state(index)
    save.set_name(new_save_data.name)
    save.set_language(new_save_data.language)
    save.set_preference("auto_reverse", new_save_data.auto_reverse)
    save.set_preference("timer", new_save_data.timer)
    save.set_preference("witch", not new_save_data.skip_witch)
    return save


def get_save(index):
    return save_state(index)


def delete_save(index):
    temp_save_state = save_state(index)
    temp_save_state.hard_erase_all()
    os.rmdir(f"src/data/save_slot_{index}")
    log.info(f"Deleting save {index}.")


def get_saves_status():
    result = []
    for i in range(1, 4):
        if _does_save_exist(i):
            temp_save_state = save_state(i, read_only=True)
            name, completion = temp_save_state.get_name(), get_completion(temp_save_state)
            result.append((name, completion))
        else:
            result.append(None)
    return result
