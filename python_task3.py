# Задача №3.
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input("Введите количество количество учеников в 1-ом классе: "))
b = int(input("Введите количество количество учеников во 2-ом классе: "))
c = int(input("Введите количество количество учеников в 3-м классе: "))
a1=(a+1)//2
b1=(b+1)//2
c1=(c+1)//2
print(a1+b1+c1)

#Вычетаем единицу чтобы корректно считалось количество дней
# // - целая часть от деления