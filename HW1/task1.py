from math import sin, cos, log


class Function:
    @staticmethod
    def f(x):
        return 2 ** (-x) - sin(x)

    @staticmethod
    def str():
        return "2^(-x) - sin(x)"

    @staticmethod
    def f_diff(x):
        return - log(2) / (2 ** x) - cos(x)


a = -5
b = 10
epsilon = 10 ** -12
n = 100

print("ЧИСЛЕННЫЕ МЕТОДЫ РЕШЕНИЯ НЕЛИНЕЙНЫХ УРАВНЕНИЙ")
print(f"f(x) = {Function.str()}")
print(f"A = {a}")
print(f"B = {b}")
print(f"Epsilon = {epsilon}")
print(f"N = {n}\n")

# Отделение корней уравнения f(x)=0
print("----------ОТДЕЛЕНИЕ КОРНЕЙ УРАВНЕНИЯ f(x)=0----------")


def equation_roots_separating(a, b, n):
    segments = []
    h = (b - a) / n
    counter = 0
    x1 = a
    y1 = Function.f(x1)
    x2 = x1 + h

    while True:
        if x2 > b:
            break

        y2 = Function.f(x2)
        if y1 * y2 <= 0:
            counter += 1
            print(f"[{x1:.3f}, {x2:.3f}]", end=" ")
            segments.append((x1, x2))
        x1 = x2
        x2 = x1 + h
        y1 = y2

    return (segments, counter)


segments, count_of_segments = equation_roots_separating(a, b, n)
print(f"\nКоличество отрезков: {count_of_segments}\n")
print("\n\n")


def bisection_method(segment):
    print("МЕТОД ПОЛОВИННОГО ДЕЛЕНИЯ")
    a_i, b_i = segment
    print(f"Начальное приближение: {(a_i + b_i) / 2}")
    amount_of_steps = 0
    while True:
        c = (a_i + b_i) / 2
        if Function.f(a_i) * Function.f(c) <= 0:
            b_i = c
        else:
            a_i = c

        if (b_i - a_i) <= 2 * epsilon:
            break
        amount_of_steps += 1

    x = (a_i + b_i) / 2
    delta = (b_i - a_i) / 2
    print(f"Количество шагов: {amount_of_steps}")
    print(f"x = {x}, Δ = {delta}, r = {abs(Function.f(x))}\n")


def newtons_method(segment):
    print("МЕТОД НЬЮТОНА")
    x_k = (segment[0] + segment[1]) / 2
    x_k_next = x_k - Function.f(x_k) / Function.f_diff(x_k)
    print(f"Начальное приближение: {x_k}")
    steps = 1
    while abs(x_k_next - x_k) > epsilon:
        x_k = x_k_next
        x_k_next = x_k - Function.f(x_k) / Function.f_diff(x_k)
        steps += 1
    print(f"Количество шагов: {steps}")
    print(f"x_m: {x_k_next}; Δ: {x_k_next - x_k}; r: {abs(Function.f(x_k_next))}")
    print()


def modified_newton_method(segment):
    print("МОДИФИЦИРОВАННЫЙ МЕТОД НЬЮТОНА")
    a_i, b_i = segment
    x_o = (a_i + b_i) / 2

    print(f"Начальное приближение: {x_o}")
    amount_of_steps = 0
    x_k_pred = x_o
    while True:
        x_k = x_k_pred - Function.f(x_k_pred) / Function.f_diff(x_o)
        if abs(x_k - x_k_pred) < epsilon:
            break
        amount_of_steps += 1
        x_k_pred = x_k

    delta = abs(x_k - x_k_pred)
    print(f"Количество шагов: {amount_of_steps}")
    print(f"x = {x_k}, Δ = {delta}, r = {abs(Function.f(x_k))}\n")


def secants_method(segment):
    print("МЕТОД СЕКУЩИХ")
    x_k_prev, x_k = segment
    x_k_next = x_k - Function.f(x_k) * (x_k - x_k_prev) / (Function.f(x_k) - Function.f(x_k_prev))
    print(f"Начальные приближения: {x_k_prev} и {x_k}")
    steps = 1
    while abs(x_k_next - x_k) > epsilon:
        x_k = x_k_next
        x_k_next = x_k - Function.f(x_k) * (x_k - x_k_prev) / (Function.f(x_k) - Function.f(x_k_prev))
        steps += 1
    print(f"Количество шагов: {steps}")
    print(f"x_m: {x_k_next}; Δ: {x_k_next - x_k}; r: {abs(Function.f(x_k_next))}")
    print()


for segment in segments:
    print(f"Уточнение корня на отрезке [{segment[0]:.3f}, {segment[1]:.3f}]")
    bisection_method(segment)
    newtons_method(segment)
    modified_newton_method(segment)
    secants_method(segment)
    print("\n\n")
