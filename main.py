import glob

from parse import makefacepatch, makerandompatch
from patchdb import PatchDB
__author__ = 'Travis'
debug = False
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
            for _ in range(25):
                t = makerandompatch(g)
                db.addPatch(g, t, face=False)

    db.drawCollage()

    db.getmeans()

    correct_faces = 0
    for f in db.faces:
        if db.gauss_decision(f):
            correct_faces += 1
    correct_noise = 0
    for n in db.noise:
        if db.gauss_decision(n):
            correct_noise += 1
    print( "Correctly classified faces: {} of {}: {}%".format(correct_faces, len(db.faces), correct_faces/len(db.faces)))
    print( "Correctly classified noise: {} of {}: {}%".format(correct_noise, len(db.noise), correct_noise/len(db.noise)))



if __name__ == "__main__":
    if not debug:
        try:
            run(facefile=sys.argv[1], nofaces=sys.argv[2])
        except Exception as e:
            print('Invalid input: ' + str(e))
    else:
        run('testfaces.txt', './notfaces/*.*')
