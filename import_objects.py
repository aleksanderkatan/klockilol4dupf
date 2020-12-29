from objects.obj_block_perma import block_perma
from objects.obj_block_empty import block_empty
from objects.obj_block_start import block_start
from objects.obj_block_end import block_end
from objects.obj_block_numeric import block_numeric
from objects.obj_block_ice import block_ice
from objects.obj_block_arrow import block_arrow
from objects.obj_block_jump import block_jump
from objects.obj_block_lift import block_lift
from objects.obj_block_portal import block_portal
from objects.obj_block_dummy import block_dummy
from objects.obj_block_lamp import block_lamp
from objects.obj_block_bridge import block_bridge
from objects.obj_block_entrance import block_entrance
from objects.obj_block_map_bridge import block_map_bridge

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

preventing_win = set()
preventing_win.add(block_numeric)
# lamp block is checked individually since it doesn't directly prevent win
