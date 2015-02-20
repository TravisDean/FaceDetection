__author__ = 'Travis'


class Point(object):
    """Keeps track of the dataset items."""

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def toint(self):
        self.x = int(self.x)
        self.y = int(self.y)
        return self

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

