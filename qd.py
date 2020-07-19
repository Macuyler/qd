#!/usr/bin/env python3

import sys
from src.config import get_config
from src.dirs import get_dirs
from src.cli import start_display


def show_usage():
    print('\n  *** qd usage:')
    print('    $ qd name_of_dir_you_want_to_go_to\n')
    return

def main():
    help_args = ['--help', '-h']
    if len(sys.argv) == 2 and sys.argv[1] not in help_args: # Check for argument
        conf = get_config()
        dirs = get_dirs(sys.argv[1], conf)
        start_display(dirs, conf)
    else:
        show_usage()
        sys.exit(1)
    return

if __name__ == '__main__':
    main()
