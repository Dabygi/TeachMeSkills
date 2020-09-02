"""Задание 21 (ООП классы и их свойства)"""

# 1. Создайте класс выражающий существительное "человек".
# Создайте 2 объекта этого класса, посмотрите их свойства.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_friend = Human('Ivan', 18)
women = Human('Olga', 20)

print(my_friend.__dict__)
print(women.__dict__)

# 2. Создайте класс выражающий существительное "дерево"
# Создайте 2 объекта этого класса, посмотрите их свойства.

class Tree:
    def __init__(self, breed, height):
        self.breed = breed
        self.height = height

tree_1 = Tree('Birch', 4)
tree_2 = Tree('Alder', 6)

print(tree_1.__dict__)
print(tree_2.__dict__)

# 3. Создайте класс выражающий существительное "дом"
# Создайте 2 объекта этого класса, посмотрите их свойства.

class House:
    def __init__(self, color, floors):
        self.color = color
        self.floors = floors

my_house = House('white', 5)
house_my_friend = House('red', 10)

print(my_house.__dict__)
print(house_my_friend.__dict__)

# 4. Создайте класс выражающий существительное "книга"
# Создайте 2 объекта этого класса, посмотрите их свойства.

class Book:
    def __init__(self, title, autor):
        self.title = title
        self.autor = autor
red_book = Book('Капитал', 'Карл Маркс')
blue_book = Book('Оно', 'Стивен Кинг')

print(red_book.__dict__)
print(blue_book.__dict__)

# 5. Создайте класс выражающий существительное "дата"
# Создайте 2 объекта этого класса, посмотрите их свойства.

class Date:
    def __init__(self, a, b):
        self.month = a
        self.number = b

january = Date(1, 31)
april = Date(4, 1)

print(january.__dict__)
print(april.__dict__)


# 6.  Создайте класс выражающий словосочетание "конверт с письмом"
# Создайте 2 объекта этого класса, посмотрите их свойства.

class Letter:
    def __init__(self, stamp, weight):
        self.stamp = stamp
        self.weight = weight

letter_to_Santa = Letter(3, 105)
letter_to_Kate = Letter(4, 115)

print(letter_to_Santa.__dict__)
print(letter_to_Kate.__dict__)