def sequence():
    try:
        value_1 = int(input('Введите первое натуральное число: '))
        value_2 = int(input('Введите второе натуральное число: '))
        value_3 = int(input('Введите третье натуральное число: '))
        list_value = sorted([value_1, value_2, value_3])
        if int(list_value[1]) - list_value[0] == list_value[2] - list_value[1]:
            print('Арифмитическая прогрессия есть! \nПрограмма завершена')
        else:
            print('Арифмитической прогрессии нет! \nПрограмма завершена')
    except ValueError:
        print('\nВведёно некорректное значение! \nПовторите попытку!\n')
        sequence()


sequence()
