from shapes.shape3d import Shape3D
from math_utils import CustomMath


class Pyramid(Shape3D):

    def __init__(self, base, h):
        self.base = base
        self.h = h

    def volume(self):
        return (self.base*self.base*self.h) / 3

    def surface(self):

        slant = CustomMath.sqrt((self.base/2)**2 + self.h*self.h)

        return self.base*self.base + 2*self.base*slant