import game_files.imports.all_blocks as o

charmap = {}
charmap['.'] = o.block_empty
charmap['0'] = o.block_perma
charmap['S'] = o.block_start
charmap['E'] = o.block_end
charmap['1'] = o.block_numeric
charmap['2'] = o.block_numeric
charmap['3'] = o.block_numeric
charmap['4'] = o.block_numeric
charmap['5'] = o.block_numeric
charmap['6'] = o.block_numeric
charmap['7'] = o.block_numeric
charmap['8'] = o.block_numeric
charmap['I'] = o.block_ice
charmap['>'] = o.block_arrow
charmap['<'] = o.block_arrow
charmap['^'] = o.block_arrow
charmap['v'] = o.block_arrow
charmap['J'] = o.block_jump
charmap['L'] = o.block_lift
charmap['P'] = o.block_portal
charmap['D'] = o.block_dummy
charmap['B'] = o.block_lamp     # stands for bulb since L is taken
charmap['b'] = o.block_lamp
charmap['M'] = o.block_bridge
charmap['e'] = o.block_entrance
charmap['m'] = o.block_map_bridge
charmap['O'] = o.block_ones
charmap['u'] = o.block_blocker
charmap['?'] = o.block_invisible
charmap['T'] = o.block_thunder
charmap['N'] = o.block_piston
charmap['R'] = o.block_reset
charmap['A'] = o.block_dual_arrow
charmap['X'] = o.block_numeric_dark     # 1
charmap['Y'] = o.block_numeric_dark     # 2
charmap['Z'] = o.block_numeric_dark     # 3
charmap['+'] = o.block_plus
charmap['/'] = o.block_minus            # - taken by birdy
charmap['a'] = o.block_moving_arrow
charmap['n'] = o.block_entrance_random
charmap['x'] = o.block_perma_unsteppable
charmap['q'] = o.block_swapping
charmap['Q'] = o.block_swapping
charmap['t'] = o.block_swapping_trigger
charmap['G'] = o.block_swapping_trigger_random

charmap['K'] = o.block_shrek
charmap['p'] = o.block_undertale_purple
charmap['i'] = o.block_undertale_pink   # p taken
charmap['o'] = o.block_undertale_orange
charmap['y'] = o.block_undertale_yellow
charmap['g'] = o.block_undertale_green
charmap['r'] = o.block_undertale_red
charmap['l'] = o.block_undertale_blue   # b taken

charmap['s'] = o.block_birdy_fragile_start
charmap['f'] = o.block_birdy_fragile_end
charmap['['] = o.block_birdy_arrow
charmap[']'] = o.block_birdy_arrow
charmap['-'] = o.block_birdy_arrow
charmap['_'] = o.block_birdy_arrow

charmap['U'] = o.block_pm_jump
charmap['z'] = o.block_pm_portal
charmap['V'] = o.block_pm_arrow
charmap['!'] = o.block_pm_flight
charmap['9'] = o.block_pm_numeric
charmap['c'] = o.block_pm_control_switcher
charmap['K'] = o.block_pm_triggerer
charmap['k'] = o.block_pm_triggerable_off

# letters left:
# W
# FGH
# C
#
# w
# dhj
#
