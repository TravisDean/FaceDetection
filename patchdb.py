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
        self.pilnoise = []
        self.noise = []

    def addPatch(self, filename, patch, face=True):
        self.mapping[filename].append(patch)
        if face:
            self.pilFaces.append(patch)
            self.faces.append(np.array(patch).ravel())
        else:
            self.pilnoise.append(patch)
            nrp = np.array(patch)
            nrpr = nrp.ravel()
            # self.noise.append(np.array(patch).ravel())

            self.noise.append(nrpr)

    def drawCollage(self):
        x = 0
        y = 0
        # patches = list(self.data.values())
        sidesize = 240
        collage = Image.new(mode="L", size=(sidesize*2, sidesize), color="blue")
        for v in self.pilFaces[:100]:
            s = v.resize((24, 24), Image.ANTIALIAS)
            collage.paste(s, (x, y))
            x += 24
            if x >= 240:
                y += 24
                x = 0
        y = 0
        x = 240
        for v in self.pilnoise[:100]:
            s = v.resize((24, 24), Image.ANTIALIAS)
            collage.paste(s, (x,y))
            x += 24
            if x >= 480:
                y += 24
                x = 240

        # collage.show()
        collage.save("collage.png")

    def getmeans(self):
        faces = np.array(self.faces)
        noise = np.array(self.noise)
        meanface = faces.mean(axis=0)
        meannoise = noise.mean(axis=0)
        # util.gshow(meanface)
        # util.gshow(meannoise)
        util.saveimage(meanface.reshape(12,12), "meanface.png")
        util.saveimage(meannoise.reshape(12,12), "meannoise.png")
        self.avgface = meanface.ravel()
        self.avgnoise = meannoise.ravel()


    def cov(self):
        return np.corrcoef(self.avgface, self.faces[9])
        # return np.corrcov(self.avgface,self.faces[0])