from PIL import Image
import os

root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\game_files\\sprites\\"


def remove_extension(s):
    return s[:s.rfind('.')]

def image_iter():
    for path, subdirs, files in os.walk(root):
        for name in files:
            yield os.path.join(path, name)


for p in image_iter():
    im = Image.open(p)
    im.save(remove_extension(p) + ".gif")




