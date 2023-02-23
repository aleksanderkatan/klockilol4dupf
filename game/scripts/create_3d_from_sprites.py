import os

from PIL import Image

old_size = (32, 32)
new_size = (32, 40)

root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\src\\sprites\\"
old_path = root + "blocks\\"
new_path = root + "blocks_3d\\"
# empty = Image.new("CMYK", (32, 40), (0, 0, 0, 0))
# empty.putalpha(120)
empty = Image.open(old_path + "empty.gif")
empty = empty.resize(new_size)
empty = empty.convert("RGBA")


def remove_extension(s):
    return s[:s.rfind('.')]


def image_iter():
    for path, subdirs, files in os.walk(old_path):
        for name in files:
            yield os.path.join(path, name), remove_extension(name)


def generate_new_image(image: Image, name):
    if name in ["level_available", "level_unavailable",
                "ones_one_0", "ones_one_1", "ones_one_2", "ones_one_3"]:
        return image
    image = image.convert("RGBA")
    ans = empty.copy()
    # ans = Image.alpha_composite(empty.copy(), image)
    for i in reversed(range(0, 8 + 1)):
        ans.paste(image, (0, i), mask=image)
    return ans


for path, name in image_iter():
    im = Image.open(path)
    im = generate_new_image(im, name)
    im.save(new_path + name + ".gif")
