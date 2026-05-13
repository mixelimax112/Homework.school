# План по дням недели
#
# Напишите программу, которая помогает планировать дела.
# Программа должна бесконечно выводить план на следующий день недели, пока пользователь нажимает 'Enter'.
#
# Данные:
#
# # Расписание дел на неделю
#
# weekly_schedule = {
#
#     "Monday": ["Gym", "Work", "Read book"],
#
#     "Tuesday": ["Meeting", "Work", "Study Python"],
#
#     "Wednesday": ["Shopping", "Work", "Watch movie"],
#
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#
#     "Friday": ["Work", "Dinner with friends"],
#
#     "Saturday": ["Hiking", "Rest"],
#
#     "Sunday": ["Family time", "Rest"]
#
# }
#
# Пример ввода:
#
# Нажмите 'Enter' для получения плана:
#
# Monday: Gym, Work, Read book
#
# Нажмите 'Enter' для получения плана:
#
# Tuesday: Meeting, Work, Study Python
#
# ...
#
# Нажмите 'Enter' для получения плана:
#
# Sunday: Family time, Rest
#
# Нажмите 'Enter' для получения плана:
#
# Monday: Gym, Work, Read book
#
# Нажмите 'Enter' для получения плана: q
#
# ...


# weekly_schedule = {
#
#      "Monday": ["Gym", "Work", "Read book"],
#
#      "Tuesday": ["Meeting", "Work", "Study Python"],
#
#      "Wednesday": ["Shopping", "Work", "Watch movie"],
#
#     "Thursday": ["Work", "Call parents", "Play guitar"],
#
#     "Friday": ["Work", "Dinner with friends"],
#
#     "Saturday": ["Hiking", "Rest"],
#
#     "Sunday": ["Family time", "Rest"]
#
# }
#
# days = list(weekly_schedule.keys())
# index = 0
#
# while True:
#     user_input = input("Нажмите 'Enter': ")
#     if user_input == "q":
#         break
#
#     day = days[index]
#     tasks = weekly_schedule[day]
#     print(f"{day}: {', '.join(tasks)}")
#     index += 1
#     if index == 7:
#         index = 0

# fruits = ["Apple", "Banana", "Orange"]
# vegetables = ["Carrot", "Tomato", "Cucumber"]
# dairy = ["Milk", "Cheese", "Yogurt"]
#
# def get_all_products(*lists):
#     for product_list in lists:
#         for item in product_list:
#             yield item.lower()
#
#
# product_gen = get_all_products(fruits, vegetables, dairy)
#
#
# for product in product_gen:
#     print(product)
# from itertools import product
#
# clothes = ["T-shirt", "Jeans", "Jacket"]
# colors = ["Red", "Blue", "Black"]
# sizes = ["S", "M", "L"]
#
# def print_combinations(items, cls, szs):
#
#     for item, color, size in product(items, cls, szs):
#         print(f"{item} - {color} - {size}")
#
#
# print_combinations(clothes, colors, sizes)