import re
import itertools

fws = re.findall(r"[\w']+", open("filter.txt", "r").read())
ws = re.findall(r"[\w']+", open("input.txt", "r").read())

for w in fws:
    for i in range(ws.count(w)):
        ws.remove(w)

ws.sort()

with open("output1.txt", "w") as tf:
    res = [(g[0], len(list(g[1]))) for g in itertools.groupby(ws)]
    res.sort(key=lambda x: x[1], reverse=True)
    for p in res:
        if not ("" + p[0]).isnumeric() and len(p[0]) > 1:
            print("{} {}".format(p[0], p[1]), file=tf)

with open("output2.txt", "w") as tf:
    res = [(g[0], len(list(g[1]))) for g in itertools.groupby(ws)]
    res.sort(key=lambda x: len(x[0]), reverse=True)
    for p in res:
        if not ("" + p[0]).isnumeric() and len(p[0]) > 1:
            print("{} {}".format(p[0], p[1]), file=tf)
