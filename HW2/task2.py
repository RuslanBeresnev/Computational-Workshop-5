from math import log
import random


class Function:
    @staticmethod
    def f(x):
        return log(1 + x)

    @staticmethod
    def str():
        return "f(x) = ln(1 + x)"


def create_table_of_values(a, b, m_plus_one):
    table = set()
    while len(table) < m_plus_one:
        x_i = random.uniform(a, b)
        table.add(x_i)

    table = sorted(table)
    result_table = []

    for x_i in table:
        f_x_i = Function.f(x_i)
        result_table.append((x_i, f_x_i))

    return result_table


def lagrange(x, n, table):
    def get_numerator(k):
        result = 1
        for i in range(n + 1):
            if i != k:
                result *= x - table[i][0]
        return result

    def get_denominator(k):
        x_k = table[k][0]
        result = 1
        for i in range(n + 1):
            if i != k:
                result *= x_k - table[i][0]
        return result

    polinom = 0
    for k in range(n + 1):
        polinom += (get_numerator(k) / get_denominator(k)) * table[k][1]

    return polinom


def newton(x, n, table):
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


def calculate(table):
    m_plus_one = len(table)
    x = float(
        input("Введите точку интерполирования x, значение в которой хотите найти: ")
    )
    n = m_plus_one
    while n >= m_plus_one:
        n = int(
            input(
                "Введите степень степень интерполяционного многочлена, "
                "который будет построен для того, чтобы найти значение в точке x: "
            )
        )
        if n >= m_plus_one:
            print(f"Введено недопустимое значение n, введите n <= {m_plus_one - 1} !")
    print()

    table = sorted(table, key=lambda tuple_of_x_and_f_x: abs(tuple_of_x_and_f_x[0] - x))
    print("Отсортированная таблица значений функции:")
    for i in range(len(table)):
        x_i, f_x = table[i]
        print(f"x_{i} = {x_i}, |x - x_{i}| = {abs(x - x_i)}, f(x_{i}) = {f_x}")
    print()

    lagrange_result = lagrange(x, n, table)
    lagrange_inaccuracy = abs(Function.f(x) - lagrange_result)
    print(
        f"Значение интерполяционного многочлена, "
        f"найденное при помощи представления "
        f"в форме Лагранжа: {lagrange_result}"
    )
    print(
        f"Значение абсолютной фактической погрешности "
        f"для формы Лагранжа: {lagrange_inaccuracy}"
    )
    print()

    newton_result = newton(x, n, table)
    newton_inaccuracy = abs(Function.f(x) - newton_result)
    print(
        f"Значение интерполяционного многочлена, "
        f"найденное при помощи представления "
        f"в форме Ньютона: {newton_result}"
    )
    print(
        f"Значение абсолютной фактической погрешности "
        f"для формы Ньютона: {newton_inaccuracy}"
    )
    print()


print("ЗАДАЧА АЛГЕБРАИЧЕСКОГО ИНТЕРПОЛИРОВАНИЯ")
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

calculate(table)
while True:
    ans = input("Ввести новые значения? (y/n): ")
    if ans == "y":
        calculate(table)
    elif ans == "n":
        exit(0)
