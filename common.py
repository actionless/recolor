
def rgb2hex(pixel):
    """ convert an (R, G, B) tuple to #RRGGBB """
    r, g, b, a = pixel
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def hex2rgb(colorstring):
    """ convert #RRGGBB to an (R, G, B) tuple """
    colorstring = colorstring.strip()
    if colorstring[0] == '#':
        colorstring = colorstring[1:]
    if len(colorstring) != 6:
        raise(ValueError("input #%s is not in #RRGGBB format" % colorstring))
    r, g, b = colorstring[:2], colorstring[2:4], colorstring[4:]
    r, g, b = [int(n, 16) for n in (r, g, b)]
    return r, g, b
