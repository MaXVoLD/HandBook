# Задание: Вывести второе по величине значение из списка, спомощью функции
list_sqr = [i ** 2 for i in range(1, 10)]  # Сгенерировал список значений


def second_max(list_value):  # Создал функцию, которая принимает значения из list_sqr
    list_value.sort(reverse=True)  # Отсортировал список от большего к меньшему
    return list_value[1]  # Вернул значение второго по индексу числа


print(second_max(list_sqr))
