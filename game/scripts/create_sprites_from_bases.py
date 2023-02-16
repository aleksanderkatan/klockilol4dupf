from PIL import Image
from PIL import ImageEnhance
import os

root = "C:\\Users\\oloiw\\PycharmProjects\\klockilol4dupf\\game\\src\\sprites\\"
old_path = root + "blocks_bases\\"
new_path = root + "blocks\\"

empty = Image.open(old_path + "empty.gif").convert("RGBA")


def remove_extension(s):
    return s[:s.rfind('.')]


def image_iter():
    for path, subdirs, files in os.walk(old_path):
        for name in files:
            yield os.path.join(path, name), remove_extension(name)


rotatable_4 = ["block_arrow", "ones_one", "block_piston",
               "pusher", "block_dual_arrow", "block_birdy_arrow", "block_moving_arrow",
               "block_pm_arrow"]

rotatable_2 = ["block_pm_dual_arrow"]

for path, name in image_iter():
    im = Image.open(path)
    # im = im.convert("RGB")
    if name in rotatable_4:
        for i in range(4):
            im.save(new_path + name + "_" + str(i) + ".gif")
            im = im.rotate(90)
    elif name in rotatable_2:
        for i in range(2):
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
        im = im.convert("RGBA")
        im = Image.blend(empty, im, alpha=.3)
        im.save(new_path + name + "_invisible_dark" + ".gif")

        im = Image.open(path)
        enhancer = ImageEnhance.Contrast(im.convert('RGB'))
        im = enhancer.enhance(0.2)
        im.save(new_path + name + "_pm" + ".gif")
    elif name == "block_pm_triggerable":
        im.save(new_path + name + "_on" + ".gif")
        im = im.convert("RGBA")
        im = Image.blend(empty, im, alpha=.3)
        im.save(new_path + name + "_off" + ".gif")
    else:
        im.save(new_path + name + ".gif")
