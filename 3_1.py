def div_func (num_1, num_2) :
    num_1, num_2 = int (num_1), int (num_2)
    if num_2 == 0 :
        return ('Деление на 0')
    div_res = num_1/num_2
    return round(div_res, 4)

print (div_func(input ('Введите первое число\n'), input ('Введите второе число\n')))