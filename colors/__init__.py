from .converters import rgb2hsl, rgb2hsv, rgb2lab, hsl2rgb, hsv2rgb, lab2rgb, lab_distance, rgb2lab_map

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

