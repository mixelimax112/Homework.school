# Анализ курсов студентов
# Реализовать программу, которая должна:
# Прочитать файл student_courses.json, содержащий:
# имя,
# дату рождения (birth_date) в формате дд.мм.гггг,
# дату поступления (enrollment_date) в том же формате,
# список курсов.
# Вычислить:
# Общее количество студентов.
# Средний возраст на момент поступления.
# Количество студентов на каждом курсе.
# Сохранить отчёт в JSON-файл student_courses_report.json.
# Данные:
# [
#   {"name": "Diana Williams", "birth_date": "12.06.1983", "enrollment_date": "29.04.2023", "courses": ["Physics", "Chemistry"]},
#   {"name": "Tina Miller", "birth_date": "06.07.2004", "enrollment_date": "18.04.2020", "courses": ["Biology", "Business"]},
#   {"name": "Kevin Miller", "birth_date": "20.12.2004", "enrollment_date": "16.12.2020", "courses": ["Linguistics", "Math", "History"]},
#   {"name": "Fiona Brown", "birth_date": "05.07.1999", "enrollment_date": "02.09.2022", "courses": ["Art", "Philosophy"]},
#   {"name": "Charlie Davis", "birth_date": "17.07.1998", "enrollment_date": "17.05.2023", "courses": ["Chemistry", "Physics", "Business"]},
#   {"name": "Diana Jones", "birth_date": "24.12.1980", "enrollment_date": "26.11.2021", "courses": ["Economics", "Linguistics"]},
#   {"name": "Alice Johnson", "birth_date": "22.09.1981", "enrollment_date": "23.12.2020", "courses": ["Chemistry", "Economics", "Math"]},
#   {"name": "Ian Lopez", "birth_date": "23.11.2001", "enrollment_date": "07.05.2020", "courses": ["Philosophy", "Art", "Physics"]},
#   {"name": "Kevin Davis", "birth_date": "30.01.1997", "enrollment_date": "20.03.2021", "courses": ["Math", "Economics"]},
#
#   ...
# ]
# Пример вывода (student_courses_report.json):
# {
#     "total_students": 100,
#     "average_enrollment_age": 27.9,
#     "students_per_course": {
#         "Art": 21,
#         "Biology": 18,
#         "Business": 28,
#         "Chemistry": 16,
#         "Economics": 23,
#         "History": 9,
#         "Linguistics": 23,
#         "Math": 23,
#         "Philosophy": 19,
#         "Physics": 19
#
#     }
#
# }



def count_student(y):

    import json
    count = 0
    with open(y, "r") as f:
        trans = json.load(f)
        for item in trans:
            for key in item.keys():
                if key == "name":
                    count += 1
    return count
print(count_student("PythonProject/student_courses.json"))

def birthday_students(x):
    import json
    from datetime import datetime
    students_ages = []
    with open(x, 'r') as f:
        trans  = json.load(f)
        for item in trans:
            birth = datetime.strptime(item['birth_date'], "%d.%m.%Y")
            enroll = datetime.strptime(item['enrollment_date'], "%d.%m.%Y")
            res = enroll - birth
            students_ages.append(res.days // 365)
    avg_age = sum(students_ages) / len(students_ages)
    return avg_age
print(birthday_students("PythonProject/student_courses.json"))



import json
from datetime import datetime


def students_per_course(x):
    with open(x, 'r', encoding='utf-8') as file:
        data = json.load(file)

    course_counts = {}
    total_age = 0
    total_students = len(data)

    for item in data:
        birth = datetime.strptime(item['birth_date'], "%d.%m.%Y")
        enroll = datetime.strptime(item['enrollment_date'], "%d.%m.%Y")

        total_age += (enroll.year - birth.year)

        for course in item['courses']:
            if course in course_counts:
                course_counts[course] += 1
            else:
                course_counts[course] = 1

    report = {
        "total_students": total_students,
        "average_enrollment_age": round(total_age / total_students, 1),
        "students_per_course": course_counts
    }

    return report



result = students_per_course("PythonProject/student_courses.json")


with open("student_courses_report.json", "w", encoding="utf-8") as outfile:
    json.dump(result, outfile, indent=4)

print("Отчет успешно сохранен в файл student_courses_report.json")