s = """
....RRRRRR..
...R111111R.
...R1RRRR21R
..R12121R1R.
.R1RRR1R12R.
R121211RR1R.
R1RR1RR..E..
R1RRR1R.....
R211131R....
R1RRR1RRR...
.R..R1111S..
.....RRRR...
"""

level = s.split("\n")

for line in reversed(level):
    for char in reversed(line):
        print(char, end="")
    print()
