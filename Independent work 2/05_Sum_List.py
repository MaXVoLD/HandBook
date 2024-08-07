# Задача: Пользователь вводит список целочисленных значений и верхнюю границу суммы.
# Проссумировать целочисленные значения до верхней границы суммы исключая значения из списка.

# ***Первая функция для ввода границы суммирования***
def input_limit():  # Функция для ввода границы суммирования
    print('Введите верхнюю границу суммирования')
    value_limit = int(input('=> '))  # Переменная для хранения границы суммирования
    print(f'\nУказать границей суммирования число {value_limit}?')
    choice = input('\nВведите "д" для подтверждения или "н" для повтора ввода: ').lower()
    if choice == 'д':
        print('\nХотите ввести исключения?')
        choice = input('Введите "д" или "н": ').lower()
        check = True
        while check:  # Цикл для выбора пользователя
            if choice == 'д':
                check = False
                input_exception(value_limit)  # Запускаем вторую функцию, передаем границу
                return value_limit  # Возвращаем результат для третьей функции
            elif choice == 'н':
                check = False
                summ_func(value_limit, [])
            else:
                print('\nОшибка ввода! Повторите попытку')
    elif choice == 'н':
        print('\n===Повторный запуск программы===')
        input_limit()  # Перезапускаем функцию


# ***Вторая функция для ввода исключений***

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
                summ_func(result_func1, list_exception)  # Запускаем 3ю функцию и передаем границу и список исключений
            else:
                print('\nПОВТОРИТЕ ПОПЫТКУ ВВОДА!')


# ***Третья функция для суммирования***


def summ_func(limit, exception):  # Функция для расчёта суммы
    summ = 0  # Переменная для хранения суммы
    list_value = []  # Список для чисел для суммирования
    for i in range(1, limit + 1):  # Функция для расчёта суммы чисел
        if i not in exception:
            summ += i
            list_value.append(i)
    print(f'\nРезультат суммирования чисел {list_value} будет {summ}')
    print('Завершить программу или повторить попытку ввода?')
    check = True  # Флаг для цикла завершения программы
    while check:  # Цикл завершения программы
        choice = input('\nВведите "в" для выхода из программы или "п" для повтора вычислений: ').lower()
        if choice == 'п':
            print('\n===Повторный запуск===')
            print()
            input_limit()
            check = False
            break
        elif choice == 'в':
            print('Программа завершена!')
            check = False
            exit()
        else:
            print('\nВведено неверное значение! повторите попытку!')
            continue


input_limit()
