from itertools import count

for num in count(int(input("введите начальное число\n"))):
    print(num)
    key = input ('для генерации следующего числа нажмите Enter, выход по q\n')
    if key == 'q':
        break
    else:
        continue