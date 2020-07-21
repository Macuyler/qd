import curses
from pathlib import Path
import sys
def start_display(paths, conf):
    if len(paths) > 0:
        # INIT curses sesion
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)

        term_y, term_x = stdscr.getmaxyx() #get termianl x and y

        #Add curses color pairs:

        current_location = 0

        root = conf.root
        clean_paths = []
        for p in paths:
            clean_string = ''
            #check if path length is greater then the width of terminal
            if len(p.replace(root, '')) > term_x - 10:
                #Make sure p doesn't start with / messes up splits later
                split_p = p.replace(root, '')
                if split_p[:1] == '/':
                    split_p = split_p[1:]

                split_p = split_p.split('/')

                max_part_len = term_x - 13
                max_part_len = max_part_len / 2


                #Max length each path string seperated by ... can be
                first_path_len = 0
                last_path_len = 0
                #count of split parts


                if len(split_p[0]) + len(split_p[1]) < max_part_len:
                    first_path_len = 2
                elif len(split_p[0]) < max_part_len:
                    first_path_len = 1

                if len(split_p[-1]) + len(split_p[-2]) < max_part_len:
                    last_path_len = 2
                elif len(split_p[-1]) < max_part_len:
                    last_path_len = 1

                first_half_of_str = ''
                last_half_of_str = ''

                if first_path_len == 2:
                    first_half_of_str = f'{split_p[0]}/{split_p[2]}'
                elif first_path_len ==1:
                    first_half_of_str = split_p[0]

                if last_path_len == 1:
                    last_half_of_str = split_p[-1]
                elif last_path_len == 2:
                    last_half_of_str = f'{split_p[-2]}/{split_p[-1]}'

                if first_path_len == 0 and last_path_len == 0:
                    last_half_of_str = split_p[-1]

                clean_string = f'{first_half_of_str}/.../{last_half_of_str}'


            else:
                clean_string = p.replace(root, '')


            clean_paths.append(clean_string)

        def clear_string(index):
            if index < len(paths):
                stdscr.addch(index, 2, ' ')
                stdscr.addstr(index, 4, clean_paths[index])

        def select_string(index):
            if index < len(path):
                line = f">{clean_paths[index]}"
                stdscr.addch(index, 2, ">")
                stdscr.addstr(index, 4, clean_paths[index], curses.A_STANDOUT)
                #stdscr.addstr(index, 0, line, curses.A_STANDOUT)

        for index, path in enumerate(clean_paths):
            stdscr.addstr(index, 4, path)

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
                sys.exit(1)


    else:
        print("NO PATHS FOUND")
