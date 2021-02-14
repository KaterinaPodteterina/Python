from itertools import cycle

new_list = input ('введите числа через пробел\n').split()
for el in cycle(new_list):
    print(el)
    key = input ('для генерации следующего числа нажмите Enter, выход по q\n')
    if key == 'q':
        break
    else:
        continue