# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


n = (int(input("Введите количество элементов 1 множества: ")))
array_1 = []
for i in range(n):
    A = int(input(f"Введите {i} элемент первого множества: "))
    array_1.append(A)


m = (int(input("Введите количество элементов 2 множества: ")))
array_2 = []
for j in range(m):
    A = int(input(f"Введите {i}элемент второго множества: "))
    array_2.append(A)
print(f"Множество 1: {array_1}")
print(f"Множество 2: {array_2}")


# set - преобразование списка в множество, в котором не может быть повторяющихся элементов
set_1 = set(array_1)
set_2 = set(array_2)
print(f"Элементы, встречающиеся в обоих множествах: {set.intersection(set_1, set_2)}")

