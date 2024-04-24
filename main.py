import os
os.system("clear")

filename = 'guide.txt'


def copy():
    print()
    print('>>Копирование<<')
    print()
    with open(filename, 'r', encoding="utf-8") as file:
        file_len = 0
        file_len = len(file.readlines())
    num_lines_str = input("Введите количество строк для копирования: ")
    line_indexes_str = input(f"Введите через запятую, без пробелов индексы строк для копирования (всего строк в файле {file_len}): ")
    copy_file = input("Введите название файла для копирования (пример: copy.txt) ")

    try:
        num_lines = int(num_lines_str)
        line_indexes = [int(idx) for idx in line_indexes_str.split(',')]
    except ValueError:
        print("Некорректный ввод. Количество строк и индексы должны быть целыми числами.")
        return

    with open(filename, 'r', encoding="utf-8") as source_file:
        lines = source_file.readlines()

    if not line_indexes:
        line_indexes = range(num_lines)

    lines_to_copy = [lines[i] for i in line_indexes if i < len(lines)]

    valid = False
    while not valid:
        answer = input("Вы точно хотите скопировать эти строки? (да/нет) ")
        if answer.lower() == 'да':
            with open(copy_file, 'a', encoding="utf-8") as target_file:
                target_file.writelines(lines_to_copy)
            print(f"Скопировано {len(lines_to_copy)} строк в файл {copy_file}")
            valid = True
        elif answer.lower() == 'нет':
            print("Копирование отменено.")
            valid = True
        else:
            print('Некорректный ответ. Введите "да" или "нет".')


def remove():
    print()
    print('>>Удаление<<')
    print()
    with open(filename, 'r', encoding="utf-8") as file:
        file_len = 0
        file_len = len(file.readlines())
    print(f"Всего строк в файле: {file_len}")
    line_nums = input("Введите номера строк для удаления через запятую (например, 1,3,5): ")
    line_nums = [int(num) for num in line_nums.split(",")]

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("Будут удалены следующие строки:")
    for num in line_nums:
        print(f"Строка {num}: {lines[num-1].strip()}")

    valid = False
    while not valid:
        confirm = input("Точно ли вы хотите удалить выбранные строки? (да/нет): ")
        if confirm.lower() == "да":
            new_lines = [line for i, line in enumerate(lines, 1) if i not in line_nums]

            with open(filename, "w", encoding="utf-8") as file:
                file.writelines(new_lines)
            valid = True
            print("Строки успешно удалены.")

        elif confirm.lower() == "нет":
            print("Удаление строк отменено.")
            valid = True
        else:
            print("Незивестный ответ.\n")
        

def add_tel():
    print()
    print('>>Добавление<<')
    print()
    data = [
        input("Введите фамилию: "),
        input("Введите имя: "),
        input("Введите отчество: "),
        input("Введите номер телефона: "),
    ]
    st = " ".join(data)
    valid = False
    while not valid:
        answer = input("Вы точно хотите скопировать эти строки? (да/нет): ")
        if answer.lower() == 'да':
            with open(filename, "a", encoding="utf-8") as f:
                f.write('\n'+st+'\n')
                print('Номер записан!')
            valid = True
        elif answer.lower() == 'нет':
            print("Копирование отменено.")
            valid = True
        else:
            print('Некорректный ответ.\n')

def get_guide():
    print()
    print('>>Показ<<')
    print()
    data = []
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    print("\t".join(title))
    print("___________________________")
    with open(filename, "r", encoding="utf-8") as f:
        st = f.read()
    print(st)
    return data


def find():
    print()
    print('>>Поиск<<')
    print()
    print(f"Поиск по:\n1 имени\n2 фамилии\n3 отчеству\n4 номеру\n0 выход")
    valid = False
    while not valid:
        search_option = input("Введите опцию поиска (1-4 или 0 для выхода): ")
        options = ['0', '1', '2', '3', '4']
        if search_option == "0":
            print('Вы вышли из поиска.')
            valid = True
        elif search_option not in options:
            print('Такой опции поиска нет. Введите другую.')
        else:
            title = ["Фамилия", "Имя", "Отчество", "Телефон"]
            search_value = input("Введите значение для поиска: ")
            n_line = []
            with open('guide.txt', 'r', encoding='utf-8') as f:
                print("\t\t".join(title))
                for counter, line in enumerate(f):
                    line = line.strip().split()
                    if search_option == "1" and search_value == line[1]:
                        n_line.append(counter)
                        print("\t\t".join(line))
                    elif search_option == "2" and search_value == line[0]:
                        n_line.append(counter)
                        print("\t\t".join(line))
                    elif search_option == "3" and search_value == line[2]:
                        n_line.append(counter)
                        print("\t\t".join(line))
                    elif search_option == "4" and search_value == line[3]:
                        n_line.append(counter)
                        print("\t\t".join(line))
            valid = True
            return n_line


def menu():
    dct = {
        "cr": 'Добавить запись (введите "cr")',
        "rm": 'Удалить запись (введите "rm")',
        "cp": 'Сокпировать данные из справочника (введите "cp")',
        "sh": 'Вывести справочник (введите "sh")',
        "fd": 'Найти контакты (введите "fd")',
        "ex": 'Выйти из программы (введите "ex")',
    }

    while True:
        for key, value in dct.items():
            print("-", value)

        cmd = input('Введите команду: ')

        if cmd == "ex":
            return cmd
        elif cmd not in dct:
            print("Такой команды нет.\n")
        else:
            return cmd


while True:
    cmd = menu()
    if cmd == "cr":
        add_tel()
    elif cmd == "rm":
        remove()
    elif cmd == "sh":
        get_guide()
    elif cmd == "cp":
        copy()
    elif cmd == "fd":
        find()
    else:
        exit()
    print('_______________________________')
    input('Нажмите enter, чтобы продолжить: ')