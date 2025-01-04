def rgb2hsv(r, g, b):
    mx = max([r, g, b])
    mn = min([r, g, b])
    mxk = mx / 255
    mnk = mn / 255
    d = mxk - mnk
    rx, gx, bx = r / 255, g / 255, b / 255
    if d == 0:
        h = 0
    elif mx == r:
        h = 60 * (((gx - bx) / d) % 6)
    elif mx == g:
        h = 60 * ((bx - rx) / d + 2)
    elif mx == b:
        h = 60 * ((rx - gx) / d + 4)
    if mx == 0:
        s = 0
    else:
        s = d / mxk
    v = mxk
    return h, s, v

def hsv2rgb(h, s, v):
    d = v * s
    hx = h / 60
    x = d * (1 - abs(hx % 2 - 1))
    if 0 <= hx < 1:
        rx, gx, bx = d, x, 0
    elif 1 <= hx < 2:
        rx, gx, bx = x, d, 0
    elif 2 <= hx < 3:
        rx, gx, bx = 0, d, x
    elif 3 <= hx < 4:
        rx, gx, bx = 0, x, d
    elif 4 <= hx < 5:
        rx, gx, bx = x, 0, d
    elif 5 <= hx < 6:
        rx, gx, bx = d, 0, x
    m = v - d
    r, g, b = rx + m, gx + m, bx + m
    r, g, b = round(255 * r), round(255 * g), round(255 * b)
    return r, g, b

def rgb2hsl(r, g, b):
    mx = max([r, g, b])
    mn = min([r, g, b])
    mxk = mx / 255
    mnk = mn / 255
    d = mxk - mnk
    rx, gx, bx = r / 255, g / 255, b / 255
    if d == 0:
        h = 0
    elif mx == r:
        h = 60 * (((gx - bx) / d) % 6)
    elif mx == g:
        h = 60 * ((bx - rx) / d + 2)
    elif mx == b:
        h = 60 * ((rx - gx) / d + 4)
    l = (mxk + mnk) / 2
    if l == 0 or l == 1:
        s = 0
    else:
        s = d / (1 - abs(2 * l - 1))
    return h, s, l

def hsl2rgb(h, s, l):
    d = (1 - abs(2 * l - 1)) * s
    hx = h / 60
    x = d * (1 - abs(hx % 2 - 1))
    if 0 <= hx < 1:
        rx, gx, bx = d, x, 0
    elif 1 <= hx < 2:
        rx, gx, bx = x, d, 0
    elif 2 <= hx < 3:
        rx, gx, bx = 0, d, x
    elif 3 <= hx < 4:
        rx, gx, bx = 0, x, d
    elif 4 <= hx < 5:
        rx, gx, bx = x, 0, d
    elif 5 <= hx < 6:
        rx, gx, bx = d, 0, x
    m = l - d / 2
    r, g, b = rx + m, gx + m, bx + m
    r, g, b = round(255 * r), round(255 * g), round(255 * b)
    return r, g, b

def rgb2lab(r, g, b):
    rr = r / 255
    gg = g / 255
    bb = b / 255

    def gm(s):
        return ((s + 0.055) / 1.055) ** 2.4 if s > 0.04045 else s / 12.92
    
    rx = gm(rr) * 100
    gx = gm(gg) * 100
    bx = gm(bb) * 100
    x = rx * 0.4124 + gx * 0.3576 + bx * 0.1805
    y = rx * 0.2126 + gx * 0.7152 + bx * 0.0722
    z = rx * 0.0193 + gx * 0.1192 + bx * 0.950

    xu = x / 95.047
    yu = y / 100.000
    zu = z / 108.883

    def w(t):
        return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    
    xw = w(xu)
    yw = w(yu)
    zw = w(zu)

    l = 116 * yw - 16
    a = 500 * (xw - yw)
    b = 200 * (yw - zw)

    return l, a, b

def lab2rgb(l, a, b):
    yw = (l + 16) / 116
    xw = a / 500 + yw
    zw = yw - b / 200

    def u(t):
        return t ** 3 if t ** 3 > 0.008856 else (t - 16 / 116) / 7.787

    xu = u(xw)
    yu = u(yw)
    zu = u(zw)

    x = xu * 95.047
    y = yu * 100.000
    z = zu * 108.883

    xx = x / 100
    yy = y / 100
    zz = z / 100

    rx = xx *  3.2406 + yy * -1.5372 + zz * -0.4986
    gx = xx * -0.9689 + yy *  1.8758 + zz *  0.0415
    bx = xx *  0.0557 + yy * -0.2040 + zz *  1.0570

    def mg(s):
        return 1.055 * (s ** (1 / 2.4)) - 0.055 if s > 0.0031308 else 12.92 * s

    rm = mg(rx)
    gm = mg(gx)
    bm = mg(bx)

    ra = rm * 255
    ga = gm * 255
    ba = bm * 255

    ra, ga, ba = round(ra), round(ga), round(ba)

    r = 0 if ra < 0 else 255 if ra > 255 else ra
    g = 0 if ga < 0 else 255 if ga > 255 else ga
    b = 0 if ba < 0 else 255 if ba > 255 else ba

    return r, g, b

def test():
    for r in range(256):
        for g in range(256):
            for b in range(256):
                print(r, "rgb-hsvl")
                assert (r, g, b) == hsv2rgb(*rgb2hsv(r, g, b))
                assert (r, g, b) == hsl2rgb(*rgb2hsl(r, g, b))
    for r in range(256):
        for g in range(256):
            for b in range(256):
                print(r, "rgb-lab")
                l, a, bb = rgb2lab(r, g, b)
                rx, gx, bx = lab2rgb(l, a, bb)
                assert abs(r - rx) + abs(g - gx) + abs(b - bx) <= 1

if __name__ == "__main__":
    test()
