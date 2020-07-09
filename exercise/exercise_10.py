# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

# Найдите сумму всех простых чисел меньше двух ста.


def exercise_10(dead_inside):

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

    print("Простые числа", a)
    return sum(a)


print(exercise_10(200))
