from converters import rgb2lab
from math import sqrt

def euclidean_distance(a, b):
    xa, ya, za = a
    xb, yb, zb = b
    dx, dy, dz = abs(xa - xb), abs(ya - yb), abs(za - zb)
    return sqrt(dx * dx + dy * dy + dz * dz)

def color_difference(rgb1, rgb2):
    return euclidean_distance(rgb2lab(*rgb1), rgb2lab(*rgb2))

def distances(colors):
    return [color_difference(a, b) for a in colors for b in colors]

def average_distance(colors):
    return sum(distances(colors)) / (len(colors) * (len(colors) - 1))

def max_distance(colors):
    return max(distances(colors))

def min_distance(colors):
    return min([a for a in distances(colors) if a > 0])

def closest(colors):
    d = distances(colors)
    mn = min([a for a in d if a > 0])
    i = d.index(mn)
    a, b = i // len(colors), i % len(colors)
    return a, b

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





