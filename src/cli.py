import curses
from pathlib import Path

def start_display(paths, conf):
    if len(paths) > 0:
        root = conf.root
        clean_paths = []
        for p in paths:
            clean_paths.append(f"\t{p.replace(root, '')}")


        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)
        current_location = 0

        def clear_string(index):
            if index < len(paths):
                stdscr.addstr(index, 0,clean_paths[index])

        def select_string(index):
            if index < len(path):
                line = f">{clean_paths[index]}"
                stdscr.addstr(index, 0, line, curses.A_STANDOUT)

        for index, path in enumerate(clean_paths):
            stdscr.addstr(index, 0, path)

        key = ''

        quit = False

        select_string(0)
        while not quit:

            key = stdscr.getch()
            stdscr.refresh()

            if key == curses.KEY_DOWN:
                if current_location +1 < len(paths):
                    clear_string(current_location)
                    current_location = current_location +1
                    select_string(current_location)
                else:
                    clear_string(current_location)
                    current_location = 0
                    select_string(current_location)
            elif key == curses.KEY_UP:
                if current_location - 1 >= 0 :
                    clear_string(current_location)
                    current_location = current_location - 1
                    select_string(current_location)
                else:
                    clear_string(current_location)
                    current_location = len(paths) - 1
                    select_string(current_location)
            elif key == 10:
                curses.endwin()
                quit = True
                home = str(Path.home())
                open(f'{home}/.qd_path', 'w').write(paths[current_location])
            elif key == ord('q'):
                quit = True

        curses.endwin()
    else:
        print("NO PATHS FOUND")
