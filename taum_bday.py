def taumBday(b, w, bc, wc, z):
    return b * min(bc, wc+z) + w * (min(bc+z, wc))