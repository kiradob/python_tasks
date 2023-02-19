# Задача №19.
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_1 = [5, 4, 6, 7, 8, -10]
k = int(input())
k = k % len(list_1)
list_result = list()

for i in range(k):
    list_result.append(list_1[len(list_1)-1-i])

for i in range(len(list_1)-k):
    list_result.append(list_1[i])
print(list_result)
