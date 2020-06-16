"""
Дан каталог книг. Реализуйте библиотеку для хранения данных книг и поиску по каталогу.
Каталог должен поддерживать возможность добавления и удаления книг, редактирования информации о книге,
а также обладать персистентностью (т.е. сохранять библиотеку в внешнем файле и подгружать обратно).
Также необходимо оформить точку входа, поддерживать поиск по различным параметрам и
обеспечить интерфейс взаимодействия пользователя с библиотекой.
"""
import pickle
from input_zad_func import *

with open("data_base.txt", "rb") as f:
    data = pickle.load(f)


def main():
    global data
    cursor = 0
    while cursor != 4:
        print(main_menu())
        cursor = try_input_range(1, 4)
        if cursor == 1:  # Пункт 1 основного меню
            sorti = 0
            while cursor != 3:
                out_in_console(data, sorti=sorti)
                print(main_menu(x=1))
                cursor = try_input_range(1, 3)
                if cursor == 1:
                    sorti = 1
                elif cursor == 2:
                    sorti = 2
        elif cursor == 2:  # Пункт 2 основного меню
            data_input(data)
        elif cursor == 3:  # Пункт 3 основного меню
            cursor = 0
            search = input('Введите часть названия или имени автора для поиска: ')
            searching_data_ = searching_data(data, search)
            if searching_data_ is not None:
                out_in_console(searching_data_)
                edit_position = try_input_range(1, len(searching_data_)+1,
                                                text='Введите позицию книги для редактирования: ')
                x = searching_data_[edit_position - 1]
                del x['Позиция']
                os.system('cls')
                while cursor != 3:
                    print(x)
                    print(main_menu(x=3))
                    cursor = try_input_range(1,3)
                    if cursor == 1:
                        x = data[data.index(searching_data_[edit_position - 1])]

                        x_temp = x.copy()
                        temp = input(f"Введите название вместо {x['Название']}(минус - не изменять)")
                        if temp != '-':
                            x_temp['Название'] = temp
                        temp = input(f"Введите автора вместо {x['Автор']}:(минус - не изменять)")
                        if temp != '-':
                            x_temp["Автор"] = temp
                        temp = input(f"Введите кол-во страниц вместо {x['Количество_страниц']}:(минус - не изменять)")
                        if temp != '-':
                            x_temp["Количество_страниц"] = temp
                        print('Проверьте правильность введения данных книги\n', x_temp)
                        if input('ok?(y/n) ') == 'y':
                            for i in x.keys():
                                print(i)
                                x[i] = x_temp[i]

                    elif cursor == 2:
                        if input(f"Удалить {searching_data_[edit_position-1]['Название']}?(y/n)") == 'y':
                            data.remove(searching_data_[edit_position-1])
                            break
    if input('Сохранить изменения в базе?(y/n): ') == 'y':
        print("Сохранено")
        with open('data_base.txt', 'wb') as f:
            pickle.dump(data, f)
    print("До свидания!")


if __name__ == '__main__':
    main()