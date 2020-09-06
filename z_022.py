"""задание 22"""

# В этом упражнении мы будем добавлять методы для классов созданных в прошлом упражнении.

# 1. Для класса "дерево" добавьте свойство рост. Сделайте метод который увеличивает рост дерева на кол-во сантиметров переданных аргументом в метод.
# Повызывайте новый метод, посмотрите как меняются свойства.

# class Tree:
#     def __init__(self, breed, age, height):
#         self.breed = breed
#         self.age = age
#         self.height = height
#
#     def height_up(self, up):
#         self.new_height = self.height + up
#
# tree_1 = Tree('Birch', 4, 3)
# tree_2 = Tree('Alder', 6, 5)
#
# tree_1.height_up(1)
# tree_2.height_up(2)
#
# print(tree_1.new_height)
# print(tree_2.new_height)

# 2. Для класса "человек" добавьте свойство съеденные конфеты (eaten_candy) как список конфет, которые съел человек.
# Создайте метод для человека который будет есть конфеты. Повызывайте новый метод, посмотрите как меняются свойства.

# class Human:
#     def __init__(self, name, age, eaten_candy):
#         self.name = name
#         self.age = age
#         self.eaten_candy = eaten_candy
#
#     def eating(self, title):
#         self.eaten_candy += title
#
# my_friend = Human('Ivan', 18, [1])
# women = Human('Olga', 20, [0, 1])
#
# my_friend.eating([2, 3, 4])
# women.eating([2, 3, 4, 5, 6])
#
# print(my_friend.eaten_candy)
# print(women.eaten_candy)

# 3. Для класса "книга" добавьте свойство - страницы в виде списка строк (1 строка - 1 страница). Сделайте метод который распечатывает страницу под номером
# переданным аргументом в метод. Повызывайте новый метод.

# class Book:
#     def __init__(self, title, autor, pages):
#         self.title = title
#         self.autor = autor
#         self.pages = pages
#
#     def page_num(self, number):
#         self.number = self.pages[number]
#
# red_book = Book('Капитал', 'Карл Маркс', ['стр1', 'стр2', 'стр3'])
# blue_book = Book('Оно', 'Стивен Кинг', ['стр4', 'стр5', 'стр6'])
#
# red_book.page_num(1)
# blue_book.page_num(2)
#
# print(red_book.number)
# print(blue_book.number)


# 4. Для класса "конверт с письмом" добавьте свойство письмо. Создайте метод который добавляет к письму подпись в конце.
# Тоесть:
# Бла бла бла
# текст письма
#
# С уважением, <имя адресата>.               <-- Это и есть подпись

# class Letter:
#     def __init__(self, stamp, weight, text):
#         self.stamp = stamp
#         self.weight = weight
#         self.text = text
#
#     def signature(self, content):
#         self.content = self.text + content
#         return self.content
#
# letter_to_Santa = Letter(3, 105, 'Бла бла бла \n текст письма \n')
# letter_to_Kate = Letter(4, 115, 'Тру ту ту \n текст письма \n')
#
# print(letter_to_Santa.signature('С уважением, Artem'))
# print(letter_to_Kate.signature('С уважением, Artem'))

# 5. (-) Для класса "дата" добавьте свойства месяц\день\год. Создайте метод который добавляет переданное количество дней к дате которую хранит.
# Повызывайте новый метод, посмотрите как меняются свойства.

class Date:
    def __init__(self, a, b, c):
        self.month = a
        self.day = b
        self.year = c

    def plus_day(self, j):
        if self.day + j <= 31:
            self.day = self.day + j
        if self.day + j > 31:
            self.day = (self.day + j) - 31
            self.month += 1

new_year = Date(1, 31, 1989)
fools_day = Date(4, 1, 1992)

new_year.plus_day(5)
print(fools_day.plus_day(6))
