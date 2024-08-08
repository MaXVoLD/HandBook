def week():
    try:
        day = int(input('Введите число от 1 до 7: '))
        if 1 <= day <= 7:
            match day:
                case 1:
                    print('Понедельник\nПрограмма завершена!')

                case 2:
                    print('Вторник\nПрограмма завершена!')
                case 3:
                    print('Среда\nПрограмма завершена!')
                case 4:
                    print('Четверг\nПрограмма завершена!')
                case 5:
                    print('Пятница\nПрограмма завершена!')
                case 6:
                    print('Суббота\nПрограмма завершена!')
                case 7:
                    print('Воскресение\nПрограмма завершена!')
        else:
            print('Введено не верное значение!\nПовторите попытку\n')
            week()
    except ValueError:
        print('Неверный тип данных!\nПовторите попытку.\n')
        week()


week()