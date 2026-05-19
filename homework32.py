# Фабрика функций округления
#
# Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
# Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.
#
# Пример вызова:
#
# print(round2(3.14159))
#
# print(round2(2.71828))
#
# print(round0(9.999))
#
# Пример вывода:
#
# 3.14
#
# 2.72
#
# 10.0

# def make_rounder(digits):
#     def rounder(number):
#         return round(number, digits)
#     return rounder
#
# round2 = make_rounder(2)
# round0 = make_rounder(0)
#
# print(round2(3.14159))
# print(round2(2.71828))
# print(round0(9.999))
# from datetime import datetime
# def make_logger():
#     events = []
#     def log(event=None):
#         if event is not None:
#             events.append(event + ": " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         return events
#     return log
# log = make_logger()
#
# log("Загрузка данных")
# log("Обработка завершена")
# for event in log():
#     print(event)
# def frame(func):
#     def wrapper():
#         print("-" * 50)
#         func()
#         print("-" * 50)
#     return wrapper
# @frame
# def say_hello():
#     print("привет игрок")
#
# say_hello()'