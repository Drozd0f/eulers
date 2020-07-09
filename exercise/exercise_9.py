# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a^2 + b^2 = c^2
# Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.


def exercise_9(limit):
    from math import sqrt
    a = 1
    b = 2
    while True:
        while a < b:
            c = sqrt(a ** 2 + b ** 2)
            if int(a + b + c) == a + b + c and a + b + c == limit:
                print(a, "+", b, "+", c)
                multiple = a * b * c
                print("Их произведение равно:")
                break
            else:
                a += 1
        a = 1
        b += 1
        if b >= limit // 2:
            break
    return multiple


print(exercise_9(1000))
