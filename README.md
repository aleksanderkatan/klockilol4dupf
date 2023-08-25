# v1.0 is finally here, go play it!

## Maze of Tiles (aka klockilol4dupf)

A puzzle game, where you have to walk over tiles the exact amount of times that is specified on them! How hard can it be?

## Engaging puzzles

![ss](game/src/sprites/other/screenshot_2.gif "This can be solved in 12 different ways. One of them is <<<v<<^>><^><^^")

## NP-Complete concept

![ss](game/src/sprites/other/screenshot_3.gif "Hamiltonian Cycle reduces to this and yes, this reduction is in the right direction")

## Overly complicated levels

![ss](game/src/sprites/other/screenshot_4.gif "Not even all of the blocks that are implemented")

## Questionable design choices

![ss](game/src/sprites/other/screenshot_1.gif "this zone is currently in development, and therefore yet unavailable")

## The Idea

The concept is based on a hazy memory of a Flash game from late 2000s, which late in development turned out to be [Platform Maze](https://www.newgrounds.com/portal/view/360130) by Bobberticus.
Another Flash game with similar idea is Birdy's Rainy Day Skipathon by Jess Hansen (can still be found on [Flash Point](https://bluemaxima.org/flashpoint/)).
All mechanics and levels from both of those have been integrated into klockilol4dupf as extra zones.


## Features

- 10 main zones, each with a different gimmick, containing over 200 puzzles in total!
- An ability to reverse any mistakes you make!
- A witch, that acts as a narrator! She speaks either Polish or English.
- Speedrun helpers, such as timer and commands setting up certain runs!
- Several extra zones for players hungry for more!
- An easy to learn level creation process based on txt files!

## Upcoming features

- More extra zones!
- A way to skip levels.
- An in-game display of the control scheme.
- Hold a direction to keep moving that way.
- Whatever you suggest that I find cool

## Installation

For <b>Windows 10/11</b>:
1) Download this repo (code -> download as .zip).
2) Create a new folder and unzip there.
3) Run klockilol4dupf.exe (a file in "game" folder).

**Do NOT move the .exe file away from that folder.** You can create a shortcut though. Windows Defender will likely stop the game from running. Press more info -> run anyway, if you trust me enough. Do NOT close the console window.
<br/><br/>

For <b>Linux</b> - just clone and run launcher.py, hopefully works
<br/><br/>

If you want to create an .exe yourself, use `pyinstaller --onefile .\klockilol4dupf.py`. 
The result will generate in the `dist` directory, and will need to be moved to the `game` directory to function properly.

When moving between devices, a save can be transferred by simply copying the save folder, and pasting it on the new device.

## Controls
- W, A, S, D or ARROW KEYS - movement  
- Q or SHIFT - undo move  
- R or / - reset current stage  
- 1,...,9 - change view mode to single layer (useful from zone 4 onward)  
- ESCAPE - go back in level hierarchy (Lobbies contain zones, zones contain levels)  
- ENTER - command line, list of available commands is under "help" command

## Commands

Commands are available after pressing Enter while in game.

- help - list all available commands in the log.
- exit - exit. It is safe to simply press the "x" though.
- auto_reverse - switch auto reverse after death.
- timer - switch speedrun timer.
- witch - switch witch comments.
- speedrun - start a speedrun given in the argument.   
    WARNING: this command wipes your save! You can back it up by copying files from `game/src/data`  
    Available speedruns:
  - platform maze (pm)
  - birdy's rainy day skipathon (birdy)
  - shrek%
  - 100%  


## Dependencies
* numpy
* pygame
* tkinter
* pickle
