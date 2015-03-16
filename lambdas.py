def blue_to_red(pixel):
    r, g, b, a = pixel
    r, b = b, r
    return r, g, b, a


def blue_to_green(pixel):
    r, g, b, a = pixel
    g, b = b, g
    return r, g, b, a


def invert(pixel):
    r, g, b, a = pixel
    r = 255 - int(r)
    g = 255 - int(g)
    b = 255 - int(b)
    return r, g, b, a


def blue_to_acid_green(pixel):
    return blue_to_red(blue_to_green(pixel))


def only_blue_to_pink(pixel):
    r, g, b, a = pixel
    if b > r and b > g:
        r, b = b, r
        g, b = b, g
    return r, g, b, a


def blue_to_pink(pixel):
    r, g, b, a = pixel
    r, b = b, r
    g, b = b, g
    return r, g, b, a


def blue_to_purple(pixel):
    r, g, b, a = pixel
    r, g = g, r
    return r, g, b, a
