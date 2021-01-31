import random
# !! this file is supposed to work independently
# !! this is a simple 2d numeric, perma, ice, jump and arrow level generator

class better_level_generator:
    def __init__(self, x, y, ice, jump2, jump3, arrow, length, redirect):
        self.x = x
        self.y = y
        self.length = length
        self.redirect = redirect
        self.grid = []
        for i in range(self.x):
            arr = []
            for j in range(self.y):
                arr.append((0, '-'))
            self.grid.append(arr)

        for i in range(ice):
            x = random.randint(1, self.x-2)
            y = random.randint(1, self.y-2)
            self.grid[x][y] = (0, "I")

        for i in range(jump2):
            x = random.randint(2, self.x-3)
            y = random.randint(2, self.y-3)
            self.grid[x][y] = (0, "J2")

        for i in range(jump3):
            x = random.randint(3, self.x-4)
            y = random.randint(3, self.y-4)
            self.grid[x][y] = (0, "J3")

        for i in range(arrow):
            x = random.randint(1, self.x-2)
            y = random.randint(1, self.y-2)
            direct = random.randint(0, 3)
            if direct == 0:
                self.grid[x][y] = (0, ">")
            if direct == 1:
                self.grid[x][y] = (0, "^")
            if direct == 2:
                self.grid[x][y] = (0, "<")
            if direct == 3:
                self.grid[x][y] = (0, "v")

    def out_of_range(self, pos):
        x, y = pos
        if x < 0:
            return True
        if y < 0:
            return True
        if x >= self.x:
            return True
        if y >= self.y:
            return True
        return False

    @staticmethod
    def next_pos(pos, direction):
        new_x, new_y = pos
        if direction == 0:
            new_x += 1
        elif direction == 1:
            new_y -= 1
        elif direction == 2:
            new_x -= 1
        else:
            new_y += 1
        return new_x, new_y

    @staticmethod
    def transpose(array):
        x = len(array)
        y = len(array[0])

        result = []
        for i in range(y):
            arr = []
            for j in range(x):
                arr.append(array[j][i])
            result.append(arr)
        return result

    def generate(self, file):
        direction = random.randint(0, 4)
        x = random.randint(1, self.x-2)
        y = random.randint(1, self.y-2)

        self.grid[x][y] = (0, 'S')

        for i in range(self.length):
            # set direction
            if self.grid[x][y][1] == 'I':
                pass
            elif self.grid[x][y][1] == '>':
                direction = 0
            elif self.grid[x][y][1] == '^':
                direction = 1
            elif self.grid[x][y][1] == '<':
                direction = 2
            elif self.grid[x][y][1] == 'v':
                direction = 3
            elif random.randint(0, self.redirect) == 0 or (x == 0 or y == 0 or x == self.x-1 or y == self.y - 1):
                direction = random.randint(0, 3)

            new_direction = direction
            while self.out_of_range(better_level_generator.next_pos((x, y), new_direction)):
                new_direction = random.randint(0, 3)
            direction = new_direction
            # direction is set

            if self.grid[x][y][1] == 'J2':
                new_x, new_y = \
                    better_level_generator.next_pos(better_level_generator.next_pos((x, y), direction), direction)
            elif self.grid[x][y][1] == 'J3':
                new_x, new_y = \
                    better_level_generator.next_pos(better_level_generator.next_pos(better_level_generator.next_pos((x, y), direction), direction), direction)
            else:

                new_x, new_y = better_level_generator.next_pos((x, y), direction)

            self.grid[x][y] = (self.grid[x][y][0]+1, self.grid[x][y][1])
            x = new_x
            y = new_y

        if self.grid[x][y][1] != '-':
            return "FAIL"
        self.grid[x][y] = (self.grid[x][y][0], 'E')

        self.grid = better_level_generator.transpose(self.grid)

        maks = 0
        total = 0

        jumps = []

        f = open(file, 'w')
        f.write(str(self.x)+"\n")
        f.write(str(self.y)+"\n")
        f.write("1\n")
        for row in self.grid:
            s = ""
            for blo in row:
                num, nam = blo
                if num == 0 and nam != 'E':
                    s += "."
                else:
                    if nam == '-':
                        if num < 9:
                            s += str(num)
                            total += num
                        else:
                            s += '0'
                        maks = max(maks, num)
                    else:
                        if nam[0] == 'J':
                            s += nam[0]
                            jumps.append(nam[1])
                        else:
                            s += nam

            f.write(s + "\n")
        f.write("\n")
        f.write("jumps ")
        for j in jumps:
            f.write(j + " ")
        f.write("\n")
        f.close()

        return maks, total

def generate(index, x, y, ice, jump2, jump3, arrow, length, redirect, max_num=None, min_total=None):
    while True:
        generator = better_level_generator(x, y, ice, jump2, jump3, arrow, length, redirect)
        res = generator.generate("../levels/102/" + str(index) + ".txt")
        if res != "FAIL":
            maks, total = res
            if max_num is not None and maks > max_num:
                print(ind, "num fail")
                continue
            if min_total is not None and total < min_total:
                print(ind, "length fail")
                continue
            print(ind, "success")
            break
        print(ind, "S/E fail")


for ind in range(1, 100):
    #generate(index=ind, x=9, y=9, ice=0, jump2=0, jump3=15, arrow=0, length=50, redirect=7, max_num=3, min_total=30)
    generate(index=ind, x=11, y=11, ice=10, jump2=10, jump3=10, arrow=20, length=60, redirect=7, max_num=3, min_total=30)
    #generate(index=ind, x=100, y=100, ice=0, jump2=0, jump3=0, arrow=0, length=5000, redirect=15, max_num=7, min_total=30)
