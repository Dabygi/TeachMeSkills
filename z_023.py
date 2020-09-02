"""Задание 23"""

# 1. Создайте класс "здание". Придумайте для его 1 свойство и 1 метод.
#    Отнаследуйте от его классы "торговый центр" и "школа".
#    Для классов "торговый центр" и "школа" придумайте 1 дополнительное свойство и 1 дополнительный метод.
#    Создайте объекты всех 3-х классов. Посмотрите их свойства, повызывайте их методы.

# class Building:
#     def __init__(self, floors):
#         self.floors = floors
#
# class Hopping_center(Building):
#     def __init__(self, area, floors):
#         self.area = area
#         super().__init__(floors)
#
# class School(Building):
#     def __init__(self, capacity, floors):
#         self.capacity = capacity
#         super().__init__(floors)
#
# build_1 = Building(3)
#
# nike = Hopping_center(100, 2)
#
# my_school = School(254, 4)
#
# print(build_1.floors, nike.__dict__, my_school.__dict__)

# 2. Создайте класс Factorial у которого должен быть метод calculate, принимающий число и считающий факториал для числа.
#    Например факториал для числа 5 = 1 * 2 * 3 * 4 * 5 = 120. Всю логику расчёта поместите в инкапсулированный метод который
#    будет вызываться внутри метода calculate.
#    Создайте объект класса Factorial и поробуйте вызвать инкапсулированный метод и метод calculate.

class Factorial:
    def __init__(self, calculate):
        self.calculate = calculate

class Hopping_center(Building):
    def __init__(self, area, floors):
        self.area = area
        super().__init__(floors)


build_1 = Building(3)

nike = Hopping_center(100, 2)

my_school = School(254, 4)

# 3. Создайте класс "банк". У банка должно быть свойство - депозиты (список чисел отражающий депозиты людей
#    в банке). Создайте метод + для класса, который должен суммировать банки и как результат создавать новый банк с депозитами исходных банков.
#    Создайте 2 объекта класса "банк". Сложите их. Посмотрите депозиты нового банка.


