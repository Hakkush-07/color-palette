import pickle
from math import sqrt
from converters import rgb2lab
from random import randint
from subprocess import run

def rgb2lab_map(file=False, read=False):
    if read:
        with open("rgb2lab.pkl", "rb") as f:
            return pickle.load(f)
    dct = {}
    for r in range(256):
        print("map", r)
        for g in range(256):
            for b in range(256):
                l, a, bb = rgb2lab(r, g, b)
                dct[(r, g, b)] = (l, a, bb)
    if file:
        with open("rgb2lab.pkl", "wb") as f:
            pickle.dump(dct, f)
    return dct

def lab_distance(lab1, lab2):
    l1, a1, b1 = lab1
    l2, a2, b2 = lab2
    dl = (l1 - l2) ** 2
    da = (a1 - a2) ** 2
    db = (b1 - b2) ** 2
    kl, ka, kb = 1, 1, 1
    return sqrt(kl * dl + ka * da + kb * db)

def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def find_farthest(color, dct=None):
    dct = dct if dct is not None else rgb2lab_map(file=False, read=True)
    lab = dct[color]
    maxd = 0
    maxc = None
    for k, v in dct.items():
        print(k)
        d = lab_distance(lab, v)
        if d > maxd:
            maxd = d
            maxc = k
    return maxc

def find_colors(color_count, iteration=1000000):
    print("start")
    dct = rgb2lab_map(file=False, read=True)
    print("map ready")
    colors = [random_rgb() for _ in range(color_count)]
    distances = []
    for c in colors:
        distance = []
        for cx in colors:
            distance.append(lab_distance(dct[c], dct[cx]))
        distances.append(distance)
    start = sum([sum(u) / (color_count - 1) for u in distances]) / color_count
    start_min = min([u for v in distances for u in v if u])
    for i in range(iteration):
        print(i, iteration)
        color = random_rgb()
        d = [lab_distance(dct[color], dct[c]) for c in colors]
        
        dsum = [sum(u) for u in distances]
        mn = min(dsum)
        mc = dsum.index(mn)
        # sum(d) - d[mc] > mn and 
        if sum(d) - d[mc] > mn and min([u for u in distances[mc] if u]) < min(u for u in d if u):
            d[mc] = 0
            distances[mc] = d
            for j in range(color_count):
                distances[j][mc] = d[j]
            colors[mc] = color
        
    end = sum([sum(u) / (color_count - 1) for u in distances]) / color_count
    end_min = min([u for v in distances for u in v if u])
    s = []
    for c, d in zip(colors, distances):
        print(c, d)
        r, g, b = c
        s.append(f"RGB({r}, {g}, {b})")
    with open("colors.txt", "w+") as f:
        f.write("\n".join(s) + "\n")
    t = []
    for c, d in zip(colors, distances):
        print(c, d)
        r, g, b = c
        l, a, bb = dct[c]
        t.append(f"RGB({r}, {g}, {b}), LAB({l}, {a}, {bb})")
    with open("colors-lab.txt", "w+") as f:
        f.write("\n".join(t) + "\n")
    print(start, end)
    print(start_min, end_min)
    print("done")

def a():
    with open("colors.txt", "r+") as file:
        content = file.read().splitlines()
    s = []
    for i, line in enumerate(content):
        s.append(f"coloring({i // 9 + 1}, {i % 9 + 1}, {line});")
    with open("color-template.asy", "r+") as f:
        x = f.read().replace("REPLACE", "\n".join(s))
    with open("test.asy", "w+") as f2:
        f2.write(x)
    run(["asy", f"test.asy"])

if __name__ == "__main__":
    rgb2lab_map(file=False, read=True)
    find_colors(20)
    a()

