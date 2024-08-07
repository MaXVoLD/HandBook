from Input_value import *


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
            print('===Повторный запуск===')
            print()
            check = False
            input_limit()
            break
        elif choice == 'в':
            print('Прогрмма завершена!')
            check = False
            exit()
        else:
            print('\nВведено неверное значение! повторите попытку!')
