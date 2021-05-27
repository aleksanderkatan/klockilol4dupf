import pygame
pygame.init()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkm
import game_files.globals as g
from game_files.save_state import global_save_state
from game_files.view_constants import global_view_constants as v


window = tk.Tk()
window.title("klockilol4dupf launcher")
window.minsize(width=300, height=200)
window.iconbitmap("game_files/sprites/icon.ico")

for i in range(0, 4+1+1):
    window.grid_rowconfigure(i, weight=1)
for i in range(0, 2+1+1):
    window.grid_columnconfigure(i, weight=1)


tk.Label(window, text="Resolution").grid(column=1, row=1)
combo_res = ttk.Combobox(window, state="readonly", width=25)
resolutions = [(2560, 1920, " (x2)"), (1920, 1080, " (last resort)"), (1600, 900, " (w i d e)"),
               (1280, 960, " (recommended)"), (900, 600, " (blurry)"), (640, 480, " (x1/2)"),
               (320, 240, " (x1/4, for lectures)"), (21, 37, " [*]")]
combo_res['values'] = [str(int(c[0])) + "x" + str(int(c[1])) + c[2] for c in resolutions]
combo_res.current(3)
combo_res.grid(column=2, row=1)

tk.Label(window, text="Language").grid(column=1, row=2)
combo_lan = ttk.Combobox(window, state="readonly", width=25)
languages = ["Polish"]
combo_lan['values'] = languages
combo_lan.current(0)
combo_lan.grid(column=2, row=2)


text = tk.StringVar()
completion_label = tk.Label(window, textvariable=text)
completion_label.grid(column=2, row=3)

def update_completion():
    completion = global_save_state.get_completion()
    completion = int(completion*100)
    text.set(str(completion) + "% completion")


def bt_reset_method():
    answer = tkm.askyesno(title='Confirmation', message='Are you sure that you want to reset save file?')
    if answer:
        global_save_state.reset()
    update_completion()


def bt_start_method():
    x, y, _ = resolutions[combo_res.current()]
    resolution = (x, y)
    v.change_resolution(resolution)
    import main                             # !! jank


tk.Button(window, text="Reset save", command=bt_reset_method, width=10).grid(column=1, row=3)
tk.Button(window, text="Start", command=bt_start_method, width=10).grid(column=1, row=4)


update_completion()
window.mainloop()

