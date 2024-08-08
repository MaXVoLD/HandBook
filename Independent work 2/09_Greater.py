def great():
    try:
        value_first = int(input('Введите первое число: '))  # Запрашиваем первое целое число
        value_second = int(input('Введите второе число: '))  # Запрашиваем второе целое число
        result = value_first if value_first > value_second else value_second  # Используем тернарный оператор
        print(f'Наибольшее число {result}')  # Выводим результат
        print('Программа завершена!')
    except ValueError:
        print('Введено неверное значение, повторите попытку ввода')
        great()


great()
