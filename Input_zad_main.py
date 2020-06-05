"""
Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу.
Каталог должен поддерживать возможность добавления и удаления книг, редактирования информации о книге,
а также обладать персистентностью (т.е. сохранять библиотеку в внешнем файле и подгружать обратно).
Также необходимо оформить точку входа, поддерживать поиск по различным параметрам и
обеспечить интерфейс взаимодействия пользователя с библиотекой.
"""
import pickle
import base64
import os

keys = {'Up':0x48, 'Down':0x50}

with open("data_base.txt", "rb") as f:
    data = pickle.load(f)

def out_in_console():
    """
    Вывод списка книг на консоль
    """
    count = -1
    leng = len(data)
    while True:
        try:
            count = int(input('Введите количество элементов БД(0 - все элементы): '))
        except:
            print('Неверный ввод, повторите')
            continue
        if count < leng or count >= 0:
            break
        print('Неверный ввод, повторите')

    print("{0:3}{1:10}{2:10}".format('№','Название', 'Автор',))
    for i in range(leng if count == 0 else count):
        print("{0:3}{1:10}{2:10} ".format(str(i+1), data[i]['Название'], data[i]['Автор'] ))
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
        if input('Добавить в библиотеку?(y/n)\n') == 'y':
            with open('data_base.txt', 'wb') as f:
                pickle.dump(data, f)
            break



def autentification():
    """
    Авторизация в программе
    """
    while True:
        autorization = False
        login = input('Введите логин: ')
        password = input('Введите пароль: ')
        test = base64.b64encode((login + password).encode("UTF-8")).decode("UTF-8")+'\n'
        with open ('autorization_data.txt', 'r') as f:
            for item in f:

                if test == item:
                    autorization = True
        if autorization:
            os.system("cls")
            print(f"Привет, {login}")
            break
        else:
            print('Неверный логин или пароль, повторите попытку')
            continue


def main_menu():
    return "1. Вывести базу данных на экран\n" \
          "2. Добавить в базу данных книгу\n" \
          "3. Удалить книгу из базы данных\n" \
          "4. Выход\n"



def main():
    print(main_menu())
    cursor = input('Введите пункт: ')
    if cursor == '1':
        out_in_console()
    elif cursor == '2':
        pass
    elif cursor == '3':
        pass
    elif cursor == '4':
        pass



main()