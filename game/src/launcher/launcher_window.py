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



# import pygame
# from tkinter import messagebox as tkm
# 
# from src.imports.view_constants import global_view_constants as v
# import threading
#
#
#
#     # tk.Label(window, text="Language").grid(column=1, row=2)
#     # combo_lan = ttk.Combobox(window, state="readonly", width=25)
#     # languages = ["Polish", "None"]
#     # combo_lan['values'] = languages
#     # combo_lan.current(0)
#     # combo_lan.grid(column=2, row=2)
#
#     text = tk.StringVar()
#     completion_label = tk.Label(window, textvariable=text)
#     # completion_label.grid(column=2, row=3)
#     completion_label.grid(column=2, row=2)
#
#
#
#     def run_game():
#         pygame.init()
#         x, y, _ = resolutions[combo_res.current()]
#         resolution = (x, y)
#         v.change_resolution(resolution)
#         # if combo_lan.current() == 1:
#         #     g.global_save_state.get_preference("witch", False)
#
#         screen = pygame.display.set_mode((v.WINDOW_X, v.WINDOW_Y))
#         import src.imports.all_sprites as s
#         from src.logic.game_logic import game_logic
#         pygame.display.set_icon(s.sprites["block_numeric_1"][0])
#         pygame.display.set_caption('klockilol4dupf')
#
#         clock = pygame.time.Clock()
#         game = game_logic(screen)
#         game.set_stage((400, 1))
#         while True:
#             for event in pygame.event.get():
#                 game.event_handler(event)
#
#             game.move()
#             game.draw()
#
#             pygame.display.update()
#             clock.tick(v.FRAME_RATE)
#
#
#     def bt_start_method():
#         window.withdraw()
#
#         # run_game()
#
#         thread = threading.Thread(target=run_game())
#         thread.start()
#
#
#     tk.Button(window, text="Reset save", command=bt_reset_method, width=10).grid(column=1, row=2)
#     tk.Button(window, text="Play", command=bt_start_method, width=20, height=2).grid(columnspan=3, row=3)
#
#     update_completion()
#     window.mainloop()





