n = 10000
epsilon = 10 ** -12


def find_roots_of_equation(func, a, b) -> list:
    segments = separation_of_roots(func, a, b)
    roots = []
    for segment in segments:
        roots.append(secants_method(func, segment))

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


def secants_method(func, segment):
    x_k_prev, x_k = segment
    x_k_next = x_k - func(x_k) * (x_k - x_k_prev) / (func(x_k) - func(x_k_prev))

    steps = 1
    while abs(x_k_next - x_k) > epsilon:
        x_k_prev = x_k
        x_k = x_k_next

        x_k_next = x_k - func(x_k) * (x_k - x_k_prev) / (func(x_k) - func(x_k_prev))
        steps += 1
    return x_k_next
