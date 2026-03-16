from shapes.shape2d import Shape2D
from math_utils import CustomMath


class RightTriangle(Shape2D):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hypotenuse(self):
        return CustomMath.sqrt(self.a*self.a + self.b*self.b)

    def area(self):
        return (self.a * self.b) / 2

    def perimeter(self):
        return self.a + self.b + self.hypotenuse()