#!/usr/bin/env python3

import sys
from os import getcwd
from src.config import get_config
from src.dirs import get_dirs
from src.cli import start_display
from src.shortcut import set_shortcut, go_to_shortcut


def show_usage():
    print('\n  *** qd usage:')
    print('\t$ qd name_of_dir_you_want_to_go_to\n')
    print("\tcommands: ")
    print('\t\t-s or --shortcut [shortcut name]')
    print('\t\t\tchange to path associated with a shortcut set with --set-shortcut\n')
    print('\t\t-ss or --set-shortcut [shortcut_name]')
    print('\t\t\tsets shortcut name to current working directory')
    return

def main():
    help_args = ['--help', '-h']
    favorate_args = ['-f', '--favorites']
    shortcut_args = ['-s', '--shortcut']
    set_shortcut_args = ['-ss', '--set-shortcut']


    if len(sys.argv) >= 2: #check if any other arugments were passed besides 'qd'
        conf = get_config()
        command_arg = sys.argv[1]

        #check for each command. If no command passed, start path search
        if command_arg in help_args:
            show_usage()
            sys.exit(1)
        elif command_arg in shortcut_args and len(sys.argv) >= 3: #this command requires an extra arg
            go_to_shortcut(sys.argv[2])
        elif command_arg in set_shortcut_args and len(sys.argv) >= 3: #requires extra arg
            # TODO: maybe allow users to set path manually? for right now it sets to working directory.
            shortcut_path = getcwd()
            name = sys.argv[2]
            set_shortcut(name, shortcut_path)
        else:
            full_path = ' '.join(sys.argv[1:])
            dirs = get_dirs(full_path, conf)
            start_display(dirs, conf, favorites=False)
    else:
        show_usage()
        sys.exit(1)

if __name__ == '__main__':
    main()
