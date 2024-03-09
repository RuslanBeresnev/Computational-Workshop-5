import numpy as np
import scipy.integrate as integrate
from Functions import Polynom
from equations_solving import find_roots_of_equation
from prettytable import PrettyTable


def __get_moment(k, a, b, weight) -> float:
    return integrate.quad(lambda x: weight(x) * (x ** k), a, b)[0]


def get_moments(n, a, b, weight) -> list:
    return [__get_moment(k, a, b, weight) for k in range(n)]


def get_nodes(n, a, b) -> list:
    nodes = []
    h = (b - a) / n
    # x_1 = a
    # x_n = b - h
    for k in range(n):
        nodes.append(a + h * k)
    return nodes


def find_coefficients_for_quad_formula(nodes, moments) -> list:
    n = len(nodes)
    matrix = np.array([[round(nodes[i] ** power, 20) for i in range(n)] for power in range(n)])
    right_part = np.array(moments)
    result = np.linalg.solve(matrix, right_part)
    return result.tolist()


def quad_formula(coefficients, nodes, func) -> float:
    n = len(nodes)
    result = 0
    for k in range(n):
        result += coefficients[k] * func(nodes[k])
    return result

# Дальнейшие функции используются для вычисления КФ НАСТ

def find_coefficients_for_omega(n, moments):
    matrix = np.array([[moments[j] for j in range(i, i + n)] for i in range(n)])
    right_part = np.array([-moments[i] for i in range(n, 2 * n)])
    return np.linalg.solve(matrix, right_part).tolist()


def find_nodes_for_max_accuracy(coefficients_for_omega, a, b):
    # Находит комплексные узлы
    # return np.roots(coefficients_for_omega + [1])
    nodes = find_roots_of_equation(lambda x: Polynom.f(coefficients_for_omega + [1], x), a, b)
    return nodes


def print_table(moments, nodes, coefficients):
    n = len(nodes)

    table_print = PrettyTable()
    table_print.field_names = ["Индексы"] + [k for k in range(1, n + 1)]
    table_print.add_row(["Узлы x_k"] + nodes)
    table_print.add_row(["Моменты μ_k"] + moments)
    table_print.add_row(["Коэффициенты A_k"] + coefficients)
    print(table_print)


# def print_orthogonal_polynom_value(coefficients_for_omega):
#     result = ''
#     for k in range(len(coefficients_for_omega)):
#         result += f'{coefficients_for_omega[k]} *'
#         pass


def print_formula_value_and_error(exact_value, coefficients, nodes, func):
    value_of_quad_formula = quad_formula(coefficients, nodes, func)
    print(f'\nПриближенное значение интеграла, вычисленное с помощью ИКФ: {value_of_quad_formula}')
    print('Погрешность по сравнению с вычисленным значением из библиотеки: '
          f'{abs(exact_value - value_of_quad_formula)}')
