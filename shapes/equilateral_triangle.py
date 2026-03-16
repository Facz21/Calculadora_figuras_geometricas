from shapes.shape2d import Shape2D
from math_utils import CustomMath


class EquilateralTriangle(Shape2D):

    def __init__(self, side):
        self.side = side

    def area(self):
        return (CustomMath.sqrt(3) / 4) * CustomMath.power(self.side, 2)

    def perimeter(self):
        return 3 * self.side