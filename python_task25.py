# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Для решения данной задачи используйте функцию .split()
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# list_1 = ["H", "e", "l", "l", "o",]
# print(''.join(list_1))

# stroka = 'Hello world Moscow Name'
# print(stroka.split(" "))

text = input().split()
text1 = {}
for i in text:
    if i in text1:
        print(f"{i}_{text1[i]+1}", end=" ")
        text1[i] += 1
    else:
        print(i, end=" ")
        text1[i] = 0
