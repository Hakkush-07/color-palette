from math import acos, sqrt, pi
import pickle

# r, g, b in [0, 255]
# l in [0, 100]
# a, b in [-128, 128]
# h in [0, 360]
# s, l, v in [0, 1]

def rgb2hsv(r, g, b):
    mx = max([r, g, b])
    mn = min([r, g, b])
    v = mx / 255
    s = 1 - mn / mx if mx else 0
    x = r - g / 2 - b / 2
    y = r * r + g * g + b * b - r * g - g * b - b * r
    z = acos(x / sqrt(y)) * 180 / pi
    h = z if g >= b else 360 - z
    return h, s, v

def hsv2rgb(h, s, v):
    mx = 255 * v
    mn = mx * (1 - s)
    z = (mx - mn) * (1 - abs((h / 60) % 2 - 1))
    r = mn if 120 <= h < 240 else mx if h < 60 or h >= 300 else z + mn
    g = mn if 240 <= h else mx if 60 <= h < 180 else z + mn
    b = mn if h < 120 else mx if 180 <= h < 300 else z + mn
    return r, g, b

def rgb2hsl(r, g, b):
    mx = max([r, g, b])
    mn = min([r, g, b])
    d = (mx - mn) / 255
    l = (mx + mn) / 510
    s = d / (1 - abs(2 * l - 1)) if l else 0
    x = r - g / 2 - b / 2
    y = r * r + g * g + b * b - r * g - g * b - b * r
    z = acos(x / sqrt(y)) * 180 / pi
    h = z if g >= b else 360 - z
    return h, s, l

def hsl2rgb(h, s, l):
    d = s * (1 - abs(2 * l-1))
    m = 255 * (l - d / 2)
    x = d * (1 - abs((h / 60) % 2 - 1))
    r = m + (0 if 120 <= h < 240 else 255 * d if h < 60 or h >= 300 else 255 * x)
    g = m + (0 if h >= 240 else 255 * d if 60 <= h < 180 else 255 * x)
    b = m + (0 if h <= 120 else 255 * d if 180 <= h < 300 else 255 * x)
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

    correct = 0 <= ra <= 255 and 0 <= ga <= 255 and 0 <= ba <= 255

    r = 0 if ra < 0 else 255 if ra > 255 else ra
    g = 0 if ga < 0 else 255 if ga > 255 else ga
    b = 0 if ba < 0 else 255 if ba > 255 else ba

    return r, g, b, correct

def test():
    print(rgb2hsv(167, 23, 98))
    print(hsv2rgb(153, 0.675, 0.1313))
    print(rgb2hsl(167, 23, 98))
    print(hsl2rgb(153, 0.675, 0.1313))
    print(rgb2lab(167, 23, 98))
    print(rgb2lab(10, 200, 30))
    print(lab2rgb(*rgb2lab(167, 23, 98)))
    print(lab2rgb(*rgb2lab(10, 200, 30)))
    print(lab2rgb(65, -128, 5))
