from shapes.shape3d import Shape3D
from math_utils import CustomMath


class Cylinder(Shape3D):

    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        return CustomMath.PI * CustomMath.power(self.r, 2) * self.h

    def surface(self):
        return 2 * CustomMath.PI * self.r * (self.r + self.h)