import game_files.level_generators.less_simple_level_generator as LSLG
import game_files.level_generators.portal_level_generator as PLG

def generate_LSLG(index, x, y, ice, jump2, jump3, arrow, length, redirect, max_num=None, min_total=None):
    return LSLG.generate(index, x, y, ice, jump2, jump3, arrow, length, redirect, max_num, min_total)

def generate_PLG(index, x, y, portals, min_portals, pair_portals, length, redirect):
    return PLG.generate(index, x, y, portals, min_portals, pair_portals, length, redirect)


