a = 0
b = 0
c = 0
d = 0
gross = int(input('введите выручку '))
expens = int(input('введите издержки '))
if gross>expens :
    print('прибыль')
    print(f" рентабельность {round((gross - expens) / gross,2)} %")
    numbers = int(input('введите численность сотрудников '))
    print(f" прибыль на одного сотрудника {round ((gross - expens) / numbers,2)}")
else :
    print('убыток')

