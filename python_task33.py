# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

n=int(input("Введите количество оценок Василия: "))
list_1=list()
for i in range(n):
    x=int(input(f"Напишите {i+1} оценкку Василия: "))
    list_1.append(x)
print(f"Исправленные оценки Василия: {list_1}")
# # То же самое можно написать в 1 строку
# list_1=[int(input()) for i in range(int(input()))]

max_n=max(list_1)
min_n=min(list_1)

for i in range(len(list_1)):
    if list_1[i]==max_n:
        list_1[i]=min_n
print(f"Настоящие оценки Василия: {list_1}")