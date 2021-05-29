# Serve as an entry point for quickgen scripts
# Use to quickly generate scripts with terminal commands.
# without need to adjust in game.
# alias mindu="python /PATH/TO/mindustry_scripts/script.py"

import os, sys
abspath = os.path.abspath(__file__)
os.chdir(os.path.dirname(abspath))

from terminal_scripts import supply
from terminal_scripts import mine
from terminal_scripts import move
from terminal_scripts import save
from terminal_scripts import defend


FUNCTIONS = {
    "supply": supply.create_supply,
    "mine": mine.mine,
    "move": move.move,
    "save": save.save,
    "defend": defend.defend,
}

def main(args):
    if len(args) > 1:
        if args[1] in FUNCTIONS:
            func = FUNCTIONS[args[1]]
            if args[2] == "help":
                help(func)
                return
            func_args = args[2:]
            FUNCTIONS[args[1]](*func_args)
        else:
            raise ValueError("Functions not found, available functions: {}".format(FUNCTIONS.keys()))
    else:
        raise ValueError("Invalid input")

if __name__ == '__main__':
    main(sys.argv)
