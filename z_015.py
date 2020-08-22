"""задание 15"""


# 1. Написать функцию, которая принимает список чисел и возвращает их сумму.

# def list(a):
#     g = 0
#     y = 0
#     z = len(a)
#     while y < z:
#         x = a[y]
#         g = g + x
#         y = y + 1
#     return g
#
# print(list([1, 2, 3, 4]))


# 2. Написать функцию, которая принимает список чисел и возвращает список который содержит числа раздёленными на 2
# пример запуска:
# fn([4,5,6])
# [2, 2.5, 3]   # то что вернуло

# def list_na2(b):
#     c = []
#     x = 0
#     z = len(b)
#     while x < z:
#         g = b[x]
#         c.append(g / 2)
#         x = x + 1
#     return c
#
# print(list_na2([2, 4, 6, 8]))

# 3. Написать функцию, которая принимает список и возвращает его размер. Нельзя пользоваться len.

# def list_len(b):
#     c = 0
#     z = sum(b)
#     while z > 0:
#         z = z - b[c]
#         c = c + 1
#     return c
#
# print(list_len([2, 4, 6, 8, 9]))

# 4. Написать функцию, которая принимает список чисел и некоторое число и возвращает True если число есть в списке, иначе возвращает False. Нельзя пользоваться in.

# def lt_4(list_1, a):
#     x = 0
#     c = len(list_1)
#     while x < c:
#         if list_1[x] == a:
#             return True
#         else:
#             x = x + 1
#     return False
#
# print(lt_4([2, 4, 6, 8, 9], 9))

# 5. Написать функцию, которая принимает список чисел и возвращает среднее значение для этих чисел.

# def arithmetic_mean(b):
#     g = 0
#     y = 0
#     z = len(b)
#     while y < z:
#         x = b[y]
#         g = g + x
#         y = y + 1
#     return g / z
#
# print(arithmetic_mean([2, 4, 6, 8]))

# 6. Написать функцию, которая принимает список чисел и возвращает максимальный элемент. Нельзя пользоваться функциями max\sort

# def max(b):
#     c = 0
#     z = len(b)
#     a = 0
#     while c < z:
#         if a < b[c]:
#             a = b[c]
#         c = c + 1
#     return a
#
# print(max((28, 4, 12, 8, 19)))

# 7 (-). Написать функцию, которая принимает список чисел и возвращает минимальный элемент. Нельзя пользоваться функциями min\sort

# def min(b):
#     c = 0
#     y = 0
#     z = len(b)
#     a = max(b)
#     while c < z:
#         if c == b[y]:
#             y = y + 1
#             c = c + 1
#
#         return a
#
# print(min((28, 4, 12, 8, 19)))


# 8. Написать функцию, которая принимает список чисел и возвращает только чётные числа

# def chetni(a):
#     c = []
#     y = 0
#     z = len(a)
#     while y < z:
#         if a[y] % 2 == 0:
#             c.append(a[y])
#         y = y + 1
#     return c
#
# print(chetni([1, 2, 3, 4]))

# 9. Написать функцию, которая принимает список чисел и возвращает только нечётные числа



# 10. Написать функцию, которая принимает 2 списка чисел и возвращает их общие элементы.
# Пример вызова: fn([1,2,3,4], [5,7, 2, 88, 3]), [2, 3]



# 11. Написать функцию, которая принимает 2 списка чисел и убирает из первого списка те числа которые есть во втором списке.



# 11.2 Написать функцию, которая принимает 2 числа а затем умножает их друг на друга. Нельзя пользоваться *.
# Подсказка: в python есть функция list(range(4)) которая вернёт список вида [0, 1, 2, 3]



# 12. Написать функцию, которая принимает 2 числа x и y. Затем возводит x в степень y.
#    Например если x = 4 а y = 3 то функция должна вернуть 64. Нельзя юзать ** (это оператор возведения в степень)



# 13. Написать функцию которая, печатает всю таблицу умножения от 1 до 10:
# 1 * 2 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# ...
# 10 * 10 = 100



# 14. Написать функцию принимающую список чисел. Затем функция печатает первое
# число из списка на расстоянии в 3 пробела слева. Все остальные числа равняет
# по самой правой цифре из первого числа. Чтобы было так:
#    567
#      2
#     33
#      3
# Подсказка: чтобы распечатать 3 пробела + число 25 можно сделать так print(‘ ’ * 3  + str(25))



# 15. Написать функцию тренажёр таблицы умножения. После её запуска у
# человека спрашивается 2 числа, а затем их произведение. Если человек
# ответил правильно ему засчитывается очко. Если человек в любое число ввёл -1
# то программа останавливается. Использовать while (в презентации после for)

# Пример запуска:

# У вас 0 очков.
# Введите первое число: 5
# Введите второе число: 7
# Сколько будет 5 * 7 ?: 35
# Верно.
# У вас 1 очков.
# Введите первое число: 2
# Введите второе число: 2
# Сколько будет 2 * 2 ?: 92
# Неверно.
# У вас 1 очков.
# Введите первое число: -1
# Пока.



# 16. Написать функцию принимающую список чисел и возвращающую максимальное и второе после максимального число.  Нельзя пользоваться max\sort



# 17. Написать функцию принимающую число и рисующую квадрат размером с это число.
# Пример:
# fn(4)
# ****
# ****
# ****
# ****

# Подсказка, чтобы создать строку с 3-мя звёздочками, можно сделать так: '*' * 3



# 18. Написать функцию принимающую число и рисующую рамку размером с это число.
# Пример:
# fn(4)
# ****
# *   *
# *   *
# ****



# 19. Написать функцию принимающую число и рисующую шахматную доску размером с это число.
# Пример:
# fn(4)
# * * * *
#  * * * *
# * * * *
#  * * * *



# 20. Написать функцию, которая принимает 2 числа, первое должно быть меньше второго, затем выводит все числа кратные 2-м между этими числами
# Пример:
# fn(3, 15)
# 4
# 6
# 8
# 10
# 12
# 14



# 21. Написать функцию принимающую число и вычисляющую его факториал. Факториал числа 5 = 1 * 2 * 3 * 4 * 5. Нельзя юзать math.factorial



# 22. Написать функцию которая принимает 3 переменные:
#   1. Сумма которую хотят положить на депозит
#   2. На сколько процентов будет увеличиватся сумма в месяц на депозите
#   3. Сколько месяцев планируют держать сумму в депозите.
# Функция должна возвращать накопленную сумму по прошествии времени.
# Например если депозит 50% а изначальная сумма 40 руб, держать планируют 3 месяца то:
# сумма на начало месяца | сумма на конец месяца
# 40                                       | 60
# 60                                       | 90
# 90                                       | 135
# В этом случае должно вернуть 135.



# 23. Написать функцию которая принимает число и если число является простым то возвращает True иначе False.
# Число является простым если оно делится без остатка на себя и на 1.
# Например число 7 является простым.



# 24. Написать функцию принимающую число и рисующую треугольник размером с это число.
# Например:
# fn(5)
# *
# **
# ***
# ****
# *****



# 25.* Написать функцию принимающую число и рисующую ромб размером с это число.
# Например:
# fn(7)
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *



# 26.* Написать функцию которая принимает 2 дня в виде чисел и возвращает сколько между ними дней. Пример вызова:
# fn(2020, 1, 26, 2020, 1, 21)  # вернёт 5
