import Archimed as arh # Программа выясняющая плавучесть объекта
import pyramid as py # Программа считающая объем усеченной пирамиды
import life_zone as life # Программа вычисляющая средний радиус обитаемой зоны

def main():
    user_choise = input('Введите 1 если arh\nВведите 2 если py\nВведите 3 если life\nВвод:')
    if user_choise.lower() == '1':
        arh.main()
    elif user_choise.lower() == '2':
        py.main()
    elif user_choise.lower() == '3':
        life.main()
    else:
        print('Не верно')
        main()


if __name__ == '__main__':
    main()