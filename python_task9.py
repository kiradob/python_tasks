# Задача №9.
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех  чисел от
# 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

# print(list(range(3,10))[:5])
#   print(i)

# i=0
# while i<5:
#     i+=1
#     if i==5:
#         print(i)
#     else:
#         print(i,end=' ')

# Решение задачи
n = int(input('Введите число: '))
result = 1
i = 2
while i<=n:
    result*=i
    i+=1
print(result)
