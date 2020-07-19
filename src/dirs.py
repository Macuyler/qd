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

def match_points(match, exact_points, non_exact_points):
    points = 0
    # Char to the left of the inputed NAME string
    left_char = match[len(match) - 2][len(match[len(match) - 2]) - 1]
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

def get_dirs(name, conf, results=8):
    scores = {}

    def add_score(path, points):
        if path in scores:
            scores[path] += points
        else:
            scores[path] = points

    for root, dirs, files in os.walk(conf.root, topdown=True):
        dirs[:] = list(filter(lambda d: apply_rules(d, root, conf), dirs))
        for subdir in dirs:
            path = os.path.join(root, subdir)
            if name in path:
                points = match_points(path.split(name), 500000, 480000)
                if points > 0:
                    points += dist_points(path)
                    add_score(path, points)
            elif name.lower() in path.lower():
                points = match_points(path.lower().split(name.lower()), 300000, 300000)
                if points > 0:
                    points += dist_points(path)
                    add_score(path, points)
    return sorted(scores.items(), key=lambda item: -item[1])[:results]
