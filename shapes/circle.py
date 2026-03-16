from shapes.shape2d import Shape2D
from math_utils import CustomMath


class Circle(Shape2D):

    def __init__(self, r):
        self.r = r

    def area(self):
        return CustomMath.PI * CustomMath.power(self.r, 2)

    def perimeter(self):
        return 2 * CustomMath.PI * self.r