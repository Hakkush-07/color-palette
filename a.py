from subprocess import run

color_a, color_b, color_c, color_d, color_e, color_f = "color_a", "color_b", "color_c", "color_d", "color_e", "color_f"
colors = [color_a, color_b, color_c, color_d, color_e, color_f]

def g(s):
    if not s:
        return []
    for i, day in enumerate(["M", "T", "W", "Th", "F"][::-1]):
        if s.startswith(day):
            return [5 - i] + g(s[len(day):])

def f():
    dct = {}
    colored = []
    with open("courses.txt", "r+") as file:
        for line in file.read().splitlines():
            if not line:
                continue
            lst = line.split()
            name, time, description = lst if len(lst) == 3 else (*lst, "")
            slots = [int(c) for c in time if c.isdigit()]
            days = g("".join([c for c in time if not c.isdigit()]))
            if name not in colored:
                colored.append(name)
            color = colors[colored.index(name)]
            for day, slot in zip(days, slots):
                dct[(day, slot)] = dct.get((day, slot), []) + [(name, description, color)]
    s = []
    for k, v in dct.items():
        day, slot = k
        if len(v) == 1:
            n, d, c = v[0]
            s.append(f"coloring2({day}, {slot}, \"{n}\", \"{d}\", {c});")
        elif len(v) == 2:
            n1, d1, c1 = v[0]
            n2, d2, c2 = v[1]
            s.append(f"conflict({day}, {slot}, \"{n1}\", \"{n2}\", {c1}, {c2});")
        else:
            s.append(f"coloring2({day}, {slot}, \"CONFLICT[{len(v)}]\", \"\", white);")
    ss = "\n".join(s)
    with open("template.txt", "r+") as file:
        content = file.read()
        new = content.replace("REPLACE", ss)
    with open(f"test.asy", "w+") as file:
        file.write(new)
    run(["asy", f"test.asy"])

f()
