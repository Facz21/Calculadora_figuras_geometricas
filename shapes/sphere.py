from shapes.shape3d import Shape3D
from math_utils import CustomMath


class Sphere(Shape3D):

    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4/3) * CustomMath.PI * CustomMath.power(self.r, 3)

    def surface(self):
        return 4 * CustomMath.PI * CustomMath.power(self.r, 2)