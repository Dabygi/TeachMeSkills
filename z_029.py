"""задание 29 регулярные выражения"""

# 1. Написать регулярное выражение которое проверяет является ли строка строкой вида "a<любое число>c".
#    Пример: a23c

import re

print(re.match("^\w\d+\w$", 'a23c') is not None)

# 2. Написать регулярное выражение которое проверяет является ли строка строкой вида "a<любое число или ничего>c".

print(re.match("^(\w\d+?\w)$", 'a23c') is not None)

# 3. (-) Написать функцию, которая выдирает логин из email. Если прислали не email вызвать исключение, в котором написать “Понимаю только email”. Использовать регулярные выражения.
# >>> get_login(“give_me_spam@gmail.com”)
# >>> “give_me_spam”
# >>> get_login(“fvdfvdfv”)
# >>> Exception: Понимаю только email

def log(email):
    x = re.match("^(\w+@\w+.\w+)$", email) is not None #через группы
    if x is True:
        print()

# 4. Написать регулярное выражение которое выражение вытягивает из тега значение.
# Пример: "<a>nn<a>"   тут значением являестя "nn", "<privet>kak dela<privet>" тут значением являестя "kak dela".
# Нужно использовать .groups()



# 5. Написать функцию которая принимает строку и выдирает из неё минуты или говорит что это не время.
#    Использовать регулярные выражения
#
# >>> fn("2018-01-09 12:32:04")
# >>> "32"
#
# >>> fn("bla bla")
# >>> "непонимаю"



# 6. Написать калькулятор который умеет +, -, *, /. Для выдирания частей использовать .groups().
# >>> calc("4 + 5")
# >>> 9



# >>> calc("4 * -5")
# >>> -20
# Помнить что числа могут быть не целыми 23.45, отрицательными.
# Перед + и * в регулярном выражении ставить \
