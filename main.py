from subprocess import run
from palette import choose_k_colors

def rgb2hex(r, g, b):
    return hex(r)[2:].zfill(2) + hex(g)[2:].zfill(2) + hex(b)[2:].zfill(2)

def main():
    colors = choose_k_colors(10, iterations=100000)
    s = []
    for i, color in enumerate(colors):
        r, g, b = color
        s.append(f"coloring({i % 5}, {i // 5 + 1}, \"\\#{rgb2hex(*color)}\", RGB({r}, {g}, {b}));")
    with open("color-template.asy", "r+") as f:
        x = f.read().replace("REPLACE", "\n".join(s)).replace("NNN", str((len(colors) - 1) // 5 + 1))
    with open("test.asy", "w+") as f2:
        f2.write(x)
    run(["asy", f"test.asy"])

if __name__ == "__main__":
    main()

