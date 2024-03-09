from math import log


class Function:
    @staticmethod
    def f(x):
        return log(1 + x)

    @staticmethod
    def str():
        return "f(x) = ln(1 + x)"


def create_table_of_values(a, b, m_plus_one):
    table = []
    h = (b - a) / (m_plus_one - 1)
    for i in range(m_plus_one):
        x_i = a + i * h
        f_x_i = Function.f(x_i)
        table.append([x_i, f_x_i])
    return table


def newton_interpolation_method(x, n, table):
    a_i = []

    for i in range(n + 1):
        subtrahend = 0
        multiplicator = 1
        for j in range(i):
            subtrahend += a_i[j] * multiplicator
            multiplicator *= table[i][0] - table[j][0]

        a_i.append((table[i][1] - subtrahend) / multiplicator)

    polinom = 0
    multiplicator = 1
    for i in range(n + 1):
        polinom += a_i[i] * multiplicator
        multiplicator *= x - table[i][0]

    return polinom


def p_n_x_minus_f_value(x, f, n, table):
    return newton_interpolation_method(x, n, table) - f


def equation_roots_segments_separating(a, b, divisions_count, f, n, table):
    segments = []
    h = (b - a) / divisions_count
    counter = 0
    x1 = a
    y1 = p_n_x_minus_f_value(x1, f, n, table)
    x2 = x1 + h

    while True:
        if x2 > b:
            break

        y2 = p_n_x_minus_f_value(x2, f, n, table)
        if y1 * y2 <= 0:
            counter += 1
            segments.append((x1, x2))
        x1 = x2
        x2 = x1 + h
        y1 = y2

    return segments, counter


def roots_finding_bisection_method(segment, epsilon, f, n, table):
    a_i, b_i = segment
    amount_of_steps = 0

    while True:
        c = (a_i + b_i) / 2
        if p_n_x_minus_f_value(a_i, f, n, table) * p_n_x_minus_f_value(c, f, n, table) <= 0:
            b_i = c
        else:
            a_i = c

        if (b_i - a_i) <= 2 * epsilon:
            break
        amount_of_steps += 1

    x = (a_i + b_i) / 2
    return x


def find_argument_for_f_x_value(a, b, divisions_count, f, n, table, epsilon):
    segments, segments_count = equation_roots_segments_separating(a, b, divisions_count, f, n,table)
    for segment in segments:
        x = roots_finding_bisection_method(segment, epsilon, f, n, table)
        print(f"X = {x}, |f(X) - F| = {abs(Function.f(x) - f)}")


def calculate(a, b, divisions_count, table):
    m_plus_one = len(table)
    f = float(input("Введите значение F, для которого хотите найти исходное значение X: "))
    n = m_plus_one
    while n >= m_plus_one:
        n = int(input(f"Введите степень n <= {m_plus_one - 1} интерполяционного полинома функции f(X): "))
        if n >= m_plus_one:
            print(f"Введено недопустимое значение n, введите n <= {m_plus_one - 1} !")
    epsilon = float(input("Введите значение epsilon, с точностью до которого хотите найти аргументы X: "))
    print(f"Найдены следующие значения X, для которых f(X) = {f}:")
    find_argument_for_f_x_value(a, b, divisions_count, f, n, table, epsilon)
    print()


print("ЗАДАЧА ОБРАТНОГО ИНТЕРПОЛИРОВАНИЯ")
print("Вариант №2")
print(Function.str())
print()

m_plus_one = int(input("Введите число значений в таблице (m + 1): "))
print("Введите концы отрезка [a, b], из которого выбираются узлы интерполяции: ")

while True:
    try:
        a = float(input("a = "))
        break
    except ValueError:
        print("Введите число a. Если это дробное число, разделитель - точка.")

while True:
    try:
        b = float(input("b = "))
        break
    except ValueError:
        print("Введите число b. Если это дробное число, разделитель - точка.")
print()

table = create_table_of_values(a, b, m_plus_one)
print("Таблица значений функции:")
for i in range(len(table)):
    x_i, f_x = table[i]
    print(f"x_{i} = {x_i}, f(x_{i}) = {f_x}")
print()

calculate(a, b, m_plus_one - 1, table)
while True:
    ans = input("Ввести новые значения? (y/n): ")
    if ans == "y":
        calculate(a, b, m_plus_one - 1, table)
    elif ans == "n":
        exit(0)
