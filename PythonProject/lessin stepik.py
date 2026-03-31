#Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и обрабатывает возможные ошибки.

#Пример вывода:

#Введите делимое: 345

#Введите делитель: 5a


#Ошибка: Введено некорректное число.
def divide_number():
    while True:
        try:
            a = input("введите делимое: ")
            b = input("Введите делитель:")

            num = float(a)
            num2 = float(b)

            return num / num2

        except ValueError:
            print("Ошибка: некорректное число")
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
print(divide_number())
print("nikita gei")
