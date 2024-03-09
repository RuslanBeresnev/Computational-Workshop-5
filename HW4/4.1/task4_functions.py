from abc import ABC, abstractmethod


class AbstractFunction(ABC):
    @abstractmethod
    def f(self, x):
        pass

    @abstractmethod
    def f_integral(self, x):
        pass

    @abstractmethod
    def f_definite_integral(self, a, b):
        pass

    @abstractmethod
    def str(self):
        pass

    @abstractmethod
    def str_integral(self):
        pass


class Function(AbstractFunction):
    def f(self, x):
        return x ** 3

    def f_integral(self, x):
        return (x ** 4) / 4

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def str(self):
        return "f(x) = x ^ 3"

    def str_integral(self):
        return "∫ f(x) dx = (x ^ 4) / 4 + C"


class ConstFunction(AbstractFunction):
    def f(self, x):
        return 1

    def f_integral(self, x):
        return x

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def str(self):
        return "f(x) = 1"

    def str_integral(self):
        return "∫ f(x) dx = x + C"


class FirstDegreePolynomialFunction(AbstractFunction):
    def f(self, x):
        return x + 1

    def f_integral(self, x):
        return (x ** 2) / 2 + x

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def str(self):
        return "f(x) = x + 1"

    def str_integral(self):
        return "∫ f(x) dx = (x ^ 2) / 2 + x + C"


class SecondDegreePolynomialFunction(AbstractFunction):
    def f(self, x):
        return x ** 2 + x + 1

    def f_integral(self, x):
        return (x ** 3) / 3 + (x ** 2) / 2 + x

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def str(self):
        return "f(x) = x ^ 2 + x + 1"

    def str_integral(self):
        return "∫ f(x) dx = (x ^ 3) / 3 + (x ^ 2) / 2 + x + C"


class ThirdDegreePolynomialFunction(AbstractFunction):
    def f(self, x):
        return x ** 3 + x ** 2 + x + 1

    def f_integral(self, x):
        return (x ** 4) / 4 + (x ** 3) / 3 + (x ** 2) / 2 + x

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def str(self):
        return "f(x) = x ^ 3 + x ^ 2 + x + 1"

    def str_integral(self):
        return "∫ f(x) dx = (x ^ 4) / 4 + (x ^ 3) / 3 + (x ^ 2) / 2 + x + C"
