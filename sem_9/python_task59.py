# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pIz2-obYS0qLr3wPKtM72X0uYObGab4R

#Задача №59. 

1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""

import pandas as pd

df = pd.read_csv('sample_data/california_housing_test.csv')

"""1. Проверить есть ли в файле пустые значения"""

df.isnull().sum()

"""Вывод: пустых значений нет, т.к. все нули

2. Показать median_house_value где median_income < 2
"""

df['median_house_value'] [df['median_income'] < 2]

"""второй способ"""

df.loc[df['median_income']<2,'median_house_value']

"""3. Показать данные в первых 2 столбцах"""

df[['longitude','latitude']]

"""ворой способ"""

df[[df.columns[0],df.columns[1]]]

"""4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000"""

df[(df['housing_median_age'] < 20) & (df['median_house_value'] > 70000)]

"""второй вариант с помощью функции loc (: означает выбрвть все данные)"""