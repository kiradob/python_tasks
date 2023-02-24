# Задача №27. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов 
# идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13
# Функция split создает список, в котором каждое слово записано отдельным элементом
# set - преобразование списка в множество, в котором не может быть повторяющихся элементов
print(len(set(input().lower().split())))

# # Вариант 2
# text = input().split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))