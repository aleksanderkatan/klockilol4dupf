from src.speedruns.speedrun_birdy import speedrun_birdy
from src.speedruns.speedrun_perfectionist import speedrun_perfectionist
from src.speedruns.speedrun_pm import speedrun_pm
from src.speedruns.speedrun_shrek import speedrun_shrek

speedruns = {
    'platform_maze': speedrun_pm,
    'platform maze': speedrun_pm,
    'pm': speedrun_pm,

    'birdy\'s rainy day skipathon': speedrun_birdy,
    'birdy': speedrun_birdy,
    'brds': speedrun_birdy,

    'shrek%': speedrun_shrek,
    'shrek': speedrun_shrek,
    'any%': speedrun_shrek,
    'any': speedrun_shrek,

    '100%': speedrun_perfectionist,
    'true ending': speedrun_perfectionist,
}
