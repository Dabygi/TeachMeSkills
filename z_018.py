"""задание 18"""

# 1. Написать функцию которая принимает один обязательный аргумент и один дефолтный со значением 7 затем возвращает их произведение.
# Вызвать функцию с передачей дефолтного аргумента и без передачи дефолтного аргумента.

def one(x, y=7):
    return x * y

print(one(2))
print(one(2, 2))

# 2. Написать функцию принимающую 2 списка. Один из них дефолтный. Функция должна возвращать сумму списков.
# Вызвать функцию с передачей дефолтного аргумента и без передачи дефолтного аргумента.

def sum_list(a, b = [1, 2, 3, 4]):
    return a + b

print(sum_list([1, 2, 3, 4]))

# 3. Написать функцию принимающую 2 числа (одно из них дефолтное) и дефолтный словарь. Функция должна возвращать сумму чисел разделенную на значение под ключём 'divisor' из словаря.
# Вызвать функцию с передачей дефолтного аргумента и без передачи дефолтного аргумента.

def fn(a, b = 3, c = {x: 2, y: 3}):
