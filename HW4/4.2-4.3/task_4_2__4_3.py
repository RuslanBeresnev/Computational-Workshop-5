from task4_functions import (
    AbstractFunction,
    MyFunction,
    ConstFunction,
    FirstDegreePolynomialFunction,
    ThirdDegreePolynomialFunction,
)
from task4_2_solving_equations import find_roots_of_equation
from prettytable import PrettyTable


def calculate_results_of_quadrature_forms(func: AbstractFunction, a, b, count) -> dict:
    h = (b - a) / count

    sum_in_nodes = 0  # от 0 до (m - 1)
    for i in range(count):
        sum_in_nodes += func.f(a + i * h)

    sum_between_nodes = 0  # от 0 до (m - 1)
    for i in range(count):
        sum_between_nodes += func.f(a + (i + 0.5) * h)

    f_a = func.f(a)
    f_b = func.f(b)
    sum_in_end_nodes = f_a + f_b

    result = {
        "left_rectangle": h * sum_in_nodes,
        "right_rectangle": h * (sum_in_nodes - f_a + f_b),
        "middle_rectangle": h * sum_between_nodes,
        "trapezoid": h / 2 * (sum_in_end_nodes + 2 * (sum_in_nodes - f_a)),
        "simpson": h / 6 * (sum_in_end_nodes + 2 * (sum_in_nodes - f_a) + 4 * sum_between_nodes)
    }

    return result


def refine_results_of_quadrature_forms(func: AbstractFunction, a, b, count) -> dict:
    J_h = calculate_results_of_quadrature_forms(func, a, b, count)
    J_half_h = calculate_results_of_quadrature_forms(func, a, b, count * 2)
    r = {
        "left_rectangle": 1,
        "right_rectangle": 1,
        "middle_rectangle": 2,
        "trapezoid": 2,
        "simpson": 4
    }

    refined_result = {
        "left_rectangle": (2 ** r["left_rectangle"] * J_half_h["left_rectangle"] - J_h["left_rectangle"]) /
                          (2 ** r["left_rectangle"] - 1),
        "right_rectangle": (2 ** r["right_rectangle"] * J_half_h["right_rectangle"] - J_h["right_rectangle"]) /
                           (2 ** r["right_rectangle"] - 1),
        "middle_rectangle": (2 ** r["middle_rectangle"] * J_half_h["middle_rectangle"] - J_h["middle_rectangle"]) /
                            (2 ** r["middle_rectangle"] - 1),
        "trapezoid": (2 ** r["trapezoid"] * J_half_h["trapezoid"] - J_h["trapezoid"]) / (2 ** r["trapezoid"] - 1),
        "simpson": (2 ** r["simpson"] * J_half_h["simpson"] - J_h["simpson"]) / (2 ** r["simpson"] - 1)
    }

    return refined_result


def find_maximum_value(func, func_diff, a, b):
    # Нахождение максимума среди концов отрезка
    max_f = abs(func(a))
    f_b = abs(func(b))
    if f_b > max_f:
        max_f = f_b

    # Нахождение максимума на отрезке
    roots_f_diff = find_roots_of_equation(func_diff, a, b)
    for root in roots_f_diff:
        f = abs(func(root))
        if f > max_f:
            max_f = f

    return max_f


