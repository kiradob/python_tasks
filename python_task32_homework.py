# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


from random import randint

def between_min_max(preset_min, preset_max, array):
    return [i for i in range(len(array)) if preset_min < array[i] < preset_max]

lst = [randint(-20, 20) for i in range(10)]
preset_min = int(input('Задайте значение минимума '))
preset_max = int(input('Задайте значение максимума '))
print('Проверяемый массив', lst)

print('Индексы элементов массива, значения которых в заданном диапазоне', between_min_max(preset_min, preset_max, lst))
