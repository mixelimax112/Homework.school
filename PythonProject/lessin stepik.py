#Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.

#Пример вывода:

#Введите делимое: 345

#Введите делитель: 5a


#Ошибка: Введено некорректное число.
import logging

logging.basicConfig(
    filename='errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
    encoding='utf-8'
)


def divide_number():
    while True:
        try:
            a = input("Введите делимое: ")
            b = input("Введите делитель: ")


            num = float(a)
            num2 = float(b)

            return num / num2

        except ValueError:

            logging.error("Ошибка: Введено некорректное число")
            return "Ошибка: Введено некорректное число"


        except ZeroDivisionError:
            logging.error ("Ошибка: Деление на ноль.")
            return "Ошибка: Деление на ноль."



print(divide_number())