import pygame
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkm
from game_files.imports.save_state import global_save_state
from game_files.imports.view_constants import global_view_constants as v
import game_files.imports.globals as g
import threading
from game_files.logic.commands import exit_game
import traceback
from game_files.imports.log import log


class exception_catching_tk(tk.Tk):
    def report_callback_exception(self, *args):
        err = "\n".join(traceback.format_exception(*args))
        log.error(err)
        exit_game()


if __name__ == "__main__":
    window = exception_catching_tk()
    window.title("klockilol4dupf launcher")
    window.minsize(width=300, height=200)
    window.iconbitmap("game_files/sprites/other/icon.ico")

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
    languages = ["Polish", "None"]
    combo_lan['values'] = languages
    combo_lan.current(0)
    combo_lan.grid(column=2, row=2)

    text = tk.StringVar()
    completion_label = tk.Label(window, textvariable=text)
    completion_label.grid(column=2, row=3)

    def update_completion():
        s = ""
        completion = global_save_state.get_completion()
        s += str(int(completion*100)) + "% completion"
        if completion == 1:
            true_completion = global_save_state.get_completion(True)
            s += "\n"
            s += str(int(true_completion*100)) + "% true completion"
        text.set(s)


    def bt_reset_method():
        answer = tkm.askyesno(title='Confirmation', message='Are you sure that you want to reset save file?')
        if answer:
            global_save_state.hard_erase_all()
        update_completion()


    def run_game():
        pygame.init()
        x, y, _ = resolutions[combo_res.current()]
        resolution = (x, y)
        v.change_resolution(resolution)
        if combo_lan.current() == 1:
            global_save_state.get_preference("witch", False)

        screen = pygame.display.set_mode((v.WINDOW_X, v.WINDOW_Y))
        import game_files.imports.all_sprites as s
        from game_files.logic.game_logic import game_logic
        pygame.display.set_icon(s.sprites["block_numeric_1"][0])
        pygame.display.set_caption('klockilol4dupf')

        clock = pygame.time.Clock()
        game = game_logic(screen)
        # src.set_stage((400, 1))
        game.set_stage((201, 0))
        while True:
            for event in pygame.event.get():
                game.event_handler(event)

            game.move()
            game.draw()

            pygame.display.update()
            clock.tick(v.FRAME_RATE)


    def bt_start_method():
        window.withdraw()

        # run_game()

        thread = threading.Thread(target=run_game())
        thread.start()


    tk.Button(window, text="Reset save", command=bt_reset_method, width=10).grid(column=1, row=3)
    tk.Button(window, text="Play", command=bt_start_method, width=20, height=2).grid(columnspan=3, row=4)

    update_completion()
    window.mainloop()

