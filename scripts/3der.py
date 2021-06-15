from PIL import Image
import os


old_size = (32, 32)
new_size = (32, 40)

root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\game_files\\sprites\\"
old_path = root + "blocks\\"
new_path = root + "blocks_3d\\"

def remove_extension(s):
    return s[:s.rfind('.')]

def image_iter():
    for path, subdirs, files in os.walk(old_path):
        for name in files:
            yield os.path.join(path, name), remove_extension(name)


def generate_new_image(image: Image, name):
    if name in ["level_available", "level_unavailable",
                "ones_one_1", "ones_one_2", "ones_one_3", "ones_one_4"]:
        return image
    ans = Image.new('RGBA', new_size, (255, 255, 255))
    for i in reversed(range(0, 8+1)):
        ans.paste(im, (0, i))
    return ans


for p, name in image_iter():
    im = Image.open(p)
    im = generate_new_image(im, name)
    im.save(new_path + name + ".gif")



