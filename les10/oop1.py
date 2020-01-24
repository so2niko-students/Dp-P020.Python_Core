class Point:
    def __init__ (self, x, y, z):
        self.coord = (x, y, z)

    def __repr__ (self):
        return "Point (%s, %s, %s)" % self.coord

    def __del__ (self):
        print('Object is deleted')

P = Point(0.0, 1.0, 0.0)
print(P)