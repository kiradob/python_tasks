# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых
# чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6-> 5

array = []
m = 100
for i in range(int(input("Введите количество элементов в массиве N = "))):
    array.append(int(input("Введите элемент массива: ")))
x = int(input("Введите число X: "))
for i in range(len(array)):
    w = abs(x - array[i])
# Функция abs() используется для возврата абсолютного значения числа.
    if w < m:
        m = w
        closest = array[i]
print(f'Ближайший элемент массива {array} к заданному числу {x} равен {closest}.')