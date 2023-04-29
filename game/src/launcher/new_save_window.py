import tkinter as tk
from tkinter import ttk

from src.launcher.new_save_data import new_save_data


def create_new_save_window(action_to_perform_with_data):
    window = tk.Tk()
    window.title(f"New save")
    window.minsize(width=250, height=200)
    window.iconbitmap("src/sprites/other/icon.ico")

    for i in range(0, 2):
        window.grid_columnconfigure(i, weight=1)
    for i in range(0, 6):
        window.grid_rowconfigure(i, weight=1)

    name_label = tk.Label(window, text="Name")
    name_label.grid(column=0, row=0, padx=10, sticky=tk.E)
    name_textbox = tk.Text(window, height=1, width=17)
    name_textbox.grid(column=1, row=0, sticky=tk.W)

    languages = ["Polish", "English"]
    language_label = tk.Label(window, text="Language")
    language_label.grid(column=0, row=1, padx=10, sticky=tk.E)
    combo_languages = ttk.Combobox(window, state="readonly", width=20)
    combo_languages['values'] = languages
    combo_languages.current(0)
    combo_languages.grid(column=1, row=1, sticky=tk.W)

    auto_reverse_var = tk.BooleanVar()
    auto_reverse_var.set(True)
    check_auto_reverse = tk.Checkbutton(window, text="Auto reverse mistakes", variable=auto_reverse_var)
    check_auto_reverse.grid(column=0, row=2, columnspan=2, padx=25, sticky=tk.W)

    enable_timer_var = tk.BooleanVar()
    check_enable_timer = tk.Checkbutton(window, text="Enable timer", variable=enable_timer_var)
    check_enable_timer.grid(column=0, row=3, columnspan=2, padx=25, sticky=tk.W)

    skip_witch_var = tk.BooleanVar()
    check_skip_witch = tk.Checkbutton(window, text="Skip dialogue", variable=skip_witch_var)
    check_skip_witch.grid(column=0, row=4, columnspan=2, padx=25, sticky=tk.W)

    create_button = tk.Button(window, text="Play!", width=20, height=3)
    create_button.grid(column=0, row=5, columnspan=2)

    def play_action():
        name = name_textbox.get("1.0", "end-1c")
        language = languages[combo_languages.current()]
        auto_reverse = auto_reverse_var.get()
        timer = enable_timer_var.get()
        skip_witch = skip_witch_var.get()
        data = new_save_data(name, language, auto_reverse, timer, skip_witch)

        window.destroy()

        action_to_perform_with_data(data)

    create_button.configure(command=play_action)

    return window
