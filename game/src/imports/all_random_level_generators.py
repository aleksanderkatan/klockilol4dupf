import src.level_generators.less_simple_level_generator as LSLG
import src.level_generators.portal_level_generator as PLG
from src.imports.log import log
from src.level_generators.spelunky_inspired_segmented_level_generator.generate import generate as SISLG


# noinspection PyPep8Naming
def generate_LSLG(index, x, y, ice, jump2, jump3, arrow, length, redirect, max_num=None, min_total=None):
    return LSLG.generate(index, x, y, ice, jump2, jump3, arrow, length, redirect, max_num, min_total)


# noinspection PyPep8Naming
def generate_PLG(index, x, y, portals, min_portals, pair_portals, length, redirect):
    return PLG.generate(index, x, y, portals, min_portals, pair_portals, length, redirect)


# noinspection PyPep8Naming
def generate_SISLG(index, segments, x, y):
    try:
        lines = SISLG(segments, x, y)
        level_string = "\n".join(lines)
        path = "src/levels/" + str(index[0]) + "/" + str(index[1]) + ".lv"
        f = open(path, "w")
        f.write(level_string)
        f.close()
        return True
    except Exception as e:
        log.error(e)
        return False
