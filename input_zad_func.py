import re
import base64
import os
def out_in_console(data, sorti=0):
    """
    Вывод списка книг на консоль
    """
    os.system('cls')
    if sorti == 1: # Сортировка по имени
        data.sort(key=lambda x: x['Название'])
    elif sorti == 2: # Сортировка по автору
        data.sort(key=lambda x: x['Автор'])
    count = -1
    leng = len(data)
    while True:
        try:
            count = int(input('Введите количество элементов БД(0 - все элементы): '))
        except:
            print('Неверный ввод, повторите')
            continue
        if count < leng and count >= 0:
            break
        print('Неверный ввод, повторите')

    print("{0:3}{1:20}{2:10}\n--------------------------------------------------------".format('№',
                                                                                                 'Название',
                                                                                                 'Автор',))
    for i in range(leng if count == 0 else count):
        print("{0:3}{1:20}{2:10} ".format(str(i+1), data[i]['Название'], data[i]['Автор'] ))
    return len(data)


def data_input():
    """
    Добавление новой книги в базу
    """
    while True:
        data.append({'Название': input("Введите название:"),
                     "Автор": input("Введите автора:"),
                     "Количество_страниц": input("Введите кол-во страниц:")})
        print('Проверьте правильность введения данных книги\n', data[-1])
        if input('ok?(y/n) ') != 'y':
            data.pop()
            continue
        # if input('Сохранить в библиотеку?(y/n)\n') == 'y':
        #     with open('data_base.txt', 'wb') as f:
        #         pickle.dump(data, f)
        break


def searching_data(search):
    while True:
        global data
        _searching_data = []
        for i in range(len(data)):
            if      re.search(search, data[i]['Автор']) is not None \
                    or re.search(search, data[i]['Название']) is not None:
                _searching_data.append(data[i])
                _searching_data[-1]['Позиция'] = i
        if len(_searching_data) == 0:
            print("Не найдено\nПовторить поиск?")
            if input('y/n?') == 'y':
                search = input('Введите часть названия или имени автора для поиска: ')  # Такой костыль получился,
                                                                                        # потому что не получилось
                                                                                        # организовать определение
                                                                                        # в начале функции
                continue
            else:
                return None

        return _searching_data






def main_menu(x=0):
    line = '--------------------------------------------------------\n'
    if x == 0:
        line+="1. Вывести базу данных на экран\n" \
              "2. Добавить в базу данных книгу\n" \
              "3. Удалить или редактировать книгу из базы данных\n" \
              "4. Выход\n"

    elif x == 1:
        line+='1. Сортировать по названию\n' \
              '2. Сортировать по автору\n' \
              '3. Назад'
    elif x == 3:
        line+='1. Изменить\n' \
              '2. Удалить\n' \
              '3. Назад'
    return line

def try_input_range(a, b, text='Введите пункт: '):
    """
    Функция принимает диапозон натуральных чисел и текст для ввода.
    возвращает ввод, если он сущиествует в данном диапозоне.
    :param a: Левая граница
    :param b: Правая граница
    :param text: Текст при вводе
    :return: ввод
    """
    while True:
        try:
            c = int(input(text))
        except:
            print('Некорректный ввод, повторите')
            continue
        if c <= b and c >= a:
            return c
        print('Некорректный ввод, повторите') #
