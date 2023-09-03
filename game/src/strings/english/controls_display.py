from src.strings.translation_bases import controls_display


class controls_display_en(controls_display):
    title_left = "Controls"
    title_right = "Commands"
    left = \
        "TAB, `   - open this window\n" +\
        "ENTER    - execute a command\n" + \
        "\n" +\
        "A, ←     - go left\n" +\
        "W, ↑     - go up\n" +\
        "D, →     - go right\n" +\
        "S, ↓     - do down\n" +\
        "Q, SHIFT - undo a move\n" +\
        "R, /     - reset the stage\n" +\
        "ESC      - exit the stage\n" +\
        "\n" +\
        "1..9     - single layer mode\n" +\
        "         (useful in zones 4+)"
    right = \
        "\'exit\'\n" +\
        "  - forces the game to shut down.\n" +\
        "  Closing the window keeps your progress.\n" +\
        "\n" +\
        "\'timer\'\n" +\
        "  - switches the timer.\n" +\
        "\n" +\
        "\'witch\'\n" +\
        "  - switches the witch encounters.\n" +\
        "\n" +\
        "\'disappearing_blocks\'\n" +\
        "  - switches block animation.\n" +\
        "\n" +\
        "\'auto_reverse\'\n" +\
        "  - switches auto move reverse on death.\n" +\
        "\n" +\
        "\'speedrun <name>\'\n" +\
        "  - DELETES YOUR SAVE, starts a speedrun.\n" +\
        "  For more info read the README.\n" +\
        "\n" +\
        "\n"
    skip_message = "I really can't beat this level, please help me."
    bottom = \
        f"\'{skip_message}\'\n" +\
        "  - skips the current stage."

