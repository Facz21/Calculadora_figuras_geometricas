class CustomMath:

    PI = 3.141592653589793

    @staticmethod
    def power(base, exp):
        result = 1
        for _ in range(exp):
            result *= base
        return result

    @staticmethod
    def sqrt(value):

        if value <= 0:
            return 0

        guess = value / 2

        for _ in range(20):
            guess = (guess + value / guess) / 2

        return guess