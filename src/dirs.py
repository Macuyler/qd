import os

def apply_rules(name, root, conf):
    path = os.path.join(root, name)
    r = True
    for e in conf.exclude:
        if path in e:
            r = False
    if name in conf.exclude:
        r = False
    if (not conf.hidden and name[0] == '.'):
        r = False
    for e in conf.include:
        if path in e:
            r = True
    if name in conf.include:
        r = True
    return r

def get_dirs(name, conf):
    for root, dirs, files in os.walk(conf.root, topdown=True):
        dirs[:] = list(filter(lambda d: apply_rules(d, root, conf), dirs))
        for subdir in dirs:
            path = os.path.join(root, subdir)
            print(path)
    return
