from task4_functions import (AbstractFunction, Function, ConstFunction, FirstDegreePolynomialFunction,
                             ThirdDegreePolynomialFunction)
from prettytable import PrettyTable


def left_rectangle(function: AbstractFunction, a, b, m):
    h = (b - a) / m
    sum = 0
    for i in range(m):
        sum += function.f(a + i * h)
    return h * sum


def right_rectangle(function: AbstractFunction, a, b, m):
    h = (b - a) / m
    sum = 0
    for i in range(m):
        sum += function.f(a + (i + 1) * h)
    return h * sum


def middle_rectangle(function: AbstractFunction, a, b, m):
    h = (b - a) / m
    sum = 0
    for i in range(m):
        sum += function.f(a + (i + 0.5) * h)
    return h * sum


def trapezoid(function: AbstractFunction, a, b, m):
    h = (b - a) / m
    sum = function.f(a) + function.f(b)
    for i in range(1, m):
        sum += 2 * function.f(a + i * h)
    return h * sum / 2


def simpson(function: AbstractFunction, a, b, m):
    h = (b - a) / m
    sum = function.f(a) + 4 * function.f(a + 0.5 * h) + function.f(b)
    for i in range(1, m):
        sum += 2 * function.f(a + i * h) + 4 * function.f(a + (i + 0.5) * h)
    return h * sum / 6


def three_eighths(function: AbstractFunction, a, b):
    h = (b - a) / 3
    sum = function.f(a) + 3 * function.f(a + h) + 3 * function.f(a + 2 * h) + function.f(b)
    return (3 / 8) * h * sum


def calculate_and_print_table_for_function(function: AbstractFunction, a, b, m):
    exact_value_of_integral = function.f_definite_integral(a, b)

    table = PrettyTable()
    table.field_names = ["", "КФ левого прямоугольника", "КФ правого прямоугольника", "КФ среднего прямоугольника",
                         "КФ трапеции", "КФ Симпсона", "КФ 3/8"]

    values = {
        "left_rectangle": left_rectangle(function, a, b, m),
        "right_rectangle": right_rectangle(function, a, b, m),
        "middle_rectangle": middle_rectangle(function, a, b, m),
        "trapezoid": trapezoid(function, a, b, m),
        "simpson": simpson(function, a, b, m),
        "three_eights": three_eighths(function, a, b),
    }

    errors = {
        "left_rectangle": abs(exact_value_of_integral - values["left_rectangle"]),
        "right_rectangle": abs(exact_value_of_integral - values["right_rectangle"]),
        "middle_rectangle": abs(exact_value_of_integral - values["middle_rectangle"]),
        "trapezoid": abs(exact_value_of_integral - values["trapezoid"]),
        "simpson": abs(exact_value_of_integral - values["simpson"]),
        "three_eights": abs(exact_value_of_integral - values["three_eights"])
    }

    table.add_row(["Значение", values["left_rectangle"], values["right_rectangle"], values["middle_rectangle"],
                   values["trapezoid"], values["simpson"], values["three_eights"]])
    table.add_row(["Погрешность", errors["left_rectangle"], errors["right_rectangle"], errors["middle_rectangle"],
                   errors["trapezoid"], errors["simpson"], errors["three_eights"]])
    table.add_row(["АСТ", "0", "0", "1", "1", "3", "3"])

    print(table)


def execute_program_loop(func: AbstractFunction):
    print()
    print(func.str())
    print(func.str_integral())

    print("\nВведите пределы интегрирования [a, b]:")
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

    exact_value_of_integral = func.f_definite_integral(a, b)
    print(f"\n{b}\n∫ f(x) dx = {exact_value_of_integral} \n{a}\n")

    print(f"На сколько частей разбить отрезок [{a}, {b}]: ", end="")
    while True:
        try:
            m = int(input())
            if m <= 0:
                print("Количество отрезков должно быть больше 0")
            else:
                break
        except ValueError:
            print("Введите количество отрезков (целое число): ", end="")

    print(f"\nПриближенные значения интеграла функции {function.str()}, вычисленные по квадратурным формулам: ")
    calculate_and_print_table_for_function(function, a, b, m)

    print("\n\nТестирование квадратурных формул на многочленах степеней, соответствующих их АСТ:")

    const_function = ConstFunction()
    print(f"\nПриближенные значения интеграла функции {const_function.str()}, вычисленные по квадратурным формулам: ")
    calculate_and_print_table_for_function(const_function, a, b, m)

    first_degree_polynomial_function = FirstDegreePolynomialFunction()
    print(f"\nПриближенные значения интеграла функции {first_degree_polynomial_function.str()}, вычисленные по "
          f"квадратурным формулам: ")
    calculate_and_print_table_for_function(first_degree_polynomial_function, a, b, m)

    third_degree_polynomial_function = ThirdDegreePolynomialFunction()
    print(f"\nПриближенные значения интеграла функции {third_degree_polynomial_function.str()}, вычисленные по "
          f"квадратурным формулам: ")
    calculate_and_print_table_for_function(third_degree_polynomial_function, a, b, m)


print("ПРИБЛИЖЁННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПО КВАДРАТУРНЫМ ФОРМУЛАМ")
function = Function()
execute_program_loop(function)
while True:
    ans = input("\nВвести новые значения? (y/n): ")
    if ans == "y":
        execute_program_loop(function)
    elif ans == "n":
        exit(0)
