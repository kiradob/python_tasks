# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# 10 -> 1 2 4 8


N = int(input("Введите число, выше которого не выполнять оперрации: "))
x = 2
result = 0
for i in range(N +1):
    result = x ** i
    if result >= N:
        break
    print(result)