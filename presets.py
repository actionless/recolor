from common import rgb2hex, hex2rgb


R = 0
G = 1
B = 2
A = 3


def blue_to_green(r, g, b, a):
    return r, b, g, a


def blue_to_red(r, g, b, a):
    return b, g, r, a


def blue_to_purple(r, g, b, a):
    return g, r, b, a


def blue_to_light_green(r, g, b, a):
    return g, b, r, a


def blue_to_pink(r, g, b, a):
    return b, r, g, a


def invert(r, g, b, a):
    r = 255 - int(r)
    g = 255 - int(g)
    b = 255 - int(b)
    return r, g, b, a


def only_blue_to_pink(r, g, b, a):
    if b > r and b > g:
        r, b = b, r
        g, b = b, g
    return r, g, b, a


def replace_colors(pixel, replacements):
    pixel_hex = rgb2hex(pixel)
    for name, (condition, replacement) in replacements.items():
        if pixel_hex == condition:
            r, g, b = hex2rgb(replacement)
            return r, g, b, pixel[A]
    # return pixel


def arc_recolor(pixel):
    replacements = {
        # "SELECTION_BG": ("#5294e2", "#cc6699"),
        "SELECTION_BG": ("#5294e2", "#aa3683"),
        # "INPUT_BG": ("#ffffff", "#c0bbbb"),
        "MENU_BG": ("#2f343b", "#0e0021"),
        "MENU_FG": ("#afbbc5", "#bcbcbc"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        # darker:
        return (r - 107, g - 105, b - 110, a)


def arc_magenta(pixel):
    new_pixel = replace_colors(pixel, {
        "SELECTION_BG": ("#5294e2", "#aa3683"),
    })
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        # blue to purple
        r, g = g, r
        return (r, g, b, a)


def arc_red(pixel):
    new_pixel = replace_colors(pixel, {
        "SELECTION_BG": ("#5294e2", "#e2527d"),
    })
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        return (g, b, r, a)


def arc_pink(pixel):
    # new_pixel = replace_colors(pixel, {
        # "SELECTION_BG": ("#5294e2", "#e2527d"),
    # })
    # if new_pixel:
        # return new_pixel
    # else:
    r, g, b, a = pixel
    return (b, r, g, a)


def fl_recolor(pixel):
    replacements = {
        "BG": ("#0d0309", "#0e0021"),
        "FG": ("#ffcc66", "#bbbcb7"),
        "TEXT_FG": ("#9999ff", "#bcbcbc"),
        "GTK2_BUTTON_BG": ("#cc99cc", "#9575c5"),
        "GTK3_BUTTON_BG": ("#cc9966", "#9575c5"),
        "SELECTION_BG": ("#ff9900", "#c57595"),
        "SELECTION_BG2": ("#cc6699", "#c57595"),
        "DISABLED_BG": ("#666699", "#465457"),
        "FOCUS": ("#ff3300", "#95c575"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        return pixel


def fl_recolor_light(pixel):
    replacements = {
        "BG": ("#0d0309", "#bbbcb7"),
        "BG2": ("#000000", "#bbbcb7"),
        "FG": ("#ffcc66", "#0e0021"),
        "TEXT_FG": ("#9999ff", "#181a15"),
        "GTK2_BUTTON_BG": ("#cc99cc", "#9575c5"),
        "GTK2_BUTTON_BG_FOCUS": ("#d4a9d4", "#6f36be"),
        "GTK3_BUTTON_BG": ("#cc9966", "#9575c5"),
        "SELECTION_BG": ("#ff9900", "#c57595"),
        "SELECTION_BG2": ("#cc6699", "#c57595"),
        "DISABLED_BG": ("#666699", "#465457"),
        "FOCUS": ("#ff3300", "#95c575"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        return pixel


def numix1(pixel):
    replacements = {
        # "BG": ("#0d0309", "#bbbcb7"),
        "SELECTION_BG": ("#f0544c", "#c57595"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        # darker:
        r, g, b, a = pixel
        return (r - 102, g - 100, b - 105, a)


def numix2(pixel):
    replacements = {
        # "BG": ("#0d0309", "#bbbcb7"),
        "SELECTION_BG": ("#f0544c", "#c57595"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        # darker:
        r, g, b, a = pixel
        return (r - 51, g - 50, b - 55, a)
