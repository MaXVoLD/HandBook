# Задание: Написать программу, которая будет считать количество цифр в числе
try:  # Проверка
    n = str(int(input('Введите целое число: ')))  # Запрашиваем у пользователя число.Перевод в int нужен для проверки
    len_n = len(n)  # Считаем количество символов
    print(f'Введено число "{n}" \nКоличество цифр в числе: {len_n}')  # Выводим результат в консоль
except ValueError:
    print('Введено неверное значение!')