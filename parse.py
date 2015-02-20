import random

from PIL import Image, ImageOps

from point import Point


__author__ = 'Travis'

ground = []


# Needs to make return a square shape in size 12x12
def getfacebounds(lex, ley, lmx, lmy, rex, rey, rmx, rmy):
    tl = Point(min(lex, lmx), min(ley, rey))
    br = Point(max(rex, rmx), max(lmy, rmy))
    xrg = br.x - tl.x
    yrg = br.y - tl.y
    maxinside = max(xrg, yrg)
    scale = maxinside / 4
    if xrg > yrg:
        tl.x -= scale
        tl.y -= (xrg - yrg) / 2 + scale
        br.x += scale
        br.y += (xrg - yrg) / 2 + scale
    else:
        tl.x -= (yrg - xrg) / 2 + scale
        tl.y -= scale
        br.x += (yrg - xrg) / 2 + scale
        br.y += scale

    return (tl.toint(), br.toint())
    # return np.s_[tl.y:br.y,
    # tl.x:br.x]


def makefacepatch(filename, lex, ley, rex, rey, lmx, lmy, rmx, rmy):
    # img = loadimage(filename)
    pimg = Image.open(filename)
    tl, br = getfacebounds(lex, ley, lmx, lmy, rex, rey, rmx, rmy)
    # draw = ImageDraw.Draw(pimg)
    # draw.rectangle([tl.x,tl.y,br.x,br.y],fill=128)

    crp = pimg.copy()
    crp = crp.crop([tl.x, tl.y, br.x, br.y])
    rsz = crp.resize((12, 12), Image.ANTIALIAS)
    eqlz = ImageOps.autocontrast(rsz, 5)
    # rsz.show()

    return eqlz
    # pimg.crop()
    # pimg.
    # pimg.show()


def makerandompatch(filename):
    pimg = Image.open(filename)
    mx, my = pimg.size
    rndx = random.randint(12, mx - 12)
    rndy = random.randint(12, my - 12)

    # pimg = pimg.crop([])

    pass


fn = "voyager.gif"
defaults = list(map(int, map(float,
                             "122.0 43.0 137.0 47.0 123.0 59.0 133.0 62.0".split())))

makefacepatch(fn, *defaults)