# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
# Какое число является 10001-ым простым числом?


def exersice_7(d):
    dead_inside = 2

    while True:
        d = 6
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

        if d == len(a):
            print("Простые числа", a)
            break

        else:
            dead_inside += 1
# "Простое число под номером", d, "это", a[d - 1]
    return a[d - 1]


print(exersice_7(6))
