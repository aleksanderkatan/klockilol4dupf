import os

root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\game_files\\levels\\"


def remove_extension(s):
    return s[:s.rfind('.')]

def path_iter():
    for path, subdirs, files in os.walk(root):
        for name in files:
            yield os.path.join(path, name)


for p in path_iter():
    os.rename(p, remove_extension(p) + ".lv")


