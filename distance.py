from converters import rgb2lab
from math import sqrt

def euclidean_distance(a, b):
    xa, ya, za = a
    xb, yb, zb = b
    dx, dy, dz = abs(xa - xb), abs(ya - yb), abs(za - zb)
    return sqrt(dx * dx + dy * dy + dz * dz)

def color_difference(rgb1, rgb2):
    return euclidean_distance(rgb2lab(*rgb1), rgb2lab(*rgb2))

def color_difference_lab(lab1, lab2):
    return euclidean_distance(lab1, lab2)

def distances(colors):
    return [
        color_difference(colors[i], colors[j])
        for i in range(len(colors))
        for j in range(i + 1, len(colors))
    ]

def distances_lab(labs):
    return [
        color_difference_lab(labs[i], labs[j])
        for i in range(len(labs))
        for j in range(i + 1, len(labs))
    ]

def average_distance(colors):
    d = distances(colors)
    return sum(d) / len(d) if d else 0

def max_distance(colors):
    d = distances(colors)
    return max(d) if d else 0

def min_distance(colors):
    d = distances(colors)
    return min(d) if d else 0

def closest(colors):
    if len(colors) < 2:
        return 0, 0
    best = None
    best_i = 0
    best_j = 1
    for i in range(len(colors)):
        for j in range(i + 1, len(colors)):
            d = color_difference(colors[i], colors[j])
            if best is None or d < best:
                best = d
                best_i = i
                best_j = j
    return best_i, best_j

def min_distance_lab(labs):
    d = distances_lab(labs)
    return min(d) if d else 0

def closest_lab(labs):
    if len(labs) < 2:
        return 0, 0
    best = None
    best_i = 0
    best_j = 1
    for i in range(len(labs)):
        for j in range(i + 1, len(labs)):
            d = color_difference_lab(labs[i], labs[j])
            if best is None or d < best:
                best = d
                best_i = i
                best_j = j
    return best_i, best_j

if __name__ == "__main__":
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    magenta = (255, 0, 255)
    cyan = (0, 255, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)
    orange = (255, 165, 0)
    colors = [red, green, blue, yellow, magenta, cyan, black, white, orange]
    dct = {red: "red", green: "green", blue: "blue", yellow: "yellow", magenta: "magenta", cyan: "cyan", black: "black", white: "white", orange: "orange"}
    for color in colors:
        for other in colors:
            print(dct[color], dct[other], color_difference(color, other))



