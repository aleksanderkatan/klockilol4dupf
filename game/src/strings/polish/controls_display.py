from src.strings.translation_bases import controls_display


class controls_display_pl(controls_display):
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
    skip_message = "Naprawdę nie jestem w stanie przejść tego poziomu."
    bottom = \
        f"\'{skip_message}\'\n" +\
        "    - pomija aktualny poziom."
