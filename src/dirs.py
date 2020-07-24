import os

filtered_paths = []

def apply_rules(name, root, conf, inp):
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
    if inp.lower() in name.lower():
        filtered_paths.append(path)
    return r

def match_points(match, exact_points, non_exact_points):
    points = 0
    # Char to the left of the inputed NAME string
    left_string = match[len(match) - 2]
    left_char = left_string[len(match[len(match) - 2]) - 1] if len(left_string) > 0 else ''
    # Char to the right of the inputed NAME string
    right_char = match[len(match) - 1][0] if len(match[len(match) - 1]) > 0 else ''
    if left_char == '/' and right_char == '':
         # Exact Match
        points += exact_points
    elif (left_char != '/' or right_char != '/') and '/' not in match[len(match) - 1]:
         # Indirect match
        points += non_exact_points
    return points

# Award n points per directory match between CWD and Path
# Subtract m points per directory after the paths split
def dist_points(p):
    points = 0
    repeat = 0
    split = False
    cwd = os.getcwd().split('/')
    path = p.split('/')
    # Loop through each dir in path
    for i in range(len(path)):
        d1 = path[i]
        d2 = ''
        if len(cwd) > i:
            d2 = cwd[i]
        if d1 == d2 and not split:
            # CWD and Path are both in this dir
            points += 1
        else:
            # CWD is not in this dir
            split = True
            repeat += 1
    repeat *= 10
    points *= 300000
    return points - repeat

def walk(dir, conf, inp):
    with os.scandir(dir) as it:
        for sub in it:
            path = os.path.join(dir, sub.name)
            if sub.is_dir() and apply_rules(sub.name, dir, conf, inp):
                walk(path, conf, inp)
    return

def get_dirs(inp, conf, results=8):
    scores = {}

    def add_score(path, points):
        if path in scores:
            scores[path] += points
        else:
            scores[path] = points

    walk(conf.root, conf, inp)
    for path in filtered_paths:
        if inp in path:
            points = match_points(path.split(inp), 500000, 480000)
            if points > 0:
                points += dist_points(path)
                add_score(path, points)
        elif inp.lower() in path.lower():
            points = match_points(path.lower().split(inp.lower()), 300000, 300000)
            if points > 0:
                points += dist_points(path)
                add_score(path, points)
    dirs = sorted(scores.items(), key=lambda item: -item[1])[:results]
    return list(map(lambda x: x[0], dirs))
