n = 10000
epsilon = 10 ** -15


def find_roots_of_equation(func, a, b):
    segments = separation_of_roots(func, a, b)

    roots = []
    for segment in segments:
        roots.append(bisection_method(func, segment))

    return roots


def separation_of_roots(func, a, b) -> list:
    segments = []

    h = (b - a) / n
    counter = 0
    x1 = a
    y1 = func(x1)
    x2 = x1 + h

    while True:
        if x2 > b:
            break

        y2 = func(x2)
        if y1 * y2 <= 0:
            counter += 1
            segments.append((x1, x2))
        x1 = x2
        x2 = x1 + h
        y1 = y2

    return segments


def bisection_method(func, segment):
    a_i, b_i = segment
    amount_of_steps = 0
    while True:
        c = (a_i + b_i) / 2
        if func(a_i) * func(c) <= 0:
            b_i = c
        else:
            a_i = c

        if (b_i - a_i) <= 2 * epsilon:
            break
        amount_of_steps += 1

    x = (a_i + b_i) / 2
    return x
