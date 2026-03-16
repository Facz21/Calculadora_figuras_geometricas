from shapes.shape3d import Shape3D
from math_utils import CustomMath


class Cone(Shape3D):

    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        return (CustomMath.PI * CustomMath.power(self.r, 2) * self.h) / 3

    def surface(self):
        slant = CustomMath.sqrt(self.r*self.r + self.h*self.h)
        return CustomMath.PI * self.r * (self.r + slant)