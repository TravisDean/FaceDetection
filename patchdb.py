from collections import defaultdict

__author__ = 'Travis'
from PIL import Image


class PatchDB(object):
    def __init__(self):
        self.mapping = defaultdict(list)
        self.faces = []
        self.notfaces = []

    def addPatch(self, filename, patch, face=True):
        self.mapping[filename].append(patch)
        if face:
            self.faces.append(patch)
        else:
            self.notfaces.append(patch)


    def drawCollage(self):
        x = 0
        y = 0
        # patches = list(self.data.values())
        sidesize = 240
        collage = Image.new(mode="L", size=(sidesize, sidesize), color="blue")
        for v in self.faces:
            s = v.resize((24, 24), Image.ANTIALIAS)
            collage.paste(s, (x, y))
            x += 24
            if x >= 240:
                y += 24
                x = 0
        collage.show()
        collage.save("collage.png")


