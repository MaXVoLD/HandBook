# Задание: Кратно ли введенное пользователем число трём
n = int(input('Введите число для проверки на кратность трём: '))
if n % 3 == 0:
    print(f'Число {n} кратно трём')
else:
    print(f'Число {n} без остатка на три не делится')
