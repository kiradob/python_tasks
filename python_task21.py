# Задача №21.
# Напишите программу для печати всех уникальных значений в словаре. 
# Примечание: Список словарей задан изначально. Пользователь его не вводит
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
# {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# словари. Dictionary или dict() или {}. В словаре есть ключ [key]=value и значение
# dic.values - функция, которая сохраняет все значения, которые находятся в словаре (возвращает список всех значений)

# Вариант 2
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
list_2 = list()
for i in list_1:
    for j in i:
        list_2.append(i[j])

list_result = list()
for i in list_2:
    if i not in list_result:
        list_result.append(i)
print(list_result)

# Вариант 3
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# set_1 = set()
# for i in list_1:
#     for j in i:
#         set_1.add(i[j])
# print(set_1)