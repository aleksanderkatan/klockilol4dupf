import os

# root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf\\game_files"
root = "D:\\Novvy_foldeer\\Gry\\moje\\klockilol4dupf"

def get_extension(s):
    return s[s.rfind('.')+1:]


d = {}
for path, subdirs, files in os.walk(root):
    for name in files:
        ex = get_extension(name)
        if ex not in d:
            d[ex] = []
        d[ex].append(os.path.join(path, name))

for key, value in d.items():
    print(key, len(value))
print()


for ext in ["txt", "py", "md"]:
    files = 0
    lines = 0
    characters = 0

    d[ext] = d[ext] if ext in d else []
    values = d[ext]
    for file in values:
        files += 1
        with open(file, encoding="utf-8") as f:
            s = f.read()
            lines += s.count("\n") + 1
            characters += len(s)

    print(f"ext: {ext}\nfiles: {files}\nlines: {lines}\ncharacters: {characters}\n")


