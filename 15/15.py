from sys import argv

_, s, t = argv

if len(s) > 1000 or len(t) > 1000:
    raise ValueError("input over 1 kb")

locs = []  # list of substring locations to print
removed = 0  # indices stripped from string to left of substring so far
while True:
    loc = s.find(t)
    if loc == -1:  # stop when substring is no longer found
        break
    locs.append(loc + 1 + removed)  # 1-indexed position in original string
    s = s[loc + 1:]  # strip all left of substring
    removed += loc + 1  # update amount stripped so far

print(' '.join([str(loc) for loc in locs]))
