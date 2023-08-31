from src.strings.translation_bases import controls_display


class controls_display_en(controls_display):
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
    skip_message = "I really can't beat this level, please help me."
    bottom = \
        f"\'{skip_message}\'\n" +\
        "    - skips the current stage."

