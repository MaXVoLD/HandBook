def equal():
    try:
        print('===Уравнение===\n Ax = B - A - 1')
        a, b = eval(input('Введите значения A и B через запятую:'))
        print(f'Ваше уравнение:\n {a}x = {b} - {a} - 1')
        result = (b - a - 1) / a
        if a == 0 and b == 1:
            print('Решением является любое число!')
        elif a == 0 and b != 1:
            print('Решений нет!')
        else:
            print(f'x = {result}')
        print('Поиск решения завершён')

    except ValueError:
        print('Введено неверное значение! Повторите попытку')
        equal()


equal()
