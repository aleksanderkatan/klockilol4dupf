from src.launcher.launcher_window import create_launcher_window
from src.launcher.new_save_window import create_new_save_window
from src.launcher.run_game import run_game
from tkinter import messagebox as tkm
import tkinter as tk
from src.imports.save_management import create_new_save, delete_save, get_saves_status, get_save


resolutions = [
    (2560, 1920, " (x2)"),
    (1280, 960, " (recommended)"),
    (640, 480, " (x1/2)"),
    (320, 240, " (x1/4, for lectures)"),
    (21, 37, " [*]")]


def create_new_save_action(launcher_window, resolution_combobox, save_index):
    def button_action():
        resolution = resolutions[resolution_combobox.current()][0], resolutions[resolution_combobox.current()][1]

        def digest_data(new_save_data):
            save = create_new_save(save_index, new_save_data)
            run_game(resolution, save)

        launcher_window.destroy()
        new_save_window = create_new_save_window(digest_data)
        new_save_window.mainloop()

    return button_action


def create_play_action(launcher_window, resolution_combobox, save_index):
    def button_action():
        resolution = resolutions[resolution_combobox.current()][0], resolutions[resolution_combobox.current()][1]
        launcher_window.destroy()
        save = get_save(save_index)
        run_game(resolution, save)

    return button_action


def create_delete_action(launcher_window, play_button, delete_button, resolution_combobox, save_index):
    def button_action():
        delete_save(save_index)
        delete_button.configure(state=tk.DISABLED)
        play_button.configure(command=create_new_save_action(launcher_window, resolution_combobox, save_index))
        play_button.configure(text="New save")

    return button_action


if __name__ == "__main__":
    statuses = get_saves_status()

    window, resolution_combo, save_navigation_buttons = create_launcher_window()

    resolution_combo['values'] = [str(int(c[0])) + "x" + str(int(c[1])) + c[2] for c in resolutions]
    resolution_combo.current(1)

    for index, data in enumerate(zip(statuses, save_navigation_buttons), start=1):
        status, (play, delete) = data
        delete.configure(command=create_delete_action(window, play, delete, resolution_combo, index))
        if status is None:
            play.configure(command=create_new_save_action(window, resolution_combo, index))
            delete.configure(state=tk.DISABLED)
        else:
            name, completion = status
            play.configure(text=f"{name} {completion}")
            play.configure(command=create_play_action(window, resolution_combo, index))


    window.mainloop()
