import os

from PIL import Image

# root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\src\\sprites\\"
root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\src\\sprites\\decorations\\"


def remove_extension(s):
    return s[:s.rfind('.')]


def image_iter():
    for path, subdirs, files in os.walk(root):
        for name in files:
            yield os.path.join(path, name)


for p in image_iter():
    im = Image.open(p)
    im.save(remove_extension(p) + ".gif")
