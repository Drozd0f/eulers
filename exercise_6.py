# Сумма квадратов первых десяти натуральных чисел равна
# 1^2 + 2^2 + ... + 10^2 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет
# 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.


def add(n, k):
    a = []
    # b = []
    i = 0
    j = 1

    for i in range(1, k + 1):
        a.append(i ** n)

    while j <= k:
        suma = (i + j) ** n
        i = i + j
        j += 1

    while True:
        if suma > sum(a):
            c = suma - sum(a)
            break
        else:
            c = sum(a) - suma
            break
    print(c)


n = int(input())
k = int(input())

add(n, k)
