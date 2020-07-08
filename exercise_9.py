# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a^2 + b^2 = c^2
# Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.
summa = 0
b = 2
d = []
while True:
    for a in range(1, b):
        c = (a ** 2 + b ** 2) ** (1 / 2)
        if c == int(c):
            # d.append(a)
            # d.append(b)
            # d.append(c)
            summa = a + b + c
            d.append(summa)
            if summa == 1000:
                print(a, "+", b, "+", c)
                print(a * b * c)
                break
    if c >= 500:
        break
    b += 1
print(d)
