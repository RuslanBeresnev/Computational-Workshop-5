import math


# Функция f(x) для Варианта 2
class Function:
    @staticmethod
    def f(x):
        return 1 / math.sqrt((1 + x ** 2) * (4 + 3 * x ** 2))

    @staticmethod
    def str():
        return "1 / sqrt((1 + x^2) * (4 + 3 * x^2))"


class Polynom:
    @staticmethod
    def f(coefficients, x):
        n = len(coefficients)
        result = 0
        for k in range(n):
            result += coefficients[k] * (x ** k)
        return result
