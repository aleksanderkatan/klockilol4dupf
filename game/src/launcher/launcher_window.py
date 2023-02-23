import tkinter as tk
import traceback
from tkinter import messagebox as tkm
from tkinter import ttk

import src.imports.globals as g
from src.imports.log import log
from src.imports.save_management import create_new_save, delete_save, get_saves_status, get_save
from src.launcher.new_save_window import create_new_save_window
from src.launcher.run_game import run_game
from src.logic.commands import exit_game


class exception_catching_tk(tk.Tk):
    def report_callback_exception(self, *args):
        err = "\n".join(traceback.format_exception(*args))
        log.error(err)
        exit_game()


def _create_launcher_window_no_logic():
    window = exception_catching_tk()
    window.title(f"klockilol4dupf {g.VERSION}")
    window.minsize(width=540, height=200)
    window.iconbitmap("src/sprites/other/icon.ico")

    for i in range(0, 3 + 1 + 1):
        window.grid_columnconfigure(i, weight=1)
    for i in range(0, 4 + 1 + 1):
        window.grid_rowconfigure(i, weight=1)

    tk.Label(window, text="Resolution").grid(column=1, row=1)
    combo_res = ttk.Combobox(window, state="readonly", width=25)
    combo_res.grid(column=2, columnspan=2, row=1)

    play1 = tk.Button(window, text="New save", width=20, height=5)
    play2 = tk.Button(window, text="New save", width=20, height=5)
    play3 = tk.Button(window, text="New save", width=20, height=5)
    play1.grid(column=1, row=3, padx=20)
    play2.grid(column=2, row=3, padx=0)
    play3.grid(column=3, row=3, padx=20)

    del1 = tk.Button(window, text="Delete", width=10, height=1)
    del2 = tk.Button(window, text="Delete", width=10, height=1)
    del3 = tk.Button(window, text="Delete", width=10, height=1)
    del1.grid(column=1, row=4)
    del2.grid(column=2, row=4)
    del3.grid(column=3, row=4)

    return window, combo_res, ((play1, del1), (play2, del2), (play3, del3))


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
        answer = tkm.askyesno(title='Confirmation',
                              message=f'Are you sure that you want to delete save file {save_index}?')
        if not answer:
            return
        delete_save(save_index)
        delete_button.configure(state=tk.DISABLED)
        play_button.configure(command=create_new_save_action(launcher_window, resolution_combobox, save_index))
        play_button.configure(text="New save")

    return button_action


def create_launcher_window():
    statuses = get_saves_status()

    window, resolution_combo, save_navigation_buttons = _create_launcher_window_no_logic()

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
            play.configure(text=f"{name}\n\n{completion}")
            play.configure(command=create_play_action(window, resolution_combo, index))
    return window
