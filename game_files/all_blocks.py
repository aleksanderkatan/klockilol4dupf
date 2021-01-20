from blocks.block_perma import block_perma
from blocks.block_empty import block_empty
from blocks.block_start import block_start
from blocks.block_end import block_end
from blocks.block_numeric import block_numeric
from blocks.block_ice import block_ice
from blocks.block_arrow import block_arrow
from blocks.block_jump import block_jump
from blocks.block_lift import block_lift
from blocks.block_portal import block_portal
from blocks.block_dummy import block_dummy
from blocks.block_lamp import block_lamp
from blocks.block_bridge import block_bridge
from blocks.block_entrance import block_entrance
from blocks.block_map_bridge import block_map_bridge
from blocks.block_ones import block_ones

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

preventing_win = set()
preventing_win.add(block_numeric)
# lamp block is checked individually since it doesn't directly prevent win
