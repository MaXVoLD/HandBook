# Задание: Преобразовать список натуральных чисел в число
n = eval(input('Через запятую числа: '))  # Запрашиваем у пользователя число. Перевод в int нужен для проверки
swap_value = ''  # Создал пустую строку для дальнейшего хранения результата вычисления в STR
if isinstance(n, int):  # Условие при котором пользователь ввел только одно число
    print(f'Результат вычисления: {n}')
elif isinstance(n, (tuple, list)):
    for i in n:
        if isinstance(i, int):  # Проверка полученного множества
            swap_value += str(i)  # Добавляем значения в строку с результатом
        else:
            print('Введён неверный тип данных!')
    swap_value = int(swap_value)  # После отработки цикла переводим послученное число в int
    print(f'Результат вычисления: {swap_value}')  # выводим результат в консоль
else:
    print('Введён неверный тип данных!')