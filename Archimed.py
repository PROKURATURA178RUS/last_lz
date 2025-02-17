# Вясним при каких значениях объект плавуч, 
# не плавуч и частично плавуч в воде
#==========================================
Rh20 = 1 # Плотность воды
G = 9.8 # Ускорение свободного падения

def main():
    
    c = float(input('Введите объем погруженой части объекта:'))
    d = float(input('Введите массу объекта:'))
    e = float(input('Введите плотность объекта:'))


    def farch(p,g,v): # Функция, находящяя силу Архимеда
        return p * g * v


    def fmg(m,g): # Функция, находящаяя силу тяжести
        return m * g 
    

    fa = farch(Rh20, G, c) 
    fm = fmg(d, G)


    if fa < fm: 
        print('Объект не плавуч')
    elif fa > fm:
        print('Объект плавуч')
    elif fa == fm:
        print('Объект частично плавуч')


if __name__ == '__main__':
    main()