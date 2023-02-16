def linify_level_string(level_string):
    level_lines = level_string.split("\n")
    commentless_lines = [(0, "")]
    for index, line in enumerate(level_lines):
        pos = line.find("#")
        if pos != -1:
            line = line[:pos]
        if pos != 0:
            commentless_lines.append((index+1, line.strip()))
    return commentless_lines
