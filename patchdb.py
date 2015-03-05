from collections import defaultdict
import util

__author__ = 'Travis'
from PIL import Image
import numpy as np


class PatchDB(object):
    def __init__(self):
        self.mapping = defaultdict(list)
        self.pilFaces = []
        self.faces = []
        self.notfaces = []

    def addPatch(self, filename, patch, face=True):
        self.mapping[filename].append(patch)
        if face:
            self.pilFaces.append(patch)
            self.faces.append(np.array(patch).ravel())
        else:
            self.notfaces.append(patch)


    def drawCollage(self):
        x = 0
        y = 0
        # patches = list(self.data.values())
        sidesize = 240
        collage = Image.new(mode="L", size=(sidesize, sidesize), color="blue")
        for v in self.pilFaces:
            s = v.resize((24, 24), Image.ANTIALIAS)
            collage.paste(s, (x, y))
            x += 24
            if x >= 240:
                y += 24
                x = 0
        # collage.show()
        collage.save("collage.png")

    def meanimage(self):
        faces = np.array(self.faces)
        meanface = faces.mean(axis=0)
        # meanface = np.median(faces, axis=0)
        # util.gshow(meanface)
        util.saveimage(meanface.reshape(12,12), "mean.png")
        self.avgface = meanface.ravel()

    def cov(self):
        return np.corrcoef(self.avgface, self.faces[9])
        # return np.corrcov(self.avgface,self.faces[0])