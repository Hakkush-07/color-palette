from subprocess import run

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

a()



