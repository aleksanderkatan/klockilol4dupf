import game_files.imports.all_blocks as o

option_map = {
    o.block_portal: 'portals',
    o.block_jump: 'jumps',
    o.block_entrance: 'entrances',
    o.block_map_bridge: 'map_bridges',
    o.block_ones: 'ones',
    o.block_piston: 'pistons',
    o.block_dual_arrow: 'dual_arrows',
    o.block_moving_arrow: 'moving_arrows',
    o.block_entrance_random: 'entrances_random',
    o.block_pm_arrow: 'pm_arrows',
    o.block_pm_numeric: 'pm_numeric',
    o.block_pm_control_switcher: 'pm_control_switchers',
}

valid_options = {value for value in option_map.values()}
valid_options.add("chavs")
valid_options.add("bombs")
valid_options.add("decorations")
valid_options.add("forced_spawn")

char_optionable_blocks = {
    o.block_numeric,
    o.block_arrow,
    o.block_birdy_arrow,
    o.block_lamp,
    o.block_swapping,
    o.block_numeric_dark,
}
