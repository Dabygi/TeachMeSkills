"""Задание 38"""

# Загрузите 2 датафрейма:
import pandas
info = pandas.read_csv("/home/dabygi/Загрузки/info.csv")
marks = pandas.read_csv("/home/dabygi/Загрузки/marks.csv")

# Описание info:
# id - номер студента
# gender - пол студента
# race - расса студента
# parents_education - образование родителей студента

# Описание marks:
# id2 - номер студента
# lunch - есть ли скидка в столовке у студента
# prep_course - ходил ли студент на подготовительные курсы
# math - оценка по математике
# reading - оценка по чтению
# writing - оценка граматнасьци студента

# 1. Узнайте для скольких людей из датафрейма info неизвестны оценки.
# Подсказка: нужно использовать 1 merge некоторого типа и .shape

# def man():
#     return (info.merge(marks, left_on='id', right_on='id2')).shape[0]
# print(man())

# 2. Узнайте для скольких людей из датафрейма marks неизвестны расса\пол\...
# Подсказка: нужно использовать 1 merge некоторого типа и .shape

# def man_race():
#     a = (info.merge(marks, left_on='id', right_on='id2', how='right')).shape[0]
#     b = (info.merge(marks, left_on='id', right_on='id2')).shape[0]
#     return a - b
# print(man_race())

# 3. Узнайте среднюю оценку по математике рассы "group A".
# Нужно использовать 1 merge некоторого типа.

# def average_mark():
#     all = (info.merge(marks, left_on='id', right_on='id2'))   # объединил две таблицы
#     b = (all[(all['race'] == 'group A')])                     # таб выборка всех с 'group A'
#     c = b['math'].sum()                                       # сумма оценок
#     return int(c / b.shape[0])                                # средняя оценка
#
# print(average_mark())

# 4. Объедините датафреймы в один так чтобы в результирующем датафрейме были люди из обоих датафреймов info и marks.
# Для тех у кого нет оценок должны быть NaN на месте оценок. Для тех у кого нет информации о рассе\поле\образовании родителей на месте инфы должны быть NaN.
# Нужно использовать 1 merge некоторого типа.
# В результирующем датафрейме будет 1000 строк.

# def man_merge():
#     return (info.merge(marks, left_on='id', right_on='id2', how='outer'))
# print(man_merge())

# 5. Объедините датафреймы в один так чтобы в результирующем датафрейме были все
# известные люди из датафрейма info. Для тех людей из info для которых нет оценок в
# marks, на месте оценок должны стоять NaN.
# Нужно использовать 1 merge некоторого типа.
# В результирующем датафрейме будет 960 строк.

# def man_left():
#     return (info.merge(marks, left_on='id', right_on='id2', how='left')).shape[0]
# print(man_left())

# 6. Объедините датафреймы в один так чтобы в результирующем датафрейме были все
# известные люди из датафрейма marks. Для тех людей из marks для которых нет расс\пола\... в info, на месте расс\пола\... должны стоять NaN.
# Нужно использовать 1 merge некоторого типа. Тип мержа должен быть не таким как в 5-м задании.
# В результирующем датафрейме будет 678 строк.

# def man_right():
#     return (info.merge(marks, left_on='id', right_on='id2', how='right')).shape[0]
# print(man_right())