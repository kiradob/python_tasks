# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в
# первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны
# N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3-> 1

array = []
for i in range(int(input('Введите количество элементов в массиве N = '))):
    array.append(int(input('Введите элемент массива ')))
x = int(input('Введите число X = '))
n = array.count(x)
print(f'Число X встречается в массиве {array} {n} раз.')
