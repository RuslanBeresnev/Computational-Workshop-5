from equations_solving import find_roots_of_equation


def p_n(n, x):
    if n == 0:
        return 1
    if n == 1:
        return x
    return ((2 * n - 1) / n) * x * p_n(n - 1, x) - ((n - 1) / n) * p_n(n - 2, x)


def get_roots_of_legendre_polynom(n):
    roots = find_roots_of_equation(lambda x: p_n(n, x), -1, 1)
    return roots


def get_coefficients(nodes: list, n) -> list:
    coefficients = []
    for i in range(n):
        coefficients.append(2 * (1 - nodes[i] ** 2) / (n * (p_n(n - 1, nodes[i]))) ** 2)
    return coefficients


def integrate(coefficients, func, nodes, a, b):
    result = 0
    for i in range(len(nodes)):
        x = (b - a) / 2 * nodes[i] + (b + a) / 2
        result += coefficients[i] * func(x)
    return result * (b - a) / 2
