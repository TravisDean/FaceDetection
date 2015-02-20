import glob

from parse import makefacepatch, makerandompatch
from patchdb import PatchDB


__author__ = 'Travis'
debug = True
import sys


def run(facefile, nofaces=None):
    db = PatchDB()
    with open(facefile) as f:
        for line in f:
            split = line.split()
            facefile = 'trainingdata\\' + split[0]
            args = list(map(int, map(float, split[1:])))
            t = makefacepatch(facefile, args[0], args[1], args[2], args[3],
                              args[6], args[7], args[10], args[11])
            db.addPatch(facefile, t)

    if nofaces is not None:
        for g in glob.glob(nofaces):
            t = makerandompatch(g)
            db.addPatch(g, t, face=False)

    db.drawCollage()

    # img = loadimage(filename)
    # Do things to it here.


if __name__ == "__main__":
    if not debug:
        try:
            run(facefile=sys.argv[1])
        except Exception as e:
            print('Invalid input: ' + str(e))
    else:
        run('testdata.txt')
