"""Задание 24"""

# 1. Оберните функцию
# def swap_words(words):
#     tmp = words.split(' ')
#     return tmp[1] + ' ' + tmp[0]

# декоратором который первую букву у выходящего значения делает большой.
# Сделать строке первую букву большой можно так:
# 'коля'.capitalize()


# Повызывайте обёрнутую функцию.

# def capit(sw):
#     def wrapper(*args):
#         result = sw(*args)
#         print(result.capitalize())
#         return result
#     return wrapper
#
# @capit
# def swap_words(words):
#     tmp = words.split(' ')
#     return tmp[1] + ' ' + tmp[0]
#
# swap_words('строке первую букву')


# 2. Оберните функцию
# def mult_on_2(ls):
#     result = []
#     for x in ls:
#         result.append(x * 2)
#     return result

# декоратором который применяет функцию 2 раза к аргументам.
# Повызывайте обёрнутую функцию.

# def double(mu):
#     def two(*args):
#         val = mu(mu(*args))
#         print(val)
#         return val
#     return two
#
# @double
# def mult_on_2(ls):
#     result = []
#     for x in ls:
#         result.append(x * 2)
#     return result
#
# mult_on_2('one')


# 3. Оберните функцию
# import math

# def my_sqrt(x):
#     return math.sqrt(x)

# декоратором который проверяет является ли аргумент отрицательным и если это так, печатает "Нельзя передавать отрицательные числа"
# и возвращает -1. Если аргумент позитивный, то просто передаёт его в функцию.

# Повызывайте обёрнутую функцию с положительными и отрицательными числами.

# import math
#
# def negative_numbers(my):
#     def two(*args):
#         for x in args:
#             if x < 0:
#                 print("Нельзя передавать отрицательные числа")
#                 return -1
#         val = my(*args)
#         print(val)
#         return val
#     return two
#
# @negative_numbers
# def my_sqrt(x):
#     return math.sqrt(x)
#
# my_sqrt()

