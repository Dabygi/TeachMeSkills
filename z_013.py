"""задание 13"""


# Подсказка
# Чтобы получить число от пользователя, можно сделать так:
# x = int(input("Введи число:"))

# 1. Написать функцию которая принимает число и если оно меньше или равно 34 печатает ваше имя иначе имя вашей мамы.

# def one():
#     x = int(input("Введи число:"))
#     if x <= 34:
#         print('Artem')
#     else: print('Yauhenia')
#
# one()

# 2. Написать функцию которая принимает 2 числа, и если их сумма равна 5 делит эту сумму на 2 и возвращает результат в противном случае возвращает их сумму.

# def two():
#     x = int(input("Введи 1-е число:"))
#     y = int(input("Введи 2-е число:"))
#     if x + y == 5:
#         c = (x + y) / 2
#         print(c)
#     else: print(x + y)
#
# two()

# 3. Написать функцию принимающую строку и если она меньше пяти символов напечатать её
# иначе напечатать сообщение 'строка сильно большая , я устал'.

# def string():
#     a = input("Введи строку:")
#     if len(a) < 5:
#         print(a)
#     else:
#         print('строка сильно большая , я устал')
#
# string()

# 4. Написать функцию которая спрашивает у пользователя 2 числа и если первое больше второго печатает их сумму иначе печатает их произведение.

# def four():
#     x = int(input("Введи 1-е число:"))
#     y = int(input("Введи 2-е число:"))
#     if x > y:
#         print(x + y)
#     else: print(x * y)
#
# four()

# 5. Написать функцию которая спрашивает таблицу умножения у пользователя и если он отвечает верно
# печатает 'верно' иначе печатает неверно.

# def mult_table():
#     x = int(input("Введи 1-е число:"))
#     y = int(input("Введи 2-е число:"))
#     c = x * y
#     b = int(input("Введи произведение 1-го и 2-го:"))
#     if b == c:
#         print('Верно!')
#     else:
#         print('Неверно!')
#
# mult_table()

# 6. Написать функцию которая спрашивает у пользователя столицу РБ и предлагает варианты:
# a: Бобруйск
# b: Лондон
# с: Минск
# Если пользователь ответил правильно - напечатать “Верно” иначе Неверно”

# def capital():
#     y = (input("Какая столица у РБ? \n a: Бобруйск \n b: Лондон \n с: Минск \n Напишите правильный вариант: "))
#     if y == 'с: Минск':
#         print('Верно!')
#     else:
#         print('Неверно!')
#
# capital()

# 7. Написать функцию которая принимает строку как аргумент, затем спрашивает какое слово заменить и каким словом заменить.

# Пример вызова функции:
# fn('Какой прекрасный день')
# Какое слово заменить: прекрасный  # спрашивает через input
# Каким словом заменить: ужасный    # спрашивает через input
# 'Какой ужасный день'                        # fn возвращает такую строчку

# def replacing_words(string):
#     x = (input("Какое слово заменить: "))
#     y = (input("Каким словом заменить: "))
#     print(string.replace(x, y))
#
# replacing_words('Какой прекрасный день')

# 8. Написать функцию принимающую имя. Если имена 'Вася' или 'Петя' то печатает привет братаны.
# Если она 'Толик' то напечатать 'Поделись на нолик'.
# Если имя не является 'Вася' или 'Петя' или 'Толик'  то функция печатает - ‘Я тебя не знаю’.

# def name_friends():
#     y = (input("Как тебя звать? "))
#     if y == 'Вася' or y == 'Петя':
#         print('привет братаны!')
#     elif y == 'Толик':
#         print('Поделись на нолик!')
#     else:
#         print('Я тебя не знаю')
#
# name_friends()

# 9.* Написать функцию, которая принимает день месяц и год в виде
# чисел и печатает Yes если такая дата существует и No если такой
# даты не существует. Считать, что в феврале всегда 28 дней.

def ver_date():
    import time
    import calendar

    date = input('Для проверки введите дату в формате dd.mm.yyyy: ')
    try:
        valid_date = time.strptime(date, '%d.%m.%Y')
        print('Yes')

    except ValueError:
        print('No')

    # y = (input("Для проверки введите дату в формате ХХ.ХХ.ХХХХ: "))
    # x = y.split('.')
    # day = int(x[0])
    # month = int(x[1])
    # year = int(x[2])
    # if 1 <= year and 1 <= month <= 12 and 1 <= day <= 28
    # print(year)

ver_date()