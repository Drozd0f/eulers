# Простые делители числа 13195 - это 5, 7, 13 и 29.

# Каков самый большой делитель числа 1000, являющийся простым числом?


def exercise_3(dead_inside):

    print("dead inside = ", dead_inside)

    a = []
    for i in range(2, dead_inside + 1):
        a.append(i)

    # print("Наши числа", a)

    b = []

    for n in range(2, dead_inside + 1):
        for k in range(n + 1, dead_inside + 1):
            if k % n == 0:
                b.append(k)

    # print("Сложеные числа для каждого числа а", b)

    c = list(set(b))

    # print("Фильтруем сложеные числа", c)

    for k in c:
        for i in a:
            if i == k:
                a.remove(k)

    # print("Простые числа", a)

    d = []

    for i in a:
        if dead_inside % i == 0:
            d.append(i)

    print("Простые делители", d)
    print("Максимальный натуральный делитель:")
    return max(d)


print(exercise_3(1000))
