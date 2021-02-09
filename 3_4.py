def my_func(x, y):
    x, y = float(x), int(y)
    if y >= 0 :
        return 'ошибка'
    else:
        rez = 1
        for i in range(abs(y)):
            rez = rez * 1/x
        return rez

x = input ('введите число\n')
y = input('введите целое отрицательное число\n')

print (my_func(x,y))