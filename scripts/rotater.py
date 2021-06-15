from PIL import Image
from PIL import ImageEnhance
import os


root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\game_files\\sprites\\"
old_path = root + "blocks_bases\\"
new_path = root + "blocks\\"

def remove_extension(s):
    return s[:s.rfind('.')]

def image_iter():
    for path, subdirs, files in os.walk(old_path):
        for name in files:
            yield os.path.join(path, name), remove_extension(name)


rotatable = ["block_arrow", "ones_one", "block_piston", "pusher", "block_dual_arrow", "block_birdy_arrow"]

for path, name in image_iter():
    im = Image.open(path)
    if name in rotatable:
        for i in range(4):
            im.save(new_path + name + "_" + str(i) + ".gif")
            im = im.rotate(90)
    elif name[:-2] == "block_numeric":
        im.save(new_path + name + ".gif")
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        sharpener = ImageEnhance.Sharpness(im.convert('RGB'))
        im = sharpener.enhance(1)
        enhancer = ImageEnhance.Brightness(im)
        im = enhancer.enhance(0.5)
        im.save(new_path + name + "_dark" + ".gif")
        im.putalpha(64)
        im.save(new_path + name + "_invisible_dark" + ".gif")
    else:
        im.save(new_path + name + ".gif")


