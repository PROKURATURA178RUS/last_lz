import Archimed as arh # Программа выясняющая плавучесть объекта
import pyramid as py # Программа считающая объем усеченной пирамиды


def main():
    user_choise = input('Введите 1 если arh\nВведите 2 если py\nВвод:')
    if user_choise.lower() == '1':
        arh.main()
    elif user_choise.lower() == '2':
        py.main()
    else:
        print('Не верно')
        main()


if __name__ == '__main__':
    main()