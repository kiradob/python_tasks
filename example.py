# dict_1 = {"first": 1, "second": 2, "third": 3, }
# for keys, value in dict_1.items():
#     print(keys, value)
#     print(dict_1.items())

# # .add - добавление элементов во множествах
# # .append - добавление элементов в списках
# # добавление элементов в кортежах: кортеж не меняется, элемент добавить не можем


# # Добавление элементов в словарь
# dict_1 = {"first": 1, "second": 2, "third": 3, }
# print(dict_1)
# dict_1["four"]=4
# print(dict_1)
# # Если хотим дабавить в словарь несколько элементов: .update
# dict_1 = {"first": 1, "second": 2, "third": 3, }
# print(dict_1)
# dict_1.update({"four":4,"five":5})
# print(dict_1)

# dict_1 = {"first": 1, "second": 2, "third": 3, }
# print(dict_1("four"))
# print(dict_1.get("four",0))
# print(dict_1.get("second",0))
# get - можно значение по умолчанию выбрать

# # Удаление элемента из списка .pop
# dict_1 = {"first": 1, "second": 2, "third": 3, }
# print(dict_1)
# dict_1.pop("second")
# print(dict_1)

# # Функции для получения всех ключей и всех значений
# dict_1 = {"first": 1, "second": 2, "third": 3, }
# print()
# print()
# print(dict_1.keys())
# print(dict_1.values())
# print()
# print()

# Вложенный словарь
dict_2={"Tom":{"English":5,"Math":5},"Red":{"English":4,"Math":3},"Jack":{"English":5,"Math":4}}
print()
for i in dict_2["Tom"].items():
# print(dict_2["Tom"])
    print(*i)
print() 
print(dict_2["Red"]["Math"])
print()
dict_2.update({"Wer":{"English":3,"Math":3}})
print(dict_2)
print()
dict_2["Tom"].update({"Trud":6})
print()
print(dict_2)
print()