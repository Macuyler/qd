"""

 # Quick Change Directory config options:
 ** The config file is located at ~/.qd_config **

 Options:
  - qd root path:       root=/path/to/root/ (Only one path should be specified here!)
  - Allow .dirs:        hidden_dirs=y |OR| hidden_dirs=n
  - Include paths:      include=[exact_name,/path/to/directory/]
  - Exclude paths:      exclude=[exact_name,/path/to/directory/]

(For Include and Exclude you can specify as many paths or names as you want, each separated by a comma.
 These items will be run against each path listing so be careful when using vague paths, for example:
 Using "exclude=[school]" to block your /home/Documents/school/ directory will also block your /home/Desktop/school/ directory.
 A better way to solve the problem above would be to use "exclude=[/home/Documents/school/]" instead.)

 Defaults:
    root=/path/to/your/home/dir/
    hidden_dirs=n
    include=[]
    exclude=[node_modules]

"""

from pathlib import Path
DECLARE_ROOT = 'root='
DECLARE_HIDDEN = 'hidden_dirs='
DECLARE_INCLUDE = 'include=['
DECLARE_EXCLUDE = 'exclude=['

class Config:
    def __init__(self, root='/', hidden=False, include=[], exclude=[]):
        self.root = root
        self.hidden = hidden
        self.include = include
        self.exclude = exclude

def get_root(line):
    _, root = line.split(DECLARE_ROOT)
    return root.strip()

def get_hidden(line):
    yesses = ['y', 'yes', 't', 'true', 'on']
    value = line.replace(DECLARE_HIDDEN, '').strip().lower()
    return value in yesses

def get_items(string):
    return string.split(']')[0].split(',')

def get_include(line):
    return get_items(line.replace(DECLARE_INCLUDE, '').strip())

# TODO: Add [...] syntax to allow appending items to default list
def get_exclude(line):
    return get_items(line.replace(DECLARE_EXCLUDE, '').strip())

def get_config():
    home = str(Path.home())
    conf = Config(root=home, exclude=['node_modules'])
    try:
        with open(f'{home}/.qd_config', 'r') as conf_file:
            for line in conf_file:
                if DECLARE_ROOT in line:
                    conf.root = get_root(line)
                elif DECLARE_HIDDEN in line:
                    conf.hidden = get_hidden(line)
                elif DECLARE_INCLUDE in line:
                    conf.include = get_include(line)
                elif DECLARE_EXCLUDE in line:
                    conf.exclude = get_exclude(line)
    except FileNotFoundError:
        print('No config file...')
    return conf
