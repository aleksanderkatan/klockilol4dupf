import os
import io
import itertools
from game.game_files.imports.log import log
from game_files.witch.witch_event import witch_event

events_path = "game_files/witch/events"
events = []


def files(root):
    for path, _, fs in os.walk(root):
        for name in fs:
            yield os.path.join(path, name)


for file_path in files(events_path):
    with io.open(file_path, mode="r", encoding="UTF-8") as f:
        level = None
        pos = None
        messages = []
        line = None

        file = ""
        for l in itertools.chain(f, ["\n"]):
            file += l
        # let + add to same message
        file = file.replace("\n+", "\\n")

        mode = 0
        try:
            for l in file.split("\n"):
                line = l.strip()

                if line == "":
                    if messages:
                        events.append(witch_event(where=(level, pos), messages=messages, index=len(events)))
                        level = None
                        pos = None
                        messages = []
                        mode = 0
                elif mode == 0:
                    level = line.split()
                    level = (int(level[0]), int(level[1]))
                    mode = 1
                elif mode == 1:
                    if line == "None":
                        pos = None
                    else:
                        pos = line.split()
                        pos = (int(pos[0]), int(pos[1]), int(pos[2]))
                    mode = 2
                elif mode == 2:
                    messages.append(line)
        except:
            log.error("level:", level)
            log.error("pos:", pos)
            log.error("messages:", messages)
            log.error("line:", line)
            log.error("file:", file_path)
            raise RuntimeError("Error while loading witch events")


# the mess
# v^v>^^^^^<>vvvvvv^<<^>^>^<<>>>^<^>vv<<<><v>>^<v><vv>>>>v^>v<^>vvv<<>^^>><<vv<^>><<v<^^^<vv>>^^><<^>vv>^><<<v<<<<<>v<^>>>>>v>^v>>^^
