import json
import sys
from pathlib import Path

shortcuts = {}
home_dir = str(Path.home())
json_file_name = ".qd_shortcuts.json"
json_file_path = f"{home_dir}/{json_file_name}"

def _get_shortcuts():
    data = {}
    if Path(json_file_path).exists():
        with open(json_file_path)as f:
            data = json.load(f)
        return data

def set_shortcut(name, path):
    shortcuts = _get_shortcuts()
    shortcuts[name] = path
    with open(json_file_path, 'w') as f:
        json.dump(shortcuts, f)
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
