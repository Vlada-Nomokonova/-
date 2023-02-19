from roman import *

#t = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']
#print(t)
#for i in t:
#    print(i, '->' ,roman_to_int(i))

#a=[4, 58, 1994, 26, 99, 69, 80]
#for i in a:
#    print(i, '->',int_to_roman(i))

i = 'Да'
while i == 'Да' or i == 'да':
    a = int(input('Это программа для перевода чисел из абабской системы счисления в римскую и обратно. Выберите режим работы (1 - из арабских чисел в римские, 2 - из римских в арабские): '))

    while a != 1 and a != 2:
        a = int(input('Введите число соответствующее режиму работы: '))

    if a == 1:
        b = int(input('Введите количество чисел, которые хотите перевести (max = 3): '))
        if b == 1:
            c1 = int(input('Введите число: '))
            c = [c1]
            for j in c:
                print(j, '->', int_to_roman(j))
            i = input('Хотите перевести другие числа? ')
        elif b == 2:
            c1 = int(input('Введите первое число: '))
            c2 = int(input('Введите второе число: '))
            c = [c1, c2]
            for j in c:
                print(j, '->', int_to_roman(j))
            i = input('Хотите перевести другие числа? ')
        elif b == 3:
            c1 = int(input('Введите первое число: '))
            c2 = int(input('Введите второе число: '))
            c3 = int(input('Введите третье число: '))
            c = [c1, c2, c3]
            for j in c:
                print(j, '->', int_to_roman(j))
            i = input('Хотите перевести другие числа? ')
    elif a == 2:
        c = input('Введите числа которые хотите перевести (через пробел): ').split()
        for j in c:
            print(j, '->', roman_to_int(j))
        i = input('Хотите перевести другие числа? ')
