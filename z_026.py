"""Задание 26 (импорт библиотек; вирт. окружение"""

# 1. Импортировать 2-мя способами функции стандартной библиотеки:

from statistics import mean

print(mean([1, 2, 3, 4, 4])) # среднеарифметическое

from math import factorial

print(factorial(4)) # факториал

from json import dumps, loads

print(dumps([1, 2, 3, 4]))

#    Понять что они делают (погуглив), повызывать к какими-нибудь аргументами.



# 2. Установить с помощью pip библитеку Jinja2 версии 2.9.3
# Проверить что библиотека установлена можно импортировав:
#        from jinja2 import Environment

# done


# 3. Создать 2 виртуальных окружения с именами old_django и new_django.

# done

# 4. В виртуальное окружение old_django установить версию django 1.6, в окружение new_django установить django 2.0
# Проверить что библиотеки установлены можно импортировав:
# from django.http import HttpResponse

# done