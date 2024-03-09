import scipy.integrate as integrate
from Functions import Function, Weight
from Logic import (get_moments, get_nodes, find_coefficients_for_quad_formula, quad_formula,
                   find_coefficients_for_omega, find_nodes_for_max_accuracy, print_table, print_formula_value_and_error)


def execute_program_loop():
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

    print('Введите число узлов для построения ИКФ:')
    while True:
        try:
            n = int(input("N = "))
            if n < 2:
                raise ValueError
            break
        except ValueError:
            print("Введите натуральное число N, оно должно быть >= 2")

    exact_value = integrate.quad(lambda x: Weight.w(x) * Function.f(x), a, b)
    print('Точное значение интеграла, вычисленное с помощью библиотеки scipy:')
    print(f"\n{b}\n∫ {Weight.str()} * {Function.str()} dx = {exact_value[0]}; error = {exact_value[1]}\n{a}\n")

    print("---------------------------------------------Вычисление с помощью ИКФ---------------------------------------------")
    moments = get_moments(n, a, b, Weight.w)
    nodes = get_nodes(n, a, b)
    coefficients = find_coefficients_for_quad_formula(nodes, moments)
    print_table(moments, nodes, coefficients)
    print_formula_value_and_error(exact_value[0], coefficients, nodes, Function.f)

    print('\nПроверка точности ИКФ на многочлене степени N - 1:')
    exact_value_of_polynom = integrate.quad(lambda x: Weight.w(x) * (x ** (n - 1)), a, b)
    moments_for_polynom = get_moments(n, a, b, Weight.w)
    nodes_for_polynom = get_nodes(n, a, b)
    coefficients_for_polynom = find_coefficients_for_quad_formula(nodes_for_polynom, moments_for_polynom)
    value_of_quad_formula_for_polynom = quad_formula(coefficients_for_polynom, nodes_for_polynom,
                                                     lambda x: (x ** (n - 1)))
    print(f'Погрешность: {abs(exact_value_of_polynom[0] - value_of_quad_formula_for_polynom)}')
    print()

    print("------------------------------------------Вычисление с помощью КФ НАСТ------------------------------------------")
    moments_for_max_accuracy = get_moments(2 * n, a, b, Weight.w)
    print("Моменты весовой функции:")
    for i in range(2 * n):
        print(f"μ{i} = {moments_for_max_accuracy[i]}")
    print()

    coefficients_for_omega = find_coefficients_for_omega(n, moments_for_max_accuracy)
    print("Коэффициенты для ортогонального многочлена омега_n:")
    for i in range(n):
        print(f"a{i} = {coefficients_for_omega[i]}")
    print(f"a{n} = 1\n")

    nodes_for_max_accuracy = find_nodes_for_max_accuracy(coefficients_for_omega, a, b)
    print("Узлы интерполяции для КФ НАСТ:")
    for i in range(n):
        print(f"x{i} = {nodes_for_max_accuracy[i]}")
    print()

    coefficients_for_max_accuracy = find_coefficients_for_quad_formula(nodes_for_max_accuracy,
                                                                       moments_for_max_accuracy[:n])
    print("Коэффициенты для квадратурной формулы:")
    for i in range(n):
        print(f"A{i} = {coefficients_for_max_accuracy[i]}")

    value_for_max_accuracy = quad_formula(coefficients_for_max_accuracy, nodes_for_max_accuracy, Function.f)
    print(f'\nПриближенное значение интеграла, вычисленное с помощью КФ НАСТ: {value_for_max_accuracy}')
    print('Погрешность по сравнению с вычисленным значением из библиотеки: '
          f'{abs(exact_value[0] - value_for_max_accuracy)}')

    print('\nПроверка точности КФ НАСТ на одночлене x^3:')
    moments_for_max_accuracy = get_moments(2 * n, a, b, Weight.w)
    coefficients_for_omega = find_coefficients_for_omega(n, moments_for_max_accuracy)
    nodes_for_max_accuracy = find_nodes_for_max_accuracy(coefficients_for_omega, a, b)
    coefficients_for_max_accuracy = find_coefficients_for_quad_formula(nodes_for_max_accuracy,
                                                                   moments_for_max_accuracy[:n])
    value_for_max_accuracy = quad_formula(coefficients_for_max_accuracy, nodes_for_max_accuracy, lambda x: x**3)
    exact_value = integrate.quad(lambda x: Weight.w(x) * (x ** 3), a, b)
    print(f'Погрешность: {abs(exact_value[0] - value_for_max_accuracy)}')

    print('\nПроверка точности КФ НАСТ на одночлене x^(2N - 1):')
    moments_for_max_accuracy = get_moments(2 * n, a, b, Weight.w)
    coefficients_for_omega = find_coefficients_for_omega(n, moments_for_max_accuracy)
    nodes_for_max_accuracy = find_nodes_for_max_accuracy(coefficients_for_omega, a, b)
    coefficients_for_max_accuracy = find_coefficients_for_quad_formula(nodes_for_max_accuracy,
                                                                       moments_for_max_accuracy[:n])
    value_for_max_accuracy = quad_formula(coefficients_for_max_accuracy, nodes_for_max_accuracy, lambda x: x ** (2 * n - 1))
    exact_value = integrate.quad(lambda x: Weight.w(x) * (x ** (2 * n - 1)), a, b)
    print(f'Погрешность: {abs(exact_value[0] - value_for_max_accuracy)}')


print("ПРИБЛИЖЁННОЕ ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ ПРИ ПОМОЩИ КФ НАСТ")
execute_program_loop()
while True:
    ans = input("\nВвести новые значения? (y/n): ")
    if ans == "y":
        execute_program_loop()
    elif ans == "n":
        exit(0)
