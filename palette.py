from random import randint
from distance import min_distance, closest, color_difference

def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

# choose k colors with big min distance
def choose_k_colors(k, iterations=100000):
    colors = [random_rgb() for _ in range(k)]
    current = min_distance(colors)
    start = current
    for i in range(iterations):
        print(i, iterations)
        a, b = closest(colors)
        A, B = colors[a], colors[b]
        C = random_rgb()
        if color_difference(A, C) < current or color_difference(B, C) < current:
            continue
        colors_a = colors.copy()
        colors_b = colors.copy()
        colors_a[a] = C
        colors_b[b] = C
        md_a = min_distance(colors_a)
        md_b = min_distance(colors_b)
        if md_a > md_b:
            if md_a > current:
                colors = colors_a
                current = md_a
        else:
            if md_b > current:
                colors = colors_b
                current = md_b
    print(f"start min distance: {start}")
    print(f"end min distance: {current}")
    return colors

if __name__ == "__main__":
    colors = choose_k_colors(6)

