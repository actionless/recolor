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


def test(pixel):
    return blue_to_purple(
        *blue_to_red(*invert(*pixel))
    )


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


def arc_monovedek_r(pixel):
    replacements = {
        # "SELECTION_BG": ("#5294e2", "#cc6699"),
        "SELECTION_BG": ("#5294e2", "#aa3683"),
        # "INPUT_BG": ("#ffffff", "#c0bbbb"),
        "MENU_BG": ("#2f343f", "#0e0021"),
        "MENU_FG": ("#afb8c5", "#888a85"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        # darker:
        return (r - 107, g - 105, b - 110, a)


def arc_monovedek_lr(pixel):
    replacements = {
        "SELECTION_BG": ("#5294e2", "#aa3683"),
        "MENU_BG": ("#2f343f", "#0e0021"),
        "MENU_FG2": ("#afb8c5", "#888a85"),
        "MENU_FG3": ("#cfdae7", "#888a85"),
        "SIDE_BG": ("#353945", "#0e0021"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        # darker:
        return (r - 47, g - 45, b - 50, a)


# def arc_monovedek_lr(pixel):
    # replacements = {
        # "SELECTION_BG": ("#5294e2", "#aa3683"),
        # "MENU_BG": ("#2f343f", "#0e0021"),
        # "MENU_FG2": ("#afb8c5", "#888a85"),
        # "MENU_FG3": ("#cfdae7", "#888a85"),
        # "SIDE_BG": ("#353945", "#0e0021"),
    # }
    # new_pixel = replace_colors(pixel, replacements)
    # if new_pixel:
        # return new_pixel
    # else:
        # r, g, b, a = pixel
        # # darker:
        # return (r - 47, g - 45, b - 50, a)


def arc_monomono_lr(pixel):
    replacements = {
        "SELECTION_BG": ("#5294e2", "#aa3683"),
        "MENU_BG": ("#2f343f", "#0e0021"),
        "MENU_FG2": ("#afb8c5", "#888a85"),
        "MENU_FG3": ("#cfdae7", "#888a85"),
        "SIDE_BG": ("#353945", "#0e0021"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        # darker:
        return (r - 46, g - 41, b - 50, a)


def arc_win9(pixel):
    replacements = {
        "BG": ("#f5f6f7", "#bfbfbf"),
        "SELECTION_BG": ("#5294e2", "#00007f"),
        "MENU_BG": ("#2f343f", "#bfbfbf"),
        "MENU_FG2": ("#afb8c5", "#000000"),
        "MENU_FG3": ("#cfdae7", "#000000"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        return pixel
        r, g, b, a = pixel
        # darker:
        return (r - 44, g - 45, b - 46, a)


def vertex98(pixel):
    replacements = {
        "TXT_BG": ("#ffffff", "#ffffff"),
        "PROGRESS_BG": ("#bababc", "#ffffff"),
        # "BG": ("#fafafa", "#bfbfbf"),
        # "BG2": ("#f3f3f5", "#bfbfbf"),

        "SELECTION_BG": ("#5294e2", "#00007f"),
        "MENU_BG": ("#2f343f", "#bfbfbf"),
        "MENU_FG2": ("#afb8c5", "#000000"),
        "MENU_FG3": ("#cfdae7", "#000000"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        if (b - r > 10) and (b - g > 10):
            return (r - 40, g - 80, b - 124, a)
        # darker:
        return (r - 59, g - 59, b - 59, a)


def arc_monovedek_lp(pixel):
    replacements = {
        "SELECTION_BG": ("#5294e2", "#963696"),
    }
    new_pixel = replace_colors(pixel, replacements)
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        # darker:
        return (r - 37, g - 35, b - 40, a)


def arc_magenta(pixel):
    new_pixel = replace_colors(pixel, {
        "SELECTION_BG": ("#5294e2", "#aa3683"),
    })
    if new_pixel:
        return new_pixel
    else:
        return blue_to_purple(*pixel)
        # return blue_to_light_green(*pixel)


def arc_purple(pixel):
    new_pixel = replace_colors(pixel, {
        "SELECTION_BG": ("#5294e2", "#963696"),
    })
    if new_pixel:
        return new_pixel
    else:
        return blue_to_purple(*pixel)
        # return blue_to_light_green(*pixel)


def arc_purple2(pixel):
    new_pixel = replace_colors(pixel, {
        "SELECTION_BG": ("#5294e2", "#963696"),
    })
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = blue_to_purple(*pixel)
        return r-38, g-47, b-30, a


def arc_red(pixel):
    new_pixel = replace_colors(pixel, {
        "SELECTION_BG": ("#5294e2", "#e2527d"),
    })
    if new_pixel:
        return new_pixel
    else:
        r, g, b, a = pixel
        return (g, b, r, a)


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
