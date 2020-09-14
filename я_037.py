"""Задание 37 (пандас)"""

import pandas

df = pandas.read_csv('/home/dabygi/Загрузки/titanic.csv')


# Описание таблицы
# Name - имя
# Sex - пол 'male' | 'female'
# Age - возраст
# Pclass - социоэкономический статус:
#  1 абрамович
#  2 хватило на timberland
#  3 нищеброд
# Survived - выжил 1 или нет 0

# 1. Распечатайте колонки которые есть датафрейме.

# print(df.columns)

# 2. Узнайте сколько людей было на борту

# print(df.shape[0])

# 3. Узнайте сколько на борту было мужчин.

# def man():
#     return df[(df['Sex'] == 'male')].shape[0]
# print(man())

# 4. Посчитайте процент выживших на борту.

# def live():
#     a = df.shape[0]
#     b = df[(df['Survived'] == 1)].shape[0]
#     return b * 100 / a
# print(live())

# 5. Кого было больше на борту, мужчин или женщин ?

# def man_or_woman():
#     a = df[(df['Sex'] == 'male')].shape[0]
#     b = df[(df['Sex'] == 'female')].shape[0]
#     if a > b:
#         return ('male')
#     else:
#         return ('female')
# print(man_or_woman())

# 6. Посчитайте сколько процентов из выживших были мужчинами?

# def live_mane_or_female():
#     live = df[(df['Survived'] == 1)].shape[0]
#     man = df[(df['Sex'] == 'male') & (df['Survived'] == 1)].shape[0]
#     return (man / live) * 100
#
# print(live_mane_or_female())

# 7. Человек какого класса вероятнее всего не выжил ?

# def no_live_class():
#     a = df[(df['Pclass'] == 1) & (df['Survived'] == 0)].shape[0] # не выжило абрамовичей
#     t = df[(df['Pclass'] == 2) & (df['Survived'] == 0)].shape[0] # не выжило 'ему хватило на timberland'
#     b= df[(df['Pclass'] == 3) & (df['Survived'] == 0)].shape[0]  # не выжило нищебродов
#     if a == max(a, t, b):
#         return 'абрамович'
#     elif t == max(a, t, b):
#         return 'ему хватило на timberland'
#     else:
#         return 'нищеброд'
#
# print(no_live_class())
