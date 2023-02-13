# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с
# номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

number = (input("Введите номер билетика: "))
sum1 = 0
sum2 = 0
for i in number[:len(number) // 2]:
    sum1 += int(i)
for j in number[len(number) // 2:]:
    sum2 += int(j)
if sum1 == sum2:
    print("Поздравляю, Ваш билетик счастливый!")
else:
    print("Билет не счастливый, повезет в следующий раз")

# len-длина
