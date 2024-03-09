from math import exp


class Function:
    @staticmethod
    def f(x):
        return exp(1.5 * 3 * x)

    @staticmethod
    def f_diff(x):
        return 1.5 * 3 * exp(1.5 * 3 * x)

    @staticmethod
    def f_2diff(x):
        return 4.5 * 4.5 * exp(1.5 * 3 * x)

    @staticmethod
    def str():
        return "f(x) = e ^ (1.5 * 3 * x)"


def create_table_of_values(a, h, m_plus_one):
    table = []
    for i in range(m_plus_one):
        x_i = a + i * h
        f_x_i = Function.f(x_i)
        table.append((x_i, f_x_i))
    return table


def first_derivative(table, h, i):
    if i == 0:
        return (-3 * table[i][1] + 4 * table[i + 1][1] - table[i + 2][1]) / (2 * h)

    if i == len(table) - 1:
        return (3 * table[i][1] - 4 * table[i - 1][1] + table[i - 2][1]) / (2 * h)

    return (table[i + 1][1] - table[i - 1][1]) / (2 * h)


def second_derivative(table, h, i):
    if i == 0:
        return (table[i][1] - 2 * table[i + 1][1] + table[i + 2][1]) / (h * h)

    if i == len(table) - 1:
        return (table[i][1] - 2 * table[i - 1][1] + table[i - 2][1]) / (h * h)

    return (table[i + 1][1] - 2 * table[i][1] + table[i - 1][1]) / (h * h)


def calculate():
    m_plus_one = int(input("Введите число значений в таблице (m + 1): "))

    print("Введите начало отрезка a: ")
    while True:
        try:
            a = float(input("a = "))
            break
        except ValueError:
            print("Введите число a. Если это дробное число, разделитель - точка.")

    print("Введите значение шага h > 0: ")
    while True:
        try:
            h = float(input("h = "))
            if h > 0:
                break
            print("h должно быть > 0")
        except ValueError:
            print("Введите число h. Если это дробное число, разделитель - точка.")

    table = create_table_of_values(a, h, m_plus_one)
    print("\nТаблица значений функции:")
    for i in range(len(table)):
        x_i, f_x = table[i]
        print(f"x_{i} = {x_i}, f(x_{i}) = {f_x}")
    print()

    for i in range(len(table)):
        x_i, f_x_i = table[i]
        f_diff = first_derivative(table, h, i)
        f_2diff = second_derivative(table, h, i)

        print(
            f"x_{i} = {x_i}\t\t\tf(x_{i}) = {f_x_i}\t\t\tt"
            f"f'(x_{i})чд = {f_diff}\t\t\t |f'(x_{i}) - f'(x_{i})чд| = {abs(Function.f_diff(x_i) - f_diff)}\t\t\t"
            f"f''(x_{i})чд = {f_2diff}\t\t\t |f''(x_{i}) - f''(x_{i})чд| = {abs(Function.f_2diff(x_i) - f_2diff)}"
        )


print(
    "Нахождение производных таблично-заданной функции по формулам численного дифференцирования"
)
print("Вариант №2")
print(Function.str())
print()

calculate()
while True:
    ans = input("Ввести новые значения? (y/n): ")
    if ans == "y":
        calculate()
    elif ans == "n":
        exit(0)
