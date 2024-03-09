import scipy
from prettytable import PrettyTable
from logic import get_roots_of_legendre_polynom, get_coefficients, integrate
from Functions import Function, Polynom


def test():
    a, b = -1, 1
    for n in range(1, 9):
        print(f"N = {n}")

        roots = get_roots_of_legendre_polynom(n)
        coefficients = get_coefficients(roots, n)

        table_print = PrettyTable()
        table_print.field_names = ["Узел", "Коэффициент"]
        for i in range(len(roots)):
            table_print.add_row([roots[i], coefficients[i]])
        print(table_print)

        d = 2 * n - 1
        print(f"Проверки на многочлене степени {d}:")
        exact_value = scipy.integrate.quad(lambda x: Polynom.f([1] * d, x), a, b)[0]
        print(f"Точное значение, найденное с помощью мат-пакета: {exact_value}")
        value_by_qf = integrate(coefficients, lambda x: Polynom.f([1] * d, x), roots, a, b)
        print(f"Приближенное значение, найденное с помощью КФ Гаусса: {value_by_qf}")
        print(f"Абсолютная погрешность: {abs(exact_value - value_by_qf)}\n\n")


def execute_program_loop():
    print(f"b\n∫ {Function.str()} dx\na\n")

    print("Введите пределы интегрирования [a, b]:")
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

    ns = []
    for i in range(3):
        print(f"Введите число узлов N{i + 1} для КФ Гаусса:")
        while True:
            try:
                n = int(input(f"N{i + 1} = "))
                if n < 1:
                    raise ValueError
                ns.append(n)
                break
            except ValueError:
                print("Введите натуральное число N")
    print()

    exact_value = scipy.integrate.quad(Function.f, a, b)[0]
    print(f"Точное значение интеграла, найденное с помощью мат-пакета: {exact_value}\n")
    for i in range(3):
        print(f"Для N{i + 1} = {ns[i]}:")
        roots = get_roots_of_legendre_polynom(ns[i])
        coefficients = get_coefficients(roots, ns[i])

        table_print = PrettyTable()
        table_print.field_names = ["Узел", "Коэффициент"]
        for j in range(len(roots)):
            table_print.add_row([roots[j], coefficients[j]])
        print(table_print)

        value_of_qf = integrate(coefficients, Function.f, roots, a, b)
        print(f"Приближенное значение, найденное с помощью КФ Гаусса: {value_of_qf}")
        print(f"Погрешность: {abs(exact_value - value_of_qf)}\n")


print("КФ ГАУССА, ЕЁ УЗЛЫ И КОЭФФИЦИЕНТЫ; ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ ПРИ ПОМОЩИ КФ ГАУССА\n")
test()
execute_program_loop()
while True:
    ans = input("\nВвести новые значения? (y/n): ")
    if ans == "y":
        execute_program_loop()
    elif ans == "n":
        exit(0)
