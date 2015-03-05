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
    scale = maxinside / 2
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

    return tl.toint(), br.toint()


def makefacepatch(filename, lex, ley, rex, rey, lmx, lmy, rmx, rmy):
    pimg = Image.open(filename)
    tl, br = getfacebounds(lex, ley, lmx, lmy, rex, rey, rmx, rmy)

    crp = pimg.copy()
    crp = crp.crop([tl.x, tl.y, br.x, br.y])
    ret = crp.resize((12, 12), Image.ANTIALIAS)

    return ret


def makerandompatch(filename):
    pimg = Image.open(filename).convert('L')
    mx, my = pimg.size
    rndx = random.randint(0, mx - 12)
    rndy = random.randint(0, my - 12)
    # print(str(rndx) + " - " + str(rndy))

    crp = pimg.copy()
    crp = crp.crop([rndx, rndy, rndx+12, rndy+12])
    ret = crp.resize((12, 12), Image.ANTIALIAS)
    return ret


fn = "voyager.gif"
defaults = list(map(int, map(float,
                             "122.0 43.0 137.0 47.0 123.0 59.0 133.0 62.0".split())))

makefacepatch(fn, *defaults)