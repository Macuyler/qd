import json
import sys
from pathlib import Path

shortcuts = {}
yesses = ['y', 'yes']
home_dir = str(Path.home())
json_file_name = ".qd_shortcuts.json"
json_file_path = f"{home_dir}/{json_file_name}"

def _get_shortcuts():
    data = {}
    if Path(json_file_path).exists():
        with open(json_file_path)as f:
            data = json.load(f)
            return data
    else:
        return {}
def _save_shortcut(name, path):
    shortcuts = _get_shortcuts()
    shortcuts[name] = path
    with open(json_file_path, 'w') as f:
        json.dump(shortcuts, f)

def remove_shortcut(name):
    shortcuts = _get_shortcuts()
    if name not in shortcuts:
        print("Shortcut " + name + " not found and not removed!")
        return
    else:
        print("removed " + name)
        del shortcuts[name]
        with open(json_file_path, 'w') as f:
            json.dump(shortcuts, f)
def list_shortcuts():
    shortcuts = _get_shortcuts()
    for st in shortcuts:
        print(f"{st}: {shortcuts[st].replace(home_dir, '')}")


def set_shortcut(name, path):
    shortcuts = _get_shortcuts()

    # if path isnt homedir or already set, save shortcut and exit
    if path == home_dir:
        confirm = input(f"Are you sure you want to map {name} to your home directory? [y/n]:")
        if confirm.lower() not in yesses:
            print("Exiting. Shortcut not set.")
            sys.exit(1)

    if name in shortcuts and path != shortcuts[name]:
        print(f"\n{name} is already mapped to path {shortcuts[name]}!")
        confirm = input("Are you sure you want to override? [y/n]:").lower()
        if confirm not in yesses:
            print(f"Shortcut {name} not updated.")
            sys.exit(1)

    for key in shortcuts:
        if key != name and shortcuts[key] == path: 
            print(f"\nShortcut {key} is already mapped to {shortcuts[key]}")
            confirm = input(f"Are you sure you want to map {name} to {path} too? [y/n]")
            if confirm.lower() not in yesses:
                print(f"Shortcut {name} not set.")
                sys.exit(1)
    
    _save_shortcut(name, path)    
    print(f"Shortcut {name} set to ~{path.replace(home_dir, '')}")
    sys.exit(1)

def go_to_shortcut(name):
    shortcuts = _get_shortcuts()
    if name in shortcuts:
        path = shortcuts[name]
        if Path(path).exists():
            print(f"Moving to ~{path.replace(home_dir, '')}")
            open(f"{home_dir}/.qd_path", 'w').write(path)
            sys.exit(0)
        else:
            print(f"PATH {path} FOR SHORTCUT {name} DOES NOT EXIST") 
            sys.exit(1)
    else:
        print(f"SHORTCUT {name} NOT SET. USE '--set-shortcut' TO SET SHORTCUT")
        sys.exit(1)
