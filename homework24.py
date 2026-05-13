# Сумма цифр числа
#
# Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
#
# Данные:
#
# num = 43197
#
# Пример вывода:
#
# 24
# def digit(number):
#     if number == 0:
#         return 0
#
#     last_digit = number % 10
#     rest = number // 10
#     return last_digit + digit(rest)
#
# print(digit(43197))
# Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
#
# Данные:
#
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
#
# Пример вывода:
#
# 28
# def nested_sum(lst):
#     if lst == []:
#         return 0
#
#     first = lst[0]
#     rest = lst[1:]
#
#     if isinstance(first, list):
#         return nested_sum(first) + nested_sum(rest)
#     else:
#         return first + nested_sum(rest)
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
# print(nested_sum(nested_numbers))