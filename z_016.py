"""Задание 16"""

# 1. Написать функцию, которая принимает список чисел и возвращает этот же список но с уже измененными числами по
# следующей логике: если число больше 100 то умножает его на 2 иначе делит его на 3. Использовать map.

# def list_in(a):
#     if a > 100:
#         a = a * 2
#     else:
#         a = a / 3
#     return a
#
# print(list(map(list_in, [300, 90, 400, 99])))

# 2. Написать функцию, которая принимает список чисел и возвращает список только четных чисел. Использовать filter.

# def chet(a):
#
#     return a % 2 == 0
#
# print(list(filter(chet, [4, 7, 9, 18, 13])))

# 3.  С помощью reduce сложить все числа в списке. Перед определением fn написать: from functools import reduce

# from functools import reduce
#
# def sum_red(a, b):
#     return a + b
#
# print(reduce(sum_red, [2, 3, 6], 0))

# 4. Написать map

# def fn(a):
#     return a + 2
#
# def maper(fn, a):
#     z = []
#     for i in a:
#         if fn(i):
#             z.append(fn(i))
#     return z
#
# print(list(maper(fn, [300, 90, 400, 99])))

# 5. Написать filter

# def fn(a):
#     return a > 100
#
# def filt(fn, a):
#     z = []
#     for i in a:
#         if fn(i):
#             z.append(i)
#     return z
#
# print(list(filt(fn, [300, 90, 400, 99])))

# 6. Написать функцию которая принимает функцию и 2 числа (пусть x и z).
# Затем функция которую приняли применяется к x-y z-раз.
# Например: def increment(m):
#             return m + 4

#            fn(increment, 6, 2)
#            fn вернёт 14. x тут равен 6. z тут равен 2.
# Тоесть написать функцию fn.

# def increment(x):
#     return x + 2
#
# def fn(increment, x, z):
#     g = 1
#     while g <= z:
#         g = g + 1
#         x = increment(x)
#     return x
# print(fn(increment, 3, 3))

# 6.* С помощью reduce найти максимальное число в списке



# 7.* Написать reduce

