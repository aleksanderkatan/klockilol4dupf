# definitely the only way to do this

from src.blocks.pure.block_perma import block_perma
from src.blocks.block_empty import block_empty
from src.blocks.pure.block_start import block_start
from src.blocks.pure.block_end import block_end
from src.blocks.pure.block_numeric import block_numeric
from src.blocks.pure.block_ice import block_ice
from src.blocks.pure.block_arrow import block_arrow
from src.blocks.pure.block_jump import block_jump
from src.blocks.pure.block_lift import block_lift
from src.blocks.pure.block_portal import block_portal
from src.blocks.semi_pure.block_dummy import block_dummy
from src.blocks.semi_pure.block_lamp import block_lamp
from src.blocks.pure.block_bridge import block_bridge
from src.blocks.impure.block_entrance import block_entrance
from src.blocks.impure.block_map_bridge import block_map_bridge
from src.blocks.pure.block_ones import block_ones
from src.blocks.pure.block_blocker import block_blocker
from src.blocks.semi_pure.block_thunder import block_thunder
from src.blocks.impure.block_invisible import block_invisible
from src.blocks.pure.block_piston import block_piston
from src.blocks.impure.block_reset import block_reset
from src.blocks.pure.block_dual_arrow import block_dual_arrow
from src.blocks.semi_pure.block_numeric_dark import block_numeric_dark
from src.blocks.semi_pure.block_plus import block_plus
from src.blocks.semi_pure.block_minus import block_minus
from src.blocks.semi_pure.block_moving_arrow import block_moving_arrow
from src.blocks.impure.block_entrance_random import block_entrance_random
from src.blocks.impure.block_perma_unsteppable import block_perma_unsteppable
from src.blocks.semi_pure.block_swapping import block_swapping
from src.blocks.semi_pure.block_swapping_trigger import block_swapping_trigger
from src.blocks.semi_pure.block_swapping_trigger_random import block_swapping_trigger_random
from src.blocks.impure.block_game_exit import block_game_exit
from src.blocks.impure.block_silent_trigger import block_silent_trigger
from src.blocks.impure.block_madeline import block_madeline

from src.blocks.impure.block_shrek import block_shrek

from src.blocks.semi_pure.undertale.block_undertale_purple import block_undertale_purple
from src.blocks.semi_pure.undertale.block_undertale_yellow import block_undertale_yellow
from src.blocks.semi_pure.undertale.block_undertale_green import block_undertale_green
from src.blocks.semi_pure.undertale.block_undertale_orange import block_undertale_orange
from src.blocks.semi_pure.undertale.block_undertale_blue import block_undertale_blue
from src.blocks.semi_pure.undertale.block_undertale_pink import block_undertale_pink
from src.blocks.semi_pure.undertale.block_undertale_red import block_undertale_red

from src.blocks.semi_pure.birdy.block_birdy_fragile_start import block_birdy_fragile_start
from src.blocks.semi_pure.birdy.block_birdy_fragile_end import block_birdy_fragile_end
from src.blocks.semi_pure.birdy.block_birdy_arrow import block_birdy_arrow

from src.blocks.semi_pure.platform_maze.block_pm_jump import block_pm_jump
from src.blocks.semi_pure.platform_maze.block_pm_portal import block_pm_portal
from src.blocks.semi_pure.platform_maze.block_pm_arrow import block_pm_arrow
from src.blocks.semi_pure.platform_maze.block_pm_flight import block_pm_flight
from src.blocks.semi_pure.platform_maze.block_pm_numeric import block_pm_numeric
from src.blocks.semi_pure.platform_maze.block_pm_control_switcher import block_pm_control_switcher
from src.blocks.semi_pure.platform_maze.block_pm_triggerer import block_pm_triggerer
from src.blocks.semi_pure.platform_maze.block_pm_triggerable_on import block_pm_triggerable_on
from src.blocks.semi_pure.platform_maze.block_pm_triggerable_off import block_pm_triggerable_off


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
standables.add(block_entrance_random)
standables.add(block_perma_unsteppable)
standables.add(block_swapping)
standables.add(block_swapping_trigger)
standables.add(block_swapping_trigger_random)
standables.add(block_game_exit)
standables.add(block_silent_trigger)
standables.add(block_madeline)

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

standables.add(block_pm_jump)
standables.add(block_pm_portal)
standables.add(block_pm_arrow)
standables.add(block_pm_flight)
standables.add(block_pm_numeric)
standables.add(block_pm_control_switcher)
standables.add(block_pm_triggerer)
standables.add(block_pm_triggerable_on)

preventing_win = set()
preventing_win.add(block_numeric)
preventing_win.add(block_birdy_fragile_start)
# lamp block is checked individually since it doesn't directly prevent win
