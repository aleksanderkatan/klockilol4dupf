import math
import random
import os
#!! this file is supposed to work independently
#!! this is a simple 2d numeric and perma level generator
class level_generator:
    @staticmethod
    def size_of_index(index):
        return index//25 + 7

    @staticmethod
    def length_of_index(index):
        return int(index*0.6) + 40

    @staticmethod
    def out_of_range(x, y, x_max, y_max):
        if x < 0:
            return True
        if y < 0:
            return True
        if x >= x_max:
            return True
        if y >= y_max:
            return True
        return False

    def generate(self, index):
        size = level_generator.size_of_index(index)
        length = level_generator.length_of_index(index)

        grid = [[0 for i in range(size)] for j in range(size)]
        remaining_length = length
        x = random.randint(0, size-1)
        y = random.randint(0, size-1)
        grid[x][y] = 2137
        while remaining_length > 0:
            direc = random.randint(0, 4)
            amo = random.randint(0, size-2)
            if random.randint(0, 3) != 0:
                amo = int(amo/2)

            while amo > 0:
                new_x = x
                new_y = y
                if direc == 0:
                    new_x += 1
                elif direc == 1:
                    new_y -= 1
                elif direc == 2:
                    new_x -= 1
                else:
                    new_y += 1

                if level_generator.out_of_range(new_x, new_y, size, size):
                    break
                grid[new_x][new_y] += 1
                x = new_x
                y = new_y
                remaining_length -= 1
                amo -= 1
        if grid[x][y] > 1000:
            return self.generate(index)
        grid[x][y] = -2137

        f = open("levels/69/" + str(index) + ".txt", 'w')
        f.write(str(size)+"\n")
        f.write(str(size)+"\n")
        f.write("1\n")
        for row in grid:
            s = ""
            for blo in row:
                if blo < -1000:
                    s += "E"
                elif blo > 1000:
                    s += "S"
                elif blo > 8:
                    s += "0"
                elif blo == 0:
                    s += "."
                else:
                    s += str(blo)
            f.write(s + "\n")

    def mass_generate(self, amount):
        for i in range(1, amount+1):
            self.generate(i)

    def clean(self, amount):
        for i in range(1, amount+1):
            os.remove("levels/69/" + str(i) + ".txt")


generator = level_generator()
generator.mass_generate(136)
#generator.clean(10)
