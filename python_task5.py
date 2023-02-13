# Задача №5.
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» 
# поезда, а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. Он хочет определить, сколько всего 
# вагонов в электричке. Напишите программу, которая будет это делать или сообщать, что без дополнительной информации 
# это сделать невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# Без доп. информации это сделать невозможно когда числа i=j равны.

i=int(input("Введите порядковый номер вагона с головы поезда, в который сел Витя: "))
j=int(input("Введите номер вагона, который написан: "))

# if (i==j and (i+j-1)%2==1 and (i+j-1)//2+1==i) or i!=j:
if i!=j:
    print("В электричке", (i+j-1), "вагонов")
else:
    print("нет")