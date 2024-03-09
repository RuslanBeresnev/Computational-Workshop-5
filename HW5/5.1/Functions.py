from math import sin


# Функция f(x) для Варианта 2
class Function:
    @staticmethod
    def f(x):
        return sin(x)

    @staticmethod
    def str():
        return "sin(x)"


# Весовая функция для Варианта 2
class Weight:
    @staticmethod
    def w(x):
        return x ** (1 / 4)

    @staticmethod
    def str():
        return "x ^ (1/4)"


class Polynom:
    @staticmethod
    def f(coefficients, x):
        n = len(coefficients)
        result = 0
        for k in range(n):
            result += coefficients[k] * (x ** k)
        return result
