from colors import *
from random import choice, randint

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

if __name__ == "__main__":
    find_colors(20)
