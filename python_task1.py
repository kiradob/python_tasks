# Задача №1.
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m 
# километров? При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2


n = int(input("Введите количество км, которое машина проходит за день: "))
m = int(input("Введите общий пробег: "))
print((m+n-1)//n)

#Вычетаем единицу чтобы корректно считалось количество дней
# // - целая часть от деления