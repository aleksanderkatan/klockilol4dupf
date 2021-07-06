from game_files.blocks.block_perma import block_perma
from game_files.blocks.block_empty import block_empty
from game_files.blocks.block_start import block_start
from game_files.blocks.block_end import block_end
from game_files.blocks.block_numeric import block_numeric
from game_files.blocks.block_ice import block_ice
from game_files.blocks.block_arrow import block_arrow
from game_files.blocks.block_jump import block_jump
from game_files.blocks.block_lift import block_lift
from game_files.blocks.block_portal import block_portal
from game_files.blocks.block_dummy import block_dummy
from game_files.blocks.block_lamp import block_lamp
from game_files.blocks.block_bridge import block_bridge
from game_files.blocks.block_entrance import block_entrance
from game_files.blocks.block_map_bridge import block_map_bridge
from game_files.blocks.block_ones import block_ones
from game_files.blocks.block_blocker import block_blocker
from game_files.blocks.block_thunder import block_thunder
from game_files.blocks.block_invisible import block_invisible
from game_files.blocks.block_piston import block_piston
from game_files.blocks.block_reset import block_reset
from game_files.blocks.block_dual_arrow import block_dual_arrow
from game_files.blocks.block_numeric_dark import block_numeric_dark
from game_files.blocks.block_plus import block_plus
from game_files.blocks.block_minus import block_minus
from game_files.blocks.block_moving_arrow import block_moving_arrow

from game_files.blocks.block_shrek import block_shrek
from game_files.blocks.undertale.block_undertale_purple import block_undertale_purple
from game_files.blocks.undertale.block_undertale_yellow import block_undertale_yellow
from game_files.blocks.undertale.block_undertale_green import block_undertale_green
from game_files.blocks.undertale.block_undertale_orange import block_undertale_orange
from game_files.blocks.undertale.block_undertale_blue import block_undertale_blue
from game_files.blocks.undertale.block_undertale_pink import block_undertale_pink
from game_files.blocks.undertale.block_undertale_red import block_undertale_red

from game_files.blocks.birdy.block_birdy_fragile_start import block_birdy_fragile_start
from game_files.blocks.birdy.block_birdy_fragile_end import block_birdy_fragile_end
from game_files.blocks.birdy.block_birdy_arrow import block_birdy_arrow

standables = set()
standables.add(block_perma)
standables.add(block_start)
standables.add(block_end)
standables.add(block_numeric)
standables.add(block_ice)
standables.add(block_arrow)
standables.add(block_jump)
standables.add(block_lift)
standables.add(block_portal)
standables.add(block_dummy)
standables.add(block_lamp)
standables.add(block_bridge)
standables.add(block_entrance)
standables.add(block_map_bridge)
standables.add(block_ones)
standables.add(block_invisible)
standables.add(block_thunder)
standables.add(block_piston)
standables.add(block_reset)
standables.add(block_dual_arrow)
standables.add(block_numeric_dark)
standables.add(block_plus)
standables.add(block_minus)
standables.add(block_moving_arrow)

standables.add(block_shrek)
standables.add(block_undertale_yellow)
standables.add(block_undertale_red)
standables.add(block_undertale_blue)
standables.add(block_undertale_orange)
standables.add(block_undertale_purple)
standables.add(block_undertale_pink)
standables.add(block_undertale_green)

standables.add(block_birdy_fragile_start)
standables.add(block_birdy_fragile_end)
standables.add(block_birdy_arrow)

preventing_win = set()
preventing_win.add(block_numeric)
preventing_win.add(block_birdy_fragile_start)
# lamp block is checked individually since it doesn't directly prevent win
