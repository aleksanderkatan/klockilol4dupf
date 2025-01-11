import random


def generate():
    undertale_letters = ['p', 'i', 'o', 'y', 'g', 'r', 'l']
    size = 13

    grid = [[random.choice(undertale_letters) for _ in range(size)] for _ in range(size)]
    start_y = random.randint(1, 6) + random.randint(1, 6)-1
    end_y = random.randint(1, 6) + random.randint(1, 6)-1
    grid[start_y][0] = "S"
    grid[end_y][size-1] = "E"

    f = open("src/levels/104/0.lv", 'w')
    f.write(str(size) + "\n")
    f.write(str(size) + "\n")
    f.write("1\n")
    for row in grid:
        f.write("".join(row) + "\n")
    return True

