from shapes.shape3d import Shape3D
from math_utils import CustomMath


class Cube(Shape3D):

    def __init__(self, side):
        self.side = side

    def volume(self):
        return CustomMath.power(self.side, 3)

    def surface(self):
        return 6 * CustomMath.power(self.side, 2)