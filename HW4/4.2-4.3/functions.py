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
    def f_diff(self, x):
        pass

    @abstractmethod
    def f_2diff(self, x):
        pass

    @abstractmethod
    def f_3diff(self, x):
        pass

    @abstractmethod
    def f_4diff(self, x):
        pass

    @abstractmethod
    def f_5diff(self, x):
        pass

    @abstractmethod
    def str(self):
        pass

    @abstractmethod
    def str_integral(self):
        pass


class MyFunction(AbstractFunction):
    def f(self, x):
        return (x ** 5) + (x ** 4)

    def f_integral(self, x):
        return (x ** 6) / 6 + (x ** 5) / 5

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def f_diff(self, x):
        return 5 * (x ** 4) + 4 * (x ** 3)

    def f_2diff(self, x):
        return 20 * (x ** 3) + 12 * (x ** 2)

    def f_3diff(self, x):
        return 60 * (x ** 2) + 24 * x

    def f_4diff(self, x):
        return 120 * x + 24

    def f_5diff(self, x):
        return 120

    def str(self):
        return "f(x) = x ^ 5 + x ^ 4"

    def str_integral(self):
        return "∫ f(x) dx = (x ^ 6) / 6 + (x ^ 5) / 5 + C"


class ConstFunction(AbstractFunction):
    def f(self, x):
        return 1

    def f_integral(self, x):
        return x

    def f_definite_integral(self, a, b):
        return self.f_integral(b) - self.f_integral(a)

    def f_diff(self, x):
        return 0

    def f_2diff(self, x):
        return 0

    def f_3diff(self, x):
        return 0

    def f_4diff(self, x):
        return 0

    def f_5diff(self, x):
        return 0

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

    def f_diff(self, x):
        return 1

    def f_2diff(self, x):
        return 0

    def f_3diff(self, x):
        return 0

    def f_4diff(self, x):
        return 0

    def f_5diff(self, x):
        return 0

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

    def f_diff(self, x):
        return 2 * x + 1

    def f_2diff(self, x):
        return 2

    def f_3diff(self, x):
        return 0

    def f_4diff(self, x):
        return 0

    def f_5diff(self, x):
        return 0

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

    def f_diff(self, x):
        return 3 * (x ** 2) + 2 * x

    def f_2diff(self, x):
        return 6 * x + 2

    def f_3diff(self, x):
        return 6

    def f_4diff(self, x):
        return 0

    def f_5diff(self, x):
        return 0

    def str(self):
        return "f(x) = x ^ 3 + x ^ 2 + x + 1"

    def str_integral(self):
        return "∫ f(x) dx = (x ^ 4) / 4 + (x ^ 3) / 3 + (x ^ 2) / 2 + x + C"
