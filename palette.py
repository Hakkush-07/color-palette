from random import randint, seed
from converters import rgb2lab
from distance import color_difference_lab

def random_rgb():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def build_distance_matrix(labs):
    size = len(labs)
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(i + 1, size):
            d = color_difference_lab(labs[i], labs[j])
            matrix[i][j] = d
            matrix[j][i] = d
    return matrix

def find_min_pair(matrix):
    size = len(matrix)
    if size < 2:
        return 0, (0, 0)
    best = None
    best_i = 0
    best_j = 1
    for i in range(size):
        for j in range(i + 1, size):
            d = matrix[i][j]
            if best is None or d < best:
                best = d
                best_i = i
                best_j = j
    return best, (best_i, best_j)

def min_excluding_index(matrix, idx):
    size = len(matrix)
    if size < 3:
        return 0, (0, 0)
    best = None
    best_pair = (0, 0)
    for i in range(size):
        if i == idx:
            continue
        for j in range(i + 1, size):
            if j == idx:
                continue
            d = matrix[i][j]
            if best is None or d < best:
                best = d
                best_pair = (i, j)
    return (best if best is not None else 0), best_pair

def min_for_replacement(index, new_lab, labs, matrix, current_min, current_pair):
    size = len(labs)
    new_distances = [0.0] * size
    min_new = None
    min_new_j = 0
    for j in range(size):
        if j == index:
            continue
        d = color_difference_lab(new_lab, labs[j])
        new_distances[j] = d
        if min_new is None or d < min_new:
            min_new = d
            min_new_j = j
    if current_pair[0] == index or current_pair[1] == index:
        min_unaffected, pair_unaffected = min_excluding_index(matrix, index)
    else:
        min_unaffected = current_min
        pair_unaffected = current_pair
    if min_new is None:
        min_new = 0
        min_new_j = 0
    if min_new <= min_unaffected:
        return min_new, (index, min_new_j), new_distances
    return min_unaffected, pair_unaffected, new_distances

# choose k colors with big min distance
def choose_k_colors(k, iterations=100000, seed_value=None):
    if seed_value is not None:
        seed(seed_value)
    colors = [random_rgb() for _ in range(k)]
    labs = [rgb2lab(*color) for color in colors]
    matrix = build_distance_matrix(labs)
    current, current_pair = find_min_pair(matrix)
    start = current
    for i in range(iterations):
        print(i, iterations)
        a, b = current_pair
        A_lab, B_lab = labs[a], labs[b]
        C = random_rgb()
        C_lab = rgb2lab(*C)
        if color_difference_lab(A_lab, C_lab) < current or color_difference_lab(B_lab, C_lab) < current:
            continue
        colors_a = colors.copy()
        colors_b = colors.copy()
        colors_a[a] = C
        colors_b[b] = C
        labs_a = labs.copy()
        labs_b = labs.copy()
        labs_a[a] = C_lab
        labs_b[b] = C_lab
        md_a, pair_a, distances_a = min_for_replacement(a, C_lab, labs, matrix, current, current_pair)
        md_b, pair_b, distances_b = min_for_replacement(b, C_lab, labs, matrix, current, current_pair)
        if md_a > md_b:
            if md_a > current:
                colors = colors_a
                labs = labs_a
                for j in range(len(labs)):
                    if j == a:
                        continue
                    matrix[a][j] = distances_a[j]
                    matrix[j][a] = distances_a[j]
                current = md_a
                current_pair = pair_a
        else:
            if md_b > current:
                colors = colors_b
                labs = labs_b
                for j in range(len(labs)):
                    if j == b:
                        continue
                    matrix[b][j] = distances_b[j]
                    matrix[j][b] = distances_b[j]
                current = md_b
                current_pair = pair_b
    print(f"start min distance: {start}")
    print(f"end min distance: {current}")
    return colors

if __name__ == "__main__":
    colors = choose_k_colors(6)
