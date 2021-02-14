def fact(num):
    f_num = 1
    for i in range(1, num+1):
        f_num*=i
        yield f_num
for el in fact(int(input('введите число для вычисления факториала\n'))):
    print(el)