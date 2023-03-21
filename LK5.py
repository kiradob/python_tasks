# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TLS3onfOr-Jo3yX1Pip9ZHgl6z0X0kXK
"""

import pandas as pd
# Чтобы подключить библиотеку к Вашей программе необходимо написать следующее:

df = pd.read_csv('sample_data/california_housing_train.csv',sep=',')
# Прочтем файл .csv(он находится в Google Colab в папке sample_data) с помощью библиотеки pandas

df.head(n=10)
# Для того чтобы прочитать первые n строк таблицы, необходимо воспользоваться следующей функцией:

df.tail(n=10)
# есть функция, которая показывает последние 10 строк таблицы.

df.shape
# Иногда заранее неизвестно сколько строк и столбцов находится внутри таблицы, чтобы это сделать необходимо воспользоваться специальной 
# функцией.

df.isnull()
# Чтобы обнаружить пустые значения в таблице данных необходимо воспользоваться функцией .isnull().

df.isnull().sum()
# Данная функция выведет количество null-значений в каждой ячейке по столбцам.

df.dtypes
# чтобы узнать тип данных нужно применить функцию .dtypes
# Делаем вывод: у всей таблицы данных один тип float(дробное число)

df.columns
# Чтобы узнать название всех столбцов в таблице, воспользуйтесь функцией .columns.

df

df['latitude']
# Если Вы хотите вывести 1 столбец на экран, то можно указать следующее
# выражение, которое позволит это сделать.

df[['latitude', 'population']]

# Задание: Необходимо вывести столбец total_rooms, у которого медианный возраст
# здания(housing_median_age) меньше 20
df[df['housing_median_age'] < 20]

df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]

print(df['population'].max())
# Максимальное значение:

print(df['population'].min())
# Минимальное значение:

print(df['population'].mean())
# Среднее значение:

print(df['population'].sum())
# Сумма:

df[['population', 'total_rooms']].median()
# Медианное значение:

df.describe()
# count - Общее кол-во не пустых строк
# mean - среднее значение в столбце
# std - стандартное отклонение от среднего значения
# min - минимальное значение
# max - максимальное значение
# Числа 25%, 50%, 75% - перцентили

import seaborn as sns
# Для того чтобы начать работу с библиотекой seaborn, ее необходимо импортировать к себе в программу:

sns.scatterplot(data=df, x="longitude", y="latitude")
# Чтобы изобразить отношения между двумя столбцами достаточно указать, какой столбец отобразить по оси x, а какой по оси y.

sns.scatterplot(data=df, x="households", y="population", hue="total_rooms")
# Помимо двумерных отношений, мы можем добавить "дополнительное измерение" с помощью цвета. В данном случае опять же достаточно очевидное 
# отношение, чем выше кол-во семей, тем выше кол-во людей и соответственно комнат
# hue="total_rooms" - говоим, что сделай расцветку по total_rooms

# мы можем использовать size дляизменения размера точек.
sns.scatterplot(data=df, x="households", y="population", hue="total_rooms", size=10)

cols = ['population', 'median_income', 'housing_median_age','median_house_value']
g = sns.PairGrid(df[cols])
g.map(sns.scatterplot)
# PairGrid принимает как аргумент pandas DataFrame и визуализирует все возможные отношения между ними, в соответствии с выбранным типом графика.

"""Линейные графики

Хорошо подойдут, если есть временная или какая-либо иная последовательность и значения, которые могут меняться в зависимости от нее. Для генерации линейных графиков в seaborn используется relplot функцию. Она также принимает DataFrame, x, y - столбцы
"""

sns.relplot(x="latitude", y="median_house_value", kind="line", data=df)
# Для визуализации выбирается тип line:
# Можно видеть, что в определенных местах долготы цена за дома резко подскакивает

"""Попробуем визуализировать longitude по отношения к median_house_value и поймем в чем же дело, почему цена так резко подскакивает.

"""

sns.relplot(x = 'longitude', y = 'median_house_value', kind = 'line', data = df)
# Можно видеть, что в определенных местах широты цена за дома также очень высока.

# Используя точечный график можно визуализировать эти отношения с большей четкостью. Скорее всего резкий рост цен связан с близостью к
# ценному объекту, повышающему качество жизни, скорее всего побережью океана или реки.
sns.scatterplot(data=df, x="latitude", y="longitude", hue="median_house_value")

"""Гистограмма

Способ представления табличных данных в графическом виде — в виде столбчатой
диаграммы. По оси x обычно указывают значение, а по оси y - встречаемость(кол-во таких значений в выборке)
"""

sns.histplot(data=df, x="median_income")
# Можно видеть что у большинства семей доход находится между значениями 2 и 6. И только очень небольшое количество людей обладают доходом > 10.

# Изобразим гистограмму по housing_median_age.
sns.histplot(data = df, x = 'housing_median_age')
# Распределение по возрасту более равномерное. Большую часть жителей составляют люди в возрасте от 20 до 40 лет. Но и молодежи не мало. Также очень
# много пожилых людей > 50 лет медианный возраст.

# Давайте посмотрим медианный доход у пожилых жителей.
sns.histplot(data=df[df['housing_median_age']>50], x="median_income")
# Большого отличия от популяции в целом не наблюдается. Скорее всего это местные жители.

# Давайте разобьем возрастные группы на 3 категории те кто моложе 20 лет, от 20 до 50 и от 50, чтобы посмотреть влияет ли это на доход.
df.loc[df['housing_median_age'] <= 20, 'age_group'] = 'Молодые'
df.loc[(df['housing_median_age'] > 20) & (df['housing_median_age'] <= 50),'age_group'] = 'Ср. возраст'
df.loc[df['housing_median_age'] > 50, 'age_group'] = 'Пожилые'
# Добавился новый столбец age_group, в котором будет указана соответствующая категория.

# Применим group_by, чтобы получить среднее значение.
df.groupby('age_group')['median_income'].mean().plot(kind='bar')
# Молодые оказываются самой богатой группой населения. Но отличие в доходе не значительное.

"""Seaborn так же позволяет нам смотреть распределение по многим параметрам.
Давайте поделим группы по доходам на 2. Те у кого медианный доход выше 6 и те у кого меньше. Изобразим дополнительное измерение с помощью оттенка в виде возрастных групп и групп по доходам.
"""

df.loc[df['median_income'] > 6, 'income_group'] = 'rich'
df.loc[df['median_income'] < 6, 'income_group'] = 'everyone_else'
sns.displot(df, x="median_house_value", hue="income_group")

"""Итоги:

Анализ данных должен предоставлять информацию и инсайт, которые не видны
невооруженным взглядом. В этом и есть красота аналитики. В данном случае можно сделать следующий выводы. Стоимость домов напрямую зависит от их
расположения, в определенной полосе(скорее всего побережье) цена на дома
высокая. Чем выше доход, тем больше шанс, что человек проживает в богатом
районе. Распределение по возрастам примерно одинаковое во всех группах
доходов. Ну и очевидно чем больше людей, тем больше семей, и соответственно
комнат и спален.

"""