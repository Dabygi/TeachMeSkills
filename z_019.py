"""Задание 19"""

# 1. Написать функцию которая принимает нефиксированное количество обязательных аргументов и суммирует их.

# def sumir(*a):
#     return sum(a)
# print(sumir(1, 2, 3))

# 2. Пробежать по значениям словаря можно так:
#    d = {'a': 1, 'b': 22}
#    for x in d.values():
#        print(x)
#    --------------------
#    1
#    22
#    Написать функцию которая принимает нефиксированное количество необязательных аргументов и перемножает их.

# def dict_2(**d):
#     a = 1
#     for x in d.values():
#         a = a * x
#     return a
#
# print(dict_2(f=2, y=3, g=4))

# 3. Написать функцию которая принимает фиксированное количество обязательных аргументов и нефиксированное количество необязательных аргументов и суммирует их.

# def sum_3(a, b, **c):
#     y = 0
#     for x in c.values():
#         y = y + x
#     return a + b + y
#
# print(sum_3(2, 3, f=1, g=2,k=3))

# 4. Написать функцию которая принимает нефиксированное количество обязательных аргументов и фиксированное количество необязательных аргументов и перемножает их.

# def mult(*a, b=3, c=4):
#     y = 1
#     for x in a:
#         y = y * x
#     return y * b * c
#
# print(mult(2, 1, 1, b=3,))

# 5. Написать функцию которая принимает нефиксированное количество обязательных аргументов и нефиксированное количество
# необязательных аргументов и суммирует их.

# def fn(*a, **b):
#     y = 0
#     for x in b.values():
#         y = y + x
#     return sum(a) + y
#
# print(fn(1, 1, 2, c=3, g=4))