# Задание: проверить списки на равенство между собой
# За предмет равенства принять длинну списков и их содерожимое
list_first = [1, 2, 3, 4, 5, 6]  # Первый список для сравнения
list_second = [1, 2, 4, 4, 6, 5]  # Второй список для сравнения
if len(list_first) == len(list_second):  # Cначала проверим их длинну
    for i in list_first:  # Проверяем каждый элемент из списка
        if i not in list_second:
            print('Списки не равны между собой!')
            exit()  # Команда для досрочного завершения программы при выполнении условия
    print('Списка равны между собой!')  # После успешного прохождения цикла выводим сообщение в консоль
else:
    print("Списки не равны между собой!")
