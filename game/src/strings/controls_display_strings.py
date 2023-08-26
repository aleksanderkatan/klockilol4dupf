class controls_display_strings:
    title_left = ""
    title_right = ""
    left = ""
    right = ""
    bottom = ""


class controls_display_strings_pl(controls_display_strings):
    title_left = "Sterowanie"
    title_right = "Komendy"
    left = \
        "A, ←     - w lewo\n" +\
        "W, ↑     - w górę\n" +\
        "D, →     - w prawo\n" +\
        "S, ↓     - w dół\n" +\
        "Q, SHIFT - cofnij ruch\n" +\
        "R, /     - zresetuj poziom\n" +\
        "ESC      - wyjdź z poziomu\n" +\
        "TAB      - pomoc\n" +\
        "ENTER    - włącz konsolę"
    right = \
        "\'exit\'\n" +\
        "    - forsuje zamknięcie gry.\n" + \
        "    Zamknięcie okna zachowuje postępy.\n" + \
        "\n" +\
        "\'disappearing_blocks\'\n" +\
        "    - włącza/wyłącza animacje bloków.\n" +\
        "\n" +\
        "\'auto_reverse\'\n" +\
        "    - włącza/wyłącza auto-cofanie ruchów.\n" +\
        "\n" +\
        "\'timer\'\n" +\
        "    - włącza/wyłącza zegar.\n" +\
        "\n" +\
        "\'witch\'\n" +\
        "    - włącza/wyłącza spotkania z wiedźmą.\n" +\
        "\n" +\
        "\'speedrun <nazwa>\'\n" +\
        "    - !USUWA ZAPIS! i uruchamia speedrun.\n" +\
        "    Po więcej informacji zajrzyj do README.\n" +\
        "\n" +\
        "\n"
    bottom = \
        "\'Naprawdę nie jestem w stanie przejść tego poziomu.\'\n" +\
        "    - pomija aktualny poziom."



class controls_display_strings_en(controls_display_strings):
    title_left = "Controls"
    title_right = "Commands"
    left = \
        "A, ←     - go left\n" +\
        "W, ↑     - go up\n" +\
        "D, →     - go right\n" +\
        "S, ↓     - do down\n" +\
        "Q, SHIFT - undo a move\n" +\
        "R, /     - reset the stage\n" +\
        "ESC      - exit the stage\n" +\
        "TAB      - help\n" +\
        "ENTER    - open the console"
    right = \
        "\'exit\'\n" +\
        "    - forces the game to shut down.\n" +\
        "    Closing the window keeps your progress.\n" +\
        "\n" +\
        "\'disappearing_blocks\'\n" +\
        "    - switches block animation.\n" +\
        "\n" +\
        "\'auto_reverse\'\n" +\
        "    - switches auto move reverse on death.\n" +\
        "\n" +\
        "\'timer\'\n" +\
        "    - switches the timer.\n" +\
        "\n" +\
        "\'witch\'\n" +\
        "    - switches the witch encounters.\n" +\
        "\n" +\
        "\'speedrun <nazwa>\'\n" +\
        "    - DELETES YOUR SAVE and starts a speedrun.\n" +\
        "    For more info read the README.\n" +\
        "\n" +\
        "\n"
    bottom = \
        "\'I really can't beat this level, please help me.\'\n" +\
        "    - skips the current stage."


def get(language):
    match language.lower():
        case "polish":
            return controls_display_strings_pl
        case "english":
            return controls_display_strings_en
    raise RuntimeError(f"Invalid language \"{language}\"")