def calculate_errors_and_print_table_for_function(func: AbstractFunction, a, b, count):
    exact_value_of_integral = func.f_definite_integral(a, b)

    values = calculate_results_of_quadrature_forms(func, a, b, count)
    refined_values = refine_results_of_quadrature_forms(func, a, b, count)

    errors = {
        "left_rectangle": abs(exact_value_of_integral - values["left_rectangle"]),
        "right_rectangle": abs(exact_value_of_integral - values["right_rectangle"]),
        "middle_rectangle": abs(exact_value_of_integral - values["middle_rectangle"]),
        "trapezoid": abs(exact_value_of_integral - values["trapezoid"]),
        "simpson": abs(exact_value_of_integral - values["simpson"]),
    }

    h = (b - a) / count

    max_f_diff = find_maximum_value(func.f_diff, func.f_2diff, a, b)
    max_f_2diff = find_maximum_value(func.f_2diff, func.f_3diff, a, b)
    max_f_4diff = find_maximum_value(func.f_4diff, func.f_5diff, a, b)

    theoretical_errors = {
        "left_rectangle": 1 / 2 * (b - a) * (h ** 1) * max_f_diff,
        "right_rectangle": 1 / 2 * (b - a) * (h ** 1) * max_f_diff,
        "middle_rectangle": 1 / 24 * (b - a) * (h ** 2) * max_f_2diff,
        "trapezoid": 1 / 12 * (b - a) * (h ** 2) * max_f_2diff,
        "simpson": 1 / 2880 * (b - a) * (h ** 4) * max_f_4diff,
    }

    errors_for_refined_values = {
        "left_rectangle": abs(exact_value_of_integral - refined_values["left_rectangle"]),
        "right_rectangle": abs(exact_value_of_integral - refined_values["right_rectangle"]),
        "middle_rectangle": abs(exact_value_of_integral - refined_values["middle_rectangle"]),
        "trapezoid": abs(exact_value_of_integral - refined_values["trapezoid"]),
        "simpson": abs(exact_value_of_integral - refined_values["simpson"]),
    }

    table = PrettyTable()
    table.field_names = [
        "",
        "КФ левого прямоугольника",
        "КФ правого прямоугольника",
        "КФ среднего прямоугольника",
        "КФ трапеции",
        "КФ Симпсона",
    ]
    table.add_row(
        [
            "Значение",
            values["left_rectangle"],
            values["right_rectangle"],
            values["middle_rectangle"],
            values["trapezoid"],
            values["simpson"],
        ]
    )
    table.add_row(
        [
            "Погрешность",
            errors["left_rectangle"],
            errors["right_rectangle"],
            errors["middle_rectangle"],
            errors["trapezoid"],
            errors["simpson"],
        ]
    )
    table.add_row(
        [
            "Теор. погрешность",
            theoretical_errors["left_rectangle"],
            theoretical_errors["right_rectangle"],
            theoretical_errors["middle_rectangle"],
            theoretical_errors["trapezoid"],
            theoretical_errors["simpson"],
        ]
    )
    table.add_row(["АСТ", "0", "0", "1", "1", "3"])
    table.add_row(["----------------------------------", "------------------------",
                   "------------------------", "------------------------",
                   "------------------------", "------------------------"])
    table.add_row(
        [
            "Уточн. значение",
            refined_values["left_rectangle"],
            refined_values["right_rectangle"],
            refined_values["middle_rectangle"],
            refined_values["trapezoid"],
            refined_values["simpson"],
        ]
    )
    table.add_row(
        [
            "Погрешность для уточн. значения",
            errors_for_refined_values["left_rectangle"],
            errors_for_refined_values["right_rectangle"],
            errors_for_refined_values["middle_rectangle"],
            errors_for_refined_values["trapezoid"],
            errors_for_refined_values["simpson"],
        ]
    )
    table.add_row(["АСТ уточн. значения", "1", "1", "3", "3", "5"])

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

    print(f"На сколько сегментов разбить отрезок [{a}, {b}]: ", end="")
    while True:
        try:
            m = int(input())
            if m <= 0:
                print(
                    "Количество сегментов должно быть больше 0, введите заново: ", end=""
                )
            else:
                break
        except ValueError:
            print("Введите количество сегментов (целое число): ", end="")

    print(f"На сколько частей разбить каждый сегмент? (Введите число l): ", end="")
    while True:
        try:
            l = int(input())
            if l <= 0:
                print(
                    "Количество частей должно быть больше 0, введите заново: ", end=""
                )
            else:
                break
        except ValueError:
            print("Введите количество частей для каждого сегмента (целое число): ", end="")

    print(f"Длина каждого сегмента: {(b - a) / m}")
    print(f"Длина каждой части в одном сегменте: {(b - a) / (m * l)}")

    exact_value_of_integral = func.f_definite_integral(a, b)
    print(f"\n{b}\n∫ f(x) dx = {exact_value_of_integral} \n{a}\n")

    print(
        f"\nПриближенные значения интеграла функции {function.str()}, вычисленные по квадратурным формулам "
        f"(для m сегментов): "
    )
    calculate_errors_and_print_table_for_function(function, a, b, m)

    print(
        f"\nПриближенные значения интеграла функции {function.str()}, вычисленные по квадратурным формулам "
        f"(для m * l частей): "
    )
    calculate_errors_and_print_table_for_function(function, a, b, m * l)

    print(
        "\n\nТестирование квадратурных формул на многочленах степеней, соответствующих их АСТ:"
    )

    const_function = ConstFunction()
    print(
        f"\nПриближенные значения интеграла функции {const_function.str()}, вычисленные по квадратурным формулам: "
    )
    calculate_errors_and_print_table_for_function(const_function, a, b, m * l)

    first_degree_polynomial_function = FirstDegreePolynomialFunction()
    print(
        f"\nПриближенные значения интеграла функции {first_degree_polynomial_function.str()}, вычисленные по "
        f"квадратурным формулам: "
    )
    calculate_errors_and_print_table_for_function(first_degree_polynomial_function, a, b, m * l)

    third_degree_polynomial_function = ThirdDegreePolynomialFunction()
    print(
        f"\nПриближенные значения интеграла функции {third_degree_polynomial_function.str()}, вычисленные по "
        f"квадратурным формулам: "
    )
    calculate_errors_and_print_table_for_function(third_degree_polynomial_function, a, b, m * l)


print("ПРИБЛИЖЁННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛА ПО СОСТАВНЫМ КВАДРАТУРНЫМ ФОРМУЛАМ")
function = MyFunction()
execute_program_loop(function)
while True:
    ans = input("\nВвести новые значения? (y/n): ")
    if ans == "y":
        execute_program_loop(function)
    elif ans == "n":
        exit(0)
