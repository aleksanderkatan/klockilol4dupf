from src.strings.translation_bases import controls_display


class controls_display_pl(controls_display):
    title_left = "Sterowanie"
    title_right = "Komendy"
    left = \
        "TAB      - otwórz to okno\n" +\
        "ENTER    - wykonaj komendę\n" +\
        "\n" +\
        "A, ←     - w lewo\n" +\
        "W, ↑     - w górę\n" +\
        "D, →     - w prawo\n" +\
        "S, ↓     - w dół\n" +\
        "Q, SHIFT - cofnij ruch\n" +\
        "R, /     - zresetuj poziom\n" +\
        "ESC      - wyjdź z poziomu\n" +\
        "\n" +\
        "1..9     - tryb jednej warstwy\n" + \
        "         (istotny od strefy 4)"
    right = \
        "\'exit\'\n" +\
        "  - forsuje zamknięcie gry.\n" + \
        "  Zamknięcie okna zachowuje postępy.\n" + \
        "\n" +\
        "\'timer\'\n" +\
        "  - włącza/wyłącza zegar.\n" +\
        "\n" +\
        "\'witch\'\n" +\
        "  - włącza/wyłącza spotkania z wiedźmą.\n" +\
        "\n" +\
        "\'disappearing_blocks\'\n" +\
        "  - włącza/wyłącza animacje bloków.\n" +\
        "\n" +\
        "\'auto_reverse\'\n" +\
        "  - włącza/wyłącza auto-cofanie ruchów.\n" +\
        "\n" +\
        "\'speedrun <nazwa>\'\n" +\
        "  - USUWA ZAPIS i uruchamia speedrun.\n" +\
        "  Więcej informacji w README.\n" +\
        "\n" +\
        "\n"
    skip_message = "Naprawdę nie jestem w stanie przejść tego poziomu."
    bottom = \
        f"\'{skip_message}\'\n" +\
        "    - pomija aktualny poziom."
