def input_limit():  # Функция для ввода границы суммирования
    print('Введите верхнюю границу суммирования')
    value_limit = int(input('=> '))  # Переменная для хранения границы суммирования
    print(f'\nУказать границу суммирования {value_limit}?')
    choice = input('\nВведите "д" для подтверждения или "н" для повтора ввода ').lower()
    if choice == 'д':
        input_exception(value_limit)  # Запускаем вторую функцию, передаем границу
        return value_limit  # Возвращаем результат для третьей функции
    elif choice == 'н':
        print('\n===Повторный запуск программы===')
        input_limit()  # Перезапускаем функцию


def input_exception(limit):  # Функция для ввода исключений
    result_func1 = limit  # Переменная принимающая в себя результат первой функции
    print('\nВведите ниже значение которое необходимо исключить')
    value_first = int(input('=> '))  # Переменная для ввода значений исключений
    if value_first < 0 or value_first > result_func1:  # Исключение не может быть меньше единицы и больше границы
        print('\nВведено неверное значение! Повторите попытку')
        input_exception(limit)  # Повторный запуск функции
    else:
        list_exception = []  # Список исключений
        check = True  # Флаг для завершения цикла
        list_exception.append(value_first)
        while check:  # Цикл для ввода исключений
            print(f'\nСписок исключённых значений: {list_exception}')
            print('Хотите добавить еще значения?')
            choice = input('Введите "д" или "н": ').lower()  # Перевёл в нижний регистр для проверки
            if choice == 'д':
                print('\nВведите следущее значение')
                value_second = int(input('=>'))
                if value_second < 0 or value_second > result_func1:
                    print('\nВведено не верное значение! Повторите попытку')
                    continue
                else:
                    list_exception.append(value_second)
            elif choice == 'н':
                check = False
                return list_exception  # Передаём список как результат функции
            else:
                print('\nПОВТОРИТЕ ПОПЫТКУ ВВОДА!')