__author__ = 'Travis'
__author__ = 'Travis'
import math
import os

import numpy as np
import pylab
import skimage.color
from pylab import cm as cm
import skimage
import skimage.io
from scipy.misc import imsave


def angle(a, b):
    return math.atan2(b.y - a.y, b.x - a.x)


def clip(i, a, b):
    return max(a, min(i, b))


def access_zeroclip(img, x, y):
    h, w = img.shape
    if x < 0 or y < 0 or x > w - 1 or y > h - 1:
        return np.zeros(img.shape)
    return img[y, x]


def access_edgeclip(img, x, y):
    h, w = img.shape
    x = clip(x, 0, w - 1)
    y = clip(y, 0, h - 1)
    return img[y, x]


def imgname(filename):
    return os.path.splitext(filename)[0]


def loadimage(name):
    i = skimage.color.rgb2gray(skimage.img_as_float(skimage.io.imread(name)))
    return i


def saveimage(i, name):
    imsave(name, i)
    return


def ishow(i, colormap=None):
    pylab.imshow(i, cmap=colormap, interpolation=None)
    pylab.show()


def gshow(i):
    pylab.imshow(i, cmap=cm.get_cmap('gray'))#, interpolation=None)
    pylab.show()



