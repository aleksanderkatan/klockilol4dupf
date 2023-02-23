import traceback
import tkinter as tk
from tkinter import ttk
import src.imports.globals as g
from src.imports.log import log
from src.logic.commands import exit_game


class exception_catching_tk(tk.Tk):
    def report_callback_exception(self, *args):
        err = "\n".join(traceback.format_exception(*args))
        log.error(err)
        exit_game()


def create_launcher_window():
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






