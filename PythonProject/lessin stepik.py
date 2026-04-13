import os


def process_files():


    log_file = input("Введите имя файла для поиска: ")
    keyword = input("Введите ключевое слово: ")

    if not os.path.exists(log_file):
        print(f"Ошибка: файл {log_file} не найден!")
    else:
        found_lines = []
        with open(log_file, "r", encoding="utf-8") as file:
            for line in file:
                if keyword in line:
                    found_lines.append(line)

        if found_lines:
            new_log_name = f"{keyword}_{log_file}"
            with open(new_log_name, "w", encoding="utf-8") as new_file:
                new_file.writelines(found_lines)
            print(f"Строки, содержащие '{keyword}', сохранены в {new_log_name}.")
        else:
            print(f"Совпадений для '{keyword}' не найдено. Файл не создан.")

    print("\n" + "=" * 40 + "\n")



    movies_file = input("Введите имя файла: ")

    if not os.path.exists(movies_file):
        print(f"Ошибка: файл {movies_file} не найден!")
    else:
        unique_lines = []
        seen = set()

        with open(movies_file, "r", encoding="utf-8") as file:
            for line in file:

                if line not in seen:
                    unique_lines.append(line)
                    seen.add(line)

        new_movies_name = f"unique_{movies_file}"
        with open(new_movies_name, "w", encoding="utf-8") as new_file:
            new_file.writelines(unique_lines)

        print(f"Дубликаты удалены. Уникальные строки сохранены в {new_movies_name}.")


if __name__ == "__main__":
    process_files()